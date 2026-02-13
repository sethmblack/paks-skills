---
name: scaffolding-of-rhetoric
description: Analyze and improve any persuasive communication using Winston Churchill's six-element framework from his 1897 essay, which guided sixty years of legendary oratory.
license: MIT
metadata:
  version: 1.0.4909
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- escalation
- scaffolding-of-rhetoric
- writing
---

# Scaffolding of Rhetoric

Analyze and improve any persuasive communication using Winston Churchill's six-element framework from his 1897 essay, which guided sixty years of legendary oratory.

---

## When to Use

- Reviewing a speech or presentation before delivery
- Improving persuasive writing (proposals, pitches, arguments)
- User asks "Make this more persuasive" or "Improve this speech"
- Preparing for high-stakes communication
- Learning to write or speak more effectively
- Diagnosing why a message failed to land

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| content | Yes | The speech, text, or persuasive communication to analyze |
| audience | No | Who will receive this message |
| purpose | No | What the communication should achieve |
| format | No | Analysis only, or analysis with revision |

---

## Churchill's Six Elements of Oratory

From "The Scaffolding of Rhetoric" (1897), written at age 23, followed for sixty years:

### 1. Correctness of Diction

**The principle:** "Knowledge of a language is measured by the nice and exact appreciation of words. There is no more important element in the technique of rhetoric than the continual employment of the best possible word."

**What to evaluate:**
- Is each word the most precise choice?
- Are there weak words that could be stronger?
- Are there vague words that could be specific?
- Are there unnecessarily complex words where simple ones serve?

**Common failures:**
- Using "utilize" when "use" is better
- Using "endeavor" when "try" is better
- Using "facilitate" when "help" is better
- Using abstract nouns when concrete verbs are available

### 2. Rhythm

**The principle:** "The sentences of the orator when he appeals to his art become long, rolling and sonorous. The great influence of sound on the human brain is well known."

**What to evaluate:**
- Do sentences vary in length and cadence?
- Are important points delivered with rhythmic force?
- Is there a mix of long, building sentences and short, punching ones?
- Does the sound support the meaning?

**Common failures:**
- Monotonous sentence length
- Important points buried in flat prose
- Ending on weak syllables
- Awkward sound combinations

### 3. Accumulation of Argument

**The principle:** "The climax of oratory is reached by a rapid succession of waves of sound and vivid pictures."

**What to evaluate:**
- Do arguments build toward a climax?
- Is the strongest point positioned at the end?
- Does evidence accumulate rather than scatter?
- Is there a sense of building momentum?

**Common failures:**
- Strongest argument first, weakening thereafter
- Points in random order
- Repetition without escalation
- Anticlimax (powerful point followed by weak one)

### 4. Analogy

**The principle:** "An apt analogy favours the belief that the unknown is only an extension of the known."

**What to evaluate:**
- Are complex ideas made accessible through comparison?
- Do analogies illuminate rather than confuse?
- Are metaphors fresh or stale?
- Is there at least one memorable image?

**Common failures:**
- Abstract concepts without concrete comparison
- Overused cliches ("journey," "ecosystem," "synergy")
- Mixed metaphors
- Analogies that obscure rather than clarify

### 5. Extravagance of Language

**The principle:** "A tendency to wild extravagance of language... so wild that reason recoils" — used strategically to move audiences beyond rational resistance.

**What to evaluate:**
- Is there appropriate emotional amplitude?
- Are stakes conveyed with sufficient gravity?
- Is passion present where passion is needed?
- Is restraint maintained where restraint serves better?

**Common failures:**
- Corporate flatness on matters requiring emotion
- Hyperbole that undermines credibility
- Emotional appeals that feel manipulative
- All head, no heart (or vice versa)

### 6. Preference for Short Words

**The principle:** "All the speeches of great English rhetoricians... display a uniform preference for short, homely words of common usage."

**What to evaluate:**
- Are Anglo-Saxon words preferred over Latin/Greek derivatives?
- Can any multisyllabic word be replaced with a short one?
- Is the language accessible to the intended audience?
- Do key moments use punching monosyllables?

**Common failures:**
- "Utilize" instead of "use"
- "Implement" instead of "do"
- "Facilitate" instead of "help"
- "Endeavor" instead of "try"
- Jargon that excludes rather than includes

---

## Analysis Framework

For each element, score 1-5:
- **1:** Absent or severely deficient
- **2:** Present but weak
- **3:** Adequate
- **4:** Strong
- **5:** Excellent

