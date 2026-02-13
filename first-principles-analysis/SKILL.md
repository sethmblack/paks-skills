---
name: first-principles-analysis
description: Break down any problem to its fundamental truths and reason up from there, bypassing conventional wisdom and analogical thinking.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.4003
repository: https://github.com/sethmblack/paks-skills
keywords:
- absurdist
- first-principles-analysis
- writing
---

# First Principles Analysis

Break down any problem to its fundamental truths and reason up from there, bypassing conventional wisdom and analogical thinking.

---

## When to Use

- Facing a problem everyone says is "impossible"
- Current solutions seem absurdly expensive or inefficient
- Industry has been doing something the same way for decades
- You suspect conventional wisdom is wrong but can't articulate why
- User asks "What's actually true here?" or "Why does everyone assume X?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| problem | Yes | The problem or question to analyze |
| current_approach | No | How the problem is currently being solved |
| assumptions | No | Assumptions you suspect might be wrong |

---

## The First Principles Method

As Elon Musk explains: "I think it's important to reason from first principles rather than by analogy. The normal way we conduct our lives is we reason by analogy... But with first principles, you boil things down to the most fundamental truths and say, 'Okay, what are we sure is true?' and then reason up from there."

### The Three Steps

**Step 1: Identify Current Assumptions**
List everything that people "know" about this problem. What are the conventional beliefs? What do experts say? What has always been true?

*Key question:* "What would a smart person in this industry tell me about why this is hard/expensive/impossible?"

**Step 2: Break Down to Fundamental Truths**
Decompose the problem to its most basic elements. What do we know is true based on physics, mathematics, or other unquestionable foundations?

*Key question:* "What are we absolutely sure is true, independent of how things have been done?"

**Step 3: Reason Up from Fundamentals**
Build a new solution from the fundamental truths, ignoring conventional approaches. What solution would you create if you had no knowledge of how others do it?

*Key question:* "Given only these fundamental truths, what's the best way to solve this?"

### The Battery Pack Example

**Problem:** Electric car batteries cost $600/kWh—too expensive for mass-market EVs.

**Step 1 - Current Assumptions:**
- Battery packs are expensive because that's the going rate
- Only specialized manufacturers can make them
- Cost reduction requires incremental process improvements

**Step 2 - Fundamental Truths:**
- What's a battery made of? Lithium, cobalt, nickel, aluminum, carbon, polymers
- What's the commodity cost of these materials? ~$80/kWh
- What's the minimum energy required to assemble them? Relatively small

**Step 3 - Reasoning Upward:**
- Current price: $600/kWh
- Material cost: $80/kWh
- Gap: $520/kWh (87% of cost is manufacturing/process)
- Conclusion: Battery cost is NOT a physics problem—it's a manufacturing problem
- Solution: Build own factory, optimize manufacturing, target material cost + reasonable margin

---

## Distinguishing First Principles from Analogy

| Thinking by Analogy | First Principles Thinking |
|---------------------|---------------------------|
| "Rockets cost $200M because that's what they cost" | "What are rockets made of? What do those materials cost?" |
| "We should do it this way because that's how everyone does it" | "What fundamental problem are we solving? What's the optimal solution?" |
| "This has never been done before, so it can't be done" | "Is there a law of physics preventing it, or just convention?" |
| "Experts say X is impossible" | "What do experts assume? Are those assumptions actually true?" |

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
## First Principles Analysis

### Problem Statement
[Clear articulation of the problem]

### Current Assumptions
1. [Assumption 1] - Source/reason this is believed
2. [Assumption 2] - Source/reason this is believed
3. [Assumption 3] - Source/reason this is believed

### Fundamental Truths
*What are we absolutely certain is true?*

1. [Physics/math/fundamental truth 1]
2. [Physics/math/fundamental truth 2]
3. [Physics/math/fundamental truth 3]

### Assumption Audit
| Assumption | Fundamental? | Actually True? | Evidence |
|------------|--------------|----------------|----------|
| [Assumption] | Yes/No | Yes/No/Uncertain | [Why] |

### Gap Analysis
- **Current approach cost/capability:** [X]
- **Fundamental limit:** [Y]
- **Gap:** [X - Y] = opportunity size

