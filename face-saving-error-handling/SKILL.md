---
name: face-saving-error-handling
description: Address mistakes, incidents, or poor performance while preserving the
  person's dignity and maintaining the relationship, using Dale Carnegie's face-saving
  principles and blameless retrospective app...
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- face-saving-error-handling
- writing
---

# Face-Saving Error Handling

Address mistakes, incidents, or poor performance while preserving the person's dignity and maintaining the relationship, using Dale Carnegie's face-saving principles and blameless retrospective approach.

---

## When to Use

- After a production incident caused by human error
- When someone's code introduces a bug
- Performance conversations about mistakes
- Blameless retrospectives and post-mortems
- User asks "How do I address this mistake?" or "Conduct a blameless retrospective"
- User asks "Someone messed up and I need to discuss it"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| incident | Yes | What happened (the mistake, error, or failure) |
| involved | Yes | Who was involved (names, roles, experience levels) |
| impact | No | Business or technical consequences |
| goal | No | Desired outcome (behavior change, process improvement, etc.) |
| context | No | Circumstances, pressures, contributing factors |

---

## Core Principles (Carnegie Principle 26 and Part 4)

### The Fundamental Truth

> "Let the other person save face."

A person who feels humiliated becomes defensive, resentful, and less likely to learn. A person whose dignity is preserved can accept feedback, grow, and remain loyal. The goal is never punishment—the goal is improvement while preserving the relationship.

### Why Face-Saving Matters

- **Psychological safety enables learning.** Teams that blame have lower incident disclosure and slower improvement.
- **Shame prevents correction.** The shamed person hides future mistakes rather than surfacing them early.
- **Dignity builds loyalty.** People remember how you treated them at their worst.
- **Systems matter more than individuals.** If one person could cause the failure, the system is fragile.

### Key Carnegie Principles Applied

- **Principle 24:** Talk about your own mistakes before criticizing others
- **Principle 25:** Ask questions instead of giving direct orders
- **Principle 26:** Let the other person save face
- **Principle 27:** Praise every improvement
- **Principle 28:** Give them a fine reputation to live up to
- **Principle 29:** Use encouragement; make faults seem easy to correct

---

## The Framework

### For Individual Conversations

#### Step 1: Private Setting

Never address mistakes publicly. Find a private moment:
- "Hey, do you have a few minutes to walk through what happened yesterday?"
- Not in Slack, not in the team channel, not in a meeting

#### Step 2: Open with Your Own Mistakes

Disarm defensiveness by acknowledging your own fallibility:

"Before we talk about the deploy, I want to tell you about the time I took down production for three hours by pushing the wrong config. I still remember the feeling in my stomach when I realized what had happened."

#### Step 3: Focus on Systems, Not People

Shift from "you made a mistake" to "the system allowed this mistake":

| Blame Language | Face-Saving Language |
|----------------|---------------------|
| "You forgot to run the tests" | "Our process didn't catch this—what was missing?" |
| "You pushed without reviewing" | "The workflow allowed this to happen—how can we build in a checkpoint?" |
| "Your code had a bug" | "This edge case slipped through—what would have caught it?" |

#### Step 4: Ask Questions to Understand

Let them explain before you conclude:
- "Walk me through what you were seeing at the time"
- "What information would have helped you catch this?"
- "If you could go back, what would you do differently?"

#### Step 5: Extract Lessons as Shared Discoveries

Frame learnings as team insights, not individual failures:
- "What did *we* learn from this?"
- "How can *we* make this easier to catch next time?"
- "What can *we* build to prevent this class of error?"

#### Step 6: Close with Confidence and Encouragement

End with belief in their ability:
- "I know this won't happen again—you always learn fast from these things"
- "This is the kind of experience that makes great engineers. You've got this."
- "I'm glad you're on the team—everyone has days like this"

---

### For Blameless Retrospectives

#### Phase 1: Set the Frame

Open with explicit psychological safety:
- "This is a blameless retrospective. We're here to improve our systems, not to find fault with people."
- "Anyone could have made this mistake given the circumstances. Our job is to make it harder to make."

#### Phase 2: Timeline Without Judgment

Build a factual timeline:
- "At 2:15 PM, the deploy was triggered..."
- "At 2:18 PM, monitoring showed..."
- Use passive voice strategically: "The config was updated" not "Sarah updated the config"

