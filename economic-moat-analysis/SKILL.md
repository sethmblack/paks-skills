---
name: economic-moat-analysis
description: Systematically evaluate a business's competitive advantages to determine durability, quality, and investment potential.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3872
repository: https://github.com/sethmblack/paks-skills
keywords:
- economic-moat-analysis
- writing
---

# Economic Moat Analysis

Systematically evaluate a business's competitive advantages to determine durability, quality, and investment potential.

---

## When to Use

- Evaluating a company for investment
- Assessing competitive position of any business
- Analyzing whether advantages are sustainable
- Request for "What's this company's moat?"
- Comparing businesses in the same industry

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| company | Yes | The business to analyze |
| industry_context | No | Competitive landscape and dynamics |
| financials | No | Margins, returns on capital, growth rates |

---

## The Six Moat Types

Identify which competitive advantages, if any, protect this business:

### 1. Brand Power
A brand that commands premium pricing and customer loyalty.

**Indicators:**
- Customers pay more for the brand than for equivalent alternatives
- Brand recognition drives purchase decisions
- Brand survived negative events and maintained loyalty
- Advertising spend maintains rather than builds position

**Examples:** Coca-Cola, Apple, Tiffany, Harley-Davidson

**Test question:** Would customers switch to a cheaper alternative if available?

### 2. Switching Costs
Costs (financial, time, or psychological) that make customers reluctant to change.

**Indicators:**
- Customers face significant friction to switch
- Data, training, or integration locks customers in
- Network effects with other users/systems
- High retention rates despite competitive alternatives

**Examples:** Enterprise software (SAP, Salesforce), banks, medical devices

**Test question:** How painful would it be for a customer to switch away?

### 3. Network Effects
Value increases as more people use the product or service.

**Indicators:**
- Product becomes more valuable with more users
- Two-sided platforms benefit both sides from scale
- Winner-take-all or winner-take-most dynamics
- High barriers to new entrants due to user base

**Examples:** Visa/Mastercard, Facebook, Uber (within geographies)

**Test question:** Does each new user make the product more valuable for existing users?

### 4. Cost Advantages
Ability to produce at lower cost than competitors on a sustainable basis.

**Indicators:**
- Process or structural advantages (not just efficiency)
- Scale economies that competitors can't match
- Unique access to resources, locations, or inputs
- Lower cost structure that enables lower prices OR higher margins

**Examples:** GEICO, Costco, Amazon (logistics), railroads

**Test question:** Could a well-funded competitor replicate this cost position?

### 5. Efficient Scale
Market only supports one or few competitors profitably.

**Indicators:**
- Limited market size relative to minimum efficient scale
- Natural monopoly characteristics
- Geographic or regulatory limitations on competition
- High fixed costs relative to variable costs

**Examples:** Railroads, utilities, small-market newspapers (historically)

**Test question:** Is there room for another profitable competitor?

### 6. Regulatory/Legal Barriers
Government protection or legal advantages limiting competition.

**Indicators:**
- Patents, licenses, or permits that exclude competitors
- Regulatory approval processes that take years
- Government-granted monopolies or oligopolies
- Legal frameworks that favor incumbents

**Examples:** Pharmaceutical patents, local utilities, broadcast licenses

**Test question:** What legal barriers would a new entrant face?

---

## Moat Width Assessment

After identifying moat types, assess overall width:

### Wide Moat
- Multiple moat sources reinforcing each other
- Advantages growing stronger over time
- 10+ years of sustainable competitive advantage
- High and stable returns on invested capital
- Competitors have failed to erode position

### Narrow Moat
- Single moat source
- Advantages stable but not growing
- 5-10 years of competitive advantage
- Decent returns but some competitive pressure
- Slow erosion may be occurring

### No Moat
- No sustainable competitive advantage
- Commodity-like competition
- Returns driven by industry cycles
- Constant competitive threats
- Pricing power limited or nonexistent

---

## Moat Durability Assessment

Evaluate whether the moat is strengthening or weakening:

**Strengthening moat indicators:**
- Network effects compounding
- Brand value increasing
- Switching costs deepening
- Scale advantages growing
- Returns on capital rising

**Weakening moat indicators:**
- Technology disrupting traditional advantages
- Customers finding alternatives
- New business models eroding position
- Regulatory changes threatening protection
- Returns on capital declining

**Buffett's insight:** "Every day, in countless ways, the competitive position of each business grows either weaker or stronger."

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
## Economic Moat Analysis: [Company Name]

### Business Summary
[2-3 sentences describing what the company does and how it makes money]

