---
name: clarity-distinctness-evaluation
description: Evaluate whether an idea, concept, or argument is sufficiently clear (vivid and present to the mind) and distinct (precisely separated from other concepts) to be trusted as a foundation for further...
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3600
repository: https://github.com/sethmblack/paks-skills
keywords:
- clarity-distinctness-evaluation
- writing
---

# Clarity-Distinctness Evaluation

Evaluate whether an idea, concept, or argument is sufficiently clear (vivid and present to the mind) and distinct (precisely separated from other concepts) to be trusted as a foundation for further reasoning.

**Token Budget:** ~600 tokens. Reserve tokens for evaluation output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Declare ideas clear/distinct that genuinely remain confused
- Use this evaluation to dismiss ideas that are merely unfamiliar
- Confuse clarity with simplicity (complex ideas can be clear)
- Confuse distinctness with isolation (related ideas can be distinct)

**Authenticity Requirement:** This skill implements Descartes' epistemological criterion from *Meditations*. An idea is clear when vividly present to an attentive mind; distinct when precisely separated from all others so it contains nothing but what is clear.

---

## When to Use

- User asks "Is this idea clear enough to build on?"
- Need to evaluate "Do I really understand this?"
- Before using a concept as a premise in reasoning
- When communication seems to fail ("We're talking past each other")
- Diagnosing why an argument feels weak
- Testing whether apparent understanding is genuine

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| idea_or_argument | Yes | The concept, claim, or reasoning to evaluate |
| intended_use | No | What the understanding will be used for (decision, teaching, building) |
| context | No | Domain or situation affecting evaluation |

---

## Workflow

### Step 1: State the Idea
Articulate the idea under evaluation as precisely as possible. If it cannot be stated precisely, that itself indicates lack of clarity.

### Step 2: Evaluate Clarity
Ask: "Is this idea vivid and present to my attentive mind?"

**Tests for Clarity:**
- Can I state it in different words without losing meaning?
- Can I give concrete examples?
- Can I identify what would make it false?
- Does it become clearer or muddier under examination?

**Clarity Levels:**
| Level | Description |
|-------|-------------|
| Clear | Vivid, present, fully grasped when attending to it |
| Partially clear | Some aspects grasped, others remain vague |
| Obscure | Dim, confused, grasped only in outline |

### Step 3: Evaluate Distinctness
Ask: "Is this idea precisely separated from all others?"

**Tests for Distinctness:**
- Can I explain how this differs from related concepts?
- Am I conflating multiple ideas under one term?
- Are the boundaries of the concept clear?
- Could someone confuse this with something else?

**Distinctness Levels:**
| Level | Description |
|-------|-------------|
| Distinct | Precisely separated, no confusion with other ideas |
| Partially distinct | Mostly separated but some overlap remains |
| Confused | Blended with other concepts, boundaries unclear |

### Step 4: Identify Sources of Obscurity/Confusion
For any lack of clarity or distinctness, diagnose the source:

**Common Sources of Obscurity:**
- Abstract without concrete grounding
- Unfamiliar (not yet learned, not mere complexity)
- Ambiguous language
- Missing definitions
- Incomplete understanding

**Common Sources of Confusion:**
- Equivocation (same word, different meanings)
- Conflation (merging distinct concepts)
- Vague boundaries
- Family resemblance without core definition

### Step 5: Assess Fitness for Purpose
Given the intended use, is the current level of clarity/distinctness sufficient?

| Purpose | Required Level |
|---------|---------------|
| Casual discussion | Partial clarity acceptable |
| Important decision | Clear and at least partially distinct |
| Foundational premise | Clear AND distinct required |
| Teaching others | Clear AND distinct required |
| Precise communication | Clear AND distinct required |

### Step 6: Recommend Improvements
If insufficient, specify what would achieve clarity/distinctness.

---

## Output Format

```markdown
## Clarity-Distinctness Evaluation: [Idea/Concept]

### Idea Under Evaluation
**Stated as:** "[The idea in user's words]"
**Restated precisely:** "[Clarified formulation]"

### Clarity Assessment

**Can be stated in different words:** [Yes/No - attempt]
**Concrete examples available:** [Yes/No - provide if yes]
**Falsification conditions clear:** [Yes/No - what would make it false]
**Effect of examination:** [Clearer / No change / Muddier]

**Clarity Level:** [Clear / Partially Clear / Obscure]
**Sources of obscurity (if any):** [Identified issues]

### Distinctness Assessment

**Differs from related concepts:** [Yes/No - explain differences]
**Conflated ideas detected:** [Yes/No - what's being merged]
**Boundaries defined:** [Yes/No - where are edges unclear]
**Confusion risk:** [Low/Medium/High - what might this be confused with]

**Distinctness Level:** [Distinct / Partially Distinct / Confused]
**Sources of confusion (if any):** [Identified issues]

### Fitness Assessment

**Intended use:** [Purpose stated or inferred]
**Required level:** [Based on purpose]
**Current status:** [Sufficient / Insufficient]

### Verdict

**Overall:** [Clear and Distinct / Needs Clarification / Needs Distinction / Needs Both]

**Recommendation:** [Specific steps to achieve required level]

### Improved Formulation (if needed)
[Clearer/more distinct version of the idea]
```

