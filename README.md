# Qiskit AI Skills

**Official, IBM-verified Agent Skills for Claude Code, IBM Bob, and other coding agents.**

[![License](https://img.shields.io/github/license/Qiskit/skills.svg?style=popout-square)](https://opensource.org/licenses/Apache-2.0)
[![Agent Skills Spec](https://img.shields.io/badge/Agent%20Skills-Specification-blue)](https://agentskills.io)

A collection of [Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) for assisting Qiskit-based quantum workflows.

## Skills

Skills are contextual and auto-loaded based on your conversation. When a request matches a skill's triggers, the agent loads and applies the relevant skill to provide accurate, grounded guidance rather than relying on general knowledge that may be outdated.

Skills are added and improved continuously, so check back for updates. See the [Roadmap](#skills-roadmap) for what is planned next.

The currently available skills are:

| Skill | Useful for |
|-------|------------|
| `migrate-qiskit-ibm-runtime` | Migrating qiskit-ibm-runtime code from an older release to the most recent one. |

## Installation

These skills follow the [Agent Skills](https://agentskills.io/) standard and can
be installed into compatible AI coding agents using the [skills CLI](https://github.com/vercel-labs/skills), through
native agent plugin marketplaces, or by cloning the repo.

### Quick start

The easiest way to install is with the [skills CLI](https://github.com/vercel-labs/skills):

```
npx skills add Qiskit/skills
```

This will prompt you to pick which agent(s) to install for and whether to install globally or just for the current project.

**Install a specific skill:**

```
npx skills add Qiskit/skills --skill skill-to-install
```

**Keep installed skills current:**

```
npx skills update
```

### Install as a plugin

#### Claude Code

Install using the [plugin marketplace](https://code.claude.com/docs/en/discover-plugins#add-from-github):

```
/plugin marketplace add Qiskit/skills
/plugin install qiskit-ai-skills@qiskit
```

#### Codex

```
codex plugin marketplace add Qiskit/skills
codex plugin add qiskit-ai-skills@qiskit
```

#### Cursor

Install from the Cursor marketplace if available, or use the [Skills CLI](https://github.com/vercel-labs/skills) above with `--agent cursor`. See [Cursor plugins docs](https://cursor.com/docs/plugins) for more information.

#### IBM Bob

Bob has no plugin/marketplace step — it reads `SKILL.md` files directly from `.bob/skills/` in a cloned project. This repo already symlinks `.bob/skills/<name>` back to the canonical `skills/<name>`, so cloning the repo is sufficient.

You can also install with the [Skills CLI](https://github.com/vercel-labs/skills) above with `--agent bob`.

### Clone / Copy

If your agent does not support a native plugin or the skills CLI, clone this repo and copy the desired skill directory to the agent's supported skill directory:

| Agent | Skill Directory | Docs |
|-------|-----------------| ----- |
| Claude Code | `~/.claude/skills/` | [docs](https://code.claude.com/docs/en/skills)
| Codex | `~/.codex/skills/` | [docs](https://developers.openai.com/codex/skills)
| Cursor | `~/.cursor/skills/` | [docs](https://cursor.com/docs/context/skills)
| IBM Bob | `.bob/skills/` | [docs](https://bob.ibm.com/docs/ide/features/skills)

## Skills Roadmap

Disclaimer: This roadmap is intended to provide guidance and does not constitute a contractual commitment.

- ✅ `qiskit-ibm-runtime` code migration (Q3 2026)
- 🚧 Error mitigation methods accuracy/cost evaluation  (Q4 2026)
- Problem-aware layout selection (Q4 2026)
- Circuit optimization for hardware execution (2027)
- Qiskit code migration (2027)
- Performance optimization for IBM Quantum hardware execution (2027)
- Domain-specific problem mapping (2027)
- Quantum workflow planning

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add a new skill, and the [Code of Conduct](CODE_OF_CONDUCT.md) for the expectations we hold each other to.

## License

Apache License 2.0 — see [LICENSE](LICENSE.txt).
