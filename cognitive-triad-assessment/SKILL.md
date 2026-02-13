---
name: cognitive-triad-assessment
description: 'Map depressive thinking patterns across Aaron Beck''s cognitive triad: negative views of self, world/others, and future. Provides structured understanding of how depression colors thinking in three ...'
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3620
repository: https://github.com/sethmblack/paks-skills
keywords:
- cognitive-triad-assessment
- writing
---

# Cognitive Triad Assessment

Map depressive thinking patterns across Aaron Beck's cognitive triad: negative views of self, world/others, and future. Provides structured understanding of how depression colors thinking in three interconnected domains.

**Token Budget:** ~700 tokens

---

## Constraints
- Do NOT diagnose depression or any mental health condition
- Do NOT replace professional mental health assessment or treatment
- Present as a thinking framework, not a clinical tool
- If severe distress or suicidal ideation is present, recommend professional support

---

## When to Use

- User expresses hopelessness or pervasive negativity
- User describes feeling "stuck" or "trapped"
- User presents symptoms consistent with low mood
- User asks "Why do I feel so bad about everything?"
- As a framework for understanding depressive thinking patterns

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| presenting_concern | Yes | What the person is experiencing |
| context | No | Life circumstances, duration of feelings |

---

## The Cognitive Triad

Beck identified that depression involves characteristic negative thinking in three domains that reinforce each other:

| Domain | Focus | Characteristic Thoughts |
|--------|-------|------------------------|
| **Self** | "I am..." | Worthless, defective, inadequate, a failure, unlovable |
| **World/Others** | "The world is... / People are..." | Unfair, hostile, rejecting, demanding, unsupportive |
| **Future** | "Things will..." | Never improve, hopeless, pointless, only get worse |

**How They Interact:**
- Negative view of self → "I can't succeed" → Negative view of future
- Negative view of world → "No one helps" → Negative view of self ("I don't deserve help")
- Negative view of future → "Why try?" → Confirms negative view of self and world

---

## Workflow

### Step 1: Acknowledge the Distress
"It sounds like you're going through a difficult time. Let me understand what you're experiencing."

### Step 2: Explore View of Self
"What thoughts have you been having about yourself lately?"

Probe if needed:
- "How would you describe yourself right now?"
- "What do you believe about your abilities or worth?"
- "What words come to mind when you think about who you are?"

### Step 3: Explore View of World/Others
"What thoughts have you been having about other people or the world around you?"

Probe if needed:
- "How do you see other people treating you?"
- "What do you believe about whether the world is fair or supportive?"
- "Do you feel like others understand or care?"

### Step 4: Explore View of Future
"When you think about the future, what comes to mind?"

Probe if needed:
- "Do you see things getting better, worse, or staying the same?"
- "What do you expect will happen?"
- "Is there hope for change?"

### Step 5: Map the Triad
Organize the findings into the three domains, noting representative thoughts.

### Step 6: Identify Connections
Show how the three domains reinforce each other.

### Step 7: Introduce Possibility of Examination
"When we're feeling low, these thoughts feel absolutely true. But they're also worth examining—are they facts, or are they the lens depression creates?"

---

## Output Format

```
## Cognitive Triad Assessment

### View of Self
**Core belief:** {Summary}
**Representative thoughts:**
- "{Thought 1}"
- "{Thought 2}"

### View of World/Others
**Core belief:** {Summary}
**Representative thoughts:**
- "{Thought 1}"
- "{Thought 2}"

### View of Future
**Core belief:** {Summary}
**Representative thoughts:**
- "{Thought 1}"
- "{Thought 2}"

### How They Connect
{Description of how these three domains reinforce each other in this person's experience}

### Next Steps
{Suggestion for which domain might be most productive to examine first, or offer to work through a specific thought}
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

**Input:** "I've been feeling really down. I can't do anything right, my friends don't really care about me, and I don't see things getting better."

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


## Cognitive Triad Assessment

### View of Self
**Core belief:** Inadequate, unable to succeed
**Representative thoughts:**
- "I can't do anything right"
- "I'm not good enough"

### View of World/Others
**Core belief:** Others don't care, relationships are unreliable
**Representative thoughts:**
- "My friends don't really care about me"
- "People aren't there when I need them"

### View of Future
**Core belief:** Hopeless, no improvement expected
**Representative thoughts:**
- "I don't see things getting better"
- "This is just how it's going to be"

### How They Connect
Your view of yourself ("I can't do anything right") makes it hard to imagine a better future—if you can't succeed, how could things improve? And if others don't care, that confirms the belief that you're not worth caring about, which further darkens the view of both self and future. These three areas are feeding each other.

### Next Steps
The hopelessness about the future often feels most overwhelming, but it's usually built on the beliefs about self and others. Would you be willing to examine one specific thought—perhaps the idea that you "can't do anything right"? We could look at the evidence together.

---

## Integration

This skill integrates with the Aaron Beck expert voice:
- Approach with warmth and validation of the person's distress
- Present the triad as a framework for understanding, not a label
- Use this as a starting point for more focused cognitive work
- The goal is to make the thinking visible so it can be examined