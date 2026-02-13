---
name: causal-diagram-construction
description: Construct a directed acyclic graph (DAG) representing the causal structure of a problem before any data analysis. The diagram makes assumptions explicit and determines what questions can be answered.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3549
repository: https://github.com/sethmblack/paks-skills
keywords:
- causal-diagram-construction
- observational
- writing
---

# Causal Diagram Construction

Construct a directed acyclic graph (DAG) representing the causal structure of a problem before any data analysis. The diagram makes assumptions explicit and determines what questions can be answered.

---

## When to Use

- User presents a data analysis problem and wants to understand relationships
- Before running any statistical analysis on observational data
- User asks "What causes what?" or "How are these variables related?"
- A/B test interpretation requires understanding of causal structure
- User wants to identify confounders, mediators, or colliders
- Someone confuses correlation with causation and needs clarity
- Research design requires explicit causal assumptions

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| problem_description | Yes | The situation, research question, or relationship to analyze |
| variables | Yes | Key variables of interest (treatment/exposure, outcome, covariates) |
| domain_knowledge | No | What is known about relationships in this domain |
| suspected_relationships | No | Hypotheses about what causes what |

---

## The Causal Diagram Framework

### Step 1: Identify All Relevant Variables

List all variables that might be involved in the causal system:

**Questions to ask:**
- What is the treatment/exposure of interest (X)?
- What is the outcome of interest (Y)?
- What might affect both X and Y (potential confounders)?
- What might be caused by X and cause Y (mediators)?
- What might be affected by both X and other variables (colliders)?
- What background factors set the context (exogenous variables)?

**Important:** Include variables even if unmeasured. The diagram represents the true causal structure, not just measured variables.

### Step 2: Determine Causal Directions

For each pair of related variables, ask:
- Does A cause B, or B cause A, or neither?
- Is there a common cause creating spurious association?
- Is this a definitional relationship or a causal one?

**Key principle:** Causation is asymmetric. If A causes B, then intervening on A changes B, but intervening on B does not change A.

**When uncertain about direction:**
- Consider temporal order (causes precede effects)
- Consider manipulation (can you intervene on A to change B?)
- Consider mechanisms (is there a plausible causal pathway?)

### Step 3: Draw the Graph

Create the directed acyclic graph (DAG):
- Each variable is a node
- Draw an arrow from cause to effect
- No cycles allowed (A cannot cause B which causes A)
- Missing arrows are assertions of non-causation

**Notation:**
```
A -> B       A causes B
A -> M -> B  M mediates A's effect on B
A <- C -> B  C confounds A and B
A -> D <- B  D is a collider
U (dashed)   Unmeasured variable
```

### Step 4: Verify the Structure

Check the diagram for:
- **Completeness:** Are all relevant variables included?
- **Direction correctness:** Does each arrow point from cause to effect?
- **Missing paths:** Are there potential relationships not represented?
- **Impossible structures:** Are there cycles? (If so, reconsider)
- **Testable implications:** What conditional independencies does this imply?

### Step 5: Identify Key Structural Features

Classify paths between treatment (X) and outcome (Y):

**Causal paths (what we want to estimate):**
- Paths where all arrows point from X toward Y
- These transmit the causal effect

**Backdoor paths (confounding):**
- Paths with an arrow into X
- These create spurious association
- Must be blocked for causal identification

**Frontdoor paths (mediation):**
- Causal paths through intermediate variables
- May allow identification via frontdoor criterion

**Collider paths:**
- Paths blocked by colliders
- Conditioning on colliders opens them (bias!)

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
## Causal Diagram: [Problem Description]

### Variables Identified

| Variable | Role | Measured? | Description |
|----------|------|-----------|-------------|
| X | Treatment/Exposure | Yes/No | [What it represents] |
| Y | Outcome | Yes/No | [What it represents] |
| [Var 1] | Confounder/Mediator/Collider | Yes/No | [Description] |
| [Var 2] | Confounder/Mediator/Collider | Yes/No | [Description] |

### Causal Diagram

```
[ASCII or description of the DAG]
```

### Path Analysis

**Causal paths (X to Y):**
1. [Path 1]: X -> ... -> Y
2. [Path 2]: X -> ... -> Y

**Backdoor paths (confounding):**
1. [Path 1]: X <- ... -> Y (blocked by: [variable] / open)
2. [Path 2]: X <- ... -> Y (blocked by: [variable] / open)

**Colliders identified:**
- [Collider variable]: Do not condition on this (would open path)

### Structural Implications

**What we can estimate:**
[Given this structure, what causal effects are identifiable?]

**What we cannot estimate:**
[What would require additional assumptions or data?]

**Critical assumptions:**
[What must be true for this diagram to be correct?]

### Recommendations

[What analysis is appropriate given this structure?]
[What variables should be controlled for?]
[What data would strengthen the analysis?]
```

---

## Key Concepts for Diagram Construction

### Confounders
- Common causes of treatment and outcome
- Create backdoor paths that must be blocked
- Example: Socioeconomic status affects both education and health

### Mediators
- Variables on the causal path between treatment and outcome
- Controlling for mediators removes (part of) the causal effect
- Example: Tar deposits mediate smoking -> lung cancer

### Colliders
- Variables caused by two other variables
- Conditioning on a collider opens a spurious path
- Example: Being in hospital (caused by both disease and accident)

### Selection Bias
- Occurs when analyzing a selected sample
- Often involves conditioning on a collider
- Example: Analyzing only hospitalized patients

---

## Common Diagram Patterns

### Simple Confounding
```
    C
   / \
  v   v
  X   Y
