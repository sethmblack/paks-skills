---
name: confounding-diagnosis
description: Given a causal diagram, identify all backdoor paths creating confounding between treatment and outcome, explain why they produce spurious associations, and determine what variables must be controll...
license: MIT
metadata:
  version: 1.0.630
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- confounding-diagnosis
- observational
- writing
---

# Confounding Diagnosis

Given a causal diagram, identify all backdoor paths creating confounding between treatment and outcome, explain why they produce spurious associations, and determine what variables must be controlled for to identify the causal effect.

---

## When to Use

- After constructing a causal diagram
- When asking "What confounders exist in this relationship?"
- Before running regression or adjustment analysis
- When evaluating research claims from observational data
- Designing a study and deciding what to measure
- User asks "What should I control for?"
- Interpreting why an association might be spurious
- Explaining Simpson's paradox cases

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| causal_diagram | Yes | The DAG showing causal relationships (can be ASCII, description, or image) |
| treatment | Yes | The exposure/intervention variable (X) |
| outcome | Yes | The outcome variable (Y) |
| measured_variables | No | Which variables in the diagram are actually measured |

---

## The Confounding Diagnosis Framework

### Step 1: Identify All Paths Between Treatment and Outcome

List every path connecting X to Y, regardless of arrow direction.

**Types of paths:**
- **Directed paths:** All arrows point from X toward Y (causal)
- **Backdoor paths:** At least one arrow points into X (confounding)

**Finding paths:**
- Start at X, follow any edge (ignore direction)
- Continue until you reach Y
- Record the sequence of variables and arrow directions

### Step 2: Classify Each Path

For each path, determine:

1. **Is it a causal path?**
   - All arrows point away from X toward Y
   - This transmits the causal effect we want to estimate
   - DO NOT block these

2. **Is it a backdoor path?**
   - Has at least one arrow pointing INTO X
   - This creates spurious association (confounding)
   - MUST be blocked for causal identification

3. **Does it contain a collider?**
   - A collider has two arrows pointing INTO it (A -> C <- B)
   - Colliders BLOCK paths by default
   - DO NOT condition on colliders (this opens the path!)

### Step 3: Determine Path Status

For each backdoor path, determine if it is:

**Open:** The path transmits spurious association
- No colliders on the path, OR
- A collider (or its descendant) is conditioned on

**Blocked:** The path does not transmit association
- Contains a non-collider that is conditioned on, OR
- Contains a collider that is not conditioned on

### Step 4: Apply the Backdoor Criterion

A set of variables Z satisfies the backdoor criterion relative to (X, Y) if:
1. Z blocks all backdoor paths between X and Y
2. Z contains no descendants of X

If such a Z exists and is measurable, the causal effect is identifiable:
**P(Y|do(X)) = sum_z P(Y|X,Z) P(Z)**

### Step 5: Identify Valid Adjustment Sets

Find all sets of variables that satisfy the backdoor criterion:

**Minimal sufficient sets:** Smallest sets that block all backdoor paths
**All sufficient sets:** Any combination that works

**Variables to AVOID including:**
- Descendants of treatment (mediators, colliders)
- Variables that open blocked paths when conditioned on
- Instruments (affect treatment but not outcome directly)

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
## Confounding Diagnosis: [Treatment] -> [Outcome]

### Causal Diagram
[Display or describe the diagram]

### Path Analysis

#### Causal Paths (Do Not Block)
| Path | Description |
|------|-------------|
| [Path 1] | X -> ... -> Y (direct/mediated effect) |

#### Backdoor Paths (Must Block)
| Path | Status | Blocked By |
|------|--------|------------|
| [Path 1] | Open/Blocked | [Variable(s)] or "Collider at [V]" |
| [Path 2] | Open/Blocked | [Variable(s)] or "Collider at [V]" |

#### Colliders Identified
| Collider | Path | Warning |
|----------|------|---------|
| [Variable] | [Path] | Do not condition on this |

### Valid Adjustment Sets

