---
name: pre-pmf-post-pmf-diagnosis
description: Diagnose whether a product or company is before or after product-market fit, and prescribe phase-appropriate behaviors. Getting this wrong leads to either premature scaling (wasted resources) or stuck iteration (missed opportunity).
version: 1.0.0
author: sethmblack
tags: [pre-pmf-/-post-pmf-diagnosis, writing]
---

# Pre-PMF / Post-PMF Diagnosis

Diagnose whether a product or company is before or after product-market fit, and prescribe phase-appropriate behaviors. Getting this wrong leads to either premature scaling (wasted resources) or stuck iteration (missed opportunity).

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Declare PMF based on vanity metrics alone
- Recommend scaling behaviors before genuine PMF evidence
- Dismiss qualitative signals in favor of pure quantitative analysis
- Ignore negative user feedback patterns

**If evidence is ambiguous:** Default to "not yet PMF" - the cost of premature scaling exceeds the cost of continued iteration.

---

## When to Use

- Team is debating whether to scale
- Confusion about whether to invest in process/culture vs. iteration
- Metrics are growing but feeling "pushed" not "pulled"
- User asks: "Do we have product-market fit?" "Are we pre-PMF or post-PMF?" "Should we focus on culture or iteration?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| product_description | Yes | What the product does and for whom |
| growth_data | Yes | User/revenue growth patterns |
| user_feedback | Yes | Qualitative signals from users |
| retention_data | No | Do users come back? |
| acquisition_effort | No | How hard is it to get users? |
| team_size | No | Current team composition |

---

## The PMF Framework

"Pre product-market fit metrics are actually relatively unhelpful and you should bias very strongly towards kind of as much inspection and high-throughput qualitative feedback as possible."

### The Core Question

Is growth **pulling** you, or are you **pushing** for growth?

**Pre-PMF:** You convince people to try. You push.
**Post-PMF:** People find you. Growth pulls. You serve demand.

### Phase Characteristics

| Dimension | Pre-PMF | Post-PMF |
|-----------|---------|----------|
| Growth feel | Pushing | Pulling |
| User acquisition | Effortful | Organic/viral |
| Churn | High, unexplained | Manageable, understood |
| Retention | Weak, drops fast | Strong, users return |
| User feedback | Mixed, confused | Clear, specific requests |
| Word of mouth | Rare | Common |
| Pricing | Customers negotiate hard | Customers accept or pay more |

### Stripe's Pre-PMF Pattern

- Started with handful of test users, observed closely
- Changed dashboard 3x and API 2-3x in first year
- Expanded to ~100 pre-launch users
- Focused on "high-throughput qualitative feedback"
- Didn't worry about culture or team structure

---

## Workflow

### Step 1: Assess the Evidence

#### Quantitative Signals

| Signal | Data | Interpretation |
|--------|------|----------------|
| Growth rate | [X% MoM] | Organic or paid? Sustainable? |
| Retention (D7, D30) | [X%, Y%] | Are users coming back? |
| NPS | [Score] | Would users recommend? |
| Churn rate | [X%] | Are users leaving? Why? |
| CAC trend | [Up/Down/Flat] | Getting easier or harder to acquire? |
| Revenue per user | [Trend] | Willing to pay more over time? |

#### Qualitative Signals

| Signal | Evidence | Interpretation |
|--------|----------|----------------|
| Word of mouth | [Examples] | Are users bringing others? |
| User pull | [Examples] | Do users ask for more? Request features? |
| Competitive switching | [Examples] | Are users leaving competitors for you? |
| Emotional attachment | [Examples] | Do users love it or just use it? |
| "What would you do if this disappeared?" | [Responses] | Devastated or meh? |

### Step 2: Apply the Pull Test

**The Critical Question:** If you stopped all marketing and sales tomorrow, would growth continue?

| Scenario | Response | Meaning |
|----------|----------|---------|
| All acquisition stops | Growth stops | Pre-PMF (or very early) |
| All acquisition stops | Growth slows significantly | Pre-PMF or Marginal PMF |
| All acquisition stops | Growth continues | Post-PMF signals |
| All acquisition stops | Growth accelerates (word of mouth) | Strong PMF |

### Step 3: Check for False Positives

Growth can happen without PMF. Check for:

| False Positive | How to Detect |
|----------------|---------------|
| Paid acquisition masking weak product | CAC rising, retention weak |
| Novelty spike | Growth concentrated in first week |
| Press/launch bump | Clear spike then decay |
| One-time event | Growth tied to external moment |
| Forced usage (B2B mandate) | Low engagement despite "adoption" |

### Step 4: Diagnose Phase

Based on evidence, determine phase:

| Phase | Criteria | Confidence |
|-------|----------|------------|
| **Pre-PMF (Clear)** | Pushing for growth, high churn, weak retention, confused feedback | High |
| **Pre-PMF (Late)** | Some organic growth, improving retention, feedback converging | Medium |
| **PMF (Marginal)** | Clear demand signals but growth fragile, requires optimization | Medium |
| **PMF (Strong)** | Demand pulls, retention strong, word of mouth, can't keep up | High |

### Step 5: Prescribe Phase-Appropriate Behaviors

---

## Output Format

