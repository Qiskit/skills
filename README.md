# Qiskit AI Skills

**Official, IBM-verified Agent Skills for Claude Code, IBM Bob, and other coding agents.**

[![License](https://img.shields.io/github/license/Qiskit/qiskit-ibm-runtime.svg?style=popout-square)](https://opensource.org/licenses/Apache-2.0)
[![Agent Skills Spec](https://img.shields.io/badge/Agent%20Skills-Specification-blue)](https://agentskills.io)

A collection of [Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) for assisting Qiskit-based quantum workflows.

## Installing

### Claude Code

Install using the [plugin marketplace](https://code.claude.com/docs/en/discover-plugins#add-from-github):

```
/plugin marketplace add Qiskit/skills
/plugin install qiskit-ai-skills@qiskit
```

### Codex, Cursor, and other Agent Skills–compatible agents

The skills in this repo follow the open [Agent Skills specification](https://agentskills.io), which several agent CLIs read directly. Clone the repo and point your agent at it, or copy the relevant `skills/<name>/` folder into wherever your agent looks for skills (see your agent's own docs for its exact directory and marketplace/install mechanics — this repo also ships `.codex-plugin/` and `.cursor-plugin/` manifests for tools that support plugin marketplaces).

### IBM Bob

Bob has no plugin/marketplace step — it reads `SKILL.md` files directly from `.bob/skills/` in a cloned project. This repo already symlinks `.bob/skills/<name>` back to the canonical `skills/<name>`, so cloning the repo is sufficient; Bob will pick up both skills automatically.

### Clone / Copy

Clone this repo and copy the skill folders into the appropriate directory for your agent:

| Agent | Skill Directory |
|-------|-----------------|
| Claude Code | `~/.claude/skills/` |
| Cursor | `~/.cursor/skills/` |
| IBM Bob | `.bob/skills/` (project) or `~/.bob/skills/` (global) |

## Skills

Skills are contextual and auto-loaded based on your conversation. When a request matches a skill's triggers, the agent loads and applies the relevant skill to provide accurate, grounded guidance rather than relying on general knowledge that may be outdated.

| Skill | Useful for |
|-------|------------|
| `migrate-qiskit-ibm-runtime` | Migrating qiskit-ibm-runtime code from an older release to the most recent one. Note that this doesn't currently include `backend.run()` migration. |

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add a new skill, test workload, or write-up.

## License

Apache License 2.0 — see [LICENSE.txt](LICENSE.txt).
