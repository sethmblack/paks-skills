---
name: analyze-references
description: Audit a references.md file to verify that all cited URLs are real, accessible, and actually support the claims attributed to them.
license: MIT
metadata:
  version: 1.0.3383
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- analyze-references
- writing
---

# Analyze References

Audit a references.md file to verify that all cited URLs are real, accessible, and actually support the claims attributed to them.

**Token Budget:** ~400 tokens
**Purpose:** Quality control for fact-checking; catch hallucinated sources

---

## When to Use

- After creating a references.md file
- Auditing existing expert persona references
- "Verify these sources are real"
- "Check for hallucinated URLs"
- Quality control before publishing

---

## The Problem

LLMs can hallucinate plausible-looking URLs and citations that:
- Don't exist at all (404)
- Exist but don't contain the claimed information
- Are real sites but wrong pages
- Have correct domains but fabricated paths

This skill systematically verifies each reference is real and accurate.

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| references_file | Yes | Path to the references.md file to audit |
| thoroughness | No | "quick" (spot-check) or "full" (every URL) |

---

## Audit Protocol

### Step 1: Extract All URLs

Parse the references.md file and extract every URL cited. Group by category:
- Wikipedia links
- Encyclopedia/reference sites (Britannica, etc.)
- Official sources (company sites, .gov, etc.)
- News articles
- Books/publications
- Other

### Step 2: Verify URL Existence

For each URL:
1. **Fetch the URL** using WebFetch
2. **Check for 404/errors** - Does the page exist?
3. **If redirected** - Note the redirect destination

### Step 3: Verify Content Match

For URLs that exist:
1. **Search for key terms** from the claim on the page
2. **Confirm the page actually supports** the cited fact
3. **Flag mismatches** where URL exists but doesn't contain claimed info

### Step 4: Categorize Results

| Status | Meaning | Action |
|--------|---------|--------|
| ✓ VERIFIED | URL exists and supports claim | None |
| ⚠ REDIRECT | URL redirects elsewhere | Update URL |
| ⚠ PARTIAL | Page exists but claim not found verbatim | Review manually |
| ✗ BROKEN | 404 or page doesn't exist | Find replacement or remove |
| ✗ MISMATCH | Page exists but contradicts claim | Correct the claim |

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
## References Audit: [Expert Name]

**File:** [path to references.md]
**Date:** [audit date]
**Thoroughness:** [quick/full]

### Summary

| Status | Count |
|--------|-------|
| ✓ Verified | X |
| ⚠ Needs Review | X |
| ✗ Broken/Invalid | X |
| **Total** | X |

### Broken or Invalid URLs

| Original URL | Status | Issue | Suggested Fix |
|--------------|--------|-------|---------------|
| [URL] | 404 | Page not found | [replacement or remove] |
| [URL] | MISMATCH | Claim not supported | [correct claim or new source] |

### URLs Needing Review

| URL | Issue | Notes |
|-----|-------|-------|
| [URL] | Redirect | Now points to [new URL] |
| [URL] | Partial match | Claim about X not found verbatim |

### Verified URLs

[List of URLs confirmed valid - can be collapsed/summarized]

### Recommendations

1. [Specific fix needed]
2. [Another fix]
```

---

## Common Hallucination Patterns

Watch for these red flags:

| Pattern | Example | Why Suspicious |
|---------|---------|----------------|
| Too-specific paths | `/article/2024/specific-fact-123` | LLMs invent plausible paths |
| Round dates in URLs | `/2020/01/01/` | Suspiciously clean dates |
| Quote in URL | `britannica.com/quote/exact-words` | Quotes aren't typically in URLs |
| Mixed domain styles | `en.wiki.org` vs `en.wikipedia.org` | Slight domain errors |
| Archived versions | `web.archive.org/...` | May not have actually checked |

---

## Quick Audit (Spot-Check)

For "quick" thoroughness:
1. Check all Wikipedia URLs (easy to verify)
2. Check any URL that looks suspiciously specific
3. Spot-check 20% of remaining URLs randomly
4. Check all URLs for claims marked as "key facts"

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

## Integration

This skill is part of the expert creation workflow. Run after:
- `fact-check-expert` creates references.md
- Before finalizing any expert persona

Can be invoked standalone for auditing existing references.

---