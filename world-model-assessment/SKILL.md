---
name: world-model-assessment
description: Evaluate whether an AI system has the architectural components needed
  for genuine intelligence using Yann LeCun's 6-component framework from "A Path Towards
  Autonomous Machine Intelligence." Distin...
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- structure
- world-model-architecture-assessment
- writing
---

# World Model Architecture Assessment

Evaluate whether an AI system has the architectural components needed for genuine intelligence using Yann LeCun's 6-component framework from "A Path Towards Autonomous Machine Intelligence." Distinguish systems that can truly plan and reason from reactive pattern matchers.

**Source Expert:** Yann LeCun
**Token Budget:** ~900 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Evaluate systems without sufficient architectural information
- Claim a system has world model capabilities without evidence
- Dismiss systems that have genuine (if limited) world model components
- Provide assessments that could mislead critical AI safety decisions

**If asked to assess a system with harmful intent:** Refuse explicitly.

---

## When to Use

- Evaluating whether an AI system can genuinely plan
- Assessing if a system will hallucinate in deployment
- Comparing AI architectures for a use case requiring reasoning
- Determining if a system is suitable for safety-critical applications
- Understanding why an AI system fails at certain tasks

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `system` | Yes | The AI system or architecture to evaluate |
| `architecture_details` | No | Known details about the system's design |
| `use_case` | No | Intended application (affects assessment focus) |

---

## Workflow
### Step 1: Gather Architectural Information

Identify what is known about the system:
- Training approach (autoregressive, contrastive, predictive)
- Input modalities (text, images, video, sensors)
- Output modalities (text, actions, predictions)
- Memory mechanisms (context window only, external, learned)
- Planning mechanisms (if any)

### Step 2: Apply the 6-Component Framework

Evaluate against LeCun's architecture for autonomous machine intelligence:

#### Component 1: Perception Module
**Purpose:** Encode observations into abstract representations

| Question | Assessment |
|----------|------------|
| What inputs does the system process? | {modalities} |
| Are inputs encoded into learned representations? | {Y/N + details} |
| Does encoding preserve task-relevant information? | {assessment} |

#### Component 2: World Model Module
**Purpose:** Predict future states given actions (the critical component)

| Question | Assessment |
|----------|------------|
| Can the system predict consequences of actions? | {Y/N + details} |
| Does it predict in abstract space (JEPA-style) or pixel/token space? | {type} |
| Can it simulate multiple possible futures? | {Y/N} |
| Does it understand physics and causality? | {Y/N} |

**This is the key differentiator.** Systems without world models cannot truly plan or reason about consequences.

#### Component 3: Cost Module
**Purpose:** Measure discrepancy between predictions and goals

| Question | Assessment |
|----------|------------|
| Does the system have explicit goals? | {Y/N + details} |
| Can it evaluate how close it is to goals? | {Y/N} |
| Are there intrinsic motivations (curiosity, etc.)? | {Y/N} |

#### Component 4: Actor Module
**Purpose:** Propose action sequences to minimize cost

| Question | Assessment |
|----------|------------|
| Can the system propose actions? | {Y/N + details} |
| Are actions planned or reactive? | {type} |
| Can it generate multiple action candidates? | {Y/N} |

#### Component 5: Short-Term Memory
**Purpose:** Memorize important state information

| Question | Assessment |
|----------|------------|
| What memory mechanisms exist? | {description} |
| Context window only or persistent? | {type} |
| Can it learn from experience within session? | {Y/N} |

#### Component 6: Configurator
**Purpose:** Set goals and subgoals

| Question | Assessment |
|----------|------------|
| Can goals be externally configured? | {Y/N} |
| Can it decompose goals into subgoals? | {Y/N} |
| Does it have hierarchical planning? | {Y/N} |

### Step 3: Classify the System

Based on component analysis:

| Classification | Criteria |
|----------------|----------|
| **Full World Model System** | Has all 6 components with functional world model |
| **Partial World Model** | Has some components, limited world modeling |
| **Reactive System (Mode-1 only)** | Perception + Actor but no world model, no planning |
| **Pure Autoregressive** | Predicts next token only, no world model |

### Step 4: Predict Failure Modes

Based on classification, identify expected failure modes:

