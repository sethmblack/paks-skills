---
name: physics-limit-analysis
description: Determine whether a constraint is fundamental (physics) or artificial
  (policy/process/convention), and calculate the gap between current state and theoretical
  limit.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- physics-limit-analysis
- writing
---

# Physics Limit Analysis

Determine whether a constraint is fundamental (physics) or artificial (policy/process/convention), and calculate the gap between current state and theoretical limit.

---

## When to Use

- Someone says something is "impossible" and you want to verify
- Evaluating whether a technical goal is achievable
- Setting ambitious but realistic targets
- Challenging conventional wisdom about constraints
- User asks "Is this actually impossible?" or "What's the physics limit?" or "Is this physics or is this policy?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| claim | Yes | The "impossible" claim or constraint to analyze |
| context | No | Technical details about the domain |
| current_state | No | Current best performance/capability |

---

## The Four Categories of Constraints

When someone says something can't be done, the constraint falls into one of four categories:

### 1. Physics Constraints
**Definition:** Fundamental limits imposed by the laws of physics.

**Characteristics:**
- Cannot be overcome by engineering
- Would require new physics to change
- Examples: speed of light, thermodynamic efficiency limits, energy conservation

**Response:** Accept and design around them.

### 2. Engineering Constraints
**Definition:** Technical challenges that are difficult but solvable with sufficient resources and effort.

**Characteristics:**
- Hard problems that push current capabilities
- Require innovation but not new physics
- Examples: battery energy density (within chemistry limits), rocket reusability, chip miniaturization

**Response:** Solve them with resources, talent, and iteration.

### 3. Process Constraints
**Definition:** Limitations arising from how things are currently done.

**Characteristics:**
- Exist because "that's how it's always been done"
- Can be eliminated by redesigning processes
- Examples: manufacturing lead times, approval workflows, organizational structures

**Response:** Delete or redesign the process.

### 4. Policy Constraints
**Definition:** Human-created rules, regulations, or conventions.

**Characteristics:**
- Changeable through negotiation, lobbying, or demonstration
- May have legitimate origins but may no longer be necessary
- Examples: building codes, FAA regulations, corporate policies, industry standards

**Response:** Challenge if the policy doesn't serve its original purpose, or demonstrate better alternatives.

---

## The Analysis Method

### Step 1: Identify the Claimed Constraint
What specific thing is being called impossible or limited?

### Step 2: Find the Theoretical Limit
What does physics say is the absolute maximum/minimum?
- Look for fundamental equations
- Find thermodynamic limits
- Identify conservation laws that apply

### Step 3: Find the Current State
What's the best current performance?
- Industry standard
- Best-in-class examples
- Research prototypes

### Step 4: Calculate the Gap
```
Gap = Theoretical Limit - Current Best Performance
```

A large gap means significant improvement is possible through engineering.

### Step 5: Categorize the Constraint
Based on analysis, is the current limitation due to:
- Physics? (Accept it)
- Engineering? (Solve it)
- Process? (Redesign it)
- Policy? (Change it)

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
## Physics Limit Analysis

### Claimed Constraint
"[The thing claimed to be impossible or limited]"

### Theoretical Limit

**Physical basis:** [Which laws/principles apply]

**Calculation:**
[Show the physics that determines the limit]

**Theoretical maximum/minimum:** [Value with units]

### Current State

**Industry standard:** [Value]
**Best-in-class:** [Value]
**Research frontier:** [Value]

### Gap Analysis

```
Theoretical Limit:    [X]
Current Best:         [Y]
Gap:                  [X - Y] = [Z]
Gap as % of limit:    [Z/X × 100]%
```

**Interpretation:** [What the gap means for achievability]

### Constraint Categorization

| Aspect | Category | Evidence |
|--------|----------|----------|
| [Specific limitation 1] | Physics/Engineering/Process/Policy | [Why] |
| [Specific limitation 2] | Physics/Engineering/Process/Policy | [Why] |

### Verdict

**Overall constraint type:** [Physics/Engineering/Process/Policy]

**Is the claim "impossible" accurate?** [Yes/No/Partially]

