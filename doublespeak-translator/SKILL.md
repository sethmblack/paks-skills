---
name: doublespeak-translator
description: Expose what language actually means by translating euphemism, jargon, and obfuscation into plain English.
license: MIT
metadata:
  version: 1.0.3860
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- doublespeak-translator
- writing
---

# Doublespeak Translator

Expose what language actually means by translating euphemism, jargon, and obfuscation into plain English.

---

## When to Use

- Reading political statements, press releases, or official communications
- Analyzing corporate announcements, HR language, or legal disclaimers
- Encountering bureaucratic or institutional language that feels evasive
- User asks "What does this really mean?" or "What are they hiding?"
- Detecting defensive language designed to obscure rather than communicate

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| text | Yes | The language to be analyzed and translated |
| context | No | Where this language appears (helps identify motives) |
| speaker | No | Who is communicating (helps identify interests) |

---

## Core Principle

George Orwell wrote: "Political language is designed to make lies sound truthful and murder respectable, and to give an appearance of solidity to pure wind."

Doublespeak serves specific functions:
- **To soften:** Making harsh realities more palatable
- **To obscure:** Hiding what's actually happening
- **To deflect:** Avoiding responsibility and accountability
- **To legitimize:** Making questionable actions seem proper

The translator's job: strip away the linguistic camouflage and reveal the reality beneath.

---

## Analysis Framework

### Step 1: Identify the Key Terms
Find the words and phrases doing the most work—especially:
- Euphemisms (softer substitutes for harsh realities)
- Abstractions (words detached from concrete meaning)
- Passive constructions (hiding the actor)
- Nominalizations (turning actions into things)
- Technical jargon (requiring specialized knowledge to decode)

### Step 2: Translate to Plain English
For each identified term, ask:
- What would a plain-speaking person call this?
- What concrete reality does this refer to?
- What is the Anglo-Saxon word for this Latinate abstraction?

### Step 3: Identify What's Being Hidden
Ask:
- What uncomfortable truth does this language avoid naming?
- What would happen if they said it plainly?
- Who would be embarrassed or held accountable?

### Step 4: Determine Who Benefits
Follow the principle of cui bono:
- Who gains from this being phrased this way?
- What interests are served by the obfuscation?
- What would the affected parties say instead?

---

## Common Doublespeak Patterns

| Doublespeak | Plain English | Function |
|-------------|---------------|----------|
| "Restructuring" | Layoffs | Softens job losses |
| "Collateral damage" | Civilian deaths | Sanitizes killing |
| "Enhanced interrogation" | Torture | Legitimizes brutality |
| "Right-sizing" | Firing people | Corporate euphemism |
| "Negative growth" | Decline/loss | Avoids admitting failure |
| "Challenging quarter" | We lost money | Deflects bad news |
| "Going forward" | (empty filler) | Sounds purposeful, means nothing |
| "At this point in time" | Now | Pretentious padding |
| "Mistakes were made" | We made mistakes | Avoids naming who |
| "Let go" | Fired | Implies it was voluntary |
| "Passed away" | Died | Softens death |
| "Pre-owned" | Used | Makes secondhand sound better |
| "Synergies" | Cuts (usually jobs) | Corporate jargon for elimination |
| "Sunset" (as verb) | Kill, end, cancel | Makes termination sound natural |

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
## Doublespeak Translation

### Original Text
> [Quote the original]

### Translation to Plain English
> [Rewrite in direct, honest language]

### Key Terms Decoded

| Doublespeak | Plain Meaning | Why the Euphemism? |
|-------------|---------------|-------------------|
| [Term 1] | [What it actually means] | [What it hides/softens] |
| [Term 2] | [What it actually means] | [What it hides/softens] |

### What's Being Hidden
[The uncomfortable reality this language is designed to obscure]

### Who Benefits
[Whose interests are served by this framing]

### The Orwell Verdict
[Brief assessment of the language's honesty]
```

---

## Constraints

- Do not assume bad faith where incompetence or habit explains the language
- Acknowledge when jargon serves legitimate technical precision
- Distinguish between acceptable shorthand and deliberate obfuscation
- Be specific—don't just say "this is vague," show exactly how
- Offer the plain alternative, not just criticism

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

**Input:** "We are implementing a strategic realignment that will result in a workforce optimization across several business units. Some positions will be eliminated as we right-size our organization to meet current market conditions. Affected team members will receive a comprehensive separation package and outplacement support."

**Output:**

## Doublespeak Translation

### Original Text
> "We are implementing a strategic realignment that will result in a workforce optimization across several business units. Some positions will be eliminated as we right-size our organization to meet current market conditions. Affected team members will receive a comprehensive separation package and outplacement support."

### Translation to Plain English
> "We are laying off employees in several departments. We're firing people to cut costs because business is bad. Those fired will get severance pay and help finding new jobs."

### Key Terms Decoded

| Doublespeak | Plain Meaning | Why the Euphemism? |
|-------------|---------------|-------------------|
| "Strategic realignment" | Layoffs | Sounds planned and smart rather than reactive |
| "Workforce optimization" | Cutting jobs | Implies efficiency rather than people losing income |
| "Positions eliminated" | People fired | Removes human element; fires "positions," not people |
| "Right-size" | Cut staff | Suggests current size was wrong; deflects blame |
| "Market conditions" | Business is struggling | Blames external forces, not management |
| "Affected team members" | People we're firing | Passive, impersonal; they're "affected" by forces, not by our decision |
| "Separation package" | Severance pay | Makes firing sound like a mutual parting |
| "Outplacement support" | Help finding another job | Sounds like a benefit rather than minimal aid |

### What's Being Hidden
- The number of jobs being cut
- Which departments and why
- Whether management failures contributed
- That real people will lose their livelihoods
- That this is a cost-cutting measure, not an "optimization"

### Who Benefits
Management benefits from language that:
- Makes them sound strategic rather than reactive
- Obscures their role in the decision
- Prevents specific accountability
- Makes harsh news easier to deliver
- Reduces likelihood of detailed follow-up questions

### The Orwell Verdict
This is textbook corporate doublespeak. Every term is chosen to soften, obscure, or deflect. The passive voice ("positions will be eliminated") hides who is eliminating them. The abstract nouns ("realignment," "optimization") float free of concrete human impact. The plain truth—"we're firing people to save money"—is buried under five layers of euphemism. If this were honest communication, it would say how many people, in which departments, and why.

---

## Integration

This skill is part of the **George Orwell** expert persona. Use it to cut through official language and find the truth beneath the words.