```markdown
## PMF Diagnosis: [Product Name]

### Product Summary
[One paragraph on what the product does and for whom]

### Evidence Assessment

#### Quantitative Signals
| Signal | Data | PMF Indicator? |
|--------|------|----------------|
| [Signal] | [Data] | Yes/No/Unclear |

#### Qualitative Signals
| Signal | Evidence | PMF Indicator? |
|--------|----------|----------------|
| [Signal] | [Evidence] | Yes/No/Unclear |

### The Pull Test
**If acquisition stopped tomorrow:** [What would happen]
**Interpretation:** [What this means]

### False Positive Check
| Potential False Positive | Present? | Evidence |
|--------------------------|----------|----------|
| Paid acquisition mask | Yes/No | [Evidence] |
| Novelty spike | Yes/No | [Evidence] |
| Forced B2B usage | Yes/No | [Evidence] |

### Diagnosis

**Phase:** Pre-PMF (Clear) / Pre-PMF (Late) / PMF (Marginal) / PMF (Strong)
**Confidence:** High / Medium / Low
**Key Evidence:** [2-3 most important data points]

### Prescribed Behaviors

#### What You Should Do
[Phase-appropriate recommendations]

#### What You Should NOT Do
[Common mistakes for this phase]

### Warning Signs to Watch

If you see these, your diagnosis may be wrong:
- [Signal that would change diagnosis]
- [Signal that would change diagnosis]

### The Collison Test

"Pre product-market fit metrics are relatively unhelpful."
**Are you measuring the right things for your phase?** [Assessment]
```

---

## Phase-Specific Prescriptions

### Pre-PMF Behaviors

**DO:**
- Prioritize speed of iteration above all else
- Get high-throughput qualitative feedback
- Observe users closely (handful at first)
- Be willing to change everything (dashboard 3x, API 2-3x)
- Stay small (smallest team that can iterate)
- Ship minimal increments rapidly

**DON'T:**
- Build culture or process (yet)
- Hire for scale
- Invest in brand
- Worry about metrics dashboards
- Optimize funnels
- Build for edge cases

### Post-PMF Behaviors

**DO:**
- Build the organization deliberately
- Codify culture
- Scale the team (carefully)
- Invest in process
- Optimize funnels and metrics
- Build for reliability and scale

**DON'T:**
- Lose the iteration speed entirely
- Hire B players because "we need people"
- Let process replace judgment
- Stop listening to users
- Assume PMF is permanent

---

## Constraints

- PMF is not binary - it's a spectrum
- PMF can be lost if product/market changes
- Different user segments may have different PMF status
- B2B and B2C PMF signals differ
- Enterprise PMF may look like fewer customers with deeper adoption

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No data available | Focus on qualitative signals. Interview 10 users. |
| Conflicting signals | Look for patterns. Which signals are most reliable? |
| B2B with few customers | Depth > breadth. Are those customers deeply engaged? |
| Marketplace (two sides) | Check PMF for each side separately. |
| New market (no comparables) | Use first principles. Are users pulling? |

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

**Input:** "We have 5,000 users, 15% MoM growth, but churn is 40%. Our NPS is 35. We're about to hire 10 engineers. Should we?"

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


## PMF Diagnosis: [SaaS Product]

### Product Summary
B2B SaaS with 5,000 users, growing 15% month-over-month. Team is considering scaling engineering headcount significantly.

### Evidence Assessment

#### Quantitative Signals
| Signal | Data | PMF Indicator? |
|--------|------|----------------|
| User count | 5,000 | Unclear (absolute numbers less meaningful) |
| Growth rate | 15% MoM | Potentially - if organic |
| Churn rate | 40% | **No** - major red flag |
| NPS | 35 | Borderline - some promoters but not overwhelming |

#### Qualitative Signals
| Signal | Evidence | PMF Indicator? |
|--------|----------|----------------|
| Word of mouth | Not mentioned | Unknown |
| User pull | Not mentioned | Unknown |
| Why users churn | Not mentioned | **Critical missing data** |

### The Pull Test
**If acquisition stopped tomorrow:** Unclear - need to know what's driving growth
**Interpretation:** 15% growth with 40% churn suggests heavy acquisition effort replacing lost users (hamster wheel)

### False Positive Check
| Potential False Positive | Present? | Evidence |
|--------------------------|----------|----------|
| Paid acquisition mask | **Likely** | High growth + high churn pattern |
| Novelty spike | Possible | Need cohort data |
| Forced B2B usage | Unknown | Need to know use case |

### Diagnosis

**Phase:** Pre-PMF (Clear)
**Confidence:** High
**Key Evidence:**
1. 40% churn is a critical failure signal - users try but don't stay
2. NPS of 35 means ~35% promoters but significant detractors
3. No evidence of organic growth or word of mouth

### Prescribed Behaviors

#### What You Should Do
- **Stop.** Do not hire 10 engineers.
- Understand why users churn. Interview 20 churned users this week.
- Identify the users who DO stay. What's different about them?
- Narrow focus to the segment that retains
- Iterate rapidly on retention, not acquisition
- Stay small until retention improves

#### What You Should NOT Do
- Scale team (you'll just churn more users faster)
- Invest in growth marketing (pouring water into leaky bucket)
- Build new features (until you know why current ones don't retain)
- Hire for "scale" (you don't have a scaling problem, you have a retention problem)

### Warning Signs to Watch

If you see these, your diagnosis may be wrong:
- Churned users say "I loved it but [specific fixable reason]"
- A specific segment has <10% churn (hidden PMF)
- Churn is driven by external factors, not product

### The Collison Test

"Pre product-market fit metrics are relatively unhelpful."
**Are you measuring the right things for your phase?**

You're tracking growth and user count. Those are vanity metrics in your situation. The only metric that matters right now is: **Why do 40% of users leave, and how do we make them stay?**

Do not hire 10 engineers until churn is under 15% and you understand exactly who your product is for.

---

## Integration

This skill is part of the **Patrick Collison** expert persona. Use it when diagnosing product stage and appropriate behaviors. It pairs well with:
- **speed-constraint-analysis** to move fast at appropriate pace for stage
- **seven-lines-of-code-audit** for DX complexity appropriate to stage
- **trapdoor-decision-filter** to identify which scaling decisions need care