**Minimal sufficient sets:**
1. {[Variable(s)]} - blocks [which paths]
2. {[Variable(s)]} - blocks [which paths]

**Variables you MUST NOT control for:**
- [Variable]: [Reason - mediator/collider/descendant]

### Confounding Explanation

[Plain-language explanation of what confounding exists and why]

**Why the naive association is misleading:**
[Explain the specific confounding mechanism]

**What controlling achieves:**
[Explain how adjustment blocks the backdoor paths]

### Practical Recommendations

**If all required variables are measured:**
[Adjustment strategy]

**If key confounders are unmeasured:**
[Implications and alternatives - instrumental variables, bounds, etc.]

**Additional data that would help:**
[What else could be measured to improve identification]
```

---

## Key Confounding Patterns

### Simple Confounding
```
    C
   / \
  v   v
  X   Y
```
- C causes both X and Y
- Backdoor path: X <- C -> Y (open)
- Solution: Control for C

### Chain Confounding
```
A -> B -> X
|         |
v         v
Y <-------+
```
- Multiple variables in confounding path
- Control for any non-collider on the path

### Unmeasured Confounding
```
    U (unmeasured)
   / \
  v   v
  X   Y
```
- Backdoor path cannot be blocked by adjustment
- Requires instrumental variable, bounds, or sensitivity analysis

### M-Bias (Overcontrol)
```
  A     B
   \   /
    v v
     M
    / \
   v   v
   X   Y
```
- M is a collider - path X <- A -> M <- B -> Y is blocked
- Controlling for M OPENS this path (bad!)
- Solution: Do NOT control for M

### Mediation (Not Confounding)
```
X -> M -> Y
```
- M is on causal path, not backdoor
- Controlling for M removes the mediated effect
- Usually do NOT control for mediators (unless estimating direct effect)

---

## Common Diagnostic Errors

### 1. Controlling for Colliders
**Error:** "We should control for everything we measured"
**Problem:** Conditioning on colliders opens blocked paths
**Rule:** Never condition on a variable with two causes on different paths

### 2. Controlling for Mediators
**Error:** "We controlled for intermediate outcomes"
**Problem:** This removes part of the causal effect
**Rule:** Don't control for descendants of treatment unless seeking direct effect

### 3. Missing Unmeasured Confounders
**Error:** "We controlled for everything measured, so causation is established"
**Problem:** Unmeasured confounders may exist
**Rule:** Adjustment only works if diagram is complete

### 4. Table 2 Fallacy
**Error:** Interpreting all coefficients in a regression as causal effects
**Problem:** Each variable has different confounding structure
**Rule:** Each causal question requires its own diagram

---

## Constraints

- Confounding diagnosis depends entirely on the correctness of the diagram
- Unmeasured confounders are common and often plausible
- "Control for everything" is wrong - some variables should NOT be controlled
- Statistical adjustment cannot fix a flawed diagram
- Different adjustment sets may have different statistical properties (precision)

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails | Instead Do |
|--------------|--------------|------------|
| **Control for everything** | Some variables should NOT be controlled (colliders, mediators) | Identify path role of each variable before deciding to control |
| **Conditioning on colliders** | Opens blocked paths, creating spurious associations | Identify colliders explicitly; never condition on them |
| **Controlling for mediators** | Removes part of the causal effect you're trying to estimate | Control only for confounders, not variables on causal path |
| **Assuming diagram is complete** | Unmeasured confounders invalidate adjustment strategy | Explicitly note unmeasured variables; acknowledge limitations |
| **Table 2 fallacy** | Interpreting all regression coefficients as causal effects | Each causal question requires its own diagram and analysis |

---

## Example

**Input:**
- Treatment: Exercise
- Outcome: Heart Disease
- Variables: Age, Diet, Genetics, Social Activity, Fitness Level

**Causal Diagram:**
```
           Genetics
          /   |   \
         v    |    v
        Age   |   Exercise ---> Fitness ---> Heart Disease
         |    v      ^              |              ^
         +--> Diet --+              +--------------+
         |
         +---> Heart Disease

