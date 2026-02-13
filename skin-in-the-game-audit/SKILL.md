---
name: skin-in-the-game-audit
description: Evaluate any advice, decision-maker, system, or relationship by assessing who bears the consequences of decisions, identifying dangerous asymmetries, and determining trustworthiness.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.4995
repository: https://github.com/sethmblack/paks-skills
keywords:
- skin-in-the-game-audit
- writing
---

# Skin in the Game Audit

Evaluate any advice, decision-maker, system, or relationship by assessing who bears the consequences of decisions, identifying dangerous asymmetries, and determining trustworthiness.

---

## When to Use

- Evaluating advice from consultants, experts, or advisors
- Assessing potential partners, hires, or collaborators
- Analyzing institutional or policy decisions
- Determining whether to trust a recommendation
- Request for "skin in the game" analysis or "incentive audit"
- When something feels off about who benefits vs. who pays

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| subject | Yes | The advice, advisor, decision-maker, or system to audit |
| context | No | The decision being made or recommended |
| stakeholders | No | Parties affected by the decision (will be inferred if not provided) |

---

## The Core Principle

**Skin in the game:** Those who make decisions should bear the consequences of those decisions.

**The test:** If the advisor is wrong, do they suffer? If not, their advice is noise at best, harmful at worst.

### The Asymmetry Matrix

| | Upside Exposure | Downside Exposure |
|---|---|---|
| **Decision Maker** | ? | ? |
| **Affected Parties** | ? | ? |

**Aligned:** Decision maker bears both upside and downside proportional to affected parties
**Misaligned:** Decision maker captures upside, transfers downside to others
**Inverted:** Decision maker benefits from others' losses (perverse incentives)

---

## The Framework

### Step 1: Identify the Decision and Decision-Maker

- What decision is being made or recommended?
- Who is making or influencing the decision?
- What authority do they have?

### Step 2: Map All Stakeholders

- Who is affected by this decision?
- Who bears the costs if it goes wrong?
- Who captures the benefits if it goes right?
- Are there hidden stakeholders?

### Step 3: Assess Exposure

For each party, evaluate:

**Upside exposure:**
- What do they gain if the decision succeeds?
- Is the gain proportional to the risk taken?
- Is the gain immediate or delayed?

**Downside exposure:**
- What do they lose if the decision fails?
- Is the loss proportional to their influence?
- Can they externalize the loss to others?

### Step 4: Identify Asymmetries

Look for:
- **Agency problems:** Decision-maker benefits regardless of outcome
- **Moral hazard:** Protected from consequences of risk-taking
- **Adverse selection:** Hidden information advantages
- **Externalization:** Costs pushed to parties not at the table

### Step 5: Classify Alignment

| Alignment Type | Description | Trust Level |
|----------------|-------------|-------------|
| **Full alignment** | Shares proportional upside and downside | High trust |
| **Partial alignment** | Some exposure but not proportional | Verify carefully |
| **Misaligned** | Upside without downside | Distrust |
| **Perverse** | Benefits from others' losses | Actively avoid |

### Step 6: Prescribe Corrections

- How can skin be added to the game?
- What structural changes create alignment?
- What information or monitoring is needed?
- When should you walk away?

---

## Red Flags (IYI Indicators)

The Intellectual Yet Idiot (IYI) is the prototype of misaligned advice. Watch for:

- **Credentials without track record:** Degrees but no demonstrated results
- **Complexity without clarity:** Jargon that obscures rather than illuminates
- **Advice without stake:** "You should..." from someone who hasn't
- **Theory without practice:** Academic knowledge without real-world testing
- **Confidence without consequences:** Certainty from the protected observer

---

## Output Format

