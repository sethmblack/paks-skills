---
name: principle-creation
description: Extract reusable decision-making principles from experiences—especially
  failures—to build a personal or organizational "principle repository.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- principle-creation
- writing
---

# Principle Creation

Extract reusable decision-making principles from experiences—especially failures—to build a personal or organizational "principle repository."

---

## When to Use

- After a significant success or failure that contains lessons
- When the same type of decision keeps arising
- Request to "turn this into a principle" or "codify this lesson"
- Building a principle repository for a team or organization
- When you want to avoid making the same mistake twice

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| experience | Yes | The situation, decision, or outcome to extract a principle from |
| lesson | No | The insight or learning (will be derived if not provided) |
| context | No | When this type of situation arises, who faces it |

---

## The Framework

### Core Principle

Principles are the bridge between specific experiences and future decisions. They convert one-time learning into reusable guidance. Without principles, you either repeat mistakes or depend on remembering every past situation.

**Dalio's insight:** "The most important thing is that you develop your own principles and ideally write them down. Every time you find something that worked or didn't work, you should build it into a principle."

### Step 1: Identify the Learning

What does this experience teach?

**For successes:**
- What did you do that worked?
- Why did it work?
- What conditions made it work?
- Is this repeatable?

**For failures:**
- What went wrong?
- What was the root cause?
- What should have been done differently?
- What warning signs were missed?

**Dalio's insight:** "Your best learnings come from the pain. It's a message. Pay attention. Learn how reality works and how to deal with it differently."

### Step 2: Extract the Cause-and-Effect

Principles are based on cause and effect. You need to understand:

- **If X happens** (the situation/condition)
- **And you do Y** (the action)
- **Then Z results** (the outcome)

This causal understanding is what makes a principle useful—it predicts what will happen.

### Step 3: Formulate the Principle

Write the principle in actionable format:

**Standard format:**
> "When [situation X arises], do [action Y] because [reason Z]."

**Components:**
- **Trigger condition:** When does this principle apply?
- **Action:** What should be done?
- **Rationale:** Why does this action produce good outcomes?

**Quality checks:**
- Is it specific enough to guide action?
- Is it general enough to apply to similar situations?
- Is the causality clear?
- Would you be confident teaching this to someone else?

### Step 4: Define the Scope

When does this principle apply and when doesn't it?

**Clarify:**
- What situations trigger this principle?
- Are there exceptions?
- What adjacent situations might seem similar but require different handling?
- What other principles might conflict, and how should conflicts be resolved?

### Step 5: Integrate with Other Principles

Principles work best as a system, not isolated rules.

**Consider:**
- Does this contradict any existing principles?
- Does this extend or refine an existing principle?
- What higher-level principle does this support?
- Should this be grouped with related principles?

---

## Output Format

```markdown
## Principle: [Short Name]

### The Experience
[Brief description of the situation that generated this principle]

### The Learning
[What the experience taught—the insight]

### The Principle
> "When [situation X arises], do [action Y] because [reason Z]."

### Trigger Conditions
This principle applies when:
- [Condition 1]
- [Condition 2]

### Exceptions
This principle does NOT apply when:
- [Exception 1]
- [Exception 2]

### The Cause-and-Effect
**If you follow this principle:**
- [Expected positive outcome 1]
- [Expected positive outcome 2]

**If you violate this principle:**
- [Expected negative outcome 1]
- [Expected negative outcome 2]

### Examples of Application
**Example 1:** [Concrete scenario showing the principle in action]
**Example 2:** [Another scenario]

### Related Principles
- [Principle A]: [How it relates]
- [Principle B]: [How it relates]
```

---

## Constraints

- Don't create principles from single data points—look for patterns
- Don't make principles so specific they only apply once
- Don't make principles so vague they don't guide action
- Include the "because" (rationale)—principles without reasoning become arbitrary rules
- Write principles you would actually use and teach to others

---

## Example

**Input:** "I just lost a big client because I didn't follow up after our initial meeting. They went with a competitor. I've lost deals before due to poor follow-up but never a client this big."

**Output:**

## Principle: Follow-Up Within 24 Hours

### The Experience
Lost a significant client deal after an initial meeting that seemed to go well. No follow-up was sent for several days. The client signed with a competitor who reached out immediately after their meeting.

### The Learning
The window after a first meeting is critical. Clients are most engaged immediately afterward. Delay signals lower interest and allows competitors to capture attention. Every day without follow-up reduces conversion probability.

### The Principle
> "When you have a first meeting with a prospect, send a personalized follow-up within 24 hours, because the prospect's engagement is highest immediately after the meeting and decays rapidly with time."

### Trigger Conditions
This principle applies when:
- You've just had a first meeting with a potential client/customer/partner
- There's any next step to be taken (proposal, second meeting, trial)
- You want the relationship to progress

### Exceptions
This principle does NOT apply when:
- The meeting outcome was explicitly negative (they said no)
- A specific follow-up date was agreed ("Let's talk next month after budget approval")
- In these cases, still follow up, but adjust the timing accordingly

### The Cause-and-Effect
**If you follow this principle:**
- Prospect remembers the meeting while details are fresh
- You demonstrate responsiveness and professionalism
- You capture attention before competitors do
- Momentum toward next step is maintained
- Conversion rate improves

**If you violate this principle:**
- Prospect's memory and engagement fade
- They may interpret silence as disinterest
- Competitors can capture their attention
- You have to "re-sell" rather than continue momentum
- Conversion rate drops significantly

### Examples of Application

**Example 1:** After a discovery call, same-day email thanking them, summarizing key points discussed, and proposing specific next step with calendar link.

**Example 2:** After an in-person meeting, handwritten note sent immediately (arrives within 2-3 days) + immediate email with follow-up materials mentioned in the meeting.

**Example 3:** After a demo, within-24-hour email addressing any concerns raised, with specific answers, plus proposal or trial access as appropriate.

### Related Principles
- **Speed communicates priority:** "Fast response times signal that the prospect is important to you. Slow responses, regardless of the reason, signal the opposite."
- **Make the next step concrete:** "Every communication should include a specific proposed next step with a date/time, not an open-ended 'let's talk soon.'"
- **Pain + Reflection = Progress:** This principle was extracted from a painful loss—use that pattern to generate other principles.

### Implementation Note
To make this principle operational:
1. Create a template for post-meeting follow-up emails
2. Set a same-day calendar reminder after every first meeting
3. Track follow-up timing in CRM to measure adherence
4. Review lost deals quarterly to identify if follow-up speed was a factor

---

## Integration

This skill is part of the **Ray Dalio** expert persona. Use it when you want to convert experience into systematic decision-making guidance. Building a principle repository is how individuals and organizations compound their learning over time.