Social Activity --> Exercise
Social Activity --> Heart Disease
```

**Output:**

## Confounding Diagnosis: Exercise -> Heart Disease

### Causal Diagram
```
        Genetics
       /   |   \
      v    v    v
    Age  Diet  Exercise ---> Fitness ---> Heart Disease
     |     |       ^              |              ^
     |     +-------+              +--------------+
     +---------------------------------->  |
                                           |
    Social Activity ---------------------->|
         |                                 |
         +-------> Exercise ---------------+
```

### Path Analysis

#### Causal Paths (Do Not Block)
| Path | Description |
|------|-------------|
| Exercise -> Fitness -> Heart Disease | Mediated effect through fitness |
| Exercise -> Heart Disease | Direct effect (if any) |

#### Backdoor Paths (Must Block)
| Path | Status | Blocked By |
|------|--------|------------|
| Exercise <- Genetics -> Heart Disease | OPEN | Genetics (if measurable) |
| Exercise <- Diet <- Genetics -> Heart Disease | OPEN | Diet or Genetics |
| Exercise <- Social Activity -> Heart Disease | OPEN | Social Activity |
| Exercise <- Age -> Heart Disease | OPEN | Age |
| Exercise <- Diet <- Age -> Heart Disease | OPEN | Age or Diet |

#### Colliders Identified
| Collider | Path | Warning |
|----------|------|---------|
| None in backdoor paths | - | - |

Note: Fitness is NOT a collider - it's a mediator. Do not control for it (unless seeking direct effect only).

### Valid Adjustment Sets

**Minimal sufficient sets:**
1. {Genetics, Social Activity, Age} - blocks all backdoor paths directly
2. {Genetics, Social Activity, Diet} - blocks via Diet instead of Age
3. {Age, Social Activity, Diet} - if Genetics unmeasured, blocks its path via Diet

**Variables you MUST NOT control for:**
- Fitness: Mediator - controlling removes the mediated causal effect
- Any descendant of Exercise would block causal path

### Confounding Explanation

The association between exercise and heart disease is confounded by multiple factors:

1. **Genetics:** People with certain genes are both more inclined to exercise AND have different heart disease risk

2. **Age:** Older people exercise less AND have higher heart disease risk (independent of exercise)

3. **Social Activity:** Socially active people exercise more AND have better health outcomes (social support)

4. **Diet:** Healthy diet correlates with exercise AND independently affects heart disease

**Why the naive association is misleading:**
If we just compare exercisers to non-exercisers, we're also comparing:
- Younger vs older people
- More vs less genetically advantaged people
- More vs less socially active people
- Better vs worse diet habits

The exercise "effect" in raw data includes all these confounding influences.

**What controlling achieves:**
By adjusting for Age, Genetics, Social Activity (and/or Diet), we compare people who are similar on these factors but differ only in exercise. This isolates the causal effect of exercise itself.

### Practical Recommendations

**If all required variables are measured:**
Control for {Age, Social Activity, Genetics} or {Age, Social Activity, Diet}.
Either set blocks all backdoor paths.

**If Genetics is unmeasured (common):**
- Control for {Age, Social Activity, Diet} - Diet partially blocks genetic confounding
- Consider family history as proxy for genetics
- Acknowledge remaining genetic confounding in limitations
- Consider sibling comparison designs

**Additional data that would help:**
- Baseline fitness (before exercise habits established)
- Instrumental variables (e.g., gym proximity)
- Longitudinal data showing exercise changes

**Warning:** Do NOT control for Fitness - this is a mediator through which exercise affects heart disease. Controlling for it would remove the mediated effect and underestimate the total causal effect.

*"There is a backdoor path through Genetics. Unless you block it - by conditioning on Genetics or using the right analysis - you cannot separate the causal effect from the confounding."*

---

## Integration

This skill is part of the **Judea Pearl** expert persona. Use it after constructing a causal diagram. It pairs with:
- **causal-diagram-construction** which must come first
- **ladder-classification** which determines if this Rung 2 analysis is needed
- **counterfactual-reasoning** for Rung 3 questions after identification