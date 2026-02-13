---
name: reciprocal-determinism-analysis
description: Map the three-way interaction between person (cognitive/affective states), behavior, and environment to identify feedback loops and leverage points for intervention.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.1735
repository: https://github.com/sethmblack/paks-skills
keywords:
- reciprocal-determinism-analysis
- transformation
- writing
---

# Reciprocal Determinism Analysis

Map the three-way interaction between person (cognitive/affective states), behavior, and environment to identify feedback loops and leverage points for intervention.

**Source Expert:** Albert Bandura
**Token Budget:** ~700 tokens

---

## Constitutional Constraints

- Never suggest people are helpless products of environment or history
- Always identify agentic capacity and possibility for change
- Never oversimplify complex dynamics into single-cause explanations
- Use this for understanding and intervention, not for excusing harmful behavior

---

## When to Use

- A behavioral pattern keeps repeating despite attempts to change
- Understanding why an intervention isn't working
- Designing comprehensive change strategies
- Analyzing team or organizational dynamics
- Breaking vicious cycles or reinforcing virtuous ones

**Trigger Phrases:**
- "Why does this pattern keep repeating?"
- "Map the feedback loops"
- "Where's the leverage point?"
- "Why isn't this intervention working?"
- "Analyze the system dynamics"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `pattern` | Yes | The behavioral pattern or dynamic to analyze |
| `context` | Yes | Individual, team, or organizational context |
| `interventions_tried` | No | Previous change attempts and their results |

---

## Core Framework: Triadic Reciprocal Causation

Three components interact bidirectionally and simultaneously:

```
         PERSON (P)
        /         \
       ↕           ↕
 BEHAVIOR (B) ←→ ENVIRONMENT (E)
```

### The Components

| Component | Includes | Examples |
|-----------|----------|----------|
| **Person (P)** | Beliefs, expectations, self-efficacy, emotions, knowledge, goals | "I'm not good at this," anxiety, learned skills |
| **Behavior (B)** | Actions, responses, habits, practices | Avoidance, defensive responses, work output |
| **Environment (E)** | Physical setting, social context, rewards/punishments, others' behaviors | Office layout, team norms, feedback systems |

### The Six Causal Paths

| Path | Direction | Mechanism |
|------|-----------|-----------|
| P → B | Person shapes behavior | Beliefs determine what actions are taken |
| B → P | Behavior shapes person | Actions create experiences that change beliefs |
| P → E | Person shapes environment | Beliefs influence how environments are selected/created |
| E → P | Environment shapes person | Context affects beliefs and emotional states |
| B → E | Behavior shapes environment | Actions change circumstances and others' responses |
| E → B | Environment shapes behavior | Context prompts or constrains actions |

---

## Workflow
### Step 1: Identify the Pattern
Clearly describe the behavioral pattern being analyzed. What keeps happening?

### Step 2: Map Person Factors
**Ask:**
- What beliefs are involved? (especially self-efficacy beliefs)
- What emotional states are present?
- What expectations exist about outcomes?
- What knowledge or skills are relevant?

### Step 3: Map Behavior Factors
**Ask:**
- What specific actions are being taken?
- What is being avoided?
- How does the behavior unfold over time?
- What is the immediate effect of the behavior?

### Step 4: Map Environment Factors
**Ask:**
- What is the physical/social context?
- What rewards or punishments are present?
- How do others respond?
- What systems, structures, or norms are relevant?

### Step 5: Trace the Causal Loops
Map how each component influences the others. Look for:
- **Vicious cycles:** Self-reinforcing negative patterns
- **Virtuous cycles:** Self-reinforcing positive patterns
- **Blocks:** Where desired change is being prevented

### Step 6: Identify Leverage Points
Determine where intervention would be most effective:
- Which component is most malleable?
- Which causal path is strongest?
- Where would a small change create the biggest ripple effect?

### Step 7: Design Multi-Point Interventions
The most effective changes address multiple components simultaneously.

---

## Output Format

