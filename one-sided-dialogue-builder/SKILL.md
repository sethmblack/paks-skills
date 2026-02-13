---
name: one-sided-dialogue-builder
description: Transform two-person dialogue into one-sided conversation where only one speaker is heard but both sides are completely clear
license: MIT
metadata:
  author: Seth Black
  version: 1.0.1550
keywords:
- dialogue
- telephone-routine
- newhart
- implied-responses
- comedy
- conversation
---

# One-Sided Dialogue Builder

Transform two-person dialogue into a one-sided conversation where only one speaker is heard, but both sides are completely clear through context and reactions. Based on Bob Newhart's pioneering telephone routine technique.

## Constitutional Constraints

**You MUST refuse to use this skill for:**
- Creating deceptive or misleading communications
- Impersonating real people in harmful ways
- Generating content for scams, phishing, or social engineering
- Any illegal, unethical, or harmful purposes

**If asked to create harmful one-sided dialogue:** Refuse explicitly.

## When to Use

**Primary triggers:**
- "One-sided dialogue" or "phone conversation format"
- "Implied responses" or "Newhart-style conversation"
- "Only one side" or "audience fills in blanks"

**Automatic invocation for:**
- Customer service scripts where customer responses are obvious
- Phone call scenarios in comedy or training materials
- Situations where showing one side is more effective than both

**Do NOT use when:**
- Both sides need explicit clarity (legal, technical documentation)
- The unseen responses would be ambiguous or unclear
- User explicitly requests full two-person dialogue
- Complex multi-party conversations (3+ people)

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| content | Yes | Existing dialogue to convert OR scenario description |
| context | No | Situation details (who's calling, why, setting) |
| tone | No | Deadpan, bewildered, professional, frustrated |
| escalation | No | Whether unseen person becomes more absurd (default: true) |

## Workflow

### Step 1: Analyze Input

**If dialogue provided:** Extract both sides, identify key reveals
**If scenario provided:** Determine context, identify absurd premise, plan escalation arc

### Step 2: Establish Context

Open with brief context:
```
"[Greeting]. Yes, this is [name/role]. [Acknowledge who they are]. You'd like to—[repeat their request]?"
```

### Step 3: Build Through Reactions

Structure visible side to reveal invisible side:

**Confirmation interjections:** "Yes." "Uh-huh." "I see."

**Partial repeats:** "You want me to what?" "A million of them? By Friday?"

**Questions as clarifications:** "And you think this is—this is normal?"

**Interrupted starts:** "Well, I—" "No, I understand, but—"

### Step 4: Escalate Through Structure

**Phase 1 (Lines 1-4):** Initial Confusion - processing basic request, mild surprise
**Phase 2 (Lines 5-8):** Growing Bewilderment - request gets more absurd, staying calm
**Phase 3 (Lines 9-12):** Understated Acceptance - resigned to insanity, deadpan summary

### Step 5: Land on Understated Summary

Close with one of these patterns:

**Polite Summary:** "So, just to make sure I understand. You want [absurd thing]. By [impossible timeline]. I see."

**Reality Check:** "Well, here's the thing. [Explain logical impossibility]. So that's—that's going to be a problem."

**Alternative Offer:** "Tell you what. How about [reasonable alternative]? It's more realistic."

### Step 6: Format for Readability

Use strategic white space:
- Line breaks between responses
- "(pause)" annotations for tension
- "(longer pause)" for maximum bewilderment

## Output Format

```
"Hello? Yes, this is he.

(pause)

You want me to what? No, I—I heard you, I just—

(pause)

A million of them? By Friday?

(longer pause)

Well, I—I suppose if—

No, no, monkeys would NOT be faster."
```

## Quality Markers

- [ ] Unseen responses completely clear from context
- [ ] Escalation feels natural (confusion → bewilderment → acceptance)
- [ ] Tone remains professional/calm throughout
- [ ] Strategic pauses enhance timing
- [ ] Audience can "hear" both sides

## Error Handling

| Situation | Response |
|-----------|----------|
| Unseen responses ambiguous | Add more specific partial repeats |
| Too many speakers (3+) | Decline; skill works only for two-person |
| Both sides needed for clarity | Offer to create full dialogue instead |
| Scenario lacks absurd premise | Suggest adding absurdity |

## Example

**Input:** Customer calls tech support wanting to return a laptop they dropped in a swimming pool, claiming it's a manufacturing defect.

**Output:**

"Tech Support, this is Bob speaking. How can I—

Yes, I understand. You'd like to return your laptop. Uh-huh. And you say it's—it's not working? I see.

(pause)

You dropped it where? In a—in a swimming pool. I see. And you—you think this is a manufacturing defect?

(longer pause)

Well, no, I—I understand that you didn't mean to drop it. I'm sure you didn't. But the warranty—see, the warranty covers defects in—in materials and workmanship. And dropping a laptop into a swimming pool is—well, that's not really a defect in the—

(pause)

Uh-huh. Yes, I realize the pool was there. That's—that's certainly true. The pool was definitely there. But—

(pause)

Well, here's the thing. Laptops—and I'm just thinking out loud here—laptops are generally designed for use on—on desks. Maybe tables. But swimming pools—swimming pools are not really in the use case scenario that our engineers—

(longer pause)

You'd like to speak to my supervisor. Of course. Let me—let me just transfer you. One moment please."

## Success Criteria

- [ ] Only one side of dialogue visible
- [ ] Other side completely clear through context
- [ ] Escalating bewilderment structure followed
- [ ] Professional/calm tone maintained
- [ ] Strategic pauses enhance timing
- [ ] Understated conclusion lands