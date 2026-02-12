---
name: worker-investment-analysis
description: Analyze worker and team investment decisions through the lens of strategic value creation rather than cost minimization.
version: 1.0.0
author: sethmblack
tags: [worker-investment-analysis, writing]
---

# Worker Investment Analysis

Analyze worker and team investment decisions through the lens of strategic value creation rather than cost minimization.

**Token Budget:** ~500 tokens
**Origin:** Henry Ford methodology (The $5 Day)

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend worker exploitation disguised as "investment"
- Suggest compensation strategies that violate labor laws or ethical standards
- Apply analysis to justify unfair labor practices
- Ignore worker welfare in pursuit of productivity

**If asked to apply this skill harmfully:** Refuse explicitly. Worker investment serves mutual benefit, not extraction.

---

## When to Use

- Compensation decisions being evaluated as "cost"
- High turnover attributed to "the market"
- Developer experience investments questioned
- User asks "Are we paying/investing enough?"
- Retention strategy needed
- Training budget discussions

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| context | Yes | The team, role, or workforce being analyzed |
| current_investment | No | Current compensation, training, tooling levels |
| turnover_data | No | Current turnover rate and costs |
| productivity_metrics | No | Output measures if available |

---

## Workflow

### Step 1: Calculate True Turnover Cost

Turnover costs include:
- Recruiting (job posts, interviews, screening)
- Onboarding (training time, reduced productivity)
- Lost knowledge (institutional, relationship, context)
- Team disruption (coverage, morale, workload)

**Rule of thumb:** Replace a skilled worker costs 50-200% of annual salary.

### Step 2: Assess Current Investment Position

| Dimension | Question |
|-----------|----------|
| Compensation | Where does pay sit vs. market? |
| Tools & Environment | How much friction in daily work? |
| Growth & Training | What opportunities for development? |
| Work Conditions | Hours, flexibility, culture? |

### Step 3: Apply the Ford Test

Ford's insight: Workers are also customers (of employment), and their quality affects your product.

- Are you creating workers who advocate for you?
- Would they choose to work here again?
- Does your investment create a competitive advantage?

### Step 4: Model Investment Scenarios

Calculate ROI of investment increases:

| Scenario | Investment | Expected Impact | Net |
|----------|------------|-----------------|-----|
| Current | $X | Baseline | $0 |
| +10% comp | $X + Y | -Z% turnover | $A |
| +DX tooling | $X + Z | +W% productivity | $B |

### Step 5: Identify Strategic Opportunities

Where can investment create asymmetric advantage?
- Areas competitors under-invest
- Capabilities hard to replicate
- Multipliers across the workforce

---

## Outputs

Format the analysis as:

```markdown
## Worker Investment Analysis: [Context]

### Turnover Cost Calculation

| Component | Cost Estimate |
|-----------|---------------|
| Recruiting | $[X] |
| Onboarding | $[Y] |
| Lost productivity | $[Z] |
| Knowledge loss | $[A] |
| **Total per departure** | **$[Total]** |

At current turnover rate ([X%]): **$[Annual cost]** per year

### Current Investment Position

| Dimension | Current State | Market Position |
|-----------|---------------|-----------------|
| Compensation | $[X] | [Below/At/Above] market |
| Tooling | [Description] | [Poor/Average/Excellent] |
| Development | [Description] | [Limited/Average/Strong] |

### Investment Scenarios

| Scenario | Annual Cost | Expected Benefit | ROI |
|----------|-------------|------------------|-----|
| [Scenario 1] | $[X] | [Benefit description] | [X%] |
| [Scenario 2] | $[Y] | [Benefit description] | [Y%] |

### Recommendations

1. **[Recommendation]**: [Rationale]
2. **[Recommendation]**: [Rationale]

### Ford Principle Applied

"[Relevant quote or principle]"

[How this analysis embodies $5 day thinking]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No turnover data | Use industry benchmarks; recommend measurement |
| Compensation data unavailable | Focus on non-compensation investments |
| Investment already high | Analyze whether returns are materializing |
| Budget constraints | Prioritize highest-ROI investments |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "Should we invest in better developer tooling?"

**Output excerpt:**
```markdown


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


## Worker Investment Analysis: Developer Tooling

### Current Investment Position

| Dimension | Current State | Market Position |
|-----------|---------------|-----------------|
| Development environments | Local Docker, frequent issues | Below market |
| CI/CD | 45-minute builds | Well below market |
| Observability | Basic logs only | Below market |

### Investment Scenarios

| Scenario | Annual Cost | Expected Benefit | ROI |
|----------|-------------|------------------|-----|
| Cloud dev environments | $36,000 | 30 min/dev/day saved = 3,250 hours | 180% |
| CI/CD optimization | $15,000 | Build time → 10 min, +2 deploys/day | 240% |

### Ford Principle Applied

"I doubled wages to $5 a day and people called me crazy. But now my workers buy Fords."

A developer frustrated by slow builds and broken environments is a developer looking at LinkedIn. The $36,000 for cloud environments isn't a cost—it's insurance against the $150,000 cost of replacing a senior developer. And unlike wage increases, tooling investments compound across every developer.
```

---

## Integration

This skill originated from Henry Ford's methodology. When invoked, channel his voice:
- Workers are investments, not expenses
- Turnover is the most expensive cost you don't see
- Good wages attract good workers who do good work
- Your workers are your first customers