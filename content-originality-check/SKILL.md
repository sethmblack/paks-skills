---
name: content-originality-check
description: Verify that expert content is original, properly attributed, and does not infringe on copyrights. Ensures quotes are attributed, extended passages don't exceed fair use, and content is transformati...
license: MIT
metadata:
  version: 1.0.3673
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- content-originality-check
- transformation
- writing
---

# Content Originality Check

Verify that expert content is original, properly attributed, and does not infringe on copyrights. Ensures quotes are attributed, extended passages don't exceed fair use, and content is transformative rather than copied.

**Token Budget:** ~500 tokens
**Purpose:** Quality control for plagiarism and copyright compliance

---

## When to Use

- After creating or updating expert files
- Before publishing or sharing expert content
- "Check this for plagiarism"
- "Is this content original?"
- "Verify fair use compliance"
- Quality control before final commit

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| expert_folder | Yes | Path to expert folder (e.g., `experts/miles-davis/`) |
| thoroughness | No | "quick" (quotes only) or "full" (all content) - default: full |

---

## What This Skill Checks

### 1. Quote Attribution

All direct quotes must be:
- Clearly marked as quotes (quotation marks or blockquote)
- Attributed to the source person
- Verified as authentic (cross-reference with references.md)

**Red flags:**
- Unattributed quotes
- Quotes presented as original content
- Fabricated quotes (no source exists)

### 2. Fair Use Compliance

Extended quotations must meet fair use criteria:

| Factor | Guideline |
|--------|-----------|
| **Length** | Single quotes: <100 words. Total from one source: <300 words or 10% of original |
| **Purpose** | Educational, commentary, criticism, or transformative use |
| **Effect on market** | Does not substitute for purchasing the original work |
| **Nature of work** | Factual works have more leeway than creative works |

**Red flags:**
- Multiple paragraphs quoted verbatim from a single source
- Song lyrics (even short excerpts can be problematic)
- Poetry (highly protected, even short quotes)
- Extended passages from biographies or books

### 3. Paraphrase Originality

Paraphrased content should be:
- Substantially reworded (not just synonym substitution)
- Restructured from the original
- Combined with original analysis or commentary

**Red flags:**
- Sentence structure matches original exactly
- Only a few words changed from source
- Multiple consecutive paraphrased sentences from same source

### 4. Transformative Content

Expert voice definitions should be:
- Original synthesis of the person's philosophy
- Not copied from existing biographies or analyses
- Unique framing for this specific use case

**Red flags:**
- Voice description matches Wikipedia or biography verbatim
- Framework descriptions copied from original works
- Examples lifted directly from source materials

---

## Checking Protocol

### Step 1: Inventory Content Types

Scan expert files and categorize content:

| Content Type | Files | Risk Level |
|--------------|-------|------------|
| Direct quotes | All files | Medium - must be attributed |
| Biographical facts | expertise.md, Chapter | Low - facts aren't copyrightable |
| Voice description | PROMPT.md | Medium - must be original synthesis |
| Methodologies/frameworks | expertise.md, skills | High - may be proprietary |
| Examples | PROMPT.md, skills | Medium - should be original |
| Song lyrics/poetry | Any | Very High - avoid or minimize |

### Step 2: Quote Audit

For each direct quote found:

1. **Verify attribution** - Is the speaker clearly identified?
2. **Check authenticity** - Is this quote in references.md as verified?
3. **Assess length** - Does it exceed fair use guidelines?
4. **Confirm purpose** - Is it used for commentary/education?

### Step 3: Passage Analysis

For extended prose sections (>50 words):

1. **Search for source** - Use WebSearch to check if text appears elsewhere
2. **Compare structure** - Does sentence structure match any source?
3. **Evaluate transformation** - Is this original synthesis or close paraphrase?

### Step 4: Special Content Review

Flag for manual review:
- Any song lyrics (even 1-2 lines)
- Poetry excerpts
- Extended book passages (>100 words from single source)
- Proprietary methodology names (trademarked terms)
- Images or media references

---

## Workflow

### Step 1: Gather and Review Inputs

Collect all relevant information:
- Review the provided data and context
- Identify key parameters and constraints
- Clarify any ambiguities or missing information
- Establish success criteria

### Step 2: Analyze the Situation

Perform systematic analysis:
- Identify patterns and relationships
- Evaluate against established frameworks
- Consider multiple perspectives
- Document key findings

### Step 3: Generate Recommendations

Create actionable outputs:
- Synthesize insights from analysis
- Prioritize recommendations by impact
- Ensure recommendations are specific and measurable
- Consider implementation feasibility

## Output Format

