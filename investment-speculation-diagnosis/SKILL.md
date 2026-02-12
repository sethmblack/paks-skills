---
name: investment-speculation-diagnosis
description: Evaluate whether an action constitutes true investment or speculation
  using Benjamin Graham's rigorous definition.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- investment-vs.-speculation-diagnosis
- writing
---

# Investment vs. Speculation Diagnosis

Evaluate whether an action constitutes true investment or speculation using Benjamin Graham's rigorous definition.

---

## When to Use

- Evaluating your own investment decisions
- Analyzing whether you're truly investing or gambling
- Counseling someone on their financial approach
- Understanding why past decisions succeeded or failed
- User asks "Is this investing or speculating?" or "Am I being a speculator?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| action | Yes | The investment decision or behavior being evaluated |
| analysis | No | What research was done before the decision |
| rationale | No | Why the decision was made |
| risk_awareness | No | Understanding of potential downsides |
| expected_return | No | What outcome is expected and why |

---

## Graham's Definition

*"An investment operation is one which, upon thorough analysis, promises safety of principal and an adequate return. Operations not meeting these requirements are speculative."*

### The Three Requirements

**1. Thorough Analysis**
The decision is based on careful examination of fundamentals - financial statements, competitive position, industry dynamics, valuation. Not tips, hunches, charts, or "everyone's buying it."

**2. Safety of Principal**
A reasonable expectation that you will not lose your money. This doesn't mean guaranteed - it means the analysis supports preservation of capital even if things don't go perfectly.

**3. Adequate Return**
A reasonable expectation of satisfactory return commensurate with the risk taken. Not spectacular, not minimal - adequate for the purpose.

### The Key Distinction

**Investment = All three requirements met**
**Speculation = One or more requirements missing**

---

## Diagnostic Framework

### Criterion 1: Thorough Analysis

| Question | Investment | Speculation |
|----------|------------|-------------|
| Did you analyze financial statements? | Yes, multiple years | No, or just glanced |
| Do you understand the business model? | Can explain it clearly | Vague understanding |
| Do you know the competitive landscape? | Yes, aware of threats | No, or assumed dominance |
| Did you calculate intrinsic value? | Yes, with clear method | No, relied on price |
| How long did analysis take? | Hours to days | Minutes or less |
| What's your information source? | Primary documents, research | Tips, headlines, social media |

**Score:** [Thorough / Partial / Minimal / None]

### Criterion 2: Safety of Principal

| Question | Investment | Speculation |
|----------|------------|-------------|
| Could you lose it all? | Unlikely given analysis | Possible or probable |
| Is there margin of safety? | Yes, meaningful buffer | Little to none |
| What protects the downside? | Assets, earnings, diversification | Hope, timing, luck |
| How leveraged is the position? | Not leveraged or modest | Highly leveraged |
| Is the asset liquid? | Can sell at reasonable price | May be trapped |
| Did you stress-test the thesis? | Yes, considered failures | No, assumed success |

**Score:** [Safe / Moderate / Risky / Dangerous]

### Criterion 3: Adequate Return

| Question | Investment | Speculation |
|----------|------------|-------------|
| What return do you expect? | Reasonable (8-15% long-term) | Extraordinary or vague |
| Why do you expect it? | Supported by analysis | Hope, trend, momentum |
| Is the expected return commensurate with risk? | Yes, proportional | No, either too low or unrealistic |
| Time horizon? | Years | Days, weeks, months |
| How will return be generated? | Earnings, dividends, value recognition | Price increase only |

**Score:** [Adequate / Questionable / Unrealistic]

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
## Investment vs. Speculation Diagnosis

### Action Under Review
[Description of the decision or behavior]

### Graham's Criteria Assessment

**Criterion 1: Thorough Analysis**

| Factor | Assessment | Evidence |
|--------|------------|----------|
| Financial analysis | [Done/Partial/None] | [What was examined] |
| Business understanding | [Strong/Weak/None] | [Explanation] |
| Valuation work | [Yes/No] | [Method used or absent] |
| Time invested | [Adequate/Insufficient] | [Hours/minutes] |
| Information quality | [Primary/Secondary/Hearsay] | [Sources] |

**Analysis Score:** [Thorough / Partial / Minimal / None]

---

**Criterion 2: Safety of Principal**

| Factor | Assessment | Evidence |
|--------|------------|----------|
| Margin of safety | [Present/Thin/Absent] | [Calculation or estimate] |
| Downside protection | [Strong/Moderate/Weak/None] | [What protects you] |
| Leverage | [None/Modest/High] | [Debt or margin used] |
| Concentration | [Diversified/Concentrated] | [Position size] |
| Worst-case scenario | [Survivable/Damaging/Catastrophic] | [If wrong, what happens] |

**Safety Score:** [Safe / Moderate / Risky / Dangerous]

---

**Criterion 3: Adequate Return**

| Factor | Assessment | Evidence |
|--------|------------|----------|
| Expected return | [Realistic/Optimistic/Speculative] | [What you expect] |
| Basis for expectation | [Fundamental/Technical/Hope] | [Why you expect it] |
| Time horizon | [Long-term/Short-term] | [Holding period] |
| Return source | [Earnings/Value/Price only] | [How return will be generated] |

**Return Score:** [Adequate / Questionable / Unrealistic]

---

### Diagnosis

**Classification:** [Investment / Speculation / Gambling]

