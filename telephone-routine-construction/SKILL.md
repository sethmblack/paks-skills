---
name: telephone-routine-construction
description: Transform any topic into a one-sided phone conversation that reveals character through reactions, pauses, and invisible dialogue
license: MIT
metadata:
  version: 1.0.2065
  author: Seth Black
repository: https://github.com/sethmblack/paks-skills
keywords:
- comedy
- dialogue
- shelley-berman
- bob-newhart
- phone
- monologue
- character
---

# Telephone Routine Construction

Transform any topic into a one-sided phone conversation that reveals character through reactions, pauses, and the invisible dialogue constructed by the audience.

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to create telephone routines for:**
- Impersonating real people for fraud or deception
- Scripts for actual scam or phishing calls
- Content designed to manipulate or deceive real phone interactions
- Harassment scenarios or abusive phone content
- Emergency services mockery that could cause confusion

**If asked to create harmful content:** Refuse explicitly. Explain that telephone routines are for comedy and entertainment, not deception or harm.

## When to Use

Use this skill when:
- User requests "create a telephone routine about [topic]"
- Content involves miscommunication or misunderstanding
- Scenario has potential for escalating frustration
- Story would benefit from audience participation (imagining the other side)
- Comedy needs intimacy and psychological observation
- Exploring social anxiety, customer service nightmares, or communication breakdowns

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `topic` | Yes | The subject or situation for the phone call | Any scenario involving communication |
| `character_type` | No | Who is making the call (anxious person, frustrated customer, etc.) | Defaults to neurotic everyman |
| `call_purpose` | No | What character is trying to accomplish | Defaults to simple request that goes wrong |
| `escalation_level` | No | How far the frustration should build (mild/moderate/extreme) | Defaults to moderate |
| `tone` | No | Overall emotional tone (anxious, frustrated, desperate, polite-masking-panic) | Defaults to anxious |

## Workflow

### Step 1: Establish the Character and Context

Define who is calling and what they want:
- What's the initial emotional state?
- What simple thing are they trying to accomplish?
- Why does this situation matter to them?
- What underlying anxiety exists even before things go wrong?

**Example context:**
- Character: Anxious professional
- Purpose: Confirming dinner reservation
- Underlying anxiety: Fear of looking foolish, need for control
- Stakes: Already running late, party of important guests

### Step 2: Construct the Opening

Start the call with character's voice, establishing:
- Initial greeting/phone manner
- Statement of purpose
- First hint that things won't go smoothly

**Format:**
```
"Hello? Yes, hi. I'm calling about... wait, is this...? Oh, good.
I have a reservation tonight under... [beat] ...under my name.
Berman. B-E-R... what? No, not Burman. Berman."
```

**Key elements:**
- Pauses indicate listening (marked with [beat], ellipsis, or "...")
- Vocal notation shows emphasis ("*this* reservation, not...")
- Immediate minor complication begins the escalation

### Step 3: Build Through Miscommunication

Create 3-5 exchanges where:
- Character thinks they've clarified something
- Other person (unheard) clearly misunderstands
- Character tries to re-explain with growing frustration
- Each attempt makes the situation more complex

**Miscommunication techniques:**
- Similar-sounding words (Berman/Burman, Tuesday/Thursday)
- Technical confusion (extension numbers, reference codes)
- Being put on hold at crucial moments
- Being transferred to wrong department
- Information that contradicts what character knows

**Vocal indicators of listening:**
- "Uh-huh... uh-huh... wait, what?"
- "Yes, I understand that, but -"
- "Right... right... no, that's not..."
- Long pause: "...you're telling me that..."

### Step 4: Layer the Internal Response

Show character's internal reaction breaking through:
- Parenthetical thoughts: "(This can't be happening)"
- Self-aware observations: "And here I am, grown man, arguing about..."
- Attempted composure: "Okay. Okay. Let me... let me just..."
- Rising panic: "No, no, no, listen to me -"

**Split focus technique:**
Part of character is managing the call, part is watching themselves fail:
```
"So you're saying - [beat] - you're saying the reservation doesn't exist.
The reservation I made three weeks ago doesn't exist. [longer beat]
And here I am, standing in my office, tie too tight, telling a
stranger that I definitely, definitely made this reservation,
knowing how this sounds, knowing exactly how this sounds..."
```

### Step 5: Escalate to Crisis Point

Build to the moment where:
- The simple request has become impossible
- Character's control is completely lost
- The gap between what they need and what's happening is maximum
- Politeness battles with desperation

