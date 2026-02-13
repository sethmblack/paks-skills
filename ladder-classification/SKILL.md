---
name: ladder-classification
description: Classify any question about data or relationships as belonging to Rung 1 (Association), Rung 2 (Intervention), or Rung 3 (Counterfactual) of the Ladder of Causation. This determines what type of an...
license: MIT
metadata:
  version: 1.0.1299
  author: sethmblack
keywords:
- ladder-classification
- observational
- writing
---

# Ladder Classification

Classify any question about data or relationships as belonging to Rung 1 (Association), Rung 2 (Intervention), or Rung 3 (Counterfactual) of the Ladder of Causation. This determines what type of analysis is required and whether available data can answer the question.

---

## When to Use

- User asks a question about data or relationships
- Before running any statistical analysis
- When someone confuses correlation with causation
- User asks "Can my data answer this question?"
- Policy or decision questions that require causal reasoning
- Questions about "what would happen if..."
- Attribution questions ("Did X cause Y?")
- Experimental vs. observational data interpretation

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| question | Yes | The question or claim to classify |
| data_available | No | Description of what data or evidence is available |
| context | No | Background on the situation being analyzed |

---

## The Ladder of Causation

### Rung 1: Association (Seeing)

**Mathematical form:** P(Y|X) - What is Y given that I observed X?

**Characteristics:**
- Purely observational
- No intervention involved
- Asks about correlation, prediction, or conditional probability
- Can be answered from observational data alone

**Key phrases indicating Rung 1:**
- "What is the probability of Y given X?"
- "Do X and Y occur together?"
- "Can I predict Y from X?"
- "What do I see when I observe X?"
- "Is there a correlation between..."

**Examples:**
- "What's the survival rate among patients who took the drug?"
- "Do smokers have higher rates of lung cancer?"
- "Can we predict default from credit score?"

**What it CANNOT answer:**
- Whether the relationship is causal
- What would happen if we intervened
- Whether we should do X to achieve Y

---

### Rung 2: Intervention (Doing)

**Mathematical form:** P(Y|do(X)) - What happens to Y if I actively set X?

**Characteristics:**
- Requires action, not just observation
- Asks about effects of interventions
- Cannot be answered from observational data alone without causal model
- Requires experimental data or causal inference methods

**Key phrases indicating Rung 2:**
- "What happens if I do X?"
- "What is the effect of X on Y?"
- "Should I do X to achieve Y?"
- "If we intervene..."
- "What is the causal effect..."

**Examples:**
- "What happens to survival if we GIVE the drug to patients?"
- "Does smoking CAUSE lung cancer?"
- "Will changing our pricing AFFECT sales?"

**What it requires:**
- A causal model (diagram)
- Either experimental data (RCT) or causal identification from observational data

---

### Rung 3: Counterfactual (Imagining)

**Mathematical form:** P(Y_x | X', Y') - What would Y have been if X had been different, given what actually happened?

**Characteristics:**
- Asks about alternative scenarios that did not occur
- Requires reasoning about specific individuals/cases
- Combines factual evidence with hypothetical intervention
- Highest level of causal reasoning

**Key phrases indicating Rung 3:**
- "What would have happened if..."
- "Would Y have occurred anyway?"
- "Was X the cause of Y in this case?"
- "If only we had done differently..."
- "Who is responsible for..."

**Examples:**
- "Would the patient have died anyway if she hadn't taken the drug?"
- "Did the policy cause the economic recovery, or would it have happened anyway?"
- "Is the company liable for the accident?"

**What it requires:**
- A structural causal model (not just a diagram)
- Knowledge of functional forms or assumptions about them
- Specific facts about the case

---

## Classification Framework

### Step 1: Identify the Core Question

Strip away rhetorical framing to find the essential question:
- What relationship is being asked about?
- Between what variables?
- Is it about observation, action, or alternatives?

### Step 2: Check for Intervention Language

**Does the question involve "doing" or "making happen"?**
- "If we give..." -> Rung 2
- "If we change..." -> Rung 2
- "The effect of implementing..." -> Rung 2

**Or is it purely observational?**
- "Among people who took..." -> Rung 1
- "The correlation between..." -> Rung 1
- "Predicting whether..." -> Rung 1

### Step 3: Check for Counterfactual Language

**Does the question involve alternative histories?**
- "Would have happened..." -> Rung 3
- "If things had been different..." -> Rung 3
- "Was X responsible for..." -> Rung 3

### Step 4: Assess Data Requirements

For each rung:

| Rung | Data Sufficient | Data Insufficient |
|------|-----------------|-------------------|
| 1 | Observational data alone | - |
| 2 | RCT data, or observational + valid causal model | Observational alone |
| 3 | Structural model + case facts | Association or intervention estimates alone |

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
## Ladder Classification: [Question]

### Classification
**Rung:** [1/2/3] - [Association/Intervention/Counterfactual]

### Analysis

**The question being asked:**
[Restate the core question precisely]

**Why this rung:**
[Explain what features indicate this classification]

