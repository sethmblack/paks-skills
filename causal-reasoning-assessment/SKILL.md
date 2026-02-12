---
name: causal-reasoning-assessment
description: Apply Yoshua Bengio's framework for distinguishing causal from correlational
  reasoning, assessing whether a system or approach can generalize beyond its training
  distribution.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- causal-reasoning-assessment
- writing
---

# Causal Reasoning Assessment

Apply Yoshua Bengio's framework for distinguishing causal from correlational reasoning, assessing whether a system or approach can generalize beyond its training distribution.

---

## Constraints
- Do NOT claim all ML needs causal reasoning (some tasks are fine with correlation)
- Do NOT dismiss correlational approaches when they are appropriate
- Acknowledge the difficulty of causal discovery
- Do NOT present causal inference as a solved problem

---

## When to Use

- Evaluating whether a model will generalize to new environments
- Analyzing failure modes of ML systems
- Discussing robustness and distribution shift
- Someone confuses prediction with understanding
- Assessing if a system truly "understands" vs pattern matches

**Trigger Phrases:**
- "Will this model work in production?"
- "Why did the model fail on new data?"
- "Does the AI understand [X]?"
- "Is this correlation or causation?"
- "How do we make this robust?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `system_or_claim` | Yes | The ML system, model, or claim to assess |
| `failure_context` | No | Specific failure or distribution shift context |
| `desired_outcome` | No | What generalization is needed |

---

## Workflow

### Step 1: Identify the Causal Question

Distinguish what kind of reasoning is required:

| Question Type | Causal? | Example |
|---------------|---------|---------|
| Prediction (same distribution) | No | "What's the next word?" |
| Intervention | Yes | "If we change X, what happens to Y?" |
| Counterfactual | Yes | "What would have happened if...?" |
| Transfer | Yes | "Will this work in a new environment?" |

**Key Insight:** "Correlation-based learning is fine for prediction within the training distribution. But the moment you need to answer 'what if' questions or deploy to new environments, you need causal structure."

### Step 2: Apply the Umbrella-Wet Streets Test

Use Bengio's canonical example to illustrate the distinction:

**Correlational Learning:**
- Observes: Umbrellas appear when streets are wet
- Might conclude: Umbrellas cause wet streets
- Failure mode: Predicts sprinklers would dry streets if umbrellas are removed

**Causal Learning:**
- Understands: Rain causes both umbrellas and wet streets
- Can answer: "If we intervene on umbrellas (ban them), streets still get wet"
- Robust to: Changes in umbrella usage patterns

**For the system being assessed:**
"What is the 'umbrella' in this system? What correlation might be mistaken for causation?"

### Step 3: Assess Distribution Shift Vulnerability

Identify potential distribution shifts that would break correlational learning:

| Shift Type | Description | Example |
|------------|-------------|---------|
| Covariate Shift | Input distribution changes | Different demographics in deployment |
| Label Shift | Outcome distribution changes | Disease prevalence varies by region |
| Concept Drift | Relationships change over time | User behavior evolves |
| Domain Shift | Entirely new environment | Lab model deployed in field |

**Assessment Question:** "What assumptions about the training distribution is this model implicitly making? When would those assumptions break?"

### Step 4: Check for Spurious Correlations

Identify features that correlate in training but are not causally relevant:

**Common Patterns:**
- Background features (grass in cow images)
- Demographic proxies (zip code for income)
- Temporal confounds (time-of-day effects)
- Dataset artifacts (annotation patterns)

**For the system:** "What features might be spuriously correlated with the target?"

### Step 5: Recommend Causal Approaches (if appropriate)

If causal reasoning is needed, suggest:

| Approach | When to Use | Limitation |
|----------|-------------|------------|
| Invariant Risk Minimization | Multiple training environments | Requires environment labels |
| Causal Discovery | Understand causal structure | Assumptions often violated |
| Intervention Data | Verify causal claims | Expensive to collect |
| Domain Randomization | Simulation-to-real transfer | May not cover real distribution |

**Key Quote Context:** "Causality is very important for the next steps of progress of machine learning. Neural nets learn correlations but not causal structure - this limits imagination, reasoning, planning, and transfer."

---

## Output Format

```markdown
## Causal Assessment: [System/Claim]

### Reasoning Type Required
[Prediction/Intervention/Counterfactual/Transfer]

### Correlation vs. Causation Analysis
[Apply umbrella test to this specific case]

### Distribution Shift Vulnerabilities
[List potential failure modes]

### Spurious Correlation Risks
[Identify non-causal features that might be exploited]

### Recommendation
[Whether causal reasoning is needed; suggested approaches]
```

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

**Input:** "We trained a model to predict customer churn. It works great on our test set but performs poorly on new customers."

**Output:**
"## Causal Assessment: Customer Churn Prediction

### Reasoning Type Required
This is a **transfer problem** - you need the model to work on new customers (new distribution), not just predict within the training population.

### Correlation vs. Causation Analysis
The umbrella test here: Your model may have learned that customers who don't use feature X churn. But is low feature usage causing churn, or is something else (perhaps poor onboarding) causing both? If you intervene to push feature X usage, you might not reduce churn if the causal relationship runs differently.

### Distribution Shift Vulnerabilities
- **Temporal shift:** Customer behavior and market conditions change over time
- **Acquisition channel shift:** New customers may come from different sources with different characteristics
- **Product changes:** Features that predicted churn historically may no longer apply after product updates

### Spurious Correlation Risks
Your model might be learning:
- Demographic proxies that don't generalize
- Time-of-signup patterns that are artifacts of marketing campaigns
- Support ticket patterns that reflect support capacity, not customer satisfaction

### Recommendation
Correlation-based churn prediction has fundamental limits for new populations. Consider:
1. Identifying causal features through A/B tests or instrumental variables
2. Using invariance-based methods if you have data from multiple time periods or channels
3. Being explicit about which features are causal vs. predictive proxies
4. Monitoring for distribution shift in deployment and retraining accordingly"

---

## Integration

This skill integrates with the Yoshua Bengio expert voice. When invoked, maintain:

- Mathematical precision about what causal inference requires
- Honest acknowledgment that causal discovery is hard
- Connection to out-of-distribution generalization research
- Practical recommendations, not just theory

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Task doesn't need causal reasoning | Note that correlational approaches may be sufficient here |
| No distribution shift expected | Recommend monitoring but acknowledge simpler approaches may work |
| Requests causal discovery tutorial | Provide overview; refer to Scholkopf, Pearl, or specialized resources |