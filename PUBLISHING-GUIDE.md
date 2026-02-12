# Paks Publishing Guide

Quick reference for publishing AI-Personas skills to paks.stakpak.dev.

## Pre-Publishing Checklist

Before publishing any skill, verify:

- [ ] SKILL.md exists with complete YAML frontmatter
- [ ] `name` field is kebab-case and matches directory name
- [ ] `description` field clearly explains when to use the skill
- [ ] `version` follows semantic versioning (start with 1.0.0)
- [ ] `author` field is set (default: AI-Personas)
- [ ] `tags` are relevant for discovery (max 8 recommended)
- [ ] Original skill content is fully preserved
- [ ] No sensitive information or credentials in the skill
- [ ] Skill has been tested locally

## YAML Frontmatter Reference

```yaml
---
name: skill-name              # Required: kebab-case, matches directory
description: Brief description # Required: When to use this skill
version: 1.0.0               # Required: Semantic versioning
author: AI-Personas          # Required: Creator name
tags: [tag1, tag2]          # Optional: For discovery (max 8)
---
```

### Required Fields

1. **name** - The skill identifier
   - Must be kebab-case (lowercase with hyphens)
   - Should match the directory name
   - Example: `absurd-escalation`, `callback-architecture`

2. **description** - What the skill does and when to use it
   - This is the PRIMARY TRIGGERING MECHANISM
   - Helps Claude understand when to invoke the skill
   - Should be 1-2 sentences, clear and specific
   - Example: "Take mundane observations and follow their internal logic to increasingly absurd but technically plausible conclusions."

### Optional Fields

3. **version** - Semantic versioning
   - Start with `1.0.0` for new skills
   - Increment for updates:
     - Major (1.x.x): Breaking changes
     - Minor (x.1.x): New features, backward compatible
     - Patch (x.x.1): Bug fixes

4. **author** - Creator or organization name
   - Default: `AI-Personas`
   - Can be individual name or organization

5. **tags** - Keywords for discovery
   - Max 8 tags recommended
   - Use existing tags when possible
   - Examples: `comedy`, `writing`, `storytelling`, `analysis`

## Publishing Process

### 1. Setup Paks CLI

```bash
# Install Paks CLI (follow current instructions from paks.stakpak.dev)
# Authenticate with your account
pak login
```

### 2. Navigate to Skill Directory

```bash
cd /Users/ziggs/Documents/InfiniteBackroom/PromptLibrary/working-ai-personas-book/paks-ready/skill-name
```

### 3. Initialize Package (First Time Only)

```bash
pak init
```

This creates package metadata and prepares for publishing.

### 4. Test Locally

Before publishing, test the skill:

```bash
# Copy to your local Claude Code skills directory
# Test in real scenarios
# Verify all examples work
```

### 5. Publish to Paks

```bash
pak publish
```

The skill will be uploaded to paks.stakpak.dev and become available to all users.

### 6. Verify Publication

Visit your skill page on paks.stakpak.dev:

```
https://paks.stakpak.dev/skills/your-publisher-name/skill-name
```

## Updating Published Skills

### Version Increment Rules

**Patch Update (1.0.X)** - Bug fixes, typo corrections
```bash
# Update version in SKILL.md
version: 1.0.1  # was 1.0.0

# Publish update
pak publish
```

**Minor Update (1.X.0)** - New features, additional examples, backward compatible
```bash
# Update version in SKILL.md
version: 1.1.0  # was 1.0.1

# Publish update
pak publish
```

**Major Update (X.0.0)** - Breaking changes, complete restructure
```bash
# Update version in SKILL.md
version: 2.0.0  # was 1.1.0

# Publish update
pak publish
```

## Publishing Strategy for AI-Personas Skills

### Phase 1: Comedy Skills (CURRENT)

Start with well-tested comedy skills:

1. ✅ absurd-escalation
2. ✅ callback-architecture
3. ✅ deadpan-authority
4. ✅ literalist-reframe
5. ✅ one-liner-compression