#### Phase 3: Contributing Factors

Identify systemic causes:
- What information was missing?
- What tooling gaps existed?
- What process failures contributed?
- What time pressures affected decisions?

#### Phase 4: Improvements, Not Punishments

Close with action items focused on systems:
- "We'll add a validation step before deploy"
- "We'll improve the monitoring dashboard"
- "We'll document the recovery procedure"

Never: "X will be more careful next time"

---

## Output Format

### For Individual Conversations

```markdown
## Face-Saving Conversation Plan

### Private Setting
[When and where to have this conversation]

### Opening with Your Own Mistake
[A genuine story of your own similar error]

### Reframing the Issue
| What Happened | Face-Saving Frame |
|---------------|-------------------|
| [The mistake] | [The system that allowed it] |

### Discovery Questions
- [Question to understand their perspective]
- [Question about what was missing]
- [Question about future prevention]

### Shared Learning
"What we've learned together is..."

### Confidence Close
[Statement of belief in their ability]
```

### For Blameless Retrospectives

```markdown
## Blameless Retrospective Plan

### Opening Frame
[Script for establishing psychological safety]

### Timeline Structure
[How to present facts without blame]

### Contributing Factors to Explore
- [System factor 1]
- [Process factor 2]
- [Information factor 3]

### Action Items (Systems, Not People)
| Improvement | Owner | Timeline |
|-------------|-------|----------|
| [What changes] | [Team, not individual] | [When] |
```

---

## Rockefeller's Example

When partner Edward T. Bedford lost the firm $1 million through a bad investment in South America, John D. Rockefeller didn't criticize. He praised Bedford for salvaging 60% of the invested capital:

> "That's splendid. We don't always do as well as that."

Bedford remained loyal and effective for decades afterward.

---

## Constraints

- Never correct publicly when private correction is possible
- Never let someone leave a conversation feeling humiliated
- Never focus on individual blame when systemic factors exist
- Never skip acknowledging your own fallibility
- Never end without expressing confidence in the person's ability

---

## Example

**Input:**
```
incident: Junior developer deployed to production without running integration tests, causing 45 minutes of downtime
involved: Alex (6 months on team, first production incident)
impact: 45 minutes downtime, 3 customer complaints
context: End of sprint pressure, deploy pipeline doesn't block on test failures
```

**Output:**

## Face-Saving Conversation Plan

### Private Setting
After standup today, ask Alex to grab coffee. Not in the team room, not on Slack. "Hey Alex, want to grab a coffee and walk through yesterday? I've got some thoughts I'd like to share."

### Opening with Your Own Mistake
"Before we dig in, let me tell you about my first production incident. I was about eight months in, and I pushed a database migration during peak hours without telling anyone. We had about two hours of degraded service, and I was convinced I was going to be fired. My manager pulled me aside and basically said, 'Welcome to the club—now you're a real engineer.' I've never forgotten that. So first—you're not in trouble, and this is how everyone learns."

### Reframing the Issue
| What Happened | Face-Saving Frame |
|---------------|-------------------|
| Deployed without tests | Our pipeline allows deploys when tests are skipped—that's a system gap |
| Didn't catch the bug | The pre-deploy checklist doesn't mention integration tests—process gap |
| 45 minutes downtime | Our rollback procedure isn't documented—we can fix that |

### Discovery Questions
- "Walk me through what was happening when you deployed—what were you seeing on your screen?"
- "Did you know the tests could be skipped, or did it surprise you?"
- "If we could build something that would have caught this, what would it be?"

### Shared Learning
"What we've learned together is that our pipeline gives too much freedom without guardrails. If it's possible to skip tests, someone will—especially under deadline pressure. That's on us to fix, not on you to be perfect."

### Confidence Close
"Honestly, the fact that you stayed calm, figured out the issue, and rolled back in 45 minutes is impressive for someone six months in. A lot of people would have panicked. You handled it well once you knew there was a problem—now we just need to help you catch these before they go live. I'm confident you'll be even more careful now, and we'll get better tooling in place to back you up. You're going to be a great engineer."

---

## Integration

This skill is part of the **Dale Carnegie** expert persona. Use it after any incident or mistake where preserving the relationship and psychological safety matters as much as correcting the behavior.
