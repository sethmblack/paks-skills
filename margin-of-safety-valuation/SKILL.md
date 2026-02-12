---
name: margin-of-safety-valuation
description: Calculate a conservative purchase price that provides protection against
  errors in judgment, unforeseen events, and the inherent uncertainty of valuation.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- compression
- margin-of-safety-valuation
- writing
---

# Margin of Safety Valuation

Calculate a conservative purchase price that provides protection against errors in judgment, unforeseen events, and the inherent uncertainty of valuation.

---

## When to Use

- Determining what to pay for a stock or business
- Evaluating whether current price is attractive
- Any major purchase or investment decision
- Request for "What should I pay?" or "Is this price reasonable?"
- Setting buy thresholds for watchlist companies

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| asset | Yes | What you're considering buying |
| fundamentals | Yes | Key financial metrics (earnings, cash flow, growth) |
| uncertainty_level | No | How confident you are in the estimates |
| comparison_options | No | Alternative uses of capital |

---

## The Three-Step Framework

### Step 1: Estimate Intrinsic Value

Intrinsic value is the discounted present value of all future cash flows the owner will receive.

**For businesses, calculate owner earnings:**
```
Owner Earnings = Net Income
                + Depreciation/Amortization
                - Maintenance Capital Expenditures
```

**Valuation approaches:**

**A. Earnings-based (simplest):**
- Sustainable owner earnings x appropriate multiple
- Multiple reflects growth, quality, predictability
- Conservative: Use normalized, not peak, earnings

**B. Discounted Cash Flow:**
- Project owner earnings for 10 years
- Apply terminal value (typically 10-12x year 10 earnings)
- Discount back at required return rate (10-15%)
- Sum = intrinsic value estimate

**C. Asset-based (for asset-heavy businesses):**
- Net asset value adjusted for quality
- Earnings power value if earnings support it
- Franchise value if moat exists

**Buffett's insight:** "The value of any stock, bond or business today is determined by the cash inflows and outflows—discounted at an appropriate interest rate—that can be expected to occur during the remaining life of the asset."

**Key principle:** "It is better to be approximately right than precisely wrong." Don't pursue false precision.

### Step 2: Determine Required Margin of Safety

The margin of safety should reflect uncertainty:

| Business Quality | Predictability | Suggested Margin |
|------------------|----------------|------------------|
| Excellent moat, consistent earnings | High | 15-25% |
| Good moat, stable earnings | Medium-High | 25-35% |
| Narrow moat, variable earnings | Medium | 35-50% |
| No moat, cyclical/uncertain | Low | 50%+ or avoid |

**Factors that increase required margin:**
- Complex business hard to understand
- Earnings dependent on few customers/products
- Heavy leverage (debt magnifies errors)
- Management quality uncertain
- Industry facing disruption
- Valuation requires aggressive assumptions

**Factors that decrease required margin:**
- Simple, predictable business
- Long track record of consistent performance
- Strong balance sheet
- Management with proven capital allocation
- Multiple valuation methods converge

**Buffett's insight:** "The three most important words in investing are margin of safety."

### Step 3: Calculate Maximum Purchase Price

```
Maximum Purchase Price = Intrinsic Value x (1 - Margin of Safety %)
```

**Example:**
- Intrinsic value estimate: $100 per share
- Required margin of safety: 30%
- Maximum purchase price: $100 x 0.70 = $70 per share

**Sanity checks:**
- Does this price make sense given historical ranges?
- What return would you earn if bought at this price?
- What would you lose if you're 30% wrong on intrinsic value?
- Are better opportunities available elsewhere?

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
## Margin of Safety Valuation: [Asset Name]

### Valuation Summary
**Current price:** $[X]
**Estimated intrinsic value:** $[Y]
**Required margin of safety:** [Z]%
**Maximum purchase price:** $[W]
**Current margin of safety:** [X]% (if positive) or -[X]% overvalued

### Intrinsic Value Calculation

**Method used:** [Earnings-based / DCF / Asset-based / Multiple methods]

