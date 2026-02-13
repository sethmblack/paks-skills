---
name: product-market-fit-diagnosis
description: Diagnose whether a product or startup has achieved product-market fit using Marc Andreessen's framework and prescribe specific next steps based on the diagnosis.
license: MIT
metadata:
  version: 1.0.1677
  author: sethmblack
keywords:
- product-market-fit-diagnosis
- transformation
- writing
---

# Product-Market Fit Diagnosis

Diagnose whether a product or startup has achieved product-market fit using Marc Andreessen's framework and prescribe specific next steps based on the diagnosis.

---

## When to Use

- Evaluating a startup's current stage and health
- Diagnosing why growth isn't happening
- Deciding what to prioritize (product vs. sales vs. hiring)
- Investment due diligence
- Founder asking "Do we have product-market fit?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **product_description** | Yes | What the product does and who it's for |
| **metrics** | Yes | Key metrics: growth rate, retention, sales cycle, customer feedback |
| **company_stage** | No | How long in market, funding stage |
| **team_actions** | No | What the team is currently focused on |

---

## Core Framework

Marc Andreessen's product-market fit definition: **"Being in a good market with a product that can satisfy that market."**

The startup lifecycle divides into two phases:
- **BPMF (Before Product-Market Fit):** Searching, iterating, surviving
- **APMF (After Product-Market Fit):** Scaling, hiring, expanding

**"The only thing that matters is getting to product/market fit."**

---

## Workflow

### Step 1: Check for BPMF Symptoms

Look for these indicators that product-market fit has NOT been achieved:

| Symptom | Questions to Ask |
|---------|------------------|
| **Low value perception** | "Are customers getting significant value?" |
| **Weak word of mouth** | "How are new customers finding you?" (If mostly paid acquisition, red flag) |
| **Slow usage growth** | "Is usage growing only when you advertise?" |
| **Lukewarm press** | "Are reviews 'meh' or 'interesting but...'?" |
| **Long sales cycles** | "How long from first contact to close?" |
| **Low close rates** | "What percentage of deals actually close?" |

**If 3+ symptoms present:** Likely BPMF

### Step 2: Check for APMF Symptoms

Look for these indicators that product-market fit HAS been achieved:

| Symptom | What It Looks Like |
|---------|-------------------|
| **Market pull** | "Customers are buying as fast as you can make it" |
| **Hiring pressure** | "Can't hire sales/support fast enough" |
| **Inbound interest** | "Reporters calling, customers finding you" |
| **Usage explosion** | "Metrics going up and to the right without advertising" |
| **Viral growth** | "Existing customers bringing new customers" |
| **Revenue acceleration** | "Month-over-month growth accelerating, not decelerating" |

**If 3+ symptoms present:** Likely APMF

### Step 3: Apply the Feel Test

Andreessen's insight: **"If you have to ask whether you have product-market fit, you don't."**

When you have it:
- You KNOW. There's no ambiguity.
- The problem becomes "how do we keep up?" not "how do we grow?"
- You're overwhelmed by demand, not searching for it.

### Step 4: Diagnose Root Cause (if BPMF)

If not at PMF, identify the likely cause:

| Cause | Indicators | Fix |
|-------|------------|-----|
| **Wrong market** | Good product, no buyers | Pivot to adjacent market |
| **Wrong product** | Right market, product doesn't solve the problem | Rebuild/iterate product |
| **Wrong segment** | Product works for some, not the target | Narrow focus to working segment |
| **Wrong positioning** | Product works but customers don't understand it | Reframe messaging |
| **Too early** | Market not ready | Survive until market matures |

### Step 5: Prescribe Actions

**If BPMF:**
- "Do whatever is required to get to product/market fit"
- Consider: changing people, rewriting product, moving markets, taking dilutive funding
- Do NOT scale sales, marketing, or headcount yet
- Focus entirely on finding fit

**If APMF:**
- Scale aggressively
- Hire ahead of demand
- Invest in infrastructure
- Expand to adjacent segments
- Focus on moat-building

---

## Outputs

### PMF Diagnosis Report

