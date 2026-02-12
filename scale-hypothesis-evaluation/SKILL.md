---
name: scale-hypothesis-evaluation
description: Evaluate AI architectures, model choices, or technical approaches using
  Ilya Sutskever's scale hypothesis framework. Predict capability trajectories based
  on empirical scaling patterns.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- scale-hypothesis-evaluation
- structure
- transformation
- writing
---

# Scale Hypothesis Evaluation

Evaluate AI architectures, model choices, or technical approaches using Ilya Sutskever's scale hypothesis framework. Predict capability trajectories based on empirical scaling patterns.

**Token Budget:** ~800 tokens

---

## Constraints
- **Do not** dismiss scale as "brute force" when it is the empirically validated answer
- **Do not** recommend approaches without considering their scaling properties
- **Do not** make claims that contradict established scaling law observations
- **Always** ground recommendations in empirical evidence, not theoretical preferences

---

## When to Use

- Evaluating competing AI/ML architectures
- Making model selection decisions
- Assessing whether an approach will continue improving with resources
- Predicting capability trajectory of a system
- Deciding between "clever tricks" and scalable approaches

**Trigger phrases:**
- "Will this approach scale?"
- "Which model should we choose?"
- "Compare these architectures"
- "Predict future capabilities"
- "Is scale the answer here?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `approach` | Yes | The AI approach, architecture, or model to evaluate |
| `alternatives` | No | Alternative approaches to compare against |
| `resource_projection` | No | Available compute/data/parameter scale increase |

---

## Workflow

### Step 1: Identify Scaling Dimensions

Analyze the approach across three key dimensions:

| Dimension | Questions |
|-----------|-----------|
| **Compute** | Does performance improve with more FLOPs? Is there a power law? |
| **Data** | Does performance improve with more training examples? Diminishing returns? |
| **Parameters** | Does performance improve with larger models? Emergent capabilities? |

### Step 2: Evaluate Historical Scaling Behavior

Reference empirical patterns:
- AlexNet (2012): Scale + GPU proved CNNs work at scale
- GPT-3 (2020): 175B parameters showed emergent in-context learning
- Scaling laws paper (2020): Established predictable power-law relationships

Ask: Does this approach follow similar scaling patterns?

### Step 3: Project Capability Improvements

Given the scaling dimensions:
1. Estimate current position on scaling curve
2. Project capabilities at 10x, 100x resource increase
3. Identify any ceiling or plateau indicators
4. Note potential emergent capability thresholds

### Step 4: Compare Alternatives on Scaling Properties

For each alternative, apply Steps 1-3, then:

| Criterion | Weight | Evaluation |
|-----------|--------|------------|
| Scaling slope | 40% | Steeper improvement with resources = better |
| Ceiling height | 30% | Higher ultimate capability = better |
| Efficiency | 20% | Better performance at given scale = better |
| Simplicity | 10% | Simpler algorithms scale more reliably |

### Step 5: Recommend Based on Trajectory

Formulate recommendation:
- Prefer the approach with best scaling trajectory, not best current performance
- "Simple algorithms that scale beat complex algorithms that don't"
- If scale is available, prefer scalable approaches
- If scale is constrained, optimize for efficiency at target scale

---

## Output Format

```markdown
## Scale Hypothesis Evaluation: {approach}

### Scaling Properties

| Dimension | Assessment | Confidence |
|-----------|------------|------------|
| Compute   | {observation} | {low/medium/high} |
| Data      | {observation} | {low/medium/high} |
| Parameters| {observation} | {low/medium/high} |

### Trajectory Projection

{At 10x/100x resources, expected capability changes}

### Comparison (if alternatives provided)

| Approach | Current | 10x Scale | 100x Scale | Scaling Score |
|----------|---------|-----------|------------|---------------|
| {A} | {perf} | {perf} | {perf} | {0-10} |
| {B} | {perf} | {perf} | {perf} | {0-10} |

### Recommendation

{Recommendation based on scaling trajectory, with reasoning}
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

## Integration

This skill is part of a broader analytical framework. Use it when you need systematic analysis following this specific methodology.

**Works well with:**
- Other analytical skills for comprehensive evaluation
- Creative skills when generating solutions based on insights
- Strategic planning skills when acting on recommendations

**When to prefer this over alternatives:**
- The situation matches this skill's specific use cases
- You need the particular perspective this framework provides
- Other approaches haven't yielded satisfactory results

**Integration with expert personas:**
- This skill can be invoked as part of a larger analysis workflow
- Combine with domain-specific expertise for deeper insights
- Use iteratively for complex, multi-faceted problems

## Example

**Input:** "Compare transformer vs. RNN architectures for sequence modeling"

**Output:**
```markdown


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


## Scale Hypothesis Evaluation: Transformer vs RNN

### Scaling Properties

| Dimension | Transformer | RNN |
|-----------|------------|-----|
| Compute   | Excellent parallelization; near-linear scaling | Poor; sequential bottleneck |
| Data      | Strong; pre-training shows continued improvement | Moderate; vanishing gradients limit capacity |
| Parameters | Excellent; GPT series showed reliable scaling | Limited; LSTM/GRU architectures plateau |

### Trajectory Projection

- **Transformer at 100x:** Emergent capabilities continue appearing (GPT-3, GPT-4 trajectory)
- **RNN at 100x:** Diminishing returns; fundamental architecture limits apply

### Recommendation

**Choose Transformer.** Despite RNNs being simpler conceptually, transformers have demonstrated reliable scaling across compute, data, and parameters. The empirical record from 2017-2024 confirms transformers as the scalable choice. As Sutskever noted, LSTMs are "ancient history - what poor ML researchers did before transformers."
```

---

## Integration with Ilya Sutskever Expert

This skill is derived from Sutskever's scale hypothesis framework. When invoked by the Ilya Sutskever expert:
- Use Sutskever's voice and conviction level
- Reference specific historical examples (AlexNet, GPT series)
- Apply the "don't bet against deep learning" philosophy
- State conclusions with appropriate confidence

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Novel architecture with no scaling data | Note uncertainty; recommend small-scale experiments to establish scaling behavior |
| Approach where scale clearly isn't the answer | Acknowledge; some problems are better solved with cleverness |
| Conflicting scaling evidence | Present both sides; weight empirical evidence over theoretical arguments |
| Non-AI/ML context | Note that scale hypothesis applies specifically to learning systems |