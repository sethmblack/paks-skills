---
name: propaganda-pattern-analysis
description: Identify manipulation techniques in communication using Orwell's framework for understanding how language controls thought.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.1687
repository: https://github.com/sethmblack/paks-skills
keywords:
- propaganda-pattern-analysis
- writing
---

# Propaganda Pattern Analysis

Identify manipulation techniques in communication using Orwell's framework for understanding how language controls thought.

---

## When to Use

- Analyzing political speeches, press releases, or campaign materials
- Evaluating advertising and marketing for manipulation
- Assessing social media content for influence operations
- User asks "Is this propaganda?" or "How is this manipulating me?"
- Teaching media literacy and critical thinking
- Examining organizational communications for manipulation patterns

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| text | Yes | The communication to analyze |
| source | No | Who created this (helps identify motives) |
| context | No | Where and when this appeared |
| target_audience | No | Who is meant to receive this |

---

## Core Principle

Orwell understood propaganda from the inside, having worked at the BBC during WWII. His insight: propaganda doesn't just tell lies—it manipulates how people can think by controlling language itself.

From *Nineteen Eighty-Four*:
> "The purpose of Newspeak was not only to provide a medium of expression for the worldview and mental habits proper to the devotees of Ingsoc, but to make all other modes of thought impossible."

Propaganda works by:
1. **Limiting what can be said** (vocabulary control)
2. **Redefining what words mean** (semantic manipulation)
3. **Creating emotional association** (bypassing reason)
4. **Establishing presuppositions** (smuggling assumptions)
5. **Attacking the concept of truth itself** (making discernment impossible)

---

## Propaganda Techniques

### 1. Vocabulary Control (Newspeak)

**What it does:** Eliminates or redefines words to make certain thoughts difficult or impossible.

**Signs:**
- Key terms are redefined to mean their opposite
- Nuanced vocabulary is replaced with crude binaries
- Certain topics become "unspeakable"
- Abbreviations strip emotional connotation ("collateral damage")

**Detection question:** What concepts become harder to express in this language?

### 2. Doublethink

**What it does:** Requires holding contradictory beliefs simultaneously, or changing position without acknowledging the change.

**Signs:**
- "War is Peace, Freedom is Slavery, Ignorance is Strength"
- Historical positions are denied or memory-holed
- Contradictions are explained as "nuance" or "evolution"
- Pointing out contradictions is treated as bad faith

**Detection question:** Does this require believing two incompatible things?

### 3. Emotional Loading

**What it does:** Attaches strong emotional associations to bypass rational evaluation.

**Signs:**
- Prestige words: "freedom," "innovation," "justice" (undefined)
- Stigma words: "radical," "extremist," "dangerous" (applied without evidence)
- Appeals to fear, pride, or belonging
- Imagery designed to trigger visceral response

**Detection question:** Remove the emotional language—what factual claim remains?

### 4. Memory Holing

**What it does:** Erases or revises inconvenient history to serve present needs.

**Signs:**
- Past positions are denied ("We never said that")
- Records are altered or made inaccessible
- Contradicting the revised history becomes "conspiracy theory"
- "That was different" without explaining how

**Detection question:** Is there an accessible record of what was actually said before?

### 5. Presupposition Smuggling

**What it does:** Embeds contested claims as assumed background facts.

**Signs:**
- Questions that can't be answered without accepting the premise ("Have you stopped beating your wife?")
- Framing that assumes the conclusion
- "Everyone knows" or "It goes without saying"
- False binaries that exclude other options

**Detection question:** What must I accept as true just to engage with this statement?

### 6. Appeal to Unnamed Authority

**What it does:** Invokes expertise or consensus that can't be verified.

**Signs:**
- "Experts say" (which experts?)
- "Studies show" (which studies?)
- "Many people are saying" (who?)
- "It's well established" (by whom?)

**Detection question:** Can I identify and verify the actual source?

### 7. Thought-Terminating Cliches

**What it does:** Ends discussion with phrases that sound profound but prevent further inquiry.

**Signs:**
- "It is what it is"
- "Everything happens for a reason"
- "Both sides have a point"
- "We'll have to agree to disagree"
- "That's just your opinion"

**Detection question:** Does this phrase advance understanding or shut it down?

### 8. The Big Lie

**What it does:** Makes a claim so audacious that people assume there must be truth to it.

**Signs:**
- Extraordinary claims without extraordinary evidence
- Repetition as substitute for proof
- Scale of claim used to intimidate questioners
- Questioning is treated as proof of bad faith

