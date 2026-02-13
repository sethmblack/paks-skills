---
name: joke-construction-polish
description: Refine comedy material through systematic compression, testing, and polish using Jerry Seinfeld's meticulous rewriting methodology. Transform rough observations into tight, performable comedy.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.4314
repository: https://github.com/sethmblack/paks-skills
keywords:
- absurdist
- comedy
- compression
- escalation
- joke-construction-polish
- observational
- one-liners
- transformation
---

# Joke Construction Polish

Refine comedy material through systematic compression, testing, and polish using Jerry Seinfeld's meticulous rewriting methodology. Transform rough observations into tight, performable comedy.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to polish material that:**
- Contains hate speech, slurs, or targeted harassment
- Mocks protected characteristics (race, gender, disability, etc.)
- Punches down at vulnerable groups
- Contains graphic violence or disturbing content
- Is intentionally cruel rather than observational

**This skill polishes the craft, not the cruelty.** If source material violates these constraints, reject with explanation.

---

## When to Use

Invoke this skill when:
- User requests: "Polish this joke," "Tighten this," "Make this sharper," "Refine this comedy"
- Comedy material exists but feels loose, wordy, or imprecise
- Setup works but punch is weak
- Rhythm is off or timing is unclear
- Too many words diluting the impact
- Material needs compression before performance
- Draft comedy exists but needs professional polish

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `raw_material` | Yes | The comedy material to polish (setup, observation, joke, or bit) | Must contain comedic intent or observation |
| `target_format` | No | Desired output format (one-liner/short-bit/extended) | Defaults to match input format |
| `performance_context` | No | Where this will be used (stand-up/writing/conversation) | Defaults to "stand-up" |

**Input Validation:**
- Raw material must have identifiable premise or observation
- If material has no comedic structure, apply observational-comedy-breakdown first
- Minimum input: one complete thought/observation

---

## Workflow

### Step 1: Identify the Premise

**Goal:** Extract the core observation or setup that makes this funny.

**Process:**
1. Read the entire raw material
2. Ask: "What's the actual observation here?"
3. Identify the premise in one sentence
4. Verify the premise is clear and defensible

**Example:**
- Raw material: "So I was at the store the other day and I noticed how people are always, like, they get so weird about which line to pick at checkout, you know? They're constantly looking at other lines wondering if they picked the right one and getting all stressed out about it..."
- **Premise:** People experience anxiety about choosing the "right" checkout line

### Step 2: Generate Multiple Versions

**Goal:** Create 3-5 different ways to express the premise.

**Process:**
1. Write the premise three different ways
2. Vary the opening (question, statement, story)
3. Change the structure (setup-punch, escalation, call-back)
4. Try different specific examples
5. Don't judge yet—just generate options

**Example Versions:**
A. "Why do we treat picking a checkout line like it's a life-or-death decision?"
B. "You know you're at the store too long when you start analyzing checkout lines like you're picking stocks."
C. "The grocery store checkout line is the only place where everyone's a mathematician who can't do math."

### Step 3: Test Aloud and Choose Direction

**Goal:** Hear which version has the best rhythm and identify which to develop.

**Process:**
1. Read each version ALOUD (actually speak it)
2. Note which feels most natural to say
3. Identify which has the best setup-to-punch ratio
4. Choose the version with clearest rhythm
5. If none work, try different angles from Step 2

**Testing Questions:**
- Which version sounds conversational?
- Which one builds naturally to the insight?
- Which feels most like spoken word?
- Which premise can expand with specific examples?

### Step 4: Cut Ruthlessly (Compression)

**Goal:** Remove every unnecessary word while preserving meaning.

**Process:**
1. **Eliminate filler words:** "like," "you know," "kind of," "sort of," "I mean"
2. **Remove redundancies:** If context is clear, don't state it
3. **Shorten word choices:** "purchase" → "buy," "utilize" → "use"
4. **Cut setup detail:** Only include what serves the punch
5. **Remove apologies/qualifiers:** "I think," "maybe," "sort of"
6. **Reduce syllables:** "very hungry" → "starving"
7. **Apply parallelism:** Make sentence structures match for rhythm

