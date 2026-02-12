---
name: ten-principles-audit
description: Systematically evaluate any design, product, process, or artifact against
  Dieter Rams' Ten Principles of Good Design to identify specific improvements.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- ten-principles-audit
- writing
---

# Ten Principles Audit

Systematically evaluate any design, product, process, or artifact against Dieter Rams' Ten Principles of Good Design to identify specific improvements.

---

## When to Use

- Evaluating a product design before launch
- Reviewing a user interface or user experience
- Assessing a process or workflow for quality
- Auditing communications, documentation, or presentations
- Request for "Rams-style analysis" or "Apply the ten principles"
- Any situation where design quality needs objective assessment

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| artifact | Yes | Description of the design, product, process, or artifact to evaluate |
| context | No | How and where it will be used |
| users | No | Who will interact with it |
| constraints | No | Limitations on the design (budget, technology, time) |

---

## The Ten Principles Framework

Evaluate the artifact against each principle, scoring 1-10:

### 1. Innovative
**Question:** Does this advance beyond what exists? Is the innovation meaningful or superficial?
**Pass criteria:** Offers genuine improvement, not change for its own sake
**Red flags:** Novelty without purpose, technology without benefit

### 2. Useful
**Question:** Does this serve genuine functional, psychological, and aesthetic needs?
**Pass criteria:** Fulfills a real purpose, satisfies actual user requirements
**Red flags:** Features without use cases, solutions seeking problems

### 3. Aesthetic
**Question:** Is aesthetic quality integral to function, or applied as decoration?
**Pass criteria:** Beauty emerges from purpose; form follows function
**Red flags:** Ornamentation, styling that contradicts function, beauty as afterthought

### 4. Understandable
**Question:** Does this clarify its own structure? Is it self-explanatory?
**Pass criteria:** Users understand purpose and operation without instruction
**Red flags:** Requires extensive explanation, hidden functionality, confusing structure

### 5. Unobtrusive
**Question:** Does this serve as a tool, or demand attention?
**Pass criteria:** Neutral, restrained, leaves room for user's self-expression
**Red flags:** Competes for attention, decorative excess, dominates rather than serves

### 6. Honest
**Question:** Does this accurately represent its capabilities?
**Pass criteria:** Communicates only functions and values it actually delivers
**Red flags:** Overpromises, creates false impressions, manipulates expectations

### 7. Long-lasting
**Question:** Will this endure, or is it merely fashionable?
**Pass criteria:** Avoids trends that will date it; remains relevant for years
**Red flags:** Follows current fashion, will appear outdated soon, planned obsolescence

### 8. Thorough
**Question:** Is every detail considered? Is anything arbitrary?
**Pass criteria:** Care and accuracy throughout; nothing left to chance
**Red flags:** Inconsistencies, arbitrary choices, incomplete execution

### 9. Environmentally Friendly
**Question:** What is the lifecycle impact? Does it conserve resources?
**Pass criteria:** Minimizes physical and visual pollution; considers full lifecycle
**Red flags:** Wasteful materials, short lifespan by design, disposal problems

### 10. As Little Design as Possible
**Question:** Has everything non-essential been removed?
**Pass criteria:** Concentrates on essentials; nothing could be removed without harm
**Red flags:** Visual noise, unnecessary features, complexity without purpose

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
## Ten Principles Audit

**Artifact:** [Name/description of what is being evaluated]
**Context:** [How/where it will be used]
**Date:** [Evaluation date]

### Evaluation Summary

| Principle | Score (1-10) | Assessment |
|-----------|--------------|------------|
| 1. Innovative | X | [Brief assessment] |
| 2. Useful | X | [Brief assessment] |
| 3. Aesthetic | X | [Brief assessment] |
| 4. Understandable | X | [Brief assessment] |
| 5. Unobtrusive | X | [Brief assessment] |
| 6. Honest | X | [Brief assessment] |
| 7. Long-lasting | X | [Brief assessment] |
| 8. Thorough | X | [Brief assessment] |
| 9. Environmentally Friendly | X | [Brief assessment] |
| 10. As Little Design as Possible | X | [Brief assessment] |

