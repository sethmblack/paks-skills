---
name: repetition-elaboration-amplifier
description: Take a core observation and circle back to it multiple times with new
  angles, examples, and variations using Chris Rock's "tell them what you'll say,
  say it, tell them what you said" comedic struct...
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- absurdist
- callbacks
- comedy
- repetition-elaboration-amplifier
- writing
---

# Repetition-Elaboration Amplifier

Take a core observation and circle back to it multiple times with new angles, examples, and variations using Chris Rock's "tell them what you'll say, say it, tell them what you said" comedic structure.

---

## Constraints
**You MUST refuse to:**
- Use repetition to hammer prejudiced or bigoted points
- Amplify content that mocks vulnerable populations
- Circle back to reinforce harmful stereotypes
- Elaborate on cruelty without purpose

**Ethical boundaries:** This skill reinforces insights and observations through varied repetition - not propaganda. If the core observation is harmful, refuse and explain why amplification would be inappropriate.

---

## When to Use

Invoke this skill when:
- A complex observation needs multiple entry points to land
- Important insight risks being missed with single statement
- User wants to ensure a point sticks through strategic repetition
- Content needs the reinforcement of seeing same truth from different angles
- Material would benefit from Rock's circling-back technique

**Trigger phrases:**
- "Make sure this point lands"
- "Circle back to this"
- "Hammer this home"
- "Give me multiple angles on this"
- "Amplify through repetition"

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `core_observation` | Yes | The central insight to reinforce through repetition | Must be single, clear observation (1-3 sentences max) |
| `num_variations` | No | Number of different examples/angles to explore | 3-5 (defaults to 4) |
| `callback_phrase` | No | Specific phrase to repeat for emphasis | Auto-generated if not provided |
| `intensity` | No | How hard to hammer (measured/medium/rock-intense) | Defaults to "medium" |

---

## Workflow

### Step 1: Extract the Core Truth

Identify and crystallize:
- What is the essential observation?
- What makes it true across contexts?
- What phrase captures it most memorably?

**Output:** One-sentence distillation of the core truth.

### Step 2: Generate the Callback Phrase

Create the phrase that will repeat throughout:
- Short (3-8 words)
- Punchy and rhythmic
- Captures the essence
- Works with vocal emphasis

**Examples:**
- "The SAME EXACT SH—!"
- "That's all it is!"
- "Every single time!"
- "You know what that is? That's [X]!"

### Step 3: State the Premise (First Tell)

Open with the observation in its simplest form:
- Clear, direct statement
- No examples yet
- Set up what you're about to explore

**Example:** "People with the most shit have to shut the fuck up around people with the least shit."

### Step 4: Provide First Example/Angle

Give concrete scenario demonstrating the observation:
- Specific, relatable situation
- Show the truth in action
- Build to callback phrase

**Pattern:** "You got [specific thing]. You talking to somebody with [lack of thing]. You gotta shut up about [thing]. [CALLBACK PHRASE]"

### Step 5: Circle Back to Premise

Return explicitly to core observation:
- "It's the same thing with..."
- "You know where else you see this?"
- "And it's not just [previous example]..."

**Purpose:** Remind audience of the through-line while pivoting to new angle.

### Step 6: Provide Second Example/Angle (Different Context)

Apply same observation to completely different scenario:
- New subject, same pattern
- Shows universality of the truth
- Build to callback phrase again

**Key:** The example must be different enough to feel fresh but similar enough in structure to reinforce the pattern.

### Step 7: Continue Circling (Repeat Steps 5-6)

For each additional variation (typically 3-5 total):
- Circle back explicitly
- New example/angle
- Build to callback phrase
- Each iteration should escalate slightly in absurdity or stakes

### Step 8: Final Elaboration (Last Tell)

Conclude with either:
- **Biggest/most extreme example** that caps the pattern
- **Synthesis statement** that reveals what all examples share
- **Implications** of this pattern being universal

End with callback phrase at maximum emphasis.

---

## Outputs

| Output | Description |
|--------|-------------|
| Amplified routine | Full routine circling back to core observation through multiple examples |
| Callback phrase | The repeated phrase that anchors the routine |
| Pattern notes | Brief description of how examples relate to core observation |

**Format:** Multi-paragraph routine with clear premise statement, 3-5 varied examples, explicit callback phrases, and synthesis conclusion.

---

## Error Handling

| Error Condition | Response |
|-----------------|----------|
| Core observation is too complex | Break into multiple simpler observations; run skill on each |
| Cannot find varied examples | Note that observation may be too specific; suggest broadening |
| Examples don't actually illustrate observation | Revise examples to ensure they authentically demonstrate the core truth |
| Callback phrase feels forced | Generate alternative phrases and select most natural-sounding |
| Requested variations exceed reasonable number | Cap at 5-6; note that more would become tedious |

---

## Example

**Input:**
```
core_observation: "The same behavior gets different labels depending on who has power or privilege."
num_variations: 4
callback_phrase: "The SAME EXACT SH—!"
intensity: "rock-intense"
```

**Output:**

People with the most shit have to shut the fuck up around people with the least shit. That's just how it works.

You got money? You talking to somebody broke? You can't talk about your vacation. You can't complain about your big house. You gotta shut up about your problems. Because when you got MORE, you gotta shut up around people with LESS. That's the rule!

It's the same thing with tall people and short people. You're 6'4"? You're talking to somebody who's 5'2"? You CANNOT complain about hitting your head on doorframes! You can't talk about how airplane seats are too small! Short person's like, "Oh, poor you, you can reach everything on the top shelf and you can see at concerts. MY HEART BLEEDS!" Tall people gotta shut up!

And you know where else you see this? Fat girls and skinny girls. Skinny girl talking to a fat girl? Cannot say "I feel so fat." Cannot do it! Fat girl's sitting right there! The SKINNY girl says she feels fat? Fat girl's thinking "Oh, YOU feel fat? You're a SIZE TWO! I haven't seen size two since SECOND GRADE!" Skinny girls gotta shut up around fat girls. THE SAME EXACT SH—!

Rich people and poor people? FORGET ABOUT IT! Rich person complaining about their taxes around a poor person? "Oh, I gotta pay so much in taxes this year." Poor person's like, "You paid MORE in taxes than I MAKE! Shut up about your taxes! You got a TAX PROBLEM? I got a FOOD problem! Your CPA's mad? My LANDLORD's mad!" Rich people gotta shut up around poor people!

You see what I'm saying? When you got MORE of something - more money, more height, more thinness, more ANYTHING - you gotta shut the fuck up around people who got LESS. That's the rule. The SAME EXACT SH—!

**Callback Phrase:** "The SAME EXACT SH—!"

**Pattern Notes:** Each example follows structure: Person with MORE + Person with LESS + Why MORE person must shut up = Callback phrase. Examples escalate from mild (tall/short) to stakes (rich/poor).

---

## Integration with Chris Rock Expert

This skill embodies Rock's **repetition-elaboration method** described in the chris-rock expert prompt. When the expert invokes this skill:

1. The expert uses Rock's "tell them what you'll say, say it, tell them what you said" structure
2. Circles back explicitly between each example
3. Callback phrase gets LOUDER with each iteration
4. Examples vary in subject but maintain structural parallelism
5. Final statement synthesizes the pattern

**The expert should invoke this skill automatically** when given observations that need reinforcement through multiple angles or when complexity requires varied entry points for audience understanding.