---
name: multi-vertical-expansion-assessment
description: Assess when and how to expand into adjacent verticals while maintaining
  core business health, using the "Spotify Machine" approach of building multiple
  verticals that work together.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- multi-vertical-expansion-assessment
- writing
---

# Multi-Vertical Expansion Assessment

Assess when and how to expand into adjacent verticals while maintaining core business health, using the "Spotify Machine" approach of building multiple verticals that work together.

**Token Budget:** ~700 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend expansion that would destroy core business without clear mitigation
- Encourage expansion driven by ego rather than strategic logic
- Ignore resource constraints that make expansion impossible
- Fabricate market data or margin projections

**If asked to justify ill-considered expansion:** Refuse explicitly. Expansion should create compounding value, not dilute focus.

---

## When to Use

- User asks "Should we expand into X?"
- User asks "Adjacent market opportunity"
- User asks "Diversification strategy"
- User says "We've saturated our core market"
- User asks "What vertical should we enter next?"
- Company has successful core product and is considering expansion

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| **core_product** | Yes | Current successful product/vertical | Must have established product-market fit |
| **proposed_vertical** | Yes | New vertical being considered | |
| **strategic_rationale** | Yes | Why this expansion makes sense | |
| **resources** | No | Available resources for expansion | |
| **timeline** | No | Expected timeline for expansion | |

---

## The Philosophy

**The "Spotify Machine" Insight:** Daniel Ek described Spotify as "not just a one-trick pony anymore, but multiple verticals working together" to create consumer choice and drive engagement.

**Strategic Principles:**
- Focus on lifetime value of customers over short-term engagement metrics
- Add new verticals every few years
- Direct sufficient resources at each vertical to achieve market leadership
- Leverage cross-vertical synergies: "You may come for the music and stay for the audiobooks"

**The Spotify Timeline:**
| Year | Vertical | Rationale |
|------|----------|-----------|
| 2008 | Music | Core product, fight piracy |
| 2019 | Podcasts | Better margins, same users |
| 2022 | Audiobooks | Variable costs, cross-sell opportunity |

---

## Workflow

### Step 1: Validate Core Business Health

Before expansion, confirm the core is strong:

| Health Indicator | Status | Minimum Threshold |
|------------------|--------|-------------------|
| Product-market fit | Yes/No | Must be Yes |
| Positive unit economics | Yes/No | Should be Yes |
| Growth trajectory | Growing/Flat/Declining | Should be Growing or Flat |
| Market position | Leader/Challenger/Follower | Should not be struggling Follower |

**Critical Rule:** Do not expand from weakness. A struggling core business rarely improves by adding complexity.

### Step 2: Assess Vertical Fit

Evaluate the proposed vertical against strategic criteria:

| Criterion | Score (1-5) | Notes |
|-----------|-------------|-------|
| **User overlap** | | Do your current users want this? |
| **Capability transfer** | | Can you apply what you've built? |
| **Brand fit** | | Does it make sense you would offer this? |
| **Margin improvement** | | Is the margin profile better or worse? |
| **Competitive advantage** | | Do you have a right to win? |
| **Resource requirement** | | Can you resource it properly? |

**Total: /30** (Threshold: 20+ to proceed)

### Step 3: Analyze Economics

| Metric | Core Vertical | New Vertical | Comparison |
|--------|---------------|--------------|------------|
| Gross margin | % | % | Better/Worse/Same |
| Customer acquisition cost | $ | $ | Better/Worse/Same |
| Payback period | months | months | Better/Worse/Same |
| Lifetime value | $ | $ | Better/Worse/Same |
| Cross-sell potential | N/A | % of core users | |

**The Spotify Margin Lesson:**
- Music: Low margin (70% to rights holders)
- Podcasts: Medium-high margin potential (no per-stream royalties)
- Audiobooks: Variable costs, better margin profile

### Step 4: Design Cross-Vertical Synergies

What synergies exist between verticals?

| Synergy Type | Description | Value |
|--------------|-------------|-------|
| **User acquisition** | Does one vertical attract users for another? | |
| **User retention** | Does having both increase stickiness? | |
| **Cross-sell** | Can you convert users between verticals? | |
| **Shared infrastructure** | Can you reuse technology/ops? | |
| **Brand reinforcement** | Does each vertical strengthen the brand? | |

**The "Come for X, Stay for Y" Test:**
Write the sentence: "Users may come for [core] and stay for [new vertical]."
If it sounds natural, synergy exists.

### Step 5: Create Expansion Plan

| Phase | Timeline | Investment | Success Metric |
|-------|----------|------------|----------------|
| **Pilot** | [Months] | [Resources] | [What proves viability] |
| **Scale** | [Months] | [Resources] | [What proves growth] |
| **Leadership** | [Months] | [Resources] | [What proves market position] |

