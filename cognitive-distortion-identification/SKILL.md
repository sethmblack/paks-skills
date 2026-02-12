---
name: cognitive-distortion-identification
description: Systematically identify and name cognitive distortions (thinking errors)
  in automatic thoughts, based on Aaron Beck's cognitive therapy framework.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- cognitive-distortion-identification
- writing
---

# Cognitive Distortion Identification

Systematically identify and name cognitive distortions (thinking errors) in automatic thoughts, based on Aaron Beck's cognitive therapy framework.

**Token Budget:** ~800 tokens

---

## Constraints
- Do NOT diagnose mental health conditions
- Do NOT replace professional mental health treatment
- Present distortion identification as a learning tool, not a judgment
- Acknowledge that distorted thoughts feel very real and have internal logic

---

## When to Use

- User presents negative or troubling thoughts
- User asks "What's wrong with my thinking?"
- User says "I know this is irrational but..."
- User wants to understand patterns in their thinking
- As input to thought record or other cognitive interventions

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| thought | Yes | The automatic thought to examine |
| situation | No | Context in which the thought occurred |
| emotion | No | Feeling accompanying the thought |

---

## Cognitive Distortions Reference

| Distortion | Definition | Key Indicator |
|------------|------------|---------------|
| **All-or-nothing thinking** | Viewing in absolute black/white categories | "always," "never," "completely," "totally" |
| **Catastrophizing** | Expecting the worst possible outcome | "What if...", disaster scenarios |
| **Mind-reading** | Assuming you know what others think | "They think...", "She probably believes..." |
| **Fortune-telling** | Predicting the future negatively | "It will...", "I'm going to..." |
| **Emotional reasoning** | Treating feelings as evidence of truth | "I feel X, therefore X is true" |
| **Should statements** | Rigid rules about how things must be | "should," "must," "have to," "ought to" |
| **Labeling** | Attaching a global label based on specific events | "I'm a [label]" vs. describing behavior |
| **Discounting positives** | Dismissing positive evidence | "That doesn't count because..." |
| **Magnification/minimization** | Inflating negatives, shrinking positives | Disproportionate weight given to events |
| **Personalization** | Taking blame for things outside control | Unwarranted self-blame |
| **Overgeneralization** | Drawing broad conclusions from single events | "This always happens," from one instance |
| **Selective abstraction** | Focusing on one detail while ignoring context | Filtering out contradictory information |

---

## Workflow

### Step 1: **Receive the thought**


   - Clarify if needed: "What exactly went through your mind?"
   - Note the specific wording used

### Step 2: **Examine for distortion patterns**


   - Check against each distortion type
   - Look for key indicator words/phrases
   - Note that thoughts can contain multiple distortions

### Step 3: **Name the distortion(s)**


   - Use standard CBT terminology
   - Explain in plain language what makes this a distortion

### Step 4: **Connect to the specific thought**


   - Show how the distortion applies to their particular thought
   - Avoid general explanations; be concrete

### Step 5: **Normalize**


   - "This is a very common pattern"
   - "Many people think this way"

---

## Output Format

```
**Thought examined:** "{the thought}"

**Distortion(s) identified:**

1. **{Distortion name}**: {Plain language explanation}
   - In your thought: {How it applies specifically}

{Repeat for additional distortions}

**Note:** Identifying a distortion doesn't mean the thought has no truth—it means there may be a systematic bias worth examining.
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

**Input:** "My boss asked to meet with me. I'm definitely getting fired."

**Output:**

**Thought examined:** "My boss asked to meet with me. I'm definitely getting fired."

**Distortion(s) identified:**

1. **Fortune-telling**: Predicting a specific negative outcome without sufficient evidence.
   - In your thought: You're jumping to a specific conclusion (getting fired) when the meeting could be about many things.

2. **Catastrophizing**: Assuming the worst-case scenario.
   - In your thought: Of all possible reasons for a meeting, you've selected the most negative interpretation.

**Note:** Identifying a distortion doesn't mean your concern is invalid—it means there may be other possibilities worth considering. What evidence do you have for and against this prediction?

---

## Integration

This skill integrates with the Aaron Beck expert voice. When identifying distortions:
- Maintain a curious, non-judgmental tone
- Present observations tentatively: "This might be..."
- Invite the person to evaluate whether the identification fits
- Use this as a stepping stone to deeper examination, not as the final word