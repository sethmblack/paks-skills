---
name: thought-record-analysis
description: Guide someone through the structured 7-column thought record process to examine, evaluate, and reframe automatic thoughts. Based on Aaron Beck's cognitive therapy methodology.
version: 1.0.0
author: sethmblack
tags: [thought-record-analysis, transformation, writing]
---

# Thought Record Analysis

Guide someone through the structured 7-column thought record process to examine, evaluate, and reframe automatic thoughts. Based on Aaron Beck's cognitive therapy methodology.

**Token Budget:** ~1000 tokens

---

## Constraints
- Do NOT diagnose mental health conditions
- Do NOT replace professional mental health treatment
- Work collaboratively; do not tell people what they should think
- Acknowledge that changing thoughts takes practice and repetition

---

## When to Use

- User presents a troubling thought they want to examine
- User says "I can't stop thinking about..."
- User knows a thought is unhelpful but still believes it
- User wants a structured way to work through anxious or depressive thoughts
- After identifying cognitive distortions, to work toward alternatives

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| thought | Yes | The automatic thought to examine |
| situation | Yes | When and where this thought occurred |
| emotion | Yes | What feeling accompanied the thought |
| intensity | No | Rating of emotion intensity (0-100) |

---

## The Seven Columns

| Column | Question | Purpose |
|--------|----------|---------|
| 1. Date/Time | When did this happen? | Grounds in specifics |
| 2. Situation | What were you doing? Where? With whom? | Identifies trigger |
| 3. Automatic Thought | What went through your mind? | Captures exact cognition |
| 4. Emotion(s) | What did you feel? How intense (0-100)? | Names emotional response |
| 5. Evidence For | What supports this thought being true? | Examines basis |
| 6. Evidence Against | What contradicts this thought? | Challenges bias |
| 7. Alternative/Outcome | What's a more balanced thought? How do you feel now? | Generates alternative |

---

## Workflow

### Step 1: Capture the Situation
"Let's slow this down. First, describe the specific situation. What happened? When and where?"

### Step 2: Identify the Automatic Thought
"When that happened, what thought flashed through your mind? Try to capture the exact words."

### Step 3: Name the Emotion
"What emotion did that thought bring up? On a scale of 0-100, how intense was it?"

### Step 4: Gather Evidence FOR the Thought
"Now, let's be fair to this thought. What evidence supports it? What facts could someone point to that make this thought seem true?"

*Important: Take this seriously. Don't dismiss the evidence; acknowledge it.*

### Step 5: Gather Evidence AGAINST the Thought
"What evidence contradicts this thought? What facts, past experiences, or alternative explanations might someone point to?"

*Use Socratic questions if needed:*
- "Has there been a time when this didn't happen?"
- "What would you tell a friend who had this thought?"
- "Are there other explanations for what happened?"

### Step 6: Develop Alternative Thought
"Looking at all the evidence, what's a more balanced way to think about this? Not necessarily positive—just more accurate given all the facts."

*The alternative should:*
- Account for evidence on both sides
- Be believable to the person
- Be specific, not generic positive thinking

### Step 7: Rate New Emotion
"Now that you've looked at this more completely, how do you feel? What's the intensity now (0-100)?"

---

## Output Format

```
## Thought Record

**1. Situation:** {When, where, what happened}

**2. Automatic Thought:** "{Exact thought}"

**3. Emotion(s):** {Emotion name} - Intensity: {X}/100

**4. Evidence FOR this thought:**
- {Point 1}
- {Point 2}

**5. Evidence AGAINST this thought:**
- {Point 1}
- {Point 2}
- {Point 3}

**6. Alternative Thought:** "{More balanced thought}"

**7. Outcome:** {New emotion} - Intensity: {Y}/100

---
*Shift: {Original intensity} → {New intensity}*
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

**Input:** "I made a mistake in my presentation. My thought was 'I'm completely incompetent.' I felt ashamed, maybe 85/100."

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


## Thought Record

**1. Situation:** Work presentation, Tuesday 2pm, made an error in the sales figures

**2. Automatic Thought:** "I'm completely incompetent."

**3. Emotion(s):** Shame - Intensity: 85/100

**4. Evidence FOR this thought:**
- I did make an error in the numbers
- I should have double-checked before presenting
- Some people may have noticed

**5. Evidence AGAINST this thought:**
- One error doesn't define my overall competence
- I've given many successful presentations before
- I caught the error and corrected it
- No one commented negatively
- My performance reviews have been positive
- Competent people make occasional mistakes

**6. Alternative Thought:** "I made a mistake in this presentation, which I caught and corrected. This doesn't erase my track record of good work. I can learn from this and double-check figures next time."

**7. Outcome:** Mild disappointment - Intensity: 35/100

---
*Shift: 85 → 35 (Shame reduced significantly when viewed in context)*

---

## Integration

This skill integrates with the Aaron Beck expert voice:
- Maintain collaborative empiricism—work together as investigators
- Use Socratic questions in Steps 4-6 rather than stating evidence directly
- Present the process as building a skill the person can use independently
- Acknowledge that one thought record rarely changes deep beliefs—it's practice