**Detection question:** What would verification actually look like?

---

## Analysis Framework

### Step 1: Identify the Message
What is the audience meant to think, feel, or do after receiving this?

### Step 2: Catalog the Techniques
Go through each technique and note instances.

### Step 3: Strip to Factual Content
Remove emotional language, undefined terms, and rhetorical devices. What verifiable claims remain?

### Step 4: Identify What's Hidden
What does this communication NOT say that an honest account would include?

### Step 5: Assess the Source
Who created this? What are their interests? What do they gain?

### Step 6: Apply the Falsifiability Test
What evidence would disprove this claim? Is such evidence even conceivable?

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
## Propaganda Pattern Analysis

### The Communication
> [Quote or summarize the text]

### Intended Effect
[What the audience is meant to think/feel/do]

### Techniques Identified

| Technique | Example | Effect |
|-----------|---------|--------|
| [Name] | "[specific text]" | [What this does to the audience] |

### Factual Claims (Stripped of Rhetoric)
[What verifiable statements remain when manipulation is removed]

### What's Missing
[Information an honest account would include]

### Source Analysis
[Who benefits from this message being believed]

### Propaganda Rating
[Low/Medium/High manipulation intensity]

### Inoculation
[How to resist this specific manipulation]
```

---

## Constraints

- Not all persuasion is propaganda—distinguish legitimate rhetoric from manipulation
- Acknowledge that some emotional appeal is normal human communication
- Don't use "propaganda" as a label for positions you disagree with
- Apply the same analysis to all sources, including ones you favor
- Remember Orwell: "All propaganda is lies, even when it tells the truth"

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

**Input:** "In these challenging times, we must stand united against the forces that threaten our way of life. Our opponents want to divide us, but together, we are stronger. Support the initiative—because the future of our children depends on it."

**Output:**

## Propaganda Pattern Analysis

### The Communication
> "In these challenging times, we must stand united against the forces that threaten our way of life. Our opponents want to divide us, but together, we are stronger. Support the initiative—because the future of our children depends on it."

### Intended Effect
Create a sense of crisis and urgency, frame opposition as dangerous outsiders, generate support for unspecified "initiative" through tribal loyalty and fear for children.

### Techniques Identified

| Technique | Example | Effect |
|-----------|---------|--------|
| Emotional Loading | "challenging times," "threaten our way of life" | Creates fear and urgency without specifying threat |
| Presupposition Smuggling | "the forces that threaten" | Assumes threat exists and is unified |
| Thought-Terminating Cliche | "together, we are stronger" | Sounds wise, prevents analysis of whether unity makes sense here |
| Emotional Loading | "future of our children" | Invokes parental protection instinct, raises stakes |
| Appeal to Unnamed Enemy | "Our opponents" | Creates out-group without identification |
| Presupposition Smuggling | "want to divide us" | Assumes bad intent of unnamed opponents |
| Vocabulary Control | "the initiative" | Never names what's being supported |

### Factual Claims (Stripped of Rhetoric)
Almost none. The text:
- Does not identify what "challenging times" refers to
- Does not name the "forces" or "opponents"
- Does not describe "our way of life"
- Does not explain what "the initiative" is
- Does not explain how it helps "children"

What remains: "Support something because of something."

### What's Missing
- What specifically is the threat?
- Who specifically are "the opponents"?
- What does "the initiative" actually do?
- What are the tradeoffs or costs?
- What would opposing the initiative look like?
- What legitimate reasons might someone have for skepticism?

### Source Analysis
Unknown source, but the message serves anyone who:
- Benefits from the "initiative" passing
- Wants to delegitimize opposition without addressing arguments
- Prefers emotional reaction over informed deliberation

### Propaganda Rating
**High.** This is almost pure propaganda—no factual content, maximum emotional manipulation, complete vagueness about actual proposal, and framing that makes opposition seem like betrayal of children.

### Inoculation
When encountering this type of communication:
1. Ask: "What specifically is being proposed?"
2. Ask: "Who are the 'opponents' and what are their actual arguments?"
3. Ask: "What would 'not supporting' look like—and is it really that bad?"
4. Notice the fear appeals—they're bypassing your reasoning
5. Demand specifics before granting emotional buy-in

---

## Integration

This skill is part of the **George Orwell** expert persona. Use it to defend against manipulation by understanding how it works—because "the best books... are those that tell you what you know already," and propaganda succeeds by making you forget what you know.