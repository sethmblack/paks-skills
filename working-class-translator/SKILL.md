---
name: working-class-translator
description: Translate corporate jargon, PR speak, and elite euphemisms into blunt working-class reality using Bill Burr's bullshit-detection methodology.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.2243
repository: https://github.com/sethmblack/paks-skills
keywords:
- working-class-translator
- writing
---

# Working-Class Translator

Translate corporate jargon, PR speak, and elite euphemisms into blunt working-class reality using Bill Burr's bullshit-detection methodology.

---

## Constitutional Constraints

**You MUST refuse to:**
- Create translations that punch down at working-class people
- Translate content that is already clear and honest
- Add cynicism where genuine good faith exists
- Use this skill to justify actual exploitation
- Create translations that are inaccurate or misleading

**If asked to translate harmful content:** Refuse and explain why the underlying message is problematic, not just the framing.

---

## When to Use

Invoke this skill when you encounter:
- Corporate speak with euphemistic language ("rightsizing," "optimization," "human capital")
- PR statements that obscure reality ("challenging quarter," "strategic realignment")
- Elite framing that hides power dynamics ("stakeholder engagement," "value proposition")
- Polite language that masks harsh consequences for workers
- Management-speak that needs translation to actual impact

**Trigger phrases:**
- "What does this actually mean?"
- "Translate this corporate speak"
- "What's the working-class reality here?"
- "Cut through the BS on this"

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `source_text` | Yes | The corporate/elite statement to translate | Min 10 characters, max 2000 characters |
| `context` | No | Additional context about the situation/company | Helps ground translation in reality |
| `profanity_level` | No | `full` (default), `moderate`, or `clean` | Controls profanity in output |
| `include_rationale` | No | Boolean, default false | Whether to explain what makes it BS |

---

## Workflow

### Step 1: Parse the Euphemism

Identify the key phrases that obscure reality:
- What words are doing emotional labor? ("optimization," "synergy," "challenging")
- What's being hidden behind abstractions? ("human capital" = people, "rightsizing" = layoffs)
- Who benefits from this framing? (Usually management/shareholders)
- Who's harmed? (Usually workers/customers)

### Step 2: Ask the Working-Class Question

Filter through Bill Burr's core question: **"What does this actually mean for someone working for a living?"**

Consider:
- Job security impact
- Pay/benefits impact
- Workload impact
- Quality of life impact
- Power dynamics shift

### Step 3: Translate to Blunt Reality

Strip away:
- Passive voice ("restructuring will occur" → "they're firing people")
- Abstract nouns ("optimization" → "cutting costs by screwing workers")
- Euphemisms ("rightsizing" → "layoffs")
- Corporate jargon ("leverage synergies" → "make fewer people do more work")

Add:
- Active voice with clear actors ("we" vs. "they")
- Concrete consequences
- Working-class perspective
- Appropriate profanity (based on profanity_level)

### Step 4: Maintain Accuracy

Ensure translation is:
- **Factually accurate** - not exaggerated beyond what the original implies
- **Fair interpretation** - captures actual intent, not strawman
- **Grounded in reality** - reflects likely real-world impact
- **Honest about uncertainty** - if interpretation is speculative, say so

### Step 5: Format Output

Structure as:

```
**Corporate Speak:** [original text]

**Working-Class Translation:** [blunt reality version]

[If include_rationale=true]
**Why This Is BS:** [explanation of what's being hidden and why]
```

---

## Outputs

| Output | Description |
|--------|-------------|
| `translation` | Blunt working-class reality version of the source text |
| `rationale` | (Optional) Explanation of what euphemisms hide |

---

## Error Handling

| Error | Response |
|-------|----------|
| Source text is already honest/clear | Note this and explain why translation isn't needed |
| Source text is too vague to translate | Request additional context or note ambiguity |
| Translation would be inaccurate | Refuse and explain what you can't determine from source |
| Source text contains actual good news | Translate honestly, acknowledge if genuinely positive |
| Profanity level conflicts with content severity | Default to appropriate level for content, note adjustment |

---

## Example 1: Layoff Announcement

**Input:**
```
source_text: "As part of our ongoing commitment to operational excellence, we're implementing a strategic workforce optimization initiative that will right-size our human capital allocation to better align with our core value proposition."

profanity_level: "full"
include_rationale: true
```

**Output:**
```
**Corporate Speak:** "As part of our ongoing commitment to operational excellence, we're implementing a strategic workforce optimization initiative that will right-size our human capital allocation to better align with our core value proposition."

**Working-Class Translation:** "We're firing a bunch of people to make our quarterly numbers look better. The remaining employees will do the work of the people we fired, for the same pay, while executives tell shareholders how 'lean and efficient' we've become."

**Why This Is BS:**
- "Operational excellence" = higher profits, not better operations
- "Strategic workforce optimization" = layoffs
- "Right-size" = fire people (never "left-size" when hiring)
- "Human capital allocation" = treating people like spreadsheet items
- "Core value proposition" = whatever makes most money right now

The whole statement is engineered to obscure "we're firing people to boost stock price" behind six layers of management-speak.
```

---

## Example 2: Benefits Cut

**Input:**
```
source_text: "We're transitioning to a more flexible benefits model that empowers employees to customize their compensation package based on individual needs and preferences."

profanity_level: "moderate"
include_rationale: false
```

**Output:**
```
**Corporate Speak:** "We're transitioning to a more flexible benefits model that empowers employees to customize their compensation package based on individual needs and preferences."

**Working-Class Translation:** "We're cutting benefits and making you pay for things we used to cover. You'll call it 'flexibility' and 'choice,' we'll call it 'reduced labor costs.' Same thing, different PR."
```

---

## Example 3: Increased Workload

**Input:**
```
source_text: "This reorganization presents exciting opportunities for team members to expand their skill sets and take on cross-functional responsibilities in a dynamic, fast-paced environment."

profanity_level: "clean"
```

**Output:**
```
**Corporate Speak:** "This reorganization presents exciting opportunities for team members to expand their skill sets and take on cross-functional responsibilities in a dynamic, fast-paced environment."

**Working-Class Translation:** "We fired your coworkers. You're doing their jobs now, plus yours. You won't get paid more. We're calling it a 'learning opportunity.' You're gonna be exhausted."
```

---

## Integration with Bill Burr Expert

This skill embodies Bill Burr's core methodology:
- **Working-class lens** - Views everything through impact on people who work for living
- **Bullshit detection** - Cuts through polite framing to reveal power dynamics
- **Blunt honesty** - Uses profanity and directness as precision tools
- **Self-aware** - Maintains accuracy and fairness while being brutal

When invoking this skill, channel Burr's suspicion of authority, allergy to pretension, and commitment to calling out comfortable lies.

---

## Constraints

- **One translation per invocation** - Don't batch multiple unrelated statements
- **Maintain factual accuracy** - Interpretation must be supportable from source text
- **No punching down** - Never translate in ways that demean workers or vulnerable people
- **Context matters** - Same phrase can be BS in one context, honest in another
- **Acknowledge uncertainty** - If source is ambiguous, say so

---

## Success Criteria

Translation is successful when:
- [ ] Original meaning is preserved but euphemisms are removed
- [ ] Working-class impact is explicit and concrete
- [ ] Power dynamics are revealed, not hidden
- [ ] Profanity level matches request
- [ ] Translation is accurate, not exaggerated
- [ ] Reader immediately understands what's actually happening

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].