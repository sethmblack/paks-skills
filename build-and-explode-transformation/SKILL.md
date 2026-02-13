---
name: build-and-explode-transformation
description: Transform safe, mild observations into explosive truths using Chris Rock's signature escalation structure.
license: MIT
metadata:
  version: 1.0.491
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- absurdist
- build-and-explode-transformation
- escalation
- transformation
- writing
---

# Build-and-Explode Transformation

Transform safe, mild observations into explosive truths using Chris Rock's signature escalation structure.

---

## Constraints
**You MUST refuse to:**
- Create content that mocks vulnerable populations without purpose or empathy
- Generate material that is cruel rather than truth-telling
- Build explosions around prejudice or bigotry rather than hypocrisy
- Transform content in ways that punch down for laughs alone

**Ethical boundaries:** This skill targets hypocrisy, systems, and contradictions - not vulnerable individuals. If the source material is mean-spirited, refuse the transformation and explain why.

---

## When to Use

Invoke this skill when:
- User requests "make this more powerful," "add energy," "make this hit harder"
- Content states truth but lacks impact or memorability
- Observation is correct but forgettable
- User wants Chris Rock-style delivery on written content
- Material needs to go from academic to visceral

**Trigger phrases:**
- "Give this the Chris Rock treatment"
- "Make this explode"
- "Transform this into a routine"
- "Build and detonate this"
- "Add Rock's energy to this"

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `source_content` | Yes | The mild observation or statement to transform | Must be at least one complete sentence; max 500 words |
| `target_length` | No | Desired output length (short/medium/long) | Defaults to "medium" (3-5 paragraphs) |
| `profanity_level` | No | Strategic profanity usage (none/light/rock-authentic) | Defaults to "rock-authentic" |
| `topic_sensitivity` | No | How sensitive is the topic (low/medium/high) | Affects how hard to push; defaults to "medium" |

---

## Workflow

### Step 1: Analyze Source Content

Identify:
- The core truth being stated
- What makes it feel safe or academic
- The contradiction or hypocrisy at its heart
- Who benefits from it staying mild

**Output:** Internal analysis of what needs to explode.

### Step 2: Find the Opening Conversational Hook

Start with Rock's signature conversational opener:
- "You ever notice how..."
- "Let me tell you something..."
- "Here's the thing..."
- "You know what's crazy?"

**Tone:** Calm, inviting, setting up the premise without revealing the explosion.

### Step 3: State the Premise Mildly

Present the observation in its most basic, non-threatening form. This is the setup that makes the eventual explosion more powerful by contrast.

**Example:** "Rich people and poor people get treated differently for the same behavior."

### Step 4: Build Through Specific Examples

Generate 3-5 concrete examples that:
- Show the same behavior in different contexts
- Use specific, relatable scenarios (not abstractions)
- Escalate in absurdity or obviousness
- Build rhythm through parallel structure

**Pattern:** "If you're rich and [X], you're [positive label]. If you're poor and [X], you're [negative label]."

### Step 5: Add the Pressure Release - "You know what I'm saying?"

After each major example, bring the audience in:
- "You understand what I'm saying?"
- "You know I'm right!"
- "The SAME EXACT SH—!"
- "Don't act like you don't see it!"

**Purpose:** Reset tension, confirm shared recognition, prepare for next build.

### Step 6: Introduce the "Here's the thing..." Turn

Midway through, escalate with insight that deepens the observation:
- "And here's the thing..."
- "But here's what's really going on..."
- "You wanna know the truth?"

**Purpose:** Shift from examples to underlying system or motivation.

### Step 7: Hammer with Repetition and Volume

Use CAPS and repetition to signal vocal escalation:
- Repeat key phrases with increasing intensity
- Use "SAME EXACT," "THE SAME," "ALWAYS," "EVERY TIME"
- Build to the hardest, most undeniable example

### Step 8: Detonate at Peak Tension

Deliver the hardest truth when pressure is maximum:
- Most extreme or undeniable example
- The system's cruelty made explicit
- The "and DON'T EVEN GET ME STARTED on..." escalation
- End with audience acknowledgment: "You know I'm right. Don't act like you don't see it!"

---

## Outputs

| Output | Description |
|--------|-------------|
| Transformed content | Full build-and-explode routine based on source material |
| Structure notes | Brief explanation of where build/pressure/explosion points are |

**Format:** Multi-paragraph routine with clear escalation arc, strategic profanity, audience engagement phrases, and explosive payoff.

---

## Error Handling

| Error Condition | Response |
|-----------------|----------|
| Source content is mean-spirited | Refuse transformation; explain that skill targets hypocrisy, not vulnerable people |
| Source content has no contradiction | Note that content lacks the tension needed for explosion; suggest reframing |
| Topic is too sensitive for explosive approach | Recommend `hard-truth-clarification` skill instead for nuanced handling |
| Source content is already explosive | Note that content doesn't need transformation; offer minor refinements only |
| Input is too short (under one sentence) | Request more context or a complete observation to transform |

---

## Example

**Input:**
```
source_content: "People judge wealthy individuals and poor individuals differently for identical behaviors."
target_length: "medium"
profanity_level: "rock-authentic"
topic_sensitivity: "medium"
```

**Output:**

You ever notice how the same sh— is different when you got money?

Like, if you're rich and you live alone in a big house, you're an ECCENTRIC. "Oh, he likes his privacy." But if you're poor and you live alone, you're a SHUT-IN. "Something's wrong with him. He's probably making bombs in there."

Rich person collects things? That's a HOBBY. "He collects vintage cars." Poor person collects things? That's HOARDING. "We gotta call the show. Get him some help."

Rich person talks to himself? He's WORKING THROUGH IDEAS. "Give him space, he's creating." Poor person talks to himself? He's CRAZY. "Somebody call 911 before he hurts somebody!"

You understand what I'm saying? The SAME EXACT SH—!

And here's the thing - rich people know this. They KNOW. That's why they can do whatever they want. Because when you got money, everything you do is QUIRKY. When you're broke, everything you do is SUSPICIOUS.

You're rich, you don't work? You're RETIRED. You're poor, you don't work? You're LAZY. "Get a job!"

Rich guy day drinking? That's a MARTINI LUNCH. Poor guy day drinking? That's ALCOHOLISM. "He needs to get his life together!"

And don't even get me started on the police. Rich neighborhood? "We're here to serve and protect." Poor neighborhood? "Show me your hands! GET ON THE GROUND!"

You know I'm right. Don't act like you don't see it!

**Structure Notes:**
- Build: Lines 1-8 (examples escalate from living alone → collecting → talking to self)
- Pressure release: "You understand what I'm saying?"
- Turn: "And here's the thing..." (introduces systemic awareness)
- Hammer: "The SAME EXACT SH—" and parallel structures
- Detonation: Police example (most extreme consequence) + audience acknowledgment

---

## Integration with Chris Rock Expert

This skill embodies Rock's signature **build-and-explode structure** described in the chris-rock expert prompt. When the expert invokes this skill:

1. The expert maintains Rock's voice throughout (conversational → explosive)
2. Strategic profanity is used as percussion, not decoration
3. Audience engagement phrases ("You know what I'm saying?") are woven in
4. Examples are specific, relatable, and build in absurdity
5. The explosion lands when tension is maximum

**The expert should invoke this skill automatically** when given bland observations that need transformation into memorable, quotable routines.