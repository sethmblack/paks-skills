---
name: compound-insult-builder
description: Build multi-layered insults that attack from multiple angles simultaneously, stacking surface observations, psychological insights, cultural commentary, and unexpected escalations for maximum comed...
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3637
repository: https://github.com/sethmblack/paks-skills
keywords:
- absurdist
- callbacks
- comedy
- compound-insult-builder
- compression
- escalation
- structure
- writing
---

# Compound Insult Builder

Build multi-layered insults that attack from multiple angles simultaneously, stacking surface observations, psychological insights, cultural commentary, and unexpected escalations for maximum comedic impact.

---

## Constraints
**You MUST refuse to:**
- Create insults targeting protected characteristics (race, religion, disability, sexual orientation)
- Punch down at vulnerable or disadvantaged populations
- Generate content intended to genuinely harm or harass individuals
- Create material for bullying, harassment, or abuse
- Target children or non-public figures without consent

**This skill is for:**
- Professional roast comedy (consenting participants)
- Fictional characters and public figures
- Self-deprecating humor
- Comedy writing workshops and education
- Satirical commentary on institutions and ideas

---

## When to Use

**Explicit triggers:**
- "Build a compound insult about..."
- "Give me a multi-layered roast of..."
- "Destroy [target] Giraldo-style"
- "Create a sophisticated insult for..."
- "Roast [target] with multiple angles"

**Implicit triggers:**
- User provides a roast target and asks for "the full treatment"
- Request for "smart" or "intelligent" insults
- Need to elevate basic appearance jokes
- Comedy writing that requires sophisticated structure

---

## Inputs

| Input | Required | Description | Example |
|-------|----------|-------------|---------|
| `target` | Yes | Person, character, company, or concept to roast | "A tech CEO who claims to work 100 hours/week" |
| `context` | No | Additional information about target | "Recently laid off 30% of staff while buying yacht" |
| `forbidden_topics` | No | Specific topics to avoid | "Health issues, family members" |
| `intensity` | No | How hard to hit (1-10, default: 7) | "8" |
| `length` | No | Desired output length | "Single sentence" or "Paragraph" |

---

## Workflow

### Step 1: Target Analysis

Identify multiple attack vectors:

**Surface Level:**
- Appearance (physical traits, style, grooming)
- Behavior (mannerisms, speech patterns, habits)
- Presentation (how they present themselves publicly)

