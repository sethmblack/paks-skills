---
name: impression-tracing
description: Test any abstract idea, concept, or term for legitimate content by tracing it back to the sense impressions from which it derives. Identifies empty concepts that are mere words without experiential...
license: MIT
metadata:
  version: 1.0.1170
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- impression-tracing
- writing
---

# Impression Tracing

Test any abstract idea, concept, or term for legitimate content by tracing it back to the sense impressions from which it derives. Identifies empty concepts that are mere words without experiential referent.

---

## When to Use

- User asks "What does this term actually mean?"
- Someone uses abstract jargon without clear definition
- A concept seems meaningful but resists precise articulation
- Evaluating buzzwords, metaphysical claims, or technical terminology
- Request to "trace this idea to its source"
- Any situation where you suspect a word has no real content

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| concept | Yes | The idea, term, or concept to trace |
| context | No | The domain or usage context where the concept appears |
| initial_definition | No | The user's attempted definition (if any) |

---

## The Tracing Framework

### Phase 1: Identify the Concept

Clearly isolate the idea under examination.

**Questions to ask:**
- "What exactly is the term or concept we're examining?"
- "In what context is this term being used?"
- "What claims are being made using this concept?"

**Goal:** A clear target for empirical investigation.

### Phase 2: Apply the Copy Principle

Attempt to trace the concept back to impressions.

**The Humean Test:**
> "From what impression is this idea derived?"

**Questions to ask:**
- "What sensory experience gives rise to this idea?"
- "Can you recall a specific impression—sight, sound, touch, emotion—that corresponds to this concept?"
- "Is this a simple idea (directly copied from impression) or complex (combination of simple ideas)?"

**If complex:**
- Decompose into component simple ideas
- Trace each component to its impression
- Check if the combination is coherent

### Phase 3: Evaluate Legitimacy

Based on tracing results, assess the concept's status.

**Possible outcomes:**
1. **Fully Grounded:** Clear impression(s) found; concept has legitimate content
2. **Partially Grounded:** Some elements trace to experience, others don't
3. **Ungrounded:** No impression can be found; concept may be empty

**Questions to ask:**
- "If we removed all impressions, would anything remain?"
- "Is this word doing genuine conceptual work or just sounding important?"
- "Could we replace this term with more concrete language?"

### Phase 4: Provide Analysis

Deliver clear verdict with explanation.

**For grounded concepts:**
- Identify the specific impressions that ground the concept
- Note any complexity or abstraction involved
- Confirm legitimate usage

**For ungrounded concepts:**
- Explain why no impression can be found
- Suggest either clarification or abandonment
- Offer more empirically grounded alternatives if possible

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
## Impression Trace: [The Concept]

### Concept Under Examination
**Term:** [State the term precisely]
**Context:** [Where/how it's being used]

### Tracing Attempt

**Simple or Complex:** [Simple (direct copy) / Complex (combination)]

**Component Analysis:** (if complex)
- Component 1: [traces to: impression X / no impression found]
- Component 2: [traces to: impression Y / no impression found]
- ...

**Impressions Identified:**
- [List specific sensory experiences, emotions, or reflections that ground the concept]
- OR: "No clear impression can be identified"

### Verdict

**Status:** GROUNDED / PARTIALLY GROUNDED / UNGROUNDED

**Analysis:**
[Explanation of why the concept does or does not have legitimate empirical content]

### Recommendations

[If grounded: confirm usage, note any caveats]
[If ungrounded: suggest clarification, alternative terms, or abandonment]

*"From what impression is this idea derived?" — David Hume*
```

---

## Common Applications

| Domain | Example Concepts to Trace |
|--------|--------------------------|
| Philosophy | Substance, essence, necessary connection, the soul |
| Business | Synergy, disruption, paradigm shift, alignment |
| Technology | Intelligence (in AI), consciousness, understanding |
| Politics | Freedom, rights, justice (when used abstractly) |
| Metaphysics | Being, nothingness, the absolute |

---

## Constraints

- Apply the test fairly—some abstract concepts do have legitimate content
- Remember Hume's "missing shade of blue"—edge cases exist but don't undermine the general principle
- Complex ideas can be legitimate if their components trace to impressions
- Don't be dogmatic—acknowledge when tracing is difficult but not impossible
- Some concepts may be legitimate despite difficulty in articulating their impressions

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

**Input:** "What does 'synergy' actually mean in business contexts?"

**Output:**



**Why this works:**

This example demonstrates the key principles of the skill in action. The approach is effective because:
- It follows the systematic workflow outlined above
- It shows concrete application of the framework
- It produces actionable, specific outputs rather than vague generalizations
- The analysis is grounded in observable details
- The recommendations are prioritized and implementable

**Alternative applications:**

This same approach can be applied to:
- Different contexts within the same domain
- Related but distinct problem types
- Scaled up or down depending on scope
- Combined with complementary analytical frameworks


## Impression Trace: "Synergy"

### Concept Under Examination
**Term:** Synergy
**Context:** Business and organizational discourse, typically meaning "the whole is greater than the sum of its parts"

### Tracing Attempt

**Simple or Complex:** Complex

**Component Analysis:**
- "Whole": Traces to perception of complete objects/systems—GROUNDED
- "Greater": Traces to comparative judgments—GROUNDED
- "Sum": Traces to mathematical operations—GROUNDED
- "Parts": Traces to perception of components—GROUNDED
- "Combined effect exceeding individual contributions": This is the core claim

**Impressions Identified:**
- The underlying claim can trace to specific observations: two people accomplishing more together than their separate efforts would sum to
- We have impressions of collaborative work, unexpected efficiencies, emergent capabilities
- The concept at its core describes an observable phenomenon

### Verdict

**Status:** PARTIALLY GROUNDED

**Analysis:**
"Synergy" can be traced to legitimate impressions of cooperative activity producing amplified results. However, the term is often used:
1. Without specifying the mechanism of amplification
2. As an empty promise without empirical verification
3. As a substitute for concrete descriptions of collaboration

When grounded in specific observations ("combining these two teams reduced overhead by 20%"), the concept has content. When used abstractly ("we'll achieve synergies"), it may be an empty word.

### Recommendations

- When using "synergy," specify the mechanism: How exactly does combination exceed summation?
- Prefer concrete descriptions: "Shared infrastructure reduces costs" rather than "synergy"
- Ask for the impression: "What specifically do you observe that you're calling synergy?"

*"From what impression is this idea derived?" — David Hume*

---

## Integration

This skill is part of the **David Hume** expert persona. Use it to test any abstract concept for empirical grounding. It pairs well with:
- **causation-examination** when the concept involves causal claims
- **is-ought-analysis** when the concept is used in moral arguments
- **mitigated-skepticism** for calibrating how harshly to judge unclear concepts

---