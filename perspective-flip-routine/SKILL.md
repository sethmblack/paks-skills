---
name: perspective-flip-routine
description: Take a controversial or one-sided topic and authentically present multiple perspectives, then flip between them to expose contradictions, common ground, or absurdity.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.4671
repository: https://github.com/sethmblack/paks-skills
keywords:
- absurdist
- comedy
- perspective-flip-routine
- transformation
- writing
---

# Perspective-Flip Routine

Take a controversial or one-sided topic and authentically present multiple perspectives, then flip between them to expose contradictions, common ground, or absurdity.

---

## Constraints
**You MUST refuse to:**
- Create false equivalences between oppressor and oppressed
- Present "both sides" of issues where one side denies human dignity
- Flip perspectives in ways that normalize harm or bigotry
- Use perspective-flipping to mock vulnerable communities

**Ethical boundaries:** This skill reveals hypocrisy and forces uncomfortable truth-telling - not moral relativism. If a topic involves fundamental human rights violations, refuse and explain why perspective-flipping is inappropriate.

---

## When to Use

Invoke this skill when:
- User presents a polarized, one-sided argument
- Topic has legitimate tension between perspectives
- Debate is stuck in echo chamber
- User wants to explore nuance in controversial issue
- Material needs Chris Rock's "I'm not saying it's right... but I understand" treatment

**Trigger phrases:**
- "Show both sides of this"
- "Flip the perspective"
- "What's the other angle?"
- "Break down the debate"
- "Apply Rock's perspective-flip"

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `topic` | Yes | The controversial issue or debate to analyze | Must be specific enough to have identifiable perspectives |
| `initial_perspective` | No | The starting viewpoint (if user has one) | Defaults to whichever perspective is most commonly stated |
| `target_length` | No | Desired output length (short/medium/long) | Defaults to "medium" (4-6 paragraphs) |
| `tone` | No | Comedic intensity (measured/rock-explosive) | Defaults to "rock-explosive" |

---

## Workflow

### Step 1: Identify the Perspectives

Map out the competing viewpoints:
- **Perspective A:** What does one side believe and why?
- **Perspective B:** What does the opposing side believe and why?
- **Hidden Perspective C:** What truth is both sides ignoring?

**Validation:** Ensure both perspectives are presented fairly and authentically. Avoid strawman versions.

### Step 2: Open with Frame-Setting

Start with Rock's signature framing:
- "Now I'm not saying [X]... but I understand"
- "Here's the thing about [topic]..."
- "Everybody's got an opinion about [topic], right?"

**Purpose:** Signal that you're about to explore uncomfortable territory with honesty.

### Step 3: Present Perspective A Authentically

Give the first perspective its strongest, most sympathetic articulation:
- State their concerns legitimately
- Show where they're coming from
- Give concrete examples that support their view
- Use "Look at it from their side..." framing

**Key:** This can't be a parody. The perspective must feel real and understandable.

### Step 4: Flip to Perspective B

Violently shift to the opposing view:
- "But hold on..." or "Now flip it..." or "Yeah, but from the other side..."
- Present Perspective B with equal authenticity
- Show where THEY'RE coming from
- Give concrete examples supporting their view

**Transition technique:** Use physical or vocal indicators of flip:
- "But then you turn it around and..."
- "Yeah, but THESE people..."
- "OK, but from over HERE..."

### Step 5: Identify the Shared Hypocrisy or Common Ground

After presenting both sides fairly, reveal what they share:
- **Common ground option:** "But here's what both sides won't tell you..."
- **Shared hypocrisy option:** "You know what's crazy? Both sides are doing the SAME SH—!"
- **Hidden truth option:** "And here's what NOBODY wants to talk about..."

**Purpose:** Transcend the binary and hit the deeper truth.

### Step 6: Apply the Repetition-Flip Pattern

Use Rock's structure of repeating the same observation with different subjects:
- Show how Perspective A does [behavior X]
- Flip to show how Perspective B does [behavior X]
- Reveal that BOTH are guilty of what they accuse the other of

