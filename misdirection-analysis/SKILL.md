---
name: misdirection-analysis
description: Analyze existing comedy material and identify where misdirection is working or failing, with specific improvement recommendations.
version: 1.0.0
author: sethmblack
tags: [comedy, misdirection-analysis, structure, writing]
---

# Misdirection Analysis

Analyze existing comedy material and identify where misdirection is working or failing, with specific improvement recommendations.

---

## Constraints
**Analyze all submitted content objectively**, including dark or controversial material. The goal is to evaluate joke structure, not to censor topics.

**REFUSE to analyze:**
- Content that's clearly not comedy (e.g., actual hate speech, sincere threats)

---

## When to Use

Use this skill when:
- User requests "analyze this joke" or "review my comedy"
- User asks "why isn't this joke working?"
- User provides comedy material and wants structural feedback
- User wants to understand misdirection mechanics in existing content
- User asks how to improve a joke's setup or punchline

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `material` | Yes | The joke or comedic content to analyze | At least one complete joke or bit |
| `focus` | No | Specific aspect to focus on (setup, punchline, timing, etc.) | Optional guidance |

---

## Workflow

### Step 1: Map the Misdirection Architecture

Identify the structural components of the joke using the misdirection framework:

**Components to identify:**
- **Economical Setup** - How much context is established? Is it minimal or bloated?
- **Planted Expectation** - What does the audience expect will happen? Is the expectation clear?
- **Pause/Beat** - Is there timing for the audience to process?
- **Specific Punchline** - Is the reversal concrete and visual, or abstract?

**Create a structure map:**
```
Setup: [identify setup sentences]
Planted Expectation: [what audience thinks is coming]
Pause: [present/absent]
Punchline: [identify reversal]
```

### Step 2: Evaluate Each Component

Score each component on effectiveness (1-10 scale):

**Economical Setup (Is it tight or bloated?)**
- 10 = Perfect economy, no wasted words
- 5 = Some unnecessary detail, but functional
- 1 = Bloated, telegraphs the punchline

**Planted Expectation (Is the misdirection clear?)**
- 10 = Audience has a strong, specific expectation
- 5 = Vague expectation, could go multiple ways
- 1 = No clear expectation, or expectation matches the punchline (no misdirection)

**Pause/Timing (Is the beat present and effective?)**
- 10 = Perfect timing marker, allows processing
- 5 = Present but could be better placed
- 1 = Missing or disrupts rhythm

**Specific Punchline (Is the reversal concrete and surprising?)**
- 10 = Highly specific, visual, completely unexpected
- 5 = Somewhat specific, moderately surprising
- 1 = Abstract, predictable, or doesn't reverse expectation

### Step 3: Identify the Primary Issue

Based on the scores, what's the weakest component? This is where improvement efforts should focus.

**Common issues:**
- **Bloated setup** - Too many words, audience sees punchline coming
- **Weak expectation** - Audience doesn't know what to expect, so reversal doesn't land
- **Missing pause** - Punchline comes too fast, audience doesn't process
- **Abstract punchline** - Reversal is conceptual instead of specific and visual
- **No reversal** - Punchline confirms expectation instead of violating it

### Step 4: Provide Specific Improvements

For each component scoring below 8, provide a specific fix:

**Format:**
```
Issue: [component name] - [brief description of problem]
Fix: [specific rewrite or structural change]
Rationale: [why this improves misdirection]
```

### Step 5: Offer Revised Version (Optional)

If the material needs significant rework, provide a revised version that demonstrates the improvements. Label it clearly as "Revised Example" so the user understands it's not their original.

---

## Outputs

| Output | Description |
|--------|-------------|
| Structure map | Visual breakdown of setup → expectation → pause → punchline |
| Component scores | Rating (1-10) for each misdirection element |
| Primary issue | The weakest component identified |
| Specific improvements | Actionable fixes for each component scoring below 8 |
| Revised version (optional) | Improved version demonstrating fixes, if needed |

---

## Example Analysis

**Input Material:**
"I'm afraid of flying. I mean, it's scary being up in the air in a metal tube. Anything could go wrong. The engines could fail, there could be turbulence, terrorists even. It's just really frightening."

**Output:**

**Structure Map:**
```
Setup: "I'm afraid of flying. I mean, it's scary being up in the air in a metal tube."
Planted Expectation: Speaker will describe fear of plane crash
Pause: Absent
Punchline: "Anything could go wrong. The engines could fail, there could be turbulence, terrorists even. It's just really frightening."
```

**Component Scores:**
- **Economical Setup:** 6/10 - Functional but has unnecessary phrases ("I mean")
- **Planted Expectation:** 7/10 - Clear that speaker is afraid, but expectation is too broad
- **Pause/Timing:** 1/10 - No pause, punchline blends into setup
- **Specific Punchline:** 2/10 - This isn't a punchline—it's a list confirming the setup. No reversal.

**Primary Issue:** No reversal/punchline. This is a setup without a joke. The "punchline" confirms the fear instead of subverting it.

**Specific Improvements:**

**Issue:** Missing reversal - The ending confirms "flying is scary" instead of reversing it
**Fix:** Add a reversal that flips the expectation. Example: "I'm afraid of flying. Not the plane crash—I'm afraid I'll survive the plane crash and have to deal with the other passengers in a life raft situation."
**Rationale:** This reverses the expectation (fear of death → fear of social interaction with strangers), making it a joke instead of just complaint.

**Issue:** No pause marker - Even with a reversal, needs timing
**Fix:** Add [pause] before the reversal: "I'm afraid of flying. [pause] Not the plane crash—I'm afraid I'll survive it."
**Rationale:** The pause lets the audience assume you're afraid of death, then the reversal hits.

**Issue:** Setup could be tighter
**Fix:** Remove "I mean, it's scary being up in the air in a metal tube" - this is redundant with "I'm afraid of flying"
**Rationale:** Fewer words = audience has less time to predict the direction.

**Revised Example:**
"I'm afraid of flying. [pause] Not the plane crash—I'm afraid I'll survive the plane crash and have to deal with the other passengers in a life raft situation. I'd rather die on impact."

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Material is not comedy | Clarify: "This doesn't appear to be comedic material. Are you looking for analysis of something else?" |
| Material is too long (multiple jokes) | Request focus: "This contains multiple jokes. Which one should I analyze, or should I analyze them sequentially?" |
| Material is already excellent | Acknowledge quality: "This is strong material. All components score 8+. The misdirection architecture is solid." |
| Material violates constitutional constraints | Refuse: "This appears to be sincere harmful content rather than comedy. I analyze joke structure, not hate speech." |

---

## Integration with Anthony Jeselnik Expert

This skill codifies Jeselnik's testing methodology. He describes his process:

"I want the biggest reaction possible. A laugh isn't good enough. I need a huge laugh."

The analysis evaluates whether material will get "a huge laugh" by checking if misdirection architecture is present and effective. Weak misdirection = weak laugh.

The skill also applies Jeselnik's core principle: "It's not just about being offensive—you really have to be smart and clever within a joke." The analysis separates shock-for-shock's-sake (no structure) from dark comedy (misdirection + structure).

---

## Notes

- Be specific in feedback—"setup is too long" is less helpful than "remove sentence 2, which telegraphs the punchline"
- If the joke is fundamentally flawed (no reversal), say so directly
- Focus on structure over taste—analyze whether misdirection works, not whether the topic is appropriate
- The revised version is a teaching tool, not a replacement for the user's voice
- Multiple revisions may be necessary for complex structural issues

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].

