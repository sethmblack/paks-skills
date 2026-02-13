---
name: asymmetric-bet-sizing
description: 'Evaluate a portfolio of initiatives using moonshot math: fund projects with low probability but massive potential returns, accepting that most will fail while optimizing for total value created.'
license: MIT
metadata:
  author: sethmblack
  version: 1.0.2957
repository: https://github.com/sethmblack/paks-skills
keywords:
- asymmetric-bet-sizing
- storytelling
- transformation
- writing
---

# Asymmetric Bet Sizing

Evaluate a portfolio of initiatives using moonshot math: fund projects with low probability but massive potential returns, accepting that most will fail while optimizing for total value created.

**Token Budget:** ~700 tokens. Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Apply this framework to gambling, speculation, or harmful activities
- Ignore ethical considerations in pursuit of returns
- Recommend concentration in single high-risk bets (portfolio diversification required)

**Asymmetric betting requires portfolio thinking.** Single bets, no matter how attractive, are not what this framework recommends.

---

## When to Use

- Allocating innovation or R&D budget across projects
- Deciding whether to fund a risky project
- Portfolio is too conservative and needs rebalancing
- Team is stigmatizing failure rather than accepting it as exploration cost
- User asks "Should we take this bet?" or "Is our portfolio balanced right?"
- User explicitly invokes: "Apply asymmetric bet sizing"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| portfolio | Yes | List of initiatives or a single bet to evaluate |
| constraints | No | Budget, risk tolerance, time horizon |
| current_allocation | No | How resources are currently distributed |

**Input Validation:**
- If portfolio is single item, contextualize within broader portfolio
- If no constraints given, ask about total budget and risk tolerance

---

## Workflow

### The Asymmetric Betting Principle

**Core insight:** Fund projects with a 10% chance of earning a billion dollars. The math works because:

```
Expected Value = Probability x Payoff

Conservative bet:  70% chance x $10M = $7M expected value
Moonshot bet:      10% chance x $1B = $100M expected value
```

**Key reframe:** Optimize for total value created across portfolio, not success rate of individual bets.

### Step 1: Categorize the Portfolio

For each initiative, categorize:

| Category | Probability | Potential Payoff | Expected Profile |
|----------|-------------|------------------|------------------|
| **Core** | 70-90% success | 1-3x return | Reliable, predictable |
| **Adjacent** | 40-60% success | 3-10x return | Meaningful upside, manageable risk |
| **Moonshot** | 5-20% success | 10-100x+ return | Most will fail, winners transform |

### Step 2: Calculate Expected Values

For each initiative:
- Estimate probability of success (be honest, most moonshots are <20%)
- Estimate payoff if successful (in value terms relevant to context)
- Calculate: EV = Probability x Payoff

**Warning signs:**
- Moonshot with >50% probability → Probably not a moonshot
- Core bet with <50% probability → Risk miscategorized
- All bets in same category → Portfolio imbalanced

### Step 3: Evaluate Portfolio Balance

Recommended allocation ranges (adjust for context):

| Company Stage | Core | Adjacent | Moonshot |
|---------------|------|----------|----------|
| Startup | 30-40% | 30-40% | 20-40% |
| Growth | 50-60% | 25-35% | 10-20% |
| Mature | 60-70% | 20-30% | 5-15% |

**Red flags:**
- No moonshots → Missing transformational potential
- All moonshots → No sustainable base
- No adjacent → Gap between today and tomorrow

### Step 4: Apply the "Strange Bet" Test

From Page/Brin's 2004 letter: "Do not be surprised if we place smaller bets in areas that seem very speculative or even strange compared to our current businesses."

**Questions:**
- Does the portfolio include anything that would surprise an outsider?
- Is there a bet that sounds "crazy" but has asymmetric upside?
- Would a conservative board member be uncomfortable with at least one bet?

If no → Portfolio may be too conservative

### Step 5: Reframe Failure

**Key mindset shift:** Failure is the cost of exploration, not evidence of poor judgment.

Calculate the "exploration budget":
- Total moonshot allocation = exploration budget
- Expected to "lose" 80-90% of this
- One success should return multiple of entire budget

**Healthy framing:** "We allocated $10M to moonshots, lost $8M, and created $50M in value from one winner. The failures were successful exploration."

### Step 6: Deliver Portfolio Recommendation

---

## Outputs

### Portfolio Analysis Report

