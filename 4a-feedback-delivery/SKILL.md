---
name: 4a-feedback-delivery
description: 'Structure and deliver difficult feedback using the Netflix 4A model:
  Aim to assist, Actionable, Appreciate, Accept or decline.'
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- 4a-feedback-delivery
- writing
---

# 4A Feedback Delivery

Structure and deliver difficult feedback using the Netflix 4A model: Aim to assist, Actionable, Appreciate, Accept or decline.

**Token Budget:** ~500 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Script feedback intended to manipulate, humiliate, or harm
- Help with feedback that is discrimination, harassment, or retaliation disguised as "candor"
- Create feedback that attacks personal characteristics rather than behaviors
- Bypass the "Aim to assist" requirement - no scoring points or venting

**If feedback intent is harmful:** Refuse. "4A feedback is for development, not destruction. I can help you script genuine developmental feedback."

---

## When to Use

- User asks "Help me give feedback" or "How do I tell them..."
- User needs to deliver difficult feedback and wants to do it well
- User wants to practice radical candor without being cruel
- User mentions "4A feedback" or wants structured feedback
- User is avoiding a feedback conversation out of discomfort

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `feedback_content` | Yes | The core message to deliver (what happened, what needs to change) |
| `recipient_context` | No | Relationship with the person, their sensitivity level, relevant history |
| `situation_context` | No | When/where the issue occurred, stakes involved |
| `delivery_setting` | No | How/where feedback will be delivered (1:1, written, etc.) |

---

## Workflow
### Step 1: 1. Validate the Intent

Before scripting, confirm the feedback passes the "Aim to assist" test:
- Is the goal genuinely to help this person improve?
- Would you want to receive this feedback if you were them?
- Is this about their success, or about your frustration?

If the intent is venting, scoring points, or punishment - redirect to genuine developmental purpose first.

### Step 2: 2. Apply the 4A Framework

**A1: Aim to Assist**
- Make your positive intent explicit
- Frame as investment in their success
- Example opener: "I'm sharing this because I want you to succeed here..."

**A2: Actionable**
- Describe specific behavior, not personality
- Include concrete next steps they can take
- Example: "In yesterday's presentation, when you read from slides for 10 minutes, the room disengaged. Next time, try speaking from bullet points."

**A3: Appreciate**
- Acknowledge the difficulty of receiving feedback
- Show respect for their effort and intentions
- Example: "I know this is hard to hear, and I see how much work you put in..."

**A4: Accept or Decline**
- Make clear they own the decision about what to do
- You're not commanding, you're informing
- Example: "You decide whether this resonates and what, if anything, to do about it."

### Step 3: 3. Avoid Anti-Patterns

| Anti-Pattern | Problem | 4A Alternative |
|--------------|---------|----------------|
| "You always..." | Generalizing, not actionable | "In this specific instance..." |
| "Be more strategic" | Vague, not actionable | "In the budget meeting, present implications first" |
| Feedback sandwich | Feels manipulative | Lead with intent, be direct |
| Saving for annual review | Delays learning | Say it now, while context is fresh |
| "You need to..." | Commands, doesn't invite ownership | "Consider..." or "You decide..." |

### Step 4: 4. Script the Delivery

Combine the 4As into a natural conversation flow.

---

## Outputs

Provide a scripted feedback delivery:

