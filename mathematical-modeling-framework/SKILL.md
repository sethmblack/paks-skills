---
name: mathematical-modeling-framework
description: Transform qualitative system descriptions into quantitative mathematical models with testable predictions, using Newton's approaches to rate analysis, equilibrium, and scaling.
version: 1.0.0
author: sethmblack
tags: [mathematical-modeling-framework, transformation, writing]
---

# Mathematical Modeling Framework

Transform qualitative system descriptions into quantitative mathematical models with testable predictions, using Newton's approaches to rate analysis, equilibrium, and scaling.

**Token Budget:** ~750 tokens
**Source Expert:** isaac-newton

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Create models intended to deceive or manipulate
- Present speculative models as validated predictions
- Hide uncertainty or limitations of models
- Use models to justify predetermined conclusions without validation

**If asked to create deceptive models:** Refuse explicitly. Models are tools for understanding, not persuasion weapons.

---

## When to Use

- "Model this mathematically"
- "What are the quantitative relationships?"
- "How does this scale?"
- "Predict what will happen if X changes"
- Capacity planning and resource estimation
- Performance analysis and optimization
- Understanding system dynamics and equilibria

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| system_description | Yes | Qualitative description of the system or phenomenon |
| observables | No | What quantities can be measured |
| predictions_needed | No | What the model should be able to predict |

---

## Core Concepts

### Fluxional Thinking (Rate of Change)

Newton asked: What is changing, and at what rate? How does the rate depend on current state?

- **Fluent:** The quantity that changes (queue depth, memory usage, user count)
- **Fluxion:** The rate of change (requests/second, bytes/minute, signups/day)
- **Rate equation:** dQ/dt = f(Q, inputs, time)

### Equilibrium Analysis

Systems tend toward states where opposing forces balance:

- What forces act on the system?
- At what state do forces balance?
- Is equilibrium stable (returns after perturbation) or unstable (diverges)?

### Scaling Laws

How does behavior change with scale?

| Type | Relationship | Example | Concern Level |
|------|--------------|---------|---------------|
| Constant | O(1) | Hash lookup | Ideal |
| Logarithmic | O(log N) | Binary search | Excellent |
| Linear | O(N) | List iteration | Acceptable |
| Linearithmic | O(N log N) | Good sorting | Moderate |
| Quadratic | O(N^2) | Nested loops | Dangerous |
| Exponential | O(2^N) | Combinatorial | Critical |

---

## Workflow
### Step 1: Identify Variables

List all quantities that matter:

| Variable | Symbol | Units | Type |
|----------|--------|-------|------|
| [Name] | [X] | [units] | Input/Output/State |

Types:
- **Input:** Controlled externally (request rate, configuration)
- **Output:** What we want to predict (latency, cost)
- **State:** Internal quantities that change over time (queue depth, connection count)

### Step 2: Establish Rate Equations

For each state variable, write how it changes:

```
d[State]/dt = [inflows] - [outflows]
```

Example: Queue depth changes at rate = (arrival rate) - (service rate)

### Step 3: Find Equilibrium Conditions

Set all rate equations to zero and solve:

```
At equilibrium: d[State]/dt = 0
Therefore: [inflows] = [outflows]
```

Analyze stability: If perturbed from equilibrium, does the system return or diverge?

### Step 4: Determine Scaling Laws

For each key quantity, identify the mathematical relationship:

- List all factors that influence it
- Determine if relationship is additive, multiplicative, or more complex
- Identify the dominant term at large scale

### Step 5: Derive Predictions

From the model, calculate specific predictions:

- If X increases by 2x, what happens to Y?
- At what X value does the system fail?
- What is the maximum sustainable rate?

### Step 6: Specify Validation Method

How will predictions be tested?

- What measurements are needed?
- What accuracy is acceptable?
- What would invalidate the model?

---

## Output Format