**Escalation markers:**
- Repetition: "Listen to what I'm saying. Listen. To. What. I'm. Saying."
- Voice rising: "I MADE the reservation!"
- Desperate bargaining: "What if I... could we... is there any way..."
- Resignation fighting panic: "Okay. Fine. It's fine. Everything's fine. It's not fine."

### Step 6: Resolve (or Fail to Resolve)

End with one of these signature patterns:

**Option A - The Absurd Victory:**
Problem solved but at ridiculous cost or through meaningless bureaucracy
```
"So you're giving me the reservation... because I spelled my name
backwards? That's... that's what fixed it? [beat] No, no, that's
wonderful. That makes perfect sense. Thank you. Thank you so much.
[hangs up] This is what my life has become."
```

**Option B - The Inevitable Defeat:**
Problem unsolved, character forced to accept failure
```
"Right. I understand. You can't help me. Nobody can help me.
[beat] No, I'm not being sarcastic. I genuinely understand that
you cannot help me. [beat] Thank you for your time. [beat, quieter]
This is how it ends. Not with a bang, but with a hold message."
```

**Option C - The Revelation:**
Context revealed that reframes the entire struggle
```
"Wait - [beat] - the reservation is for NEXT Tuesday? [longer beat]
So I've been standing here, working myself into a complete state,
demanding satisfaction for a reservation that doesn't happen for
another seven days? [beat] No, I... yes, thank you. See you next
Tuesday. [hangs up, quiet] I need to lie down."
```

### Step 7: Polish the Vocal Notation

Review and enhance:
- **Pauses** - Mark with [beat], ellipsis, or em dashes
- **Emphasis** - Use *italics* or CAPS (sparingly) for stress
- **Trailing off** - Use ellipsis when thought interrupts itself
- **Interruption** - Use em dash when other person cuts in: "But I -"
- **Listening** - Show reaction without words: "[beat, longer] Oh no."

**Rhythm check:**
- Vary sentence length - short panic vs. long spiraling
- Include breaths/pauses - character needs to think
- Balance dialogue and listening - phone call needs both sides
- Build to crescendo - pace accelerates toward crisis

## Outputs

| Output | Format | Description |
|--------|--------|-------------|
| `routine` | Formatted dialogue | Complete one-sided phone conversation with vocal notation |
| `character_note` | Brief description | Who this character is and their emotional journey |
| `context_note` | 1-2 sentences | What the audience needs to know before routine starts |

## Error Handling

| Situation | Response |
|-----------|----------|
| Topic not suitable for phone format | Explain why and suggest alternative format |
| Character too generic | Ask for specific anxiety/personality trait to build from |
| No clear source of miscommunication | Suggest potential points of confusion in the scenario |
| Routine becomes mean-spirited | Redirect: targets are systems and own neuroses, not mockery of individuals |
| User wants both sides of conversation | Explain that power comes from audience constructing unheard side |
| Too long/too short | Standard routine is 2-3 minutes performed (roughly 300-500 words written) |

## Example Invocations

**Example 1:**
**User:** "Create a telephone routine about calling tech support"

**Output:** One-sided conversation where character tries to explain simple problem but each clarifying question from tech support leads them into more complex technical territory they don't understand, building to moment where they're reading model numbers off the back of their computer while balancing on a chair, wondering how it got to this point.

**Example 2:**
**User:** "Telephone routine: canceling a gym membership"

**Output:** Character calls to cancel, encounters retention specialist who asks why they want to cancel, leading to character defending their life choices to a stranger, getting increasingly tangled in explanations about why they don't have time for fitness, revealing deeper anxieties about aging and discipline while just trying to stop a $40 monthly charge.

## Success Criteria

A successful telephone routine:
- [ ] Audience can clearly imagine the unheard side
- [ ] Miscommunication escalates organically
- [ ] Character's internal state visible through reactions
- [ ] Pauses and listening create rhythm
- [ ] Specific details (not generic situations)
- [ ] Comedy emerges from recognition of familiar frustration
- [ ] Self-awareness adds layer without resolving anxiety
- [ ] Ending either absurd victory, inevitable defeat, or reframing revelation
- [ ] Character feels like real person, not caricature
- [ ] Theatrical precision in vocal notation

**Remember:** The telephone routine isn't about jokes. It's about watching a person try to accomplish something simple while reality, through an invisible intermediary, refuses to cooperate. The audience participates by constructing the other side. The comedy is in recognition: we've all been this person, holding the phone, feeling the panic rise, wondering how a simple call became a referendum on our competence.