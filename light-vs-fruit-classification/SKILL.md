---
name: light-vs-fruit-classification
description: Distinguish between "experiments of light" (investigations that illuminate
  causes and build understanding) and "experiments of fruit" (investigations that
  produce useful results). Ensures understan...
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- light-vs.-fruit-classification
- transformation
- writing
---

# Light vs. Fruit Classification

Distinguish between "experiments of light" (investigations that illuminate causes and build understanding) and "experiments of fruit" (investigations that produce useful results). Ensures understanding precedes application and prevents blind optimization.

---

## When to Use

- User asks "Should we investigate or just try things?"
- Team is optimizing without understanding why things work
- Need to decide between research and development approaches
- Something works but nobody knows why
- Pattern of "random success" - hits that can't be repeated
- Request to "classify this investigation" or "what kind of experiment is this?"
- Evaluating an R&D portfolio or research agenda
- Determining whether to pursue understanding or results

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| investigation | Yes | The inquiry, experiment, or project being evaluated |
| current_state | No | What is already known about the domain |
| goals | No | What outcomes are being sought |
| constraints | No | Time, resource, or other limitations |

---

## The Core Distinction

### Experiments of Light (Lucifera)

**Purpose:** To illuminate causes, reveal mechanisms, and build understanding.

**Characteristics:**
- Asks "WHY does this work?" not "DOES this work?"
- Values negative results (they eliminate hypotheses)
- Seeks general principles, not just particular solutions
- May not produce immediately useful outcomes
- Creates knowledge that transfers to other problems

**Examples:**
- Investigating why a successful campaign worked (not just celebrating the success)
- Understanding the mechanism behind a drug effect (not just that it reduces symptoms)
- Studying why some customers churn to understand retention generally

### Experiments of Fruit (Fructifera)

**Purpose:** To produce useful results, solve immediate problems, and create value.

**Characteristics:**
- Asks "DOES this work?" not "WHY does this work?"
- Values positive results (they provide solutions)
- Seeks working solutions, even without understanding
- Produces immediately applicable outcomes
- May not transfer to other contexts

**Examples:**
- A/B testing to find the best headline (without understanding why it works)
- Drug trial to determine efficacy (without mechanism understanding)
- Trying retention tactics to reduce churn (without understanding root cause)

---

## Why Light Must Precede Fruit

Bacon's insight: **Fruit without light is fragile.**

| Without Understanding | Consequence |
|----------------------|-------------|
| Success by luck | Cannot be repeated reliably |
| Optimization without mechanism | Hits local maxima, misses better approaches |
| Solution without diagnosis | Treats symptoms, not causes |
| Working system with unknown principles | Cannot be debugged, adapted, or improved |

**The Maxim:** "Those who seek fruit before light will have neither fruit nor light in the end."

---

## Workflow
### Phase 1: Describe the Investigation

What is being done? What question is being asked? What outcome is sought?

### Phase 2: Apply the Light/Fruit Test

**Light indicators (mark if present):**
- [ ] Primary question is "why" or "how" (not "what" or "whether")
- [ ] Negative results would be valuable (eliminate hypotheses)
- [ ] Goal is transferable understanding
- [ ] Current outcome: building mental models
- [ ] Would publish findings even if they don't solve immediate problem

**Fruit indicators (mark if present):**
- [ ] Primary question is "what works" or "which is better"
- [ ] Only positive results matter
- [ ] Goal is solving this specific problem
- [ ] Current outcome: working solution
- [ ] Findings only matter if they produce immediate value

### Phase 3: Assess Current Understanding

| Understanding Level | Description | Implication |
|--------------------|-------------|-------------|
| **None** | Don't know what works or why | Light desperately needed |
| **Empirical** | Know what works, not why | Light should precede more fruit |
| **Partial** | Some mechanistic understanding | Can pursue both in parallel |
| **Strong** | Clear mental model of domain | Fruit pursuit appropriate |

### Phase 4: Evaluate the Risk

What happens if you pursue fruit without sufficient light?

| Risk | Description |
|------|-------------|
| Fragile success | Solution works but you can't explain or repeat it |
| Local maximum | Optimization finds good-enough, misses great |
| Wrong problem | Efficient solution to misdiagnosed issue |
| Debugging blind | When it breaks, you have no mental model to fix it |
| No transfer | Learning doesn't help adjacent problems |

### Phase 5: Make Recommendation

Based on current understanding level and risks, recommend:

### Step 1: Pursue light (understanding) before fruit



### Step 2: Pursue both in parallel



### Step 3: Pursue fruit (results) with current understanding



---

## Output Format