**Overall Score:** XX/100

### Critical Issues
[List the most significant violations, prioritized by impact]

### Detailed Analysis

#### Strengths
[What this design does well, with specific examples]

#### Areas for Improvement
[Specific issues with actionable recommendations for each]

### Recommendations
[Prioritized list of specific changes to improve the design]

### The Essential Question
[Would I recommend this for production? Why or why not?]
```

---

## Scoring Guide

| Score | Meaning |
|-------|---------|
| 9-10 | Exemplary - Sets standard for the principle |
| 7-8 | Good - Satisfies the principle with minor issues |
| 5-6 | Adequate - Meets basic requirements, room for improvement |
| 3-4 | Poor - Significant violations of the principle |
| 1-2 | Failing - Fundamentally contradicts the principle |

---

## Constraints

- Score honestly; inflation helps no one
- Cite specific elements, not general impressions
- Recommendations must be actionable, not abstract
- Consider constraints—a budget product judged against luxury standards fails unfairly
- Focus on what matters most; not all principles carry equal weight for all artifacts

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

**Input:** "Evaluate our new mobile banking app dashboard"

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


## Ten Principles Audit

**Artifact:** Mobile banking app dashboard
**Context:** Primary interface for daily banking tasks on iOS/Android
**Date:** 2026-01-18

### Evaluation Summary

| Principle | Score (1-10) | Assessment |
|-----------|--------------|------------|
| 1. Innovative | 5 | Standard card layout; no meaningful advancement |
| 2. Useful | 7 | Core functions accessible; some buried features |
| 3. Aesthetic | 4 | Decorative gradients contradict clarity |
| 4. Understandable | 6 | Main functions clear; secondary functions hidden |
| 5. Unobtrusive | 3 | Promotional cards compete with user tasks |
| 6. Honest | 5 | "Instant" transfers take 1-3 business days |
| 7. Long-lasting | 4 | Glassmorphism will date within 2 years |
| 8. Thorough | 6 | Good primary flows; edge cases neglected |
| 9. Environmentally Friendly | 7 | Digital product; server efficiency unknown |
| 10. As Little Design as Possible | 3 | Excessive animations, unused features prominent |

**Overall Score:** 50/100

### Critical Issues
1. **Promotional content prioritized over user tasks** (Unobtrusive: 3)
2. **Fashionable visual style that will age poorly** (Long-lasting: 4)
3. **Visual complexity without functional benefit** (As Little Design: 3)

### Detailed Analysis

#### Strengths
- Account balance immediately visible (Useful)
- Transaction history well-organized (Thorough)
- Core transfer function accessible in two taps (Useful)

#### Areas for Improvement
- Marketing cards occupy 40% of first viewport; user's primary task (check balance, make transfer) pushed down
- Glassmorphism blur effects reduce readability and follow trend that will appear dated
- Animation on every interaction adds 200-300ms to perceived response time without functional purpose
- "Instant transfer" label when transfers actually take 1-3 days (Honest)

### Recommendations
1. **Remove or minimize promotional content** - Banking app serves banking tasks, not marketing
2. **Replace trendy visual effects with timeless clarity** - High contrast, clear typography, no blur effects
3. **Eliminate decorative animations** - Keep only animations that communicate system state
4. **Audit all labels for accuracy** - "Instant" must mean instant or be relabeled

### The Essential Question
Not recommended for production in current form. Core functionality exists but is compromised by marketing priorities and fashionable styling that contradicts the app's purpose as a financial tool requiring clarity and trust.

---

## Integration

This skill is part of the **Dieter Rams** expert persona. Use it when you need rigorous, principle-based design evaluation unclouded by trend-following or subjective preference.