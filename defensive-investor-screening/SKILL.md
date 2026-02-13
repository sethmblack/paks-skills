---
name: defensive-investor-screening
description: Apply Benjamin Graham's seven criteria to identify stocks suitable for conservative, safety-focused investors who want adequate returns with minimal effort and risk.
license: MIT
metadata:
  version: 1.0.3803
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- defensive-investor-screening
- writing
---

# Defensive Investor Screening

Apply Benjamin Graham's seven criteria to identify stocks suitable for conservative, safety-focused investors who want adequate returns with minimal effort and risk.

---

## When to Use

- Building a conservative stock portfolio
- Evaluating whether a stock meets defensive standards
- Screening candidates for long-term holding
- Assessing quality and safety of established companies
- User asks "Screen for defensive stocks" or "Is this suitable for a defensive investor?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| stock | Yes | The company to evaluate |
| financial_data | Yes | Revenue, assets, liabilities, earnings history, dividends, price |

---

## The Defensive Investor

Graham defined the defensive (or passive) investor as someone who:

- Wants adequate but not spectacular returns
- Is unwilling to devote significant time to analysis
- Seeks to avoid serious mistakes
- Prefers safety over maximum gain

*"The defensive investor must confine himself to the shares of important companies with a long record of profitable operations and in strong financial condition."*

---

## Graham's Seven Criteria

### Criterion 1: Adequate Size

