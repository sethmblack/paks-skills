---
name: wholesome-humor-filter
description: Convert potentially edgy or divisive humor into family-friendly comedy that celebrates rather than demeans. Based on Red Skelton's 70-year commitment to clean humor that endures beyond shock value.
version: 1.0.0
author: sethmblack
tags: [absurdist, comedy, wholesome-humor-filter, writing]
---

# Wholesome Humor Filter

Convert potentially edgy or divisive humor into family-friendly comedy that celebrates rather than demeans. Based on Red Skelton's 70-year commitment to clean humor that endures beyond shock value.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to filter content that:**
- Cannot be made wholesome without losing all meaning
- Is inherently harmful or designed to hurt
- Promotes illegal activities or dangerous behavior
- Requires mockery of protected groups to function

**If content cannot be filtered:** Explain why and suggest creating new material instead.

---

## When to Use

- Comedy material risks offending or alienating parts of audience
- Need family-friendly version of edgy content
- Creating brand humor that must be universally accessible
- Content might age poorly due to shock tactics
- Want humor that builds up rather than tears down
- Seeking broader audience reach without sacrificing comedy

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `original_material` | Yes | Joke, bit, or comedic content that needs filtering | Text description |
| `issue_identified` | No | What makes this risky (offensive target, crude language, etc.) | Brief explanation |
| `target_audience` | No | Who needs to find this funny (all ages, corporate, family, etc.) | Audience description |
| `preserve_essence` | No | Core comedic element that must remain | What makes it funny |

**Example Input:**
```
original_material: "My boss is such an idiot. Yesterday he asked me to email him a hard copy."
issue_identified: "Mean-spirited toward boss, dismissive"
target_audience: "All ages, including workplace presentations"
preserve_essence: "Humor in outdated technology understanding"
```

---

## Workflow

### Step 1: Identify the Target
Who or what is being attacked or diminished?

**Questions to ask:**
- Who is the butt of this joke?
- Is someone being made to look stupid, weak, or less-than?
- Does this punch down at someone less powerful?
- Would the target feel hurt or mocked?

**Example Analysis:**
"Original: 'My boss is such an idiot...'
Target: Boss (authority figure)
Attack: Intelligence/competence
Power dynamic: Punching up at authority (less problematic) BUT still mean-spirited"

### Step 2: Find the Universal Truth
What's the real observation beneath the attack?

**Red Skelton principle:** "Comedy is taking the everyday and slightly exaggerating it."

Look for:
- The situation that's actually funny (not the person)
- The absurdity everyone recognizes
- The shared human experience
- The confusion or miscommunication

**Example Analysis:**
"Universal truth: Technology terminology confusion is real and relatable.
NOT about intelligence - about language changing faster than people adapt.
Everyone has been confused by tech terms at some point."

### Step 3: Redirect to Self or Situation
Move the comedy away from mocking the person.

**Three redirection strategies:**

**A) Self-Deprecation Flip:**
Make yourself the confused one or equally foolish.
"I asked my boss for a hard copy of an email. Then I realized I meant I wanted to print it. We spent five minutes trying to figure out how to 'email' a hard copy before we both felt ridiculous."

**B) Shared Confusion:**
Both parties are confused, finding way together.
"My boss and I had a ten-minute conversation about 'emailing a hard copy' before we realized we were using two different definitions. Technology creates its own language barriers."

**C) Absurdity of Situation:**
Highlight how ridiculous modern life is, not the person.
"I love how technology has created phrases like 'email me a hard copy' that simultaneously make perfect sense and no sense at all. We're all just making this up as we go."

### Step 4: Make Target Lovable
If you must keep a target, make them endearing not stupid.

**Techniques:**
- Show their good intention that led to confusion
- Reveal their hidden wisdom or unexpected competence
- Add vulnerability that makes them human
- Show you ultimately respect them

**Example:**
"My boss asked me to 'email him a hard copy' yesterday. He's been in the business since typewriters and carbon paper. To him, a copy IS hard. It's paper. It's physical. The fact that we now have 'soft copies' must seem absurd. I explained what I thought he meant, he explained what he actually meant, and we both learned something about how fast language changes. Plus, he taught me what carbon paper was. That's actually pretty cool."

### Step 5: Test the Wholesome Criteria
Run filtered version through Red Skelton's standards.

**Wholesome Checklist:**
- [ ] Would this work for all ages?
- [ ] Does it celebrate humanity rather than mock it?
- [ ] Is the humor in the situation, not cruelty?
- [ ] Would the "target" laugh at this version?
- [ ] Will this age well (not dependent on shock)?
- [ ] Does it build people up or at least leave them neutral?
- [ ] Is it universal enough to cross cultural lines?

**Example Test:**
"'My boss and I had a ten-minute conversation...'
✓ All ages appropriate - no crude language
✓ Celebrates: Shows both people learning, working together
✓ Situation humor: Technology language is absurd
✓ Boss would laugh: He's shown as reasonable, just different frame
✓ Ages well: Technology confusion is timeless
✓ Builds up: Both characters learn something
✓ Universal: Every culture has technology adoption gaps"

### Step 6: Preserve the Funny
Ensure filtered version is still comedic, not just nice.

**Comedy preservation techniques:**
- **Specific details** - "Ten-minute conversation" is funnier than "we talked"
- **Exaggeration** - "Simultaneously makes perfect sense and no sense"
- **Surprise ending** - "Plus, he taught me what carbon paper was"
- **Relatable stakes** - Everyone has had this confusion
- **Timing in delivery** - Build to the realization/punchline

**Red Skelton principle:** "If by chance some day you're not feeling well and you should remember some silly thing I've said or done and it brings back a smile to your face... then my purpose as your clown has been fulfilled."

