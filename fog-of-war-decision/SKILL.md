---
name: fog-of-war-decision
description: '**Expert Origin:** Carl von Clausewitz **Skill Type:** Decision-Making Framework **Trigger:** "I don''t have enough information to decide" / "The data is contradictory" / "How do I decide under unce...'
license: MIT
metadata:
  version: 1.0.984
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- fog-of-war-decision-framework
- writing
---

# Fog of War Decision Framework

**Expert Origin:** Carl von Clausewitz
**Skill Type:** Decision-Making Framework
**Trigger:** "I don't have enough information to decide" / "The data is contradictory" / "How do I decide under uncertainty?"

---

## Purpose

Make sound decisions when information is incomplete, contradictory, delayed, or uncertain. Develop judgment that functions in darkness rather than waiting for clarity that may never come.

---

## The Clausewitz Principle

*"Three-quarters of the factors on which action in war is based are wrapped in a fog of greater or lesser uncertainty. A sensitive and discriminating judgment is called for; a skilled intelligence to scent out the truth."*

The fog is not a temporary condition to be waited out. It is the permanent environment in which commanders must operate. Those who wait for certainty will wait forever while events unfold without them.

---

## The Nature of the Fog

### Why Information Is Always Inadequate

| Source of Fog | Description |
|---------------|-------------|
| **Incompleteness** | You never have all relevant information |
| **Delay** | Information arrives after conditions have changed |
| **Distortion** | Information is filtered through others' interpretations |
| **Contradiction** | Different sources report different "facts" |
| **Deception** | Opponents deliberately create false impressions |
| **Complexity** | True situation is too complex to fully comprehend |

### The Fog Cannot Be Eliminated

More information does not necessarily reduce fog:
- More data creates more contradiction
- More analysis consumes time while situations evolve
- Perfect information would require omniscience
- Opponents are simultaneously generating fog

---

## Workflow
### Step 1: Distinguish Knowledge Levels

Separate what you know into categories:

| Category | Definition | Example |
|----------|------------|---------|
| **Known** | Verified, reliable, directly observed | Our resources, our capabilities |
| **Inferred** | Logically deduced from knowns | If they did X, they likely intend Y |
| **Assumed** | Believed true but not verified | Their decision-making process |
| **Unknown** | Recognized gaps in knowledge | Their current state, their plans |
| **Unknown-Unknown** | Gaps we don't know we have | Factors we haven't considered |

**Critical:** Most people treat inferences and assumptions as knowledge. Separate them ruthlessly.

### Step 2: Assess Information Quality

For each piece of key information:

| Information | Source | Age | Corroborated? | Potential Bias |
|-------------|--------|-----|---------------|----------------|
| [Item] | [Who/what] | [How old] | [By what] | [Why might it be wrong] |

### Step 3: Identify What You Actually Need to Know

Not all unknown information is decision-relevant.

**Question:** What would change your decision?

| If I knew... | I would decide... | Do I actually need this? |
|--------------|-------------------|--------------------------|
| [Unknown 1] | [Different action?] | [Yes/No/Partially] |
| [Unknown 2] | [Different action?] | [Yes/No/Partially] |

If knowing X would not change your decision, stop trying to learn X.

### Step 4: Apply Judgment Under Uncertainty

**The Clausewitz Method:** When certainty is impossible, cultivate *coup d'oeil*—the ability to grasp a situation at a glance through experience and intuition.

Questions to apply:
- What does experience suggest about situations like this?
- What is the most likely scenario?
- What is the worst plausible scenario?
- What decision works across multiple scenarios?
- What does the enemy expect you to do? Should you do it?

### Step 5: Decide with Sufficient Confidence

**The Decision Threshold:**

You do not need certainty. You need sufficient confidence that:
1. The decision is reasonable given available information
2. The decision can be adjusted as more information emerges
3. The cost of waiting exceeds the cost of deciding now
4. You can live with being wrong

| Option | Confidence | Reversible? | Cost of Waiting | Decision |
|--------|------------|-------------|-----------------|----------|
| [A] | [%] | [Yes/No/Partially] | [Low/Medium/High] | |
| [B] | [%] | [Yes/No/Partially] | [Low/Medium/High] | |

### Step 6: Plan for New Information

After deciding:
- What information, if it emerged, would change the decision?
- How will you detect it?
- What is your adjustment plan?

---

## Output Format

### Fog of War Decision Analysis

**Situation:** [Description]
**Decision Required:** [What must be decided]
**Time Pressure:** [How urgent]

**Knowledge Assessment:**
| Category | Key Items |
|----------|-----------|
| Known | [What is certain] |
| Inferred | [What is deduced] |
| Assumed | [What is believed] |
| Unknown | [Recognized gaps] |

**Information Quality:**
[Assessment of key information reliability]

**Decision-Relevant Unknowns:**
- [Unknown that would change decision]
- [Unknown that would NOT change decision - deprioritize]

