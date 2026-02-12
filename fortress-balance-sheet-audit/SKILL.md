---
name: fortress-balance-sheet-audit
description: Assess organizational or financial resilience across the four pillars of fortress thinking: capital, liquidity, earnings quality, and operational strength.
version: 1.0.0
author: sethmblack
tags: [fortress-balance-sheet-audit, writing]
---

# Fortress Balance Sheet Audit

Assess organizational or financial resilience across the four pillars of fortress thinking: capital, liquidity, earnings quality, and operational strength.

**Token Budget:** ~800 tokens. Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Provide specific financial advice that requires professional licensing
- Guarantee outcomes based on the assessment
- Fabricate data or metrics not provided by the user
- Minimize serious financial risks to avoid uncomfortable conversations

**If asked to guarantee resilience:** Clarify that this framework identifies gaps but cannot predict all future scenarios.

---

## When to Use

- User asks "Is our balance sheet strong enough?"
- User asks "Can we survive a downturn?"
- User asks "Assess our financial resilience"
- User asks "Are we prepared for crisis?"
- Organization is entering uncertain economic conditions
- Before major strategic commitments requiring capital
- After a near-miss or stress event to assess remaining strength

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **financial_position** | Yes | Capital levels, liquidity metrics, debt structure, regulatory ratios |
| **earnings_profile** | Yes | Revenue streams, margin stability, diversification across segments |
| **operational_context** | Yes | Team capabilities, systems reliability, key process dependencies |
| **stress_scenarios** | No | Specific scenarios to test (e.g., "30% revenue decline", "key customer loss") |

**Input Validation:**
- If financial_position is missing: Request specific metrics (cash, equity, debt ratios)
- If earnings_profile is missing: Request revenue breakdown and margin information
- If vague: Ask for specifics before proceeding

---

## The Four Pillars Framework

### Pillar 1: Capital Strength

**Core Question:** Do you have significantly more capital than required minimums?

| Assessment Level | Criteria |
|-----------------|----------|
| Fortress (5) | Capital 50%+ above requirements/peers; can absorb major losses and still act |
| Strong (4) | Capital 25-50% above requirements; comfortable buffer |
| Adequate (3) | Meets requirements with 10-25% buffer; limited margin for error |
| Vulnerable (2) | At or near minimums; stress would threaten compliance |
| Critical (1) | Below requirements or dependent on specific outcomes |

### Pillar 2: Liquidity Position

**Core Question:** Can you meet all obligations and still have capacity to act?

| Assessment Level | Criteria |
|-----------------|----------|
| Fortress (5) | 12+ months runway; no forced-sale scenarios; access to backup facilities |
| Strong (4) | 6-12 months runway; manageable stress scenarios |
| Adequate (3) | 3-6 months runway; would need to take action under moderate stress |
| Vulnerable (2) | Less than 3 months runway; dependent on continuous cash flow |
| Critical (1) | Immediate liquidity concerns; forced-sale risk |

### Pillar 3: Earnings Quality

**Core Question:** Are earnings diversified, stable, and sustainable under stress?

| Assessment Level | Criteria |
|-----------------|----------|
| Fortress (5) | Multiple independent revenue streams; strong margins; recurring/contractual revenue |
| Strong (4) | Diversified but with concentration risk; good margins; mostly recurring |
| Adequate (3) | Moderate concentration; variable margins; mix of recurring/transactional |
| Vulnerable (2) | High concentration; thin margins; mostly transactional |
| Critical (1) | Single revenue stream; negative or breakeven margins; entirely transactional |

### Pillar 4: Operational Strength

**Core Question:** Can your people, systems, and processes execute under pressure?

| Assessment Level | Criteria |
|-----------------|----------|
| Fortress (5) | Deep bench; resilient systems; tested crisis procedures; culture of execution |
| Strong (4) | Capable team with some gaps; reliable systems; some crisis preparation |
| Adequate (3) | Key person dependencies; functional systems; limited crisis testing |
| Vulnerable (2) | Critical gaps in leadership; fragile systems; no crisis preparation |
| Critical (1) | Leadership crisis; system failures occurring; no capacity for additional stress |

---

## Workflow
### Step 1: Gather Position Data

For each pillar, collect specific metrics:

**Capital:** Equity ratios, debt-to-equity, regulatory capital (if applicable), unrestricted cash
**Liquidity:** Cash runway, credit facilities, asset liquidity, cash burn rate
**Earnings:** Revenue by segment, margin by segment, customer concentration, contract terms
**Operations:** Key person map, system uptime, process documentation, crisis response history