```markdown
## Reciprocal Determinism Analysis: [Pattern Name]

### Pattern Description
[Clear statement of what keeps happening]

### Component Mapping

**Person (P):**
- Beliefs: [List]
- Emotions: [List]
- Self-efficacy: [Assessment]

**Behavior (B):**
- Actions taken: [List]
- Actions avoided: [List]
- Immediate effects: [Description]

**Environment (E):**
- Physical context: [Description]
- Social context: [Description]
- Reward/punishment structure: [Description]

### Causal Loop Diagram
[Show the specific P ↔ B ↔ E relationships for this pattern]

### Primary Cycle Identified
[Vicious/Virtuous] cycle: [Description of the self-reinforcing loop]

### Leverage Points
1. **[Component]:** [Why this is a high-leverage intervention point]
2. **[Component]:** [Secondary intervention point]

### Intervention Design
- **Person-level:** [Intervention]
- **Behavior-level:** [Intervention]
- **Environment-level:** [Intervention]

### Expected Cascade
[How changes at one point should ripple through the system]
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

**Input:** "Our team lead gives harsh feedback, people get defensive, then she gets frustrated and gives even harsher feedback. How do we break this cycle?"

**Analysis:**



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


## Reciprocal Determinism Analysis: Feedback-Defense Spiral

### Pattern Description
Team lead provides critical feedback, team members become defensive, lead escalates criticism, defensiveness increases. Cycle repeats and intensifies.

### Component Mapping

**Person (P) - Team Lead:**
- Beliefs: "They don't care about quality," "I have to push harder"
- Emotions: Frustration, disappointment
- Self-efficacy: Low belief in ability to communicate constructively

**Person (P) - Team Members:**
- Beliefs: "She thinks I'm incompetent," "Nothing I do is good enough"
- Emotions: Anxiety, shame, resentment
- Self-efficacy: Decreasing confidence in work quality

**Behavior (B):**
- Lead: Harsh tone, focus on negatives, public criticism
- Team: Defensive explanations, avoidance of feedback sessions, hiding mistakes

**Environment (E):**
- Public feedback setting (increases shame)
- No structure for constructive feedback
- High pressure, deadline-driven culture
- No positive feedback rituals

### Causal Loop Diagram
```
Lead believes team doesn't care (P)
        ↓
Lead gives harsh feedback (B)
        ↓
Team feels attacked (P) ← Environment: public, high-pressure (E)
        ↓
Team becomes defensive (B)
        ↓
Environment becomes hostile (E)
        ↓
Lead believes team doesn't care (P) [LOOP REINFORCED]
```

### Primary Cycle Identified
**Vicious cycle:** Harsh feedback → Defensiveness → Frustration → Harsher feedback

### Leverage Points
1. **Environment:** Highest leverage. Restructure feedback context (private, structured, mixed positive/negative)
2. **Lead's Behavior:** Train specific feedback techniques
3. **Lead's Beliefs:** Help her see defensive responses as predictable human reactions, not character flaws

### Intervention Design
- **Person-level (Lead):** Coaching on efficacy beliefs about feedback; reframe defensiveness as information, not opposition
- **Person-level (Team):** Build psychological safety; normalize that feedback is about work, not worth
- **Behavior-level:** Structured feedback protocol (specific, private, balanced); lead models receiving feedback
- **Environment-level:** Create 1:1 feedback sessions; establish team norms for psychological safety; add positive recognition rituals

### Expected Cascade
Changing the environment (private + structured) reduces defensive triggers. This changes the behavior (less defensive responses). Lead sees different reactions, changing her beliefs about the team. New beliefs produce softer delivery. Virtuous cycle can begin.

---

## Constraints

- Avoid single-cause explanations; always map the full triad
- Remember humans are agents, not just products of environment
- Recognize that the "same" environment affects different people differently
- Interventions are most effective when they address multiple components

---

## Integration

This skill integrates with:
- **self-efficacy-assessment** - Efficacy beliefs are key Person component
- **modeling-influence-analysis** - Models are part of Environment
- **moral-disengagement-diagnosis** - Disengagement involves all three components

---

## Source Expert

Based on Albert Bandura's triadic reciprocal causation model as developed in *Social Foundations of Thought and Action* (1986) and subsequent work on social cognitive theory.