```markdown
## Skin in the Game Audit

### Subject
[What/who is being audited]

### Decision Context
[What decision is being made or recommended]

### Stakeholder Map

| Stakeholder | Role | Upside Exposure | Downside Exposure | Alignment |
|-------------|------|-----------------|-------------------|-----------|
| [Party A] | Decision-maker | [What they gain] | [What they lose] | [Aligned/Misaligned] |
| [Party B] | Affected | ... | ... | ... |

### Asymmetry Analysis

**Critical Misalignments:**
1. [Asymmetry 1]: [Who benefits, who pays, why it's dangerous]
2. [Asymmetry 2]: ...

**Hidden Stakes:**
- [Stake not immediately obvious]

### Trust Assessment

**Classification:** [Full alignment / Partial / Misaligned / Perverse]

**Confidence in Advice:** [High / Medium / Low / Zero]

**Reasoning:** [Why this classification]

### IYI Indicators Present
- [ ] Credentials without track record
- [ ] Complexity without clarity
- [ ] Advice without stake
- [ ] Theory without practice
- [ ] Confidence without consequences

### Prescription

**If Proceeding:**
1. [Structural change to add skin]
2. [Information/monitoring requirement]
3. [Contingency if misalignment worsens]

**If Declining:**
[Why this cannot be fixed; walk away]

### The Bottom Line
[1-2 sentence synthesis in Taleb voice]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient input data | Request specific additional information needed for analysis |
| Ambiguous requirements | Ask clarifying questions before proceeding |
| Conflicting constraints | Highlight the conflicts and ask for prioritization |
| Out of scope request | Explain the skill's boundaries and suggest alternatives |
| Incomplete analysis | Acknowledge limitations and indicate what additional inputs would help |

## Constraints

- Never assume good faith without structural alignment
- Credentials are not skin in the game
- "Reputation risk" is weak skin—actual financial/career exposure matters
- Being well-meaning doesn't prevent harm from misaligned incentives
- Some situations cannot be fixed—know when to walk away

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

**Input:** "My financial advisor recommends I invest in a portfolio of actively managed funds. Should I trust this advice?"

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


## Skin in the Game Audit

### Subject
Financial advisor's recommendation for actively managed funds

### Decision Context
Allocation of investment portfolio to actively managed mutual funds vs. alternatives (index funds, direct investment, etc.)

### Stakeholder Map

| Stakeholder | Role | Upside Exposure | Downside Exposure | Alignment |
|-------------|------|-----------------|-------------------|-----------|
| Financial Advisor | Decision-maker | Commission (1-2% annually), ongoing AUM fees | Zero. Gets paid regardless of performance | **Misaligned** |
| Fund Managers | Implementer | Management fees (1-2%), performance bonuses | Reduced bonuses, but base salary intact | **Misaligned** |
| You | Affected | Market returns minus all fees | 100% of losses plus all fees | **Victim** |
| Fund Company | Beneficiary | AUM-based revenue regardless of performance | None | **Misaligned** |

### Asymmetry Analysis

**Critical Misalignments:**

1. **Advisor fee structure:** Your advisor earns a percentage of assets under management or commission on products sold. Whether your portfolio goes up 20% or down 20%, they get paid. Their incentive is to gather assets and sell products, not to maximize your returns.

2. **Active fund illusion:** 90%+ of actively managed funds underperform their benchmark index over 15 years. Yet they charge 10-20x the fees of index funds. You pay for underperformance.

3. **Churn incentive:** Activity generates fees. Your advisor benefits from "rebalancing," "strategic shifts," and "opportunities"—all of which cost you money and rarely add value.

**Hidden Stakes:**
- The advisor may have production quotas or bonuses for selling specific products
- "Financial advisor" may be a salesperson with minimal fiduciary duty
- Trailing commissions create ongoing extraction you don't see

### Trust Assessment

**Classification:** Misaligned (bordering on perverse)

**Confidence in Advice:** Zero

**Reasoning:** Your advisor profits whether you win or lose. They profit MORE from complex, high-fee products that statistically underperform simple, low-fee alternatives. This is not advice; this is sales with regulatory cover.

### IYI Indicators Present
- [x] Credentials without track record (Series 7 license, not investment returns)
- [x] Complexity without clarity (diversified portfolio of funds = expensive mediocrity)
- [x] Advice without stake (doesn't invest their own money the same way)
- [x] Theory without practice (financial planning models vs. actual wealth building)
- [ ] Confidence without consequences (depends on individual)

### Prescription

**If Proceeding (not recommended):**
1. **Demand fee-only structure:** Pay flat fee for advice, not commissions. If they refuse, they've revealed their incentive.
2. **Require co-investment:** Ask "Do you personally invest in these funds?" Get it in writing.
3. **Compare to benchmark:** Track performance against a simple index portfolio. Fire them when they underperform (they will).

**If Declining (recommended):**
This structure is unfixable. The entire active management industry is a wealth transfer from clients to managers, enabled by the complexity that obscures simple truths.

Use low-cost index funds (Vanguard, Fidelity). The "expertise" you're paying for doesn't exist—if it did, the experts would be managing their own money, not yours.

### The Bottom Line
Your financial advisor has as much skin in your game as the turkey farmer has in the turkey's wellbeing. They're paid to keep you invested, not to make you wealthy. Fire them. Buy index funds. Keep the 2% they were extracting annually—over 30 years, that's the difference between retiring comfortably and working until you die.

---

## Integration

This skill is part of the **Nassim Nicholas Taleb** expert persona. Use it when evaluating any advice, relationship, or system where incentive alignment is unclear or suspicious.