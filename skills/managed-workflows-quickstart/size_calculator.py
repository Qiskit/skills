# This code is part of a Qiskit project.
#
# (C) Copyright IBM 2026.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Pick the ``function_size`` a problem needs: before submitting, and again inside the job.

Copy this file into the function folder next to ``entrypoint.py``. The same file then works
in two places:

- **Client side, before submitting.** Standard library only, with no ``qiskit-serverless``
  needed::

      from size_calculator import calculate_function_size

      size = calculate_function_size(**args)          # "s", "m", "l" or "xl"
      job = fn.run(function_size=size, **args)

- **Inside the job.** Call this once, at the start of ``run_function``, with the arguments the
  job runs::

      from size_calculator import validate_size

      validate_size(**args)

  It reads the size the job was given (``get_function_size()``) and compares it with the
  size calculated for the problem:
    - **too small:** raises, so the job stops before it runs out of memory;
    - **larger than needed:** logs a warning and records an event in ``job.events()``, then
      continues;
    - **equal:** continues.

The cutoffs come from **measured runs**, not from the formula alone. The block below takes:
    - ``MEMORY_GB``, copied from ``scale_probe.py``;
    - ``FIT``, the ``fit`` entry in ``scale_probe.json`` written by the last
      ``mw_sweep.py fit``, ``sweep`` or ``climb``;
    - ``SIZES``, the memory of each profile in ``sizes_map`` (from ``compute_profiles()``).

``python size_calculator.py [runs.json]`` checks the calculator before you ship it. For every
measured run it confirms that the calculated size's machine had at least the memory the run
used, and it prints the size each tier in ``scale_probe.py`` maps to.

Re-fill the block, and re-upload, whenever ``sizes_map`` or the fit changes. The copy inside
the function is the one ``validate_size`` uses.
"""

import json
import os
import sys

# ============================ EDIT THIS BLOCK ============================


def MEMORY_GB(p):  # pylint: disable=invalid-name
    """EDIT: the same formula as ``MEMORY_GB`` in scale_probe.py, unchanged."""
    return p["workers"] * 8 * (p["n"] ** 2 + p["n_vectors"] * p["n"]) / 1e9


FIT = {"base": 0.5, "k": 1.0}  # EDIT: scale_probe.json -> "fit" (peak = base + k * formula)
HEADROOM = 1.3  # the same headroom scale_probe.py picks machines with
SIZES = {  # EDIT: label -> memory (GB) of the profile it maps to in sizes_map
    "s": 32,
    "m": 128,
    "l": 768,
}
DEFAULTS = {}  # EDIT: defaults of the researcher's function for arguments MEMORY_GB reads
FILLED = False  # EDIT: set True once FIT and SIZES come from measured runs; until then the
# in-job check only logs, so the sweep and climb jobs of Step 4 are never stopped by it

# ========================= machinery below this line =========================

VALID_LABELS = ("s", "m", "l", "xl")


def _labels():
    labels = sorted(SIZES, key=lambda label: SIZES[label])
    bad = [label for label in labels if label not in VALID_LABELS]
    if bad:
        raise ValueError(f"size_calculator: labels must be s, m, l or xl, got {bad}")
    return labels


def needed_gb(**args):
    """Memory the problem needs at its peak, with headroom: (base + k * formula) * HEADROOM."""
    problem = {**DEFAULTS, **args}
    try:
        formula = MEMORY_GB(problem)
    except KeyError as exc:
        raise ValueError(
            f"size_calculator: cannot size this problem, missing argument {exc}; "
            "pass it or add its default to DEFAULTS"
        ) from None
    return (FIT["base"] + FIT["k"] * formula) * HEADROOM


def calculate_function_size(**args):
    """Return the smallest size label whose machine has the memory this problem needs.

    A problem past the largest size returns the largest label with a warning: estimates that
    far out are often high, so trying it there is the next step (see SKILL.md, Step 4).
    """
    need = needed_gb(**args)
    labels = _labels()
    for label in labels:
        if SIZES[label] >= need:
            return label
    largest = labels[-1]
    print(
        f"size_calculator: this problem needs ~{need:.3g} GB, more than '{largest}' "
        f"({SIZES[largest]} GB), the largest size measured; trying '{largest}'.",
        file=sys.stderr,
    )
    return largest


def validate_size(**args):
    """Call once at the start of ``run_function``. Raise if the job's size is too small."""
    from qiskit_serverless import (  # pylint: disable=import-outside-toplevel
        ServerlessError,
        get_function_size,
        send_error,
    )

    if not FILLED:
        print("size_calculator: not filled in yet (FILLED = False); skipping the size check.", flush=True)
        return
    given = (get_function_size() or "").lower()
    if not given:
        print("size_calculator: no function size on this job; skipping the size check.", flush=True)
        return
    need = needed_gb(**args)
    expected = calculate_function_size(**args)
    order = _labels()
    print(
        f"size_calculator: size given '{given}', calculated '{expected}' (~{need:.3g} GB).",
        flush=True,
    )
    if given not in order:
        print(f"size_calculator: '{given}' is not in SIZES; skipping the size check.", flush=True)
        return
    if order.index(given) < order.index(expected):
        raise ServerlessError(
            code="FunctionSizeTooSmall",
            message=(
                f"Size '{given}' ({SIZES[given]} GB) is too small for this problem, which needs "
                f"~{need:.3g} GB. Resubmit with function_size='{expected}'."
            )
        )
    if order.index(given) > order.index(expected):
        print(
            f"size_calculator: size '{given}' is larger than this problem needs; '{expected}' "
            "would do.",
            flush=True,
        )
        send_error(
            code="FunctionSizeTooLarge",
            message="The function size is larger than this job needs.",
            exception="FunctionSizeTooLarge",
            args={"provided_size": given, "calculated_size": expected, "needed_gb": round(need, 3)},
        )


def self_check(runs_file):
    """Check the calculator against measured runs and print the size of every tier."""
    ok = True
    if os.path.exists(runs_file):
        with open(runs_file, encoding="utf-8") as handle:
            runs = json.load(handle)
        for run in runs:
            peak = (run.get("resources") or {}).get("peak_gb")
            if peak is None or run.get("where") == "local":
                continue
            label = calculate_function_size(**run["problem"])
            fits = SIZES[label] >= peak
            ok &= fits
            print(
                f"{'ok ' if fits else 'BAD'} {run.get('job_id', '-'):<38} measured {peak:.3g} GB -> "
                f"'{label}' ({SIZES[label]} GB)"
            )
    else:
        print(f"no {runs_file}: nothing measured to check against")
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        sys.path.insert(0, here)
        from scale_probe import TIERS  # pylint: disable=import-outside-toplevel

        for tier, problem in TIERS.items():
            print(
                f"tier {tier}: ~{needed_gb(**problem):.3g} GB -> "
                f"'{calculate_function_size(**problem)}'"
            )
    except ImportError:
        pass
    if not ok:
        sys.exit(
            "size_calculator: a measured run needed more than the size it maps to. Refit "
            "(mw_sweep.py fit) and update FIT before shipping."
        )


if __name__ == "__main__":
    self_check(sys.argv[1] if len(sys.argv) > 1 else "runs.json")
