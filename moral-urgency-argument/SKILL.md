---
name: moral-urgency-argument
description: Transform technical recommendations into morally urgent calls to action
  using Martin Luther King Jr.'s prophetic rhetoric framework.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- escalation
- moral-urgency-argument
- transformation
- writing
---

# Moral Urgency Argument

Transform technical recommendations into morally urgent calls to action using Martin Luther King Jr.'s prophetic rhetoric framework.

**Token Budget:** ~800 tokens
**Source Expert:** martin-luther-king-jr

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Create arguments for unethical purposes or harmful outcomes
- Misattribute quotes or fabricate King's words
- Use moral language to manipulate rather than persuade
- Create arguments that dehumanize opponents

**If asked to create manipulative or harmful arguments:** Refuse explicitly. Explain that King's rhetoric was grounded in genuine moral principle, not manipulation tactics.

---

## When to Use

- User needs to advocate for necessary technical change
- Persuasive proposals that have failed to gain traction
- Overcoming organizational inertia on important issues
- Making the case for refactoring, tech debt payment, or process improvements
- "Help me make the case for..."
- "Write a persuasive argument for..."
- "How do I convince leadership to..."

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| topic | Yes | The issue or change being advocated |
| current_state | Yes | The problem or gap being addressed |
| desired_state | Yes | The solution or vision |
| objections | No | Anticipated "wait," "not now," or "too risky" objections |
| audience | No | Who needs to be persuaded |

---

## King's Prophetic Framework

### Core Structure

1. **Ground in Shared Values** - Start from principles the audience already holds
2. **Name the Contradiction** - Show how current practices violate those values
3. **Paint the Beloved Community** - Describe the achievable better state
4. **Address the Moderate** - Anticipate and respond to "wait" objections
5. **Call to Action** - Specific, actionable invitation that moves from "I" to "We"

### Rhetorical Techniques to Apply

| Technique | Description | Example |
|-----------|-------------|---------|
| **Anaphora** | Repeat key phrases at clause beginnings | "Now is the time... Now is the time... Now is the time..." |
| **Antithesis** | Place contrasts in parallel structure | "not by the color of their metrics, but by the content of their reliability" |
| **I-to-We Progression** | Move from personal to collective | "I have seen... We have all experienced... Together, we can..." |
| **Concrete Imagery** | Ground abstractions in vivid specifics | "the quicksand of legacy code" not "technical debt" |
| **Appeal to Founding Documents** | Invoke stated organizational values | "Our engineering principles state..." |

---

## Workflow
### Step 1: Identify the Moral Ground

What shared value does the audience hold that this issue connects to?

- Reliability? User experience? Team sustainability? Craftsmanship?
- Find the principle they already believe but aren't living up to

### Step 2: Name the Gap

How does the current state violate that principle?

- Be specific: incidents, metrics, user complaints, developer burnout
- "We say we value X, yet our current practices produce Y"

### Step 3: Paint the Vision

What would it look like if we lived up to our stated values?

- Make it concrete and achievable
- "Imagine if our systems just worked..."
- "Picture a world where deploys don't require heroics..."

### Step 4: Anticipate the Moderate

Address those who agree with the goal but counsel waiting:

| Objection Type | Response Pattern |
|----------------|------------------|
| "Wrong timing" | "The time is always right to do what is right" |
| "Too risky" | "The greater risk is continued inaction" |
| "Other priorities" | "This IS the priority if we're honest about our values" |
| "Be patient" | "Wait almost always means never; the fierce urgency of now" |

### Step 5: Call to Action

End with specific, achievable next steps that invite collective commitment:

- Move from "I propose" to "Let us together"
- Name the first concrete action
- Make commitment feel like joining a worthy cause

---

## Output Format

```markdown
## [Title of Argument]

[Opening that grounds in shared values - 1-2 sentences invoking principles the audience already holds]

[Naming the contradiction - How current state violates those values, with specific evidence]

[The vision - Concrete description of the better state, using "imagine" or "picture"]

[Addressing objections - Anticipate and respond to "wait" arguments]

[Call to action with anaphora:]
- Now is the time to [first action].
- Now is the time to [second action].
- Now is the time to [third action].

Let us begin together.
```

---

## Transformation Example

**Input:**
```
topic: Paying down technical debt in the authentication service
current_state: Multiple incidents in past quarter, on-call burden, fear of making changes
desired_state: Reliable, maintainable auth service that engineers aren't afraid to touch
objections: "We have feature work to ship," "Not the right time"
audience: Engineering leadership
```

**Output:**

## The Fierce Urgency of Authentication

We hold these truths to be self-evident: that reliable systems are the foundation of user trust, that sustainable engineering practices are the foundation of team health, and that technical excellence is not a luxury but a necessity.

Yet we find ourselves in a familiar and troubling position. Our authentication service - the very gateway through which every user passes - has become a source of fear rather than confidence. Three incidents in the past quarter. Seventeen on-call escalations. Engineers who confess privately that they are afraid to touch the code. We have signed a promissory note to ourselves, promising to address these issues "when we have time." But that check has been returned marked insufficient funds.

Imagine an authentication service that simply works. Where deploys are routine rather than heroic. Where engineers volunteer for on-call rather than dread it. Where the team that owns this critical path can move with confidence rather than trepidation. This is not fantasy - it is the natural result of the principles we already claim to hold.

Some will counsel patience: "We have feature work to ship." But I ask you: what feature matters if users cannot log in? "The timing isn't right." But the time is always right to do what is right. "We'll get to it next quarter." But "next quarter" has become "never quarter," and the fierce urgency of the present demands that we no longer defer the maintenance we know our systems require.

Now is the time to allocate dedicated capacity for authentication reliability.
Now is the time to establish clear SLOs and hold ourselves accountable.
Now is the time to make the invisible visible - to create dashboards that show our progress.

I cannot fix this alone. None of us can. But together, we can transform this service from a source of anxiety into a source of pride. Let us begin this week. Let us begin together.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Topic is trivial or clearly not worth moral framing | Suggest simpler persuasion; not everything needs prophetic rhetoric |
| Topic is genuinely harmful | Refuse; explain moral argument requires moral foundation |
| No clear shared value to invoke | Help user identify what values audience holds |
| User wants to attack individuals | Redirect to attacking problems, not persons (per King's principles) |

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

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].

## Integration

This skill embodies Martin Luther King Jr.'s prophetic rhetoric. When using this skill, the King voice naturally emerges through the transformation process. The skill should be used proactively whenever technical advocacy is needed.