```markdown
## Light vs. Fruit Classification: [Investigation Name]

### Investigation Summary
**What is being done:** [Description]
**Question being asked:** [The core inquiry]
**Outcome sought:** [What success looks like]

---

### Classification Assessment

**Light Indicators Present:**
- [X] / [ ] Why/how question
- [X] / [ ] Negative results valuable
- [X] / [ ] Transferable understanding sought
- [X] / [ ] Building mental models
- [X] / [ ] Would share findings regardless of outcome

**Fruit Indicators Present:**
- [X] / [ ] What works question
- [X] / [ ] Only positive results matter
- [X] / [ ] Solving specific problem
- [X] / [ ] Working solution sought
- [X] / [ ] Findings only matter if immediately useful

**Classification:** [LIGHT / FRUIT / HYBRID]

---

### Understanding Assessment

**Current Understanding Level:** [None / Empirical / Partial / Strong]

**Evidence:**
- [What is known and not known about this domain]
- [Prior experiments and their results]
- [Existing theories or models]

---

### Risk Analysis

**If pursuing fruit without sufficient light:**

| Risk | Likelihood | Impact | Notes |
|------|-----------|--------|-------|
| Fragile success | [L/M/H] | [L/M/H] | [Explanation] |
| Local maximum | [L/M/H] | [L/M/H] | [Explanation] |
| Wrong problem | [L/M/H] | [L/M/H] | [Explanation] |
| Debugging blind | [L/M/H] | [L/M/H] | [Explanation] |
| No transfer | [L/M/H] | [L/M/H] | [Explanation] |

---

### Recommendation

**Path Forward:** [LIGHT FIRST / FRUIT FIRST / PARALLEL]

**Rationale:**
[Why this path is appropriate given the classification and risks]

**If Light First:**
- [What understanding is needed before pursuing results]
- [How to structure the investigation for illumination]
- [What would indicate sufficient understanding]

**If Fruit First:**
- [Why current understanding is sufficient]
- [What understanding gaps are acceptable]
- [How to capture learning while pursuing results]

**If Parallel:**
- [How to structure both tracks]
- [How findings from each inform the other]
- [Decision point for pivoting to single track]

---

*"Those who have handled sciences have been either men of experiment or men of dogmas. The men of experiment are like the ant, they only collect and use; the reasoners resemble spiders, who make cobwebs out of their own substance. But the bee takes a middle course: it gathers its material from the flowers of the garden and of the field, but transforms and digests it by a power of its own." - Francis Bacon*
```

---

## Constraints

- Do not privilege light over fruit absolutely - both are necessary
- Acknowledge time and resource constraints that may force fruit-first approaches
- Recognize that some domains have more accumulated light than others
- Fruit experiments can accidentally produce light (unexpected findings)
- Light without eventual fruit is sterile - understanding must eventually serve use

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

**Input:** "We're running A/B tests on our checkout flow. Conversion improved 15% but we don't know why."

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


## Light vs. Fruit Classification: Checkout A/B Testing

### Investigation Summary
**What is being done:** A/B testing different checkout flow designs
**Question being asked:** Which checkout flow produces higher conversion?
**Outcome sought:** Higher conversion rate on checkout

---

### Classification Assessment

**Light Indicators Present:**
- [ ] Why/how question - No, asking "which is better"
- [ ] Negative results valuable - No, only winning variants matter
- [ ] Transferable understanding sought - No, solving this specific flow
- [ ] Building mental models - No, optimizing metrics
- [ ] Would share findings regardless of outcome - Unlikely

**Fruit Indicators Present:**
- [X] What works question - Yes, "which variant converts"
- [X] Only positive results matter - Yes, seeking winning variant
- [X] Solving specific problem - Yes, this checkout flow
- [X] Working solution sought - Yes, higher conversion
- [X] Findings only matter if immediately useful - Yes

**Classification:** FRUIT (pure)

---

### Understanding Assessment

**Current Understanding Level:** Empirical

**Evidence:**
- Know that variant B converts 15% better than A
- Do NOT know why (mechanism unclear)
- No theory of what makes checkout flows convert
- Previous tests also found winners without understanding

---

### Risk Analysis

**If continuing fruit without gaining light:**

| Risk | Likelihood | Impact | Notes |
|------|-----------|--------|-------|
| Fragile success | HIGH | MEDIUM | If conditions change, don't know why B worked; can't adapt |
| Local maximum | HIGH | HIGH | May be optimizing the wrong dimension; 15% vs. potential 50% |
| Wrong problem | MEDIUM | HIGH | Checkout friction may not be the real conversion barrier |
| Debugging blind | HIGH | MEDIUM | If conversion drops, no model to diagnose |
| No transfer | HIGH | LOW | Learning doesn't help other conversion problems |

---

### Recommendation

**Path Forward:** LIGHT FIRST (then return to fruit)

**Rationale:**
Current approach produces wins but no understanding. The 15% improvement is real but fragile - you cannot explain it, repeat it intentionally, or transfer the learning. Before more A/B testing, invest in understanding WHY variant B works.

**Specific Light-Seeking Actions:**

1. **User research:** Interview customers who completed checkout with variant B. What did they notice? What almost made them abandon?

2. **Session recordings:** Watch actual checkout sessions. Where do users hesitate? What's different between A and B behavior?

3. **Hypothesis formation:** What theory explains why B works? Test that theory, not just variants.

4. **Decomposition:** Which specific element of variant B drives the effect? Isolate and test.

**Success Criterion for Light:**
You have sufficient light when you can predict, before running the test, whether a new variant will improve conversion and explain WHY.

**Then Return to Fruit:**
With understanding, future A/B tests become more targeted, learning compounds, and success becomes repeatable.

---

*"Those who have handled sciences have been either men of experiment or men of dogmas... But the bee takes a middle course." - Francis Bacon*

---

## Integration

This skill is part of the **Francis Bacon** expert persona. Use it to ensure understanding precedes optimization. It pairs well with:
- **tables-of-investigation** for pursuing light when recommended
- **idol-diagnosis** for clearing obstacles before investigation
- **anticipation-vs-interpretation** for evaluating whether conclusions are properly grounded