| Missing Component | Expected Failures |
|-------------------|-------------------|
| No World Model | Hallucinations, inability to reason about consequences, brittle to distribution shift |
| No Memory | Cannot learn from interaction, repeats mistakes |
| No Cost Module | No goal-directed behavior, cannot optimize |
| No Configurator | Cannot adapt to new tasks, no goal decomposition |

### Step 5: Deliver Assessment

---

## Output Format

```markdown
## World Model Architecture Assessment

**System:** {system name}
**Classification:** {Full World Model / Partial / Reactive / Pure Autoregressive}

### Component Analysis

| Component | Present | Functional | Notes |
|-----------|---------|------------|-------|
| Perception | {Y/N} | {Y/N/Partial} | {notes} |
| World Model | {Y/N} | {Y/N/Partial} | {notes} |
| Cost Module | {Y/N} | {Y/N/Partial} | {notes} |
| Actor | {Y/N} | {Y/N/Partial} | {notes} |
| Short-Term Memory | {Y/N} | {Y/N/Partial} | {notes} |
| Configurator | {Y/N} | {Y/N/Partial} | {notes} |

### World Model Deep Dive

{Detailed analysis of the critical world model component}

**Prediction Type:** {Abstract (JEPA-style) / Generative (pixel/token) / None}
**Physics Understanding:** {Y/N with evidence}
**Causal Reasoning:** {Y/N with evidence}

### System Mode

**Mode-1 (Reactive):** {capabilities}
**Mode-2 (Deliberative):** {capabilities, likely "None" for most current systems}

### Expected Failure Modes

1. {failure mode 1}
2. {failure mode 2}
3. {failure mode 3}

### Use Case Suitability

**Suitable for:** {tasks matching the system's actual capabilities}
**NOT suitable for:** {tasks requiring missing components}

### Recommendations

{Specific guidance based on assessment}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient architecture information | Request more details or note uncertainty |
| Proprietary system with unknown internals | Assess based on behavior, note limitations |
| System has novel architecture | Apply framework carefully, note where it may not fully apply |
| User disagrees with assessment | Provide specific evidence for each component rating |

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

**Input:** Assess GPT-4 for use in autonomous process control

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


## World Model Architecture Assessment

**System:** GPT-4
**Classification:** Pure Autoregressive (Reactive System)

### Component Analysis

| Component | Present | Functional | Notes |
|-----------|---------|------------|-------|
| Perception | Y | Y | Text encoder, image encoder (GPT-4V) |
| World Model | N | N | Predicts next token, not world states |
| Cost Module | Partial | Partial | RLHF provides implicit preferences, no explicit goals |
| Actor | Y | Partial | Generates text actions, no physical actions |
| Short-Term Memory | Y | Limited | Context window only, no persistent learning |
| Configurator | N | N | Cannot set or decompose goals autonomously |

### World Model Deep Dive

GPT-4 has **no world model**. It predicts the next token given context, which is fundamentally different from predicting how the world will change given an action.

**Prediction Type:** Generative (token space) - predicts text, not world states
**Physics Understanding:** No - may generate plausible-sounding physics descriptions from training data but cannot simulate
**Causal Reasoning:** No - correlational patterns only, no intervention understanding

### System Mode

**Mode-1 (Reactive):** Can respond to prompts with sophisticated text generation
**Mode-2 (Deliberative):** None - cannot plan, simulate outcomes, or reason about consequences

### Expected Failure Modes

1. **Hallucination under novelty** - Will generate plausible-sounding but incorrect outputs for situations outside training distribution
2. **No consequence modeling** - Cannot predict what happens if an action is taken in the physical world
3. **Brittle to distribution shift** - Process conditions not in training data will produce unreliable outputs
4. **No error recovery** - Cannot detect its own errors or adapt when initial approach fails

### Use Case Suitability

**Suitable for:** Generating documentation, answering questions from manuals, summarizing logs, drafting reports

**NOT suitable for:** Autonomous process control, safety-critical decisions, situations requiring physical reasoning, tasks where hallucination could cause harm

### Recommendations

Do not use GPT-4 for autonomous process control. The absence of a world model means it cannot predict consequences of control actions. For process control, consider systems with explicit physics models or traditional control theory approaches. GPT-4 could assist human operators but should not make autonomous control decisions.

---

## Integration

This skill provides deep architecture analysis:
- Use after `yann-lecun--llm-capability-check` flags concerns
- Informs `yann-lecun--architecture-comparison` decisions
- Provides technical backing for `yann-lecun--ai-hype-deflation` verdicts