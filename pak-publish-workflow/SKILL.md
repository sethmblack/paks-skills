---
name: pak-publish-workflow
description: Complete workflow for validating and publishing skills to the PAK registry at paks.stakpak.dev
license: MIT
metadata:
  version: 1.0.2365
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- pak
- publishing
- skills
- workflow
---

# PAK Publish Workflow

Complete workflow for validating and publishing skills to the PAK registry at paks.stakpak.dev.

---

## Constitutional Constraints

- **Validate before publish** - Never publish a skill without running `paks validate` first
- **Quote YAML safely** - Any description containing colons (`:`) must be wrapped in double quotes
- **Commit before publish** - All changes must be committed to git before publishing
- **One skill at a time** - Verify each skill publishes successfully before moving to the next

---

## When to Use

- Publishing new skills to the PAK registry
- Batch publishing multiple skills
- Troubleshooting validation failures
- Setting up the paks CLI for the first time

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| skill_directory | Yes | Path to the skill directory containing SKILL.md |
| batch | No | List of skill directories for batch publishing |

---

## Workflow

### Step 1: Install PAK CLI

**First-time setup only.**

```bash
# macOS/Linux via Homebrew
brew tap stakpak/stakpak
brew install paks

# Verify installation
paks --version
```

---

### Step 2: Validate Skill

**Before publishing, ensure the skill passes validation.**

```bash
cd /path/to/skill-directory
paks validate .
```

**Common Validation Errors:**

| Error | Cause | Fix |
|-------|-------|-----|
| `Failed to parse SKILL.md frontmatter as YAML` | Colon in description | Wrap description in double quotes |
| `name field missing` | Missing required field | Add `name: skill-name` to frontmatter |
| `description is very short` | Warning only | Expand description (not required) |

**Fix: Colon in Description**

❌ Invalid:
```yaml
description: Analyze this: and that
```

✅ Valid:
```yaml
description: "Analyze this - and that"
```

---

### Step 3: Commit Changes

**Skills must be committed before publishing.**

```bash
git add skill-directory/
git commit -m "Add skill-name skill"
git push origin main
```

---

### Step 4: Publish to Registry

**Single skill:**
```bash
paks publish skill-directory -y
```

**Batch publish:**
```bash
for skill in skill1 skill2 skill3; do
  echo "Publishing $skill..."
  paks publish "$skill" -y
done
```

**Publish persona bundles:**
```bash
for bundle in persona-bundles/*/; do
  paks publish "$bundle" -y
done
```

---

### Step 5: Verify Publication

```bash
# Search for your skill
paks search skill-name

# View skill details
paks info owner/skill-name

# Test installation
paks install owner/skill-name
```

**Browse at:** https://paks.stakpak.dev

---

## Output Format

```markdown
## PAK Publish Report

### Skills Published

| Skill | Version | Status |
|-------|---------|--------|
| walkability-audit | v1.0.2305 | ✅ Published |
| induced-demand-analysis | v1.0.2306 | ✅ Published |

### Validation Issues Fixed

| Skill | Issue | Fix Applied |
|-------|-------|-------------|
| walkability-audit | Colon in description | Quoted description |

### Verification

- Registry search: `paks search urban-planning` ✅
- Install test: `paks install owner/skill` ✅
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Validation fails | Check frontmatter YAML; look for unquoted colons |
| "not a terminal" error | Use `-y` flag to skip interactive prompts |
| "Uncommitted changes" warning | Commit and push before publishing |
| Version mismatch | Tool auto-syncs; no action needed |
| Network error | Retry; check internet connection |

---

## Example

**Input:** Publish all urban planner skills to PAK

**Execution:**

1. **Validate all skills:**
```bash
cd /Users/ziggs/Documents/InfiniteBackroom/paks-skills

for skill in walkability-audit induced-demand-analysis brt-system-design; do
  if paks validate "$skill" > /dev/null 2>&1; then
    echo "✓ $skill valid"
  else
    echo "✗ $skill INVALID"
  fi
done
```

2. **Fix any validation errors:**
```bash
# If description has colon, edit SKILL.md:
# Change: description: Text with: colon
# To:     description: "Text with - colon"
```

3. **Commit fixes:**
```bash
git add .
git commit -m "Fix YAML frontmatter for PAK validation"
git push origin main
```

4. **Publish all:**
```bash
for skill in walkability-audit induced-demand-analysis brt-system-design; do
  paks publish "$skill" -y
done
```

5. **Verify:**
```bash
paks search walkability
# Output: sethmblack/walkability-audit
```

---

## Quick Reference

| Command | Description |
|---------|-------------|
| `paks validate <dir>` | Check skill is valid |
| `paks publish <dir> -y` | Publish with auto-confirm |
| `paks publish <dir> --dry-run` | Preview what would happen |
| `paks search <keyword>` | Search registry |
| `paks info <owner>/<skill>` | View skill details |
| `paks install <owner>/<skill>` | Install a skill |
| `paks list` | List installed skills |

---

## Integration

This skill pairs well with:
- **skill-creation** - Create new skills before publishing
- **yaml-validation** - Catch frontmatter issues early