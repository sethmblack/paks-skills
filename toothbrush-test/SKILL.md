---
name: toothbrush-test
description: Evaluate products, features, or acquisitions by testing whether they will be used daily by billions and genuinely improve lives, using Larry Page's prioritization framework that values usefulness over financial metrics.
license: MIT
metadata:
  version: 1.0.2126
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- toothbrush-test
- product-evaluation
- acquisition
- writing
---

# Toothbrush Test

Evaluate any product, feature, or acquisition by testing whether it will be used daily and genuinely improves lives, prioritizing usefulness over financial metrics. This evaluation framework originated from Larry Page's approach to acquisitions at Google, where he would ask: "Is this something people will use once or twice a day, and does it make their life better?" Products that pass this test become infrastructure for how billions organize their lives. The test deliberately sets aside financial projections in favor of fundamental utility, because truly useful products tend to find monetization paths, while products optimized for monetization often fail to create lasting value.

---

## When to Use

- Evaluating whether to build a product or feature
- Assessing an acquisition target
- Prioritizing between product opportunities
- Deciding whether to invest engineering resources
- Filtering moonshot ideas for genuine utility
- User asks "Should we build this?" or "Is this worth pursuing?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| subject | Yes | The product, feature, or acquisition to evaluate |
| target_users | No | Who would use this (default: general population) |
| usage_claim | No | Expected usage frequency if known |
| life_improvement | No | How it claims to make life better |

---

## Core Principle

Larry Page's insight is that the best products solve problems so fundamental that they become part of daily life—like brushing teeth. The test asks two questions: Will people use this at least once or twice a day? Does it genuinely make their lives better? Both must be true. Frequency without improvement creates addiction; improvement without frequency creates forgettable tools. The combination creates products that billions cannot imagine living without.

---

## Methodology

### Phase 1: Subject Definition

**Step 1: Define What Is Being Evaluated**

Clearly articulate:
- What is this product, feature, or acquisition?
- What problem does it solve?
- What is the claimed value proposition?
- Who are the target users?

### Phase 2: Frequency Assessment

**Step 2: Apply the Frequency Test**

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
- Is there natural habit-forming potential?

### Phase 3: Life Improvement Assessment

**Step 3: Apply the Life Improvement Test**

**Question:** Does this genuinely make life better?

| Improvement Type | Assessment |
|------------------|------------|
| Solves real pain point | STRONG PASS |
| Saves meaningful time | PASS |
| Enables previously impossible action | PASS |
| Provides entertainment or joy | PASS (if not exploitative) |
| Convenience only | MARGINAL |
| No clear improvement | FAIL |
| Creates dependency without benefit | FAIL |

**Consider:**
- Would users notice if this disappeared?
- Does it improve life or just fill time?
- Is the improvement genuine or manufactured need?

### Phase 4: Scale Assessment

**Step 4: Calculate Scale Potential**

**Question:** Could this reach billions of users?

| Scale Potential | Assessment |
|-----------------|------------|
| Universal human need | STRONG PASS |
| Large demographic need | PASS |
| Niche but deep need | MARGINAL |
| Limited addressable market | FAIL |

### Phase 5: Verdict

**Step 5: Synthesize and Deliver Verdict**

Combine assessments:
- All PASS or STRONG PASS = Overall PASS
- Any FAIL = Overall FAIL or requires strong justification
- MARGINAL on frequency can be offset by STRONG PASS on improvement (or vice versa)

---

## Output Format

```markdown
## Toothbrush Test: [Subject]

### Subject Definition
**Product/Feature:** [Description]
**Target Users:** [Who]
**Value Proposition:** [Claimed benefit]

### Frequency Assessment
**Expected usage:** [Frequency]
**Verdict:** PASS / MARGINAL / FAIL
**Rationale:** [Why]

### Life Improvement Assessment
**Improvement type:** [Category]
**Verdict:** PASS / MARGINAL / FAIL
**Rationale:** [Why]

### Scale Potential
**Addressable users:** [Estimate]
**Verdict:** PASS / MARGINAL / FAIL
**Rationale:** [Why]

---

### FINAL VERDICT: PASS / MARGINAL / FAIL

**Recommendation:** [Build/acquire, defer, or pass with rationale]

**Key insight:** [One sentence summary]
```

---

## Constraints

- Daily use via exploitation or addiction does not count—improvement must be genuine
- B2B products require adaptation: test for decision-maker engagement and business outcome improvement
- Platform potential should be evaluated separately from core use case
- Financial metrics are deliberately excluded—this tests utility, not monetization
- Single strong criterion can sometimes offset marginal on another, but requires explicit justification
- Already-successful products can still be tested to validate intuition or identify risks

