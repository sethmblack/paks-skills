---
name: experimentum-crucis
description: Design crucial experiments that definitively test hypotheses by isolating variables, verifying intrinsic properties, and producing unambiguous results.
license: MIT
metadata:
  version: 1.0.928
  author: sethmblack
keywords:
- experimentum-crucis
- transformation
- writing
---

# Experimentum Crucis

Design crucial experiments that definitively test hypotheses by isolating variables, verifying intrinsic properties, and producing unambiguous results.

**Token Budget:** ~700 tokens
**Source Expert:** isaac-newton

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Design experiments intended to harm users or systems
- Create tests that cannot ethically be conducted
- Propose experiments that would violate privacy or consent
- Design "experiments" intended to confirm a predetermined conclusion

**If asked to design harmful experiments:** Refuse explicitly. Offer alternative approaches that achieve the knowledge goal ethically.

---

## When to Use

- "Design an experiment to test this hypothesis"
- "How do we prove this conclusively?"
- "Isolate the variable causing this behavior"
- "Is this effect intrinsic or introduced by our test?"
- Debugging where multiple factors may be involved
- A/B testing where clean separation matters
- Performance analysis where noise must be eliminated

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| hypothesis | Yes | The claim to test |
| system | Yes | The system or phenomenon to investigate |
| constraints | No | Limitations on what can be modified or measured |

---

## Origin: Newton's Prism Experiments

In 1666, Newton performed his "experimentum crucis" (crucial experiment):

1. **Isolated a single color** by passing white light through a prism, then through a hole to select only blue light
2. **Passed it through a second prism** to test if blue could be further decomposed
3. **Observed it remained pure blue** - color is intrinsic to light, not added by the prism
4. **Reversed the process** - recombining spectral colors produced white light again

This methodology proves properties are intrinsic rather than artifacts of the experimental apparatus.

---

## Workflow

### Step 1: State the Hypothesis Precisely

Convert the vague claim into a testable statement:
- What specific prediction does the hypothesis make?
- What observable outcome would confirm it?
- What observable outcome would refute it?

**Template:** "If [hypothesis] is true, then [observable prediction]. If false, then [alternative observation]."

### Step 2: Identify All Variables

List every factor that could influence the outcome:

| Variable Type | Description | Examples |
|--------------|-------------|----------|
| **Independent** | What you will change | Configuration, input, timing |
| **Dependent** | What you will measure | Response time, error rate, output |
| **Confounding** | What might interfere | Other processes, network, cache |
| **Controlled** | What you will hold constant | Environment, load, version |

### Step 3: Design the Isolation

Create conditions where ONLY the independent variable differs:

**Control condition:** System without the change
**Test condition:** System with ONLY the change

Ensure:
- All confounding variables are eliminated or held constant
- The test apparatus does not introduce the effect being measured
- The measurement does not alter the phenomenon

### Step 4: Verify Intrinsic vs Introduced

Design a check that the observed effect is intrinsic to the change, not an artifact:

- **Reversibility test:** Does removing the change remove the effect?
- **Second transformation:** Does applying the change again produce consistent results?
- **Alternative pathway:** Does achieving the same state via different means produce the same effect?

### Step 5: Define Success Criteria

Specify exactly what constitutes:
- **Confirmation:** What measurement range confirms the hypothesis?
- **Refutation:** What measurement range refutes it?
- **Inconclusive:** What would indicate the experiment failed to isolate variables?

Include:
- Sample size / number of trials
- Statistical significance threshold if applicable
- Edge cases that must be tested

### Step 6: Document the Experimental Protocol

Write step-by-step instructions that another person could follow to replicate the experiment exactly.

---

## Output Format

