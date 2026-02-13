---
name: grand-challenge-selection
description: Evaluate whether a problem is worth pursuing using Hassabis's five-dimension assessment framework. The best problems have clear win conditions, scientific significance, real-world impact, tractabil...
license: MIT
metadata:
  version: 1.0.1065
  author: sethmblack
keywords:
- grand-challenge-selection
- transformation
- writing
---

# Grand Challenge Selection

Evaluate whether a problem is worth pursuing using Hassabis's five-dimension assessment framework. The best problems have clear win conditions, scientific significance, real-world impact, tractability, and talent attraction.

---

## When to Use

- User asks "Is this problem worth solving?" or "Should we pursue this?"
- Evaluating a new research direction, product initiative, or technical challenge
- Scoping AI/ML projects or any ambitious technical undertaking
- Someone proposes a goal that seems either too vague or too incremental
- Comparing multiple potential problem areas to focus on
- Defending or questioning the choice of a specific problem

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| problem_description | Yes | The problem, research direction, or challenge being evaluated |
| domain_context | No | Field or industry where the problem exists |
| available_resources | No | Team size, timeline, funding, or other constraints |
| existing_benchmarks | No | Known ways to measure progress in this domain |
| competing_approaches | No | What others have tried or are trying |

---

## The Grand Challenge Selection Framework

### Step 1: Assess Measurability

Can progress be quantified objectively? The best problems have clear win conditions.

**Questions to ask:**
- Is there an existing benchmark or competition (e.g., CASP for protein folding)?
- Can success be scored against ground truth?
- Will the community agree on what "solved" means?
- Can intermediate progress be measured?

**Red flags:**
- "We'll know it when we see it" (too subjective)
- No existing evaluation methodology
- Success depends on opinion rather than measurement

**Example:** AlphaFold targeted CASP competition where predictions could be scored against experimental structures using GDT scores.

### Step 2: Assess Scientific Significance

Does solving this advance fundamental understanding? Great problems reveal deep truths.

**Questions to ask:**
- Is this a long-standing challenge? (10+ years of attempts)
- Would solving it settle theoretical debates?
- Does it require developing new methods that generalize?
- Would it appear in textbooks as a milestone?

**Red flags:**
- Only matters for one specific application
- Incremental improvement on existing capabilities
- No fundamental insight required to solve it

**Example:** Protein folding was biology's "50-year grand challenge" - solving it revealed that attention mechanisms could capture evolutionary and physical constraints in ways that generalize.

### Step 3: Assess Real-World Impact

Will the solution help people? Grand challenges must matter beyond academia.

**Questions to ask:**
- Who benefits from a solution?
- How many people or what scale of problem?
- What becomes possible that was impossible before?
- Is there a clear path from solution to application?

**Red flags:**
- Impact is theoretical or speculative
- Requires many additional breakthroughs to be useful
- Helps only a narrow niche

**Example:** AlphaFold2 enabled drug discovery acceleration, disease understanding, and enzyme design - 2+ million researchers use it across 190 countries.

### Step 4: Assess Tractability

Can it be decomposed into solvable subproblems? Ambitious does not mean impossible.

**Questions to ask:**
- What are the component challenges?
- Which subproblems have existing solutions?
- What capability would enable the next step?
- Are there intermediate milestones with value?
- Is there sufficient training data or a way to generate it?

**Red flags:**
- Requires solving multiple unsolved problems simultaneously
- No clear decomposition exists
- All-or-nothing (no valuable intermediate states)

**Example:** Protein folding could be decomposed: 1D sequence to 3D structure required integrating evolutionary information (MSA), physical constraints, and attention mechanisms - each addressable component.

### Step 5: Assess Talent Attraction

Will ambitious researchers want to work on it? Great problems attract great people.

