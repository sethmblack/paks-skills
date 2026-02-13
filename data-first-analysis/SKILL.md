---
name: data-first-analysis
description: Analyze evidence with crystallographic precision, distinguishing what is demonstrated from what is speculated. Let the data lead rather than confirming preconceptions.
license: MIT
metadata:
  version: 1.0.739
  author: sethmblack
keywords:
- data-first-analysis
- writing
---

# Data-First Analysis

Analyze evidence with crystallographic precision, distinguishing what is demonstrated from what is speculated. Let the data lead rather than confirming preconceptions.

---

## When to Use

- User asks "What does the data actually show?" or "Analyze this evidence"
- Request to interpret results or evaluate claims
- User may be overreaching from limited evidence
- Need to distinguish proof from probability from possibility
- High-stakes decisions that require careful evidence assessment
- User asks "Am I overreaching?" or "Is this conclusion warranted?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| evidence | Yes | The data, observations, or findings to analyze |
| claim | No | The conclusion or claim being considered |
| context | No | Background on the situation, stakes, or audience |

---

## The Data-First Framework

### Step 1: Document the Evidence

Before interpreting, catalog exactly what evidence exists:

- What observations or measurements do we have?
- What is the source and quality of each piece of evidence?
- What are the conditions under which data was collected?
- Are there gaps in the evidence?

**Key question:** What do we actually have, stripped of interpretation?

### Step 2: Identify What is Demonstrated

Evidence that reaches the level of "demonstrated":
- Directly observed, not inferred
- Replicated or replicable
- Robust to different conditions
- Would convince a skeptic

**Test:** Could I defend this claim to someone who examined only the raw evidence?

### Step 3: Identify What is Probable

Conclusions that are likely but not certain:
- Strong inference from demonstrated evidence
- Pattern consistent with evidence but not uniquely explained by it
- Relies on reasonable assumptions

**Test:** What alternative explanations exist? How likely are they?

### Step 4: Identify What is Possible

Conclusions that evidence is consistent with but does not strongly support:
- One of several explanations
- Relies on additional assumptions
- Limited by sample size, scope, or method

**Test:** Is this possible, or merely not ruled out?

### Step 5: Identify What Remains Unknown

Explicitly acknowledge:
- What the evidence does not address
- What further investigation would clarify
- What we cannot determine from current data

**Franklin's principle:** "While the X-ray evidence cannot, at present, be taken as direct proof... other considerations make the existence of a helical structure highly probable."

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
## Data-First Analysis: [Topic]

### Evidence Inventory
| Evidence | Source | Quality | Notes |
|----------|--------|---------|-------|
| [Item 1] | [Where from] | [High/Medium/Low] | [Conditions, caveats] |
| [Item 2] | [Where from] | [High/Medium/Low] | [Conditions, caveats] |

### What is Demonstrated
[Conclusions that can be stated with high confidence based on direct evidence]
- [Conclusion 1]
- [Conclusion 2]

### What is Probable
[Conclusions that are strongly indicated but not proven]
- [Conclusion 1] — [supporting reasoning]
- [Conclusion 2] — [supporting reasoning]

### What is Possible
[Conclusions consistent with evidence but not strongly supported]
- [Possibility 1] — [why it's possible, why it's not certain]
- [Possibility 2] — [why it's possible, why it's not certain]

### What Remains Unknown
- [Unknown 1] — [what evidence would clarify]
- [Unknown 2] — [what evidence would clarify]

### Assessment of [Specific Claim, if provided]
**Verdict:** [Demonstrated / Probable / Possible / Unsupported / Contradicted]
**Appropriate language:** [How to state this claim given the evidence]
**To strengthen:** [What additional evidence would increase confidence]
```

---

## Evidence Quality Indicators

### High Quality
- Direct measurement or observation
- Controlled conditions
- Documented methodology
- Replicated results
- Peer reviewed or independently verified

### Medium Quality
- Indirect observation
- Partially controlled conditions
- Some documentation gaps
- Single observation
- Expert judgment

### Low Quality
- Hearsay or secondhand
- Uncontrolled conditions
- Poor or no documentation
- Contradicted by other evidence
- Potential bias in source

---

## Common Errors to Avoid

1. **Confirmation bias**
   - Finding patterns that match expectations
   - Overlooking contradictory evidence
   - Apply Franklin's method: what would prove me wrong?

2. **Overreach**
   - Claiming certainty when only probability is warranted
   - Stating as demonstrated what is merely suggested
   - Use the tiered framework to calibrate claims

3. **Conflation**
   - Treating correlation as causation
   - Treating consistency as proof
   - Each tier of certainty is distinct

4. **Ignoring alternatives**
   - One explanation is not the only explanation
   - Enumerate alternatives explicitly

5. **Premature closure**
   - Rushing to conclusions before evidence is sufficient
   - What remains unknown deserves explicit acknowledgment

---

## Constraints

- This skill is for interpretation, not for gathering evidence or deciding what to do
- Output should be proportional to evidence quality—less certain conclusions require more hedging
- The framework is rigorous; do not skip tiers or conflate levels of certainty
- When in doubt, err toward caution

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

**Input:** "We ran a customer survey and 85% of respondents said they'd recommend our product. Can we claim we have high customer satisfaction?"

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


## Data-First Analysis: Customer Satisfaction Claim

### Evidence Inventory
| Evidence | Source | Quality | Notes |
|----------|--------|---------|-------|
| 85% recommend rate | Customer survey | Medium | Response rate unknown, sample may be biased |
| Survey methodology | Company internal | Low | No documentation of question wording, sampling |

### What is Demonstrated
- 85% of survey respondents selected the "would recommend" option
- At least some customers have positive sentiment

### What is Probable
- Customers who responded to the survey are generally satisfied — the 85% figure is high enough that even with some positive bias, underlying satisfaction is likely
- The product is not generating widespread dissatisfaction among active users — truly dissatisfied customers often complain even in biased samples

### What is Possible
- Overall customer satisfaction is genuinely high — possible if survey sample is representative
- The 85% figure overstates true satisfaction — possible if only satisfied customers responded
- Satisfaction varies significantly by customer segment — cannot determine from aggregate data

### What Remains Unknown
- Response rate (what percentage of customers completed the survey?)
- Sample composition (who was surveyed? who responded?)
- Comparison to industry benchmarks
- Satisfaction of non-respondents
- Question wording and methodology

### Assessment of "High Customer Satisfaction" Claim
**Verdict:** Probable (for respondents); Possible (for all customers)
**Appropriate language:** "85% of surveyed customers would recommend our product" or "Early customer feedback is strongly positive"
**To strengthen:** Document response rate, compare to benchmark, survey a random sample including inactive customers

---

## Integration

This skill is part of the **Rosalind Franklin** expert persona. Use it when you need rigorous evidence interpretation and want to avoid overreaching from limited data. It pairs well with:
- **experimental-design-framework** for planning how to gather stronger evidence
- **variable-control-analysis** when results seem inconsistent
- **evidence-sufficiency-assessment** for deciding whether to act on conclusions