**Mathematical form:**
[Express in appropriate notation: P(Y|X), P(Y|do(X)), or P(Y_x|...)]

### Data Requirements

**Can available data answer this?**
[Yes/No/Partially]

**What would be needed:**
[Specify what data, model, or assumptions are required]

**Common mistake to avoid:**
[What error might someone make with this question?]

### Recommendations

**If trying to answer from Rung 1 data:**
[What can actually be concluded vs. what cannot]

**To properly answer this question:**
[What analysis or data would be appropriate]

### Reframing Options

**Rung 1 version:** [Observational question that CAN be answered]
**Rung 2 version:** [Interventional question requiring causal model]
**Rung 3 version:** [Counterfactual question requiring structural model]
```

---

## Common Classification Errors

### Asking Rung 2 Questions with Rung 1 Data

**Example:** "People who exercise live longer, so I should exercise."

**Error:** The observation (Rung 1) doesn't prove the intervention (Rung 2) will work. Healthy people might both exercise AND live longer due to a common cause.

### Asking Rung 3 Questions with Rung 2 Data

**Example:** "The drug works on average, so it would have saved this patient."

**Error:** Average treatment effects (Rung 2) don't tell us about specific individuals (Rung 3). The patient might have been a non-responder.

### Confusing Prediction with Causation

**Example:** "We can predict crime from neighborhood characteristics, so those characteristics cause crime."

**Error:** Prediction (Rung 1) requires correlation, not causation. The characteristics might be markers, not causes.

---

## Constraints

- Classification determines method, not answer
- A question's rung is inherent; you cannot answer Rung 2 with Rung 1 methods
- Many practical questions are Rung 2/3 but get answered with Rung 1 data (incorrectly)
- Moving up the ladder requires additional assumptions, not just more data
- "Big data" alone cannot climb the ladder; causal models are required

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

**Input:** "Our analysis shows that customers who use our mobile app have 30% higher retention. Should we push all customers to download the app?"

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


## Ladder Classification: App Usage and Retention

### Classification
**Rung:** The question contains TWO levels:
- Observation (Rung 1): "customers who use our mobile app have 30% higher retention"
- Recommendation (Rung 2): "should we push all customers to download"

### Analysis

**The question being asked:**
1. (Stated) App users have higher retention - this is Rung 1, association
2. (Implied) Will making people use the app increase retention - this is Rung 2, intervention

**Why this classification:**
- The observation "customers who use the app have higher retention" is Rung 1 - it describes what we see in the data
- The recommendation "push all customers to download" is about an intervention - it asks what will happen if we DO something
- The speaker is treating a Rung 1 observation as if it answers a Rung 2 question

**Mathematical form:**
- What was measured: P(retention | app usage) - association
- What is being asked: P(retention | do(app usage)) - intervention

### Data Requirements

**Can available data answer this?**
No. The observational data tells us about association, not causation.

**What would be needed:**
- A causal diagram showing what might cause both app usage and retention
- Either an experiment (randomize app promotion) or identification strategy (instrument, regression discontinuity)
- Analysis of confounders (are loyal customers more likely to download the app?)

**Common mistake to avoid:**
Assuming that because app users retain better, making non-users download the app will improve their retention. The correlation might be explained entirely by selection: loyal customers download apps AND stick around, but the app isn't causing the retention.

### Recommendations

**If trying to answer from Rung 1 data:**
You can say: "App usage is associated with higher retention."
You CANNOT say: "Using the app causes higher retention" or "Making customers use the app will improve retention."

**To properly answer this question:**
1. Draw the causal diagram (app usage, retention, customer loyalty, other factors)
2. Identify potential confounders (loyal customers might both download apps and retain)
3. Either run an experiment (randomly promote app to some customers) or find an identification strategy
4. Estimate the causal effect of app usage, not just the association

### Reframing Options

**Rung 1 version:** "Is app usage correlated with retention?"
- Answer: Yes, 30% higher
- This is what the data shows

**Rung 2 version:** "Does using the app cause higher retention?"
- Cannot answer from observational data alone
- Requires experiment or causal identification

**Rung 3 version:** "Would this churned customer have stayed if they had downloaded the app?"
- Even harder - requires structural model and individual-level reasoning

### Bottom Line

The 30% retention difference is real but doesn't support the recommendation. You're observing correlation (Rung 1) but recommending intervention (Rung 2). To bridge that gap, you need causal reasoning - specifically, a model that rules out confounding. Otherwise, you might spend resources pushing app downloads with no retention benefit.

*"Your analysis is stuck on the first rung - association. You're asking 'what do I see?' But your policy question requires the second rung: 'what if I intervene?'"*

---

## Integration

This skill is part of the **Judea Pearl** expert persona. Use it to diagnose questions before analysis. It pairs with:
- **causal-diagram-construction** when a Rung 2 question requires a causal model
- **confounding-diagnosis** to identify what confounders block causal identification
- **counterfactual-reasoning** when Rung 3 questions arise