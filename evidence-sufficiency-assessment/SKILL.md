---
name: evidence-sufficiency-assessment
description: 'Determine whether evidence is sufficient to support a claim before publishing,
  presenting, or deciding. Apply Franklin''s standard of scientific integrity: state
  what is demonstrated, acknowledge wh...'
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- evidence-sufficiency-assessment
- writing
---

# Evidence Sufficiency Assessment

Determine whether evidence is sufficient to support a claim before publishing, presenting, or deciding. Apply Franklin's standard of scientific integrity: state what is demonstrated, acknowledge what remains uncertain.

---

## When to Use

- User asks "Is this enough evidence?" or "Can I make this claim?"
- Before publishing findings or recommendations
- Before presenting conclusions to stakeholders
- Making high-stakes decisions based on available data
- User asks "Should I publish/present/recommend this?"
- Evaluating whether to commit resources based on evidence

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| evidence | Yes | The data, findings, or observations available |
| claim | Yes | The specific conclusion or recommendation being considered |
| stakes | No | Consequences of being wrong, cost of waiting for more evidence |
| audience | No | Who will receive this claim, their expectations |

---

## The Sufficiency Framework

### The Franklin Standard

Rosalind Franklin wrote: "While the X-ray evidence cannot, at present, be taken as direct proof that the structure is helical, other considerations discussed below make the existence of a helical structure highly probable."

This models the standard:
- Distinguish what evidence directly proves from what it strongly suggests
- Explicitly acknowledge what remains uncertain
- Qualify claims appropriately to match evidence strength

### Step 1: Assess Evidence Strength

For each piece of evidence, evaluate:

**Directness:**
- Does it directly demonstrate the claim?
- Or does it require inference, analogy, or assumption?

**Quality:**
- How reliable is the source?
- How rigorous was the collection method?
- Has it been verified or replicated?

**Sufficiency:**
- Does it cover the scope of the claim?
- Are there gaps in the evidence base?
- Could the same evidence support alternative conclusions?

### Step 2: Classify the Claim

Based on evidence strength, classify the claim:

| Level | Meaning | Appropriate Language |
|-------|---------|---------------------|
| **Proof** | Evidence directly demonstrates; no reasonable alternative explanation | "X is [claim]" / "We have demonstrated that..." |
| **Strong evidence** | Highly probable; alternatives are unlikely | "Evidence strongly indicates..." / "The data support the conclusion that..." |
| **Probable** | More likely than not; but alternatives exist | "The evidence suggests..." / "It is likely that..." |
| **Possible** | Consistent with evidence; but not strongly supported | "The evidence is consistent with..." / "It is possible that..." |
| **Insufficient** | Cannot determine; evidence does not adequately address | "Current evidence is insufficient to determine..." |
| **Contradicted** | Evidence points against the claim | "The evidence does not support..." / "Current data contradict..." |

### Step 3: Evaluate Stakes and Standards

The required evidence threshold depends on consequences:

**High stakes (medical, legal, irreversible decisions):**
- Require proof or very strong evidence
- Cost of being wrong is high
- Err toward caution

**Medium stakes (significant resource commitment):**
- Strong evidence or probable is often sufficient
- Balance cost of wrong decision against cost of delay
- Acknowledge uncertainty explicitly

**Low stakes (reversible, low-cost decisions):**
- Possible or even insufficient can justify action
- Cost of waiting may exceed cost of being wrong
- Proceed with monitoring and adjustment

### Step 4: Identify Gaps

Explicitly catalog what would strengthen the claim:

- What additional evidence would increase confidence?
- What would change "probable" to "strong evidence"?
- What would eliminate alternative explanations?
- Is that additional evidence obtainable? At what cost?

### Step 5: Formulate Appropriate Statement

Craft language that accurately represents evidence strength:

**Too strong:** "We have proven that X causes Y" (when evidence only suggests)
**Too weak:** "There might be some indication that possibly X" (when evidence is strong)
**Appropriate:** Match language to classification from Step 2

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
## Evidence Sufficiency Assessment

### The Claim
[Specific statement or recommendation being evaluated]

### Evidence Summary
| Evidence | Strength | Relevance | Limitations |
|----------|----------|-----------|-------------|
| [Evidence 1] | [Direct/Indirect] | [High/Medium/Low] | [Gaps, caveats] |
| [Evidence 2] | [Direct/Indirect] | [High/Medium/Low] | [Gaps, caveats] |

### Sufficiency Classification
**Verdict:** [Proof / Strong Evidence / Probable / Possible / Insufficient / Contradicted]

**Reasoning:**
[Why this classification; what evidence establishes; what remains uncertain]

### Alternative Explanations
[What else could explain the evidence? How likely are alternatives?]

