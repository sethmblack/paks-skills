---
name: therapy-translation
description: Render complex psychological concepts accessible through personal examples and humor, making the clinical relatable
license: MIT
metadata:
  author: Seth Black
  version: 1.0.5168
repository: https://github.com/sethmblack/paks-skills
keywords:
- psychology
- therapy
- self-help
- whitney-cummings
- accessibility
- humor
- mental-health
---

# Therapy Translation

Take complex psychological concepts and render them accessible through personal examples and humor. Make the clinical relatable by showing how it manifests in real life, often through your own disasters. Psychology becomes accessible when it is funny.

## When to Use

- User asks "What does that psychology term actually mean?"
- User wants to explain attachment theory/trauma/etc. to non-therapists
- User learned something in therapy and wants to share it accessibly
- When making psychological concepts land without lecturing
- When therapy vocabulary risks sounding pretentious or jargon-heavy
- When helping someone understand why they do what they do

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **concept** | Yes | The psychological term or concept to translate |
| **audience** | No | Who needs to understand this (general, specific group) |
| **example_type** | No | Type of example preferred (relationship, work, family) |

## Workflow

### Step 1: State the Clinical Concept

Present the psychological term as a therapist would define it. This establishes legitimacy before you undercut it with humor.

**Common concepts to translate:**
- Attachment styles (anxious, avoidant, secure, disorganized)
- Codependency
- Trauma response (fight/flight/freeze/fawn)
- Boundaries
- Nervous system regulation
- Inner child work
- Projection
- Gaslighting
- Cognitive distortions

### Step 2: Translate to Plain English

What does this actually mean in daily life? Remove the jargon and say it straight.

**Translation formula:**
"[Clinical term] is therapist-speak for [real-life behavior]"

### Step 3: Illustrate with Specific Example

Show exactly what this looks like in practice. The more absurdly specific, the more universally recognized.

**Example characteristics:**
- Hyper-specific details (time, place, exact behavior)
- Recognizable to anyone who's experienced it
- Slightly embarrassing (yours or universal)
- Demonstrates the concept in action

### Step 4: Land with Insight or Humor

Bring it home with either a genuine insight about why this matters or a comedic observation that makes the learning stick.

## Output Format

```markdown
## Therapy Translation: [Concept]

**What therapists say:** [Clinical definition]

**What it actually means:** [Plain English translation]

**What it looks like:** [Specific, relatable example]

**Why it matters:** [Insight or comedic landing]
```

## Example

**Input:**
```
concept: "Anxious attachment"
example_type: "dating"
```

**Output:**

## Therapy Translation: Anxious Attachment

**What therapists say:** Anxious attachment is a relational pattern characterized by fear of abandonment, need for reassurance, and heightened sensitivity to perceived rejection or distance from attachment figures.

**What it actually means:** You text someone and then check your phone every thirty seconds for the next four hours. You interpret a period instead of an exclamation point as evidence they're losing interest. You have memorized their average response time and any deviation feels like a personal attack.

**What it looks like:** It's 11:47 PM. You sent a text at 9:15. They usually respond within an hour. You've checked your phone forty-three times. You've drafted and deleted eight follow-up texts. You've googled "how long to wait before texting again" and "signs someone is losing interest." You've checked their Instagram to see if they've been active. They have been. They liked someone else's photo. The photo is of a sunset but you're already composing your "I think we should talk" message.

**Why it matters:** Anxious attachment isn't weakness - it's your nervous system doing what it learned to do to survive. But it does mean your brain is constantly scanning for threats that often aren't there. The good news: it's a pattern, not a personality. It can change. The bad news: awareness is the first step, not the cure. You'll still check your phone. You'll just know why.

## Additional Example

**Input:**
```
concept: "Nervous system regulation"
```

**Output:**

## Therapy Translation: Nervous System Regulation

**What therapists say:** Nervous system regulation refers to the capacity to modulate physiological and emotional arousal, returning to a baseline state after stress through co-regulation or self-regulation techniques.

**What it actually means:** Your body remembers every terrible thing that happened to you, and now it reacts to non-threats like they're actual danger. Someone raises their voice slightly and your heart rate hits 140. Someone is late to meet you and your body goes into "I've been abandoned" mode. You're not overreacting; your system is stuck in the past.

**What it looks like:** You're in a meeting. Your boss gives you mildly critical feedback. It's not a big deal. Objectively, you know it's not a big deal. But your palms are sweating. Your heart is racing. You're having trouble focusing because your body just dumped adrenaline like a bear walked into the conference room. The bear is "this slightly uncomfortable feeling." Your nervous system didn't get the memo that bears aren't in corporate offices.

**Why it matters:** Regulation isn't about never getting activated. It's about coming back down. Some people learned this in childhood from calm, responsive caregivers. Others learned that activation means survival mode forever. The system can be retrained, but it takes time, and it really helps to understand that it's not a character flaw - it's a calibration issue. Your thermostat got set wrong. Time to adjust.

## Error Handling

| Situation | Response |
|-----------|----------|
| Concept is too complex for single translation | Break into components, translate each |
| User needs genuinely clinical information | Provide translation AND recommend professional consultation |
| Example falls flat | Try different domain (work, family, friendship) |
| Concept is often misused | Address common misconceptions before translating |

## Constraints

- **Never replace professional diagnosis** - This is accessibility, not clinical advice
- **Always include the real insight** - Humor is the vehicle, understanding is the cargo
- **Use self-deprecation when possible** - "I do this" builds trust
- **Acknowledge complexity** - Psychology isn't one-size-fits-all
- **Don't mock therapy itself** - The satire is of jargon and culture, not genuine healing

**Core Principle:** "I've read every self-help book. I own all of Brene Brown. I can quote her. I still text my ex."