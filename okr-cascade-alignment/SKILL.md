---
name: okr-cascade-alignment
description: Create aligned OKR cascades from company to team to individual level, ensuring vertical and horizontal alignment following John Doerr's methodology from *Measure What Matters*.
version: 1.0.0
author: sethmblack
tags: [okr-cascade-alignment, writing]
---

# OKR Cascade Alignment

Create aligned OKR cascades from company to team to individual level, ensuring vertical and horizontal alignment following John Doerr's methodology from *Measure What Matters*.

**Token Budget:** ~800 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Create cascades that would pit teams against each other destructively
- Set individual OKRs that ignore worker wellbeing or ethics
- Design systems that enable blame without support

**If asked to create harmful cascades:** Refuse and explain the organizational damage.

---

## When to Use

- User says "Align team OKRs", "How do our OKRs connect?", "Create OKR cascade"
- Organization is rolling out OKRs to multiple levels
- Teams feel disconnected from company objectives
- Need to identify cross-functional dependencies

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| company_okrs | Yes | Top-level company OKRs |
| teams | Yes | List of teams or functions to align |
| individuals | No | Roles or individuals for individual-level OKRs |

---

## Workflow

### Step 1: Validate Company OKRs

Before cascading, verify top-level OKRs are:
- Measurable (specific key results)
- Focused (3-5 objectives)
- Ambitious (stretch goals)
- Clear (team can understand them)

If company OKRs are weak, flag and recommend fixing first.

### Step 2: Map Contributions

For each company key result:
- Which teams can contribute?
- What is each team's natural contribution?
- Are there dependencies between teams?

Create contribution map:
```
Company KR1 → Team A (primary), Team B (support)
Company KR2 → Team C (primary), Team A (support)
Company KR3 → Team B (primary), Team C (support)
```

### Step 3: Create Team OKRs

For each team, create OKRs that:
- **Connect up** - Contribute to at least one company KR
- **Are owned** - Team has control over outcomes
- **Are specific** - Tailored to team's domain

Balance:
- 50% aligned to company OKRs (connected)
- 50% team-specific (operational necessities)

### Step 4: Create Individual OKRs (if requested)

For individuals:
- Connect to at least one team KR
- Reflect the individual's unique contribution
- Balance: roughly 50% connected, 50% personal development

### Step 5: Verify Alignment

Check:
- **Vertical alignment:** Does each level connect upward?
- **Horizontal alignment:** Are cross-team dependencies identified?
- **Gaps:** Are there company KRs with no team coverage?
- **Overload:** Are any teams carrying too much?

---

## Output Format

```markdown
## OKR Cascade: [Organization Name]

### Alignment Summary

| Company KR | Contributing Teams | Primary Owner |
|------------|-------------------|---------------|
| [KR1] | [Team A, Team B] | [Team A] |
| [KR2] | [Team C] | [Team C] |

### Company Level

**Objective:** [Company objective]
- KR1: [Key result]
- KR2: [Key result]
- KR3: [Key result]

### Team Level

#### [Team A]

**Objective:** [Team objective aligned to company goal]
- KR1: [Contributes to Company KR1] → Links to Company KR1
- KR2: [Team-specific operational KR]
- KR3: [Team-specific operational KR]

**Dependencies:** [Team B for X, Team C for Y]

[Repeat for each team]

### Individual Level (if applicable)

#### [Role/Name]

**Objective:** [Individual objective]
- KR1: [Contributes to Team KR1] → Links to Team KR1
- KR2: [Individual development KR]

### Gaps and Risks

| Issue | Impact | Recommendation |
|-------|--------|----------------|
| [Gap/Risk] | [Impact] | [Fix] |
```

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
```
Company OKRs:
- Objective: Achieve market leadership
  - KR1: Reach $50M ARR
  - KR2: Acquire 500 enterprise customers
  - KR3: Achieve 130% net revenue retention

Teams: Sales, Customer Success, Product
```

**Output:**

## OKR Cascade: Example Corp

### Alignment Summary

| Company KR | Contributing Teams | Primary Owner |
|------------|-------------------|---------------|
| $50M ARR | Sales, Product | Sales |
| 500 enterprise customers | Sales, Marketing | Sales |
| 130% NRR | Customer Success, Product | Customer Success |

### Company Level

**Objective:** Achieve market leadership in enterprise AI
- KR1: Reach $50M ARR by end of fiscal year
- KR2: Acquire 500 enterprise customers
- KR3: Achieve 130% net revenue retention

### Team Level

#### Sales

**Objective:** Build a world-class enterprise sales organization

**Key Results:**
- KR1: Close $35M in new ARR → Links to Company KR1
- KR2: Acquire 350 new enterprise logos → Links to Company KR2
- KR3: Reduce sales cycle from 90 to 60 days

**Dependencies:** Product (demo environment), Marketing (lead generation)

#### Customer Success

**Objective:** Create customers who grow and advocate

**Key Results:**
- KR1: Achieve 130% net revenue retention → Links to Company KR3
- KR2: Expand 50 accounts by $10K+ each → Links to Company KR1
- KR3: Achieve 70+ NPS across customer base

**Dependencies:** Product (feature requests), Sales (handoff quality)

#### Product

**Objective:** Deliver capabilities that win and retain enterprise customers

**Key Results:**
- KR1: Ship enterprise SSO and audit logging by Q2 → Supports Sales KR1, KR2
- KR2: Reduce critical bugs to <5 open at any time → Supports CS KR1
- KR3: Achieve 90% feature adoption in top 20 accounts

**Dependencies:** Engineering capacity, Customer Success (feedback loop)

### Gaps and Risks

| Issue | Impact | Recommendation |
|-------|--------|----------------|
| Marketing not included | Company KR2 (customers) has lead gen dependency | Add Marketing OKRs |
| Product capacity risk | Multiple team dependencies on Product | Prioritization conversation needed |

---

## Integration

This skill integrates with the **john-doerr** expert persona. Embody Doerr's emphasis on transparency and connection - OKRs should be visible and linked.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Company OKRs are vague | Flag and recommend fixing before cascading |
| Too many teams | Group into logical clusters |
| No individual data | Cascade to team level only, provide individual template |