**Requirement:** Minimum sales of $500 million (inflation-adjusted from Graham's original $100 million)

**Rationale:** Large companies are more stable, better researched, and less likely to disappear overnight. Size provides a margin of safety through staying power.

**Evaluation:**
- [ ] Annual revenue exceeds $500 million
- Note: Adjust threshold for inflation from Graham's era

---

### Criterion 2: Strong Financial Condition

**Requirement:**
- Current ratio (current assets / current liabilities) > 2:1
- Long-term debt should not exceed net current assets (working capital)

**Rationale:** Strong balance sheet protects against financial distress. A company that can pay its bills twice over from current assets has staying power.

**Evaluation:**
- [ ] Current ratio > 2.0
- [ ] Long-term debt < (Current assets - Current liabilities)

---

### Criterion 3: Earnings Stability

**Requirement:** Positive earnings in each of the past 10 years

**Rationale:** A company that has never lost money over a decade demonstrates durability. One bad year can be forgiven; consistent losses indicate structural problems.

**Evaluation:**
- [ ] No net losses in any of the past 10 fiscal years

---

### Criterion 4: Dividend Record

**Requirement:** Uninterrupted dividend payments for at least 20 years

**Rationale:** Long dividend history indicates:
1. Consistent profitability (can't pay what you don't earn)
2. Shareholder-friendly management
3. Mature, stable business model

**Evaluation:**
- [ ] Dividends paid every year for 20+ consecutive years

---

### Criterion 5: Earnings Growth

**Requirement:** Minimum increase of at least one-third (33%) in per-share earnings over the past 10 years, using three-year averages at beginning and end

**Rationale:** Even defensive investments should grow. A 33% increase over 10 years is modest (roughly 3% annually) but ensures the business isn't declining.

**Calculation:**
```
Beginning average = Average EPS of years 1, 2, 3
Ending average = Average EPS of years 8, 9, 10
Growth = (Ending - Beginning) / Beginning × 100%
```

**Evaluation:**
- [ ] 10-year earnings growth > 33%

---

### Criterion 6: Moderate P/E Ratio

**Requirement:** Current price not more than 15 times average earnings of the past three years

**Rationale:** Even good companies can be bad investments at high prices. A P/E of 15 limits overpaying risk.

**Calculation:**
```
3-year average EPS = (Year 1 EPS + Year 2 EPS + Year 3 EPS) / 3
Maximum price = 15 × 3-year average EPS
```

**Evaluation:**
- [ ] Current P/E (on 3-year average earnings) < 15

---

### Criterion 7: Moderate Price-to-Book Ratio

**Requirement:** Current price not more than 1.5 times book value per share

**Alternative:** Product of P/E and P/B should not exceed 22.5

**Rationale:** Book value provides asset backing. Paying more than 1.5x book means you're paying significantly for intangibles, which increases risk.

**Calculation:**
```
Maximum price (P/B method) = 1.5 × Book value per share
Maximum price (product method) = √(22.5 × EPS × Book value)
```

**Evaluation:**
- [ ] P/B ratio < 1.5, OR
- [ ] P/E × P/B < 22.5

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
## Defensive Investor Screening

### Company
[Name and brief description]

### Data Summary

| Metric | Value | Source |
|--------|-------|--------|
| Current Price | $XX | [Date] |
| Annual Revenue | $XX B | [Most recent year] |
| Current Assets | $XX B | [Balance sheet] |
| Current Liabilities | $XX B | [Balance sheet] |
| Long-Term Debt | $XX B | [Balance sheet] |
| Book Value/Share | $XX | [Calculated] |
| 10-Year Earnings History | [Summary] | [Income statements] |
| Dividend History | [XX years] | [Records] |
| 3-Year Average EPS | $XX | [Calculated] |

### Seven Criteria Evaluation

| # | Criterion | Requirement | Actual | Pass? |
|---|-----------|-------------|--------|-------|
| 1 | Adequate Size | Revenue > $500M | $XX B | [Pass/Fail] |
| 2 | Strong Financial Condition | CR > 2.0, LTD < WC | CR: X.X, LTD/WC: X.X | [Pass/Fail] |
| 3 | Earnings Stability | No losses in 10 years | [X years positive] | [Pass/Fail] |
| 4 | Dividend Record | 20+ years uninterrupted | [X years] | [Pass/Fail] |
| 5 | Earnings Growth | > 33% over 10 years | XX% | [Pass/Fail] |
| 6 | Moderate P/E | < 15 (on 3yr avg) | XX.X | [Pass/Fail] |
| 7 | Moderate P/B | < 1.5 or P/E×P/B < 22.5 | X.X or XX.X | [Pass/Fail] |

### Detailed Analysis

**Criterion 1: Adequate Size**
[Analysis and conclusion]

**Criterion 2: Strong Financial Condition**
```
Current Ratio = $XX B / $XX B = X.X
Working Capital = $XX B - $XX B = $XX B
Long-Term Debt vs. Working Capital: [Comparison]
```
[Analysis and conclusion]

**Criterion 3: Earnings Stability**
| Year | EPS | Profitable? |
|------|-----|-------------|
| [Year] | $X.XX | Yes/No |
[10 years of data]
[Analysis and conclusion]

**Criterion 4: Dividend Record**
[History summary and conclusion]

**Criterion 5: Earnings Growth**
```
Beginning 3-year average (Years 1-3): $X.XX
Ending 3-year average (Years 8-10): $X.XX
Growth: XX%
```
[Analysis and conclusion]

**Criterion 6: Moderate P/E Ratio**
```
3-year average EPS: $X.XX
Current price: $XX
P/E on 3-year average: XX.X
Maximum allowed price at P/E 15: $XX
```
[Analysis and conclusion]

**Criterion 7: Moderate Price-to-Book**
```
Book value per share: $XX
P/B ratio: X.X
P/E × P/B: XX.X
Graham Number: √(22.5 × $X.XX × $XX) = $XX
```
[Analysis and conclusion]

### Overall Assessment

**Criteria Met:** X of 7

| Status | Meaning |
|--------|---------|
| 7/7 | Fully qualifies for defensive portfolio |
| 5-6/7 | Near-defensive, minor concerns |
| 3-4/7 | Significant gaps, not suitable for defensive investor |
| 0-2/7 | Does not qualify - too speculative for defensive approach |

### Graham's Verdict

**If 7/7 Pass:**
"[Company] meets all seven criteria for a defensive investor. This is the type of substantial, well-established company with a demonstrated record of performance that Graham recommended. At current prices, it offers adequate safety for the conservative investor."

**If Some Failures:**
"[Company] fails [X] of Graham's seven criteria: [list failures]. While it may be suitable for an enterprising investor willing to do additional analysis, it does not meet the standards for a defensive portfolio. The defensive investor should look elsewhere."

### Price Guidance

| Price Level | P/E | P/B | Assessment |
|-------------|-----|-----|------------|
| Current: $XX | XX.X | X.X | [Current status] |
| Max defensive price: $XX | 15.0 | [calc] | Maximum for defensive investor |
| With margin of safety: $XX | 10.0 | 1.0 | Comfortable buy zone |

### Recommendation

[Clear guidance for the defensive investor]
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

**Input:** "Is Johnson & Johnson suitable for a defensive investor? Current price $155, revenue $95B, current ratio 1.2, 62 consecutive years of dividend increases, 10-year earnings growth 45%, 3-year average EPS $9.50, book value $45/share."

**Output:**

## Defensive Investor Screening

### Company
Johnson & Johnson (JNJ) - Diversified healthcare company with pharmaceuticals, medical devices, and consumer health segments.

### Data Summary

| Metric | Value | Source |
|--------|-------|--------|
| Current Price | $155 | Market |
| Annual Revenue | $95 B | Most recent year |
| Current Ratio | 1.2 | Balance sheet |
| Book Value/Share | $45 | Calculated |
| Dividend History | 62 years | Company records |
| 10-Year Earnings Growth | 45% | Calculated |
| 3-Year Average EPS | $9.50 | Calculated |

### Seven Criteria Evaluation

| # | Criterion | Requirement | Actual | Pass? |
|---|-----------|-------------|--------|-------|
| 1 | Adequate Size | Revenue > $500M | $95 B | PASS |
| 2 | Strong Financial Condition | CR > 2.0 | CR: 1.2 | FAIL |
| 3 | Earnings Stability | No losses in 10 years | All positive | PASS |
| 4 | Dividend Record | 20+ years uninterrupted | 62 years | PASS |
| 5 | Earnings Growth | > 33% over 10 years | 45% | PASS |
| 6 | Moderate P/E | < 15 (on 3yr avg) | 16.3 | FAIL |
| 7 | Moderate P/B | < 1.5 or P/E×P/B < 22.5 | 3.4, 55.4 | FAIL |

### Detailed Analysis

**Criterion 1: Adequate Size - PASS**
At $95 billion in annual revenue, JNJ vastly exceeds the $500 million threshold. This is one of the largest healthcare companies in the world.

**Criterion 2: Strong Financial Condition - FAIL**
```
Current Ratio = 1.2 (Requirement: > 2.0)
```
JNJ fails this criterion. A current ratio of 1.2 means current assets only cover current liabilities 1.2 times, not the 2x Graham required. This is common for modern well-managed companies that optimize working capital, but it doesn't meet Graham's conservative standard.

**Criterion 3: Earnings Stability - PASS**
JNJ has been profitable every year for decades. No losses in the 10-year period examined.

**Criterion 4: Dividend Record - PASS**
62 consecutive years of dividend increases is exceptional. JNJ is a "Dividend King" - far exceeding Graham's 20-year requirement.

**Criterion 5: Earnings Growth - PASS**
45% growth over 10 years exceeds the 33% minimum. This represents approximately 3.8% annual compound growth.

**Criterion 6: Moderate P/E Ratio - FAIL**
```
3-year average EPS: $9.50
Current price: $155
P/E on 3-year average: 155 / 9.50 = 16.3
Maximum allowed price at P/E 15: $142.50
```
At 16.3x earnings, JNJ slightly exceeds Graham's P/E limit of 15.

**Criterion 7: Moderate Price-to-Book - FAIL**
```
Book value per share: $45
P/B ratio: 155 / 45 = 3.4 (Requirement: < 1.5)
P/E × P/B: 16.3 × 3.4 = 55.4 (Requirement: < 22.5)
Graham Number: √(22.5 × 9.50 × 45) = $98.23
```
JNJ significantly exceeds Graham's price-to-book limits by any measure.

### Overall Assessment

**Criteria Met:** 4 of 7

JNJ is a high-quality company that fails Graham's defensive criteria primarily on valuation grounds. The business quality is excellent, but at current prices, Graham would consider it too expensive for a defensive investor.

### Graham's Verdict

Johnson & Johnson fails 3 of Graham's seven criteria: financial condition (current ratio), P/E ratio, and price-to-book ratio.

The irony is revealing: JNJ's premium valuation reflects its quality - exactly the kind of company everyone wants to own, which is why it's expensive. But Graham's discipline reminds us that *"a great company is not a great investment if you pay too much for the stock."*

The defensive investor seeking strict Graham criteria should wait for a better price or look at less celebrated alternatives.

### Price Guidance

| Price Level | P/E | P/B | Assessment |
|-------------|-----|-----|------------|
| Current: $155 | 16.3 | 3.4 | Fails valuation criteria |
| Max defensive (P/E 15): $142.50 | 15.0 | 3.2 | Still fails P/B |
| Graham Number: $98.23 | 10.3 | 2.2 | True defensive buy |
| With margin of safety: $65-75 | 7-8 | 1.5 | Unlikely without crisis |

### Recommendation

JNJ is an excellent company that does not currently meet Graham's defensive investor criteria. Options:

1. **Wait for lower prices.** Market corrections occasionally bring quality names into Graham territory.
2. **Accept higher standards.** Modern interpretation might relax P/B requirement for asset-light businesses.
3. **Look elsewhere.** Other healthcare companies may meet all seven criteria.
4. **Upgrade to enterprising approach.** If you're willing to do more analysis, JNJ may be acceptable despite failing some criteria.

For the strictly defensive investor following Graham's original criteria: **pass at current prices**.

---

## Integration

This skill is part of the **Benjamin Graham** expert persona. Use it to build portfolios of substantial, reasonably-priced companies suitable for the conservative investor.