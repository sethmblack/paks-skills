---
name: reduction-protocol
description: 'Systematically identify and eliminate unnecessary elements from any artifact until nothing remains that could be removed without impairing function. Based on Dieter Rams'' principle: "Less, but bett...'
license: MIT
metadata:
  version: 1.0.1745
  author: sethmblack
keywords:
- reduction-protocol
- writing
---

# Reduction Protocol

Systematically identify and eliminate unnecessary elements from any artifact until nothing remains that could be removed without impairing function. Based on Dieter Rams' principle: "Less, but better."

---

## When to Use

- Simplifying a product, interface, or process
- Editing documents, presentations, or communications
- Streamlining workflows or procedures
- Reducing code complexity
- Decluttering any system with accumulated elements
- Request for "simplify," "reduce," "what can I cut"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| artifact | Yes | The design, document, process, or system to reduce |
| core_function | Yes | The essential purpose this artifact must serve |
| constraints | No | What cannot be removed (requirements, regulations) |

---

## The Reduction Process

### Phase 1: Establish Function

Before removing anything, establish with clarity:
- **What is the core function?** State in one sentence.
- **Who is this for?** Define the user/audience.
- **What must they accomplish?** List essential tasks/outcomes.
- **What constraints exist?** Regulatory, technical, organizational.

*Without clarity of function, reduction becomes arbitrary deletion.*

### Phase 2: Inventory Elements

List every element in the artifact:
- For products: features, components, controls, materials
- For interfaces: screens, buttons, text, images, animations
- For documents: sections, paragraphs, sentences, words
- For processes: steps, approvals, handoffs, communications

Create a complete inventory before evaluation.

### Phase 3: Categorize Each Element

For each element, determine category:

| Category | Definition | Action |
|----------|------------|--------|
| **Essential** | Removal would impair core function | Keep |
| **Supportive** | Aids core function but not strictly necessary | Question |
| **Decorative** | Adds aesthetic without functional purpose | Remove unless proven valuable |
| **Redundant** | Duplicates another element's function | Remove |
| **Legacy** | Exists because it always has, no current purpose | Remove |
| **Anticipatory** | Added for "might need it" without evidence | Remove |

### Phase 4: Apply Reduction Questions

For each Supportive, Decorative, or questionable element:

1. **The Removal Test:** If I remove this, does the user's ability to accomplish the core function diminish?
2. **The Justification Test:** Can I articulate why this element must exist?
3. **The Frequency Test:** How often is this actually used/needed?
4. **The Alternative Test:** Could another element serve this function?
5. **The Cost Test:** What burden does this element create (complexity, maintenance, confusion)?

If an element fails these tests, mark for removal.

### Phase 5: Validate Reductions

Before finalizing:
- Review removed elements: any truly essential items incorrectly categorized?
- Test reduced artifact against core function: does it still accomplish the purpose?
- Consider edge cases: are legitimate but rare needs addressed?
- Verify constraints: have any requirements been violated?

### Phase 6: Document Results

Record what was removed and why, for future reference and to prevent reintroduction.

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
## Reduction Protocol Results

**Artifact:** [Name/description]
**Core Function:** [One-sentence statement of essential purpose]
**Date:** [Analysis date]

### Element Inventory

| Element | Category | Decision | Rationale |
|---------|----------|----------|-----------|
| [Element 1] | Essential | Keep | [Why] |
| [Element 2] | Redundant | Remove | [Why] |
| ... | ... | ... | ... |

### Summary

| Category | Count | Action |
|----------|-------|--------|
| Essential | X | Kept |
| Supportive | X | Y kept, Z removed |
| Decorative | X | Removed |
| Redundant | X | Removed |
| Legacy | X | Removed |
| Anticipatory | X | Removed |

**Total elements:** [Before] → [After]
**Reduction:** [Percentage]

### Removed Elements
[List of removed elements with brief rationale for each]

