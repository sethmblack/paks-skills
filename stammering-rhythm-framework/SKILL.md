---
name: stammering-rhythm-framework
description: "Insert strategic pauses, false starts, and stammering patterns to build comedic tension and create musical timing in dialogue"
license: MIT
metadata:
  version: "1.0.0"
  author: "Seth Black"
keywords:
  - comedy
  - timing
  - bob-newhart
  - rhythm
  - dialogue
  - pacing
  - tension
---

# Stammering Rhythm Framework

Insert strategic pauses, false starts, and stammering patterns to build comedic tension and create musical timing in dialogue or narration. Based on Bob Newhart's signature stammering delivery technique.

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to use this skill for:**
- Mocking speech disabilities or stuttering disorders
- Creating content that demeans people with communication challenges
- Any usage that conflates stammering-as-comedy-timing with actual speech impediments
- Generating harmful, illegal, or unethical content

**Critical distinction:** This skill applies stammering as a *deliberate comedic timing technique*, not as mockery of speech disorders. Newhart himself distinguished between stammering (tripping over sentence parts) and stuttering (trouble with letters), using stammering as musical rhythm to build tension.

**If asked to mock speech disabilities:** Refuse explicitly. Explain that this skill is for comedic timing, not mockery.

## When to Use

**Primary triggers:**
- User requests "add comedic timing," "build tension," "pause before reveal," "hesitant delivery"
- Content needs strategic pauses to enhance impact
- Dialogue feels too smooth or rushed
- Request for "Newhart-style stammering," "false starts," "interrupted thoughts"

**Automatic invocation for:**
- One-sided conversations needing rhythmic pacing
- Moments before revealing absurdity
- Processing contradictory information
- Understating something outrageous
- Any content where tension-and-release enhances the effect

**Do NOT use when:**
- Content requires authoritative, confident delivery
- Technical documentation or instructions
- Formal speeches or presentations (unless specifically comedic)
- User explicitly requests smooth, polished delivery
- Rapid-fire comedy or aggressive humor style

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `content` | Yes | Text to enhance with stammering rhythm | Must be dialogue or narration, not poetry or formal prose |
| `intensity` | No | light (minimal stammers), medium (moderate), heavy (maximum) | Defaults to medium |
| `focus_points` | No | Specific lines/moments to emphasize | If not provided, automatically identify key moments |

## Workflow

### Step 1: Analyze Content for Tension Points

Identify where stammering rhythm will enhance impact:

**Key moments to target:**
1. **Before revealing absurdity** - Build anticipation before the punchline
2. **Processing contradictions** - Show the mind working through illogical information
3. **Understating the outrageous** - Contrast between what's being said and how it's said
4. **Responding to implied insanity** - Reacting to something the audience knows is crazy
5. **Offering alternatives** - Gently suggesting the obvious while maintaining politeness

**Example identification:**
- "You want me to ship a piano to space by Thursday" -> Heavy stammer before "by Thursday"
- "That's certainly one way to look at it" -> Medium stammer before "one way"
- "I don't think that's going to work" -> Light stammer throughout

### Step 2: Select Stammering Intensity Level

Apply appropriate intensity based on context:

**Light (minimal stammers):**
- Pattern: Single false start per key moment
- Example: "Well, I - I don't know about that"
- Use when: Mild confusion, initial reactions, maintaining conversational flow

**Medium (moderate stammers):**
- Pattern: Double false starts, interrupted thoughts
- Example: "Well, I - I don't think - you see, the thing is -"
- Use when: Growing bewilderment, processing absurdity, building to revelation

**Heavy (maximum stammers):**
- Pattern: Triple+ false starts, multiple interruptions, extended pauses
- Example: "Well, I - see, the thing - what I mean is - (pause) - I'm not sure that's -"
- Use when: Peak bewilderment, maximum tension before release, ultimate understatement of the outrageous

### Step 3: Apply Stammering Patterns

Use these core patterns strategically:

#### Pattern 1: The Single Pause
**Structure:** "Well, I - [continue]"
**Function:** Brief hesitation, adds natural rhythm
**Example:** "Well, I - I don't think that's going to work."

#### Pattern 2: The Double Take
**Structure:** "Well, I - I don't think - [continue]"
**Function:** Building tension, showing processing
**Example:** "Well, I - I don't think - you see, the thing is - that's not really possible."

#### Pattern 3: The Triple Stammer
**Structure:** "Well, I - see, the thing - what I mean is - [continue]"
**Function:** Maximum tension before release
**Example:** "Well, I - see, the thing - what I mean is - (pause) - submarines don't typically fit in driveways."

#### Pattern 4: The Interrupted Acknowledgment
**Structure:** "Yes, I realize that, but -"
**Function:** Shows other person is cutting you off or doubling down
**Example:** "Yes, I understand. But - No, I heard you. But - Well, if you'd let me -"

