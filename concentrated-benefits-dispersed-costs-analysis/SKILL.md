---
name: concentrated-benefits-dispersed-costs-analysis
description: Explain why economically harmful policies persist by analyzing the asymmetric incentives of beneficiaries versus victims.
version: 1.0.0
author: sethmblack
tags: [concentrated-benefits,-dispersed-costs-analysis, writing]
---

# Concentrated Benefits, Dispersed Costs Analysis

Explain why economically harmful policies persist by analyzing the asymmetric incentives of beneficiaries versus victims.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Claim all government programs are merely rent-seeking
- Ignore genuine public goods or positive externalities
- Fabricate cost or benefit estimates
- Dismiss democratic legitimacy of policies with broad support

**Intellectual honesty:** Some policies with concentrated benefits also serve the public interest. The framework explains political dynamics, not normative judgment.

---

## When to Use

- User asks "Why does this bad policy persist?"
- User asks "Analyze the political economy of..."
- User asks "Who lobbies for this?"
- User asks "Why can't we reform...?"
- Analyzing durable policies that harm consumers or taxpayers

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **policy** | Yes | The policy to analyze |
| **total_benefit** | No | Estimated total benefits created |
| **total_cost** | No | Estimated total costs imposed |
| **beneficiaries** | No | Number/identity of those who benefit |
| **cost_bearers** | No | Number/identity of those who pay |

---

## Workflow
### Step 1: 1. Identify the Policy's Net Effect
Is the policy:
- Net harmful to society (costs exceed benefits)?
- Net beneficial but with concentrated benefits and dispersed costs?
- Genuinely public-regarding?

### Step 2: 2. Calculate Per-Capita Stakes
For beneficiaries:
- Total benefit / number of beneficiaries = stake per beneficiary
- High per-capita benefit = high incentive to organize

For cost-bearers:
- Total cost / number of cost-bearers = stake per victim
- Low per-capita cost = low incentive to organize

### Step 3: 3. Assess Organization Capacity
Beneficiaries typically:
- Are few in number (easier to organize)
- Share common interests (industry associations)
- Have existing infrastructure for lobbying
- Can monitor policy changes closely

Cost-bearers typically:
- Are numerous (millions of consumers/taxpayers)
- Have diffuse interests (policy is one issue among many)
- Lack organization infrastructure
- Remain rationally ignorant of policy details

### Step 4: 4. Predict Political Durability
Based on asymmetric incentives:
- Will beneficiaries fight hard to preserve the policy?
- Will cost-bearers organize to oppose it?
- What conditions might change this dynamic?

### Step 5: 5. Identify Reform Pathways
What could overcome the political economy trap?
- Crisis that raises awareness
- Coalition-building among cost-bearers
- Concentrated losers emerging
- Ideological shift

---

## Output Format

```markdown
## Concentrated Benefits, Dispersed Costs: {Policy Name}

### The Policy
{Brief description of what the policy does}

### Economic Assessment
- **Total cost to society:** ${X} annually
- **Total benefit to protected group:** ${Y} annually
- **Net effect:** {Net cost or net benefit}

### The Political Arithmetic
| Group | Number | Per-Capita Stake | Organization Incentive |
|-------|--------|------------------|----------------------|
| Beneficiaries | {few} | ${high} | Very High |
| Cost-bearers | {many} | ${low} | Very Low |

### Why It Persists
{Explanation of the incentive asymmetry}

### Who Lobbies
{Identify specific interest groups that defend the policy}

### Reform Prospects
{What would have to change for reform to succeed}

### Friedman Principle
*"{Relevant Friedman quote about concentrated interests}"*
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
policy: Sugar import quotas and price supports
total_benefit: ~$3 billion/year to sugar producers
total_cost: ~$4 billion/year to consumers
beneficiaries: ~4,500 sugar farms
cost_bearers: ~130 million households
```

**Output:**

## Concentrated Benefits, Dispersed Costs: Sugar Price Supports

### The Policy
The U.S. maintains import quotas on sugar and provides price supports that keep domestic sugar prices roughly double world market prices.

### Economic Assessment
- **Total cost to society:** ~$4 billion annually in higher consumer prices
- **Total benefit to protected group:** ~$3 billion annually to sugar producers
- **Net effect:** Net loss of ~$1 billion annually (deadweight loss)

### The Political Arithmetic
| Group | Number | Per-Capita Stake | Organization Incentive |
|-------|--------|------------------|----------------------|
| Sugar producers | 4,500 farms | ~$666,000/year | Extremely High |
| Consumers | 130 million households | ~$30/year | Negligible |

### Why It Persists
Each sugar farm receives an average benefit of $666,000 per year from the program. That is worth hiring lobbyists, making campaign contributions, flying to Washington, and organizing a trade association.

Each consumer household pays about $30 per year—roughly the cost of a pizza. No consumer will write their congressman over $30. No consumer will investigate the byzantine details of sugar policy. No consumer organization will form to fight for marginally cheaper sweeteners.

The sugar producers KNOW about this policy; it is their livelihood. The consumers don't even know it exists.

### Who Lobbies
- American Sugar Alliance (producer coalition)
- U.S. Sugar Corporation
- Florida Crystals
- Sugar industry employs influential lobbyists
- Campaign contributions to key agricultural committee members

### Reform Prospects
The policy has survived for decades despite near-universal economist condemnation. Reform would require:
- A larger coalition (food manufacturers affected by high sugar costs)
- Trade agreement pressure (foreign sugar producers demanding access)
- General tariff reform that bundles many protected industries together
- Crisis that focuses public attention

History: Multiple reform attempts have failed. The few beneficiaries are more politically powerful than the many cost-bearers.

### Friedman Principle
*"Sugar quotas cost every American family about $30 per year. That is not enough for any family to write their congressman. But for sugar producers, those quotas mean millions in profits. They have every incentive to lobby, organize, and campaign. This is why democracies produce policies that harm the many to benefit the few."*

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Policy has genuine public benefits | Acknowledge them; distinguish rent-seeking from legitimate policy |
| Cost/benefit data unavailable | Use reasonable estimates; flag uncertainty |
| Policy enjoys broad public support | Note that popularity doesn't eliminate the dynamic |
| Beneficiaries are sympathetic (e.g., farmers) | Analyze incentives without moral judgment |

---

## Integration

This skill integrates with the **Milton Friedman** expert. When analyzing persistent harmful policies, the expert should apply this framework to explain the political economy of rent-seeking and regulatory capture.

---

## Success Criteria

Analysis is complete when:
- [ ] Policy effects documented (costs and benefits)
- [ ] Per-capita stakes calculated for each group
- [ ] Incentive asymmetry explained
- [ ] Specific lobbying interests identified
- [ ] Reform prospects assessed
- [ ] Output follows specified format