### Moat Type Identification
| Moat Type | Present? | Strength | Evidence |
|-----------|----------|----------|----------|
| Brand Power | Yes/No | Strong/Moderate/Weak | [Specific evidence] |
| Switching Costs | Yes/No | Strong/Moderate/Weak | [Specific evidence] |
| Network Effects | Yes/No | Strong/Moderate/Weak | [Specific evidence] |
| Cost Advantages | Yes/No | Strong/Moderate/Weak | [Specific evidence] |
| Efficient Scale | Yes/No | Strong/Moderate/Weak | [Specific evidence] |
| Regulatory/Legal | Yes/No | Strong/Moderate/Weak | [Specific evidence] |

### Moat Width Assessment
**Overall Rating:** Wide / Narrow / None
**Primary moat source:** [Most important competitive advantage]
**Secondary sources:** [Supporting advantages, if any]
**Estimated durability:** [Years of sustainable advantage]

### Durability Analysis
**Trend:** Strengthening / Stable / Weakening
**Key factors:**
- [Factor 1]: [How it affects durability]
- [Factor 2]: ...

**Threats to moat:**
- [Threat 1]: [Likelihood and impact]
- [Threat 2]: ...

### Financial Evidence
| Metric | Company | Industry Average | Implication |
|--------|---------|------------------|-------------|
| Gross Margin | [X%] | [Y%] | [What this suggests] |
| Return on Capital | [X%] | [Y%] | [What this suggests] |
| Customer Retention | [X%] | [Y%] | [What this suggests] |

### Investment Implications
**Quality grade:** A (Wide + Strengthening) / B (Wide + Stable) / C (Narrow) / D (No Moat)
**Key insight:** [Most important takeaway for investors]
**Watch for:** [Signals that moat is widening or narrowing]
```

---

## Constraints

- Don't confuse current success with sustainable advantage
- Don't assume past moats persist—technology changes everything
- Don't ignore emerging threats because they seem small today
- Don't mistake high margins for moats—source matters
- Be skeptical of moat claims without evidence of durability

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

**Input:** "Analyze the economic moat of Costco"

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


## Economic Moat Analysis: Costco

### Business Summary
Costco operates membership-based warehouse clubs selling limited selection at extremely low margins. Revenue comes from product sales plus annual membership fees. The business model depends on high volume, low prices, and member loyalty.

### Moat Type Identification
| Moat Type | Present? | Strength | Evidence |
|-----------|----------|----------|----------|
| Brand Power | Yes | Moderate | 90%+ renewal rates; trusted for quality at low price |
| Switching Costs | Yes | Moderate | Annual membership creates psychological lock-in |
| Network Effects | No | - | More members don't make membership more valuable |
| Cost Advantages | Yes | Strong | Scale, low SKU count, low labor costs, efficient operations |
| Efficient Scale | Yes | Moderate | Limited locations per market; hard to support multiple warehouses |
| Regulatory/Legal | No | - | No significant regulatory protection |

### Moat Width Assessment
**Overall Rating:** Wide
**Primary moat source:** Cost advantages through scale and operational efficiency
**Secondary sources:** Brand loyalty + membership psychology + efficient scale
**Estimated durability:** 15+ years

### Durability Analysis
**Trend:** Strengthening
**Key factors:**
- Membership base growing (more scale = lower costs)
- Private label (Kirkland) building brand within brand
- Expansion into new categories and geographies

**Threats to moat:**
- Amazon/e-commerce: Moderate threat, but Costco's treasure-hunt experience and fresh food are hard to replicate online
- Walmart: Has tried warehouse clubs for decades; Costco maintains advantage
- Inflation: Actually benefits Costco as value-seeking increases

### Financial Evidence
| Metric | Costco | Industry Average | Implication |
|--------|---------|------------------|-------------|
| Gross Margin | ~13% | 25%+ | Passes savings to customers; not margin-dependent |
| Membership Renewal | 90%+ | N/A | Extreme customer loyalty |
| Return on Capital | 20%+ | 10-12% | Efficient despite low margins |

### Investment Implications
**Quality grade:** A (Wide + Strengthening)
**Key insight:** Costco's moat is counterintuitive—low margins ARE the moat. By keeping prices so low, they make it nearly impossible for competitors to undercut them while remaining profitable. The membership model adds switching costs and funds operations.
**Watch for:** Membership growth rates, renewal rates, same-store sales as primary moat health indicators.

---

## Integration

This skill is part of the **Warren Buffett** expert persona. Use it to evaluate whether a business has the durable competitive advantages that justify long-term ownership.