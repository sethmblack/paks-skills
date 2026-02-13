---
name: induction-audit
description: Systematically examine any inference from observed data to unobserved cases. Identifies the uniformity assumptions being made, surfaces distributional shift risks, and forces acknowledgment of indu...
license: MIT
metadata:
  version: 1.0.1178
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- induction-audit
- structure
- writing
---

# Induction Audit

Systematically examine any inference from observed data to unobserved cases. Identifies the uniformity assumptions being made, surfaces distributional shift risks, and forces acknowledgment of inductive limits.

---

## When to Use

- User asks "Will this generalize?" or "Is this pattern reliable?"
- Evaluating ML model predictions on new data
- Assessing statistical inferences or trend extrapolations
- Someone claims "the data shows X will continue"
- Policy decisions based on historical patterns
- Any prediction that relies on the future resembling the past
- Request to "audit this inference" or "check these assumptions"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| inference | Yes | The specific prediction or generalization being made |
| observed_data | No | Description of the data/observations the inference is based on |
| target_domain | No | Where the inference is being applied (if different from training) |
| stakes | No | How much depends on the inference being correct |

---

## The Audit Framework

### Phase 1: Identify the Inference

Precisely state what is being inferred from what.

**Questions to ask:**
- "What exactly is being predicted or generalized?"
- "From what specific observations does this inference derive?"
- "What is the gap between observed and unobserved?"

**Goal:** Clear articulation of the inductive leap.

### Phase 2: Surface the Uniformity Assumption

Every inductive inference assumes nature (or the domain) is uniform.

**The Humean Question:**
> "On what grounds do we assume the unobserved will resemble the observed?"

**Questions to ask:**
- "What must remain constant for this inference to hold?"
- "What are we assuming about the similarity between training and deployment?"
- "Is this assumption explicit or hidden?"

**Common uniformity assumptions:**
- Distribution stability (no domain shift)
- Causal mechanism stability (relationships persist)
- Temporal stability (patterns continue)
- Population representativeness (sample generalizes)

### Phase 3: Identify Failure Modes

Where might the uniformity assumption break down?

**Humean insight:**
> "Experience only tells us what has happened, not what will happen."

**Questions to ask:**
- "What would cause this pattern to stop holding?"
- "What distributional shifts are possible?"
- "Are there known regime changes in this domain?"
- "What's the longest similar pattern that eventually broke?"

**Common failure modes:**
- Distribution shift (new data differs from training)
- Confounding variables change
- Selection bias in original data
- Regime changes (new rules apply)
- Black swan events

### Phase 4: Assess Justification Quality

How good is the available justification for this inference?

**Important:** Hume showed we cannot *rationally* justify induction without circularity. But some inductive practices are better supported than others.

**Questions to ask:**
- "How uniform is the past experience?"
- "How large and representative is the sample?"
- "Is there theoretical backing for why the pattern should persist?"
- "What is the base rate of similar inferences failing?"

### Phase 5: Calibrate Confidence

Recommend appropriate confidence level.

**The Maxim:**
> "A wise man proportions his belief to the evidence."

**Confidence factors:**
- Uniformity of past experience
- Domain similarity
- Theoretical support
- Stakes of being wrong
- Time horizon of prediction

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
## Induction Audit: [The Inference]

### The Inference Under Examination
**Prediction/Generalization:** [State precisely what is being inferred]
**Based On:** [What observations support this]
**Applied To:** [Where the inference will be used]

### Uniformity Assumptions Identified

1. **[Assumption 1]:** [Description]
   - Explicit or hidden: [E/H]
   - Testability: [Can this assumption be checked?]

2. **[Assumption 2]:** [Description]
   - Explicit or hidden: [E/H]
   - Testability: [Can this assumption be checked?]

### Failure Modes

**High Risk:**
- [Scenario where inference fails catastrophically]

**Medium Risk:**
- [Scenario where inference partially fails]

**Low Risk:**
- [Scenario where inference degrades gradually]

### Justification Assessment

