---
name: analysis-synthesis-method
description: Decompose complex problems into their simplest components, solve each part in order from simple to complex, then reconstruct the whole systematically to ensure completeness.
license: MIT
metadata:
  version: 1.0.3309
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- analysis-synthesis-method
- writing
---

# Analysis-Synthesis Method

Decompose complex problems into their simplest components, solve each part in order from simple to complex, then reconstruct the whole systematically to ensure completeness.

**Token Budget:** ~700 tokens. Reserve tokens for decomposition output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Skip the enumeration step (verification that nothing is omitted)
- Present a reconstruction as complete when components remain unaddressed
- Apply this method to problems better served by holistic approaches
- Fabricate components not genuinely part of the problem

**Authenticity Requirement:** This skill implements Descartes' four rules from *Discourse on the Method*. The method requires proceeding from simple to complex with nothing omitted.

---

## When to Use

- User says "This problem is too complex" or "I don't know where to start"
- Request to "break this down" or "divide and conquer"
- Complex system needs to be understood part by part
- Multi-step project needs systematic approach
- Problem seems overwhelming and needs structure
- User wants to ensure nothing is missed

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| problem_statement | Yes | The complex problem or question to decompose |
| known_constraints | No | Fixed requirements or limitations |
| simplicity_criteria | No | What counts as "simple enough" in this domain |
| completeness_requirement | No | How thorough the enumeration must be |

---

## Workflow
### Step 1: Evidence (Rule 1)
State clearly what is being analyzed. Accept only what is clear:
- What exactly is the problem?
- What are we trying to achieve?
- What do we know with clarity?

### Step 2: Analysis (Rule 2)
Divide the problem into as many parts as necessary:
- What are the component parts?
- Can any part be divided further?
- What is the smallest meaningful unit?