Next batch:
- observational-comedy-breakdown
- callback-setup
- comic-deflation
- comedy-pathos-balance
- clean-comedy-transformation

### Phase 2: Writing & Communication

- clarity-filter
- executive-summary
- technical-translation
- audience-adaptation

### Phase 3: Business & Analysis

- stakeholder-analysis
- decision-framework
- root-cause-analysis
- scenario-planning
- competitive-analysis

### Phase 4: Specialized Domains

- Expert-specific skills
- Industry-specific frameworks
- Niche methodologies

## Batch Publishing Workflow

To convert and publish multiple skills efficiently:

```bash
# 1. Convert batch of skills
cd /Users/ziggs/Documents/InfiniteBackroom/PromptLibrary/working-ai-personas-book/scripts

python3 convert-to-paks.py --batch /path/to/AI-Personas/skills \
  --skills skill1 skill2 skill3 skill4 skill5

# 2. Review each converted skill
cd ../paks-ready

# Check each SKILL.md
for skill in skill1 skill2 skill3 skill4 skill5; do
  head -10 $skill/SKILL.md
  echo "---"
done

# 3. Test skills locally (manual step)

# 4. Publish each skill
for skill in skill1 skill2 skill3 skill4 skill5; do
  cd $skill
  pak init
  pak publish
  cd ..
done
```

## Common Issues & Solutions

### Issue: Description Too Generic

❌ Bad: "A skill for comedy"
✅ Good: "Take mundane observations and escalate through logical progression to delightful absurdity"

The description should explain WHEN and WHY to use the skill.

### Issue: Tags Not Helping Discovery

❌ Bad: `[skill, ai, helper, tool]` (too generic)
✅ Good: `[comedy, hedberg, observational, absurdist]` (specific)

Use tags that users would actually search for.

### Issue: Version Confusion

Start with `1.0.0` and follow semantic versioning:
- `1.0.0` → First publication
- `1.0.1` → Fixed typo in examples
- `1.1.0` → Added new technique section
- `2.0.0` → Complete restructure of workflow

### Issue: Name Conflicts

If skill name is taken, try:
- Add context: `hedberg-absurd-escalation`
- Add domain: `comedy-absurd-escalation`
- Use full phrase: `absurd-logical-escalation`

## Quality Standards

Before publishing, ensure:

### Content Quality
- [ ] All sections are complete and clear
- [ ] Examples are comprehensive and tested
- [ ] Error handling is documented
- [ ] Constitutional constraints are ethical and clear

### Technical Quality
- [ ] YAML frontmatter is valid
- [ ] All required fields present
- [ ] Markdown formatting is clean
- [ ] No broken links or references

### User Experience
- [ ] Description clearly explains trigger conditions
- [ ] Workflow steps are actionable
- [ ] Examples show realistic usage
- [ ] Error messages are helpful

## Maintenance

### Regular Reviews

- Review published skills quarterly
- Check for user feedback
- Update examples with new use cases
- Improve descriptions based on actual usage

### Deprecation

If a skill needs to be deprecated:

1. Mark as deprecated in description
2. Publish final version with deprecation notice
3. Point users to replacement skill
4. Keep available for 6 months before removal

## Analytics & Feedback

After publishing, monitor:

- **Download count** - How many users are finding the skill
- **User feedback** - Comments and ratings
- **Usage patterns** - When and how it's being used
- **Error reports** - Issues users encounter

Use this data to:
- Improve descriptions
- Add missing examples
- Clarify confusing sections
- Create complementary skills

## Resources

- **Paks Platform:** https://paks.stakpak.dev/
- **Semantic Versioning:** https://semver.org/
- **Converter Script:** `../scripts/convert-to-paks.py`
- **AI-Personas Source:** `/Users/ziggs/Documents/InfiniteBackroom/Demo2/AI-Personas/skills/`

---

**Last Updated:** 2026-02-11
**Current Phase:** Phase 1 - Comedy Skills
**Skills Published:** 0 (ready to publish: 5)
