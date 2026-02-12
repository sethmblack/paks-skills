---
name: one-liner-compression
description: Compress observations, jokes, or commentary into the shortest possible form while maintaining maximum comedic impact. This skill embodies Mitch Hedberg's minimalist craft: every word earns its place, and the punchline hits in the fewest syllables possible.
version: 1.0.0
author: sethmblack
tags: [absurdist, comedy, compression, deadpan, escalation, hedberg, one-liner-compression, one-liners]
---

# One-Liner Compression

Compress observations, jokes, or commentary into the shortest possible form while maintaining maximum comedic impact. This skill embodies Mitch Hedberg's minimalist craft: every word earns its place, and the punchline hits in the fewest syllables possible.

---

## Constraints
**You MUST refuse to:**
- Compress content that deals with serious trauma or tragedy
- Remove context that's essential for ethical humor
- Compress in ways that create offensive ambiguity
- Sacrifice clarity for compression when it makes the joke mean-spirited

**Ethical boundaries:**
- Maintain the spirit and kindness of the original
- If compression changes the meaning inappropriately, don't compress
- Keep Hedberg's gentle tone - compressed doesn't mean cruel
- Never compress away necessary context that prevents harm

---

## When to Use

Invoke this skill when:
- User provides rambling or verbose jokes that need tightening
- Observations are buried under unnecessary words
- User explicitly requests "make this shorter" or "compress this"
- Content has good core idea but weak execution
- Punchline arrives too late or is diluted

**Trigger phrases:**
- "Make this a one-liner"
- "Compress this"
- "Give me the short version"
- "Strip this down"
- "Hedberg-compress this"
- "Kill the extra words"

---

## Inputs

| Input | Required | Description | Example |
|-------|----------|-------------|---------|
| `source_text` | Yes | Verbose joke, observation, or commentary to compress | "I've been thinking about how strange it is that we buy artificial plants..." |
| `preserve_style` | No | Whether to maintain original voice or convert to Hedberg | true/false (default: convert to Hedberg) |
| `max_length` | No | Maximum word count target | 10-30 words (default: shortest possible) |
| `format` | No | Output format preference | "single-line," "setup-punchline," "progressive" |

---

## Workflow

### Step 1: Identify the Core Insight

Strip away all decoration and find the essential observation. What is the actual joke or insight?

**Ask:**
- What's the surprising element?
- What's the twist or reversal?
- What's the one thing that needs to be communicated?

**Example:**
- Verbose: "I've been thinking about how strange it is that we have these plants in our homes that aren't real, they're artificial, and yet we're supposed to take care of them as if they were real, but I forgot to do that and they died anyway"
- Core insight: Fake plants died because I didn't fake water them

### Step 2: Strip Non-Essential Elements

Remove everything that doesn't serve the core insight:

**Eliminate:**
- Preambles: "I've been thinking about..." "It's interesting that..." "You know what's weird?"
- Qualifiers: "kind of," "sort of," "maybe," "a little bit"
- Redundancies: "artificial plants that aren't real"
- Explanations: "what I mean is..." "in other words..."
- Transitions: "and then," "so anyway," "but the thing is"
- Weak verbs: "started to," "began to," "tried to"

**Keep:**
- Setup (minimum necessary)
- Twist/punchline
- Connective tissue (only if essential)

### Step 3: Find the Shortest Path to the Punchline

Map the most direct route from setup to punchline. Remove all detours.

**Structure options:**

**Format A: Single statement with embedded twist**
```
"[Setup with twist built in]."
```
Example: "My fake plants died because I did not pretend to water them."

**Format B: Setup, then punchline**
```
"[Minimal setup]. [Punchy conclusion]."
```
Example: "I haven't slept for ten days. That would be too long."

**Format C: Progressive reveal**
```
"[State observation]. [Complication]. [Twist]."
```
Example: "I'm against picketing. But I don't know how to show it."

### Step 4: Test for Dead Weight

Read the compressed version. Can any word be removed without losing meaning or impact?

**Word-by-word audit:**
- Adjectives: Kill unless essential
- Adverbs: Kill unless essential
- Articles: Keep only if removal causes confusion
- Pronouns: Use only when reference is crystal clear

**Example compression:**
- Before: "My very fake plants unfortunately died..."
- After: "My fake plants died..."
- Reason: "very" and "unfortunately" add nothing

