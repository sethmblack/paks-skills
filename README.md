# AI-Personas Skills for Paks

This directory contains AI-Personas skills converted to Paks format for publishing on [paks.stakpak.dev](https://paks.stakpak.dev/).

## What is Paks?

Paks is a skill package manager for AI coding assistants (Claude Code, Cursor, Copilot, etc.). It allows developers to discover, install, and share reusable AI skills across different tools and platforms.

Think of it like npm for AI assistant skills - you can publish your skills to paks.stakpak.dev and others can install them with a simple command.

## Paks Format Requirements

Every skill package in Paks must follow this structure:

```
skill-name/
├── SKILL.md (required)        # Main skill file with YAML frontmatter
├── scripts/ (optional)        # Executable code for deterministic tasks
├── references/ (optional)     # Documentation loaded as needed
└── assets/ (optional)         # Templates and files used in outputs
```

### SKILL.md Format

The `SKILL.md` file must contain YAML frontmatter with these fields:

```yaml
---
name: skill-name              # Required: kebab-case identifier
description: Brief description # Required: What the skill does and when to use it
version: 1.0.0               # Semantic versioning
author: Author Name          # Who created this skill
tags: [tag1, tag2, tag3]    # Related keywords for discovery
---

# Rest of the skill documentation
```

**Important:**
- `name` and `description` are **required** fields
- The description is the primary triggering mechanism - it helps Claude understand when to use the skill
- Use kebab-case for skill names (e.g., `absurd-escalation`)
- Version should follow semantic versioning (e.g., `1.0.0`)

## Converted Skills

Currently converted skills (proof of concept):

| Skill | Description | Tags |
|-------|-------------|------|
| **absurd-escalation** | Take mundane observations and escalate through logical progression to delightful absurdity | absurdist, comedy, hedberg, escalation |
| **callback-architecture** | Transform linear narratives into structured stories with planted details that pay off | callbacks, comedy, mulaney, storytelling |
| **deadpan-authority** | Deliver absurd content with unwavering authoritative composure | deadpan, comedy, chapman, authority |
| **literalist-reframe** | Take idioms and expressions at face value to expose hidden absurdities | wordplay, comedy, hedberg, literalism |
| **one-liner-compression** | Compress observations into minimal form while maintaining maximum comedic impact | compression, comedy, hedberg, minimalism |

## How to Use the Converter

### Convert a Single Skill

```bash
cd /Users/ziggs/Documents/InfiniteBackroom/PromptLibrary/working-ai-personas-book/scripts

python3 convert-to-paks.py /path/to/AI-Personas/skills/skill-name
```

### Convert Multiple Skills (Batch Mode)

```bash
# Convert specific skills
python3 convert-to-paks.py --batch /path/to/AI-Personas/skills \
  --skills absurd-escalation deadpan-authority literalist-reframe

# Convert all skills in a directory
python3 convert-to-paks.py --batch /path/to/AI-Personas/skills
```

### Custom Options

```bash
# Specify custom output directory
python3 convert-to-paks.py /path/to/skill --output /custom/output

# Specify custom author name
python3 convert-to-paks.py /path/to/skill --author "Your Name"

# Combine options
python3 convert-to-paks.py --batch /path/to/skills \
  --skills skill1 skill2 \
  --output /custom/output \
  --author "Your Name"
```

### Get Help

```bash
python3 convert-to-paks.py --help
```

## How the Converter Works

The `convert-to-paks.py` script performs these steps:

1. **Read PROMPT.md** - Reads the original AI-Personas skill file
2. **Extract metadata** - Pulls title from first `# heading` and description from first paragraph
3. **Generate tags** - Analyzes content for comedy techniques, frameworks, and keywords
4. **Create YAML frontmatter** - Generates proper Paks-compliant metadata
5. **Output SKILL.md** - Writes the converted file to `paks-ready/{skill-name}/SKILL.md`

### What Gets Converted

- **Title** → `name` (converted to kebab-case from directory name)
- **First paragraph** → `description`
- **Content analysis** → `tags` (auto-generated)
- **Full PROMPT.md** → Body of SKILL.md (preserved as-is)
- **Version** → `1.0.0` (initial version)
- **Author** → `AI-Personas` (or custom via `--author`)

### What Stays the Same

The converter preserves all the original skill content:
- Constitutional Constraints
- When to Use sections
- Inputs/Outputs
- Workflow steps
- Examples
- Error handling

This ensures the skill works exactly the same way in Paks as in AI-Personas.

## How to Publish Skills to Paks

### Prerequisites

1. Create an account on [paks.stakpak.dev](https://paks.stakpak.dev/)
2. Install the Paks CLI (follow instructions on the website)
3. Authenticate with your account

### Publishing Steps

1. **Prepare your skill** - Ensure SKILL.md has proper YAML frontmatter
2. **Test locally** - Verify the skill works as expected
3. **Initialize package** - Run `pak init` in your skill directory
4. **Publish** - Run `pak publish` to upload to paks.stakpak.dev
5. **Version updates** - Increment version number and republish for updates

### Publishing Checklist

- [ ] SKILL.md exists with complete YAML frontmatter
- [ ] `name` and `description` fields are filled
- [ ] Version follows semantic versioning (1.0.0)
- [ ] Tags are relevant and helpful for discovery
- [ ] Skill has been tested and works correctly
- [ ] Any optional directories (scripts/, references/, assets/) are included if needed

## Current Status

**Conversion Progress:**
- ✅ Converter script created and tested
- ✅ 5 sample skills converted successfully
- ✅ Directory structure established
- ⏳ Ready for publishing (pending Paks account setup)

**Next Steps:**
1. Test converted skills in Claude Code
2. Set up Paks publisher account
3. Publish initial 5 skills to paks.stakpak.dev
4. Convert additional comedy-related skills
5. Expand to other skill categories (business, writing, analysis, etc.)

## Source Files

All skills are converted from the AI-Personas repository:

```
/Users/ziggs/Documents/InfiniteBackroom/Demo2/AI-Personas/skills/
```

Original format: `{skill-name}/PROMPT.md`

## Directory Structure

```
paks-ready/
├── README.md (this file)
├── absurd-escalation/
│   └── SKILL.md
├── callback-architecture/
│   └── SKILL.md
├── deadpan-authority/
│   └── SKILL.md
├── literalist-reframe/
│   └── SKILL.md
└── one-liner-compression/
    └── SKILL.md
```

## Contributing

To add more skills to this collection:

1. Identify skills from AI-Personas that would be useful to the wider community
2. Run the converter script on those skills
3. Review the generated SKILL.md for accuracy
4. Test the skill in your AI assistant
5. Submit for publishing

### Recommended Skills for Conversion

**Comedy & Writing:**
- observational-comedy-breakdown
- callback-setup
- comic-deflation
- comedy-pathos-balance

**Business & Communication:**
- stakeholder-analysis
- decision-framework
- clarity-filter
- executive-summary

**Analysis & Research:**
- pattern-recognition
- root-cause-analysis
- scenario-planning
- competitive-analysis

## Support

For issues with:
- **The converter script** - Check the script source code or file an issue
- **Paks platform** - Visit [paks.stakpak.dev](https://paks.stakpak.dev/) documentation
- **Original AI-Personas skills** - Visit the [AI-Personas repository](https://github.com/sethmblack/AI-Personas)

## License

These skills are part of the AI-Personas project. Check the original repository for license information.

## Resources

- **Paks Website:** https://paks.stakpak.dev/
- **AI-Personas Repository:** https://github.com/sethmblack/AI-Personas
- **Converter Script:** `../scripts/convert-to-paks.py`

---

**Last Updated:** 2026-02-11
**Conversion Tool Version:** 1.0.0
**Total Skills Converted:** 5
