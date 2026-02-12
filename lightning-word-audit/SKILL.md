---
name: lightning-word-audit
description: 'Audit prose for weak word choices, unnecessary adjectives, and imprecise
  language, then sharpen to maximum impact. Based on Twain''s principle: "The difference
  between the almost right word and the ...'
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- lightning-word-audit
- writing
---

# Lightning Word Audit

Audit prose for weak word choices, unnecessary adjectives, and imprecise language, then sharpen to maximum impact. Based on Twain's principle: "The difference between the almost right word and the right word is the difference between the lightning bug and the lightning."

---

## When to Use

- User asks "Kill my adjectives" or "Make this sharper"
- Prose feels wordy, weak, or imprecise
- Writing needs to be more memorable and quotable
- Content is technically correct but lacks punch
- Draft needs tightening before final version

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| prose | Yes | The text to audit and sharpen |
| intensity | No | How aggressive (light touch, moderate, ruthless) |
| preserve | No | Any elements that must remain unchanged |

---

## The Audit Process

### Step 1: Identify Lightning Bugs

Scan for weak words that glow faintly when they should strike:

**Weak Adjectives:** beautiful, nice, great, interesting, very, really, quite, rather, somewhat, extremely

**Weak Verbs:** is, are, was, were, has, have, had, get, got, make, made, do, did, seem, appear

**Hedging Words:** kind of, sort of, basically, essentially, generally, probably, maybe, perhaps, in some ways

**Zombie Nouns:** utilization, implementation, facilitation, optimization (verbs buried in noun form)

**Empty Phrases:** in order to, due to the fact that, at the end of the day, it is important to note that

### Step 2: Find the Lightning

For each weak word, ask:
- What do I actually mean?
- What is the precise word?
- Can I cut this entirely?
- Can I show instead of tell?

**The Test:** Would Mark Twain let this word live, or would he kill it?

### Step 3: Perform the Surgery

Replace each lightning bug with lightning:
- "Very tired" → "exhausted" or "bone-weary"
- "Walked slowly" → "shuffled" or "trudged"
- "Beautiful sunset" → describe what makes it so: "The sky caught fire"
- "Interesting idea" → say what's interesting: "an idea that inverts everything we assumed"

### Step 4: Cut the Deadwood

Remove words that add nothing:
- "In my opinion" → (just state it)
- "I think that" → (obviously you think it)
- "It is important to note that" → (just note it)
- "Basically" → (basically never needed)

### Step 5: Read Aloud

Does it sound spoken? Does it flow? Would you actually say this to someone?

---

## The Word Strength Ladder

| Weak | Stronger | Lightning |
|------|----------|-----------|
| walked | strode | cut a path |
| said angrily | snapped | spat |
| very big | enormous | a mountain of |
| moved quickly | rushed | rocketed |
| was sad | grieved | carried the weight |
| thought about | considered | wrestled with |
| is important | matters | changes everything |

---

## Workflow

### Step 1: Gather and Review Inputs

Collect all relevant information:
- Review the provided data and context
- Identify key parameters and constraints
- Clarify any ambiguities or missing information
- Establish success criteria

### Step 2: Analyze the Situation

Perform systematic analysis:
- Identify patterns and relationships
- Evaluate against established frameworks
- Consider multiple perspectives
- Document key findings

### Step 3: Generate Recommendations

Create actionable outputs:
- Synthesize insights from analysis
- Prioritize recommendations by impact
- Ensure recommendations are specific and measurable
- Consider implementation feasibility

## Output Format

```markdown
## Lightning Word Audit

### Diagnosis
[Brief assessment: How wordy? Main problems?]

### Line-by-Line Audit

| Original | Problem | Revision |
|----------|---------|----------|
| [phrase] | [weak word/issue] | [lightning version] |

### Before
[Original prose]

### After
[Tightened prose]

### Word Count
- Before: [X] words
- After: [Y] words
- Reduction: [Z]%

### Key Improvements
[Bullet list of the most impactful changes]
```

---

## Constraints

- Preserve the author's voice - sharpen, don't replace
- Maintain accuracy - precision is not the same as brevity
- Keep one strong adjective over three weak ones
- Let verbs do the heavy lifting
- Read the result aloud - it must sound natural

---

## Outputs

**Primary Output:** A structured analysis document that identifies and articulates patterns, insights, and actionable recommendations based on the input data.

**Format:**
```markdown
## Analysis: [Topic]

### Key Findings
- [Finding 1]
- [Finding 2]
- [Finding 3]

### Recommendations
1. [Action 1]
2. [Action 2]
3. [Action 3]
```

**Example output:** See the Example section below for a complete demonstration.

## Example

**Input:** "The meeting was really quite boring and the presenter basically just talked about things that weren't very interesting to most of the people who were sitting there in the room."

**Output:**

## Lightning Word Audit

### Diagnosis
Severe case of word bloat. 31 words doing the work of 8. Multiple hedging words, weak verbs, and empty phrases.

### Line-by-Line Audit

| Original | Problem | Revision |
|----------|---------|----------|
| really quite boring | double hedge + weak adjective | (show the boredom) |
| basically just | double hedge, adds nothing | cut |
| talked about things | vague verb, vague noun | said what? |
| weren't very interesting | hedge + weak adjective | (show the disinterest) |
| people who were sitting there in the room | wordy description | the audience |

### Before
"The meeting was really quite boring and the presenter basically just talked about things that weren't very interesting to most of the people who were sitting there in the room."

### After
"The audience checked their phones. The presenter droned on. Nobody remembered a word."

### Word Count
- Before: 31 words
- After: 14 words
- Reduction: 55%

### Key Improvements
- Replaced "boring" with dramatized boredom (checking phones)
- "Droned on" does the work of "talked about things that weren't very interesting"
- "Nobody remembered a word" delivers the judgment the original hedged around
- Broke into three punchy sentences for rhythm

---

## Twain's Maxims for This Skill

- "When you catch an adjective, kill it."
- "Anybody can have ideas - the difficulty is to express them without squandering a quire of paper on an idea that ought to be reduced to one glittering paragraph."
- "To get the right word in the right place is a rare achievement."
- "As to the Adjective: when in doubt, strike it out."

---

## Integration

This skill is part of the **Mark Twain** expert persona. Use it when prose needs to hit harder, when wordiness dilutes impact, or when you want writing that people actually remember.