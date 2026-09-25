# Qiskit AI Skills

**Official, IBM-verified Agent Skills for Claude Code, IBM Bob, and other coding agents.**

[![License](https://img.shields.io/github/license/Qiskit/skills.svg?style=popout-square)](https://opensource.org/licenses/Apache-2.0)
[![Agent Skills Spec](https://img.shields.io/badge/Agent%20Skills-Specification-blue)](https://agentskills.io)

A collection of [Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) for assisting Qiskit-based quantum workflows.

## Skills

Skills are contextual and auto-loaded based on your conversation. When a request matches a skill's triggers, the agent loads and applies the relevant skill to provide accurate, grounded guidance rather than relying on general knowledge that may be outdated.

| Skill | Useful for |
|-------|------------|
| `migrate-qiskit-ibm-runtime` | Migrating `qiskit-ibm-runtime` code from an older release to the most recent one. Note that this doesn't currently include `backend.run()` migration. |

## Installing

### Claude Code

Install using the [plugin marketplace](https://code.claude.com/docs/en/discover-plugins#add-from-github):

```
/plugin marketplace add Qiskit/skills
/plugin install qiskit-ai-skills@qiskit-ai-skills
```

### Codex, Cursor, and other Agent Skills–compatible agents

The skills in this repo follow the open [Agent Skills specification](https://agentskills.io), which several agent CLIs read directly.

Both Codex and Cursor discover skills under `.agents/skills/`, and this repo symlinks `.agents/skills/<name>` back to the canonical `skills/<name>`. Cloning the repo and working inside it is therefore enough for those agents to pick the skills up; to make them available everywhere, copy the skill folder into your user-level skills directory instead (see [Clone / copy](#clone--copy)).

This repo also ships `.cursor-plugin/` and `.codex-plugin/` manifests for those tools' plugin/marketplace flows — see your agent's own docs for its install mechanics.

### IBM Bob

Bob has no plugin/marketplace step — it reads `SKILL.md` files directly from `.bob/skills/` in a cloned project. This repo already symlinks `.bob/skills/<name>` back to the canonical `skills/<name>`, so cloning the repo is sufficient; Bob will pick the skills up automatically.

### Clone / copy

Clone this repo and copy the `skills/<name>/` folders you want into the appropriate directory for your agent:

| Agent | Skill directory |
|-------|-----------------|
| Claude Code | `~/.claude/skills/` (global) or `.claude/skills/` (project) |
| Codex | `~/.agents/skills/` (global) or `.agents/skills/` (project) |
| Cursor | `~/.cursor/skills/` or `~/.agents/skills/` (global); `.cursor/skills/` or `.agents/skills/` (project) |
| IBM Bob | `~/.bob/skills/` (global) or `.bob/skills/` (project) |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add a new skill, and the [Code of Conduct](CODE_OF_CONDUCT.md) for the expectations we hold each other to.

## License

Apache License 2.0 — see [LICENSE](LICENSE.txt).
