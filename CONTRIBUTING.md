# Contributing

This repo collects skills, commands, and other agent-harness artifacts for
quantum-computing research workflows, along with the test workloads and run
transcripts used to evaluate them, and notes on what works.

## Before you start

If you are new to Qiskit contributing we recommend you do the following before diving into the code:

* Read the [Code of Conduct](https://github.com/Qiskit/qiskit/blob/main/CODE_OF_CONDUCT.md)
* Familiarize yourself with the Qiskit community (via [Slack](https://qisk.it/join-slack),
   [Stack Exchange](https://quantumcomputing.stackexchange.com), [GitHub](https://github.com/qiskit-community/feedback/discussions) etc.)

## Issues and pull requests

We use [GitHub pull requests](https://help.github.com/articles/about-pull-requests) to accept
contributions.

While not required, opening a new issue about the bug you're fixing or the
feature you're working on before you open a pull request is an important step
in starting a discussion with the community about your work. The issue gives us
a place to talk about the idea and how we can work together to implement it in
the code. It also lets the community know what you're working on, and if you
need help, you can reference the issue when discussing it with other community
and team members.

For documentation issues relating to pages in the guides, tutorials, and migration guides sections of [quantum.cloud.ibm.com](https://quantum.cloud.ibm.com/docs/), please open an issue in the [Qiskit/documentation repo](https://github.com/Qiskit/documentation/issues/new/choose).

If you've written some code but need help finishing it, want to get initial
feedback on it prior to finishing it, or want to share it and discuss prior
to finishing the implementation, you can open a *Draft* pull request and prepend
the title with the **\[WIP\]** tag (for Work In Progress). This will indicate
to reviewers that the code in the PR isn't in its final state and will change.
It also means that we will not merge the commit until it is finished. You or a
reviewer can remove the [WIP] tag when the code is ready to be fully reviewed for merging.


## Code review

All code merged to Qiskit, even from maintainers, goes through a code-review
process after a pull request is made.  There are a small number of
maintainers who can authorize a final merge, but code review involves everyone
working together to make Qiskit better.  You can review code even if you
are not a maintainer, which helps make sure pull requests are technically
correct, well tested, and easier to tackle in their final maintainer review.

The code-review process is a normal part of software development, and nothing to
be scared of; for very easy changes it can be as simple as a maintainer saying
"looks good to me!" (or in short, "LGTM!") and merging the PR.  For more complex changes, it's often a
back-and-forth where the reviewer may ask a couple of questions about why things
were done a particular way, and make suggestions for improvement.  You don't
need to do everything suggested if you've got good reasons to disagree, but
communicate that clearly and politely.

If you're struggling with code review or a PR on Qiskit, you can ask for help in
the `#qiskit-pr-help` channel on [the public Qiskit Slack](https://qisk.it/join-slack).

Remember that the PR author is a human, not just a username!  It's OK to ask
questions about the code, but don't be mean or rude about it even if you don't
like it.  It's also fine to provide comments that are just compliments with no
suggested changes, if you particularly like something!

Qiskit maintainers may close any pull request if the review effort is expected to outweigh the benefit
to the project, even with no proposed alternative. This is a subjective decision made by maintainers.


## Contributor Licensing Agreement

Before you can submit any code, all contributors must sign a
contributor license agreement (CLA). By signing a CLA, you're attesting
that you are the author of the contribution, and that you're freely
contributing it under the terms of the Apache-2.0 license.

When you contribute to the Qiskit project with a new pull request,
a bot will evaluate whether you have signed the CLA. If required, the
bot will comment on the pull request, including a link to accept the
agreement. The [individual CLA](https://qisk.it/cla)
document is available for review as a PDF.

Note: If your contribution is part of your employment or your contribution
is the property of your employer, then you will more than likely need to sign a
[corporate CLA](https://qisk.it/corporate-cla) too and
email it to us at <qiskit@us.ibm.com>.


## Adding a skill

Skills live under `skills/<skill-name>/SKILL.md`. Follow the same style as the existing ones for consistency.

If the skill needs supporting reference files (data the skill reads but that
shouldn't be independently invocable), put them alongside `SKILL.md` in the
same directory, as plain files — not as nested commands.

If the skill's job is to select from among several structured options (a
decision-matrix problem, like picking an error mitigation strategy), consider
the registry + capability-page pattern.

## Testing

Once you've made a code change, it is important to verify that your change
does not break any existing tests and that any new tests that you've added
also run successfully. Before you open a new pull request for your change,
you'll want to make sure the changes you made are well tested and be able
to show proof of that in the PR.