---

## The Wax Test (Exemplar)

Descartes' wax argument illustrates the distinction:

**Sensory idea of wax:** Color, smell, texture, sound - these are CLEAR (vivid when perceived) but NOT DISTINCT (they change and are confused with the wax itself).

**Intellectual idea of wax:** Extended, flexible, changeable substance - this is CLEAR (grasped by intellect) AND DISTINCT (separates the wax's essence from its accidental properties).

Use this as a model: seek the intellectual grasp that survives change and examination.

---

## Constraints

- Clarity is not the same as simplicity - quantum mechanics can be clear to a physicist
- Distinctness is not isolation - "justice" can be distinct while related to "fairness"
- First encounters with ideas are rarely clear - this tests current state, not learnability
- Cultural/domain familiarity affects perceived clarity - account for this
- The test is relative to a mind: clear to an expert, obscure to a novice

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Idea cannot be stated | That IS the diagnosis: not yet clear enough to articulate |
| User insists idea is clear despite failing tests | Distinguish feeling of clarity from demonstrated clarity |
| Highly technical idea | Evaluate clarity for intended audience, not universal clarity |
| Multiple ideas conflated in input | Separate them first, then evaluate each |
| Idea requires context not provided | Request context or evaluate with stated assumptions |

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

**Input:** "I want to build a startup around 'democratizing AI.' Is this clear enough to build a company on?"

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


## Clarity-Distinctness Evaluation: "Democratizing AI"

### Idea Under Evaluation
**Stated as:** "Democratizing AI"
**Restated precisely:** [Attempting...] Making AI accessible/available to more people? Reducing barriers to AI use? Distributing power over AI systems? Enabling participation in AI development?

*Note: Multiple possible meanings suggest distinctness issues.*

### Clarity Assessment

**Can be stated in different words:** Partially. "Making AI accessible" preserves some meaning, but "democratizing" carries connotations (power distribution, participation) that "accessible" misses.

**Concrete examples available:**
- OpenAI releasing GPT to public?
- No-code ML tools?
- Community governance of AI systems?
- AI education for non-programmers?

All plausible - which indicates the concept isn't pinned down.

**Falsification conditions clear:** Unclear. What would count as "not democratizing"? Expensive proprietary AI? Centralized control? The opposite isn't defined, so the concept isn't either.

**Effect of examination:** Muddier. The more we probe, the more meanings emerge.

**Clarity Level:** Partially Clear - there's something there about accessibility/distribution, but the core is vague.

**Sources of obscurity:**
1. "Democratize" is metaphorical - democracy is a political system, not directly applicable to technology
2. Multiple dimensions conflated: access, cost, control, participation, understanding

### Distinctness Assessment

**Differs from related concepts:**
- vs. "Making AI affordable" - overlaps but democratize implies more than price
- vs. "Open-source AI" - overlaps but democratize suggests end-user access, not developer access
- vs. "AI literacy" - overlaps but democratize suggests capability, not just understanding

These are related but not identical - yet the phrase "democratizing AI" doesn't clearly specify which.

**Conflated ideas detected:** Yes
1. Access (can I use it?)
2. Affordability (can I afford it?)
3. Understanding (can I grasp what it does?)
4. Control (can I influence how it's built?)
5. Participation (can I contribute to its development?)

**Boundaries defined:** No. Where does "democratizing AI" end? Does it include governance? Regulation? Education?

**Confusion risk:** High. Investors, customers, and employees might all understand this differently.

**Distinctness Level:** Confused - multiple distinct goals are merged under one phrase.

**Sources of confusion:**
1. Equivocation on "democracy" (access? participation? equality?)
2. Conflation of user access, developer access, and governance
3. Undefined scope (AI tools? AI systems? AI companies?)

### Fitness Assessment

**Intended use:** Foundation for a startup (mission statement, product direction, hiring, fundraising)
**Required level:** Clear AND Distinct - must communicate precisely to stakeholders
**Current status:** Insufficient

### Verdict

**Overall:** Needs Both Clarification and Distinction

**Recommendation:**
1. Choose ONE of the conflated meanings as primary
2. Define it concretely (what specifically will users be able to do?)
3. Specify what is NOT included
4. Test: Can you complete "We will have succeeded when..."?

### Improved Formulation Options

Instead of "democratizing AI," consider:

- **"No-code AI for small businesses"** - Clear (specific tool type), Distinct (specific audience, specific format)
- **"Community-governed AI models"** - Clear (governance focus), Distinct (about control, not just access)
- **"AI education for non-programmers"** - Clear (education), Distinct (knowledge vs. tools)

Each is clearer AND more distinct than "democratizing AI" - and each would build a different company.

*"A clear idea is one present and apparent to an attentive mind. A distinct idea is one so precisely separated from all others that it contains nothing but what is clear."*

---

## Integration

This skill is part of the **Rene Descartes** expert persona. It implements his epistemological criterion from *Meditations on First Philosophy*. Use it to test whether ideas are ready to build on.

Pairs well with:
- **methodical-doubt-analysis** (ideas that survive doubt should be clear and distinct)
- **analysis-synthesis-method** (each component should be clearly understood)
- **foundational-certainty-mapping** (foundations must be clear and distinct)