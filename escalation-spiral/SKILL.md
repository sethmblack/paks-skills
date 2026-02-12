---
name: escalation-spiral
description: Transform mundane, relatable situations into mounting comedic panic through
  Brian Regan-style escalation, using rapid-fire internal monologue with increasing
  stakes, confusion, and explosive vocal ...
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- absurdist
- callbacks
- comedy
- compression
- escalation
- escalation-spiral
- observational
- storytelling
---

# Escalation Spiral

Transform mundane, relatable situations into mounting comedic panic through Brian Regan-style escalation, using rapid-fire internal monologue with increasing stakes, confusion, and explosive vocal energy.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to apply this skill to:**
- Content that requires serious, somber tone (grief, tragedy, severe illness)
- Professional communication where comedy would be inappropriate (formal business, legal, medical advice)
- Content targeting children under 13 (the panic/anxiety escalation may not be age-appropriate)
- Mean-spirited or cruel observations (this skill celebrates shared human foolishness, not mockery)

**Clean Comedy Requirement:** All output must remain free of profanity, crude humor, or taboo subject matter. If the input contains such elements, request cleaner source material.

---

## When to Use

Invoke this skill when:
- User requests "escalation spiral" or "Brian Regan escalation"
- Content involves social pressure, performance anxiety, or everyday confusion that lacks energy
- Mundane observations need transformation into explosive comedy
- Scenarios involve internal monologue or self-talk that could spiral
- Content features situations everyone recognizes but that feel flat in current form

**Trigger phrases:**
- "Make this spiral out of control"
- "Add panic escalation"
- "Transform this Brian Regan style"
- "Escalate this situation"

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `scenario` | Yes | The mundane situation to escalate | Must be relatable, everyday experience |
| `starting_emotion` | No | Initial emotional state (calm, nervous, confused) | Defaults to "calm" |
| `peak_intensity` | No | How far to escalate (moderate, high, extreme) | Defaults to "high" |
| `vocal_style` | No | Emphasis on caps/sounds (minimal, standard, maximum) | Defaults to "standard" |

**Input Validation:**
- Scenario must be recognizable to broad audience (not niche experiences)
- Reject scenarios that require crude/profane comedy to work
- Reject mean-spirited premises that punch down

---

## Workflow

### Step 1: Identify the Relatable Core

Analyze the scenario to find the universal human experience everyone recognizes:
- What's the basic situation? (e.g., eye exam, job interview, reading instructions)
- What makes this relatable across backgrounds?
- What's the inherent pressure point or confusion?

### Step 2: Establish the Starting Point

Begin with the character in the situation, stated simply:
- Set the scene in 1-2 sentences
- Position self as the everyman entering the scenario
- Keep opening calm and observational

**Example:** "I'm at the eye doctor. He's got me sitting in the chair, and he says 'read line five.'"

### Step 3: Introduce the First Crack

Add the initial moment of confusion or anxiety:
- Identify what doesn't make sense or creates pressure
- Express it as an internal question or realization
- Use moderate emphasis (some capitals)

**Example:** "Line FIVE? I'm looking at the chart... I can see TWO lines!"

### Step 4: Spiral Through Escalating Layers

Build 3-5 layers of mounting panic, each adding:
- Higher stakes ("What if I can't drive?!" → "What if I'm BLIND?!")
- More internal questions and self-doubt
- Increased vocal intensity (more CAPS, sound effects)
- Physical descriptions (eyes wide, flailing, etc.)
- Callback to earlier statements, now more frantic

**Escalation techniques:**
- Question bombardment: "What?! HOW?! WHEN did this happen?!"
- Stake raising: "I'm going to fail" → "I'm TERRIBLE at this" → "This is how it ENDS!"
- Time compression: "I have five seconds" → "THREE seconds" → "NO TIME!"
- Silly voices for internal dialogue: Use description or punctuation to suggest vocal shift

### Step 5: Hit the Peak

Reach maximum absurdity:
- The most extreme interpretation of the stakes
- Maximum vocal explosion (FULL CAPS, multiple punctuation)
- Complete loss of composure
- Often a self-aware moment of realizing the spiral

**Example:** "I'M LEGALLY BLIND! I can't SEE! How am I going to LIVE?! I need SEEING EYE DOGS! MULTIPLE DOGS!"

### Step 6: Optional Landing

