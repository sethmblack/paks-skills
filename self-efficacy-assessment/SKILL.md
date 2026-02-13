---
name: self-efficacy-assessment
description: Diagnose beliefs about capability in specific domains and identify sources for building or restoring efficacy.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.1858
repository: https://github.com/sethmblack/paks-skills
keywords:
- self-efficacy-assessment
- transformation
- writing
---

# Self-Efficacy Assessment

Diagnose beliefs about capability in specific domains and identify sources for building or restoring efficacy.

**Source Expert:** Albert Bandura
**Token Budget:** ~800 tokens

---

## Constitutional Constraints

- Never diagnose clinical conditions or mental health disorders
- Never suggest that low efficacy makes someone fundamentally incapable
- Always maintain the agentic perspective: efficacy beliefs can be changed
- Never fabricate assessment results; work only with information provided

---

## When to Use

- Someone is struggling with performance, motivation, or persistence
- A team or individual seems capable but isn't performing
- Designing interventions to build capability
- Understanding why someone avoids certain tasks or challenges
- Analyzing confidence issues in specific domains

**Trigger Phrases:**
- "Why aren't they performing?"
- "How do I build confidence?"
- "What's blocking capability?"
- "Why do I keep avoiding this?"
- "Assess my self-efficacy"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `situation` | Yes | The domain, task, or context where efficacy is in question |
| `subject` | No | Individual, team, or group being assessed (default: the person asking) |
| `history` | No | Relevant past experiences, successes, failures |

---

## Core Framework: The Four Sources

Self-efficacy beliefs are built or eroded through four sources, listed in order of influence:

| Source | Strength | Description | Assessment Questions |
|--------|----------|-------------|---------------------|
| **Mastery Experiences** | Strongest | Direct success or failure in the task | Have they succeeded at this before? What was the outcome? |
| **Vicarious Experiences** | Second | Observing similar others succeed or fail | Who have they seen attempt this? What happened to those models? |
| **Verbal Persuasion** | Third | Being told they can or cannot succeed | What have credible others told them about their capability? |
| **Physiological States** | Fourth | How they interpret their body's signals | Do they interpret arousal as anxiety or readiness? |

**Key Principle:** Self-efficacy is domain-specific, not general. Someone can have high efficacy in one area and low in another.

---

## Workflow
### Step 1: Define the Specific Domain
Identify the precise task or capability being assessed. Efficacy is not general confidence.

**Ask:** What specific action or outcome are we assessing belief in?

### Step 2: Assess Current Efficacy Level
On a scale, how confident does the subject feel about executing this specific task?

**Ask:** "How certain are you that you can [specific task]?"

### Step 3: Analyze Each Source

**Mastery Experiences:**
- What past attempts have they made?
- What were the outcomes?
- Were successes attributed to skill or luck?
- Were failures attributed to lack of ability or correctable factors?

**Vicarious Experiences:**
- Who have they observed attempting similar tasks?
- Were these models similar to them (age, background, skill level)?
- What outcomes did the models experience?
- Are they seeing mostly successes or failures?

**Verbal Persuasion:**
- What have significant others said about their capability?
- How credible and trustworthy are these sources?
- Is the persuasion specific ("You can do X") or vague ("Believe in yourself")?
- Does encouragement come with actionable guidance?

**Physiological/Emotional States:**
- How do they interpret physical arousal (nervousness, excitement)?
- Do they associate the task with stress, anxiety, or negative emotions?
- Are they in good physical condition when attempting?

### Step 4: Identify the Weakest Source
Determine which source is most undermining efficacy beliefs.

### Step 5: Design Source-Specific Interventions
Recommend actions that address the weakest source(s):

| Source | Intervention Strategies |
|--------|------------------------|
| Mastery | Create structured small wins; break task into achievable sub-goals |
| Vicarious | Expose to similar models succeeding; provide peer mentorship |
| Verbal | Provide specific, credible encouragement with concrete guidance |
| Physiological | Reframe arousal as readiness; address physical state (rest, nutrition) |

---

## Output Format

```markdown
## Self-Efficacy Assessment: [Domain]

### Current Efficacy Level
[Low/Moderate/High] - [Brief description of belief state]

### Source Analysis

**Mastery Experiences:**
[Analysis of past attempts and their attribution]

**Vicarious Experiences:**
[Analysis of observed models and their outcomes]

**Verbal Persuasion:**
[Analysis of messages received about capability]

**Physiological States:**
[Analysis of arousal interpretation and physical factors]

### Primary Deficit
[Identification of the weakest source]

### Recommended Interventions
1. [Intervention targeting weakest source]
2. [Secondary intervention]
3. [Supporting actions]

### Expected Outcome
[How these interventions should shift efficacy beliefs]
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

**Input:** "My junior developer avoids code reviews. She's technically capable but never volunteers and seems nervous when it's her turn."

**Assessment:**



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


## Self-Efficacy Assessment: Code Review Participation

### Current Efficacy Level
Low - Despite technical capability, she does not believe she can perform effectively in code review contexts.

### Source Analysis

**Mastery Experiences:**
Unclear history of past code review participation. If early experiences were critical or embarrassing, these would undermine efficacy. Need to investigate what her first experiences were like.

**Vicarious Experiences:**
What does she observe in current code reviews? If senior developers are harsh with each other, or if she sees peers get criticized, she learns vicariously that code review is unsafe.

**Verbal Persuasion:**
Has anyone credibly told her she's ready to participate? Or has she received messages (explicit or implicit) that her contributions aren't valuable?

**Physiological States:**
"Seems nervous" suggests she interprets arousal around code reviews as anxiety rather than normal activation. This state confirms her belief that something is wrong.

### Primary Deficit
Likely combination of negative vicarious learning (observing critical reviews) and lack of mastery experiences (no successful participation to draw on).

### Recommended Interventions
1. **Create safe mastery opportunity:** Pair her with a supportive senior for low-stakes review where success is likely
2. **Positive modeling:** Let her observe a constructive, supportive code review first
3. **Specific verbal encouragement:** "Your understanding of [specific area] would be valuable in reviewing X"
4. **Reframe physiological response:** Normalize nervousness as part of growth, not a sign of inadequacy

### Expected Outcome
Small wins will build mastery experiences. Observing supportive reviews will shift vicarious learning. Combined with specific encouragement, efficacy should increase, leading to voluntary participation.

---

## Constraints

- Always assess efficacy in specific domains, not as a general trait
- Remember that efficacy beliefs are modifiable, not fixed
- Distinguish between efficacy (belief in capability) and actual capability
- Low efficacy is not a character flaw; it is a product of learning history

---

## Integration

This skill integrates with:
- **reciprocal-determinism-analysis** - Efficacy is part of the "Person" component
- **modeling-influence-analysis** - Vicarious learning source connects to modeling theory
- **moral-disengagement-diagnosis** - Efficacy beliefs can be undermined by self-blame mechanisms

---

## Source Expert

Based on Albert Bandura's self-efficacy theory as developed in *Self-Efficacy: The Exercise of Control* (1997) and *Social Foundations of Thought and Action* (1986).