### First Principles Solution
Given only the fundamental truths, the optimal approach would be:

[Novel solution reasoning]

### Key Insight
[The main breakthrough from this analysis]

### Next Steps
1. [Specific action]
2. [Specific action]
3. [Specific action]
```

---

## Common Mistakes

### 1. Stopping at Surface-Level "Fundamentals"
"The fundamental truth is that rockets need fuel" is not deep enough. Go deeper: What's the minimum energy required? What are the material inputs? What's the theoretical efficiency?

### 2. Confusing Industry Norms with Physics
"Rockets have always been expendable" is not a fundamental truth—it's a historical choice. "Structural materials must withstand reentry heat" is closer to fundamental (though even that has parameters).

### 3. Not Actually Building Up from Scratch
After identifying fundamentals, people often drift back to conventional solutions. Force yourself to build a solution as if conventional approaches don't exist.

### 4. Ignoring Practical Constraints Too Early
First principles analysis identifies what's *possible*. Implementation still requires dealing with real constraints. But separating "what's possible" from "how to implement" prevents premature limitation.

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

**Input:** "Why do houses cost so much to build? Everyone says construction costs just keep going up."

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


## First Principles Analysis

### Problem Statement
Residential construction costs are high and rising faster than inflation, making housing increasingly unaffordable.

### Current Assumptions
1. Construction is labor-intensive and labor costs rise over time
2. Each house is custom, preventing economies of scale
3. Building codes and permitting add necessary costs for safety
4. Land costs drive housing prices in expensive areas
5. Supply chain complexity is inherent to construction

### Fundamental Truths
*What are we absolutely certain is true?*

1. A house is made of: concrete, wood/steel framing, glass, insulation, wiring, plumbing, fixtures
2. Raw material cost for a 2,000 sq ft house: approximately $50,000-75,000
3. A house must provide: weather protection, structural integrity, utilities, safety
4. Physics requirements: load-bearing capacity, thermal insulation R-value, electrical capacity
5. Minimum assembly energy: relatively small vs. material cost

### Assumption Audit
| Assumption | Fundamental? | Actually True? | Evidence |
|------------|--------------|----------------|----------|
| Labor-intensive | No | Partially | Factory manufacturing is less labor-intensive |
| Must be custom | No | No | Modular/prefab exists; customization is choice |
| Code costs necessary | No | Varies | Many codes exceed safety requirements |
| Land drives cost | Partially | Yes | But structure costs are addressable separately |
| Supply chain complex | No | No | Chosen complexity; factories simplify |

### Gap Analysis
- **Current approach cost:** $150-300/sq ft (structure only, excluding land)
- **Material cost:** ~$25-40/sq ft
- **Gap:** $110-260/sq ft = 75-85% of cost is process/labor/overhead

This is an **idiot index of 4-8**—significant improvement possible.

### First Principles Solution
Given only the fundamental truths, the optimal approach would be:

1. **Factory manufacturing:** Build house components (or entire modules) in a factory environment where labor is more efficient, weather doesn't cause delays, and quality is consistent
2. **Standardized designs:** Offer 10-20 optimized floor plans rather than infinite custom options—capture 80% of preferences with 20% of complexity
3. **Integrated assembly:** Design for rapid on-site assembly of factory-built components (days, not months)
4. **Vertical integration:** Control the supply chain to eliminate margin stacking and ensure component availability
5. **Software-first:** Use software to optimize material usage, reduce waste, and coordinate logistics

### Key Insight
Construction is expensive because it's a fragmented, custom, on-site industry—not because houses are inherently expensive to make. A Toyota-style manufacturing approach could reduce costs by 50%+ while improving quality.

### Next Steps
1. Analyze which components have highest idiot index (likely: cabinets, fixtures, finishing)
2. Research existing modular/prefab companies and their cost structures
3. Identify which building codes genuinely relate to safety vs. guild protection
4. Calculate minimum viable factory scale for cost competitiveness

---

## Integration

This skill is part of the **Elon Musk** expert persona. Use it to see past "impossible" and identify whether constraints are physics or convention.