### Stakes Assessment
**If correct:** [Positive outcomes of acting on claim]
**If incorrect:** [Costs of being wrong]
**Cost of delay:** [What is lost by waiting for more evidence]
**Appropriate threshold:** [What level of certainty is needed for this decision]

### Gaps and Strengthening
To increase confidence:
- [Additional evidence 1] would [effect on confidence]
- [Additional evidence 2] would [effect on confidence]

Feasibility: [Can this evidence be obtained? At what cost/time?]

### Recommendation
**Can the claim be made?** [Yes/No/With qualification]

**Appropriate language:**
[Exact phrasing that accurately represents evidence strength]

**If proceeding:**
[What acknowledgments or caveats to include]

**If not proceeding:**
[What additional evidence to gather first]
```

---

## Calibration Guide

### Phrases That Overstate Evidence
Avoid unless evidence reaches "Proof" level:
- "This proves..."
- "We have shown conclusively..."
- "It is certain that..."
- "There is no doubt..."

### Phrases That Understate Evidence
Avoid when evidence is strong:
- "It might be that..."
- "There is some indication..."
- "Possibly..."
- "We cannot rule out..."

### Well-Calibrated Phrases
Match to evidence level:

**Strong evidence:**
- "The evidence strongly supports..."
- "The data indicate..."
- "There is substantial evidence that..."

**Probable:**
- "The evidence suggests..."
- "It is likely that..."
- "Based on available data..."

**Possible:**
- "The evidence is consistent with..."
- "One interpretation is..."
- "It is possible that..."

---

## Constraints

- This skill is for assessing sufficiency, not for gathering evidence or interpreting it
- Different audiences have different expectations; adjust framing for context
- Scientific publication requires higher standards than business decisions
- When in doubt, err toward acknowledging uncertainty

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

**Input:** "We surveyed 50 users and 40 said they'd pay for our premium feature. Can we say there's strong market demand?"

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


## Evidence Sufficiency Assessment

### The Claim
"There is strong market demand for our premium feature"

### Evidence Summary
| Evidence | Strength | Relevance | Limitations |
|----------|----------|-----------|-------------|
| 80% of 50 surveyed users expressed willingness to pay | Indirect | High | Small sample; stated vs. actual behavior |
| Survey methodology | Unknown | Critical | Sample selection, question wording not specified |

### Sufficiency Classification
**Verdict:** Possible

**Reasoning:**
The 80% positive response is encouraging but insufficient to establish "strong market demand" because:
1. Sample size is small (50 users, 95% CI for 80% is approximately 67%-90%)
2. Stated willingness to pay often differs from actual purchase behavior
3. Sample may not represent the broader market (who was surveyed?)
4. "Premium feature" acceptance depends on price point (not tested)

### Alternative Explanations
- Respondents expressed enthusiasm but would not pay at proposed price
- Sample is biased toward power users or early adopters
- Users interpreted "willingness to pay" loosely (e.g., small amount vs. meaningful subscription)
- Social desirability bias (wanting to be supportive)

### Stakes Assessment
**If correct:** Valuable signal to invest in premium feature development
**If incorrect:** Wasted development resources; opportunity cost of other features
**Cost of delay:** Moderate (market window, competitor moves)
**Appropriate threshold:** "Probable" would be sufficient given reversibility of software decisions; "Strong evidence" would be preferred before major investment

### Gaps and Strengthening
To increase confidence:
- Larger sample (n=200+) would narrow confidence interval
- Revealed preference test (pre-orders, waitlist signups) would show actual behavior
- Price sensitivity testing would validate at proposed price point
- Representative sampling would extend beyond current user base

Feasibility: Pre-order test is low-cost and could be done in 2 weeks

### Recommendation
**Can the claim be made?** With significant qualification

**Appropriate language:**
"Early survey data suggest interest in a premium feature, with 80% of 50 surveyed users expressing willingness to pay. This is encouraging but preliminary; stated intent often overstates actual purchase behavior."

**If proceeding with development:**
- Acknowledge this as early signal, not validated demand
- Plan for smaller initial investment with validation gates
- Design a real-market test (waitlist, pre-order) before major commitment

**If seeking validation first:**
- Run pre-order or waitlist test with 500+ target users
- Test at actual proposed price point
- Measure conversion rate, not just stated interest

---

## Integration

This skill is part of the **Rosalind Franklin** expert persona. Use it when you need to decide whether evidence supports action or claims. It pairs well with:
- **data-first-analysis** for interpreting what evidence actually shows
- **experimental-design-framework** for designing tests to gather stronger evidence
- **variable-control-analysis** if evidence quality is compromised by uncontrolled factors