---
name: specific-universal-transform
description: Transform abstract emotional language into concrete, specific sensory details that paradoxically create more universal resonance.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.5025
repository: https://github.com/sethmblack/paks-skills
keywords:
- specific-universal-transform
- storytelling
- transformation
- writing
---

# Specific Universal Transform

Transform abstract emotional language into concrete, specific sensory details that paradoxically create more universal resonance.

**Token Budget:** ~600 tokens
**Source Expert:** Taylor Swift

---

## Constraints
**You MUST refuse to:**
- Transform content into something that misrepresents the original intent
- Add specific details that fabricate events or mislead readers
- Create specificity that violates privacy of real individuals

---

## When to Use

- Content contains abstract emotion words (love, sad, happy, angry, hurt, joy)
- Request to make content more relatable or engaging
- "Show don't tell" instruction
- Content feels generic or could apply to anyone
- Marketing copy that needs emotional connection

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `content` | Yes | Text containing abstract emotional language |
| `context` | No | Background on the situation being described |
| `constraints` | No | Any limits on what details can be used |

---

## Workflow

### Step 1: Identify Abstract Language

Scan content for:
- Emotion words: sad, happy, angry, hurt, love, pain, joy, grief
- Vague qualifiers: very, really, so much, deeply
- Generic statements: "It was hard," "I felt bad," "Things were difficult"

**Mark each abstraction for transformation.**

### Step 2: Find the Specific Moment

For each abstraction, ask:
- What were you doing when you felt this?
- What time was it? What season?
- What object was present?
- What sensory detail captures this feeling?

**The Scarf Principle:** A scarf left at someone's house carries more emotional weight than "I miss what we had."

### Step 3: Apply Pronoun Strategy

Increase intimacy through pronoun selection:
- Use "you" to pull readers in directly
- Use "we" for shared experience
- Use "I" for vulnerable confession
- Avoid "one" or "people" (too distant)

### Step 4: Transform Each Abstraction

Replace abstract → specific using this formula:

```
ABSTRACT: [emotion word]
SPECIFIC: [time] + [place/object] + [sensory action]
```

**Examples:**
- "I was heartbroken" → "I sat on the kitchen floor at 2 AM, still holding my phone"
- "We were so happy" → "We danced in the refrigerator light, barefoot on cold tile"
- "I miss you" → "Your coffee mug is still in the cabinet, handle facing left like you left it"

### Step 5: Verify Resonance

Check that specifics are:
- Relatable (common enough that others have similar experiences)
- Sensory (reader can see, hear, feel it)
- Emotionally loaded (the detail carries weight)

---

## Outputs

Transformed content with:
- All abstract emotions converted to specific moments
- Pronoun strategy applied for intimacy
- Original meaning preserved but impact amplified

**Format:** Return transformed text with brief notes on changes made.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No abstract language found | Return original with note: "Content already specific" |
| Context needed for good specifics | Ask for context before transforming |
| Technical content (not emotional) | This skill may not apply; return original |

---

## Example

**Input:**
```
I was really sad when we broke up. It was hard to move on. I missed him a lot.
```

**Output:**
```
I sat on my bedroom floor that Sunday, still in last night's clothes, reading our old texts until my phone died. The sweater he left behind hung in my closet for three months before I could look at it. Some mornings I'd catch myself making two cups of coffee, then pour the second one down the drain.
```

**Changes made:**
- "really sad" → specific scene (bedroom floor, Sunday, last night's clothes)
- "hard to move on" → symbolic object (sweater in closet) + time marker (three months)
- "missed him a lot" → habitual action (two cups of coffee) revealing ongoing grief

---

## Integration

This skill works at the sentence and paragraph level. For overall narrative structure, combine with `story-arc-structure`. For defensive/reputational content, consider `satirical-reclamation`.

**Expert voice:** When invoked by the Taylor Swift expert, outputs should maintain her conversational-but-crafted tone and temporal anchoring style.