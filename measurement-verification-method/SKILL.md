---
name: measurement-verification-method
description: Ground claims and decisions in measurable evidence, designing appropriate
  metrics and verification processes—following Marie Curie's principle that what cannot
  be measured cannot be known with cert...
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- measurement-verification-method
- writing
---

# Measurement Verification Method

Ground claims and decisions in measurable evidence, designing appropriate metrics and verification processes—following Marie Curie's principle that what cannot be measured cannot be known with certainty.

---

## When to Use

- Evaluating claims that lack supporting evidence
- Designing metrics for a project or goal
- Verifying whether an intervention actually worked
- Moving from opinion to evidence-based decision
- Request for "proof" or "verification" of claims

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| claim | Yes | The assertion, assumption, or belief to verify |
| context | No | Background on the domain or situation |
| available_data | No | What measurements or evidence currently exist |
| constraints | No | Limitations on what can be measured |

---

## The Measurement Methodology

### The Core Insight

Marie Curie's research was built on measurement. When she wanted to know whether other substances besides uranium emitted rays, she did not speculate—she measured. Every compound, one by one, with precise instruments. Only through systematic measurement did knowledge emerge.

**Claims without measurement are speculation. Science begins when we measure.**

### Step 1: Clarify the Claim

State precisely what is being asserted:
- What exactly is the claim?
- What would need to be true for this claim to be correct?
- What would need to be true for this claim to be false?
- Is the claim even measurable?

**Key question:** "What does this claim actually assert, in concrete terms?"

### Step 2: Identify the Measurable Proxy

Determine what can be measured:
- What observable phenomenon corresponds to the claim?
- What metric would indicate truth or falsehood?
- How close is the proxy to the actual claim?
- What distortions might the proxy introduce?

**Curie's method:** Radioactivity couldn't be seen, but its ionizing effect on air could be measured with a piezoelectric electrometer. The proxy (electrical current) reliably indicated the phenomenon (radioactivity).

### Step 3: Design the Measurement

Create a rigorous measurement process:
- What instrument or method will be used?
- What is the precision required?
- What controls are necessary?
- How will bias be minimized?

**Key questions:**
- Can someone else replicate this measurement?
- Would different measurers get the same result?
- Are we measuring what we think we're measuring?

### Step 4: Establish Success Criteria

Define what the measurement results would mean:
- What result would confirm the claim?
- What result would refute the claim?
- What result would be ambiguous?
- What confidence level is required?

**Curie's principle:** Before measuring, know what the results would mean. Don't decide after the fact.

### Step 5: Execute the Measurement

Collect the data systematically:
- Follow the measurement protocol consistently
- Document the process and any deviations
- Record raw data, not just conclusions
- Note anomalies and unexpected observations

### Step 6: Interpret with Humility

Draw conclusions appropriate to the evidence:
- What does the measurement actually show?
- What does it NOT show?
- What uncertainty remains?
- What further measurement would reduce uncertainty?

**Curie's wisdom:** "I never see what has been done; I only see what remains to be done." Measurement reveals truth but also reveals what we still don't know.

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
## Measurement Verification Analysis

### The Claim
[Precise statement of what is being asserted]

### Claim Clarification
- **If true, would mean:** [concrete implication]
- **If false, would mean:** [concrete implication]
- **Measurability assessment:** [Can this be measured? How directly?]

### Measurement Design

**Measurable proxy:** [What observable phenomenon indicates the claim]
**Proxy validity:** [How closely does proxy match actual claim]

**Measurement approach:**
| Element | Specification |
|---------|---------------|
| Metric | [What to measure] |
| Method | [How to measure] |
| Precision | [Required accuracy] |
| Controls | [What to hold constant] |
| Sample | [What/who to measure] |
| Duration | [How long to measure] |

### Success Criteria
| Result | Interpretation |
|--------|----------------|
| [Outcome A] | Claim confirmed because [reason] |
| [Outcome B] | Claim refuted because [reason] |
| [Outcome C] | Inconclusive because [reason] |

### Current Evidence Assessment
**Available data:** [What exists now]
**What it shows:** [Current state of evidence]
**Gaps:** [What's missing]

### Verdict
**Claim status:** [Verified / Refuted / Unverified / Partially Supported]
**Confidence:** [High / Medium / Low]
**Remaining uncertainty:** [What we still don't know]
**Recommended action:** [What to do based on evidence]
```

---

## Constraints

- Do not accept claims without evidence
- Do not reject claims without measurement
- Do not confuse proxy with phenomenon
- Do not overstate certainty beyond what measurement supports
- Acknowledge the limits of what has been measured

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

**Input:** "Our new onboarding flow is better because users say they like it more in surveys."

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


## Measurement Verification Analysis

### The Claim
The new onboarding flow is "better" than the previous flow.

### Claim Clarification
- **If true, would mean:** Users who go through new onboarding have superior outcomes (retention, activation, satisfaction, success)
- **If false, would mean:** New onboarding produces equal or worse outcomes despite positive sentiment
- **Measurability assessment:** "Better" is vague. Must define better at WHAT. Survey sentiment is measurable but is a weak proxy for actual improvement.

### Measurement Design

**Measurable proxies:**

| Proxy | Validity | What It Measures |
|-------|----------|------------------|
| Survey satisfaction | Low | What users SAY they feel |
| Completion rate | Medium | Whether users finish onboarding |
| Time to first value | High | Whether users reach activation faster |
| 7-day retention | High | Whether users return |
| 30-day retention | High | Whether users stick long-term |
| Support tickets | Medium | Whether users are confused |

**Current measurement (surveys):** Measures stated preference, not actual behavior. Users often like things that don't help them, and dislike things that do. Survey satisfaction is necessary but insufficient.

**Recommended measurement approach:**

| Element | Specification |
|---------|---------------|
| Metric | 7-day retention rate, time to first value action |
| Method | A/B test: randomly assign users to old vs. new flow |
| Precision | 95% confidence, detect 5% difference |
| Controls | Same user segments, same time period, same product version |
| Sample | Minimum 1,000 users per variant |
| Duration | 2-4 weeks of enrollment, 30 days of observation |

### Success Criteria
| Result | Interpretation |
|--------|----------------|
| New flow has higher retention AND positive surveys | Claim confirmed—users like it AND it works |
| New flow has higher retention BUT neutral/negative surveys | Claim partially confirmed—works but users don't recognize it |
| New flow has equal retention AND positive surveys | Claim REFUTED—users like it but it's not actually better |
| New flow has lower retention despite positive surveys | Claim strongly refuted—sentiment misleads |

### Current Evidence Assessment
**Available data:** Survey responses showing higher stated satisfaction
**What it shows:** Users SAY they prefer the new flow
**Gaps:** No behavioral measurement. No retention data. No comparison of actual outcomes.

### Verdict
**Claim status:** UNVERIFIED
**Confidence:** Low—current evidence is insufficient
**Remaining uncertainty:** Whether stated preference translates to actual better outcomes
**Recommended action:** Do not conclude "better" based on surveys alone. Implement A/B test measuring retention and activation. Survey data is encouraging but not conclusive.

---

*"To answer this question, I measured. You must do the same. What users say they prefer and what actually serves them may not be the same. Only measurement will tell you."*

---

## Integration

This skill is part of the **Marie Curie** expert persona. Use it when claims are made without sufficient evidence—measurement is the foundation of knowing.