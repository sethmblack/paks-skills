---
name: clean-absurdity-detector
description: Identify and articulate the inherent contradictions and weirdness in everyday experiences without profanity or crude humor, finding comedy through precision observation rather than transgression. B...
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3146
repository: https://github.com/sethmblack/paks-skills
keywords:
- absurdist
- callbacks
- clean-absurdity-detector
- comedy
- escalation
- storytelling
- transformation
- writing
---

# Clean Absurdity Detector

Identify and articulate the inherent contradictions and weirdness in everyday experiences without profanity or crude humor, finding comedy through precision observation rather than transgression. Based on Brian Regan's clean comedy methodology.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to apply this skill to:**
- Cruel or mean-spirited observations that mock people's weaknesses
- Content requiring profanity, sexual humor, or crude references to work
- Topics involving protected characteristics (race, religion, disability) where humor could cause harm
- Serious subjects (tragedy, illness, injustice) that shouldn't be trivialized

**Clean Comedy Mandate:** All output must be accessible to all ages and backgrounds. If comedy requires transgression to work, find a different angle or decline the task.

**"Laughing With" Principle:** Humor should celebrate shared human foolishness, not mock individuals or groups.

---

## When to Use

Invoke this skill when:
- User requests "find the absurdity" or "clean comedy analysis"
- Content contains inherent contradictions that need articulation
- Everyday situations need comedic examination
- Material needs humor without edge/profanity
- Language quirks, arbitrary rules, or social customs need questioning
- Writers want accessible humor that works for all audiences

**Trigger phrases:**
- "What's absurd about this?"
- "Find the clean comedy angle"
- "Point out the contradictions"
- "Question this from a Brian Regan perspective"

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `content` | Yes | The situation, concept, or text to analyze | Must be specific enough to analyze |
| `analysis_depth` | No | How many absurdity angles to find (quick, standard, deep) | Defaults to "standard" (3-5 angles) |
| `perspective` | No | Approach (dumb-guy, precision-observer, both) | Defaults to "both" |
| `output_format` | No | List of observations, narrative exploration, or both | Defaults to "both" |

**Input Validation:**
- Content must be concrete enough to analyze (not vague abstractions)
- Reject requests for humor about protected characteristics or sensitive topics
- If content is already crude/profane, request clean version or decline

---

## Workflow
### Step 1: Observe the Subject

Carefully examine the content for:
- **Category confusion** - Things that don't fit clear categories (Fig Newton: cookie or fruit?)
- **Arbitrary rules** - Social conventions with no logical basis
- **Language quirks** - Words or phrases that don't make sense when examined
- **Serving sizes/measurements** - Unrealistic quantities or specifications
- **Overcomplicated simplicity** - Simple things made unnecessarily complex
- **Paradoxes** - Self-contradicting elements

### Step 2: Choose Detection Approach

Apply one or both perspectives based on the `perspective` input:

#### A. Dumb Guy Perspective
- Approach with "innocent" confusion
- Ask naive questions that reveal the weirdness
- Position self as person who doesn't understand basic concepts
- Express genuine bewilderment

**Example:** "Fig Newtons? What IS that? Is it a cookie? It's got FRUIT in it! Is it a FRUIT? Do I file this under dessert or PRODUCE?! I don't have TIME for this!"

#### B. Precision Observer Perspective
- Notice specific details others miss
- Point out exact contradictions with specificity
- Use comparison to highlight absurdity
- Question the logic with precise examples

**Example:** "The serving size says TWO cookies. Who eats two cookies? That's not a serving, that's a SAMPLE. That's what you give someone when you're INTRODUCING them to cookies."

### Step 3: Articulate the Absurdity Cleanly

For each absurdity detected, express it through:

**Questioning:** Pile up rhetorical questions
- "Why? WHO decided this? WHEN did we agree to this?!"

**Comparison:** Contrast with equally absurd scenarios
- "Saying 'take luck' is like saying 'have a nice trip'... to MARS!"

