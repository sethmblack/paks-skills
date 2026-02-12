---
name: ruthless-cut
description: Apply Hemingway's editing principles to eliminate unnecessary words, adjectives, adverbs, and qualifications from any prose.
version: 1.0.0
author: sethmblack
tags: [ruthless-cut, structure, writing]
---

# Ruthless Cut

Apply Hemingway's editing principles to eliminate unnecessary words, adjectives, adverbs, and qualifications from any prose.

---

## When to Use

- Prose feels bloated or overwritten
- Too many adjectives and adverbs
- Sentences are longer than they need to be
- Writing sounds self-conscious or trying too hard
- Request for "Hemingway edit" or "make this leaner"
- Word count must be reduced without losing meaning

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| prose | Yes | The text to edit |
| reduction_target | No | Desired percentage reduction (default: cut until it hurts) |
| preserve | No | Any elements that must be kept |

---

## The Five Cuts

### Cut 1: Adjectives
Adjectives weaken nouns. A strong noun needs no modifier.

**Questions to ask:**
- Does this adjective add information the noun doesn't carry?
- Is there a stronger noun that contains the adjective?
- Would the sentence work without it?

**Before:** "The small, frightened child ran across the dark, empty street."
**After:** "The child ran across the street."

If "small" matters, show size through action. If "frightened" matters, show fear through behavior. "Dark" and "empty" might earn their place - test each one.

### Cut 2: Adverbs
Adverbs almost never earn their place. They modify verbs that should be strong enough alone.

**The test:** Is there a verb that contains the adverb?

**Before:** "He walked slowly toward the door."
**After:** "He shuffled toward the door." Or: "He walked toward the door."

**Hemingway's rule:** If the verb needs help, choose a better verb.

### Cut 3: Qualifications
Words that hedge, soften, or retreat from commitment.

**Kill these:** very, really, quite, somewhat, rather, fairly, slightly, almost, basically, actually, literally, essentially, generally, virtually, practically

**Before:** "It was actually quite difficult and rather frustrating."
**After:** "It was difficult."

### Cut 4: Redundancy
Words that say what's already been said.

**Kill these:**
- "past history" - history is past
- "future plans" - plans are future
- "completely destroyed" - destroyed is complete
- "absolutely essential" - essential is absolute
- "advance warning" - warnings come in advance
- "brief moment" - moments are brief

**Before:** "She made a sudden, unexpected decision."
**After:** "She decided."

### Cut 5: Passive Construction
Passive voice adds words and hides the actor.

**Before:** "The ball was thrown by John."
**After:** "John threw the ball."

Passive has uses. In most cases, active is cleaner.

---

## Workflow

### Step 1: **First pass:** Mark all adjectives. Test each one. Cut or replace.



### Step 2: **Second pass:** Mark all adverbs. Most die. Replace the verb if needed.



### Step 3: **Third pass:** Find qualifiers (very, really, quite, rather). Kill them.



### Step 4: **Fourth pass:** Find redundancy. Eliminate.



### Step 5: **Fifth pass:** Find passive voice. Convert where appropriate.



### Step 6: **Final pass:** Read aloud. Does every word earn its place? If you can cut it without loss, cut it.



---

## Output Format

```markdown
## Ruthless Cut

### Original
[Original prose]

**Word count:** [X]

### Edited Version
[Cut prose]

**Word count:** [Y] (reduced by Z%)

### What Was Cut
| Original | Edited | Why |
|----------|--------|-----|
| [phrase] | [phrase] | [adjective/adverb/qualifier/redundant/passive] |

### Notes
[Any observations about the cuts or choices made]
```

---

## Constraints

- Cut for clarity, not obscurity
- Preserve meaning while eliminating excess
- Don't cut structural words that provide necessary rhythm
- Keep cuts that serve the voice or character in dialogue
- When uncertain, cut - what remains will be stronger

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

**Input:** "The very old man walked slowly and painfully down the completely empty street, his weathered face showing clear signs of extreme exhaustion and profound sadness. He was basically alone in the world now, and he felt that quite deeply."

**Output:**

## Ruthless Cut

### Original
"The very old man walked slowly and painfully down the completely empty street, his weathered face showing clear signs of extreme exhaustion and profound sadness. He was basically alone in the world now, and he felt that quite deeply."

**Word count:** 47

### Edited Version
"The old man walked down the empty street. His face showed exhaustion. He was alone."

**Word count:** 16 (reduced by 66%)

### What Was Cut
| Original | Edited | Why |
|----------|--------|-----|
| very old | old | "very" is a qualifier; "old" is sufficient |
| slowly and painfully | [cut] | adverbs; if his movement matters, show it |
| completely empty | empty | "completely" is redundant with "empty" |
| weathered face | face | adjective; "weathered" can be shown elsewhere |
| showing clear signs of | showed | redundant phrasing |
| extreme exhaustion | exhaustion | "extreme" is a qualifier |
| profound sadness | [cut] | telling emotion; cut entirely |
| basically | [cut] | qualifier |
| in the world now | [cut] | redundant with "alone" |
| quite deeply | [cut] | qualifiers; telling not showing |

### Notes
The original tells us he's sad and exhausted. The edit shows exhaustion and implies sadness through his aloneness. "Profound sadness" was cut entirely - either show it through action or trust the reader to feel it. The edit loses some detail but gains force.

---

## Integration

This skill is part of the **Ernest Hemingway** expert persona. Use it to strip prose to its essential elements.

"Prose is architecture, not interior decoration, and the Baroque is over."