**Investment Principle:** Direct sufficient resources at each vertical to achieve market leadership. Half-hearted expansion fails.

### Step 6: Define Kill Criteria

What would make you exit this vertical?

| Kill Trigger | Threshold | Timeline |
|--------------|-----------|----------|
| User adoption below | [X%] | By [date] |
| Margin profile below | [X%] | By [date] |
| Core business impact | [X negative signal] | If observed |

---

## Outputs

Return a structured Multi-Vertical Expansion Assessment:

```markdown
## Multi-Vertical Expansion Assessment: [New Vertical]

### Core Business Health Check

| Indicator | Status | Proceed? |
|-----------|--------|----------|
| Product-market fit | | |
| Unit economics | | |
| Growth trajectory | | |
| Market position | | |

**Core Health Verdict:** Ready for expansion / Not ready

### Vertical Fit Analysis

| Criterion | Score | Notes |
|-----------|-------|-------|
| User overlap | /5 | |
| Capability transfer | /5 | |
| Brand fit | /5 | |
| Margin improvement | /5 | |
| Competitive advantage | /5 | |
| Resource requirement | /5 | |
| **Total** | /30 | Threshold: 20 |

### Economic Comparison

| Metric | Core | New | Comparison |
|--------|------|-----|------------|
| Gross margin | | | |
| CAC | | | |
| LTV | | | |

### Cross-Vertical Synergies

**"Come for [core], stay for [new]":** [Natural/Forced/Impossible]

| Synergy | Description | Strength |
|---------|-------------|----------|
| [Type] | [How it works] | High/Medium/Low |

### Expansion Plan

| Phase | Timeline | Investment | Success Metric |
|-------|----------|------------|----------------|
| Pilot | | | |
| Scale | | | |
| Leadership | | | |

### Kill Criteria

| Trigger | Threshold | Timeline |
|---------|-----------|----------|
| [Signal] | [Number] | [Date] |

### Recommendation

**Verdict:** Expand / Do Not Expand / Expand with Conditions

**Rationale:**
[Summary of key factors driving recommendation]

**Key Risks:**
1. [Risk 1]
2. [Risk 2]

**Next Steps:**
1. [Action 1]
2. [Action 2]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Core business unhealthy | Recommend fixing core before expanding |
| Vertical fit score below 20 | Recommend against expansion; identify what would need to change |
| No clear synergies | Question strategic rationale; may be better as separate company |
| Insufficient resources | Recommend phased approach or partnership |
| User requests expansion for defensive reasons | Distinguish defense from opportunity; defense alone is weak rationale |

---

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
core_product: "B2B SaaS for project management, 100K users, profitable"
proposed_vertical: "Time tracking and invoicing for freelancers"
strategic_rationale: "Same buyers, adjacent workflow, higher margin"
resources: "$2M budget, can hire 10-person team"
```

**Output Summary:**

> **Core Health: Ready for expansion.** Profitable core with 100K users provides stable base.
>
> **Vertical Fit: 22/30** - Passes threshold.
> - User overlap: 3/5 (freelancers are related but different from B2B teams)
> - Capability transfer: 4/5 (project data flows to time tracking naturally)
> - Brand fit: 4/5 (sensible extension)
> - Margin improvement: 5/5 (SaaS to SaaS, similar or better)
> - Competitive advantage: 3/5 (crowded market, no clear edge)
> - Resource requirement: 3/5 (10 people is tight for new vertical)
>
> **Synergy Test:** "Come for project management, stay for time tracking" - sounds natural but only if the same user does both. Freelancers and B2B teams may not overlap as much as assumed.
>
> **Recommendation: Expand with conditions.**
> - Start by adding time tracking to existing product (not separate vertical)
> - Test whether existing users adopt before building standalone freelancer product
> - If 20%+ of existing users use time tracking, then build standalone
> - Kill criteria: Less than 10% adoption of time tracking by existing users in 6 months

---

## Integration

This skill originates from the **Daniel Ek** expert methodology. When used:
- Apply "Spotify Machine" thinking: verticals should work together
- Focus on lifetime value, not just engagement
- Each vertical should aim for market leadership, not also-ran
- Remember: "You may come for the music and stay for the audiobooks"

---

## Success Criteria

Multi-Vertical Expansion Assessment is complete when:
- [ ] Core business health validated
- [ ] Vertical fit scored (threshold 20+)
- [ ] Economics compared (margin, CAC, LTV)
- [ ] Cross-vertical synergies identified
- [ ] Expansion plan phased (pilot, scale, leadership)
- [ ] Kill criteria defined
- [ ] Clear recommendation delivered with rationale