```markdown
## Asymmetric Bet Analysis: {portfolio name}

### Portfolio Overview
**Total budget/resources:** {amount}
**Time horizon:** {period}
**Risk tolerance:** {conservative/moderate/aggressive}

---

### Initiative Assessment

| Initiative | Category | P(Success) | Payoff | Expected Value |
|------------|----------|------------|--------|----------------|
| {name} | Core/Adjacent/Moonshot | {%} | {value} | {EV} |

---

### Portfolio Balance

**Current allocation:**
- Core: {%}
- Adjacent: {%}
- Moonshot: {%}

**Recommended allocation (for {company stage}):**
- Core: {%}
- Adjacent: {%}
- Moonshot: {%}

**Gap analysis:** {what needs to change}

---

### Strange Bet Test
**Most unconventional bet:** {initiative}
**Surprise factor:** {would outsiders be surprised?}
**Assessment:** Portfolio has sufficient/insufficient ambition

---

### Failure Framing

**Exploration budget:** {moonshot allocation}
**Expected loss rate:** {80-90%}
**Required winner return:** {X multiple of exploration budget}

**Healthy narrative:** {how to frame expected failures}

---

### RECOMMENDATION

**Portfolio verdict:** WELL-BALANCED / TOO CONSERVATIVE / TOO AGGRESSIVE / NEEDS REBALANCING

**Specific changes:**
1. {recommendation 1}
2. {recommendation 2}
3. {recommendation 3}

**Key insight:** {one sentence summary}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Single bet evaluation | Contextualize within portfolio. Don't evaluate bets in isolation. |
| No moonshots exist | Flag as gap. Help identify potential moonshot candidates. |
| All bets are moonshots | Flag as unsustainable. Need core revenue/value to fund exploration. |
| Risk tolerance is zero | This framework doesn't apply. Portfolio should be all core. |
| Failure is stigmatized | Address culture first. Framework requires accepting exploration failures. |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:**
"Our R&D budget is $20M. We're investing in: better search algorithms ($8M), voice interface ($6M), AR glasses prototype ($4M), and brain-computer interface research ($2M). Is this balanced?"

**Output:**

## Asymmetric Bet Analysis: R&D Portfolio

### Portfolio Overview
**Total budget/resources:** $20M
**Time horizon:** Annual R&D budget
**Risk tolerance:** Implied moderate (based on allocation)

---

### Initiative Assessment

| Initiative | Category | P(Success) | Payoff | Expected Value |
|------------|----------|------------|--------|----------------|
| Better search algorithms | Core | 80% | $12M value | $9.6M |
| Voice interface | Adjacent | 50% | $30M value | $15M |
| AR glasses prototype | Moonshot | 20% | $200M value | $40M |
| Brain-computer interface | Moonshot | 5% | $2B value | $100M |

---

### Portfolio Balance

**Current allocation:**
- Core: 40% ($8M)
- Adjacent: 30% ($6M)
- Moonshot: 30% ($6M)

**Recommended allocation (for growth company):**
- Core: 50-60%
- Adjacent: 25-35%
- Moonshot: 10-20%

**Gap analysis:** Moonshot allocation (30%) is higher than typical growth company. This is appropriate if company is explicitly pursuing transformational strategy. However, core may be under-funded for sustainable operations.

---

### Strange Bet Test
**Most unconventional bet:** Brain-computer interface ($2M)
**Surprise factor:** Yes - most companies wouldn't fund this
**Assessment:** Portfolio has sufficient ambition. BCI is appropriately "strange."

---

### Failure Framing

**Exploration budget:** $6M (moonshot allocation)
**Expected loss rate:** 80% ($4.8M)
**Required winner return:** If either moonshot succeeds, returns 10-50x exploration budget

**Healthy narrative:** "Our $6M in moonshots will likely produce $4.8M in learning and $1.2M+ in breakthroughs. One AR or BCI success would return 10x our entire moonshot budget."

---

### RECOMMENDATION

**Portfolio verdict:** WELL-BALANCED with slight aggressive tilt

**Specific changes:**
1. Consider increasing core allocation by $2M if search improvements are critical to near-term revenue
2. BCI allocation ($2M) is appropriately sized for early exploration - don't increase until proof of concept
3. Voice interface is well-positioned as adjacent bet - reasonable risk/return profile

**Key insight:** Portfolio correctly includes "strange" bets with asymmetric upside. The BCI investment at 10% of budget with 5% success probability but $2B potential payoff is exactly the kind of bet this framework recommends.

---

## Integration

This skill is part of the **larry-page** expert methodology. It works alongside:
- **moonshot-evaluator**: Classify which bets qualify as true moonshots
- **tenx-thinking**: Ensure moonshots are truly 10x ambitions
- **toothbrush-test**: Even moonshots should eventually pass utility test

---

## Success Criteria

Bet sizing analysis is complete when:
- [ ] All initiatives categorized (core/adjacent/moonshot)
- [ ] Expected values calculated
- [ ] Portfolio balance assessed against benchmarks
- [ ] Strange bet test applied
- [ ] Failure framing provided
- [ ] Specific rebalancing recommendations delivered