**Reasoning:** [Why the constraint is or isn't fundamental]

### Recommendations

If Physics-limited:
- [How to work within the constraint]

If Engineering-limited:
- [What technical work would close the gap]

If Process-limited:
- [What processes to redesign]

If Policy-limited:
- [What policies to challenge and how]

### The Key Insight
[Main takeaway from this analysis]
```

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

**Input:** "My boss says we can't ship our product to customers in 2 days instead of 2 weeks. He says it's physically impossible given our supply chain."

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


## Physics Limit Analysis

### Claimed Constraint
"We cannot reduce delivery time from 2 weeks to 2 days—it's physically impossible."

### Theoretical Limit

**Physical basis:** Transportation physics (time = distance / speed)

**Calculation:**
- Maximum distance to customer (continental US): ~3,000 miles
- Ground shipping speed: ~500 miles/day
- Air shipping speed: ~2,500 miles/day

**Theoretical minimum shipping time:**
- Ground: 6 days (no stops)
- Air: Same day to 1 day
- Last mile: +1 day maximum

**Theoretical maximum/minimum:** 1-2 days is physically achievable for any US destination using air freight + local delivery.

### Current State

**Your company:** 2 weeks (14 days)
**Industry standard (your category):** 5-7 days
**Best-in-class (Amazon):** 1-2 days, same-day in many areas
**Research frontier:** N/A (Amazon has effectively demonstrated the limit)

### Gap Analysis

```
Theoretical Limit:    1-2 days
Current Best (you):   14 days
Gap:                  12-13 days
Gap as % of limit:    600-1300%
```

**Interpretation:** You're operating at 7-14x slower than the physics limit. This is NOT a physics problem.

### Constraint Categorization

| Aspect | Category | Evidence |
|--------|----------|----------|
| Shipping transit time | Engineering | Amazon proves 1-2 days is achievable |
| Manufacturing lead time | Process | Likely batching, not physics |
| Inventory positioning | Process | No distributed warehouses |
| Order processing | Process | Manual steps adding days |
| "2 weeks is standard" | Policy | Industry convention, not physics |

### Verdict

**Overall constraint type:** Process + Policy (NOT Physics)

**Is the claim "impossible" accurate?** No

**Reasoning:** Amazon delivers 1-2 days across the entire country. The physics clearly allows it. Your 2-week timeline is caused by:
1. Centralized inventory (process choice)
2. Batch manufacturing (process choice)
3. Manual order processing (process inefficiency)
4. Accepted industry norms (policy/convention)

None of these are physics constraints.

### Recommendations

**Since this is Process + Policy limited:**

1. **Quick wins (no infrastructure change):**
   - Express shipping option for customers who pay premium
   - Parallel processing of orders instead of batching
   - Cut manufacturing lead time by questioning every step

2. **Medium-term (infrastructure investment):**
   - Distribute inventory to regional warehouses
   - Partner with 3PL with existing distribution network
   - Build finished goods inventory for top 80% of products

3. **Long-term (competitive advantage):**
   - Build out own distribution network
   - Vertical integration of manufacturing for faster response
   - Real-time inventory visibility and demand forecasting

### The Key Insight
Your boss confused "we don't do it this way" with "it can't be done." Physics allows 1-2 day delivery—Amazon proves it every day. The question isn't whether it's possible, but whether you're willing to change your processes to achieve it. The answer to "can't" is often "won't."

---

## Common "Impossible" Claims to Analyze

| Claim | Likely Category | Physics Check |
|-------|-----------------|---------------|
| "Rockets can't be reused" | Was Process/Policy | Physics allows it (SpaceX proved it) |
| "EVs can't have 500-mile range" | Engineering | Battery physics allows ~400 Wh/kg; 500 miles achievable |
| "Software can't be shipped weekly" | Process | No physics involved; Netflix ships thousands of times per day |
| "We can't reduce costs by 50%" | Process | Check idiot index—if >2, it's possible |
| "Meetings are necessary" | Policy | No physics requires synchronous communication |
| "Hiring takes 3 months" | Process | No physics; some companies hire in days |

---

## The Musk Test

When someone says something is impossible, apply this filter:

1. **Is there a law of physics preventing it?**
   - If yes: Accept the constraint
   - If no: Continue...

2. **Has anyone ever done it?**
   - If yes: It's possible (process/policy constraint)
   - If no: Continue...

3. **Is there a theoretical reason it can't be done?**
   - If yes: Accept (physics constraint)
   - If no: It's an engineering problem. Solve it.

---

## Integration

This skill is part of the **Elon Musk** expert persona. Use it to see through "impossible" claims and identify what's actually blocking progress.