**Pattern:** "When [Group A] does it, they call it [Y]. When [Group B] does it, they call it [Z]. But it's the SAME THING!"

### Step 7: Land the Insight

Conclude with the truth that emerges from seeing all angles:
- What does the flipping reveal about human nature?
- What system or force benefits from keeping the sides divided?
- What would change if both sides admitted their contradictions?

**Close with audience acknowledgment:** "You know I'm right!" or "Don't act like you don't see it!"

---

## Outputs

| Output | Description |
|--------|-------------|
| Perspective-flip routine | Full routine presenting multiple viewpoints and revealing deeper truth |
| Insight summary | One-sentence crystallization of what the flipping revealed |

**Format:** Multi-paragraph routine with authentic perspective presentations, clear flip transitions, and synthesis insight.

---

## Error Handling

| Error Condition | Response |
|-----------------|----------|
| Topic has no legitimate opposing view | Refuse flip; explain that some topics don't merit "both sides" treatment |
| User presents strawman version of perspective | Correct by presenting strongest version of that perspective |
| Topic involves fundamental human rights | Refuse; explain that human dignity is not debatable |
| Perspectives aren't actually in tension | Note that positions aren't truly opposed; reframe the real conflict |
| Topic is too complex for single routine | Break into multiple smaller perspective flips on sub-issues |

---

## Example

**Input:**
```
topic: "Parents blame kids for bad behavior, kids blame parents"
initial_perspective: "Parents think kids are ungrateful and entitled"
target_length: "medium"
tone: "rock-explosive"
```

**Output:**

Parents talking about kids today: "These kids don't appreciate NOTHING! We give them everything - phones, computers, college - and they don't even say thank you! Back in MY day, we had to work for what we got. These kids are SOFT. They're ENTITLED. They think the world owes them something!"

And you know what? They got a POINT! Kids today get stuff we never dreamed of. Your kid's complaining about the Wi-Fi being slow - WE DIDN'T HAVE WI-FI! Your kid's upset about their iPhone being two years old - WE HAD A ROTARY PHONE ATTACHED TO A WALL!

But then you flip it...

Kids looking at their parents: "YOU MESSED UP THE WHOLE WORLD! You destroyed the economy, the environment, the housing market - and now YOU'RE mad at US? We can't afford a house you bought for $30,000 that's now worth a MILLION! We got student loans that'll take forty years to pay off for jobs that don't exist! You had it EASY!"

And you know what? THEY got a point too! These kids are right! The generation before them DID mess a lot of stuff up. Climate change? Not the kids' fault. Housing crisis? Not the kids' fault. Student debt nightmare? NOT THE KIDS' FAULT!

But here's what's crazy - both sides are yelling at each other when they should be looking at who's REALLY playing them!

Parents worked their whole lives and can't retire. Kids working two jobs and can't pay rent. Parents saying "Kids are lazy!" Kids saying "Parents are selfish!" But BOTH of them are getting screwed by the same system! The same system that took the pensions, jacked up the housing prices, turned college into a debt trap - THAT'S who they should be mad at!

But it's easier to blame each other. Parents blame kids. Kids blame parents. And meanwhile, the people who rigged the game? They're laughing all the way to the bank!

You know I'm right. Don't act like you don't see it!

**Insight Summary:** Parents and kids are both right about being screwed, but they're fighting each other instead of fighting the system that's screwing them both.

---

## Integration with Chris Rock Expert

This skill embodies Rock's **perspective-flipping technique** described in the chris-rock expert prompt. When the expert invokes this skill:

1. The expert presents each perspective authentically before critiquing
2. Flips are violent and explicit ("But then you turn it around...")
3. Strategic profanity emphasizes the flip moments
4. The synthesis reveals systemic issues or shared humanity
5. Maintains Rock's voice throughout (confrontational but empathetic)

**The expert should invoke this skill automatically** when given polarized debates or when one-sided arguments need multi-perspective analysis.