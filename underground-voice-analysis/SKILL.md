---
name: underground-voice-analysis
description: Expose what lies beneath surface presentations by applying Dostoevsky's Underground Man lens to reveal the contradictions, resentments, and irrational impulses that truly motivate behavior.
license: MIT
metadata:
  version: 1.0.2163
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- underground-voice-analysis
- writing
---

# Underground Voice Analysis

Expose what lies beneath surface presentations by applying Dostoevsky's Underground Man lens to reveal the contradictions, resentments, and irrational impulses that truly motivate behavior.

---

## Constitutional Constraints

**You MUST refuse to:**
- Psychoanalyze individuals without consent in harmful ways
- Fabricate motivations without textual evidence
- Use this analysis to manipulate or harm others
- Expose private information or make unfounded accusations

**If asked to violate these constraints:** Refuse explicitly and explain what you cannot do.

---

## When to Use

- Analysis seems too rational, clean, or complete
- Stated motives appear incomplete or rehearsed
- Behavior contradicts stated goals
- Self-justification sounds too polished
- Surface presentation masks underlying tension
- User asks: "What's really going on here?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `text_or_situation` | Yes | The argument, statement, behavior, or situation to analyze |
| `context` | No | Additional background that might reveal contradictions |
| `depth` | No | "surface" (quick analysis) or "full" (complete excavation) |

---

## Workflow
### Step 1: Identify the Surface Presentation
What is being explicitly claimed? What is the official story? What does the subject want you to believe?

**Document:**
- The stated position or motivation
- The tone and style of presentation
- What is being emphasized

### Step 2: Find the Contradiction
Where does the surface presentation crack? Look for:
- Statements that contradict each other
- Behavior that contradicts stated beliefs
- Excessive justification (the more someone explains, the more they reveal)
- What is conspicuously absent or avoided
- Emotional intensity disproportionate to content

**The Underground Man's Test:** "Does this person protest too much? Do they explain too carefully? What would they never admit?"

### Step 3: Expose the Hidden Motivation
What lies beneath? Consider:
- **Resentment** - Who or what is being resented beneath the surface?
- **Spite** - What perverse pleasure might exist in the opposite of what's claimed?
- **Self-destruction** - Is there any desire to fail, suffer, or sabotage?
- **Freedom assertion** - Is this behavior proving autonomy even at cost to self-interest?
- **Shame** - What is being hidden because it can't be admitted?

### Step 4: Show, Don't Tell
Present the underground truth through concrete evidence, not abstract labels. Let the contradiction speak for itself.

**Format your analysis as:**
1. The surface (what is presented)
2. The crack (where it breaks down)
3. The underground (what lies beneath)
4. The evidence (how we see it)

---

## Output Format

```markdown
## Surface Presentation
[What is being claimed or shown]

## The Crack
[Where the contradiction appears - specific evidence]

## Underground Truth
[What lies beneath - the hidden motivation]

## Evidence
[Concrete details that reveal the underground]

## Implication
[What this means for understanding the subject]
```

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

**Input:** "The CEO's memo announcing layoffs: 'This was an incredibly difficult decision. We care deeply about every team member, and this action, while painful, positions us for long-term success. We remain committed to our people-first culture.'"

**Underground Voice Analysis:**

## Surface Presentation
The CEO presents as a reluctant, caring leader forced by circumstances to make painful choices. The emphasis on difficulty and pain positions the decision-maker as suffering alongside those affected.

## The Crack
"We remain committed to our people-first culture" - spoken in the same breath as eliminating people. The phrase "positions us for long-term success" reveals the actual priority: the company's survival, not its people. "Incredibly difficult decision" - but the decision was made nonetheless, and quite efficiently.

## Underground Truth
The CEO experiences not just regret but a form of relief and even power. There is satisfaction in surviving the decision, in being the one who decides who stays and who goes. The elaborate expressions of pain serve two functions: they protect the CEO's self-image as a good person, and they pre-empt criticism by claiming suffering equivalent to those actually losing their jobs. The "people-first culture" invocation is pure spite - asserting the very thing being violated.

## Evidence
- The memo was written before the decision was announced, meaning the "difficulty" was already processed and resolved
- "Positions us" reveals identification with the surviving entity, not with those being cut
- The passive construction "this action" distances the CEO from agency in the decision

## Implication
The memo is a performance of suffering that protects the performer from having to genuinely reckon with the power being exercised. The Underground Man would recognize this immediately: the CEO cannot admit the dark satisfaction that accompanies such power, so elaborate justifications must fill the gap.

---

## Constraints

- Always ground analysis in textual or behavioral evidence
- Acknowledge when analysis is speculative
- Present underground truths without moralizing
- Maintain the Dostoevskian principle: even the exposed deserve compassion
- Do not flatten complexity - the underground truth and the surface can both be partially true

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient text/context | Request more material or note limitations |
| No apparent contradiction | State that the surface appears consistent; not everything has an underground |
| Multiple possible underground truths | Present alternatives; truth is often plural |
| Analysis would be harmful | Refuse and explain ethical boundary |

---

## Integration

This skill derives from Dostoevsky's characterization of the Underground Man in *Notes from Underground* (1864). The Underground Man exists beneath social surfaces, paralyzed by excessive consciousness, finding pleasure in degradation, acting against self-interest to prove freedom.

**Source Expert:** fyodor-dostoevsky

**Complementary Skills:**
- `polyphonic-reframing` - After exposing underground truth, give it voice alongside surface
- `grand-inquisitor-diagnosis` - When underground truth involves freedom-security tradeoff