```markdown
## Mathematical Model: [System Name]

### Variables

| Variable | Symbol | Units | Type | Description |
|----------|--------|-------|------|-------------|
| [Name] | [X] | [units] | [type] | [what it represents] |

### Rate Equations

**[State Variable 1]:**
```
d[S1]/dt = [expression]
```
*Interpretation:* [Plain English explanation]

### Equilibrium Analysis

**Equilibrium condition:**
[State variable] reaches equilibrium when [condition].

Solving: [mathematical solution]

**Stability:** [Stable/Unstable] because [reasoning]

### Scaling Laws

| Quantity | Scales As | Dominant Factor | Implication |
|----------|-----------|-----------------|-------------|
| [X] | O([f(N)]) | [factor] | [what this means] |

### Predictions

1. **Prediction 1:** If [input change], then [output change]
   *Derivation:* [Brief math]

2. **Prediction 2:** [System limit] occurs when [condition]
   *Derivation:* [Brief math]

### Validation Requirements

- Measure [X] under conditions [Y]
- Model is validated if predictions within [Z]%
- Model is invalidated if [specific failure condition]

### Limitations

- Assumes [assumption 1]
- Does not account for [factor not modeled]
- Valid only for [range of conditions]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| System too complex | Simplify to essential variables, note what's excluded |
| No measurable quantities | Propose proxy measurements or estimation methods |
| Nonlinear relationships | Use piecewise linear approximations or note nonlinearity |
| Stochastic behavior | Add variance/distribution to predictions |
| Model predictions wrong | This is valuable! Identify which assumption failed |

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

**Input:** "Model our API rate limiting system: we allow 100 requests per minute per user, but users often burst and get throttled"

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


## Mathematical Model: API Rate Limiting

### Variables

| Variable | Symbol | Units | Type | Description |
|----------|--------|-------|------|-------------|
| Request rate | r | req/min | Input | Actual user request rate |
| Token bucket | B | tokens | State | Available request tokens |
| Bucket capacity | C | tokens | Constant | Maximum tokens (100) |
| Refill rate | R | tokens/min | Constant | Token replenishment (100) |
| Throttle rate | T | req/min | Output | Requests rejected |

### Rate Equations

**Token bucket:**
```
dB/dt = R - min(r, B)
     = 100 - min(r, B)
```
*Interpretation:* Bucket refills at 100/min, drains at request rate (limited by available tokens).

### Equilibrium Analysis

**Equilibrium condition:**
Bucket reaches steady state when dB/dt = 0.

**Case 1: r <= 100 (under limit)**
- B reaches C (100 tokens)
- No throttling: T = 0

**Case 2: r > 100 (over limit)**
- B reaches 0
- Throttle rate: T = r - 100

**Stability:** Stable - perturbations decay as bucket fills/drains.

### Scaling Laws

| Quantity | Scales As | Dominant Factor | Implication |
|----------|-----------|-----------------|-------------|
| Throttle rate | O(r - R) for r > R | Excess request rate | Linear increase |
| Recovery time | O(C/R) | Bucket capacity | ~1 minute to full |
| Burst capacity | O(C) | Bucket size | 100 requests max burst |

### Predictions

1. **Burst tolerance:** A user at 0 requests can immediately send 100 requests
   *Derivation:* Full bucket = C = 100 tokens available

2. **Steady-state throttle:** A user sending 150 req/min will have 50 req/min rejected
   *Derivation:* T = r - R = 150 - 100 = 50

3. **Recovery after burst:** After emptying bucket, full capacity restored in 1 minute
   *Derivation:* t = C/R = 100/100 = 1 minute

4. **Sustained burst damage:** User sending 200 req/min for 10 minutes loses 1000 requests
   *Derivation:* T * t = (200-100) * 10 = 1000

### Validation Requirements

- Measure actual vs expected throttle rate over 10-minute windows
- Model validated if within 5% of predictions
- Model invalidated if throttling occurs at r < 90 req/min

### Limitations

- Assumes uniform request distribution within minute
- Does not account for request processing time
- Does not model multiple users competing for shared resources

---

## Integration

This skill originates from the **isaac-newton** expert, embodying Newton's approach to mathematical description of natural phenomena. When using this skill:

- Every quantity must have units
- Rate equations describe how things change
- Equilibria reveal system operating points
- Scaling laws predict behavior at limits
- Models are validated by experiment, not argument

---

## Success Criteria

Mathematical model is complete when:

- [ ] All relevant variables identified with units
- [ ] Rate equations capture system dynamics
- [ ] Equilibrium conditions are analyzed
- [ ] Scaling laws are characterized
- [ ] Specific, testable predictions are derived
- [ ] Validation method is specified
- [ ] Limitations are honestly stated