### Step 2: Score Each Pillar (1-5)

Apply the assessment criteria. Be honest - this is about understanding reality, not confirming comfort.

**Jamie Dimon principle:** "Don't try to use numbers to prove what you think. Try to use numbers to understand what you are doing."

### Step 3: Stress Test the Position

For each scenario (provided or default):
- What happens to each pillar under this stress?
- Which pillar breaks first?
- What would recovery require?

**Default stress scenarios:**
1. Revenue declines 30% for 12 months
2. Largest customer/revenue stream lost immediately
3. Major system failure or cyberattack
4. Key leader departure during crisis

### Step 4: Identify Gaps and Recommendations

For any pillar scoring below 4:
- Specific gap identified
- Recommended action to close gap
- Timeline for strengthening
- Cost/investment required

### Step 5: Determine Overall Fortress Status

**Overall Rating:**
- **Fortress:** All pillars score 4+; stress tests show resilience
- **Strong:** Average 4+; no pillar below 3; manageable gaps
- **Adequate:** Average 3+; gaps identified but not critical
- **Vulnerable:** Any pillar scores 2 or below; significant gaps
- **Critical:** Multiple pillars scoring 2 or below; immediate action required

---

## Output Format

```markdown
## Fortress Balance Sheet Audit

**Assessment Date:** {date}
**Overall Status:** {Fortress/Strong/Adequate/Vulnerable/Critical}

### Pillar Scores

| Pillar | Score | Key Finding |
|--------|-------|-------------|
| Capital Strength | X/5 | {one-line summary} |
| Liquidity Position | X/5 | {one-line summary} |
| Earnings Quality | X/5 | {one-line summary} |
| Operational Strength | X/5 | {one-line summary} |

### Stress Test Results

| Scenario | Breaking Point | Recovery Requirement |
|----------|---------------|---------------------|
| {scenario} | {which pillar fails first} | {what's needed to recover} |

### Critical Gaps

{For each gap: description, recommended action, timeline, investment}

### Fortress Building Priorities

1. {Highest priority action}
2. {Second priority action}
3. {Third priority action}

### Bottom Line

{2-3 sentence summary in Dimon voice: direct assessment and core recommendation}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Incomplete financial data | Request specific missing metrics; note limitations in assessment |
| Unrealistic self-assessment | Challenge with probing questions; apply honest assessment protocol |
| No stress scenarios provided | Use default scenarios; note assumptions |
| Data too vague to score | Return "Unable to assess" for that pillar with specific data needs |
| Multiple critical findings | Prioritize by immediate risk; recommend professional consultation |

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

**Input:** Tech startup with $2M cash, 6 months runway, 80% revenue from one customer, 3-person leadership team

**Output:**



**Why this works:**

This example demonstrates the key principles of the skill in action. The approach is effective because:
- It follows the systematic workflow outlined above
- It shows concrete application of the framework
- It produces actionable, specific outputs rather than vague generalizations
- The analysis is grounded in observable details
- The recommendations are prioritized and implementable

**Alternative applications:**

This same approach can be applied to:
- Different contexts within the same domain
- Related but distinct problem types
- Scaled up or down depending on scope
- Combined with complementary analytical frameworks


## Fortress Balance Sheet Audit

**Assessment Date:** 2026-01-29
**Overall Status:** Vulnerable

### Pillar Scores

| Pillar | Score | Key Finding |
|--------|-------|-------------|
| Capital Strength | 2/5 | No equity cushion; dependent on next funding round |
| Liquidity Position | 3/5 | 6 months runway adequate but tight; no backup facilities |
| Earnings Quality | 2/5 | 80% concentration in single customer is critical risk |
| Operational Strength | 3/5 | Lean team functional but key person dependencies |

### Critical Gaps

**Customer Concentration:** Loss of primary customer would be existential. Immediate priority to diversify.

**Capital Buffer:** No capacity to weather extended stress or pursue opportunities. Fundraising or profitability path needed.

### Bottom Line

You are not a fortress - you are a house that could catch fire quickly. Your 80% customer concentration is a critical vulnerability that must be addressed before any other strategic initiative. A fortress balance sheet is not built during a crisis. Start building it now.

---

## Integration

This skill is derived from the **Jamie Dimon** expert's fortress balance sheet philosophy. When invoked by the Dimon expert, outputs should maintain his direct, operationally-grounded voice.

**Related skills:** crisis-acquisition-evaluation, honest-assessment-protocol