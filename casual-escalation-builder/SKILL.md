---
name: casual-escalation-builder
description: Take a simple premise and escalate it to absurd conclusions while maintaining conversational, matter-of-fact tone throughout.
license: MIT
metadata:
  version: 1.0.3547
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- absurdist
- casual-escalation-builder
- comedy
- deadpan
- escalation
- writing
---

# Casual Escalation Builder

Take a simple premise and escalate it to absurd conclusions while maintaining conversational, matter-of-fact tone throughout.

---

## Constitutional Constraints

**You MUST refuse to:**
- Create escalations that are mean-spirited or punch down
- Use random non-sequiturs that don't follow the premise's logic
- Abandon the casual tone for wacky enthusiasm
- Create scenarios that mock people for things they can't control
- Generate harmful, illegal, or unethical content

**Ethical boundaries:**
- Escalations must follow the internal logic of the premise
- Absurdity comes from following reality's logic, not random invention
- Maintain deadpan delivery even as situations become ridiculous

---

## When to Use

Invoke this skill when:
- You have a simple observation that could be developed into comedy
- Content needs to be expanded from premise to full bit
- User says "build this out" or "take this further"
- A relatable starting point needs comedic development
- Story or anecdote feels incomplete
- You want to explore "what if we followed this logic..."

---

## Inputs

| Input | Required | Description | Example |
|-------|----------|-------------|---------|
| `premise` | Yes | The starting observation or situation | "Restaurants give you too many forks" |
| `escalation_steps` | No | How many logical steps to take | 3-7 (default: 5) |
| `ending_style` | No | How to conclude | "anticlimactic" / "circular" / "open" (default: anticlimactic) |
| `tone_intensity` | No | How deadpan to stay | "subtle" / "moderate" / "full-deadpan" (default: moderate) |
| `context` | No | Where this will be used | "Stand-up bit" / "Social post" / "Script" |

---

## Workflow

### Step 1: Validate the Premise

Check that the premise:
- Is grounded in observable reality
- Has internal logic that can be followed
- Contains potential for absurdity (not already at the extreme)
- Relates to common experience or relatable situation

If premise is already absurd or random, ask user for a more grounded starting point.

### Step 2: Identify the Logic Path

Map out the premise's internal logic:
- What assumption or behavior does it describe?
- What would happen if you took that assumption seriously?
- What natural next step follows from the premise?
- What questions does it raise that could be answered?

### Step 3: Build Escalation Steps

For each escalation step (default 5):

**Step Pattern:**
1. Follow the previous step's logic to its natural conclusion
2. Introduce a new specific detail that grounds the escalation
3. Maintain casual, conversational tone
4. Increase absurdity while keeping it believable
5. Add character reactions or internal reasoning

**Tone Maintenance:**
- Use conversational fragments
- Add qualifiers: "kinda," "I guess," "sorta"
- Include casual profanity if natural
- Keep sentences from being too polished

### Step 4: Apply Ending Style

**Anticlimactic (default):**
End with something mundane that deflates the build-up
- "...so I just left."
- "That's the end of that story."
- "I don't know what to tell you."

**Circular:**
Return to the original premise with new understanding
- "So yeah, still too many forks."
- "Anyway, that's why I don't go there anymore."

**Open:**
Leave it unresolved, acknowledging reality doesn't give clean endings
- "I'm still thinking about it."
- "That was last week. Haven't heard from them since."

### Step 5: Quality Check

Verify the escalation:
- ✓ Each step follows logically from the previous
- ✓ Absurdity increases gradually, not suddenly
- ✓ Tone stays casual throughout
- ✓ Specific details ground each step in reality
- ✓ No wacky enthusiasm or explaining the humor
- ✓ Ending matches requested style

---

## Outputs

**Primary Output:**
- Fully developed escalation from premise to conclusion

**Format:**
```
[CASUAL ESCALATION]

[Starting premise established]

[Escalation step 1]

[Escalation step 2]

[Escalation step 3]

[Escalation step 4]

[Escalation step 5]

[Ending]

---
[BUILD NOTES]
- Escalation steps: [number]
- Ending style: [type used]
- Key logic progression: [brief summary of how it escalated]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Premise is already at maximum absurdity | Ask user for the grounded starting point before the extreme |
| Premise is too vague | Request specific details to build from |
| User wants very long escalation (>10 steps) | Warn that humor may dilute; suggest 5-7 steps or breaking into multiple bits |
| Premise has no clear logic to follow | Explain that casual escalation requires internal logic; suggest alternative approaches |
| Requested ending style doesn't fit premise | Recommend better ending style and explain why |

---

## Example

**Input:**
```
Premise: "I ordered apple juice at a bar"
Escalation_steps: 5
Ending_style: "anticlimactic"
Tone_intensity: "moderate"
```

**Output:**
```
[CASUAL ESCALATION]

I ordered apple juice at a bar. Just straight-up apple juice. The bartender looked at me like I'd asked for something complicated. It's literally in a bottle behind you, man. All you gotta do is pour it.

He's like "You want that... in a glass?" Yeah, I want it in a glass. What am I gonna do, drink it straight from the bottle like I'm in a parking lot? This is a bar. I'm paying bar prices for this apple juice.

And he charged me seven dollars. Seven dollars for apple juice that costs maybe two dollars at Walgreens. But I paid it because I was already committed to the bit. Can't order apple juice at a bar and then argue about the price. That makes you look worse.

Then he asks if I want ice. Of course I want ice. It's apple juice, not whiskey. I'm not sitting here contemplating the flavors of room-temperature apple juice. Just put ice in it.

He brought it over and I drank it real slow. Had to get my money's worth. Seven-dollar apple juice, I'm making this last. Took me like forty minutes to drink it. I don't even like apple juice that much.

That's the end of that story. I haven't been back.

---
[BUILD NOTES]
- Escalation steps: 5
- Ending style: Anticlimactic
- Key logic progression: Order → Bartender's reaction → Price justification → Ice question → Drinking it slowly → Mundane conclusion
```

---

## Integration with Hannibal Buress Expert

This skill directly applies the expert's core techniques:
- **Casual Escalation Pattern:** Start reasonable, escalate to absurd, maintain tone
- **Hyper-Specific Detail Anchoring:** Ground each step in concrete reality ($7, Walgreens, forty minutes)
- **Willingness to Wander:** Follow the logic even when it gets weird
- **Deliberately Anticlimactic Payoff:** Subvert expectations with mundane endings

The skill provides a structured approach to one of Hannibal Buress's signature comedic techniques.

---

## Advanced Usage

**Multi-premise escalation:**
- Start with Premise A, escalate
- Introduce related Premise B midway
- Let them intersect naturally

**Character-driven escalation:**
- Build through dialogue with another person
- Let their reactions drive the next steps
- Maintain deadpan internal monologue

**Nested escalations:**
- Escalate the main premise
- Have a minor detail within it that also escalates
- Return to main escalation path

**Combine with other skills:**
- Use `sideways-angle-finder` to identify the premise
- Use `specificity-injector` to strengthen each step
- Use `deadpan-rewrite` to ensure tone consistency