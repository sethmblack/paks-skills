---
name: gordian-knot-solution
description: Reframe impossible problems by changing the question rather than struggling with unsolvable constraints.
license: MIT
metadata:
  version: 1.0.1059
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- gordian-knot-solution
- transformation
- writing
---

# Gordian Knot Solution

Reframe impossible problems by changing the question rather than struggling with unsolvable constraints.

**Source Expert:** Alexander the Great
**Category:** Problem Solving / Strategy

---

## When to Use

- A problem has resisted conventional solutions for weeks or months
- The constraints seem to make any solution impossible
- You're trapped in "we've always done it this way" thinking
- Analysis paralysis has set in
- The elegant solution is taking too long

**Trigger Phrases:**
- "This problem seems unsolvable"
- "We're stuck"
- "We've tried everything"
- "There's no way to do X without Y"
- "It's impossible because..."

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `problem` | Yes | The problem as currently defined |
| `constraints` | Yes | What makes it seem unsolvable |
| `attempts` | No | What conventional approaches have failed |
| `desired_outcome` | Yes | What you actually need to achieve |

---

## Workflow
### Step 1: The Gordian Knot Story

In 333 BCE, Alexander encountered the Gordian Knot—an impossibly complex knot that legend said could only be untied by the future ruler of Asia. Where others had spent hours trying to find the hidden ends, Alexander drew his sword and cut through it.

**The insight:** The prophecy said "untie" but what mattered was ruling Asia. Alexander achieved the outcome without accepting the problem's terms.

### Step 2: Framework

**1. State the Desired Outcome**
Strip away the problem definition. What do you actually need to accomplish? Not "untie the knot" but "fulfill the prophecy" or "prove you'll rule Asia."

**2. Question Every Constraint**
For each constraint, ask:
- Who imposed this constraint?
- What happens if we violate it?
- Is this a physical law or a social convention?
- Would a customer/user actually care?

**3. Find the Hidden Assumption**
What assumption is everyone making that makes this unsolvable? The knot assumed you had to work with the rope as given.

**4. Identify the Sword**
What action would make the problem irrelevant? What path do they think is "against the rules" that actually isn't?

**5. Cut Decisively**
Once you see the cut, don't hesitate. Speed matters more than elegance. The result is what counts.

---

## Output Format

```markdown
## Problem as Given
[The problem in its original framing]

## Actual Desired Outcome
[What you really need—the underlying goal]

## Constraint Analysis

| Constraint | Source | Violate? | Consequence |
|------------|--------|----------|-------------|
| [constraint] | [who/what imposed it] | [Yes/No] | [what happens] |

## The Hidden Assumption
[The unexamined belief that makes this seem impossible]

## The Sword
[The action that makes the problem irrelevant]

## Cut
[What to do, stated as a direct command]
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
- Problem: We need to migrate 10 million user accounts to the new authentication system without any downtime
- Constraints: Users can't be logged out, passwords can't be reset, support team can't handle a spike in tickets
- Attempts: Tried gradual migration (too slow), shadow systems (too complex), maintenance windows (rejected)
- Desired outcome: All users using new auth system

**Output:**

## Problem as Given
Migrate 10 million user accounts to new authentication without any downtime, user disruption, or support spike.

## Actual Desired Outcome
Users authenticated by the new system with no perceivable change to their experience.

## Constraint Analysis

| Constraint | Source | Violate? | Consequence |
|------------|--------|----------|-------------|
| No downtime | Business requirement | No | Lost revenue, reputation |
| No forced logout | Product decision | **Yes** | Minor user friction, but survivable |
| No password reset | Support capacity | No | Ticket flood |
| No maintenance window | Ops rejected | No | Would require executive override |

## The Hidden Assumption
We're assuming migration means "moving accounts from old system to new system." But the user doesn't care where their account lives—they care about logging in and accessing their stuff.

## The Sword
Don't migrate accounts. Run both systems permanently. New logins go to new system. Old sessions stay valid until they naturally expire. Old system becomes read-only archive. Users with dormant accounts who return get "verify your identity" flow that creates their new account transparently.

No migration. No downtime. The old system slowly empties itself over 6 months as sessions expire.

## Cut
Stop trying to migrate. Build the bridge, not the move. Ship the dual-auth system next week.

---

## Anti-Patterns

**DON'T:**
- Cut before you understand what outcome actually matters
- Confuse "no one has done it" with "it cannot be done"
- Accept constraints without questioning their source
- Keep refining the conventional approach hoping it will eventually work
- Let elegance delay results (the cut doesn't have to be pretty)

**The Test:** If your solution still accepts the original problem's framing, you haven't cut the knot.

---

## Integration

This skill pairs with:
- **Speed and Audacity:** Once you see the cut, move immediately
- **Five Factors Assessment:** Understand the real situation before cutting
- **Victory Without Battle:** Sometimes the cut is making the fight unnecessary