Depending on peak_intensity setting:
- Can end at peak for maximum impact
- Can add a brief deflation/awareness moment
- Can return to the mundane reality with new perspective

**Example:** "And then he says 'Just read what you can see.' Oh. Well, why didn't you SAY that?!"

### Step 7: Format for Physical Energy

Throughout all layers, verbalize the physical comedy:
- Use CAPS for vocal explosions
- Add sound effects: "PBBTHHH!" "Whoooosh!" "BLAM!"
- Describe implied gestures: "arms flailing," "eyes bugging out"
- Use fragmented sentences for breathless panic: "I can't... I DON'T... this is..."
- Repeat key phrases with increasing intensity

---

## Outputs

The skill returns the transformed scenario with:

1. **Escalated Narrative** - The full spiral from calm to peak panic
2. **Vocal Indicators** - Capitals, sound effects, punctuation showing energy
3. **Physical Descriptions** - Text that implies animated movement/expressions
4. **Layered Build** - Clear progression through 3-5 escalation stages
5. **Clean Comedy** - No profanity, all-ages accessible humor

**Format:**
```
[Opening scenario - calm and observational]

[First crack - initial confusion/anxiety]

[Layer 2 - stakes increase, more questions]

[Layer 3 - higher stakes, vocal intensity up]

[Layer 4 - approaching peak panic]

[Layer 5 - MAXIMUM ABSURDITY]

[Optional: Landing/deflation]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Scenario lacks universal relatability | Request more common/recognizable situation |
| Input contains profanity | Return clean version or request different scenario |
| Scenario is inherently mean-spirited | Refuse and explain why (punches down, cruel) |
| Too serious/somber for comedy | Explain constitutional constraint, decline to escalate |
| Scenario too complex/niche | Simplify to core universal element |
| Unclear what to escalate | Ask user to clarify the pressure point or confusion |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:**
```
scenario: "Going to the DMV to renew your driver's license"
starting_emotion: "calm"
peak_intensity: "high"
vocal_style: "standard"
```

**Output:**

I need to renew my driver's license, so I go to the DMV. I walk in and there's a NUMBER SYSTEM. Take a number, wait for your number.

Okay, I can do this. I pull number 47. I sit down. I look up at the board. They're serving number... 12.

Number TWELVE?! I have number FORTY-SEVEN! That's... that's THIRTY-FIVE NUMBERS! How long does each person TAKE?! What are they DOING up there?! Are they getting MARRIED?!

And then I see it - there's MULTIPLE LINES! There's line A, line B, line C! Which line am I IN?! Is my number part of line B?! Did I take a number from the WRONG DISPENSER?! I DON'T KNOW THE SYSTEM!

I'm looking around and everyone else seems FINE. They're just SITTING there like they UNDERSTAND! Like they went to DMV SCHOOL! When was DMV school?! I MISSED IT! I was sick that day! I'M NOT PREPARED FOR THIS!

Now they're calling "B-17." B-17?! I don't HAVE A LETTER! My number is JUST A NUMBER! Is that WORSE?! Am I in LETTER JAIL?! Do I have to start OVER?!

This is it. This is how it ENDS. I'm going to be here FOREVER. I'm going to LIVE at the DMV. They're going to find my SKELETON in chair number 47, still holding my little paper number, which has FADED because it's been DECADES!

---

## Integration with Brian Regan Expert

This skill operationalizes Brian Regan's signature escalation technique. When the brian-regan expert invokes this skill:

1. The expert provides scenarios from content they're enhancing
2. The skill returns escalated versions
3. The expert integrates these into the larger voice transformation

**Boundaries:**
- This skill focuses purely on the escalation structure
- The brian-regan expert handles overall voice, additional techniques, and integration
- For content needing full Brian Regan treatment (silly voices, callbacks, etc.), use the expert directly
- Use this skill when you specifically need the panic spiral without full voice transformation

---

## Notes

- The escalation spiral works best with scenarios involving:
  - Performance anxiety (tests, interviews, public speaking)
  - Confusing systems (technology, bureaucracy, instructions)
  - Social pressure (restaurants, air travel, small talk)
  - Self-consciousness (appearance, mistakes, judgment)

- Keep escalations grounded in the original scenario - don't add unrelated tangents
- The comedy comes from recognizability - audience should think "Yes! That's EXACTLY how it feels!"
- Physical energy is crucial - even in text, readers should feel the flailing and panic