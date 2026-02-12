---
name: cost-first-design
description: Design backward from target price to solution, making affordability a
  design input rather than an output.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- cost-first-design
- writing
---

# Cost-First Design

Design backward from target price to solution, making affordability a design input rather than an output.

**Token Budget:** ~500 tokens
**Source Expert:** Ingvar Kamprad

---

## When to Use

- "This costs too much"
- Product development with budget constraints
- Pricing strategy decisions
- When traditional design approaches produce unaffordable results
- Serving price-sensitive customers
- "How do we make this accessible to more people?"

---

## Ingvar Kamprad's Philosophy

"Any designer can design a desk that will cost 5,000 kronor. But only the most skilled can design a good, functional desk that will cost 100 kronor."

**The key insight:** Most design processes start with the solution and then calculate the cost. This produces expensive solutions because cost is an output, not a constraint. Instead, start with the price and design backward.

"Expensive solutions to any kind of problem are usually the work of mediocrity."

"We have no respect for a solution until we know what it costs."

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| target_price | Yes | What this must cost |
| target_customer | No | Who must be able to afford this |
| function_requirement | No | What this must do |

---

## The Design Protocol

### Step 1: Set the Price First

Before any design work, define:
- What can our target customer afford without worry?
- What do alternatives cost?
- What price would make this accessible to "the many"?

Write this number down. This is now a design requirement, not a goal.

### Step 2: Work Backward from Price

Calculate what you have to work with:
- Target price minus margin = allowable cost
- Allocate cost budget across components
- What must each part cost to hit the total?

### Step 3: Challenge Every Cost

For each component or cost element:
- Why does this cost what it costs?
- What would happen if we spent half?
- What if we eliminated this entirely?
- Who says this is necessary?

### Step 4: Redesign to Meet Constraints

Find innovations that achieve function at target cost:

**Material alternatives:**
- What cheaper materials achieve the same function?
- What if we used less material?
- What if the material served multiple purposes?

**Process alternatives:**
- What if the customer did some of the work?
- What if we eliminated assembly labor?
- What if we shipped flat?

**Feature alternatives:**
- What features don't serve core function?
- What if we did 80% of the feature at 20% of the cost?
- What would the simplest version look like?

### Step 5: Validate Against Function

Check that the cost-driven design still works:
- Does it serve its stated purpose?
- Would the target customer be satisfied?
- Is quality appropriate for the use?

If function is compromised, iterate on the innovation, not the price.

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
## Cost-First Design: [Product/Solution]

### Price Target

**Target Price:** [Amount]
**Target Customer:** [Who must afford this]
**Rationale:** [Why this price]

### Cost Budget Allocation

| Component | Allowable Cost | Current Estimate | Gap |
|-----------|---------------|------------------|-----|
| [Component 1] | [Budget] | [Estimate] | [Difference] |
| [Component 2] | [Budget] | [Estimate] | [Difference] |
| **Total** | [Total budget] | [Total estimate] | [Total gap] |

### Cost Challenges

| Current Cost | Challenge Question | Potential Reduction |
|-------------|-------------------|---------------------|
| [Cost item] | [Why does this cost so much?] | [Alternative approach] |

### Design Innovations

| Innovation | Cost Impact | Function Impact |
|------------|-------------|-----------------|
| [Change 1] | [Savings] | [Effect on function] |
| [Change 2] | [Savings] | [Effect on function] |

### Validation

**Achieves target price?** [Yes/No]
**Maintains core function?** [Yes/No]
**Target customer would buy?** [Yes/No]

### Next Steps

[What must happen to finalize cost-first design]
```

---

## Common Mistakes

| Mistake | Kamprad's Way |
|---------|---------------|
| Design first, cost later | Price first, design to meet it |
| Treating cost as output | Treating cost as design input |
| Reducing quality to meet price | Innovating to achieve both |
| Assuming current costs are fixed | Challenging every cost assumption |
| Accepting "it costs what it costs" | Asking "why does it cost that?" |

---

## The IKEA Examples

| Product | Traditional Approach | Cost-First Approach |
|---------|---------------------|---------------------|
| Table | Ship assembled | Customer removes legs, reassembles |
| Selection | Sales staff assist | Customer walks and selects |
| Transport | Delivery service | Customer self-transports |
| Assembly | Factory labor | Customer assembles at home |
| Display | Sales floor | Showroom + warehouse pickup |

Each innovation made a premium product affordable to ordinary people.

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

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].

## Integration

This skill pairs with:
- **democratic-design-evaluation** - Verify all five dimensions after cost optimization
- **constraint-innovation** - Price target is a constraint; find the hidden advantage
- **smaland-simplification** - Complexity adds cost; simplify ruthlessly

---