---
name: uncertainty-assessment
description: Distinguish genuine uncertainty from calculable risk, and select the appropriate decision-making framework.
license: MIT
metadata:
  version: 1.0.2159
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- uncertainty-assessment
- writing
---

# Uncertainty Assessment

Distinguish genuine uncertainty from calculable risk, and select the appropriate decision-making framework.

---

## When to Use

- Planning for the future when outcomes are unknown
- Deciding how much precision to demand in forecasts
- Evaluating risk models and projections
- Designing systems that must handle the unknown
- User asks "Is this risky or uncertain?" or "Can we calculate the odds?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| situation | Yes | The decision or planning context |
| knowns | Yes | What information is available |
| unknowns | Yes | What cannot be known or predicted |

---

## Keynes's Distinction

John Maynard Keynes, in *A Treatise on Probability* (1921), established a crucial distinction that most people ignore:

### Risk (Calculable)
- Outcomes are unknown but probabilities CAN be estimated
- Historical data provides reliable frequency information
- The system generating outcomes is stable and understood
- Example: Casino games, actuarial tables, quality control

### Uncertainty (Not Calculable)
- Outcomes are unknown AND probabilities CANNOT be meaningfully estimated
- No relevant historical frequency data
- The system is novel, unstable, or poorly understood
- Example: Will this startup succeed? Will there be a war? What technology will dominate in 20 years?

### Keynes's Key Insight
"About these matters there is no scientific basis on which to form any calculable probability whatever. We simply do not know."

Most planning errors come from treating uncertainty as risk - pretending we can calculate what is fundamentally incalculable.

---

## The Assessment Framework

### Step 1: Classify the Unknown

| Question | Risk | Uncertainty |
|----------|------|-------------|
| Do we have relevant historical data? | Yes, stable patterns | No, or patterns are unstable |
| Is the generating system understood? | Yes, mechanism is clear | No, novel or complex |
| Can we run repeated trials? | Yes, or simulate them | No, one-shot decision |
| Are experts' predictions reliable? | Yes, track record exists | No, experts disagree wildly |
| Is the future similar to the past? | Yes, continuity expected | No, regime changes possible |

**If mostly "Risk" answers:** Use expected value calculations, probability models, optimization.

**If mostly "Uncertainty" answers:** Use robustness, resilience, optionality, scenario planning.

### Step 2: Select Appropriate Framework

**For Risk:**
- Calculate expected values
- Optimize for best outcome
- Use diversification to manage variance
- Trust historical patterns

**For Uncertainty:**
- Build resilience to multiple scenarios
- Preserve optionality (don't lock in)
- Focus on downside protection
- Use satisficing over optimizing
- Maintain reserves for the unexpected

### Step 3: Identify Hybrid Situations

Many situations contain both:
- **Near-term**: Often risk-like (more predictable)
- **Long-term**: Often uncertain (compounding unknowns)
- **Core operations**: Often risk-like (established patterns)
- **New ventures**: Often uncertain (novel territory)

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
## Uncertainty Assessment

### Situation
[Brief description]

### Classification: [RISK / UNCERTAINTY / HYBRID]

### Evidence for Classification

**Risk Indicators:**
- [Present / Absent]: [Evidence]

**Uncertainty Indicators:**
- [Present / Absent]: [Evidence]

### Recommended Framework

[Risk-appropriate OR Uncertainty-appropriate OR Hybrid approach]

### Specific Recommendations

1. [Recommendation with rationale]
2. [Recommendation with rationale]
3. [Recommendation with rationale]

### Warning: Common Errors to Avoid

- [Specific error this situation invites]

### The Keynesian Verdict

[Summary in Keynes's voice]
```

---

## Common Errors This Skill Prevents

### False Precision
Producing detailed forecasts for genuinely uncertain situations. A precise number (17.3% probability) feels more scientific than "we don't know," but it's often less honest.

### Model Worship
Trusting models built on historical data when the future may differ structurally. "The model says..." is not an argument when the model's assumptions may not hold.

### Planning Rigidity
Creating detailed plans that assume one scenario when multiple scenarios are possible. Plans optimized for expected outcomes fail catastrophically under unexpected ones.

### Ignoring Fat Tails
Treating extreme outcomes as negligible because they're "unlikely" - but under uncertainty, we don't know how unlikely they are.

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

**Input:** "We're planning our five-year business strategy. Our financial team has built a detailed model projecting revenue growth at 8% annually with 95% confidence intervals."

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


## Uncertainty Assessment

### Situation
Five-year business strategy with detailed financial projections

### Classification: HYBRID (leaning UNCERTAINTY)

### Evidence for Classification

**Risk Indicators:**
- Present: Historical revenue data exists for extrapolation
- Present: Industry averages provide benchmarks
- Absent: Stable competitive environment (technology disruption possible)
- Absent: Reliable 5-year forecasting track record

**Uncertainty Indicators:**
- Present: Five-year horizon compounds unknowns
- Present: Technology and competitive landscape could shift
- Present: Macroeconomic conditions unpredictable
- Present: Customer preferences may evolve unpredictably

### Recommended Framework

Shift from optimization (maximizing expected 8% growth) to resilience (surviving multiple scenarios while capturing upside).

### Specific Recommendations

1. **Scenario planning over point forecasts**: Build strategy that works under 3-4 different futures (strong growth, stagnation, disruption, new opportunity), not just the "expected" one.

2. **Preserve optionality**: Avoid commitments that lock you into one path. The value of flexibility under uncertainty is higher than models suggest.

3. **Stage investments**: Rather than committing fully to the 5-year plan, create decision points where you can reassess as uncertainty resolves.

4. **Stress test for survival**: Ensure the organization survives the pessimistic scenarios, not just thrives in the optimistic ones.

5. **Discount the confidence intervals**: 95% confidence over 5 years assumes stability that likely won't hold. Treat the intervals as illustrative, not predictive.

### Warning: Common Errors to Avoid

- **Don't confuse the model with reality.** The 95% confidence interval is a property of the model, not the world. If the model's assumptions fail, the interval is meaningless.
- **Don't punish people for being wrong about the unknowable.** If forecasts miss due to genuine uncertainty, that's not a forecasting failure - it's the nature of uncertainty.

### The Keynesian Verdict

Your financial team has done what financial teams do - they've translated uncertainty into the familiar language of risk, complete with confidence intervals that suggest knowability. But about matters five years hence, "there is no scientific basis on which to form any calculable probability whatever. We simply do not know."

This doesn't mean planning is useless - it means planning should be robust to our ignorance, not optimized around our guesses. Build a strategy that survives being wrong, not one that requires being right.

---

## Integration

This skill is part of the **John Maynard Keynes** expert persona. Use it to avoid the common error of false precision in an uncertain world.