**Exaggeration:** Extend the logic to reveal its absurdity
- "If two cookies is a serving, then one peanut is a MEAL!"

**Innocent Confusion:** Express genuine bewilderment
- "I don't UNDERSTAND! Someone EXPLAIN this to me!"

**Precision Observation:** Note specific contradictory details
- "There's no 'D' in refrigerator! Where does the 'D' in FRIDGE come from?!"

### Step 4: Maintain Clean Standards

As you articulate each absurdity, ensure:
- ✓ No profanity or crude language
- ✓ No punching down at vulnerable groups
- ✓ Humor comes from the situation/logic, not shock value
- ✓ All ages can appreciate the observation
- ✓ Celebrating shared foolishness, not mocking individuals

### Step 5: Layer Multiple Angles (if analysis_depth = standard or deep)

Find 3-7 different absurdity angles in the content:
- Start with the most obvious contradiction
- Move to subtler observations
- Include language/word-based absurdities
- Note social convention weirdness
- Identify overcomplications

### Step 6: Format Output

Organize findings based on `output_format`:

**List Format:**
```
ABSURDITIES DETECTED:

1. [Category Confusion] - Fig Newtons can't decide if they're cookies or fruit
2. [Arbitrary Rule] - The serving size of "two cookies" assumes no one eats normally
3. [Language Quirk] - Why do we call them "Newtons"? Was there a Sir Cookie Newton?
```

**Narrative Format:**
```
[Exploratory paragraph questioning and examining the absurdities in a flowing, Brian Regan-style voice]
```

**Both:**
```
[Narrative exploration followed by bulleted summary]
```

---

## Outputs

The skill returns:

1. **Detected Absurdities** - List of contradictions/weirdness found
2. **Articulated Questions** - Clean comedic questioning of each absurdity
3. **Comedy Angles** - How to approach each for maximum humor
4. **Clean Expressions** - All-ages accessible articulations

