---
name: feature-vs-product-test
description: Determine whether a startup idea is a standalone product that can become a company, or a feature that will be absorbed by larger platforms.
license: MIT
metadata:
  version: 1.0.3990
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- feature-vs.-product-test
- writing
---

# Feature vs. Product Test

Determine whether a startup idea is a standalone product that can become a company, or a feature that will be absorbed by larger platforms.

---

## When to Use

- Evaluating a startup idea before committing
- Assessing competitive risk from big tech platforms
- Due diligence on investment opportunities
- Deciding whether to build, buy, or partner
- Analyzing why a startup failed (post-mortem)

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **idea_description** | Yes | What the product does and who it's for |
| **adjacent_platforms** | No | Larger platforms that operate nearby |
| **moat_claims** | No | What the founder claims as defensible advantages |

---

## Core Framework

Marc Andreessen's insight: **"If you're just building an inventory tracking tool, you're a feature. Shopify or Toast will add that in six months."**

**Features** get absorbed by platforms that have:
- Existing user base
- Adjacent functionality
- Distribution advantage
- Engineering resources

**Products** become companies because they have:
- Standalone value proposition
- Network effects or data moats
- Distinct buyer/user relationship
- Defensible technical depth

---

## Workflow

### Step 1: Identify Adjacent Platforms

List all larger platforms that operate in the same space:

| Platform Type | Examples |
|--------------|----------|
| Horizontal platforms | Salesforce, Microsoft, Google, Apple |
| Vertical platforms | Shopify (commerce), Toast (restaurants), Stripe (payments) |
| Social platforms | Meta, TikTok, LinkedIn |
| Cloud providers | AWS, Azure, GCP |

**Ask:** Who has users that would want this functionality?

### Step 2: Apply the "Six Month Test"

Could a platform add this functionality in 6 months?

| Factor | Feature Signal | Product Signal |
|--------|---------------|----------------|
| Technical complexity | Simple CRUD, basic ML | Deep tech, years of R&D |
| Data requirements | Uses platform's existing data | Requires proprietary data collection |
| User workflow | Incremental improvement | New workflow or behavior |
| Integration depth | Works best integrated | Works best standalone |

### Step 3: Assess Defensibility

Evaluate the claimed moat:

| Moat Type | Durability | Feature Risk |
|-----------|------------|--------------|
| Network effects | High | Low - hard to replicate |
| Proprietary data | High | Low - requires time to build |
| Switching costs | Medium | Medium - platforms can match |
| Brand | Medium | Medium - but slow to build |
| Regulatory/legal | Medium | Low - but can change |
| Technical IP | Low-Medium | High if commodity tech |
| First mover | Low | High - easily overtaken |

### Step 4: Check Platform Economics

Would a platform be economically motivated to build this?

| Question | If Yes (Feature Risk) | If No (Product Potential) |
|----------|----------------------|---------------------------|
| Does it drive platform usage? | High risk | Lower risk |
| Does it improve platform metrics? | High risk | Lower risk |
| Is the market large enough for platform to care? | High risk | Lower risk |
| Does it compete with platform revenue? | High risk | Lower risk |

### Step 5: Assess Standalone Viability

Could this be a successful standalone company?

| Question | Feature Signal | Product Signal |
|----------|---------------|----------------|
| Can you sell without the platform? | No | Yes |
| Do you control the customer relationship? | No | Yes |
| Can you price independently? | No | Yes |
| Does your value increase without the platform? | No | Yes |

### Step 6: Render Verdict

Based on the analysis, classify:

**FEATURE** - High absorption risk, recommend against
**PRODUCT** - Standalone viability, can become a company
**BORDERLINE** - Could go either way, depends on execution and speed

---

## Outputs

### Feature vs. Product Assessment

