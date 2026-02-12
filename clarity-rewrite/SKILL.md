---
name: clarity-rewrite
description: Transform complex, obscure, or muddled writing into clear, precise, accessible
  prose following Russell's methodology.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- clarity-rewrite
- transformation
- writing
---

# Clarity Rewrite

Transform complex, obscure, or muddled writing into clear, precise, accessible prose following Russell's methodology.

**Token Budget:** ~700 tokens (this prompt). Reserve tokens for rewrite output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Simplify in ways that distort the meaning
- Remove necessary nuance or caveats
- Make harmful content more persuasive through clarity

**If the original contains harmful content:** Note the issue; do not clarify harmful messaging.

---

## Origin

This skill embodies Bertrand Russell's legendary prose style. Russell said he formed "the habit of turning a sentence over and over in my mind, until I had a combination of brevity, clarity, and rhythm." W.V. Quine noted that readers were "beguiled by the wit and a sense of new-found clarity." This skill applies Russell's method of achieving elegance through simplicity.

---

## When to Use

- User asks "Make this clearer"
- User asks "Simplify this explanation"
- Confronting jargon-heavy or obscure writing
- Translating technical content for general audiences
- Improving the readability of one's own writing
- Making complex ideas accessible without dumbing them down

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **text** | Yes | The text to be clarified |
| **audience** | No | Target audience (default: intelligent general reader) |
| **constraints** | No | Any requirements to preserve (technical terms, length, etc.) |

---

## Workflow
### 1. Diagnose the Obscurity

Identify what makes the text unclear:

| Problem Type | Symptoms |
|--------------|----------|
| **Jargon** | Technical terms without explanation |
| **Abstraction** | No concrete examples |
| **Passive voice** | Hidden agents; unclear who does what |
| **Buried lead** | Main point not stated clearly or early |
| **Unnecessary complexity** | Long sentences, nested clauses |
| **Vagueness** | Imprecise words ("various," "somewhat," "factors") |
| **Nominalizations** | Verbs turned into nouns ("implementation" vs "implement") |

**Output:** List of specific obscurity problems identified

### 2. Extract the Core Message

Before rewriting, ensure you understand what is being said:
- What is the main claim or point?
- What are the supporting points?
- What is the logical structure?

**Russell's test:** Can you state this in one clear sentence? If not, is the original actually saying anything?

**Output:** Core message in one sentence (if possible)

### 3. Apply Clarity Principles

**Russell's principles:**

### Step 1: **Brevity** - Use fewer words; cut what doesn't add meaning



### Step 2: **Clarity** - Prefer common words to rare ones; prefer concrete to abstract



### Step 3: **Rhythm** - Sentences should flow; vary length but default to shorter



**Specific techniques:**
- Replace jargon with plain language (or define it)
- Convert abstract statements to concrete examples
- Change passive to active voice
- Front-load the main point
- Break long sentences into shorter ones
- Turn nominalizations back into verbs

**Output:** Rewritten text

### 4. Verify Meaning Preservation

Compare the rewrite to the original:
- Have you changed the meaning?
- Have you lost important nuance?
- Have you oversimplified?

If meaning has shifted, revise the rewrite.

**Output:** Confirmation that meaning is preserved (or note of necessary trade-offs)

### 5. Polish for Rhythm

Russell sought "a combination of brevity, clarity, and rhythm." Read the rewrite aloud:
- Does it flow?
- Are there awkward constructions?
- Could any word be cut without loss?

**Output:** Final polished version

---

## Outputs

### Clarity Rewrite Report

```markdown
## Clarity Rewrite

### Original Text
[Original text provided]

### Diagnosis
**Problems identified:**
- [Problem 1]
- [Problem 2]
- [Problem 3]

### Core Message
[One-sentence summary of what the text is saying]

### Rewritten Text
[Clarified version]

### Changes Made
| Original | Revised | Why |
|----------|---------|-----|
| [phrase] | [phrase] | [reason] |

### Preservation Check
[Confirmation that meaning is preserved, or note of trade-offs]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Text is already clear | Note that; suggest only minor improvements if any |
| Text is incoherent (not just unclear) | Flag that the original may not make sense; clarify what can be clarified |
| Technical terms must be preserved | Keep terms but add brief explanations |
| Length constraints conflict with clarity | Note the trade-off; prioritize as user specifies |
| Original meaning is ambiguous | Note ambiguity; offer alternative interpretations |

---

## Clarity Checklist

Before submitting rewrite:
- [ ] Main point is stated early and clearly
- [ ] All jargon is defined or replaced
- [ ] Abstract claims have concrete examples
- [ ] Active voice used where possible
- [ ] No unnecessary words
- [ ] Sentences are appropriately short
- [ ] Meaning from original is preserved

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "The implementation of the new paradigm necessitates the facilitation of synergistic collaboration between various stakeholders in order to optimize the leveraging of core competencies."

**Output:**

## Clarity Rewrite

### Original Text
"The implementation of the new paradigm necessitates the facilitation of synergistic collaboration between various stakeholders in order to optimize the leveraging of core competencies."

### Diagnosis
**Problems identified:**
- Heavy nominalization ("implementation," "facilitation," "leveraging")
- Business jargon ("paradigm," "synergistic," "stakeholders," "core competencies")
- Vague terms ("various")
- Passive/impersonal construction
- No concrete content

### Core Message
"To make the new approach work, the relevant people need to cooperate and use their skills effectively."

(Note: Even this is vague because the original is vague. What paradigm? Which stakeholders? What competencies?)

### Rewritten Text
"To make this new approach work, the teams involved must cooperate and use their strengths effectively."

Or, if we add specificity:
"For the new customer service model to succeed, sales and support teams must work together and apply their expertise."

### Changes Made
| Original | Revised | Why |
|----------|---------|-----|
| "implementation of the new paradigm" | "to make the new approach work" | Nominalization → verb; jargon → plain language |
| "necessitates the facilitation of" | "must" | Pompous circumlocution → direct verb |
| "synergistic collaboration" | "work together" | Jargon → plain language |
| "various stakeholders" | "the teams involved" | Vague → slightly less vague (ideally specify which teams) |
| "optimize the leveraging of core competencies" | "apply their expertise" | Three jargon terms → plain language |

### Preservation Check
The rewrite preserves the meaning—which is admittedly thin. The original says little of substance; the rewrite says the same little clearly. True clarity would require knowing what paradigm, which stakeholders, and what competencies. Clarity cannot add meaning that isn't there.

---

## Integration

This skill originated from the **bertrand-russell** expert. It applies Russell's method of achieving elegance through simplicity—the discipline of turning sentences over until they achieve brevity, clarity, and rhythm.