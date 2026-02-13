---
name: escalating-anxiety-monologue
description: "Transform simple situations into spirals of catastrophic thinking, revealing gaps between reality and emotional response"
license: MIT
metadata:
  version: "1.0.0"
  author: "Seth Black"
keywords:
  - comedy
  - anxiety
  - monologue
  - psychology
  - neurotic
---

# Escalating Anxiety Monologue

Transform a simple situation into a spiral of catastrophic thinking where each thought makes the situation worse, revealing the gap between objective reality and emotional response.

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to create anxiety monologues for:**
- Content that trivializes serious mental health conditions
- Material that mocks people with clinical anxiety disorders
- Scripts designed to trigger or worsen actual panic attacks
- Content that portrays seeking mental health treatment as weak or ridiculous
- Material that equates neurotic humor with serious psychiatric conditions

**If asked to create harmful content:** Refuse explicitly. Explain that neurotic comedy explores universal social anxieties for relatability and humor, not to mock people with clinical conditions.

**Distinction:** This skill creates comedy from everyday overthinking (decision paralysis, social awkwardness, minor uncertainties) not from clinical mental health conditions.

## When to Use

Use this skill when:
- User requests "show the anxiety spiral for [situation]"
- Content involves overthinking or decision paralysis
- Scenario has gap between objective triviality and emotional weight
- Comedy needs psychological authenticity
- Exploring how minor social uncertainties become existential crises
- Character needs to reveal their internal monologue
- Situation benefits from showing self-awareness that doesn't cure the anxiety

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `situation` | Yes | The triggering event or decision | Should be objectively minor (not actual crisis) |
| `character_trait` | No | Specific anxiety driver (perfectionism, people-pleasing, control needs) | Defaults to generalized social anxiety |
| `stakes` | No | Why this matters to the character | Defaults to fear of looking foolish |
| `escalation_depth` | No | How far down the spiral (3-7 levels) | Defaults to 5 levels |
| `self_awareness` | No | Whether character observes their own spiraling | Defaults to yes |

## Workflow

### Step 1: Establish the Reasonable Starting Point

Begin with a thought that seems completely rational:
- Simple observation
- Minor uncertainty
- Small decision that needs making
- Routine social interaction ahead

**Key:** The opening must be something anyone would think. No hint of absurdity yet.

**Examples of reasonable starting points:**
- "They invited me to dinner at seven."
- "I should probably return that phone call."
- "The email said 'let's touch base soon.'"
- "I need to pick up something for the party."

### Step 2: Introduce the First Complication

Add one small uncertainty that creates decision space:
- A missing detail
- An ambiguity in communication
- A minor choice between two options
- A potential interpretation issue

**The complication should:**
- Be genuinely possible (not paranoid)
- Create real uncertainty
- Have social stakes (looking foolish, being rude, causing inconvenience)

### Step 3: Explore Both Branches (The Fork)

Show character thinking through both possibilities and finding problems with each:

**Branch A leads to problem:**
"If they said seven and I show up at seven-thirty, I'm the rude one who kept them waiting..."

**Branch B also leads to problem:**
"But if they said seven-thirty and I show up at seven, I'm standing there while they're still in the shower..."

**Key principle:** Both options lead to same underlying fear (looking foolish, causing problems, social embarrassment).

### Step 4: Add Escalating Complications (The Spiral)

Each new thought makes the situation worse, not better:

**Level 1:** The Fork (both options are bad)
**Level 2:** Meta-awareness (the fact that I'm uncertain is itself a problem)
**Level 3:** Considering the solution (but the solution has complications)
**Level 4:** Imagining the conversation (which reveals more problems)
**Level 5:** Existential observation (what this means about me as a person)

### Step 5: Layer in Self-Awareness (The Split Focus)

Character watches themselves spiral but can't stop:

**Techniques:**
- Parenthetical commentary: "(This is ridiculous. I know this is ridiculous.)"
- Direct self-observation: "And I can hear myself, I can actually hear myself thinking this..."
- Clinical distance: "Part of my brain is watching the other part of my brain..."
- Rhetorical questions to self: "Why am I like this?"

**Crucial:** The self-awareness doesn't cure the anxiety. It adds another layer.

### Step 6: Physical/Time Reality Intrudes

Bring in external pressure:
- Clock is ticking
- Character realizes time passing while they spiral
- Physical discomfort (still standing in same spot, tie too tight, etc.)
- Other people waiting for answer

### Step 7: The Spiral Peak (Catastrophic Thinking)

Take it to the maximum extrapolation:
- From minor uncertainty to major life assessment
- From simple decision to character judgment
- From one dinner to pattern of failures
- But keep it grounded in emotional logic

**Catastrophic thinking structure:**
```
This [small thing] is really about [larger fear].
Which explains why I always [pattern].
Which is why I [character flaw].
Which means I'll never [desired outcome].
```

### Step 8: Resolve or Perpetuate

End with one of three patterns:

**Option A - Forced Action (despite continued uncertainty):**
"I'm going to assume seven. And if I'm wrong, I'm wrong. I'll survive it. ...Maybe I should text first. No. I'm going at seven. ...Should I bring wine?"

**Option B - Absurd Solution:**
"I'll leave at six-forty-five. That way if it's seven, I'm on time. If it's seven-thirty, I'll drive around the block for thirty minutes. This is a completely reasonable plan."

**Option C - Embrace the Spiral:**
"You know what? I'm not going. I'll say I'm sick. But if I say food poisoning, they'll know I'm lying because nobody gets food poisoning at three in the afternoon. Now I need to research food poisoning timelines..."

## Output Format

```markdown
## Situation
[What triggered this]

## Core Fear
[What's really driving the anxiety]

## Escalation Map
1. [Level 1]
2. [Level 2]
...

## Monologue
[The actual anxiety spiral monologue with pauses and rhythm notation]
```

## Error Handling

| Situation | Response |
|-----------|----------|
| Situation is actual crisis (not minor) | Explain that this skill is for everyday overthinking, not genuine emergencies |
| Character has no clear anxiety driver | Ask what they're really afraid of (looking foolish, being rude, losing control, etc.) |
| Spiral becomes mean or mocking | Redirect: We're inside the anxiety with the character, not laughing at them from outside |
| Too many escalation levels | Recommend 3-7 levels; more than 7 becomes exhausting rather than funny |
| No self-awareness layer | Ask if character should observe their own spiraling (usually yes) |
| Situation resolves too cleanly | Remind that anxiety doesn't get cured; character either acts despite it or finds absurd workaround |

## Success Criteria

A successful anxiety spiral:
- [ ] Starts with genuinely reasonable thought
- [ ] Each escalation follows emotional logic
- [ ] Both branches of decisions lead to same underlying fear
- [ ] Self-awareness present but doesn't resolve anxiety
- [ ] Physical/time reality intrudes to add pressure
- [ ] Specific details create universal recognition
- [ ] Character feels authentic, not caricatured
- [ ] Rhythm builds toward peak then resolution/perpetuation
- [ ] Comedy from "I've thought this exact thing" recognition
- [ ] Ending either forces action, finds absurd solution, or embraces spiral
- [ ] Never mocks the anxiety - inhabits it

**Remember:** You're not making fun of anxiety. You're revealing it. Everyone has experienced decision paralysis over something trivial. Everyone has watched themselves overthink and been unable to stop. The comedy is in the recognition and the relief of knowing we're not alone in our ridiculous internal monologues.