```
C confounds X-Y relationship. Control for C.

### Mediation
```
X -> M -> Y
```
M mediates X's effect on Y. Don't control for M to get total effect.

### Collider Bias
```
X -> D <- Y
```
D is a collider. Never condition on D.

### Unmeasured Confounding
```
    U (unmeasured)
   / \
  v   v
  X   Y
```
Backdoor path through U cannot be blocked by conditioning.

### Frontdoor Pattern
```
    U (unmeasured)
   / \
  v   v
  X   Y
  |   ^
  v   |
  M --+
```
Can identify X->Y effect via M even with unmeasured U.

---

## Constraints

- The diagram represents your assumptions, not discovered truth
- All causal conclusions depend on the diagram being correct
- Unmeasured confounders are common and often undetectable
- No diagram can be proven correct from data alone
- Direction of causation requires domain knowledge, not statistics
- Cycles indicate you need a more sophisticated model (e.g., feedback systems)

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Unclear causal direction | Note uncertainty, consider both possibilities, identify what would distinguish them |
| Cycles present | Indicate time-indexed version or equilibrium model needed |
| Too many variables | Focus on treatment, outcome, and their direct causes first |
| No confounders identified | Question whether this is realistic; most observational settings have confounding |
| All paths blocked | Good news: causal effect may be identifiable. Verify identification conditions |

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

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails | Instead Do |
|--------------|--------------|------------|
| **Diagram-free analysis** | Running statistics without explicit causal assumptions | Draw the diagram first, then determine analysis |
| **Data-driven structure** | Trying to discover causal structure from correlations alone | Use domain knowledge; data cannot prove direction |
| **Missing unmeasured variables** | Diagrams should include all relevant variables, not just measured ones | Include unmeasured confounders with explicit notation |
| **Conditioning on colliders** | Opens spurious paths and creates bias | Identify colliders and never condition on them |
| **Controlling for mediators** | Removes part of the causal effect you're trying to estimate | Control only for confounders, not mediators |

## Example

**Input:** "We found that people who drink coffee have lower rates of depression. Is coffee protective?"

**Output:**

## Causal Diagram: Coffee and Depression

### Variables Identified

| Variable | Role | Measured? | Description |
|----------|------|-----------|-------------|
| Coffee | Exposure | Yes | Daily coffee consumption |
| Depression | Outcome | Yes | Depression diagnosis |
| Energy | Potential Mediator | No | Energy levels and alertness |
| SES | Potential Confounder | Sometimes | Socioeconomic status |
| Genetics | Potential Confounder | Usually No | Genetic predisposition |
| Social Activity | Potential Confounder | Sometimes | Social engagement level |
| Sleep | Potential Confounder/Mediator | Sometimes | Sleep quality |

### Causal Diagram

```
     Genetics         SES        Social Activity
        |              |               |
        v              v               v
    +---+---+      +---+---+      +----+----+
    |       |      |       |      |         |
    v       v      v       v      v         v
  Coffee   Depression <---------+         Sleep
    |         ^                             |
    |         |                             |
    v         |                             v
  Energy -----+----------------------------Depression
```

Simplified version focusing on key paths:
```
        SES
       /   \
      v     v
   Coffee  Depression
      |       ^
      v       |
   Energy ---+
```

### Path Analysis

**Causal paths (Coffee to Depression):**
1. Coffee -> Energy -> Depression (potential protective mechanism)
2. Coffee -> Depression (direct effect, if any)

**Backdoor paths (confounding):**
1. Coffee <- SES -> Depression (OPEN - must control for SES)
2. Coffee <- Genetics -> Depression (OPEN - usually unmeasured)
3. Coffee <- Social Activity -> Depression (OPEN - may be measurable)

**Colliders identified:**
- None in simplified structure

### Structural Implications

**What we can estimate:**
- If SES, social activity, and other confounders are measured and controlled, we can estimate the causal effect of coffee on depression
- However, genetic confounding is likely unmeasured

**What we cannot estimate:**
- The causal effect if genetic confounding exists and is unmeasured
- We would need a natural experiment or instrumental variable

**Critical assumptions:**
- SES captures most socioeconomic confounding
- No reverse causation (depression doesn't cause coffee drinking)
- Energy is a mediator, not a confounder

### Recommendations

Your observed association (coffee drinkers have less depression) likely reflects multiple phenomena:

1. **Possible causal effect:** Coffee may genuinely improve mood via energy/alertness
2. **Likely confounding:** Higher SES enables coffee habit and protects against depression
3. **Possible reverse causation:** Depressed people may drink less coffee (fatigue, anhedonia)

**To analyze this properly:**
- Control for SES, social activity, and other measured confounders
- Acknowledge genetic confounding cannot be controlled
- Consider longitudinal data to address reverse causation
- A randomized trial would be definitive but impractical

**Bottom line:** The association is real, but calling it "protective" requires believing the diagram has no unmeasured confounders. Given the likelihood of genetic confounding, caution is warranted.

*"You cannot analyze this data until you draw the diagram. Once you draw the arrows, the mathematics tells you what you can and cannot conclude."*

---

## Integration

This skill is part of the **Judea Pearl** expert persona. Use it as the first step in any causal analysis. It pairs with:
- **ladder-classification** to determine what type of question is being asked
- **confounding-diagnosis** to analyze the backdoor paths identified
- **counterfactual-reasoning** for "what if" questions after structure is established