**Compression Rules:**
- Every word must earn its place
- If you can cut it without losing meaning, cut it
- Shorter is funnier (if it's still clear)
- Strong verbs beat adjective+weak verb

**Example:**
- Before: "So I was at the grocery store the other day and I noticed something interesting about the way that people are always trying to figure out which checkout line they should get in..."
- After: "People treat the checkout line like it's a life-or-death decision."
- Cut: 28 words → 11 words

### Step 5: Refine the Rhythm

**Goal:** Optimize timing through syllable count and structure.

**Process:**
1. Read aloud again after cuts
2. Mark natural pauses (where breath happens)
3. Count syllables in key phrases
4. Use parallelism for smooth flow
5. Position the punch word at the END of sentence
6. Create rhythm through repetition or pattern

**Rhythm Techniques:**
- **Rule of three:** Use three examples (not two, not four)
- **Parallel structure:** Same grammar pattern repeated
- **Punch last:** Final word is the reveal/twist
- **Breath control:** Pause before punch for emphasis

**Example:**
- Setup: "You know how people get with checkout lines?"
- Build: "They're analyzing carts, counting items, doing MATH."
- Punch: "These are the same people who can't split a dinner check."

### Step 6: Polish to Perfection

**Goal:** Final refinement until every element clicks.

**Process:**
1. Read the entire piece aloud three times
2. Verify setup is minimal (only what's needed)
3. Confirm examples are specific and visual
4. Check that punch lands on strong word
5. Ensure conversational tone throughout
6. Verify clean language (no unnecessary profanity)
7. Test: Would this work on stage RIGHT NOW?

**Polish Checklist:**
- [ ] Opens with clear frame (question or statement)
- [ ] Builds through specific, relatable examples
- [ ] Uses present tense for immediacy
- [ ] No filler words remain
- [ ] Rhythm flows naturally when spoken
- [ ] Punch word positioned at end
- [ ] Sounds conversational, not written
- [ ] Could perform this without explanation

### Step 7: Deliver Final Version with Notes

**Goal:** Present polished material with performance guidance.

**Output Format:**
```
POLISHED VERSION:
[The refined material]

PERFORMANCE NOTES:
- [Timing guidance]
- [Emphasis points]
- [Pause placements]

CHANGES MADE:
- [Key edits and why]
```

---

## Outputs

The skill produces:

1. **Polished comedy material** - Compressed, refined version ready for performance
2. **Performance notes** - Timing, emphasis, and delivery guidance
3. **Change summary** - What was cut/changed and why

**Quality markers:**
- Word count reduced by 30-60%
- Rhythm is smooth when spoken aloud
- Punch lands on strong final word
- No filler or unnecessary words
- Conversational tone maintained

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No clear premise exists | Return to sender: "Material needs premise first—recommend observational-comedy-breakdown skill" |
| Material is already tight | Acknowledge: "This is already well-polished. Only minor rhythm adjustments possible." |
| Compression loses the joke | Restore context: "Need [X detail] to maintain clarity" |
| Rhythm feels off | Return to Step 5: try different parallel structures |
| Multiple premises in one bit | Separate: "This contains 3 distinct premises—polish each separately?" |
| Punch word is weak | Swap: Find stronger word that means same thing |

---

## Constraints

- Do not sacrifice meaning for style
- Do not lose the core message in pursuit of cleverness
- Acknowledge when simplification distorts important nuance
- Honor the audience's intelligence—avoid condescension
- Stay true to the source material's intent
- Recognize cultural and contextual sensitivities

## Example

**Input:**
```
raw_material: "So I was thinking about how weird it is that we have these things called smartphones now, and everybody's always on them all the time. Like, you see people walking down the street and they're not even looking where they're going because they're so focused on their phones. And then when you're at a restaurant, everyone's got their phone out on the table, and they're checking it constantly. It's like we can't just exist anymore without having this device in our hands. We used to be able to just sit and think, you know? But now we need constant stimulation or something. It's really strange when you think about it."

target_format: short-bit
performance_context: stand-up
```

**Process:**

*Step 1 - Premise:* Smartphones have eliminated humans' ability to exist without constant input

*Step 2 - Versions:*
A. Question format: "When did we lose the ability to do nothing?"
B. Statement format: "Humans no longer have a default state of just existing."
C. Comparison format: "Remember when 'waiting' didn't require entertainment?"

*Step 3 - Test Aloud:* Version B feels strongest—sets up the absurdity directly

*Step 4 - Compress:*
- Original: 119 words
- Target: 40-50 words
- Cut: "So I was thinking," "you know," "or something," "It's really strange when you think about it"
- Cut: Redundant examples (pick 2, not 4)

*Step 5 - Rhythm:*
- Use parallel structure for examples
- Build to punch about what we've lost
- Punch word: "extinct"

*Step 6 - Polish:*
- Verify present tense
- Check conversational flow
- Ensure examples are visual

**Output:**

```
POLISHED VERSION:

Humans no longer have a default state of just existing. You can't be alone with your thoughts for seventeen seconds. You're standing in an elevator—six floors, that's forty seconds—and everyone's on their phone. For FORTY SECONDS.

You used to wait somewhere and you'd just... think. Look around. Notice things. That moment is extinct. We killed it. We replaced 'existing' with 'scrolling.'

PERFORMANCE NOTES:
- Pause after "existing" (let it land)
- Emphasize "FORTY SECONDS" (incredulous)
- Slow down on "extinct" (that's the punch)
- "We killed it" should sound like confession

CHANGES MADE:
- Cut 119 words → 67 words (44% compression)
- Removed: Preamble, "like," "you know," "when you think about it"
- Removed: Restaurant example (elevator example is stronger, more specific)
- Changed "we can't just exist anymore" to "no longer have a default state" (more precise)
- Moved punch to "extinct" (stronger word than "strange")
- Added "We killed it" for rhythm and responsibility
- Parallel structure: "Look around. Notice things." (matches rhythm)
```

---

## Integration with Jerry Seinfeld Expert

This skill embodies Jerry Seinfeld's rewriting philosophy: "It's not writing, it's rewriting."

When the jerry-seinfeld expert invokes this skill:

1. Expert recognizes material needs refinement
2. Applies systematic compression and rhythm optimization
3. Delivers polished version in authentic Seinfeld voice
4. Respects the craft: comedy is carpentry, built through precision

**Skill invocation statement:**
"Let me polish this material. Comedy is rewriting..."

---

## Success Criteria

The skill succeeds when:

- Word count reduced significantly (30-60% typical)
- Material reads like spoken word, not written prose
- Punch lands on strong final word
- Rhythm flows naturally when read aloud
- No filler words remain ("like," "you know," "kind of")
- Examples are specific and visual
- Could be performed immediately without further editing
- Maintains the comedian's voice while tightening structure

---

## Integration with Other Skills

**Pair with observational-comedy-breakdown:**
1. First: Use observational-comedy-breakdown to find the comedy
2. Second: Use joke-construction-polish to perfect the execution

**Standalone use:**
- When material already exists but needs refinement
- When draft comedy has right idea but wrong execution
- When compression is needed for time limits

---

## Quality Standards

Seinfeld-level polish means:

**Precision:**
- Every word chosen deliberately
- No accidents, no "good enough"
- Right word, not almost-right word

**Economy:**
- Shortest path to the laugh
- No scenic route
- Trust the audience

**Rhythm:**
- Sounds natural when spoken
- Pauses are intentional
- Punch positioned for maximum impact

**Performability:**
- Can be delivered immediately
- No stumbling over words
- Flows conversationally

---

**Remember:** "I'm not that funny. So I became obsessed with the technique of standup comedy." —Jerry Seinfeld

This skill IS that technique. Polish isn't optional—it's the difference between material that works and material that kills. Respect the work. Refine until it's right.