**Questions to ask:**
- Would top researchers be excited to join?
- Does it offer career-defining potential?
- Is it at the frontier of what's possible?
- Does it combine interesting technical challenges?
- Is failure instructive (you learn even if you don't fully succeed)?

**Red flags:**
- Seems like "grunt work" to top talent
- Success depends on resources rather than insight
- Appears incremental rather than transformative

**Example:** DeepMind recruited top ML and biology researchers for AlphaFold because it was clearly a career-defining opportunity at the frontier of AI and science.

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
## Grand Challenge Assessment: [Problem Name]

### Problem Summary
[One paragraph description of the problem being evaluated]

### Five-Dimension Evaluation

| Dimension | Score (1-5) | Assessment |
|-----------|-------------|------------|
| Measurability | X | [Key finding] |
| Scientific Significance | X | [Key finding] |
| Real-World Impact | X | [Key finding] |
| Tractability | X | [Key finding] |
| Talent Attraction | X | [Key finding] |

**Total Score: XX/25**

### Detailed Analysis

#### Measurability (X/5)
[What benchmark exists or could be created? How would we score progress?]

#### Scientific Significance (X/5)
[What fundamental understanding would this advance? How long has this been an open problem?]

#### Real-World Impact (X/5)
[Who benefits? At what scale? What applications become possible?]

#### Tractability (X/5)
[What are the subproblems? What capabilities are needed? Is data available?]

#### Talent Attraction (X/5)
[Would top researchers want to work on this? Is it at the frontier?]

### Recommendation

**Verdict:** PURSUE / REFINE / DEFER / PASS

**Rationale:** [2-3 sentences on overall recommendation]

**If PURSUE:**
- Suggested benchmark: [What to target]
- First milestone: [Initial capability to build]
- Key risk: [What could derail this]

**If REFINE:**
- Missing element: [What dimension needs work]
- Suggested reformulation: [How to make it a better grand challenge]

**If DEFER:**
- Blocking prerequisite: [What must be solved first]
- Revisit when: [Conditions that would change assessment]

**If PASS:**
- Fundamental issue: [Why this is not a grand challenge]
- Alternative: [Better problem formulation or different direction]
```

---

## Scoring Calibration

### Measurability

| Score | Criteria |
|-------|----------|
| 5 | Established benchmark with objective scoring; community consensus on "solved" |
| 4 | Clear metric exists but not widely adopted; measurable with some ambiguity |
| 3 | Progress can be quantified but "solved" is debatable |
| 2 | Only subjective evaluation possible; hard to compare approaches |
| 1 | No way to measure progress; success is entirely subjective |

### Scientific Significance

| Score | Criteria |
|-------|----------|
| 5 | Decades-old grand challenge; would resolve fundamental debates; textbook milestone |
| 4 | Major open problem in the field; would advance theory significantly |
| 3 | Meaningful research contribution; useful new methods |
| 2 | Incremental advance; application-specific without broader insight |
| 1 | No theoretical significance; purely engineering execution |

### Real-World Impact

| Score | Criteria |
|-------|----------|
| 5 | Benefits billions; enables transformative applications; clear path to deployment |
| 4 | Benefits millions; significant practical value; path to deployment exists |
| 3 | Benefits thousands of researchers/practitioners; enables new research directions |
| 2 | Narrow application; benefits specific niche only |
| 1 | No clear practical benefit; purely academic exercise |

### Tractability

| Score | Criteria |
|-------|----------|
| 5 | Clear decomposition; subproblems have partial solutions; data available; intermediate value |
| 4 | Decomposition exists; most components addressable; some gaps |
| 3 | Possible decomposition; significant unknowns; path is visible |
| 2 | Unclear how to decompose; requires multiple simultaneous breakthroughs |
| 1 | No clear path; seems to require magic or undefined breakthroughs |

### Talent Attraction

| Score | Criteria |
|-------|----------|
| 5 | Top researchers already interested; career-defining opportunity; frontier of possible |
| 4 | Would attract strong researchers; interesting technical challenges |
| 3 | Reasonable research project; would attract good (not top) talent |
| 2 | Appears incremental; hard to recruit top people |
| 1 | Perceived as grunt work; no one ambitious wants to work on it |

---

## Constraints

- A low score in one dimension does not disqualify a problem - it highlights where work is needed
- Score 20+ suggests a genuine grand challenge worth major investment
- Score 15-19 suggests potential with refinement needed
- Score below 15 suggests this is not (yet) a grand challenge
- Measurability and Tractability are often improvable; Scientific Significance usually is not
- Be honest about talent attraction - if you would not be excited, neither would others

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Problem too vague | Ask for specifics: "What would solved look like?" |
| Problem too narrow | Explore generalization: "What broader challenge does this address?" |
| No existing benchmark | Propose one: "What metric would make progress visible?" |
| All dimensions low | This is not a grand challenge; help reformulate or redirect |
| Scores high but gut says no | Trust the instinct; articulate which assumption is wrong |

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

**Input:** "We want to build an AI that can design new antibiotics to combat resistance."

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


## Grand Challenge Assessment: AI-Driven Antibiotic Discovery

### Problem Summary
Develop an AI system that can design novel antibiotic compounds to address the growing crisis of antimicrobial resistance. The system would generate candidate molecules with predicted efficacy against resistant bacteria and favorable safety/pharmacokinetic profiles.

### Five-Dimension Evaluation

| Dimension | Score (1-5) | Assessment |
|-----------|-------------|------------|
| Measurability | 4 | In-vitro efficacy testable; clinical success harder to measure pre-trial |
| Scientific Significance | 4 | Major challenge in drug discovery; would advance generative chemistry |
| Real-World Impact | 5 | Antibiotic resistance is existential threat; millions of lives at stake |
| Tractability | 3 | Requires molecule generation + efficacy prediction + ADMET; some components solved |
| Talent Attraction | 5 | At frontier of AI + biology; career-defining if successful |

**Total Score: 21/25**

### Detailed Analysis

#### Measurability (4/5)
Candidate molecules can be tested in-vitro against bacterial panels. Predicted binding affinities can be compared to experimental results. However, true clinical success (Phase 3 trials) takes years and cannot serve as a rapid benchmark. Intermediate metrics like CASP-like competitions for binding prediction exist but are imperfect proxies.

#### Scientific Significance (4/5)
Antibiotic discovery has been a major challenge for decades. New classes of antibiotics are rarely discovered. AI-driven generation would advance computational chemistry and generative biology significantly. Not quite at the "50-year grand challenge" level but close.

#### Real-World Impact (5/5)
WHO estimates antimicrobial resistance could cause 10 million deaths annually by 2050. New antibiotics are desperately needed. Success would save millions of lives and establish AI as essential to drug discovery.

#### Tractability (3/5)
Decomposition exists: 1) Generate novel molecular structures, 2) Predict efficacy against targets, 3) Predict safety/pharmacokinetics. AlphaFold addresses protein structure; generative chemistry is advancing. However, connecting structure to in-vivo efficacy remains hard. Limited training data for truly novel mechanisms of action.

#### Talent Attraction (5/5)
This is the frontier of AI-for-science. Top researchers at DeepMind, Isomorphic Labs, and others are already working on related problems. Clear career-defining opportunity. Combines interesting ML (generation, prediction) with meaningful application.

### Recommendation

**Verdict:** PURSUE

**Rationale:** This scores 21/25 - a genuine grand challenge. The combination of existential real-world importance, frontier technical challenges, and measurable (if imperfect) benchmarks makes this worth major investment. Tractability is the main weakness.

**If PURSUE:**
- Suggested benchmark: In-vitro MIC (Minimum Inhibitory Concentration) against a panel of resistant strains; compare AI-designed candidates to random/baseline generation
- First milestone: Generate molecules with predicted efficacy that pass initial in-vitro screening at >50% rate
- Key risk: Generated molecules may fail in-vivo despite in-vitro success; limited training data for novel mechanisms

---

## Integration

This skill is part of the **Demis Hassabis** expert persona. Use it at the start of any major project, research direction, or strategic initiative. The assessment provides objective criteria for whether a problem deserves grand-challenge-level investment.

Pairs with:
- **capability-ladder-design** to map the progression after a problem is selected
- **benchmark-definition** to specify the measurability dimension in detail