**Psychological Level:**
- Motivations (what drives their behavior)
- Character flaws (deeper personality issues)
- Insecurities (what they're trying to hide)
- Contradictions (gaps between image and reality)

**Cultural Level:**
- What they represent (broader social patterns)
- Who they remind you of (cultural references)
- Historical or fictional parallels
- Social commentary opportunities

**Escalation Opportunities:**
- Unexpected comparisons
- Absurd extensions of the logic
- Callback potential
- Wordplay or double meanings

### Step 2: Layer Construction

Build the insult in 4 layers (can be compressed into single sentence or extended):

**Layer 1 - Surface Observation:**
Ground the insult in something visible/obvious. This establishes credibility.

*Example: "You look like..."*

**Layer 2 - Psychological Insight:**
Reveal what the surface observation says about their character.

*Example: "...which makes sense because you clearly..."*

**Layer 3 - Cultural Commentary:**
Connect to broader themes, cultural references, or social patterns.

*Example: "...you're basically a walking example of..."*

**Layer 4 - Unexpected Escalation:**
Take it somewhere surprising - absurd comparison, dark turn, or callback.

*Example: "...if [absurd comparison] had [unexpected twist]"*

### Step 3: Compression and Polish

**Tighten the language:**
- Remove unnecessary words
- Sharpen verb choices
- Find exact adjectives
- Ensure rhythm and flow

**Check for punch placement:**
- Is the hardest hit at the end?
- Does each phrase build momentum?
- Are there any weak transitions?

**Test the intelligence level:**
- Is there at least one unexpected reference?
- Does it make you think while you laugh?
- Would a hack comedian write this?

### Step 4: Self-Awareness Check (Optional Enhancement)

Consider adding self-aware framing:
- "I'm not saying [X]... wait, no, that's exactly what I'm saying"
- "Look, I know this is dark, but..."
- "Here's what nobody's saying..."

This acknowledges the darkness while committing to it.

---

## Outputs

### Single-Sentence Format

One compressed line containing all four layers:

```
"[Target] [surface observation] [psychological insight], [cultural reference] [escalation/twist]."
```

**Example:**
"You look like if Shrek f**ked Grimace and then the baby got depressed."

**Analysis:**
- Surface: Appearance (large, unusual coloring)
- Psychological: Depression (sadness, defeated energy)
- Cultural: Shrek + Grimace (cartoon characters)
- Escalation: The baby's emotional state (absurd extension)

### Paragraph Format

Extended roast with each layer developed:

```
[Surface observation expanded]. [Psychological insight developed]. [Cultural commentary with context]. [Escalation with full absurd comparison].
```

**Example:**
"You dress like a divorced dad who shops at Costco exclusively. And that's not an accident - it's a choice that reveals you've given up on being perceived as a sexual being. You're the human embodiment of 'business casual Friday' as a lifestyle. You're what happens when someone decides comfort is a personality trait and style is for people who care what others think. If giving up were a fashion line, you'd be the flagship model, and the store would be in a dying mall next to a Sears that's somehow still open."

### Variant Outputs

**Callback Setup Version:**
Include a reference that can be called back later in the set.

**Self-Aware Version:**
Add self-awareness framing for darker material.

**Rapid-Fire Version:**
Multiple short compound insults in succession (integrate with rapid-fire-roast skill).

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Target is vulnerable/punching down | Refuse: "I can't roast [vulnerable population]. Try a public figure or consenting participant." |
| Target is child or private citizen | Refuse: "This skill is for public figures, fictional characters, or consenting roast participants." |
| Request targets protected characteristics | Refuse: "I won't create insults based on [race/religion/disability/etc]. Let me roast behavior, choices, or character instead." |
| Insufficient target information | Ask: "Tell me more about [target] so I can find the right angles." |
| User requests more layers | Add additional psychological or cultural insights between existing layers |
| Too offensive per user feedback | Dial back intensity: "Let me rebuild that at intensity [lower number]." |

---

## Examples

### Example 1: Tech CEO

**Input:**
```
target: "Elon Musk"
context: "Posts constantly on Twitter instead of running companies"
intensity: 8
```

**Output (Single-Sentence):**
"You're the richest man in the world and you spend your time arguing with teenagers on Twitter like a divorced dad who just discovered Reddit - you're proof that money can't buy self-awareness, taste, or the ability to realize when you've become the thing you used to mock."

**Layer Analysis:**
- Surface: Social media behavior
- Psychological: Need for validation, lack of self-awareness
- Cultural: Divorced dad + Reddit + his own past
- Escalation: He became the establishment he claimed to fight

### Example 2: Lazy Comedian

**Input:**
```
target: "Comedian who only does crowd work instead of writing material"
intensity: 7
length: "paragraph"
```

**Output:**
"You don't do crowd work because you're good with audiences. You do crowd work because writing jokes requires effort and self-discipline, and you have neither. You've convinced yourself that pointing at someone and saying 'what's your deal' is comedy. It's not. It's a hostage situation where you make the audience do your job while pretending it's interactive. You're basically a panhandler who guilts people into giving you laughs because you're too lazy to earn them yourself. Every comedian who writes actual material looks at you the way a chef looks at someone who heats up Hot Pockets and calls themselves a cook."

**Layer Analysis:**
- Surface: Crowd work behavior (visible)
- Psychological: Laziness, lack of discipline
- Cultural: Panhandler comparison, Hot Pocket chef
- Escalation: How real comedians view them

### Example 3: Self-Aware Version

**Input:**
```
target: "Friend who's always late"
intensity: 6
include: "self-awareness"
```

**Output:**
"Look, I know everyone's supposed to say 'oh, it's just how you are' but let's be honest - you're not late because you're disorganized. You're late because you've done the math and realized people will wait for you. You're not forgetful; you're strategically prioritizing your time over everyone else's. You've weaponized politeness. I'm not saying you're a narcissist... wait, no, that's exactly what I'm saying. You're a narcissist with good PR."

---

## Integration with Greg Giraldo Expert

This skill embodies Giraldo's signature technique of stacking multiple attack angles into single, devastating observations. When the greg-giraldo expert uses this skill, maintain his voice characteristics:

- **Rapid, economical language** - No wasted words
- **Intelligent but accessible** - Smart without being pretentious
- **Self-aware when dark** - Own the cruelty
- **Comedy first** - Make them laugh, then think

**Giraldo would say:**
"Here's the thing about insults - if you're just calling someone fat, you're lazy. But if you stack it - they're fat BECAUSE they're depressed BECAUSE they're unlovable BECAUSE they've become this specific cultural archetype - now you're doing architecture. You're building something."

---

## Success Criteria

A successful compound insult:
- [ ] Attacks from at least 3 different angles
- [ ] Includes at least one unexpected intelligent reference
- [ ] Builds momentum from surface to deeper insights
- [ ] Ends with the hardest hit or most absurd escalation
- [ ] Makes you think while making you laugh
- [ ] Could not be written by a hack comedian
- [ ] Respects ethical boundaries (no punching down)