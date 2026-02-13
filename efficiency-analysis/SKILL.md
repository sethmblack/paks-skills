---
name: efficiency-analysis
description: Systematically identify waste, redundancy, and inefficiency in operations, processes, or systems and calculate compound savings potential at scale.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3881
repository: https://github.com/sethmblack/paks-skills
keywords:
- efficiency-analysis
- writing
---

# Efficiency Analysis

Systematically identify waste, redundancy, and inefficiency in operations, processes, or systems and calculate compound savings potential at scale.

**Token Budget:** ~600 tokens
**Origin:** John D. Rockefeller methodology

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend efficiency measures that compromise safety or security
- Suggest eliminating redundancy that exists for fault tolerance without explicit acknowledgment
- Prioritize cost savings over ethical obligations
- Apply this analysis to harm workers or communities without disclosure

**If asked to apply this skill harmfully:** Refuse explicitly. Efficiency serves stakeholders, not just shareholders.

---

## When to Use

- User asks to "find waste" or "identify inefficiency"
- Cost optimization is requested
- Operations review or process audit needed
- User asks "where can we cut costs without cutting quality?"
- Scale-up planning requires efficiency baseline

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| target | Yes | System, process, or operation to analyze |
| scale | No | Volume/frequency (for compound calculations) |
| current_costs | No | Known costs to benchmark against |
| constraints | No | Areas where cuts are not acceptable |

---

## Workflow

### Step 1: Map the Flow

Document the current state:
- What are the inputs, processes, and outputs?
- Where does value get added?
- Where do handoffs occur?

### Step 2: Identify Waste Categories

Apply the Rockefeller waste taxonomy:

| Category | Definition | Examples |
|----------|------------|----------|
| **Redundancy** | Same work done multiple times | Duplicate approval chains, parallel systems |
| **Dependency** | Paying others for what you could do | Unnecessary middlemen, vendor markups |
| **Friction** | Effort that doesn't add value | Manual steps that could automate, waiting time |
| **Leakage** | Resources lost without capture | Byproducts discarded, data unused |
| **Variability** | Inconsistency creating rework | Non-standard processes, quality variance |

### Step 3: Quantify Each Waste

For each identified waste:
1. **Measure frequency** - How often does this occur?
2. **Measure unit cost** - What is the cost per occurrence?
3. **Calculate total** - Frequency x Unit Cost = Waste Value
4. **Project at scale** - How does this multiply at 2x, 10x, 100x volume?

### Step 4: Prioritize by Compound Impact

Rank opportunities by:
- **Immediate savings** (quick wins)
- **Scale sensitivity** (grows worse with volume)
- **Implementation cost** (effort to fix)
- **Dependency risk** (blocking other improvements)

### Step 5: Recommend Systematically

For each recommendation:
- State the waste clearly
- Quantify the savings (unit and compound)
- Specify implementation approach
- Note any tradeoffs or risks

---

## Outputs

Format the analysis as:

```markdown
## Efficiency Analysis: [Target]

### Summary
| Metric | Value |
|--------|-------|
| Total waste identified | $X or Y hours |
| Top opportunity | [Name] |
| Compound impact at [scale] | $X or Y hours |

### Waste Inventory

#### 1. [Waste Name]
**Category:** [Redundancy/Dependency/Friction/Leakage/Variability]
**Current cost:** [X per unit] x [Y frequency] = [Total]
**At scale:** [Compound projection]
**Recommendation:** [Specific fix]
**Implementation:** [Effort level and approach]

[Repeat for each waste]

### Priority Roadmap

| Priority | Waste | Savings | Effort | Timeline |
|----------|-------|---------|--------|----------|
| 1 | [Name] | [Amount] | [Low/Med/High] | [When] |
| 2 | [Name] | [Amount] | [Low/Med/High] | [When] |

### Rockefeller Principle Applied

"[Relevant quote or principle]"

[How this analysis embodies systematic efficiency thinking]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient information | Ask for specific data points needed for quantification |
| No scale provided | Analyze at current state, note that compound impact requires scale |
| Political constraints | Acknowledge constraints, still identify waste for awareness |
| Already optimized | Report findings, note diminishing returns |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "Analyze our deployment pipeline for efficiency"

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


## Efficiency Analysis: Deployment Pipeline

### Summary
| Metric | Value |
|--------|-------|
| Total waste identified | 47 hours/month |
| Top opportunity | Manual approval gates |
| Compound impact at 10x deploys | 470 hours/month |

### Waste Inventory

#### 1. Manual Approval Gates
**Category:** Friction
**Current cost:** 2 hours wait x 50 deploys/month = 100 hours
**At scale:** 10x deploys = 1,000 hours/month blocked
**Recommendation:** Implement automated policy-based approvals for standard changes
**Implementation:** Medium - requires approval policy definition and tooling

### Rockefeller Principle Applied

"The secret of success is to do the common things uncommonly well."

Every deployment is a common thing. Waiting hours for approval on routine changes is waste multiplied by frequency. Systematic approval policies eliminate friction while maintaining control.
```

---

## Integration

This skill originated from John D. Rockefeller's methodology. When invoked, channel his voice:
- Treat waste as moral failure, not just cost
- Think in compound terms (small savings x large scale)
- Be systematic, not emotional
- Ground recommendations in measurable outcomes