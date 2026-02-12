---
name: counterfactual-reasoning
description: Answer "What would have happened if...?" questions by computing counterfactuals from a structural causal model. This is the highest rung of causal reasoning, enabling attribution, regret analysis, and moral/legal responsibility determination.
version: 1.0.0
author: sethmblack
tags: [counterfactual-reasoning, writing]
---

# Counterfactual Reasoning

Answer "What would have happened if...?" questions by computing counterfactuals from a structural causal model. This is the highest rung of causal reasoning, enabling attribution, regret analysis, and moral/legal responsibility determination.

---

## When to Use

- Questions about what would have happened under different circumstances
- Attribution: "Did X cause Y in this specific case?"
- Responsibility: "Who/what is responsible for this outcome?"
- Regret analysis: "Should we have done differently?"
- Legal causation: "Would the harm have occurred anyway?"
- Individual treatment effects: "Would this person have responded to treatment?"
- Explanation: "Why did this happen?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| counterfactual_question | Yes | The "what if" question to answer |
| causal_model | Yes | Structural causal model or causal diagram with assumptions |
| observed_facts | Yes | What actually happened in the case |
| functional_assumptions | No | Assumed forms of causal mechanisms |

---

## The Counterfactual Framework

### Understanding Counterfactuals

A counterfactual asks: "Given what actually happened, what would have happened if something had been different?"

**Notation:**
- Y_x: The value Y would have taken had X been set to x
- P(Y_x = y | X = x', Y = y'): Probability Y would have been y under intervention x, given we observed x' and y'

**Key distinction from intervention:**
- Intervention (Rung 2): P(Y | do(X=x)) - What happens on average if we set X
- Counterfactual (Rung 3): P(Y_x | X=x', Y=y') - What would have happened for this specific unit

### The Three-Step Counterfactual Algorithm

#### Step 1: Abduction (Update Background)

Use the observed evidence to infer the values of exogenous variables U.

**Process:**
- Start with prior distribution over U
- Condition on what was observed (X=x', Y=y', other evidence)
- Obtain posterior distribution P(U | evidence)

**Intuition:** Figure out what "kind of unit" this is based on what we observed.

#### Step 2: Action (Intervene)

Modify the structural equations to implement the hypothetical intervention.

**Process:**
- Replace the equation for X with X := x (the counterfactual value)
- Keep all other structural equations unchanged
- Keep the U values from Step 1

**Intuition:** In an alternate world, change only what the counterfactual specifies.

#### Step 3: Prediction (Compute)

Use the modified model with the abduced U values to compute the counterfactual outcome.

**Process:**
- Propagate the intervention through the causal mechanisms
- Compute Y_x given the U values from abduction
- Report P(Y_x | evidence)

**Intuition:** See what Y would have been in this alternate world.

---

## Structural Causal Model Requirements

### Components Needed

**Structural equations:** Y = f(X, U_Y)
- Specify how each variable is determined by its causes
- U represents unobserved factors

**Exogenous distributions:** P(U)
- Prior distribution over background factors

**Graph structure:** DAG implied by equations
- Which variables cause which

### Level of Knowledge Required

| Knowledge Level | What You Can Compute |
|-----------------|---------------------|
| Graph only | Interventional queries (Rung 2) |
| Graph + functional forms | Counterfactuals for all units |
| Graph + distributional assumptions | Bounds on counterfactuals |
| Specific U values | Exact counterfactual for this unit |

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
## Counterfactual Analysis: [Question]