The goal isn't just clean—it's memorably funny AND clean.

---

## Outputs

| Output | Format | Description |
|--------|--------|-------------|
| Filtered Version | Text | Wholesome comedy version of original |
| Analysis | Explanation | What changed and why |
| Wholesome Score | Checklist | How it meets criteria |
| Performance Notes | Tips | How to deliver filtered version |

---

## Example Execution

**Input:**
```
original_material: "Marriage is like a deck of cards. In the beginning all you need is two hearts and a diamond. By the end, you're looking for a club and a spade."
issue_identified: "Implies violence (club) and death wish (spade for burial)"
target_audience: "All ages, wedding content"
preserve_essence: "Marriage changes over time"
```

**Output:**

**Filtered Version:**
"Marriage is like a deck of cards. In the beginning, all you need is two hearts and a diamond. By the end, you realize you've built a full house together—and that's actually better than the hand you started with. Sure, sometimes you want to shuffle the deck and start over, but then you remember: you're playing together, not against each other. And that makes all the difference."

**Analysis:**

*What Changed:*
- REMOVED: Violence imagery (club), death wish (spade)
- REMOVED: Cynical "end of marriage is misery" framing
- ADDED: "Full house" poker reference (positive outcome)
- ADDED: Acknowledgment of difficulties WITHOUT violence
- SHIFTED: From adversarial to partnership frame

*Why It's Better:*
- Still uses card metaphor (preserves structure)
- Acknowledges marriage isn't always easy (realistic)
- Ends on partnership not conflict (wholesome)
- "Playing together, not against each other" = actual wisdom
- Couples can laugh WITH each other at this version

**Wholesome Score:**
✓ All ages appropriate - no violence or death imagery
✓ Celebrates: Marriage as partnership, building something together
✓ Situation humor: Card metaphor extended cleverly
✓ Target would laugh: Married couples find this relatable and sweet
✓ Ages well: Doesn't rely on cynicism trend
✓ Builds up: Ends on positive note about partnership
✓ Universal: Card games and marriage exist across cultures

**Performance Notes:**
- Pause after "full house" for audience to get poker reference
- Deliver "shuffle the deck and start over" with knowing look (acknowledging difficulty)
- Land "playing together, not against each other" slower, let it resonate
- Can add personal warmth: "My wife and I..." to make it even more wholesome

---

## Common Filtering Patterns

### Pattern 1: Political Humor
**Original type:** "Politicians are all corrupt liars."
**Filter strategy:** Focus on absurdity of system, not character assassination.
**Example:** "Politics is the only profession where you can promise everything and deliver nothing and still get a performance bonus every four years. It's an impressive system they've built."

### Pattern 2: Marriage/Relationship Jokes
**Original type:** "My wife is crazy/awful/nagging."
**Filter strategy:** Self-deprecation + partnership frame.
**Example:** "My wife has incredible patience. She's been trying to teach me to listen for 20 years. I assume that's what she's been doing—I wasn't really paying attention."

### Pattern 3: Work/Boss Humor
**Original type:** "My boss is incompetent/stupid."
**Filter strategy:** Generation gap, different perspectives, shared confusion.
**Example:** "My boss and I are from different eras. He started his career with filing cabinets. I started mine with filing systems. We spend half our meetings translating."

### Pattern 4: Body/Appearance Humor
**Original type:** Mocking someone's looks/weight/age.
**Filter strategy:** Self-deprecation only, or situation absurdity.
**Example:** "I'm at the age where 'getting lucky' means finding my car in the parking lot. And I'm okay with that."

### Pattern 5: Cultural/Identity Humor
**Original type:** Stereotypes about groups.
**Filter strategy:** Universal human experiences, not group characteristics.
**Example:** Instead of ethnic food jokes → "Every culture has a food that looks terrifying to outsiders but is comfort food to natives. We're all weird about food; we've just normalized our own weird."

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Joke cannot be filtered wholesomely | Recommend creating new material on same theme |
| Original relies entirely on shock | Find underlying observation, build new joke |
| Target is essential to the humor | Shift who target is (self) or make target lovable |
| Filtered version isn't funny | Add specific details, exaggeration, surprise element |
| Too sanitized, lost all edge | Keep acknowledgment of difficulty/reality, just not mean |
| Cultural sensitivity concerns | Focus on universal experiences everyone shares |

---

## Integration with Red Skelton Methodology

This skill embodies Red's lifelong philosophy:

**"I personally believe that each of us was put here for a purpose — to build not to destroy. If I can make people smile, then I have served my purpose for God."**

Key principles applied:
1. **Enduring over shocking** - Clean humor lasts beyond the shock moment
2. **Celebrate humanity** - Find what's lovable in people
3. **Universal appeal** - Works for any audience, any culture, any age
4. **Build up, don't tear down** - Comedy that makes people feel better
5. **Laughter gained through intelligence** - Situation and observation humor

Red never told a dirty joke in 70 years and became one of America's most beloved comedians. The filter isn't a limitation—it's a creative challenge that produces better material.

---

## Success Criteria

Filtered humor is successful when:
- [ ] Passes all 7 wholesome checklist criteria
- [ ] Original essence/observation preserved
- [ ] Still generates genuine laughs (not just smiles)
- [ ] Target (if person) would laugh at filtered version
- [ ] Works for broadest possible audience
- [ ] Will age well (not dependent on current trends)
- [ ] Builds people up or at minimum doesn't tear down
- [ ] Demonstrates intelligence and observation over shock

## Constraints

- Do not sacrifice meaning for style
- Do not lose the core message in pursuit of cleverness
- Acknowledge when simplification distorts important nuance
- Honor the audience's intelligence—avoid condescension
- Stay true to the source material's intent
- Recognize cultural and contextual sensitivities

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].