---

## Anti-Patterns to Avoid

**1. Confusing Engagement with Value**
High daily usage does not automatically mean life improvement. Social media feeds are used constantly but may not pass the "makes life genuinely better" test. Both criteria must be evaluated independently.

**2. Manufactured Necessity**
Products designed to create dependency rather than solve existing problems. If the "need" only exists because of the product itself, this is not genuine life improvement.

**3. Niche Excellence Dismissal**
Not every great product must reach billions. A product that fails scale potential but strongly passes frequency and improvement may still be worth building for the right organization.

**4. Financial Projection Substitution**
The test deliberately excludes revenue projections. Saying "this could generate $X revenue" does not address whether it passes the toothbrush test. Utility and monetization are separate questions.

**5. Acqui-hire Rationalization**
Using the toothbrush test to justify acquisitions that are really about talent or technology, not the product itself. Be honest about what you are actually evaluating.

---

## Examples

### Example 1: Calendar Scheduling App (Strong Pass)

**Situation:** Evaluating acquisition of a company that makes a calendar scheduling app.

**Application:**

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
**Addressable users:** Hundreds of millions to billions
**Verdict:** PASS
**Rationale:** Universal need across professionals, students, families. Not limited to specific demographics.

### FINAL VERDICT: PASS

**Key insight:** Calendar scheduling is infrastructure for how billions organize their lives, not a nice-to-have feature.

---

### Example 2: Photo Filter App (Marginal)

**Situation:** Evaluating whether to acquire a trendy photo filter application.

**Application:**

### Subject Definition
**Product/Feature:** Photo filter and editing app
**Target Users:** Social media users, primarily younger demographics
**Value Proposition:** Make photos look better for sharing

### Frequency Assessment
**Expected usage:** Several times per week for active users, declining over time
**Verdict:** MARGINAL
**Rationale:** Not daily for most users. Usage spikes around events but not routine. Filter trends change, causing usage migration.

### Life Improvement Assessment
**Improvement type:** Entertainment and self-expression
**Verdict:** MARGINAL
**Rationale:** Provides creative outlet and social validation, but not solving a pain point. Users might notice absence briefly but would adapt quickly. Could be replaced by many alternatives.

### Scale Potential
**Addressable users:** Hundreds of millions (social media sharers)
**Verdict:** PASS
**Rationale:** Large addressable market, though not universal.

### FINAL VERDICT: MARGINAL

**Key insight:** Photo filter apps are features, not products. They work best as components of larger platforms rather than standalone acquisitions.

---

### Example 3: Enterprise Security Product (Adapted Pass)

**Situation:** Evaluating B2B security monitoring platform.

**Application:**

### Subject Definition
**Product/Feature:** Real-time security threat monitoring for enterprises
**Target Users:** Security teams, IT administrators
**Value Proposition:** Continuous protection against cyber threats

### Frequency Assessment (Adapted for B2B)
**Expected usage:** Continuous monitoring with daily human interaction
**Verdict:** PASS
**Rationale:** Security dashboards are checked daily by security teams. Alerts require constant attention. The product is infrastructure for security operations.

### Life Improvement Assessment (Adapted for B2B)
**Improvement type:** Enables critical business function, prevents catastrophic outcomes
**Verdict:** STRONG PASS
**Rationale:** Security breaches are existential threats. Product prevents outcomes that would devastate organizations. Clear, measurable value.

### Scale Potential
**Addressable users:** Every organization with digital infrastructure
**Verdict:** PASS
**Rationale:** Universal enterprise need as digitization increases.

### FINAL VERDICT: PASS (B2B Adapted)

**Key insight:** For B2B, adapt the test: daily engagement by decision-makers plus genuine business outcome improvement equals pass.

---

## Integration

This skill is part of the **larry-page** expert methodology.

**Works with:**
- `tenx-thinking` for products that pass—ask "how could this be 10x better?"
- `moonshot-evaluator` for high-pass results that may qualify for moonshot investment
- `asymmetric-bet-sizing` for portfolio decisions informed by toothbrush assessments

**When to prefer this skill:**
- Early-stage product evaluation before detailed analysis
- Acquisition screening before due diligence
- Feature prioritization decisions

**Cautions:**
- This is a filter, not a complete analysis—products that pass still require further evaluation
- Does not address competitive position, team quality, or integration potential
- Deliberately ignores financials; those require separate analysis