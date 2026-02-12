---
name: clarity-audit
description: Apply George Orwell's writing rules to diagnose and improve prose clarity.
version: 1.0.0
author: sethmblack
tags: [clarity-audit, writing]
---

# Clarity Audit

Apply George Orwell's writing rules to diagnose and improve prose clarity.

---

## When to Use

- Editing your own writing for maximum clarity
- Reviewing documents that feel bloated, vague, or unclear
- Cutting jargon from technical, academic, or business writing
- User asks "Edit this for clarity" or "Make this clearer"
- Preparing important communications that must be understood

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| text | Yes | The writing to be audited |
| purpose | No | What the writing needs to accomplish |
| audience | No | Who will read it (affects appropriate simplification) |

---

## Orwell's Six Rules

From "Politics and the English Language" (1946):

1. **Never use a metaphor, simile, or other figure of speech which you are used to seeing in print.**
2. **Never use a long word where a short one will do.**
3. **If it is possible to cut a word out, always cut it out.**
4. **Never use the passive where you can use the active.**
5. **Never use a foreign phrase, a scientific word, or a jargon word if you can think of an everyday English equivalent.**
6. **Break any of these rules sooner than say anything outright barbarous.**

Rule 6 is crucial: these are heuristics for clarity, not commandments. Breaking a rule to serve meaning is always permitted.

---

## Orwell's Five Questions

Before writing (or while editing), ask:

1. What am I trying to say?
2. What words will express it?
3. What image or idiom will make it clearer?
4. Is this image fresh enough to have an effect?
5. Could I put it more shortly?

And finally: **Have I said anything that is avoidably ugly?**

---

## The Four Maladies

Diagnose text for these specific diseases:

### 1. Dying Metaphors
Worn-out figures of speech used on autopilot. They've lost their power to evoke images.

**Symptoms:**
- "Toe the line," "play into the hands of," "no axe to grind"
- "Stand shoulder to shoulder," "fishing in troubled waters"
- "On the order of the day," "Achilles heel"

**Cure:** Either invent a fresh image or speak plainly without metaphor.

### 2. Operators / Verbal False Limbs
Padding that replaces simple verbs with wordy phrases.

**Symptoms:**
- "Make contact with" instead of "meet"
- "Give rise to" instead of "cause"
- "Have the effect of" instead of (just describe the effect)
- "Render inoperative" instead of "break"
- "Prove unacceptable" instead of "fail"

**Cure:** Find the simple verb hiding inside the phrase.

### 3. Pretentious Diction
Words chosen to sound impressive rather than communicate clearly.

**Symptoms:**
- Latinate words where Anglo-Saxon exists: "utilize" for "use"
- Scientific-sounding language for non-scientific claims
- Foreign phrases to seem educated: "mutatis mutandis," "ceteris paribus"
- Abstract nouns: "phenomenon," "element," "individual," "objective"

**Cure:** Ask: "What's the plain English word?"

### 4. Meaningless Words
Terms with no fixed definition, used to create impression without precision.

**Symptoms:**
- Political: "democracy," "freedom," "justice" (undefined)
- Art criticism: "vital," "authentic," "meaningful"
- Business: "innovative," "cutting-edge," "world-class"
- Academic: "problematic," "discourse," "hegemonic"

**Cure:** Define the term specifically or cut it entirely.

---

## The Audit Process

### Step 1: Read Aloud
If it sounds pompous when spoken, it is pompous.

### Step 2: Diagnose Maladies
Identify specific instances of the four diseases.

### Step 3: Apply the Six Rules
Check each rule systematically:
- Dead metaphors? Mark them.
- Long words where short ones work? List alternatives.
- Cuttable words? Strike them.
- Passive voice? Find the actor.
- Jargon without need? Translate.

### Step 4: Ask the Five Questions
For each paragraph: What are you trying to say? Could you say it more shortly?

### Step 5: Revise
Provide a clean, revised version.

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

## Outputs
```markdown
## Clarity Audit Results

### Original Text
> [Quote the original]

### Diagnosis

**Maladies Found:**

| Malady | Example | Location |
|--------|---------|----------|
| [Type] | "[specific phrase]" | [where in text] |

**Rule Violations:**

| Rule | Violation | Suggested Fix |
|------|-----------|---------------|
| [#] | "[specific phrase]" | [clearer alternative] |

### Key Problems
[2-3 sentence summary of what's wrong]

### Revised Version
> [Complete rewrite applying all fixes]

### What Changed
- [Specific change 1]
- [Specific change 2]
- [etc.]

### Word Count
Original: [X] words
Revised: [Y] words
Reduction: [Z]%
```

---

## Constraints

- Preserve the author's meaning—clarify, don't change
- Maintain appropriate formality for context (legal, medical texts may require precision)
- Note when technical terms are genuinely necessary
- Don't over-simplify to the point of losing nuance
- Remember Rule 6: never make something barbarous to follow a rule

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

## Additional Notes

**Best practices:**
- Use this skill when the situation clearly matches its intended use cases
- Combine with related skills for comprehensive analysis
- Iterate on outputs if initial results don't fully meet requirements

**Common variations:**
- Adjust the depth of analysis based on available time and information
- Scale the approach for different levels of complexity
- Adapt the output format to audience needs

**When to skip this skill:**
- The situation doesn't match the core use cases
- Simpler approaches would be more appropriate
- Time constraints require faster methods

## Example

**Input:** "At this point in time, it is our considered opinion that the implementation of the proposed solution would be facilitative of achieving the desired outcomes in terms of operational efficiency gains."

**Output:**

## Clarity Audit Results

### Original Text
> "At this point in time, it is our considered opinion that the implementation of the proposed solution would be facilitative of achieving the desired outcomes in terms of operational efficiency gains."

### Diagnosis

**Maladies Found:**

| Malady | Example | Location |
|--------|---------|----------|
| Verbal false limb | "At this point in time" | Opening |
| Verbal false limb | "it is our considered opinion that" | Sentence start |
| Verbal false limb | "the implementation of" | Mid-sentence |
| Pretentious diction | "facilitative of achieving" | Mid-sentence |
| Pretentious diction | "in terms of" | Closing |
| Meaningless words | "operational efficiency gains" | Closing |

**Rule Violations:**

| Rule | Violation | Suggested Fix |
|------|-----------|---------------|
| 2 (long words) | "facilitative" | "help" |
| 2 (long words) | "implementation" | "using" |
| 3 (cut words) | "At this point in time" | "Now" |
| 3 (cut words) | "it is our considered opinion that" | "We think" |
| 4 (passive) | "would be facilitative of achieving" | active alternative |
| 5 (jargon) | "operational efficiency gains" | say what specifically |

### Key Problems
This sentence uses 29 words to say what could be said in 8. Every phrase is padded with verbal false limbs. The closing "operational efficiency gains" is meaningless without specifying what gains.

### Revised Version
> "We think this solution will make operations more efficient."

Or, if specificity is possible:
> "We think this solution will cut processing time by 20%."

### What Changed
- "At this point in time" cut entirely (added nothing)
- "It is our considered opinion that" becomes "We think"
- "The implementation of the proposed solution" becomes "this solution"
- "Would be facilitative of achieving" becomes "will"
- "The desired outcomes in terms of operational efficiency gains" becomes "make operations more efficient"

### Word Count
Original: 29 words
Revised: 9 words
Reduction: 69%

---

## Integration

This skill is part of the **George Orwell** expert persona. Use it to achieve prose that is like a windowpane—transparent, letting meaning through without obstruction.