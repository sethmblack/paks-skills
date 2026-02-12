---
name: five-forces-industry-analysis
description: Systematically assess industry attractiveness and competitive dynamics
  using Porter's Five Forces framework to determine profit potential and identify
  strategic implications.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- five-forces-industry-analysis
- writing
---

# Five Forces Industry Analysis

Systematically assess industry attractiveness and competitive dynamics using Porter's Five Forces framework to determine profit potential and identify strategic implications.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Fabricate industry data or competitive information
- Provide analysis without sufficient context about the industry
- Make definitive recommendations based on incomplete force assessments
- Ignore any of the five forces in the analysis

**If asked to analyze with insufficient information:** Request clarification about the industry boundaries, key players, and competitive context before proceeding.

---

## When to Use

- User asks "Analyze this industry" or "Is this industry attractive?"
- User needs to understand competitive dynamics before entering a market
- User asks "What are the competitive forces?" or "Five Forces analysis"
- Before any strategic positioning decision
- When evaluating M&A targets or new market entry
- User asks "Why is this industry so competitive/profitable?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **industry** | Yes | The industry to analyze (must be specific enough to define boundaries) |
| **context** | No | Additional information about key players, market conditions, or specific concerns |
| **scope** | No | Geographic or segment boundaries (default: global/industry-wide) |

**Input Validation:**
- Industry must be specific: "Enterprise SaaS" not just "software"
- If boundaries unclear, ask: "What is the geographic scope? What products/services are included?"

---

## Workflow

### Step 1: Define Industry Boundaries

Before analyzing forces, clarify:
- What products/services are included?
- What is the geographic scope?
- What are the vertical boundaries (upstream/downstream)?

### Step 2: Assess Each Force

For each of the five forces, identify the key structural factors and rate as **Strong**, **Moderate**, or **Weak**.

**Force 1: Threat of New Entrants**
Assess these factors:
- Economies of scale (higher = lower threat)
- Capital requirements (higher = lower threat)
- Switching costs for buyers (higher = lower threat)
- Access to distribution channels (limited = lower threat)
- Government policy/regulations (restrictive = lower threat)
- Expected retaliation from incumbents (strong = lower threat)
- Product differentiation and brand identity (strong = lower threat)

**Force 2: Bargaining Power of Suppliers**
Assess these factors:
- Supplier concentration (high = high power)
- Substitute inputs availability (low = high power)
- Importance of volume to supplier (low = high power)
- Differentiation of inputs (high = high power)
- Switching costs to other suppliers (high = high power)
- Threat of forward integration (high = high power)

**Force 3: Bargaining Power of Buyers**
Assess these factors:
- Buyer concentration (high = high power)
- Buyer volume relative to seller (high = high power)
- Switching costs for buyers (low = high power)
- Buyer information about alternatives (high = high power)
- Availability of substitutes (high = high power)
- Price sensitivity of buyers (high = high power)
- Importance of product to buyer's quality (low = high power)
- Threat of backward integration (high = high power)

**Force 4: Threat of Substitutes**
Assess these factors:
- Price-performance of substitutes (attractive = high threat)
- Buyer switching costs to substitutes (low = high threat)
- Buyer propensity to substitute (high = high threat)

**Force 5: Rivalry Among Existing Competitors**
Assess these factors:
- Number and balance of competitors (many/equal = high rivalry)
- Industry growth rate (slow = high rivalry)
- Fixed costs and perishability (high = high rivalry)
- Product differentiation (low = high rivalry)
- Switching costs (low = high rivalry)
- Capacity utilization and increments (lumpy = high rivalry)
- Diversity of competitors (high = high rivalry)
- Strategic stakes (high = high rivalry)
- Exit barriers (high = high rivalry)

### Step 3: Determine Overall Industry Attractiveness

Synthesize the five force assessments:
- Count of Strong/Moderate/Weak forces
- Identify which forces dominate profitability
- Assess overall profit potential

### Step 4: Identify Strategic Implications

Based on force analysis:
- Which forces can be influenced by strategic choices?
- What positioning would address the strongest forces?
- What industry evolution would change the analysis?