| Factor | Rating | Notes |
|--------|--------|-------|
| Sample uniformity | Strong/Moderate/Weak | [Explanation] |
| Domain similarity | Strong/Moderate/Weak | [Explanation] |
| Theoretical backing | Strong/Moderate/Weak | [Explanation] |
| Historical reliability | Strong/Moderate/Weak | [Explanation] |

### Recommended Confidence

**Level:** HIGH / MODERATE / LOW / VERY LOW

**Rationale:**
[Why this confidence level is appropriate]

### Mitigation Recommendations

1. [How to hedge against failure mode 1]
2. [How to monitor assumption 1]
3. [What would update your confidence]

*"We have no reason to draw any inference concerning any object beyond those of which we have had experience." — David Hume*
```

---

## Special Cases

### Machine Learning Models

For ML model generalization:
- Training distribution vs. deployment distribution
- Inductive bias of the model architecture
- No Free Lunch theorem implications
- Cross-validation as partial check (not guarantee)

### Statistical Inference

For statistical predictions:
- Population representativeness
- Confidence interval interpretation (frequentist assumptions)
- Prior sensitivity (Bayesian assumptions)
- Multiple testing corrections

### Historical/Trend Extrapolation

For historical patterns:
- Regime change risk
- Survivorship bias in historical data
- Base rate of similar trends reversing
- Structural vs. cyclical patterns

---

## Constraints

- Do not claim induction is invalid—we must use it; the question is how carefully
- Acknowledge that some inductive practices are better than others
- Distinguish between the philosophical problem and practical reliability
- Remember Hume's resolution: custom guides us where reason cannot
- Harsh criticism should match high stakes

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

**Input:** "Our ML model achieves 94% accuracy on test data. We're deploying it to production next month."

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


## Induction Audit: ML Model Deployment

### The Inference Under Examination
**Prediction:** Model will maintain ~94% accuracy in production
**Based On:** Performance on held-out test set
**Applied To:** Production environment next month

### Uniformity Assumptions Identified

1. **Distribution Stability:** Production data will resemble test data
   - Explicit or hidden: Often hidden
   - Testability: Monitor production distributions

2. **Temporal Stability:** Patterns learned remain valid over time
   - Explicit or hidden: Hidden
   - Testability: Track performance over time

3. **Feature Availability:** Same features available in production
   - Explicit or hidden: Sometimes explicit
   - Testability: Audit pipeline

4. **Label Consistency:** What counts as positive/negative remains constant
   - Explicit or hidden: Hidden
   - Testability: Check labeling guidelines

### Failure Modes

**High Risk:**
- Distribution shift from test to production (different user populations, seasonality, new edge cases)
- Data pipeline differences (preprocessing mismatches)

**Medium Risk:**
- Gradual concept drift over time
- Adversarial adaptation (users learn to game the model)

**Low Risk:**
- Minor accuracy degradation within acceptable bounds

### Justification Assessment

| Factor | Rating | Notes |
|--------|--------|-------|
| Sample uniformity | Unknown | How was test set constructed? Representative of production? |
| Domain similarity | Unknown | Is production environment identical to development? |
| Theoretical backing | Moderate | Depends on problem type and model choice |
| Historical reliability | Unknown | Has similar deployment worked before? |

### Recommended Confidence

**Level:** MODERATE (pending additional information)

**Rationale:**
94% test accuracy is encouraging but tells us nothing about production generalization. The fundamental Humean problem applies: test performance guarantees nothing about future performance. Need more information about test set construction and production similarity.

### Mitigation Recommendations

1. Compare test and production data distributions before deployment
2. Implement real-time performance monitoring with alerting
3. Run shadow mode before full deployment
4. Establish rollback criteria and procedures
5. Define "acceptable performance" and check frequently

*"We have no reason to draw any inference concerning any object beyond those of which we have had experience." — David Hume*

---

## Integration

This skill is part of the **David Hume** expert persona. Use it to audit any inductive inference. It pairs well with:
- **causation-examination** when the inference involves causal claims
- **mitigated-skepticism** for calibrating how critical to be
- **impression-tracing** when the terms in the inference need clarification

---