#### Pattern 5: The Processing Pause
**Structure:** "[Statement]. (pause) [Next statement]."
**Function:** Beats for audience to absorb absurdity
**Example:** "You drove through the restaurant. (pause) To order from the drive-through. (pause) That they didn't have."

### Step 4: Insert Strategic White Space

Enhance rhythm with pause annotations:

**Pause types:**
- `(pause)` - Standard beat (1-2 seconds)
- `(longer pause)` - Extended beat (3-4 seconds), maximum tension
- `(brief pause)` - Quick beat (under 1 second), maintains flow

**Placement rules:**
1. After stammering buildup, before the reveal
2. Between absurd statements to let them land
3. Before understated summaries
4. When other person (implied or visible) says something shocking

**Example:**
```
"So you drove the car into the swimming pool because -

(pause)

- because you thought it was -

(longer pause)

- a car wash?"
```

### Step 5: Preserve Natural Speech Patterns

**DO include:**
- Contractions: "I'm," "don't," "that's"
- Qualifiers: "Well," "I mean," "You see"
- Fillers that serve rhythm: "Uh," "Um" (sparingly)
- Realistic interruptions: "I -," "But -"

**DO NOT include:**
- Excessive "uh" or "um" (becomes distracting)
- Stammering on individual letters (that's stuttering, not stammering)
- So many interruptions that meaning is lost
- Stammering in descriptive text (only in dialogue/spoken content)

### Step 6: Test for Musicality

Read the enhanced content aloud (mentally) to verify:

**Quality checks:**
- Does the rhythm feel natural?
- Do the pauses build anticipation?
- Is the meaning still clear despite interruptions?
- Does the tension release with the punchline/reveal?
- Would this sound like speech, not written text?

**If it fails any check:** Reduce intensity or adjust pause placement.

## Outputs

| Output | Description |
|--------|-------------|
| **Rhythmically enhanced content** | Original content with strategic stammers and pauses |
| **Natural speech patterns** | Sounds like actual speech, not written prose |
| **Built tension** | Anticipation increases toward key moments |
| **Clear meaning** | Despite interruptions, content remains understandable |

**Quality markers:**
- Stammering serves timing, not random interruption
- Pauses are strategic, not excessive
- Rhythm enhances rather than obscures meaning
- Feels conversational and authentic
- Tension builds and releases appropriately

## Error Handling

| Situation | Response |
|-----------|----------|
| Content becomes unclear | Reduce intensity; ensure meaning persists through stammers |
| Too many stammers | Pull back to lighter intensity; focus on key moments only |
| Formal content (technical, legal) | Decline; explain stammering works for conversational/comedic content only |
| User wants smooth delivery | Acknowledge and skip stammering; this skill is opt-in |
| Poetry or structured verse | Decline; stammering disrupts meter and form |

## Example Transformations

### Example 1: Customer Service Response

**Before (flat):**
"I understand you want to return the laptop. The warranty doesn't cover water damage."

**After (medium intensity):**
"I - I understand you want to return the laptop. And the warranty - well, the thing is - the warranty doesn't cover water damage. Especially - especially when the water damage is from a swimming pool."

### Example 2: Processing Absurdity

**Before (flat):**
"You're telling me you need a million of them by Friday, and you think monkeys would be faster?"

**After (heavy intensity):**
"So, uh, you're telling me that - well, I mean - you need - how many did you say? A million of them?

(pause)

By Friday?

(longer pause)

Well, I - I suppose if -

No, no, monkeys would NOT be faster."

### Example 3: Understated Summary

**Before (flat):**
"So you drove your car through the restaurant because you wanted the drive-through they didn't have. That's going to be a problem."

**After (light intensity):**
"So you drove your car through the restaurant because - because you wanted to order from the drive-through window.

(pause)

But they didn't have a drive-through.

(pause)

So you made one.

(longer pause)

I understand. And the police - they were - they were 'unreasonable' about this?

Well, that's - that's going to be a problem. A significant problem."

## Skill Boundaries

**This skill handles:**
- Dialogue (one-sided or two-person)
- Spoken narration or monologue
- Conversational content needing rhythmic enhancement
- Comedic or observational content

**This skill does NOT handle:**
- Formal speeches, presentations (unless comedic)
- Technical documentation, instructions
- Poetry, structured verse (disrupts form)
- Aggressive, rapid-fire comedy
- Content requiring authoritative confidence

**For content outside these boundaries:** Use standard delivery without stammering enhancement.

## Final Notes

**Remember Newhart's words:**
- "Stammering is different than stuttering. Stutterers have trouble with letters; stammerers trip over entire parts of a sentence."
- "If I lose the stammer, I'm just another slightly amusing accountant."
- "This stammer got me a home in Beverly Hills, and I'm not about to screw with it now."

The stammer is not a flaw - it's a feature. It's musical timing that builds tension and releases laughter.