### The Question
**Counterfactual query:** [Precise statement of what's being asked]
**In notation:** P(Y_x | observed evidence)

### Observed Facts
| Variable | Observed Value | Meaning |
|----------|----------------|---------|
| [Var 1] | [Value] | [Interpretation] |
| [Var 2] | [Value] | [Interpretation] |

### Causal Model

**Structural Equations:**
```
[Equations showing causal mechanisms]
```

**Graph:**
```
[DAG representation]
```

### Step 1: Abduction

**Prior beliefs about U:**
[What we initially assumed about background factors]

**Conditioning on evidence:**
[How the observed facts update our beliefs]

**Posterior inference:**
[What we now believe about U given the evidence]

### Step 2: Action

**Original equation for [treatment variable]:**
[Original structural equation]

**Modified equation (intervention):**
[Treatment variable] := [counterfactual value]

**Other equations unchanged:**
[List unchanged equations]

### Step 3: Prediction

**Computing the counterfactual outcome:**
[Show the propagation through the model]

**Result:**
[The counterfactual answer]

### Interpretation

**In plain language:**
[What this means for the specific question]

**Confidence and limitations:**
[What assumptions this depends on, sensitivity]

**Practical implications:**
[What follows from this analysis]
```

---

## Common Counterfactual Questions

### Causes of Effects (Attribution)

**Question:** "Did X cause Y in this case?"
**Approach:** Compare factual Y with counterfactual Y_x' (what Y would have been without X)

**Probability of Causation:**
- **PN (Probability of Necessity):** P(Y_x' = 0 | X = 1, Y = 1)
  - "Would Y not have happened without X?"
- **PS (Probability of Sufficiency):** P(Y_x = 1 | X = 0, Y = 0)
  - "Would X have caused Y if X had occurred?"
- **PNS:** P(Y_x = 1, Y_x' = 0)
  - "Would X cause Y and would Y not occur without X?"

### Treatment on the Treated

**Question:** "What was the effect of treatment on those who received it?"
**Formula:** E[Y_1 - Y_0 | X = 1]
**Distinction:** Different from ATE (average treatment effect on everyone)

### Regret Analysis

**Question:** "Should we have made a different decision?"
**Approach:** Compare actual outcome with counterfactual outcome under alternative decision

### But-For Causation (Legal)

**Question:** "But for the defendant's action, would the harm have occurred?"
**Legal standard:** If P(Y_x' = harm) is low, then X was a but-for cause

---

## Example Types

### Binary Example

**Setup:**
- X = 1 (patient took drug), Y = 1 (patient died)
- Model: Y = X*U + (1-X)*V, where U = effect if treated, V = effect if untreated

**Question:** "Would the patient have survived if she hadn't taken the drug?"

**Abduction:** Given Y=1 and X=1, we know U=1 (she died with treatment). V is unknown but we have prior beliefs.

**Action:** Set X := 0

**Prediction:** Y_0 = 0*U + (1-0)*V = V. Result depends on V distribution.

### Continuous Example

**Setup:**
- X = years of education, Y = income, U = ability
- Model: Y = 2X + 3U + noise

**Question:** "What would this person's income have been with 2 more years of education?"

**Abduction:** From observed (X, Y), infer U

**Action:** Set X := X + 2

**Prediction:** Y' = 2(X+2) + 3U + noise = Y + 4

---

## Constraints and Limitations

### What Counterfactuals Require

- Structural model (not just causal diagram)
- Assumptions about functional forms or bounds
- Willingness to reason about unobservable scenarios

### What Counterfactuals Cannot Do

- Prove what definitely happened (they give probabilities)
- Be computed from data alone without model assumptions
- Be verified empirically (the counterfactual didn't happen)

### Sensitivity to Assumptions

- Counterfactual conclusions depend on:
  - Correctness of causal structure
  - Assumed functional forms
  - Distribution of unmeasured factors
- Always report sensitivity to key assumptions

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No structural model provided | Request model or state assumptions needed |
| Insufficient observed facts | Identify what additional evidence would help |
| Model underdetermined | Provide bounds rather than point estimates |
| Question is actually Rung 1 or 2 | Redirect to appropriate analysis |
| Causal structure uncertain | Analyze under multiple possible models |

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

**Input:**
- Question: "A patient took a new drug and died. Would she have died anyway without the drug?"
- Observed: Patient took drug (X=1), patient died (Y=1), patient was high-risk (Z=1)
- Model: We know the drug helps 80% of high-risk patients but harms 10%

**Output:**

## Counterfactual Analysis: Drug and Patient Death

### The Question
**Counterfactual query:** Would this patient have survived if she had not taken the drug?
**In notation:** P(Y_0 = 0 | X = 1, Y = 1, Z = 1)

### Observed Facts
| Variable | Observed Value | Meaning |
|----------|----------------|---------|
| X (Treatment) | 1 (took drug) | Patient received the drug |
| Y (Outcome) | 1 (died) | Patient died |
| Z (Risk) | 1 (high-risk) | Patient was in high-risk category |

### Causal Model

**Structural Equations:**
```
Z = U_Z (exogenous risk status)
X = treatment decision (observed)
Y = f(X, Z, U_Y)

Where U_Y encodes individual response type:
- "Helped by drug": Y_1=0, Y_0=1 (survives with drug, dies without)
- "Harmed by drug": Y_1=1, Y_0=0 (dies with drug, survives without)
- "Always dies": Y_1=1, Y_0=1 (dies regardless)
- "Never dies": Y_1=0, Y_0=0 (survives regardless)
```

**Population distribution (high-risk patients):**
- P(Helped) = 0.80
- P(Harmed) = 0.10
- P(Always dies) = 0.08
- P(Never dies) = 0.02

**Graph:**
```
Z ---> Y
       ^
       |
X -----+
```

### Step 1: Abduction

**Prior beliefs about U_Y:**
Among high-risk patients: 80% helped, 10% harmed, 8% always-dies, 2% never-dies

**Conditioning on evidence:**
We observed X=1, Y=1 (took drug and died).

Only two response types are consistent with Y=1 when X=1:
- "Harmed by drug" (Y_1=1): Possible
- "Always dies" (Y_1=1): Possible

We can rule out:
- "Helped by drug" (Y_1=0): Inconsistent with death
- "Never dies" (Y_1=0): Inconsistent with death

**Posterior inference:**
P(Harmed | X=1, Y=1, Z=1) = 0.10 / (0.10 + 0.08) = 0.556
P(Always dies | X=1, Y=1, Z=1) = 0.08 / (0.10 + 0.08) = 0.444

### Step 2: Action

**Original treatment:**
X = 1 (patient took drug)

**Counterfactual intervention:**
X := 0 (suppose patient had NOT taken drug)

**Structural equations under intervention:**
Y_0 = f(X=0, Z=1, U_Y)

### Step 3: Prediction

**Computing Y_0 for each response type:**
- If "Harmed by drug": Y_0 = 0 (would have survived)
- If "Always dies": Y_0 = 1 (would have died anyway)

**Probability of survival without drug:**
P(Y_0 = 0 | X=1, Y=1, Z=1)
= P(Harmed | evidence) × P(Y_0=0 | Harmed)
+ P(Always dies | evidence) × P(Y_0=0 | Always dies)
= 0.556 × 1 + 0.444 × 0
= **0.556 (about 56%)**

### Interpretation

**In plain language:**
Given that this high-risk patient took the drug and died, there is approximately a 56% probability that she would have survived had she not taken the drug. Conversely, there is a 44% probability she would have died regardless.

**This means:**
- The drug more likely harmed this patient than not
- But we cannot be certain - she might have been a "doomed" patient
- The probability that the drug caused her death (Probability of Necessity) is 56%

**Confidence and limitations:**
- This analysis depends critically on the population response type distribution
- If the drug actually harmed more than 10%, the probability of causation increases
- We assumed independence between risk status and response type
- Real clinical decisions require additional factors

**Practical implications:**
- For legal purposes: More probable than not (>50%) that the drug caused death
- For clinical learning: This case suggests possible harm, warrants investigation
- For regulatory purposes: Individual case doesn't override population benefit (80% helped)

**Important caveat:**
While the drug more likely than not caused this patient's death, the drug still benefits the high-risk population overall. Policy decisions should be based on population effects, not individual counterfactuals.

*"The patient died after taking the drug. Would she have died anyway? This is a counterfactual question. It asks about a world that did not happen, and yes, we can answer it - with 56% probability, she would have survived without the drug."*

---

## Integration

This skill is part of the **Judea Pearl** expert persona. It represents the highest rung of causal reasoning. It pairs with:
- **causal-diagram-construction** which provides the structural foundation
- **ladder-classification** which identifies when Rung 3 reasoning is needed
- **confounding-diagnosis** which is prerequisite for identification