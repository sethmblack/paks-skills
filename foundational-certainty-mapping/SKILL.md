---
name: foundational-certainty-mapping
description: Map the epistemic foundations of a domain, belief system, or project - identifying what is certain, what depends on what, and where uncertainty enters the chain of reasoning.
license: MIT
metadata:
  version: 1.0.997
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- foundational-certainty-mapping
- writing
---

# Foundational Certainty Mapping

Map the epistemic foundations of a domain, belief system, or project - identifying what is certain, what depends on what, and where uncertainty enters the chain of reasoning.

**Token Budget:** ~650 tokens. Reserve tokens for mapping output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Claim certainty where genuine doubt exists
- Dismiss legitimate uncertainty as mere anxiety
- Construct false hierarchies to make things seem more certain than they are
- Ignore dependency relationships between beliefs

**Authenticity Requirement:** This skill implements the structural approach of Descartes' *Meditations* - finding the indubitable foundation (cogito) and building outward. Every domain has its cogito-equivalent.

---

## When to Use

- User asks "What can I build on here?" or "What do I know for sure?"
- Need to "map the foundations" of a project or belief system
- Before making major decisions, to understand what's solid vs. shaky
- When uncertainty is paralyzing - distinguish genuine from false uncertainty
- Establishing epistemological footing in a new domain
- Understanding why a system of beliefs holds together (or doesn't)

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| domain_or_project | Yes | The area to map |
| existing_beliefs | No | Current claims or assumptions to evaluate |
| certainty_threshold | No | How strict: philosophical, practical, or working-assumption |

**Certainty Thresholds:**
- **Philosophical:** Cannot be doubted even by evil demon standard
- **Practical:** Reliable enough that doubting would be unreasonable
- **Working-assumption:** Best available belief given current evidence

---

## Workflow

### Step 1: Identify the Cogito-Equivalent
Ask: "What must be true for this inquiry to even be possible?"

Every domain has something that cannot be coherently denied:
- In logic: The laws of thought (cannot deny without using them)
- In science: That there is something to observe
- In business: That you exist, intend something, and act in a world
- In relationships: That you and another exist and communicate

This becomes the foundation. Everything else builds from here.

### Step 2: Inventory Beliefs
List all claims, assumptions, and beliefs relevant to the domain. Include:
- Explicit claims
- Implicit assumptions
- Things "everyone knows"
- Premises of ongoing reasoning

### Step 3: Classify by Certainty Level

| Level | Description | Symbol |
|-------|-------------|--------|
| Indubitable | Cannot be coherently denied; cogito-level | ◆ |
| Self-evident | Clear and distinct; needs no proof | ● |
| Proven | Derived validly from higher levels | ○ |
| Strongly supported | Evidence compels but doubt possible | △ |
| Assumed | Taken for granted; not examined | □ |
| Uncertain | Actively doubtful | ? |

### Step 4: Map Dependencies
For each belief, identify:
- What it depends on (what must be true for this to be true)
- What depends on it (what would fall if this fell)

Create a hierarchy showing the dependency structure.

### Step 5: Identify Vulnerability Points
Where does uncertainty enter? What assumed beliefs, if false, would cascade?

- **Single points of failure:** Many beliefs depend on one uncertain assumption
- **Hidden assumptions:** Things taken for granted but not examined
- **Weakest links:** Where evidence is thinnest in the chain

### Step 6: Assess Overall Foundation
Given the map:
- How solid is the base?
- How much rests on uncertain ground?
- What would it take to strengthen the foundation?

---

## Output Format

```markdown
## Foundational Certainty Map: [Domain/Project]

### The Cogito-Equivalent
**Foundation:** [What cannot be coherently denied here]
**Why indubitable:** [What makes denial self-refuting]

### Belief Inventory

| # | Belief/Claim | Level | Symbol | Depends On |
|---|--------------|-------|--------|------------|
| 1 | [Foundation] | Indubitable | ◆ | Nothing |
| 2 | [Belief 2] | [Level] | [Symbol] | 1 |
| 3 | [Belief 3] | [Level] | [Symbol] | 1, 2 |
| 4 | [Belief 4] | [Level] | [Symbol] | 3 |
[Continue as needed]

### Dependency Hierarchy

```
◆ [Foundation]
├── ● [Self-evident 1]
│   ├── ○ [Proven from above]
│   │   └── △ [Supported by evidence]
│   └── □ [Assumed, not examined]
│       └── ? [Uncertain conclusion]
└── ● [Self-evident 2]
    └── △ [Supported]
```

### Vulnerability Analysis

**Strongest elements:**
- [What is most certain and load-bearing]

**Single points of failure:**
- [Beliefs that many others depend on, but are less than certain]

**Hidden assumptions:**
- [Things taken for granted that haven't been examined]

**Weakest links:**
- [Where uncertainty enters the chain most critically]

### Cascade Analysis
If [uncertain belief X] is false, these also fall:
- [List of dependent beliefs]

### Foundation Assessment

**Overall solidity:** [Strong / Moderate / Weak]
**Recommendation:** [What would strengthen the foundation]

### Building Forward
Given this foundation, you can confidently:
- [What actions/conclusions are supported]

You should hedge or investigate further:
- [What remains uncertain]

You should not assume:
- [What lacks foundation despite common assumption]
```

---

## Certainty Levels Explained

**Indubitable (◆):** Denying it would be self-refuting. "I think" cannot be doubted by the thinker. In business: "I am trying to accomplish something" - cannot run a project while denying you're trying to accomplish it.

**Self-evident (●):** Clear and distinct upon examination, needs no further proof. Basic logical truths, definitional truths, immediate introspective reports.

**Proven (○):** Follows validly from indubitable or self-evident premises. If the premises are certain and the logic valid, the conclusion inherits certainty.

**Strongly supported (△):** Evidence compels belief, but alternatives are conceivable. Most empirical knowledge, including scientific theories.

**Assumed (□):** Taken for granted without examination. May be well-founded or may be cultural artifact. Needs examination.

**Uncertain (?):** Active doubt exists. Either evidence conflicts, or reasoning is incomplete, or the matter is genuinely unknown.

---

## Constraints

- Philosophical certainty is rare - most practical reasoning uses lower thresholds
- The map reflects current knowledge - new evidence can shift levels
- Dependencies may not be obvious - probe for hidden assumptions
- Some domains have no indubitable foundation - map shows this clearly
- The goal is clarity about uncertainty, not elimination of all doubt

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No clear cogito-equivalent | Note that domain lacks indubitable foundation; map from strongest available |
| Everything seems uncertain | Check if doubt is genuine or anxiety; some things must be assumed to act |
| Circular dependencies | Identify the circle; at least one element must be foundational |
| User wants more certainty than available | Honestly map the actual state; don't manufacture false certainty |
| Very large domain | Focus on relevant subset; map can be expanded |

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

**Input:** "I'm planning to change careers into data science. Map my foundational certainties."

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


## Foundational Certainty Map: Career Change to Data Science

### The Cogito-Equivalent
**Foundation:** I exist, have values, can learn, and seek a better situation.
**Why indubitable:** Denying this while planning a career change is self-refuting. The very act of planning presupposes agency, values, and the possibility of change.

### Belief Inventory

| # | Belief/Claim | Level | Symbol | Depends On |
|---|--------------|-------|--------|------------|
| 1 | I exist and can act | Indubitable | ◆ | Nothing |
| 2 | I want more fulfilling/better-paying work | Self-evident | ● | 1 |
| 3 | Data science is a legitimate field | Proven | ○ | 1 |
| 4 | Data science pays well | Strongly supported | △ | 3 |
| 5 | I can learn data science skills | Assumed | □ | 1 |
| 6 | I will enjoy data science work | Uncertain | ? | 5 |
| 7 | I can get a data science job | Assumed | □ | 5, 4 |
| 8 | The field will remain viable for my career | Uncertain | ? | 3 |
| 9 | This change will make me happier | Uncertain | ? | 2, 6, 7 |

### Dependency Hierarchy

```
◆ I exist and can act
├── ● I want something better
│   └── ? This change will make me happier
│       ├── ? I will enjoy DS work
│       │   └── □ I can learn DS skills
│       └── □ I can get a DS job
│           ├── □ I can learn DS skills
│           └── △ DS pays well
│               └── ○ DS is legitimate field
└── ○ DS is legitimate field
    └── ? Field will remain viable
```

### Vulnerability Analysis

**Strongest elements:**
- My existence and agency (cannot be doubted)
- My desire for improvement (clear and present)
- Data science is a real field with real jobs (easily verified)

**Single points of failure:**
- "I can learn data science skills" (□ Assumed)
  - Many downstream beliefs depend on this
  - Has not been tested
  - If false, much of the plan collapses

**Hidden assumptions:**
- Learning ability is like past learning (may differ for technical skills)
- Job market will accept career changers
- Remote/flexible options exist

**Weakest links:**
- "I will enjoy data science work" - completely untested
- "Field will remain viable" - requires prediction

### Cascade Analysis
If "I can learn data science skills" is false:
- "I can get a data science job" falls
- "I will enjoy data science work" becomes moot
- "This change will make me happier" becomes highly uncertain
- The entire career change premise weakens

### Foundation Assessment

**Overall solidity:** Moderate
- Strong: The desire is real, the field is real, the opportunity structure exists
- Weak: Core assumption (I can learn this) is untested; outcome (will I enjoy it?) is unknown

**Recommendation:**
Test the foundational assumption before committing:
1. Take an introductory course - can you learn this material?
2. Do a project - do you enjoy the actual work?
3. Talk to practitioners - is the daily reality appealing?

### Building Forward

Given this foundation, you can confidently:
- Research the field and its requirements
- Begin introductory learning as a test
- Explore options without full commitment

You should hedge or investigate further:
- Your ability to learn technical material (test it)
- Your actual enjoyment of the work (try it)
- Job market receptivity to career changers (research specific paths)

You should not assume:
- That interest equals aptitude
- That current market conditions will persist
- That happiness will follow from better pay

*Find your certainties. Build from them. Test your assumptions before depending on them.*

---

## Integration

This skill is part of the **Rene Descartes** expert persona. It implements the structural approach of *Meditations* - finding the indubitable foundation and building systematically outward. Use it to understand what you can rely on.

Pairs well with:
- **methodical-doubt-analysis** (test beliefs before mapping)
- **analysis-synthesis-method** (decompose then map foundations of each part)
- **clarity-distinctness-evaluation** (ensure mapped beliefs are clear)