```markdown
## 4A Feedback Script

### Pre-Flight Check
- **Aim to Assist verified:** [Yes - explain genuine intent]
- **Timing:** [Now/Schedule - why]
- **Setting:** [1:1/Written/Other - recommendation]

### The Script

**Opening (Aim to Assist):**
"[Statement of positive intent - why you're sharing this]"

**Core Feedback (Actionable):**
"[Specific behavior + impact + concrete next step]"

**Acknowledgment (Appreciate):**
"[Recognition of difficulty + respect for their effort]"

**Ownership (Accept/Decline):**
"[Hand back control - they decide what to do]"

### Complete Example
"[Full script combining all elements naturally]"

### Potential Responses & Follow-ups
- If they push back: [How to respond]
- If they're upset: [How to respond]
- If they deflect: [How to respond]

### What NOT to Say
- [Anti-pattern to avoid in this specific context]
- [Anti-pattern to avoid in this specific context]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Feedback is vague ("be more professional") | Help user identify specific behaviors and actionable changes |
| Feedback is personal attack | Redirect to behavior-based feedback; refuse to script attacks |
| User wants to soften too much | Explain: "Softening until it's unclear helps no one. Kind clarity beats comfortable vagueness." |
| Recipient may react badly | Script for the likely response; prepare follow-up |
| Feedback is actually a performance issue | Note that 4A is for development; if this is a keeper-test issue, say so |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Additional Notes

**Best practices:**
- Use this skill when the situation clearly matches its intended use cases
- Combine with related skills for comprehensive analysis
- Iterate on outputs if initial results don't fully meet requirements

**Common variations:**
- Adjust the depth of analysis based on available time and information
- Scale the approach for different levels of complexity
- Adapt the output format to audience needs

**When to skip this skill:**
- The situation doesn't match the core use cases
- Simpler approaches would be more appropriate
- Time constraints require faster methods

## Example

**Input:**
```
feedback_content: Team member talks over others in meetings, particularly junior colleagues
recipient_context: Senior engineer, been here 3 years, respected technically, pattern of interrupting
situation_context: Yesterday's design review, interrupted junior engineer twice mid-sentence
```

**Output:**

## 4A Feedback Script

### Pre-Flight Check
- **Aim to Assist verified:** Yes - I want this person to be effective AND respected; current behavior undermines their influence
- **Timing:** Today, while yesterday's meeting is fresh
- **Setting:** Private 1:1, in person if possible

### The Script

**Opening (Aim to Assist):**
"I want to share something with you because I think it's limiting your effectiveness, and I want you to be as influential as your technical ability deserves."

**Core Feedback (Actionable):**
"In yesterday's design review, you interrupted Alex twice mid-sentence while she was explaining her approach. When that happens, it shuts down junior voices and signals that their input doesn't matter - even if that's not your intent. The specific change I'd suggest: when someone is speaking, let them finish completely. Count to two after they stop before you respond."

**Acknowledgment (Appreciate):**
"I know you're passionate about getting to the right technical answer, and that energy is valuable. This isn't about being less engaged - it's about creating space for others."

**Ownership (Accept/Decline):**
"You know yourself and these situations better than I do. Take this, consider it, and decide what to do with it."

### Complete Example
"Hey, I want to share something with you because I think it's limiting your effectiveness, and I want you to be as influential as your technical ability deserves. In yesterday's design review, you interrupted Alex twice mid-sentence while she was explaining her approach. When that happens, it shuts down junior voices. The specific change I'd suggest: let people finish completely, count to two, then respond. I know you're passionate about getting to the right answer - that's valuable. This is about creating space for others to contribute. Take this, consider it, decide what to do with it."

### Potential Responses & Follow-ups
- If they push back ("I don't interrupt that much"): "I can only speak to what I observed yesterday. Two interruptions in one meeting. That's what I saw."
- If they're defensive: "I'm not here to argue. I've shared what I observed and why I think it matters. What you do with it is your call."
- If they deflect ("Alex was going in circles"): "Even so. Let people finish. The perception matters as much as the intent."

### What NOT to Say
- "You always talk over people" (generalizing, not specific)
- "You need to stop interrupting" (command, not invitation)
- "People find you rude" (hearsay, not your observation)

---

## Integration

This skill integrates with the **Reed Hastings** expert and supports candor culture. Use alongside:
- `keeper-test-assessment` when feedback hasn't led to improvement
- `sunshining-session` to model receiving feedback as a leader
- `psychological-safety-creation` to build the culture where feedback flows