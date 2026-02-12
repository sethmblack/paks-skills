# AI-Personas Skills for Paks

**1,443 AI skills** ready for use with Claude Code, Cursor, Copilot, and other AI coding assistants.

## Quick Install

Install any skill directly from GitHub:

```bash
# Install paks CLI
brew tap stakpak/stakpak
brew install paks

# Install a skill (replace SKILL_NAME with any skill from this repo)
paks install https://github.com/sethmblack/paks-skills/tree/main/SKILL_NAME --agent claude-code
```

**Examples:**
```bash
# Install the 10X force analysis skill
paks install https://github.com/sethmblack/paks-skills/tree/main/10x-force-analysis --agent claude-code

# Install the absurd escalation comedy skill
paks install https://github.com/sethmblack/paks-skills/tree/main/absurd-escalation --agent claude-code

# Install for Cursor instead
paks install https://github.com/sethmblack/paks-skills/tree/main/10x-force-analysis --agent cursor
```

## What is Paks?

Paks is a skill package manager for AI coding assistants. Think of it like npm for AI skills - install reusable capabilities across Claude Code, Cursor, Copilot, and more.

## Browse Skills

See [INDEX.md](INDEX.md) for the complete list of 1,443 skills organized by category.

**Skill Categories:**
- Business & Strategy (10X forces, competitive analysis, etc.)
- Comedy & Creative Writing (absurdist comedy, character voices, etc.)
- Philosophy & Thinking (stoic practices, analytical frameworks, etc.)
- Technical & Engineering (code review, architecture, etc.)
- And many more...

## Skill Format

Each skill folder contains a `SKILL.md` file with:

```yaml
---
name: skill-name
description: What the skill does and when to use it
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
  - keyword1
  - keyword2
---

# Skill content and instructions...
```

## Managing Installed Skills

```bash
# List installed skills
paks list --agent claude-code

# Remove a skill
paks remove skill-name --agent claude-code

# List all skills across all agents
paks list --all
```

## Supported AI Agents

| Agent | Install Flag |
|-------|--------------|
| Claude Code | `--agent claude-code` |
| Cursor | `--agent cursor` |
| VS Code | `--agent vscode` |
| GitHub Copilot | `--agent copilot` |
| Goose | `--agent goose` |
| OpenCode | `--agent opencode` |

## Contributing

Want to add or improve skills? PRs welcome!

## License

MIT License - See individual skills for specific licensing.
