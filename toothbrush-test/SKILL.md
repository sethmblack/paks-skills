---
name: toothbrush-test
description: Evaluate any product, feature, or acquisition by testing whether it will
  be used daily and genuinely improves lives, prioritizing usefulness over financial
  metrics.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- toothbrush-test
- writing
---

# Toothbrush Test

Evaluate any product, feature, or acquisition by testing whether it will be used daily and genuinely improves lives, prioritizing usefulness over financial metrics.

**Token Budget:** ~700 tokens. Reserve tokens for evaluation output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Apply this test to justify addictive or harmful products
- Ignore ethical concerns in favor of usage metrics
- Recommend products that exploit users even if used daily

**Daily use does not equal value.** Cigarettes pass the frequency test but fail the "makes life better" test. Both criteria must be met.

---

## When to Use

- Evaluating whether to build a product or feature
- Assessing an acquisition target
- Prioritizing between product opportunities
- User asks "Should we build this?" or "Is this worth pursuing?"
- User explicitly invokes: "Does this pass the toothbrush test?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| subject | Yes | The product, feature, or acquisition to evaluate |
| target_users | No | Who would use this (default: general population) |
| usage_claim | No | Expected usage frequency if known |
| life_improvement | No | How it claims to make life better |

**Input Validation:**
- If subject is vague, ask: "What specifically does this product do?"
- If target users unclear, ask: "Who is this for?"

---

## Workflow

### Step 1: Define the Subject

Clearly articulate what is being evaluated:
- What is this product/feature/acquisition?
- What problem does it solve?
- What is the claimed value proposition?

### Step 2: Apply the Frequency Test

**Question:** Will people use this once or twice a day?

| Usage Level | Assessment |
|-------------|------------|
| Multiple times daily | STRONG PASS |
| Once daily | PASS |
| Several times per week | MARGINAL |
| Weekly or less | FAIL |
| One-time or rare use | FAIL |

**Consider:**
- Is the use case inherently recurring?
- Does it integrate into daily routines?
- Is there habit-forming potential (positive sense)?

### Step 3: Apply the Life Improvement Test

**Question:** Does this genuinely make life better?

| Improvement Type | Assessment |
|------------------|------------|
| Solves real pain point | STRONG PASS |
| Saves meaningful time | PASS |
| Enables previously impossible action | PASS |
| Provides entertainment/joy | PASS (if not exploitative) |
| Convenience only | MARGINAL |
| No clear improvement | FAIL |
| Creates dependency without benefit | FAIL |

**Consider:**
- Would users notice if this disappeared?
- Does it improve life or just fill time?
- Is the improvement genuine or manufactured need?

### Step 4: Calculate Scale Potential

**Question:** Could this reach billions of users?

| Scale Potential | Assessment |
|-----------------|------------|
| Universal human need | STRONG PASS |
| Large demographic need | PASS |
| Niche but deep need | MARGINAL |
| Limited addressable market | FAIL |

### Step 5: Deliver Verdict

Combine assessments into final recommendation.

---

## Outputs

### Toothbrush Test Report

```markdown
## Toothbrush Test: {subject}

### Subject Definition
**Product/Feature:** {description}
**Target Users:** {who}
**Value Proposition:** {claimed benefit}

### Frequency Assessment
**Expected usage:** {frequency}
**Verdict:** PASS / MARGINAL / FAIL
**Rationale:** {why}

### Life Improvement Assessment
**Improvement type:** {category}
**Verdict:** PASS / MARGINAL / FAIL
**Rationale:** {why}

### Scale Potential
**Addressable users:** {estimate}
**Verdict:** PASS / MARGINAL / FAIL
**Rationale:** {why}

---

### FINAL VERDICT: PASS / MARGINAL / FAIL

**Recommendation:** {build/acquire, defer, or pass with rationale}

**Key insight:** {one sentence summary of the evaluation}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Subject too vague | Ask for specific product description |
| B2B product (not consumer) | Adapt test: "Will decision-makers engage daily? Does it improve business outcomes?" |
| Platform vs product | Evaluate the core use case, not the platform potential |
| Addictive product | Fail the life improvement test. Daily use via exploitation is not value. |
| Already successful product | Use test to validate intuition or identify risks |

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
"We're considering acquiring a company that makes a calendar scheduling app."

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


## Toothbrush Test: Calendar Scheduling App

### Subject Definition
**Product/Feature:** Calendar scheduling application
**Target Users:** Professionals, students, anyone who schedules meetings
**Value Proposition:** Simplify scheduling by eliminating back-and-forth emails

### Frequency Assessment
**Expected usage:** Multiple times daily (view calendar, schedule meetings)
**Verdict:** STRONG PASS
**Rationale:** Calendar is inherently daily tool. Users check multiple times per day. Scheduling friction occurs constantly in professional contexts.

### Life Improvement Assessment
**Improvement type:** Saves meaningful time, solves real pain point
**Verdict:** PASS
**Rationale:** Scheduling coordination is genuine friction. Eliminating 5-10 back-and-forth emails per meeting creates real time savings. Users would notice if this disappeared.

### Scale Potential
**Addressable users:** Hundreds of millions to billions (anyone who schedules)
**Verdict:** PASS
**Rationale:** Universal need across professionals, students, families. Digital calendaring is global. Not limited to specific demographics.

---

### FINAL VERDICT: PASS

**Recommendation:** Proceed with acquisition evaluation. Product passes the toothbrush test. Next evaluate team quality, competitive position, and integration potential.

**Key insight:** Calendar scheduling meets daily utility threshold - it's infrastructure for how billions organize their lives, not a nice-to-have feature.

---

## Integration

This skill is part of the **larry-page** expert methodology. It works alongside:
- **tenx-thinking**: After passing toothbrush test, ask "how could this be 10x better?"
- **moonshot-evaluator**: High-pass toothbrush results may qualify for moonshot investment
- **asymmetric-bet-sizing**: Portfolio decisions informed by toothbrush assessments

---

## Success Criteria

Toothbrush test is complete when:
- [ ] Subject clearly defined
- [ ] Frequency assessment completed with rationale
- [ ] Life improvement assessment completed with rationale
- [ ] Scale potential evaluated
- [ ] Clear PASS/MARGINAL/FAIL verdict delivered
- [ ] Actionable recommendation provided