### Step 5: Verify Hedberg Delivery Pattern

Ensure the compressed version follows Hedberg's delivery patterns:

**Checklist:**
- [ ] Present tense when possible ("I'm against" not "I was against")
- [ ] Simple sentence structure (avoid subordinate clauses)
- [ ] Natural speech patterns (contractions okay: "I'm" not "I am")
- [ ] Casual connectors only if they help flow ("but," "so")
- [ ] No exclamation points
- [ ] Twist/punchline in final phrase
- [ ] Deadpan tone (no "isn't this crazy?" signaling)

---

## Outputs

**Primary Output:** Compressed one-liner(s) in Hedberg style

**Format:**
```markdown
## Original
[Verbose source text]

## Compressed
[One-liner version]

## Compression Analysis (optional)
- Original word count: X
- Compressed word count: Y
- Reduction: Z%
- What was removed: [explanation]
- What was preserved: [explanation]
```

---

## Examples

### Example 1: Fake Plants

**Input:**
```
source_text: "I've been thinking about how strange it is that we have these plants in our homes that aren't real, they're artificial, and yet we're supposed to take care of them as if they were real, but I forgot to do that and they died anyway"
```

**Output:**
```markdown
## Original (48 words)
"I've been thinking about how strange it is that we have these plants in our homes that aren't real, they're artificial, and yet we're supposed to take care of them as if they were real, but I forgot to do that and they died anyway"

## Compressed (13 words)
"My fake plants died because I did not pretend to water them."

## Compression Analysis
- Original word count: 48
- Compressed word count: 13
- Reduction: 73%
- What was removed: Preamble ("I've been thinking"), redundancy ("aren't real, they're artificial"), explanation ("supposed to take care of them as if they were real")
- What was preserved: Core paradox (fake plants + died + didn't pretend to water)
- Why it works: The compression makes the absurdity more obvious - the parallel structure of "fake plants / pretend to water" hits harder without explanation
```

### Example 2: Picketing

**Input:**
```
source_text: "You know, I've always felt like I'm really against the concept of picketing, like standing outside with signs and protesting and all that, but the ironic thing is, if I wanted to express my opposition to picketing, I'd probably have to picket, which would be contradictory, so I just don't know what to do about it"
```

**Output:**
```markdown
## Original (56 words)
"You know, I've always felt like I'm really against the concept of picketing, like standing outside with signs and protesting and all that, but the ironic thing is, if I wanted to express my opposition to picketing, I'd probably have to picket, which would be contradictory, so I just don't know what to do about it"

## Compressed (13 words)
"I'm against picketing, but I don't know how to show it."

## Compression Analysis
- Original word count: 56
- Compressed word count: 13
- Reduction: 77%
- What was removed: Preamble ("you know"), qualifiers ("really"), explanations ("standing outside with signs"), spelling out the irony ("which would be contradictory")
- What was preserved: The central paradox (against picketing / can't demonstrate opposition without picketing)
- Why it works: The compressed version makes you figure out why it's impossible, which is funnier than having it explained
```

### Example 3: Sleep Duration

**Input:**
```
source_text: "Someone asked me how long it's been since I slept, and I told them I haven't slept in ten days, and they were really concerned, but what I meant was not that I've been awake for ten consecutive days, because that would be way too long and probably impossible, I just meant I haven't slept recently, you know, in the past ten days"
```

**Output:**
```markdown
## Original (64 words)
"Someone asked me how long it's been since I slept, and I told them I haven't slept in ten days, and they were really concerned, but what I meant was not that I've been awake for ten consecutive days, because that would be way too long and probably impossible, I just meant I haven't slept recently, you know, in the past ten days"

## Compressed (12 words)
"I haven't slept for ten days, because that would be too long."

## Compression Analysis
- Original word count: 64
- Compressed word count: 12
- Reduction: 81%
- What was removed: The question setup, the explanation of the misunderstanding, the clarification
- What was preserved: The misdirection (setup implies consecutive sleeplessness, punchline reveals it's just within ten-day span)
- Why it works: By removing the explanation, the listener has to parse "because that would be too long" and realize it means "that's not what I meant," which creates an active discovery moment
```

### Example 4: Club Sandwich