**Division Criteria:**
- Each part should be simpler than the whole
- Parts should be relatively independent (changes to one don't cascade unpredictably)
- Parts should collectively exhaust the problem (nothing left over)

### Step 3: Order (Rule 3)
Arrange parts from simplest to most complex:
- Which parts depend on no others?
- Which parts require understanding of previous parts?
- What is the natural learning order?

**Ordering Principles:**
- Foundational concepts first
- Independent before dependent
- Concrete before abstract
- Known before unknown

### Step 4: Enumeration (Rule 4)
Make reviews so complete that nothing is omitted:
- Have all parts been identified?
- Does the list account for the entire problem?
- What might have been missed?

### Step 5: Synthesis
Solve each part in order, then reconstruct:
- Address the simplest component first
- Build understanding/solution progressively
- Verify each step before proceeding
- Reconstruct the whole from solved parts

### Step 6: Verification
Confirm the synthesis is complete:
- Does the reconstruction address the original problem?
- Are all components accounted for?
- Does the whole function as intended?

---

## Output Format

```markdown
## Analysis-Synthesis: [Problem Statement]

### Step 1: Clear Problem Statement
**Original problem:** [As stated]
**Clarified problem:** [Precise formulation]
**Goal:** [What success looks like]

### Step 2: Decomposition

| # | Component | Description | Complexity |
|---|-----------|-------------|------------|
| 1 | [Part 1] | [Brief description] | Simple |
| 2 | [Part 2] | [Brief description] | Simple |
| 3 | [Part 3] | [Brief description] | Medium |
| 4 | [Part 4] | [Brief description] | Complex |

### Step 3: Ordered Sequence

**Dependency Map:**
```
[Part 1] (foundational)
    ↓
[Part 2] (builds on 1)
    ↓
[Part 3] (builds on 1, 2)
    ↓
[Part 4] (builds on all)
```

**Recommended Order:**
1. [Start here - simplest, no dependencies]
2. [Next - requires only step 1]
3. [Continue building...]
4. [Final - most complex, all prerequisites complete]

### Step 4: Enumeration Check

**Components accounted for:** [List]
**Potential gaps identified:** [Any missing pieces]
**Coverage assessment:** [Complete / Partial - needs X]

### Step 5: Component Solutions

**Component 1: [Name]**
- Approach: [How to address]
- Solution/Understanding: [Result]
- Verified: [Yes/No]

**Component 2: [Name]**
[Repeat structure]

### Step 6: Synthesis

**Reconstruction:**
[How the components fit together to form the complete solution]

**Verification:**
- Original problem addressed: [Yes/No]
- All components integrated: [Yes/No]
- Gaps or issues: [Any remaining problems]

### Summary
[Brief statement of the complete solution/understanding]
```

---

## Types of Decomposition

### Structural Decomposition
Breaking into physical or logical parts:
- System → Subsystems → Components
- Document → Sections → Paragraphs
- Organization → Departments → Roles

### Temporal Decomposition
Breaking into phases or stages:
- Project → Phases → Tasks
- Process → Steps → Actions
- Learning → Levels → Lessons

### Functional Decomposition
Breaking by purpose or capability:
- Goal → Sub-goals → Actions
- Feature → Functions → Operations
- Need → Requirements → Specifications

### Causal Decomposition
Breaking by cause-and-effect:
- Outcome → Contributing Factors → Root Causes
- Effect → Proximate Causes → Distal Causes

---

## Constraints

- Some problems are genuinely holistic - decomposition may lose emergent properties
- The "simplest" part is relative to the domain and the person
- Enumeration can never be absolutely guaranteed complete - aim for reasonable thoroughness
- Synthesis may reveal that decomposition was incorrect - iterate if needed
- Order matters: solving complex parts before simple foundations wastes effort

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Problem too vague | Request clarification before decomposing |
| Cannot find natural divisions | Try different decomposition type (structural, temporal, functional) |
| Parts are not independent | Note dependencies; order becomes critical |
| Enumeration seems incomplete | Ask: "What would someone object is missing?" |
| Synthesis doesn't match original | Re-examine decomposition; may have lost something |
| Too many components | Group into higher-level clusters, then decompose clusters |

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

**Input:** "I need to learn machine learning but I don't know where to start. It seems overwhelming."

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


## Analysis-Synthesis: Learning Machine Learning

### Step 1: Clear Problem Statement
**Original problem:** Learning machine learning seems overwhelming
**Clarified problem:** How to systematically acquire ML knowledge from zero to practical competence
**Goal:** Ability to understand, implement, and apply ML models to real problems

### Step 2: Decomposition

| # | Component | Description | Complexity |
|---|-----------|-------------|------------|
| 1 | Math foundations | Linear algebra, calculus, probability | Simple-Medium |
| 2 | Programming skills | Python, data manipulation | Simple |
| 3 | Core ML concepts | What ML is, types of learning, evaluation | Simple |
| 4 | Classical algorithms | Regression, trees, clustering | Medium |
| 5 | Neural networks | Perceptrons to deep learning | Medium-Complex |
| 6 | Practical tools | Libraries, frameworks, environments | Medium |
| 7 | Project experience | End-to-end implementation | Complex |

### Step 3: Ordered Sequence

**Dependency Map:**
```
[Programming] + [Math foundations]
         ↓
   [Core ML concepts]
         ↓
   [Classical algorithms]
         ↓
    [Practical tools]
         ↓
   [Neural networks]
         ↓
  [Project experience]
```

**Recommended Order:**
1. Programming fundamentals (Python, NumPy, Pandas) - no prerequisites
2. Math foundations (enough linear algebra and stats to follow) - can parallel with #1
3. Core ML concepts (vocabulary, problem types, evaluation) - needs #1, #2
4. Classical algorithms (start with linear regression, decision trees) - needs #3
5. Practical tools (scikit-learn, Jupyter) - needs #4
6. Neural networks (after classical is solid) - needs #4, #5
7. Project experience (integrate everything) - needs all above

### Step 4: Enumeration Check

**Components accounted for:**
- Prerequisites (math, programming) ✓
- Foundational knowledge (concepts, vocabulary) ✓
- Core techniques (classical, neural) ✓
- Practical implementation (tools, projects) ✓

**Potential gaps identified:**
- Domain knowledge (if applying to specific field)
- MLOps/deployment (production concerns)
- Ethics and responsible AI

**Coverage assessment:** Complete for foundational competence. Gaps are advanced topics.

### Step 5: Component Solutions

**Component 1: Programming**
- Approach: Python tutorial + data manipulation exercises
- Resources: Python basics (2 weeks), NumPy/Pandas (2 weeks)
- Verified when: Can load, clean, and manipulate datasets

**Component 2: Math foundations**
- Approach: Khan Academy or 3Blue1Brown for intuition
- Focus: Matrix operations, derivatives, probability distributions
- Verified when: Can follow ML paper math sections

**Component 3: Core ML concepts**
- Approach: Andrew Ng's course intro lectures
- Key topics: Supervised/unsupervised, train/test split, overfitting, metrics
- Verified when: Can explain ML problem formulation

[Continue for remaining components...]

### Step 6: Synthesis

**Reconstruction:**
Learning ML is not one overwhelming task but seven interconnected skills acquired in order. Start with programming and math in parallel (4 weeks). Then core concepts (2 weeks). Then classical algorithms with practical tools (4 weeks). Then neural networks (4 weeks). Then a capstone project integrating everything (4 weeks). Total: ~18 weeks for foundational competence.

**Verification:**
- Original problem addressed: Yes - clear path from overwhelmed to competent
- All components integrated: Yes - builds progressively
- Gaps or issues: Advanced topics (MLOps, ethics) deferred to second phase

### Summary
Break "learn ML" into: (1) code + math, (2) concepts, (3) classical methods, (4) tools, (5) deep learning, (6) projects. Master them in this order, spending roughly 2-4 weeks per component. The overwhelming whole becomes a series of manageable parts.

*"Divide each difficulty into as many parts as is feasible and necessary to resolve it."*

---

## Integration

This skill is part of the **Rene Descartes** expert persona. It implements his four rules of method from *Discourse on the Method*. Use it for any complex problem that resists direct attack.

Pairs well with:
- **methodical-doubt-analysis** (test components for certainty)
- **clarity-distinctness-evaluation** (ensure each component is clearly understood)
- **foundational-certainty-mapping** (identify what to build on)