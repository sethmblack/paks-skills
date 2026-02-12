---
name: fact-check-expert
description: Systematically verify factual claims in an expert persona's files, remove unverifiable information, and generate a comprehensive references document with sources.
version: 1.0.0
author: sethmblack
tags: [fact-check-expert, writing]
---

# Fact-Check Expert

Systematically verify factual claims in an expert persona's files, remove unverifiable information, and generate a comprehensive references document with sources.

---

## When to Use

- After creating or updating an expert persona
- User asks to "fact-check" or "verify" an expert
- Request to "add references" or "cite sources" for an expert
- Reviewing expert files for accuracy
- Preparing expert for publication or sharing
- Quality assurance on persona content

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| expert_name | Yes | The expert folder name (e.g., "miles-davis", "steve-jobs") |
| thoroughness | No | "quick" (biographical only), "standard" (all categories), "exhaustive" (cross-reference 3+ sources) |

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

## Files to Process

For the specified expert, read and verify claims in:

1. **expertise.md** - Primary source of factual claims (biographical data, works, dates, quotes)
2. **PROMPT.md** - Persona definition (may contain historical claims)
3. **skill-extraction-report.md** - Methodology analysis (may reference specific events)
4. **{expert-name}_Chapter.md** - Condensed version (subset of above)

---

## Claim Categories to Verify

### Category 1: Biographical Facts
- Full name, birth date, birth place
- Death date, death place (if applicable)
- Education, degrees, institutions
- Major life events with dates

**Verification Sources:** Wikipedia, Encyclopedia Britannica, official biographies

### Category 2: Works & Publications
- Book titles and publication dates
- Album/film/product releases with dates
- Patents, inventions, discoveries
- Company founding dates

**Verification Sources:** Library catalogs, Discogs, IMDb, USPTO, company records

### Category 3: Career Events
- Employment dates and positions
- Company foundings, departures, returns
- Major achievements with dates
- Awards and recognition

**Verification Sources:** News archives, official bios, award databases

### Category 4: Associated People
- Collaborators, partners, co-founders
- Band members, team members
- Mentors, students, influences
- Relationships to other historical figures

**Verification Sources:** Cross-referenced biographies, news articles

### Category 5: Quotes
- Direct quotations attributed to the person
- Speech excerpts with dates/contexts
- Interview statements
- Book passages

**Verification Sources:** Books, interview transcripts, speech archives, Wikiquote

### Category 6: Achievements & Records
- "First ever" or "best-selling" claims
- Records, awards, recognitions
- Comparative superlatives
- Industry rankings

**Verification Sources:** Industry databases, Guinness records, chart archives

### Category 7: Financial Claims
- Acquisition prices
- Company valuations
- Revenue/profit figures
- Investment amounts

**Verification Sources:** SEC filings, news reports, company announcements

### Category 8: Methodological Claims
- How they worked or created
- Specific processes attributed to them
- Habits, routines, practices
- Teaching or leadership methods

**Verification Sources:** Biographies, interviews, firsthand accounts

---

## Verification Workflow

### Step 1: Extract Claims

Parse each file and extract factual claims organized by category:

```
CLAIM EXTRACTION LOG
====================
File: expertise.md

BIOGRAPHICAL:
- [L12] "Born: May 26, 1926, Alton, Illinois"
- [L13] "Died: September 28, 1991, Santa Monica, California"

WORKS:
- [L45] "Kind of Blue (1959)"
- [L46] "Bitches Brew (1970)"

QUOTES:
- [L78] "Do not fear mistakes. There are none."
...
```

### Step 2: Verify Each Claim

For each extracted claim:

1. **Search** for authoritative sources using WebSearch
2. **Cross-reference** with 2+ sources when possible
3. **Record** source URLs and verification status
4. **Flag** any discrepancies or conflicting information

