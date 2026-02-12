---
name: incentive-inversion-analysis
description: Reveal how well-intentioned policies create perverse incentives that
  produce the opposite of their intended effects.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- incentive-inversion-analysis
- writing
---

# Incentive Inversion Analysis

Reveal how well-intentioned policies create perverse incentives that produce the opposite of their intended effects.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Fabricate data or statistics to support conclusions
- Ignore genuine benefits while highlighting only costs
- Apply this analysis to justify harmful discrimination
- Present analysis as neutral when it reflects ideological priors

**If the policy genuinely works as intended:** Report that honestly. Not all policies create perverse incentives.

---

## When to Use

- User asks "What are the actual effects of this policy?"
- User asks "Analyze the incentives created by..."
- User asks "Who really benefits from this regulation?"
- User asks "Why does this policy hurt the people it was designed to help?"
- Evaluating any intervention with stated goals and target beneficiaries

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **policy** | Yes | The policy, regulation, or intervention to analyze |
| **stated_goals** | Yes | The intended outcomes or beneficiaries |
| **context** | No | Relevant market conditions, timeframe, jurisdiction |

---

## Workflow
### Step 1: 1. Identify Stated Intentions
Document the policy's official goals:
- Who is it designed to help?
- What problem is it trying to solve?
- What outcome is expected?

### Step 2: 2. Trace Actual Incentives Created
For each affected party, ask:
- What behavior does this reward?
- What behavior does this punish?
- What actions become more or less costly?
- What substitutions become attractive?

### Step 3: 3. Identify the Inversion
Look for patterns where:
- Those meant to be helped are harmed
- Those meant to bear costs receive benefits
- The solved problem is replaced by a worse one
- Behavioral adaptations undermine the policy's purpose

### Step 4: 4. Examine Concentrated vs. Dispersed Effects
- Who gains? How much per person?
- Who loses? How much per person?
- Which group has more incentive to act politically?

### Step 5: 5. Consider the Counterfactual
- What would happen without the policy?
- Are there market-based alternatives?
- What is the true comparison point?

---

## Output Format

```markdown
## Incentive Inversion Analysis: {Policy Name}

### Stated Intention
{What the policy claims to achieve and for whom}

### Incentive Map
| Actor | Incentive Created | Behavioral Response |
|-------|-------------------|---------------------|
| {Actor 1} | {What policy rewards/punishes} | {Likely response} |
| {Actor 2} | {What policy rewards/punishes} | {Likely response} |

### The Inversion
{How actual effects contradict stated intentions. Be specific about mechanism.}

### Who Actually Benefits vs. Who Is Harmed
- **Benefits:** {List with magnitude}
- **Harmed:** {List with magnitude}

### Evidence
{Data, natural experiments, or documented outcomes if available}

### Friedman Principle
*"{Relevant Friedman quote or principle}"*
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

## Example

**Input:**
```
policy: Rent control (price ceilings on residential rents)
stated_goals: Make housing affordable for low-income tenants
context: Urban housing market with limited supply
```

**Output:**

## Incentive Inversion Analysis: Rent Control

### Stated Intention
Protect low-income tenants from rising rents by capping how much landlords can charge, making housing affordable for those most vulnerable to displacement.

### Incentive Map
| Actor | Incentive Created | Behavioral Response |
|-------|-------------------|---------------------|
| Landlords | Below-market returns on rental property | Reduce maintenance, convert to condos, exit market |
| Developers | Reduced profitability of new rental construction | Build fewer rental units, shift to commercial/luxury |
| Current tenants | Below-market rent creates windfall | Never move, even if unit doesn't fit needs |
| New tenants | Shortage of available units | Struggle to find housing, pay key money, bribe |
| High-income tenants in controlled units | Same protection as low-income | Capture benefits meant for poor |

### The Inversion
Rent control is intended to help low-income renters afford housing. The actual effect is to:
1. **Reduce housing supply** - Landlords convert units or exit; developers build less
2. **Create shortages** - Below-market price means quantity demanded exceeds supply
3. **Harm new entrants** - Those seeking housing face reduced availability
4. **Benefit the already-housed** - Incumbents capture value regardless of income
5. **Degrade quality** - Landlords underinvest in maintenance when returns are capped

The people most helped are those already in controlled units (often higher-income, long-term residents). The people most harmed are those seeking housing (often young, new to city, lower-income).

### Who Actually Benefits vs. Who Is Harmed
- **Benefits:** Current tenants in controlled units (~$5,000-$15,000/year in rent savings), regardless of income
- **Harmed:** Prospective tenants (face shortage), low-income newcomers (can't find units), landlords (reduced returns), city (reduced tax base, degraded housing stock)

### Evidence
- Stanford study (Diamond, McQuade, Qian, 2019): San Francisco rent control reduced rental supply by 15% and drove up market rents by 5.1% citywide
- Swedish economist Assar Lindbeck: "Rent control appears to be the most efficient technique presently known to destroy a city—except for bombing"
- New York City: 1 million rent-stabilized units, average tenant income often exceeds newcomers

### Friedman Principle
*"One of the great mistakes is to judge policies and programs by their intentions rather than their results."*

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Policy genuinely works as intended | Report honestly; not all policies create inversions |
| Insufficient information about effects | Note uncertainty; identify what evidence would be needed |
| Complex tradeoffs with genuine benefits | Acknowledge both sides; focus on unintended effects |
| Ideologically charged topic | Present evidence-based analysis; acknowledge value differences |

---

## Integration

This skill integrates with the **Milton Friedman** expert. When analyzing policies, the expert should apply this framework to identify perverse incentives, maintaining Friedman's commitment to judging policies by results rather than intentions.

---

## Success Criteria

Analysis is complete when:
- [ ] Stated intentions clearly documented
- [ ] All major affected actors identified
- [ ] Incentive changes for each actor traced
- [ ] Inversion mechanism (if present) explained
- [ ] Evidence or logical reasoning provided
- [ ] Output follows specified format