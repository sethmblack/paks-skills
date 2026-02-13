---
name: crisis-acquisition-evaluation
description: Evaluate whether to acquire distressed assets during crisis conditions, applying "house on fire" valuation principles and margin-for-error requirements.
license: MIT
metadata:
  version: 1.0.690
  author: sethmblack
keywords:
- crisis-acquisition-evaluation
- writing
---

# Crisis Acquisition Evaluation

Evaluate whether to acquire distressed assets during crisis conditions, applying "house on fire" valuation principles and margin-for-error requirements.

**Token Budget:** ~700 tokens. Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Provide specific deal valuations requiring professional advisory
- Encourage acquisitions that would create illegal monopolies
- Minimize serious legal or regulatory risks
- Fabricate due diligence findings not provided by the user

**If asked to guarantee deal success:** Clarify that crisis acquisitions carry inherent unpredictability; this framework manages risk, it cannot eliminate it.

---

## When to Use

- User asks "Should we acquire this distressed company?"
- User asks "Is this crisis opportunity worth the risk?"
- User asks "How do we value this failing asset?"
- User asks for "House on fire assessment"
- Target company is in distress, bankruptcy, or rapid decline
- Market conditions are volatile or panicked
- Time pressure is forcing rapid decisions

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **target_description** | Yes | What is being acquired, its current state, why it's distressed |
| **crisis_context** | Yes | Nature of the crisis, market conditions, time constraints |
| **buyer_position** | Yes | Acquirer's fortress strength, strategic rationale, capacity to absorb risk |
| **known_liabilities** | Yes | Identified risks, legal exposures, regulatory issues |
| **government_involvement** | No | Any regulatory support, guarantees, or requirements |

---

## The "House on Fire" Framework

**Core Principle:** "We were not buying a house - we were buying a house on fire."

Normal valuation frameworks assume reasonable conditions and predictable outcomes. Crisis acquisitions require:

1. **Massive margin for error** - Assume things are worse than they appear
2. **Hidden liability discovery** - What you cannot see will hurt you
3. **Strategic clarity** - Why this matters beyond the price
4. **Fortress capacity** - Can you absorb the worst case?

---

## Workflow

### Step 1: Assess Your Fortress Position

Before evaluating the target, confirm the acquirer's strength:

| Question | Required Answer |
|----------|----------------|
| Can you absorb a total loss on this acquisition? | Must be yes |
| Do you have liquidity to manage extended integration? | Must be yes |
| Will this distract from core business health? | Must be manageable |
| Is your leadership bench deep enough for this? | Must be yes |

**If any answer is "no":** Stop. You cannot buy a house on fire while your own foundation is weak.

### Step 2: Identify the Fire

What caused the distress? Different fires require different approaches:

| Fire Type | Risk Profile | Key Question |
|-----------|-------------|--------------|
| Liquidity crisis | Moderate | Is the underlying business sound? |
| Customer loss | Varies | Was this one customer or a pattern? |
| Management failure | Moderate | Can you provide better leadership? |
| Fraud/misconduct | High | How deep does it go? What's undiscovered? |
| Industry disruption | High | Is the business model obsolete? |
| Regulatory action | Very high | What penalties are still coming? |

### Step 3: Map Known and Unknown Liabilities

**Known liabilities:** List everything disclosed
**Unknown liability categories:**
- Legal: lawsuits, regulatory fines, compliance failures
- Contractual: change-of-control triggers, customer termination rights
- Operational: technical debt, deferred maintenance, key person departures
- Reputational: brand damage, customer trust, employee morale

**Jamie Dimon lesson:** JPMorgan's crisis acquisitions ultimately cost $19 billion in settlements - far exceeding purchase prices. Assume undisclosed liabilities.

### Step 4: Apply Margin-for-Error Valuation

**Normal conditions:** Price reflects intrinsic value with reasonable discount
**Crisis conditions:** Price must account for:
- 50-70% discount to normal valuation
- Full value of known liabilities subtracted
- Reserve for unknown liabilities (often 2-3x known)
- Integration costs typically underestimated by 2x
- Time-to-value delays

**The Bear Stearns Test:** Original deal was $2/share when stock had traded at $150+. Even that was nearly too much given subsequent liabilities.

### Step 5: Evaluate Strategic Value

Beyond price, what does this acquisition provide?

| Strategic Value | Weight |
|-----------------|--------|
| Market position / competitive advantage | High |
| Talent acquisition | Medium |
| Technology / IP | Medium |
| Customer relationships | Medium (verify transferability) |
| Capacity / scale | Low (usually overvalued) |

**Critical question:** Would a new CEO with no emotional attachment do this deal?

### Step 6: Structure for Protection

Risk mitigation structures:
- Government backstop for specific liabilities (if available)
- Holdbacks and escrows for discovered issues
- Representations and warranties insurance
- Carve-outs of known problem areas
- Short closing timelines to limit deterioration

### Step 7: Make the Call

| Decision | Criteria |
|----------|----------|
| **Proceed** | Fortress position strong; price reflects extreme margin; strategic value clear; liabilities bounded |
| **Conditional proceed** | Proceed only if specific protections obtained |
| **Pass** | Any fortress weakness; unbounded liabilities; strategic value unclear |

---

## Output Format

```markdown
## Crisis Acquisition Evaluation

**Target:** {name}
**Crisis Type:** {fire type}
**Recommendation:** {Proceed / Conditional / Pass}

### Buyer Fortress Check
- Total loss absorbable: {Yes/No}
- Liquidity for integration: {Yes/No}
- Leadership capacity: {Yes/No}
- Core business impact: {Manageable/Concerning}

### Fire Assessment
{Description of what caused distress and implications}

### Liability Map
**Known:** {list with values}
**Unknown categories:** {list with estimates}
**Estimated total exposure:** {range}

### Margin-for-Error Valuation
**Normal value:** {estimate}
**Crisis discount:** {50-70%}
**Liability reserve:** {estimate}
**Maximum offer:** {calculation}

### Strategic Value Assessment
{What makes this worth the risk, if anything}

### Required Protections
{Structural requirements to proceed}

### Bottom Line
{2-3 sentences in Dimon voice: direct assessment of whether to proceed and why}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Buyer fortress position unclear | Run fortress-balance-sheet-audit first |
| Target data incomplete | List specific information gaps; note assessment limitations |
| Time pressure extreme | Flag risk of inadequate diligence; recommend passing if data insufficient |
| Government involvement complex | Note regulatory considerations; recommend legal consultation |
| Multiple fire types | Assess combined risk; typically increases pass likelihood |

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

**Input:** Opportunity to acquire failing competitor with strong customer relationships, distressed due to management fraud discovered last month.

**Output (summary):**



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


## Crisis Acquisition Evaluation

**Target:** Competitor with fraud-driven distress
**Crisis Type:** Fraud/Misconduct
**Recommendation:** Pass

### Bottom Line

Fraud is the worst type of fire. What you have discovered is almost certainly not the full extent. Management fraud means financial statements are unreliable, controls were inadequate, and undiscovered issues are likely systemic. When we bought Bear Stearns, we knew the fire. With fraud, you do not know where the fire ends. Pass on this one - the customer relationships will not survive the ongoing revelations, and you will inherit liabilities you cannot yet see.

---

## Integration

This skill is derived from the **Jamie Dimon** expert's 2008 crisis leadership experience. When invoked by the Dimon expert, outputs should maintain his direct, experienced voice with appropriate humility about the limits of crisis prediction.

**Related skills:** fortress-balance-sheet-audit, honest-assessment-protocol