Verification statuses:
- ✓ **Verified** - Confirmed by reliable source(s)
- ⚠ **Corrected** - Original claim had error; corrected with source
- ✗ **Unverifiable** - No reliable source found; will be removed
- ? **Uncertain** - Conflicting sources; needs human review

### Step 3: Generate references.md

Create a comprehensive references document in the expert folder:

```markdown
# {Expert Name} - References & Fact Verification

**Verification Date:** {YYYY-MM-DD}
**Expert Folder:** `experts/{expert-name}/`
**Thoroughness Level:** {quick|standard|exhaustive}

## Summary

| Metric | Count |
|--------|-------|
| Total claims checked | X |
| ✓ Verified | X |
| ⚠ Corrected | X |
| ✗ Removed (unverifiable) | X |

---

## Biographical Facts

| Claim | Status | Source |
|-------|--------|--------|
| Born: {date}, {place} | ✓ | [Wikipedia]({url}) |
| Died: {date}, {place} | ✓ | [Britannica]({url}) |

## Works & Publications

| Work | Date | Status | Source |
|------|------|--------|--------|
| {Title} | {Year} | ✓ | [{Source}]({url}) |

## Quotes

| Quote | Context | Status | Source |
|-------|---------|--------|--------|
| "{quote text}" | {where/when said} | ✓ | [{Source}]({url}) |

## Career Events

| Event | Date | Status | Source |
|-------|------|--------|--------|
| {event description} | {date} | ✓ | [{Source}]({url}) |

## Associated People

| Person | Relationship | Status | Source |
|--------|--------------|--------|--------|
| {name} | {role} | ✓ | [{Source}]({url}) |

## Achievements

| Achievement | Status | Source |
|-------------|--------|--------|
| {claim} | ✓ | [{Source}]({url}) |

## Removed Claims

| Original Claim | File | Line | Reason |
|----------------|------|------|--------|
| "{claim}" | expertise.md | L45 | No source found |

---

## Sources Consulted

1. [Wikipedia - {Name}]({url})
2. [Encyclopedia Britannica]({url})
3. [{Other Source}]({url})
...
```

### Step 4: Update Source Files

For each unverifiable claim:
1. Locate the claim in the source file
2. Remove or modify the claim
3. Document the removal in references.md

For corrected claims:
1. Update the claim with verified information
2. Document the correction in references.md

---

## Outputs
After completion, the expert folder will contain:

```
experts/{expert-name}/
├── expertise.md          (updated - unverifiable claims removed)
├── PROMPT.md             (updated - if claims were removed)
├── skill-extraction-report.md (updated - if claims were removed)
├── {expert-name}_Chapter.md   (updated - if claims were removed)
└── references.md         (NEW - comprehensive source documentation)
```

---

## Example Invocation

```
/fact-check-expert miles-davis
/fact-check-expert steve-jobs thoroughness:exhaustive
/fact-check-expert abraham-lincoln thoroughness:quick
```

---

## Quality Standards

### Acceptable Sources (in order of preference)

1. **Primary sources** - Original works, speeches, interviews by the person
2. **Academic sources** - Peer-reviewed articles, university press books
3. **Encyclopedia sources** - Britannica, specialized encyclopedias
4. **Wikipedia** - For basic biographical facts (with citation to Wikipedia's sources)
5. **Reputable news** - Major newspapers, established magazines
6. **Industry databases** - AllMusic, IMDb, USPTO, etc.

### Unacceptable Sources

- Personal blogs without citations
- Social media posts
- User-generated content without verification
- Sources with clear bias or conflict of interest
- Circular citations (A cites B which cites A)

---

## Notes

- Focus verification effort on claims that matter most to the persona's authenticity
- Quotes require the highest verification standard (exact wording matters)
- Dates within ±1 year are acceptable for non-critical events
- When sources conflict, prefer primary sources or more authoritative secondary sources
- If a claim cannot be verified but is non-essential, remove it rather than include uncertainty

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].

