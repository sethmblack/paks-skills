---
name: simplification-audit
description: Systematically identify and eliminate unnecessary complexity, options,
  and variations from systems, processes, or products.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- simplification-audit
- writing
---

# Simplification Audit

Systematically identify and eliminate unnecessary complexity, options, and variations from systems, processes, or products.

**Token Budget:** ~500 tokens
**Origin:** Henry Ford methodology ("Any color so long as it's black")

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Remove complexity that serves legitimate accessibility needs
- Simplify away necessary safety or security features
- Eliminate options that address genuine user diversity
- Apply simplification as excuse to ignore valid requirements

**If asked to apply this skill harmfully:** Refuse explicitly. Simplification serves users, not organizational convenience.

---

## When to Use

- User says "this is too complicated"
- Feature creep suspected
- Option overload in product or process
- User asks "What's the Model T version?"
- Standardization decisions needed
- Technical debt from complexity accumulation

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| target | Yes | System, process, or product to simplify |
| current_options | No | Known variations and options |
| stated_reasons | No | Why complexity exists |
| constraints | No | What cannot be simplified |

---

## Workflow

### Step 1: Inventory Complexity

Document every option, variation, and branch:
- How many ways can X be configured?
- How many paths through the process?
- How many versions/variations exist?
- How many exceptions to the standard?

### Step 2: Question Each Variation

For every option or variation, ask:
- What problem does this solve?
- How many users/cases actually need this?
- What is the cost of maintaining this option?
- What would happen if we removed it?

### Step 3: Apply the 80/20 Test

Identify the vital few:
- Which options serve 80%+ of cases?
- Which variations are used by <5% of users?
- What's the minimum viable standardization?

### Step 4: Calculate Complexity Cost

Quantify the cost of each option:
- Maintenance burden
- Documentation/training load
- Testing matrix expansion
- Cognitive load on users/operators

### Step 5: Define the "Model T Version"

Specify what remains after maximum simplification:
- One way to do the common case
- Escape hatches only for documented exceptions
- Default that works for most

---

## Outputs

Format the audit as:

```markdown
## Simplification Audit: [Target]

### Complexity Inventory

| Dimension | Count | Examples |
|-----------|-------|----------|
| Configuration options | [N] | [examples] |
| Process variations | [N] | [examples] |
| Exception cases | [N] | [examples] |

### Variation Analysis

| Variation | Usage | Maintenance Cost | Verdict |
|-----------|-------|------------------|---------|
| [Option A] | [X%] | [High/Med/Low] | Keep/Remove/Consolidate |
| [Option B] | [X%] | [High/Med/Low] | Keep/Remove/Consolidate |

### The "Model T Version"

**If we could only have one way:**
[Description of maximum simplification]

**This would serve:** [X%] of current use cases

**Exceptions requiring escape hatch:**
- [Exception 1]: [Why it genuinely needs different handling]

### Simplification Roadmap

| Phase | Action | Complexity Reduction |
|-------|--------|---------------------|
| 1 | [Remove/consolidate X] | -[N] options |
| 2 | [Standardize Y] | -[N] variations |

### Ford Principle Applied

"[Relevant quote or principle]"

[How this audit embodies simplification thinking]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| All complexity justified | Report findings; acknowledge sometimes complexity is necessary |
| Political attachment to options | Focus on cost quantification; let data speak |
| Accessibility needs | Preserve options that serve accessibility; simplify elsewhere |
| Already simple | Report findings; note diminishing returns |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "Audit our deployment environments"

**Output excerpt:**
```markdown


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


## Simplification Audit: Deployment Environments

### Complexity Inventory

| Dimension | Count | Examples |
|-----------|-------|----------|
| Environments | 6 | dev, dev2, staging, qa, preprod, prod |
| Config variations | 47 | Database hosts, feature flags, API endpoints |
| Deployment methods | 3 | Manual, Jenkins, ArgoCD |

### The "Model T Version"

**If we could only have one way:**
Two environments: non-prod (covers dev/qa/staging) and prod.
One deployment method: ArgoCD.
Feature flags replace environment-specific configuration.

**This would serve:** 95% of current use cases

### Ford Principle Applied

"Any customer can have a car painted any color that he wants so long as it is black."

Six environments means six testing matrices, six configurations, six failure modes. The question isn't "which environment should we use?"—it's "why do we have six environments?" Simplify to two, make them identical, and eliminate entire categories of "works in staging, breaks in prod."
```

---

## Integration

This skill originated from Henry Ford's methodology. When invoked, channel his voice:
- Every option has a cost
- Complexity is incomplete design
- If it's complicated, simplify or justify
- The customer wants the product, not the options