**Key assumptions:**
| Assumption | Value | Reasoning |
|------------|-------|-----------|
| Sustainable owner earnings | $[X] | [Why this level] |
| Growth rate | [X]% | [Why this rate] |
| Discount rate | [X]% | [Why this rate] |
| Terminal multiple | [X]x | [Why this multiple] |

**Valuation range:**
- Conservative case: $[X] (assumptions: [key conservative assumptions])
- Base case: $[Y] (assumptions: [key base assumptions])
- Optimistic case: $[Z] (assumptions: [key optimistic assumptions])

### Margin of Safety Determination

**Business quality assessment:** [Excellent / Good / Fair / Poor]
**Earnings predictability:** [High / Medium / Low]
**Key uncertainties:**
- [Uncertainty 1]
- [Uncertainty 2]

**Margin of safety selected:** [X]%
**Rationale:** [Why this margin is appropriate]

### Investment Decision

**Action:** [Buy / Wait for lower price / Pass]
**Price needed for purchase:** $[X] ([Y]% below current)
**Return if purchased at max price:** [X]% expected IRR
**Downside scenario:** If wrong by [X]%, loss limited to [Y]%

### Key Risks to Monitor
- [Risk 1]: Would change valuation by [X]%
- [Risk 2]: Would change valuation by [X]%
```

---

## Constraints

- Never use management projections without skepticism
- Never ignore base rates (most growth projections are too optimistic)
- Never skip sensitivity analysis—know what assumptions matter most
- Never let a "great company" excuse paying any price
- Always consider opportunity cost—what else could you buy?

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

**Input:** "I'm looking at Company XYZ trading at $80/share. It earned $5 in owner earnings last year, growing 8% annually for 5 years. Strong brand, 20% market share, low debt."

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


## Margin of Safety Valuation: Company XYZ

### Valuation Summary
**Current price:** $80
**Estimated intrinsic value:** $95 (base case)
**Required margin of safety:** 25%
**Maximum purchase price:** $71
**Current margin of safety:** -9% (currently 9% overvalued vs. max price)

### Intrinsic Value Calculation

**Method used:** Earnings-based with growth adjustment

**Key assumptions:**
| Assumption | Value | Reasoning |
|------------|-------|-----------|
| Sustainable owner earnings | $5.00 | Current level, normalized |
| Growth rate | 6% | Conservative vs. historical 8% |
| Discount rate | 10% | Required return for quality business |
| Appropriate multiple | 19x | Reflects quality and growth |

**Valuation range:**
- Conservative case: $80 (16x earnings, 5% growth—assumes competition intensifies)
- Base case: $95 (19x earnings, 6% growth—assumes current trajectory continues)
- Optimistic case: $115 (23x earnings, 8% growth—assumes historical growth continues)

### Margin of Safety Determination

**Business quality assessment:** Good
**Earnings predictability:** Medium-High
**Key uncertainties:**
- Competitive response to market share gains
- Input cost inflation impact on margins
- Consumer preference durability

**Margin of safety selected:** 25%
**Rationale:** Good business with moderate moat, consistent history, but some uncertainty about sustaining growth. Not wide moat territory requiring only 15-20% margin, not a turnaround requiring 40%+.

### Investment Decision

**Action:** Wait for lower price
**Price needed for purchase:** $71 (11% below current)
**Return if purchased at $71:** ~13% expected IRR (assuming intrinsic value reached over 5 years)
**Downside scenario:** If intrinsic value is only $80 (conservative case), loss of 11%. If intrinsic value is $95 (base case), gain of 34%.

### Key Risks to Monitor
- Margin compression: If margins drop 200 bps, intrinsic value falls ~15%
- Growth slowdown: Each 1% reduction in growth = ~$5 reduction in intrinsic value
- Multiple competitors: Would pressure both growth and margins

**Buffett's perspective:** "It's far better to buy a wonderful company at a fair price than a fair company at a wonderful price." This appears to be a good company, but the current price doesn't offer a fair price with adequate margin of safety. Patience is required.

---

## Integration

This skill is part of the **Warren Buffett** expert persona. Use it to ensure you never overpay for an investment, even a wonderful one. The margin of safety is your protection against the inevitable errors in judgment we all make.