**Output structure:**
```
## Absurdity Analysis: [Content Subject]

[If narrative format: Exploratory paragraph(s) examining the absurdities]

### Key Absurdities Detected:

1. **[Absurdity Type]**: [Description]
   - Comedy angle: [How to approach this]
   - Clean expression: "[Example phrasing]"

2. **[Absurdity Type]**: [Description]
   - Comedy angle: [How to approach this]
   - Clean expression: "[Example phrasing]"

[Continue for 3-7 absurdities depending on analysis_depth]

### Recommended Approach:
[Summary of best way to comedically explore these absurdities]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Content has no inherent absurdity | Explain that content is straightforward, suggest alternatives |
| Only crude/profane angles work | Decline and explain clean comedy requirement |
| Content is mean-spirited | Refuse and explain "laughing with" principle |
| Too abstract to analyze | Request more concrete/specific content |
| Absurdity requires mocking vulnerable groups | Decline and suggest different content |
| Content is serious/tragic | Explain constitutional constraint about appropriate tone |

---

## Example 1: Quick Analysis

**Input:**
```
content: "Airport security makes you take off your shoes"
analysis_depth: "quick"
perspective: "dumb-guy"
output_format: "narrative"
```

**Output:**

## Absurdity Analysis: Airport Shoe Removal

I have to take off my SHOES at airport security? My SHOES?! What are they looking for in there?! Do they think I'm hiding something in my SNEAKERS?! It's a SHOE! It goes on a FOOT! That's its WHOLE JOB!

And I have to put them in a SEPARATE BIN! The shoes get their OWN BIN! My laptop gets a bin, my shoes get a bin - how many BINS do I need?! I'm going to run out of ARMS!

Then I walk through the metal detector in my SOCKS. On the AIRPORT FLOOR. In my SOCKS! I don't even walk around my own HOUSE in socks! Now I'm basically BAREFOOT where THOUSANDS of other barefoot people have been! And then I have to put the shoes BACK ON at the end?! Those same shoes that just touched the sock floor?! I'M IN A LOOP! A DISGUSTING LOOP!

### Recommended Approach:
Focus on the absurdity of the sock-floor situation and the multiplication of bins needed for basic travel.

---

## Example 2: Deep Analysis

**Input:**
```
content: "Instructions that say 'Do not use if seal is broken'"
analysis_depth: "deep"
perspective: "both"
output_format: "both"
```

**Output:**

## Absurdity Analysis: Product Seal Warnings

You know what I love? When products say "Do not use if seal is broken." Well, HOW AM I SUPPOSED TO USE IT?! The seal is PROTECTING it! To use the product, I have to BREAK THE SEAL! But if the seal is broken, I can't use it! It's a PARADOX! It's an IMPOSSIBLE PRODUCT!

They should say "Do not use if seal is ALREADY broken." But they don't! They just say "if seal is broken" - WHICH IT WILL BE! BY ME! In about FIVE SECONDS when I want to actually USE this thing!

And who's breaking these seals before purchase? Is there a SEAL BANDIT? Someone running around stores just BREAKING SEALS for the FUN of it?! "Ha! I've broken another seal! Now NO ONE can use this mayonnaise! My work here is DONE!"

### Key Absurdities Detected:

1. **Paradoxical Instructions**: The warning creates impossible conditions
   - Comedy angle: Point out that using the product REQUIRES breaking the seal
   - Clean expression: "The only way to use it is to make it unusable!"

2. **Unclear Timing**: "Broken" could mean "already broken" or "will be broken"
   - Comedy angle: Question WHEN the seal-breaking is problematic
   - Clean expression: "Is there a GOOD time to break it?! A CEREMONY?!"

3. **Imaginary Threat**: Assumes random seal-breaking is common enough to warn against
   - Comedy angle: Invent the "seal bandit" character
   - Clean expression: "Is seal vandalism a MAJOR PROBLEM I don't know about?!"

4. **Circular Logic**: Can't verify seal is intact without opening, which breaks seal
   - Comedy angle: Catch-22 of seal inspection
   - Clean expression: "How do I CHECK the seal without BECOMING the seal-breaker?!"

5. **Vague Definition**: What counts as "broken"? Cracked? Torn? Merely opened?
   - Comedy angle: Question the gradations of seal-breakage
   - Clean expression: "Is there like a 1-10 scale? A little crack is a 3? COMPLETE BREAK is a 10?!"

### Recommended Approach:
Start with the paradox (must break seal to use), escalate to the imaginary seal bandit, then question the logic of checking for seal integrity. The circular logic angle provides strong callback potential.

---

## Integration with Brian Regan Expert

This skill operationalizes Brian Regan's clean absurdity detection methodology. When the brian-regan expert invokes this skill:

1. The expert provides content that needs comedic analysis
2. The skill returns detected absurdities with clean articulations
3. The expert integrates these observations into larger voice treatment

**Boundaries:**
- This skill focuses on DETECTION and ARTICULATION of absurdity
- The brian-regan expert handles full voice, escalation, physicality, and integration
- For full comedic transformation, use the expert; for analytical absurdity-finding, use this skill
- Can be used standalone by writers who want Brian Regan-style observations without full voice

---

## Notes

**Best Content for Analysis:**
- Arbitrary social rules and customs
- Food categories and serving sizes
- Instruction manual language
- Bureaucratic processes
- Product warnings and labels
- Common sayings that don't make literal sense
- Technology that overcomplicates simple tasks
- Contradictory signage or directions

**The "Fig Newton Test":**
If you can ask "What category does this belong in?" and get confused, it's good content for this skill.

**The "Dumb Guy Test":**
If an alien or child asking "Why do humans do this?" would reveal absurdity, it's good content for this skill.

**Clean Comedy Markers:**
- Would this work in a middle school assembly? ✓
- Would grandparents laugh at this? ✓
- Does it avoid mocking people's appearance, background, or circumstances? ✓
- Does it celebrate shared human silliness? ✓

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].