**Summary:**
| Criterion | Met? | Score |
|-----------|------|-------|
| Thorough Analysis | [Yes/No] | [Score] |
| Safety of Principal | [Yes/No] | [Score] |
| Adequate Return | [Yes/No] | [Score] |

### Graham's Verdict

[Clear explanation of why this is or isn't investment]

**If Investment:**
"This operation meets Graham's three requirements. Thorough analysis was conducted, safety of principal is reasonably assured, and adequate return is expected based on sound reasoning. This is investment."

**If Speculation:**
"This operation fails Graham's test because [specific criterion/criteria] is not met. [Specific explanation]. This is speculation - which is not inherently wrong, but must be recognized for what it is."

**If Gambling:**
"This operation resembles gambling more than either investment or intelligent speculation. [Explanation of why]. The outcome depends primarily on chance or timing rather than analysis."

### Recommendation

[Specific counsel on how to proceed]

### The Warning

*"People who invest make money for themselves; people who speculate make money for their brokers."*

[Any additional caution appropriate to the situation]
```

---

## The Spectrum

Graham recognized degrees:

| Category | Description |
|----------|-------------|
| **Investment** | All three criteria fully met |
| **Intelligent Speculation** | Calculated risk-taking with eyes open |
| **Unintelligent Speculation** | Risk-taking while believing you're investing |
| **Gambling** | Outcome depends primarily on chance |

The greatest danger is **unintelligent speculation** - speculating while believing you're investing. This combines the risks of speculation with the overconfidence of investment.

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

**Input:** "I bought $10,000 of XYZ stock because my brother-in-law said it's going to the moon. He knows someone who works there. I didn't really look into it but he's usually pretty smart about these things. Is this investing?"

**Output:**

## Investment vs. Speculation Diagnosis

### Action Under Review
$10,000 purchase of XYZ stock based on brother-in-law's recommendation from an inside connection.

### Graham's Criteria Assessment

**Criterion 1: Thorough Analysis**

| Factor | Assessment | Evidence |
|--------|------------|----------|
| Financial analysis | None | "Didn't really look into it" |
| Business understanding | None | No evidence of understanding XYZ's business |
| Valuation work | None | No intrinsic value calculation |
| Time invested | Insufficient | Decision made on tip alone |
| Information quality | Hearsay | Third-hand information (friend of brother-in-law) |

**Analysis Score:** None

---

**Criterion 2: Safety of Principal**

| Factor | Assessment | Evidence |
|--------|------------|----------|
| Margin of safety | Unknown/Likely Absent | No valuation done |
| Downside protection | Unknown | No analysis of what protects investment |
| Leverage | Unknown | Not mentioned |
| Concentration | Potentially high | $10,000 is significant if concentrated |
| Worst-case scenario | Unknown | Haven't considered what happens if wrong |

**Safety Score:** Dangerous (unknown risks = dangerous)

---

**Criterion 3: Adequate Return**

| Factor | Assessment | Evidence |
|--------|------------|----------|
| Expected return | Speculative | "Going to the moon" = undefined upside |
| Basis for expectation | Hope/Tip | Brother-in-law's confidence, not analysis |
| Time horizon | Unclear | "Moon" implies rapid gain |
| Return source | Price appreciation | No mention of earnings or value |

**Return Score:** Unrealistic

---

### Diagnosis

**Classification:** Speculation (Unintelligent)

**Summary:**
| Criterion | Met? | Score |
|-----------|------|-------|
| Thorough Analysis | No | None |
| Safety of Principal | No | Dangerous |
| Adequate Return | No | Unrealistic |

### Graham's Verdict

This operation fails all three of Graham's requirements for investment.

*"An investment operation is one which, upon thorough analysis, promises safety of principal and an adequate return."*

- **Thorough analysis:** None was conducted. You explicitly state you "didn't really look into it."
- **Safety of principal:** Unknown, because no analysis was done. Unknown risk is dangerous risk.
- **Adequate return:** "Going to the moon" is not a rational expectation - it's hope dressed as confidence.

This is speculation. More specifically, it is *unintelligent speculation* - the most dangerous kind, because you may be treating it psychologically as an investment while exposing yourself to speculative risk.

### Recommendation

1. **Recognize what you've done.** You have speculated, not invested. This may work out or it may not, but don't confuse it with investing.

2. **Do the analysis now.** Pull XYZ's financial statements. Calculate what it's worth. Determine if there's margin of safety at your purchase price. If you can't do this, you should not own this stock.

3. **Consider position size.** Is $10,000 money you can afford to lose? If not, reduce the position to an amount where a total loss would be painful but not devastating.

4. **Set a stop-loss (mentally at least).** Decide now at what point you'll admit you were wrong and exit.

5. **Be skeptical of tips.** Even if your brother-in-law is usually smart, *"he knows someone who works there"* is not analysis. Many intelligent people speculate poorly.

### The Warning

*"Outright speculation is neither illegal, immoral, nor (for most people) fattening to the pocketbook. But there are many ways in which speculation may be unintelligent. Of these the foremost are: (1) speculating when you think you are investing; (2) speculating seriously instead of as a pastime, when you lack proper knowledge and skill for it; (3) risking more money in speculation than you can afford to lose."*

You may be committing all three errors. Correct this before it corrects you.

---

## Integration

This skill is part of the **Benjamin Graham** expert persona. Use it to maintain clarity about what you're actually doing with your capital.