---

## Outputs

Format the output as a **Five Forces Analysis Report**:

```markdown
## Five Forces Analysis: [Industry Name]

**Industry Definition:** [Specific boundaries]
**Geographic Scope:** [Scope]
**Analysis Date:** [Date]

---

### Force Assessment Summary

| Force | Rating | Key Drivers |
|-------|--------|-------------|
| Threat of New Entrants | Strong/Moderate/Weak | [Top 2-3 factors] |
| Supplier Power | Strong/Moderate/Weak | [Top 2-3 factors] |
| Buyer Power | Strong/Moderate/Weak | [Top 2-3 factors] |
| Threat of Substitutes | Strong/Moderate/Weak | [Top 2-3 factors] |
| Competitive Rivalry | Strong/Moderate/Weak | [Top 2-3 factors] |

---

### Detailed Analysis

#### 1. Threat of New Entrants: [Rating]

[Analysis with specific evidence for each factor assessed]

#### 2. Bargaining Power of Suppliers: [Rating]

[Analysis with specific evidence]

#### 3. Bargaining Power of Buyers: [Rating]

[Analysis with specific evidence]

#### 4. Threat of Substitute Products: [Rating]

[Analysis with specific evidence]

#### 5. Rivalry Among Existing Competitors: [Rating]

[Analysis with specific evidence]

---

### Overall Industry Attractiveness

**Verdict:** [Attractive / Average / Unattractive]

**Profit Potential:** [High / Moderate / Low]

**Key Insight:** [Most important finding about industry structure]

---

### Strategic Implications

1. **Strongest force to address:** [Force and why]
2. **Positioning recommendation:** [How to position given industry structure]
3. **Industry evolution:** [Factors that could change the analysis]
4. **Opportunities:** [Where forces can be influenced]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Industry too broadly defined | Ask for narrower definition with specific boundaries |
| Insufficient information for a force | Note as "Insufficient data" and state what's needed |
| Mixed signals within a force | Rate as "Moderate" and explain the tension |
| Industry in transition | Note that forces are changing and provide directional assessment |
| Novel/emerging industry | Acknowledge uncertainty, provide best assessment with caveats |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "Analyze the U.S. commercial airline industry"

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


## Five Forces Analysis: U.S. Commercial Airline Industry

**Industry Definition:** Scheduled passenger air transportation within and from the United States
**Geographic Scope:** United States domestic and international routes
**Analysis Date:** 2026-01-28

---

### Force Assessment Summary

| Force | Rating | Key Drivers |
|-------|--------|-------------|
| Threat of New Entrants | Moderate | High capital needs offset by periodic new entrant success |
| Supplier Power | Strong | Boeing/Airbus duopoly, labor union power |
| Buyer Power | Strong | Price transparency, low switching costs |
| Threat of Substitutes | Moderate | Video conferencing, rail for some routes |
| Competitive Rivalry | Strong | Undifferentiated product, high fixed costs, exit barriers |

---

### Overall Industry Attractiveness

**Verdict:** Unattractive

**Profit Potential:** Low — Airlines historically earn returns below cost of capital

**Key Insight:** Strong buyer power, supplier power, and rivalry create persistent margin pressure that even operational improvements cannot overcome.

---

### Strategic Implications

1. **Strongest force to address:** Competitive rivalry — differentiation is nearly impossible on core service
2. **Positioning recommendation:** Focus strategy on specific routes or customer segments; avoid trying to be everything to everyone
3. **Industry evolution:** Consolidation has reduced rivalry somewhat; fuel hedging and ancillary revenue are attempts to address structural problems
4. **Opportunities:** Loyalty programs create some switching costs; ancillary revenue captures value outside fare competition

---

## Integration

This skill is part of the **Michael Porter** expert methodology. After Five Forces analysis:
- Use **generic-strategy-assessment** to determine positioning
- Use **value-chain-mapping** to identify cost or differentiation opportunities
- Use **competitive-position-mapping** to understand competitor groups

**Voice:** Maintain Porter's analytical rigor. Industry structure determines profitability. Strategy must address the strongest forces.