**Input:**
```
source_text: "It's funny because every time I go to a restaurant I tend to order a club sandwich pretty frequently, and the thing that's amusing about it is that clubs usually have membership requirements, right? Like you have to be a member to get in and enjoy the benefits. So technically speaking, I'm ordering a club sandwich even though nobody has verified my club membership status. How am I getting away with this?"
```

**Output:**
```markdown
## Original (68 words)
"It's funny because every time I go to a restaurant I tend to order a club sandwich pretty frequently, and the thing that's amusing about it is that clubs usually have membership requirements, right? Like you have to be a member to get in and enjoy the benefits. So technically speaking, I'm ordering a club sandwich even though nobody has verified my club membership status. How am I getting away with this?"

## Compressed (18 words)
"I order the club sandwich all the time, but I'm not even a member, man. I don't know how I get away with it."

## Compression Analysis
- Original word count: 68
- Compressed word count: 18
- Reduction: 74%
- What was removed: Meta-commentary ("it's funny," "the thing that's amusing"), explanation of what clubs are, formal language
- What was preserved: Core absurdity (ordering club sandwich without membership), Hedberg's casual delivery ("man")
- Why it works: The compressed version trusts the audience to understand clubs have members without explanation, and the casual "man" keeps Hedberg's laid-back tone
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Source text has no joke/insight | Note that compression requires a core insight first; suggest identifying what the point is before compressing |
| Joke is already optimally compressed | Acknowledge it's already tight; suggest alternative phrasings or note no compression needed |
| Compression removes essential context | Include minimum context necessary; note where the line is between compression and clarity loss |
| Multiple jokes in source | Separate and compress each independently, or ask which to prioritize |
| Joke requires longer setup | Note some jokes need setup; offer "short" version vs. "shortest possible" version |

---

## Integration with Mitch Hedberg Expert

This skill is a core component of the Mitch Hedberg expert voice. When the expert invokes this skill:

1. **Automatic activation** - Expert should use this when encountering verbose humor or observations
2. **Voice consistency** - All output maintains Hedberg's compressed, deadpan delivery
3. **Combines with other techniques** - Often used AFTER literalist-reframe or absurd-escalation to tighten the result

**Expert → Skill relationship:**
- Expert provides the voice and persona
- Skill provides the compression methodology
- Together they produce authentic Hedberg-style minimalist comedy

---

## Quality Checklist

Before delivering output, verify:

- [ ] Core insight is preserved
- [ ] All non-essential words removed
- [ ] Punchline is in final phrase/clause
- [ ] Present tense used when possible
- [ ] Simple sentence structure (no complex clauses)
- [ ] Casual, natural language (contractions okay)
- [ ] No exclamation points
- [ ] Deadpan tone maintained
- [ ] Word count is minimized without losing clarity
- [ ] Each remaining word earns its place

---

## Advanced Techniques

### The Parallel Structure

When the joke involves two related elements, use parallel structure for compression and impact.

**Example:**
"My fake plants died because I did not pretend to water them."
- "fake plants" parallels "pretend to water"
- The parallel structure emphasizes the absurd logic

### The Delayed Clarification

Setup implies one meaning, punchline clarifies in unexpected direction.

**Example:**
"I haven't slept for ten days, because that would be too long."
- First clause: sounds like bragging about stamina
- Second clause: reveals it means "within the past ten days"

### The Understated Reversal

State the opposite of what's expected, delivered casually.

**Example:**
"An escalator can never break: it can only become stairs. Sorry for the convenience."
- Expected: apology for inconvenience
- Delivered: apology for convenience (it's now more useful)

---

## Notes

**Why this skill is valuable:**

Compression is difficult because:
1. Writers get attached to their words
2. Setup often feels necessary even when it isn't
3. Hard to know where the line is between compression and confusion
4. Most people explain too much

This skill provides objective criteria for what to cut and what to keep.

**Hedberg's mastery:**

Mitch Hedberg's jokes feel effortless because every word is load-bearing. He trusted his audience to make connections without spelling them out. His compression wasn't about being brief; it was about being precise. No word worked harder than it had to, and no word did less than its share.

**The acid test:**

Can you remove one word without losing the joke? If yes, remove it. Repeat until no.

**Common mistake:**

Compression is not summarization. Don't remove the twist, the paradox, or the surprise to make it shorter. Remove the preamble, the explanation, and the unnecessary decoration. The joke itself is sacred - everything around it is negotiable.