```markdown
## Feature vs. Product Test: [Idea Name]

### Summary
**Classification:** FEATURE / PRODUCT / BORDERLINE
**Platform Risk:** High / Medium / Low
**Recommendation:** [Build as company / Pivot / Don't pursue]

### Adjacent Platform Analysis

| Platform | Proximity | Would They Build? | Timeline |
|----------|-----------|-------------------|----------|
| [platform] | [close/medium/far] | [yes/no/maybe] | [months] |

### Six Month Test
**Could a major platform build this in 6 months?**
[Yes/No with reasoning]

### Defensibility Assessment

| Claimed Moat | Reality Check | Durability |
|--------------|---------------|------------|
| [moat claim] | [actual status] | [high/medium/low] |

### Platform Economics
**Would platforms be economically motivated to build this?**
[Analysis of incentives]

### Standalone Viability
| Factor | Assessment |
|--------|------------|
| Sell without platform | [Yes/No] |
| Own customer relationship | [Yes/No] |
| Independent pricing | [Yes/No] |
| Value without platform | [Yes/No] |

**Standalone Score:** X/4

### Verdict

[Clear statement with reasoning]

### Recommendations

**If Pursuing:**
- [how to build defensibility]
- [what to do before platforms notice]

**If Pivoting:**
- [direction to consider]
- [how to find product not feature]
```

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
Idea: AI tool that summarizes Slack conversations and creates action items
Adjacent platforms: Slack, Microsoft Teams, Notion, Asana
Moat claims: "Better AI than competitors", "First mover advantage"
```

**Output:**

## Feature vs. Product Test: Slack AI Summarizer

### Summary
**Classification:** FEATURE
**Platform Risk:** Critical (9/10)
**Recommendation:** Do not pursue as standalone company

### Adjacent Platform Analysis

| Platform | Proximity | Would They Build? | Timeline |
|----------|-----------|-------------------|----------|
| Slack | Direct | Already building (Slack AI) | Now |
| Microsoft Teams | Direct | Yes (Copilot) | Now |
| Notion | Adjacent | Yes (Notion AI) | 6 months |
| Asana | Adjacent | Likely | 12 months |

### Six Month Test
**Could a major platform build this in 6 months?**

Yes. In fact, they already have. Slack announced Slack AI in 2023 with conversation summaries and action item extraction. Microsoft Copilot in Teams does the same. This is core platform functionality, not a standalone business.

### Defensibility Assessment

| Claimed Moat | Reality Check | Durability |
|--------------|---------------|------------|
| "Better AI" | Using same foundational models (GPT-4, Claude) as platforms | Low - not defensible |
| "First mover" | Platforms already launched similar features | None - already overtaken |

### Platform Economics
**Would platforms be economically motivated to build this?**

Absolutely. This is a premium feature that:
- Drives platform stickiness (users stay in Slack)
- Enables premium pricing (Slack AI is paid add-on)
- Uses their proprietary data (conversation history)
- Improves core metrics (engagement, retention)

Slack and Microsoft have every incentive to build this and have already done so.

### Standalone Viability
| Factor | Assessment |
|--------|------------|
| Sell without platform | No - requires Slack/Teams integration |
| Own customer relationship | No - Slack owns the user |
| Independent pricing | No - competes with platform's own pricing |
| Value without platform | No - worthless without the conversations |

**Standalone Score:** 0/4

### Verdict

This is a textbook feature. It has:
- Zero standalone viability
- No defensible moat
- Direct platform competition already in market
- Complete dependency on platforms that are building the same thing

The claimed moats ("better AI", "first mover") are not real. Any AI quality advantage is temporary and likely illusory given everyone uses the same foundational models.

### Recommendations

**Do Not Pursue** as currently conceived.

**If Pivoting:**
- Look for workflow that platforms WON'T build (cross-platform, controversial, vertical-specific)
- Consider: cross-platform meeting intelligence (Zoom + Slack + Docs)
- Consider: vertical-specific compliance summarization (legal, healthcare)
- Find the use case platforms are economically DISincentivized to build

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No adjacent platforms identified | Good sign - may be genuinely new market |
| Platform already tried and failed | Investigate why - may indicate product viability |
| Highly regulated space | Factor in platform risk tolerance for compliance |
| B2B vertical | Platforms often ignore small verticals - lower feature risk |

---

## Integration

This skill integrates with the **marc-andreessen** expert. The assessment should be delivered with characteristic bluntness - if it's a feature, say so clearly.

Related skills:
- `software-disruption-analysis` - For understanding platform dynamics
- `product-market-fit-diagnosis` - For evaluating execution
- `tam-expansion-analysis` - For market sizing if product potential