### Kept Elements
[List of essential elements that remain, with justification for any non-obvious inclusions]

### Resulting Artifact
[Description of the reduced artifact]

### Validation
- Core function preserved: [Yes/No with evidence]
- Edge cases addressed: [Yes/No with notes]
- Constraints satisfied: [Yes/No with notes]

### Recommendations
[Any additional observations or suggestions for further improvement]
```

---

## Constraints

- Never remove elements without understanding their purpose first
- Distinguish "unused" from "essential safety net"
- Consider the complete user, not just the primary use case
- Reduction is not about minimizing count, but maximizing clarity
- Some elements earn their place through rare but critical use

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

**Input:** "Simplify this weekly status report template"

**Artifact:** 12-section weekly status report template
**Core Function:** Communicate project status to stakeholders so they can make decisions

**Output:**

## Reduction Protocol Results

**Artifact:** Weekly status report template
**Core Function:** Communicate project status to stakeholders for decision-making
**Date:** 2026-01-18

### Element Inventory

| Element | Category | Decision | Rationale |
|---------|----------|----------|-----------|
| Project name/date header | Essential | Keep | Identifies the report |
| Executive summary | Essential | Keep | Core communication |
| Detailed task breakdown | Redundant | Remove | Duplicates project management tool |
| Risk register excerpt | Supportive | Keep (condense) | Supports decisions |
| Team member activity log | Decorative | Remove | Interesting but not decision-relevant |
| Budget variance | Essential | Keep | Key decision factor |
| Customer feedback verbatim | Anticipatory | Remove | Rarely read; summary sufficient |
| Historical comparison | Legacy | Remove | Added years ago, no one uses |
| Next week's forecast | Essential | Keep | Core communication |
| Appendix A-D | Redundant | Remove | Available in other systems |
| Signature blocks | Legacy | Remove | Digital reports need no signatures |
| Distribution list | Decorative | Remove | Email handles distribution |

### Summary

| Category | Count | Action |
|----------|-------|--------|
| Essential | 4 | Kept |
| Supportive | 1 | Kept (condensed) |
| Decorative | 2 | Removed |
| Redundant | 2 | Removed |
| Legacy | 2 | Removed |
| Anticipatory | 1 | Removed |

**Total elements:** 12 → 5
**Reduction:** 58%

### Removed Elements
- **Detailed task breakdown:** Duplicates Jira; stakeholders don't read granular tasks
- **Team member activity log:** Activity ≠ progress; creates accountability theater
- **Customer feedback verbatim:** Summary of themes sufficient; verbatim in separate system
- **Historical comparison:** No stakeholder has requested or referenced in 18 months
- **Appendices A-D:** Reference materials available in shared drive; inclusion bloats report
- **Signature blocks:** Vestige of paper process; no function in digital workflow
- **Distribution list:** Email system handles; redundant in document body

### Kept Elements
1. **Header:** Project identification (condensed to one line)
2. **Executive summary:** 3-bullet status (on track / at risk / blocked)
3. **Key risks:** Top 3 only, with owner and mitigation
4. **Budget variance:** Actual vs. planned, variance explanation if >5%
5. **Next week forecast:** 3 key milestones/deliverables

### Resulting Artifact
One-page report: Header + 3-bullet summary + 3 risks + budget line + 3 forecasted items. Readable in under 2 minutes. Decision-relevant information only.

### Validation
- Core function preserved: Yes - stakeholders receive information needed for decisions
- Edge cases addressed: Yes - detailed information available via links to source systems
- Constraints satisfied: Yes - compliance requirements met through executive summary

### Recommendations
- Add single hyperlink to detailed project dashboard for those wanting depth
- Establish consistent day/time for distribution to create predictable rhythm
- Review template quarterly: what's being read? what prompts questions?

---

## Integration

This skill is part of the **Dieter Rams** expert persona. Use it when complexity has accumulated and clarity requires systematic reduction. Remember: the goal is not minimal element count, but maximum clarity of function.