```markdown
## Product-Market Fit Diagnosis: [Product Name]

### Summary
**Status:** BPMF / APMF / Borderline
**Confidence:** High / Medium / Low

### Symptom Analysis

#### BPMF Indicators Present
- [ ] Low value perception: [evidence]
- [ ] Weak word of mouth: [evidence]
- [ ] Slow organic growth: [evidence]
- [ ] Lukewarm reception: [evidence]
- [ ] Long sales cycles: [evidence]
- [ ] Low close rates: [evidence]

**BPMF Score:** X/6

#### APMF Indicators Present
- [ ] Market pull: [evidence]
- [ ] Hiring pressure: [evidence]
- [ ] Inbound interest: [evidence]
- [ ] Usage explosion: [evidence]
- [ ] Viral growth: [evidence]
- [ ] Revenue acceleration: [evidence]

**APMF Score:** X/6

### Diagnosis

[Clear statement of PMF status with reasoning]

### Root Cause (if BPMF)

**Primary Issue:** [Wrong market / Wrong product / Wrong segment / Wrong positioning / Too early]

**Evidence:** [Why this is the likely cause]

### Prescribed Actions

**Immediate (This Week):**
1. [specific action]
2. [specific action]

**Short-term (This Month):**
1. [specific action]
2. [specific action]

**Do NOT Do:**
- [action to avoid given current status]

### The Andreessen Test

"If you have to ask whether you have product-market fit, you don't."

**Verdict:** [Do they know they have it, or are they asking?]
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
Product: B2B SaaS for restaurant inventory management
Metrics: 50 customers after 18 months, 15% monthly churn, 90-day sales cycle,
most leads come from outbound sales
Company stage: Seed funded, 2 years old
Team actions: Focused on adding features customers request
```

**Output:**

## Product-Market Fit Diagnosis: Restaurant Inventory SaaS

### Summary
**Status:** BPMF (Before Product-Market Fit)
**Confidence:** High

### Symptom Analysis

#### BPMF Indicators Present
- [x] Low value perception: 15% monthly churn suggests customers not getting enough value
- [x] Weak word of mouth: Most leads from outbound (not referrals)
- [x] Slow organic growth: 50 customers in 18 months is ~3/month
- [x] Long sales cycles: 90 days is very long for SMB software
- [x] Low close rates: Implied by outbound-heavy acquisition

**BPMF Score:** 5/6

#### APMF Indicators Present
- [ ] Market pull: No evidence
- [ ] Hiring pressure: No evidence
- [ ] Inbound interest: Minimal
- [ ] Usage explosion: No evidence
- [ ] Viral growth: No evidence
- [ ] Revenue acceleration: No evidence

**APMF Score:** 0/6

### Diagnosis

This product is clearly in BPMF phase. The 15% monthly churn is the most damning signal - customers are actively leaving, indicating the product isn't solving a painful enough problem or isn't solving it well enough. The 90-day sales cycle for what should be SMB quick-decision software suggests either wrong buyer or weak value proposition.

### Root Cause

**Primary Issue:** Wrong segment (possibly wrong market)

**Evidence:**
- Restaurant inventory is a real problem, but restaurants have thin margins and high failure rates
- They're notoriously difficult customers (time-poor, tech-skeptical)
- The feature-request-driven roadmap suggests chasing customers rather than solving a core problem
- High churn + long sales cycle = not a "hair on fire" problem for this segment

### Prescribed Actions

**Immediate (This Week):**
1. Interview the 10 customers with longest tenure - what's different about them?
2. Calculate actual ROI delivered to retained customers - is it 10x the cost?

**Short-term (This Month):**
1. Consider pivoting to adjacent market (food distributors, ghost kitchens, catering)
2. Stop adding features; identify ONE thing that drives retention
3. Find 5 customers who would be devastated if you shut down - understand why

**Do NOT Do:**
- Do NOT hire more sales people (you're not ready to scale)
- Do NOT keep building requested features (you're chasing, not leading)
- Do NOT raise more funding yet (validates wrong direction)

### The Andreessen Test

"If you have to ask whether you have product-market fit, you don't."

**Verdict:** The founders are asking. They don't have it.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient metrics | Ask for specific data on growth rate, retention, acquisition channels |
| Very early stage (pre-revenue) | Assess based on engagement signals, not revenue metrics |
| Two-sided marketplace | Analyze each side separately, then combined |
| Enterprise with few customers | Use qualitative signals (buyer urgency, expansion revenue) |

---

## Integration

This skill integrates with the **marc-andreessen** expert. The diagnosis should be delivered with characteristic directness - don't sugarcoat a BPMF diagnosis.

Related skills:
- `feature-vs-product-test` - Often relevant for BPMF products
- `market-over-team-analysis` - For root cause analysis
- `startup-idea-evaluation` - For earlier-stage assessment