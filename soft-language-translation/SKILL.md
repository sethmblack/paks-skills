---
name: soft-language-translation
description: A systematic methodology for converting sanitized, bureaucratic, or deliberately vague language into direct, honest speech. This skill renders the obscure transparent by replacing comfort-language ...
license: MIT
metadata:
  version: 1.0.1932
  author: sethmblack
keywords:
- soft-language-translation
- writing
---

# Soft Language Translation

A systematic methodology for converting sanitized, bureaucratic, or deliberately vague language into direct, honest speech. This skill renders the obscure transparent by replacing comfort-language with precision.

## When to Use
- Reviewing legal documents, terms of service, or contracts
- Analyzing political statements or corporate communications
- Cutting through HR-speak, management jargon, or institutional language
- Writing clearer versions of obfuscated content
- Helping others understand what's actually being said to them
- Creating before/after comparisons that reveal rhetorical manipulation
- Training yourself or others to recognize language patterns that obscure meaning



## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| input_data | Yes | The primary data or content to analyze |
| context | No | Additional background or constraints (default: none) |
| output_format | No | Preferred format for results (default: structured markdown) |

## Workflow
### Step 1: Read for Discomfort Avoidance

Scan the text asking: "What might be uncomfortable to say directly here?"

Soft language appears when someone wants to communicate information while avoiding:
- Accountability ("Errors occurred" vs. "We made errors")
- Negative emotional response ("We're sunsetting the product" vs. "We're killing it")
- Legal exposure ("The product may not perform as expected" vs. "It might fail")
- Conflict ("We have concerns" vs. "We object")
- Clarity of bad news ("Your position has been eliminated" vs. "You're fired")

### Step 2: Identify the Translation Targets

Mark specific phrases that exhibit:

**Abstraction:** Concepts instead of specifics
- "Workforce adjustment" = ?
- "Operational challenges" = ?
- "Going forward" = ?

**Passivization:** Removing the actor
- "It was decided" = ?
- "The policy was implemented" = ?
- "Steps are being taken" = ?

**Nominalization:** Verbs turned into nouns
- "We made a determination" = We determined
- "We are in discussions" = We are discussing
- "Implementation will occur" = We will implement

**Hedging:** Softening certainty
- "It would appear that" = It seems / It is
- "There may be some concern" = People are concerned
- "Not inconsistent with" = Consistent with

**Jargon:** Insider language that excludes
- "Synergize" = Work together
- "Leverage" = Use
- "Actionable" = Useful

### Step 3: Apply the Translation Rules

For each target phrase, apply these conversion principles:

| Soft Version | Translation Principle | Hard Version |
|--------------|----------------------|--------------|
| Abstract noun | → Concrete noun | What specifically? |
| Passive voice | → Active voice | Who did this? |
| Nominalization | → Original verb | What action? |
| Hedge | → Direct statement | Say it straight |
| Euphemism | → Plain term | What's it called normally? |
| Jargon | → Common word | How would you explain this to a stranger? |

### Step 4: Preserve Meaning, Restore Clarity

The goal isn't to change what's being said, but to say it plainly. Your translation should:
- Convey the same information
- Use fewer words where possible
- Name actors and actions
- Restore emotional/practical reality
- Be understandable to anyone

### Step 5: Present Side-by-Side

Show the original and translation together. The contrast itself is the insight.

## Examples of Application

### Example 1: Corporate Announcement

**ORIGINAL:**
"In alignment with our commitment to operational excellence and sustainable growth, we are implementing a strategic workforce optimization initiative that will impact approximately 2,300 positions across multiple divisions. Affected team members will be provided with comprehensive transition support services."

**TRANSLATION:**
"We are firing 2,300 people. We will offer some help finding new jobs."

**WHAT WAS HIDDEN:**
- Who decided (passive voice throughout)
- That people are losing their jobs ("positions" being "impacted")
- The scale relative to total workforce
- What "comprehensive transition support" actually includes

---

### Example 2: Terms of Service

**ORIGINAL:**
"We reserve the right to modify, suspend, or discontinue any aspect of the Service at any time, with or without notice, and without liability to you or any third party."

**TRANSLATION:**
"We can change or stop the service whenever we want. We don't have to tell you first. You can't sue us about it."

**WHAT WAS HIDDEN:**
- Nothing, technically - but the legal phrasing makes the power imbalance feel normal and non-negotiable

---

### Example 3: Political Statement

**ORIGINAL:**
"While we remain committed to the principles underlying this initiative, given the current fiscal environment and stakeholder feedback, we are reassessing the implementation timeline and scope of the proposed measures."

**TRANSLATION:**
"We're not doing this anymore. People complained and we don't have the money."

**WHAT WAS HIDDEN:**
- That the initiative is effectively dead
- That opposition succeeded
- Whose "feedback" mattered
- When or whether anything will happen

---

### Example 4: Medical/Professional

**ORIGINAL:**
"The procedure carries a small but non-negligible risk of adverse outcomes, which may include but are not limited to temporary discomfort, prolonged recovery, or in rare cases, suboptimal results."

**TRANSLATION:**
"This might hurt. It might take longer to heal than expected. Sometimes it doesn't work well."

**WHAT WAS HIDDEN:**
- Nothing directly hidden, but the clinical language creates emotional distance from risk

## Key Principles

1. **Soft language is a choice.** Every phrase that obscures was selected over one that clarifies. Ask why.

2. **Restoration, not distortion.** Translation should reveal what was said, not change it. Accuracy matters.

3. **Actor and action.** Every sentence should answer: Who did what? If the original hides this, the translation should expose it.

4. **Syllable reduction often helps.** Shorter words are usually more direct. "Use" not "utilize." "End" not "terminate." "Problem" not "challenge."

5. **The test is the stranger.** Would someone with no context understand the translation? That's the clarity standard.

6. **Some softness is kind.** Not all indirect language is manipulation. Sometimes tact is appropriate. Distinguish between euphemism-as-manipulation and euphemism-as-kindness.

## Output Format

When translating soft language, structure your output as:

```
ORIGINAL: [The soft/obfuscated text]

TRANSLATION: [Direct, plain-language version]

KEY CONVERSIONS:
- [Soft term 1] → [Direct term 1]
- [Soft term 2] → [Direct term 2]
- [etc.]

WHAT THE SOFTNESS CONCEALED: [What becomes visible in the direct version]
```

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

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Practice Prompts

1. Translate a corporate earnings call paragraph into plain language.
2. Take a privacy policy section and state what it actually means for users.
3. Convert a political non-answer into what the speaker is actually communicating.
4. Translate a rejection letter (job, school, etc.) into its real content.
5. Find a public apology and translate it into what's being acknowledged vs. avoided.

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].