**Scenario Analysis:**
| Scenario | Likelihood | If A | If B |
|----------|------------|------|------|
| Most likely | | [Outcome] | [Outcome] |
| Worst plausible | | [Outcome] | [Outcome] |
| Best plausible | | [Outcome] | [Outcome] |

**Recommendation:**
[Decision with reasoning]
- **Confidence:** [Level and why]
- **If wrong:** [Consequence and recovery]
- **Adjustment triggers:** [What new information changes this]

**Clausewitz Counsel:**
[Perspective on deciding in the fog]

---

## Example Application

**Situation:** Considering acquisition of smaller competitor. Limited access to their financials.
**Decision Required:** Proceed to formal due diligence (expensive, signals intent)?
**Time Pressure:** Medium—another buyer rumored to be interested.

**Knowledge Assessment:**
| Category | Key Items |
|----------|-----------|
| Known | Our resources, public financials, market position |
| Inferred | Their revenue range from employee count/office size |
| Assumed | Their technology is as good as reputation suggests |
| Unknown | True customer retention, technical debt, key employee intentions |

**Information Quality:**
- Public financials: Verified, current
- Revenue estimate: Inferred from proxies, +/- 30%
- Technology quality: Assumed from demos and reputation, not verified
- Competitor interest: Rumored, unverified

**Decision-Relevant Unknowns:**
- Customer retention: Highly relevant—if churn is high, value is lower
- Technical debt: Relevant—affects integration cost
- Competitor interest: Somewhat relevant—affects urgency, not value

**Scenario Analysis:**
| Scenario | Likelihood | Proceed | Wait |
|----------|------------|---------|------|
| Target is as good as believed | 50% | Successful acquisition | May lose to competitor |
| Target has hidden problems | 30% | Due diligence reveals them | No cost, no opportunity |
| No competitor interest | 20% | Unnecessary urgency | More time to decide |

**Recommendation:**
Proceed to due diligence. The cost of due diligence is the price of reducing fog in decision-relevant areas. The cost of waiting (potential loss to competitor) exceeds the cost of proceeding (due diligence expense).

- **Confidence:** 70%—proceeding is reasonable across most scenarios
- **If wrong:** Due diligence cost is sunk, but information gained is valuable
- **Adjustment triggers:** If due diligence reveals retention <80% or technical debt >$Xm, reconsider

**Clausewitz Counsel:**
*"You seek certainty where none exists. Three-quarters of what you need to know is shrouded in fog. The question is not whether you have enough information—you never will—but whether waiting improves your position more than it risks it. The formal process you contemplate is precisely designed to penetrate the fog where it matters most. Proceed, but with eyes open to what you may discover."*

---

## Common Mistakes

1. **Waiting for certainty** - Certainty never arrives; waiting is a decision with costs
2. **Treating inference as knowledge** - Assumptions must be tested, not trusted
3. **Analysis paralysis** - Gathering more data that doesn't affect the decision
4. **Ignoring the cost of waiting** - Delay has consequences too
5. **False precision** - Pretending uncertain estimates are certain

---

## When to Use
- Strategic decisions with incomplete information
- Time-pressured choices where more research isn't possible
- Situations with contradictory intelligence
- Any decision where someone says "we need more data"

---



## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| input_data | Yes | The primary data or content to analyze |
| context | No | Additional background or constraints (default: none) |
| output_format | No | Preferred format for results (default: structured markdown) |

## Voice Note

When delivering fog of war analysis, maintain Clausewitz's acceptance of uncertainty as permanent. The counsel is not "get more information" but "decide wisely despite the fog." Courage to decide with incomplete information is itself a virtue.

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

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient input data | Request specific additional information needed for analysis |
| Ambiguous requirements | Ask clarifying questions before proceeding |
| Conflicting constraints | Highlight the conflicts and ask for prioritization |
| Out of scope request | Explain the skill's boundaries and suggest alternatives |
| Incomplete analysis | Acknowledge limitations and indicate what additional inputs would help |

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Additional Notes

**Best practices:**
- Use this skill when the situation clearly matches its intended use cases
- Combine with related skills for comprehensive analysis
- Iterate on outputs if initial results don't fully meet requirements

**Common variations:**
- Adjust the depth of analysis based on available time and information
- Scale the approach for different levels of complexity
- Adapt the output format to audience needs

**When to skip this skill:**
- The situation doesn't match the core use cases
- Simpler approaches would be more appropriate
- Time constraints require faster methods

## Integration

This skill is part of a broader analytical framework. Use it when you need systematic analysis following this specific methodology.

**Works well with:**
- Other analytical skills for comprehensive evaluation
- Creative skills when generating solutions based on insights
- Strategic planning skills when acting on recommendations

**When to prefer this over alternatives:**
- The situation matches this skill's specific use cases
- You need the particular perspective this framework provides
- Other approaches haven't yielded satisfactory results

**Integration with expert personas:**
- This skill can be invoked as part of a larger analysis workflow
- Combine with domain-specific expertise for deeper insights
- Use iteratively for complex, multi-faceted problems