```markdown
## Experimentum Crucis: [Hypothesis Title]

### Hypothesis
[Precise, testable statement]

### Prediction
- If true: [Observable outcome]
- If false: [Alternative outcome]

### Variables

| Type | Variable | How Controlled |
|------|----------|----------------|
| Independent | [X] | Deliberately varied |
| Dependent | [Y] | Measured precisely |
| Controlled | [Z1, Z2...] | Held constant by [method] |
| Confounding | [C1, C2...] | Eliminated by [method] |

### Experimental Design

**Control Condition:**
[Precise description of baseline]

**Test Condition:**
[Precise description with ONLY the independent variable changed]

### Intrinsic Verification
[How we verify the effect is real, not an artifact]

### Success Criteria
- **Confirmed if:** [Specific measurement threshold]
- **Refuted if:** [Specific measurement threshold]
- **Inconclusive if:** [Conditions indicating isolation failure]

### Protocol
1. [Step 1]
2. [Step 2]
3. [Step N]

### Replication Requirements
[How many times? By whom? Under what conditions?]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Too many confounding variables | Propose staged experiments, isolating one variable at a time |
| Cannot create control condition | Suggest A/B testing, feature flags, or rollback approaches |
| Measurement affects phenomenon | Recommend sampling, logging, or non-intrusive monitoring |
| Effect too small to detect | Calculate required sample size, propose more sensitive metrics |
| Hypothesis not falsifiable | Reformulate to make predictions that could be wrong |

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

**Input:** "Hypothesis: Our caching layer is causing the increased latency under high load"

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


## Experimentum Crucis: Cache-Induced Latency Under Load

### Hypothesis
The caching layer causes latency to increase disproportionately when request rate exceeds 1000 RPS.

### Prediction
- If true: Bypassing the cache at high load will reduce p99 latency
- If false: Bypassing the cache will not significantly change latency, or will increase it

### Variables

| Type | Variable | How Controlled |
|------|----------|----------------|
| Independent | Cache enabled/disabled | Feature flag |
| Dependent | p99 latency (ms) | Measured at load balancer |
| Controlled | Request rate | Fixed at 1200 RPS via load generator |
| Controlled | Request distribution | Same set of requests replayed |
| Confounding | Database load | Isolated read replica for test |
| Confounding | Network variability | Same-region testing only |

### Experimental Design

**Control Condition:**
System at 1200 RPS with cache enabled, standard configuration.

**Test Condition:**
Identical system at 1200 RPS with cache bypassed (requests include `Cache-Control: no-cache`), all other configuration identical.

### Intrinsic Verification
1. **Reversibility:** Re-enable cache, verify latency returns to original level
2. **Consistency:** Repeat test 3 times, verify effect is reproducible
3. **Cache-miss baseline:** Measure at 100 RPS with cache disabled to establish baseline overhead

### Success Criteria
- **Confirmed if:** p99 latency with cache disabled is > 15% lower than with cache enabled
- **Refuted if:** p99 latency is unchanged or higher without cache
- **Inconclusive if:** Latency variance exceeds 20% between trials (indicates uncontrolled variables)

### Protocol
1. Deploy to isolated test environment with dedicated database replica
2. Warm up system for 5 minutes at 500 RPS
3. Measure baseline: 10 minutes at 1200 RPS, cache enabled, record p99
4. Disable cache via feature flag
5. Wait 2 minutes for system to stabilize
6. Measure test: 10 minutes at 1200 RPS, cache disabled, record p99
7. Re-enable cache, measure 5 minutes to verify reversibility
8. Repeat steps 2-7 twice more

### Replication Requirements
3 complete trials. Results valid only if all 3 trials show consistent direction of effect.

---

## Integration

This skill originates from the **isaac-newton** expert, embodying Newton's experimental methodology from Opticks. When using this skill:

- Isolate ruthlessly - one variable at a time
- Verify the effect is intrinsic, not an artifact of testing
- Reversibility is a powerful check
- If the experiment is inconclusive, the problem is the experimental design, not the phenomenon

---

## Success Criteria

Experimentum crucis design is complete when:

- [ ] Hypothesis is precisely stated and falsifiable
- [ ] All variables are identified and classified
- [ ] Control and test conditions differ by exactly one variable
- [ ] Method to verify intrinsic vs introduced effect is specified
- [ ] Success criteria are quantitative and unambiguous
- [ ] Protocol is replicable by others