```markdown
## Content Originality Check: {Expert Name}

**Folder:** `{expert_folder}`
**Date:** {YYYY-MM-DD}
**Thoroughness:** {quick/full}

### Summary

| Category | Count | Status |
|----------|-------|--------|
| Direct quotes | X | ✓ All attributed |
| Extended passages | X | ✓ Within fair use |
| Paraphrased content | X | ✓ Sufficiently transformed |
| Special content | X | ⚠ Review needed |

### Overall Status: {PASS / REVIEW NEEDED / FAIL}

---

### Quote Attribution

| Quote | File:Line | Attribution | Status |
|-------|-----------|-------------|--------|
| "{quote excerpt}..." | expertise.md:45 | ✓ Attributed to {person} | PASS |
| "{quote excerpt}..." | PROMPT.md:23 | ✗ No attribution | FAIL |

### Fair Use Analysis

| Passage | Source | Word Count | Purpose | Status |
|---------|--------|------------|---------|--------|
| Biography section | Wikipedia-style | ~150 words | Educational | ✓ PASS |
| Book excerpt | {Title} | ~250 words | Commentary | ⚠ BORDERLINE |

### Flagged Content

| Content | File:Line | Issue | Recommendation |
|---------|-----------|-------|----------------|
| Song lyric | expertise.md:89 | Copyright risk | Remove or get license |
| Close paraphrase | PROMPT.md:34 | Too similar to source | Rewrite substantially |

### Special Review Items

Items requiring human judgment:

1. **{Item}** - {explanation of concern}
2. **{Item}** - {explanation of concern}

---

### Recommendations

1. {Specific action needed}
2. {Specific action needed}
```

---

## Risk Categories

### Low Risk (Generally Safe)
- Biographical facts (birth dates, career events)
- Short quotes (<25 words) with attribution
- Original synthesis and analysis
- Public domain content

### Medium Risk (Use Caution)
- Quotes 25-100 words with attribution
- Paraphrased methodologies
- Framework descriptions
- Voice characterizations

### High Risk (Minimize or Avoid)
- Quotes >100 words
- Song lyrics (any length)
- Poetry (any length)
- Extended book passages
- Trademarked terms without acknowledgment
- Content from living authors without clear fair use justification

### Very High Risk (Avoid Entirely)
- Unattributed quotes
- Verbatim copying without quotation marks
- Multiple pages from single copyrighted source
- Content presented as original when it's not

---

## Common Issues and Fixes

| Issue | Example | Fix |
|-------|---------|-----|
| Unattributed quote | "Just ship it." appears without speaker | Add: **{Person} said:** "Just ship it." |
| Close paraphrase | Sentence structure matches Wikipedia | Rewrite with different structure and add original insight |
| Excessive quoting | 5 paragraphs from one book | Summarize in own words, quote only key phrases |
| Song lyric | "Hello darkness my old friend" | Remove entirely or describe the song without lyrics |
| Proprietary term | "Getting Things Done®" | Add ® symbol and attribution to David Allen |

---

## Outputs

**Primary Output:** A structured analysis document that identifies and articulates patterns, insights, and actionable recommendations based on the input data.

**Format:**
```markdown
## Analysis: [Topic]

### Key Findings
- [Finding 1]
- [Finding 2]
- [Finding 3]

### Recommendations
1. [Action 1]
2. [Action 2]
3. [Action 3]
```

**Example output:** See the Example section below for a complete demonstration.

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].

## Integration

### With Create-Expert Workflow

Run this check:
- After Phase 3 (Training) - catch issues early
- After Phase 11 (Chapter) - before final validation
- Can be combined with Phase 12 (Validate References)

### With Other Skills

- **fact-check-expert**: Verifies quotes are authentic
- **analyze-references**: Confirms sources exist
- **content-originality-check**: Ensures content is legally usable (this skill)

---

## Constraints

- **Not a legal opinion** - This skill provides guidelines, not legal advice
- **Fair use is contextual** - Final determination requires human judgment
- **When in doubt, rewrite** - Original content is always safer than borderline fair use
- **Song lyrics are special** - Music publishers are aggressive; avoid lyrics entirely
- **Living authors** - Extra caution with recent works still generating revenue

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Can't find original source | Flag as "source unknown" for manual review |
| Borderline fair use | Flag as "REVIEW NEEDED" with explanation |
| Clear copyright violation | Mark as FAIL with specific fix required |
| Trademarked term found | Note for acknowledgment, not necessarily removal |

---

## Example Check

**Input:** `experts/miles-davis/`

**Process:**
1. Scan all files for quoted content → Found 12 quotes
2. Verify all quotes attributed → 11/12 attributed (1 missing in PROMPT.md)
3. Check quote lengths → All under 50 words ✓
4. Scan for extended passages → Found 200-word biography section
5. Search for source matches → No verbatim matches found ✓
6. Check for special content → No lyrics/poetry found ✓

**Output:**
```
Overall Status: REVIEW NEEDED

Issues:
1. PROMPT.md:67 - Quote "Do not fear mistakes..." missing attribution
   Fix: Add "Miles Davis said:" before quote

Recommendations:
1. Add attribution to unattributed quote in PROMPT.md
```

---

## Quick Check (Abbreviated)

For `thoroughness: quick`, only check:
1. All direct quotes are attributed
2. No song lyrics or poetry present
3. No single quote exceeds 100 words

Skip: paraphrase analysis, extended passage search, full transformation review