**Threshold:** Total score below 18 indicates significant revision needed. Score of 24+ indicates strong persuasive craft.

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
## Rhetoric Analysis: [Title/Description]

### Overall Score: [X]/30

### Element Scores

| Element | Score | Assessment |
|---------|-------|------------|
| Correctness of Diction | X/5 | [Brief note] |
| Rhythm | X/5 | [Brief note] |
| Accumulation of Argument | X/5 | [Brief note] |
| Analogy | X/5 | [Brief note] |
| Extravagance | X/5 | [Brief note] |
| Short Words | X/5 | [Brief note] |

### Strengths
[What works well]

### Critical Issues
[What must be fixed]

### Specific Recommendations

#### Diction Fixes
[Specific word replacements]

#### Rhythm Improvements
[Sentence restructuring suggestions]

#### Structure Changes
[Reordering for better accumulation]

#### Analogy Additions
[Concrete images to add]

### Revised Version (if requested)
[Full revision implementing recommendations]
```

---

## Constraints

- Analyze against all six elements—do not skip any
- Provide specific, actionable recommendations, not vague suggestions
- If revising, implement recommendations fully—do not provide partial fixes
- Do not mistake length for quality—short, powerful beats long and weak
- Respect the original voice while improving craft
- Some content may intentionally violate a principle (e.g., technical documentation prioritizes precision over rhythm)—note these as appropriate rather than deficient

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

**Input:** "We need to leverage our core competencies to drive stakeholder value and facilitate synergistic outcomes in our go-to-market strategy. Our team is well-positioned to implement best-in-class solutions."

**Analysis Output:**

## Rhetoric Analysis: Corporate Strategy Statement

### Overall Score: 8/30

### Element Scores

| Element | Score | Assessment |
|---------|-------|------------|
| Correctness of Diction | 1/5 | Nearly every word could be better |
| Rhythm | 2/5 | Flat, no variation, no music |
| Accumulation of Argument | 1/5 | No building, no climax |
| Analogy | 1/5 | No images, no comparisons |
| Extravagance | 1/5 | No passion, no stakes |
| Short Words | 2/5 | Latinate jargon dominates |

### Strengths
- Contains multiple ideas that could be developed
- Positive tone (though generic)

### Critical Issues
1. **Jargon saturation:** "Leverage," "core competencies," "stakeholder value," "facilitate," "synergistic," "go-to-market," "best-in-class" — none of these mean anything concrete
2. **No imagery:** Not a single vivid picture
3. **No stakes:** Why should anyone care?
4. **No rhythm:** Every sentence plods at the same pace
5. **No specificity:** Could apply to any company, any industry, any time

### Specific Recommendations

#### Diction Fixes
- "leverage" → "use"
- "core competencies" → "what we do best"
- "facilitate" → "create"
- "synergistic outcomes" → "results that multiply"
- "go-to-market strategy" → "how we will sell"
- "well-positioned" → "ready"
- "implement" → "build"
- "best-in-class" → [delete entirely or give specific comparison]

#### Rhythm Improvements
- Vary sentence length
- End with strong, short words
- Create at least one building sequence

#### Structure Changes
- Begin with stakes: what happens if we fail? succeed?
- Build to a specific, memorable close

#### Analogy Additions
- What is the team like? (athletes, builders, explorers?)
- What does success look like concretely?

### Revised Version

We know what we do best. We build products that our customers cannot live without.

But building is not enough. We must sell. We must put these products into the hands of people who need them—faster than our competitors, better than we have before.

Here is how we will do it:

We will focus on three markets where our product already wins. We will go deep before we go wide. We will turn every satisfied customer into an advocate who brings us more.

We are ready. The question is not whether we can compete. The question is whether we will execute. The answer is yes.

Now—let's build.

---

### Score After Revision: 23/30
- Diction: 4/5 (concrete, active)
- Rhythm: 4/5 (varied, punchy close)
- Accumulation: 4/5 (builds to "Now—let's build")
- Analogy: 3/5 (improved but still room for imagery)
- Extravagance: 4/5 (appropriate stakes, not overwrought)
- Short Words: 4/5 (Anglo-Saxon dominates)

---

## Integration

This skill is part of the **Winston Churchill** expert persona. Use it when you need to analyze or improve any persuasive communication against the framework Churchill developed at 23 and practiced for sixty years. The orator who rallied Britain through its darkest hour first understood rhetoric as a craft with learnable elements.