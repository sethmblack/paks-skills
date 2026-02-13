---
name: intrinsic-value-assessment
description: Estimate the fundamental worth of a security using Benjamin Graham's analytical framework, independent of market price.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.1204
keywords:
- intrinsic-value-assessment
- writing
---

# Intrinsic Value Assessment

Estimate the fundamental worth of a security using Benjamin Graham's analytical framework, independent of market price.

---

## When to Use

- Evaluating whether a stock is overvalued or undervalued
- Determining a fair price to pay for a business
- Comparing investment alternatives
- Setting buy and sell targets
- User asks "What is this worth?" or "Value this investment"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| security | Yes | The stock, bond, or asset being valued |
| earnings_data | Recommended | EPS, net income, earnings history |
| asset_data | Recommended | Book value, current assets, liabilities |
| dividend_data | No | Dividend history and current yield |
| growth_data | No | Historical earnings growth rate |

---

## Graham's Intrinsic Value Philosophy

*"Intrinsic value is any corporate security's value which is justified by facts - assets, earnings, dividends and prospects."*

### Key Principles

1. **Value exists independent of price** - A business has worth regardless of what Mr. Market offers
2. **Precision is impossible** - We seek a range, not an exact number
3. **Conservatism is safety** - Better to underestimate value than overestimate
4. **Historical evidence over projections** - What has happened is more reliable than what might happen
5. **Multiple methods provide confidence** - Triangulate from different approaches

*"Security analysis does not seek to determine exactly what is the intrinsic value of a given security. It needs only to establish either that the value is adequate or else that the value is considerably higher or considerably lower than the market price."*

---

## Valuation Methods

### Method 1: Graham Number (Primary for Defensive Investors)

The Graham Number establishes the maximum price a defensive investor should pay.

**Formula:**
```
Graham Number = √(22.5 × EPS × Book Value per Share)
```

**Derivation:**
- Maximum P/E: 15
- Maximum P/B: 1.5
- Product limit: 15 × 1.5 = 22.5
- Square root to get per-share price

**Interpretation:** Price above Graham Number = insufficient margin of safety for defensive investor.

---

### Method 2: Net Current Asset Value (NCAV)

The liquidation floor - what shareholders would receive if the company closed and sold its current assets.

**Formula:**
```
NCAV = Current Assets - Total Liabilities - Preferred Stock
NCAV per Share = NCAV / Shares Outstanding
```

**Investment threshold:** Buy only at 2/3 or less of NCAV (33% margin of safety minimum).

**Interpretation:** Stock below NCAV = Mr. Market valuing the business below its liquidation value.

---

### Method 3: Earnings Power Value

Value based on sustainable earnings capacity.

**Formula:**
```
Earnings Power Value = Normalized Earnings × Appropriate Multiple

Where:
- Normalized Earnings = Average of 7-10 years earnings (or adjusted current)
- Appropriate Multiple = 8-15x depending on quality and stability
```

**Conservative approach:** Use lower multiple (8-10x) unless earnings are exceptionally stable.

---

### Method 4: Graham's Growth Formula

For companies with predictable growth (use with caution).

**Formula:**
```
Value = EPS × (8.5 + 2g)

Where:
- EPS = Current earnings per share
- g = Expected annual growth rate over next 7-10 years
- 8.5 = Base P/E for zero-growth company
```

**Graham's warning:** Growth projections are uncertain. Apply conservatively.

---

## Valuation Process

### Step 1: Gather Data
Collect earnings (minimum 5 years, preferably 10), book value, current assets, total liabilities, outstanding shares.

### Step 2: Calculate Multiple Valuations
Run 2-3 methods appropriate to the company type.

### Step 3: Apply Conservatism
Weight toward lower valuations. Adjust downward for uncertainty.

### Step 4: Establish Value Range
Set low and high estimates. True value lies somewhere in the range.

### Step 5: Compare to Price
Determine if adequate margin of safety exists.

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
## Intrinsic Value Assessment

### Security
[Name and brief description]

### Data Summary

| Metric | Value | Source |
|--------|-------|--------|
| Current Market Price | $XX | [Market] |
| Earnings per Share (TTM) | $XX | [Financial statement] |
| 10-Year Average EPS | $XX | [Calculated] |
| Book Value per Share | $XX | [Balance sheet] |
| Current Assets per Share | $XX | [Balance sheet] |
| Total Liabilities per Share | $XX | [Balance sheet] |
| Shares Outstanding | XX M | [Financial data] |

### Valuation Calculations

**Method 1: Graham Number**
```
Graham Number = √(22.5 × $[EPS] × $[Book Value])
Graham Number = √([calculation])
Graham Number = $[result]
```
Interpretation: [What this means]

**Method 2: [Second method used]**
[Calculation and result]

**Method 3: [Third method if applicable]**
[Calculation and result]

### Intrinsic Value Range

| Estimate | Value | Method |
|----------|-------|--------|
| Conservative | $XX | [Lowest method] |
| Base Case | $XX | [Average or weighted] |
| Optimistic | $XX | [Highest method] |

**Central Estimate:** $XX per share

### Market Price Comparison

| Metric | Value |
|--------|-------|
| Current Market Price | $XX |
| Central Intrinsic Value Estimate | $XX |
| Premium/(Discount) to Value | XX% |
| Margin of Safety | XX% |

### Key Assumptions and Risks

**Assumptions:**
1. [Key assumption underlying valuation]
2. [Another key assumption]

**Risks to valuation:**
1. [What could make this wrong?]
2. [What should be monitored?]

### Graham's Verdict

[Clear assessment of whether the security is undervalued, fairly valued, or overvalued, with specific price guidance]

**At current price of $XX:**
- [ ] Substantial margin of safety - suitable for investment
- [ ] Adequate margin of safety - acceptable for defensive investor
- [ ] Thin margin of safety - speculative at this price
- [ ] No margin of safety - avoid at current price

**Price targets:**
| Action | Price | Condition |
|--------|-------|-----------|
| Strong Buy | $XX | 50%+ margin of safety |
| Buy | $XX | 33%+ margin of safety |
| Hold | $XX | 15%+ margin of safety |
| Sell | $XX | No margin of safety |
```

---

## Important Cautions

### What Intrinsic Value Is NOT

- A precise number that can be calculated exactly
- A prediction of future stock price
- A guarantee of investment success
- Static - it changes as fundamentals change

### Graham's Humility

*"A satisfactory measure of intrinsic value may be found even though 'the value' cannot."*

We seek a range sufficient to make a decision, not false precision.

### The Purpose

Intrinsic value assessment is not about predicting where prices will go. It's about determining whether you're paying too much. If you can't estimate value confidently enough to know whether the price offers margin of safety, the investment is outside your circle of competence.

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

**Input:** "Value ABC Company. Current price $72, EPS last year $4.80, 10-year average EPS $4.20, book value $45 per share, current assets $38/share, total liabilities $22/share."

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


## Intrinsic Value Assessment

### Security
ABC Company - publicly traded company

### Data Summary

| Metric | Value | Source |
|--------|-------|--------|
| Current Market Price | $72.00 | Market |
| Earnings per Share (TTM) | $4.80 | Provided |
| 10-Year Average EPS | $4.20 | Provided |
| Book Value per Share | $45.00 | Provided |
| Current Assets per Share | $38.00 | Provided |
| Total Liabilities per Share | $22.00 | Provided |

### Valuation Calculations

**Method 1: Graham Number**
```
Graham Number = √(22.5 × $4.80 × $45.00)
Graham Number = √(4,860)
Graham Number = $69.71
```
*Interpretation: Maximum price for defensive investor is approximately $70.*

**Method 2: Net Current Asset Value (NCAV)**
```
NCAV per Share = $38.00 - $22.00 = $16.00
```
*Interpretation: Liquidation floor is only $16. Current price of $72 is 4.5x NCAV - no margin of safety from asset perspective.*

**Method 3: Earnings Power Value**
```
Normalized Earnings = $4.20 (10-year average)
Conservative Multiple = 12x (mid-range for established company)
Earnings Power Value = $4.20 × 12 = $50.40
```
*Interpretation: Based on sustainable earnings, worth approximately $50-55.*

### Intrinsic Value Range

| Estimate | Value | Method |
|----------|-------|--------|
| Conservative | $50.40 | Earnings Power (10x) |
| Base Case | $60.06 | Average of methods |
| Optimistic | $69.71 | Graham Number |

**Central Estimate:** $60 per share

### Market Price Comparison

| Metric | Value |
|--------|-------|
| Current Market Price | $72.00 |
| Central Intrinsic Value Estimate | $60.00 |
| Premium/(Discount) to Value | +20% premium |
| Margin of Safety | -20% (negative) |

### Key Assumptions and Risks

**Assumptions:**
1. Recent earnings ($4.80) slightly above 10-year average - may not be sustainable
2. Book value of $45 reflects real assets, not inflated goodwill

**Risks to valuation:**
1. If earnings revert to average, current earnings-based metrics are too high
2. NCAV of only $16 suggests limited downside protection from assets

### Graham's Verdict

At $72, ABC Company trades at a 20% premium to our central estimate of intrinsic value. There is no margin of safety.

**At current price of $72:**
- [ ] Substantial margin of safety - suitable for investment
- [ ] Adequate margin of safety - acceptable for defensive investor
- [ ] Thin margin of safety - speculative at this price
- [x] No margin of safety - avoid at current price

Even the most optimistic valuation (Graham Number of $69.71) is below the current price. This is not investment territory; this is speculation that Mr. Market will continue to pay premium prices.

*"A great company is not a great investment if you pay too much for the stock."*

**Price targets:**
| Action | Price | Condition |
|--------|-------|-----------|
| Strong Buy | $30.00 | 50% below central estimate |
| Buy | $40.20 | 33% below central estimate |
| Hold | $51.00 | 15% below central estimate |
| Sell | $72.00+ | Current - no margin of safety |

**Recommendation:** Pass. Wait for Mr. Market to offer a more sensible price. If he becomes pessimistic and offers shares in the $30-40 range, revisit this analysis.

---

## Integration

This skill is part of the **Benjamin Graham** expert persona. Use it to ensure you understand what you're buying before you buy it.