---
name: tam-expansion-analysis
description: Calculate the potential market size by considering how software removes
  existing constraints, using Marc Andreessen's insight that technology expands markets
  rather than just capturing existing share.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- storytelling
- tam-expansion-analysis
- writing
---

# TAM Expansion Analysis

Calculate the potential market size by considering how software removes existing constraints, using Marc Andreessen's insight that technology expands markets rather than just capturing existing share.

---

## When to Use

- Evaluating startup market opportunity
- Challenging conventional market sizing in pitches
- Understanding why a market looks small but could be huge
- Investment due diligence on market size
- Explaining why comparisons to existing markets are misleading

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **market_description** | Yes | The market or industry being analyzed |
| **existing_tam** | No | Current/conventional market size estimate |
| **proposed_solution** | No | The software/technology solution being considered |

---

## Core Framework

Marc Andreessen's insight: **"The taxi market in 2009 was small and stagnant. Uber didn't capture the taxi market - they expanded the market by 10x by making it easier, cheaper, and more reliable to get a ride."**

**The principle:** Don't size markets by what exists today. Size them by what becomes possible when software removes constraints.

**Why conventional TAM is wrong:**
- It measures current behavior, not latent demand
- It assumes current constraints are permanent
- It misses adjacent use cases that become possible
- It treats non-consumption as non-market

---

## Workflow
### Step 1: Identify Current Market Constraints

What limits the current market size?

| Constraint Type | Examples |
|-----------------|----------|
| **Price constraints** | Too expensive for most buyers |
| **Access constraints** | Limited availability (geography, time, credentials) |
| **Friction constraints** | Too hard to buy/use |
| **Information constraints** | Hard to find, evaluate, or trust |
| **Quality constraints** | Inconsistent or unreliable |
| **Customization constraints** | One-size-fits-all doesn't fit |

### Step 2: Assess Constraint Removal

For each constraint, ask: **What if software reduced this to near-zero?**

| Constraint | Current Impact | After Software | Market Expansion |
|------------|---------------|----------------|------------------|
| Price | X buyers | Y buyers (larger) | Y/X multiplier |
| Access | Limited reach | Universal reach | Geographic multiplier |
| Friction | High effort | Zero effort | Frequency multiplier |
| Information | Opacity | Transparency | Conversion multiplier |

### Step 3: Identify Adjacent Use Cases

What becomes possible that wasn't before?

**Questions to ask:**
- Who doesn't use this today because of constraints?
- What substitute behaviors would convert to this?
- What use cases are "too small" for current solutions?
- What becomes viable at lower price/friction?

### Step 4: Apply the Uber Pattern

**Before Uber (2009 taxi market):**
- Limited to urban areas
- Expensive
- Unreliable (can't get a cab in rain)
- Cash-only, no receipts
- No accountability
- Only used for necessity

**After Uber:**
- Available everywhere with drivers
- Variable pricing, often cheaper
- Reliable (always know a car is coming)
- Seamless payment
- Rated drivers and riders
- Used for convenience, not just necessity

**Result:** Market expanded 10x+ because:
- People took rides they wouldn't have taken before
- New use cases emerged (going out drinking, airport runs)
- People who never used taxis became regular users

### Step 5: Calculate Expanded TAM

**Formula:**
```
Expanded TAM = (Current TAM x Access Multiplier x Price Multiplier x Frequency Multiplier) + Adjacent Markets
```

**Multiplier guidance:**
| Factor | Conservative | Moderate | Aggressive |
|--------|--------------|----------|------------|
| Access | 1.5x | 3x | 10x |
| Price | 1.5x | 2x | 5x |
| Frequency | 1.5x | 2x | 3x |

### Step 6: Find Comparable Expansions

Reference similar market expansions:

| Market | Before Software | After Software | Expansion |
|--------|-----------------|----------------|-----------|
| Taxis -> Rideshare | $11B (2009) | $100B+ (2020) | ~10x |
| Hotels -> Short-term rentals | $100B | $300B+ | 3x+ |
| Retail -> E-commerce | Constrained by stores | Infinite selection | Expanding 10%+ annually |
| Music distribution | $15B physical | $25B streaming (growing) | Still expanding |

---

## Outputs

### TAM Expansion Analysis

```markdown
## TAM Expansion Analysis: [Market]

### Summary
**Conventional TAM:** $[X]
**Expanded TAM Estimate:** $[Y]
**Expansion Multiplier:** [Y/X]x
**Confidence:** High / Medium / Low

### Current Market Constraints

| Constraint | Impact on Market | Evidence |
|------------|------------------|----------|
| [Constraint 1] | [How it limits market] | [Data/observation] |
| [Constraint 2] | [How it limits market] | [Data/observation] |

### Constraint Removal Analysis

| Constraint | Current State | After Software | Market Effect |
|------------|---------------|----------------|---------------|
| [Constraint] | [Now] | [Future] | [Multiplier] |

### Adjacent Use Cases Unlocked

**Current non-consumers who would convert:**
- [Segment 1]: [Why they don't participate today]
- [Segment 2]: [Why they don't participate today]

**New use cases enabled:**
- [Use case 1]: [Why it becomes possible]
- [Use case 2]: [Why it becomes possible]

### Comparable Market Expansions

| Comparable | Before | After | Expansion | Relevance |
|------------|--------|-------|-----------|-----------|
| [Example] | $X | $Y | Nx | [Why comparable] |

### TAM Calculation

**Formula applied:**
```
Current TAM: $[X]
x Access Multiplier: [N]x
x Price Multiplier: [N]x
x Frequency Multiplier: [N]x
+ Adjacent Markets: $[Z]
= Expanded TAM: $[Y]
```

### Key Insight

[The main reason why conventional TAM understates the opportunity]

### Caveats

- [Assumption 1 that could be wrong]
- [Assumption 2 that could be wrong]
```

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
```
Market: Personal financial advisory services
Existing TAM: $50B (wealth management industry)
Proposed solution: AI-powered financial advisor accessible to everyone
```

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


## TAM Expansion Analysis: Personal Financial Advisory

### Summary
**Conventional TAM:** $50B (wealth management)
**Expanded TAM Estimate:** $200-500B
**Expansion Multiplier:** 4-10x
**Confidence:** Medium (depends on AI capability and trust)

### Current Market Constraints

| Constraint | Impact on Market | Evidence |
|------------|------------------|----------|
| Minimum account size | Only serves wealthy ($250K+ typical minimum) | 90% of Americans don't use financial advisors |
| High fees | 1% AUM prices out small accounts | $10K account = $100/year value |
| Access/appointments | Limited advisor time, inconvenient | Hours of operation, waiting for appointments |
| Trust/relationships | Takes time to build, varies by advisor | Advisor quality highly variable |
| Complexity | Advice is hard to understand | Most Americans financially illiterate |

### Constraint Removal Analysis

| Constraint | Current State | After AI Advisor | Market Effect |
|------------|---------------|------------------|---------------|
| Minimum | $250K+ | $0 | 10x more people served |
| Cost | 1% AUM | $10-50/month flat | 20x cheaper for small accounts |
| Access | Business hours | 24/7 instant | 3x more interactions |
| Trust | Variable, takes time | Consistent, immediate | Higher conversion |
| Complexity | Expert jargon | Plain language | More participation |

### Adjacent Use Cases Unlocked

**Current non-consumers who would convert:**
- **Middle class households ($50-250K assets):** 100M+ Americans who "can't afford" advisors
- **Young people:** Don't think they have enough to manage
- **Immigrants:** Often excluded from traditional financial services
- **Gig workers:** Complex finances, no employer benefits

**New use cases enabled:**
- Daily financial check-ins (vs. annual reviews)
- Real-time spending guidance
- Tax optimization throughout year (not just April)
- Life event planning on demand
- Financial education integrated with advice

### Comparable Market Expansions

| Comparable | Before | After | Expansion | Relevance |
|------------|--------|-------|-----------|-----------|
| Tax prep -> TurboTax | $10B (CPAs) | $15B+ (DIY) | 1.5x | Similar democratization |
| Stock trading -> Robinhood | $10B (commissions) | $0 commissions | Killed old revenue, grew participation 10x |
| Legal -> LegalZoom | $300B (lawyers) | $500M (DIY docs) | Small slice, but new market |

### TAM Calculation

**Formula applied:**
```
Current TAM: $50B (wealth management)
x Access Multiplier: 3x (10x more people, lower spend per person)
x Frequency Multiplier: 2x (daily vs. annual engagement)
+ Adjacent Markets: $50B (insurance, tax, lending integration)
= Expanded TAM: $350B
```

Conservative: $200B (2x access, 1.5x frequency, $50B adjacent)
Aggressive: $500B (5x access, 2x frequency, $100B adjacent)

### Key Insight

The $50B wealth management TAM dramatically understates the opportunity because it only measures people wealthy enough to use current services. Financial advice is a universal need - EVERYONE needs to manage money - but current delivery constrains it to the wealthy.

When you make financial advice free, instant, and accessible, you're not competing for the $50B - you're creating a new $200-500B market of people who never had access before.

This is the Uber pattern: the taxi market was $11B not because only $11B of rides were needed, but because taxis only served a fraction of potential riders. Same with financial advice.

### Caveats

- Assumes AI can achieve sufficient trust (major question mark)
- Regulatory barriers may limit advice scope
- Monetization model uncertain if not AUM-based
- Incumbent response (Schwab, Fidelity have resources)

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No clear constraints to remove | Market may already be efficient - expansion limited |
| Regulatory barriers | Factor into timeline, not impossibility |
| No comparable expansions | Note higher uncertainty, provide range |
| Already expanded market | Analyze next wave of expansion |

---

## Integration

This skill integrates with the **marc-andreessen** expert. The analysis should emphasize the expansion narrative and challenge conventional TAM assumptions.

Related skills:
- `software-disruption-analysis` - For understanding how software enables expansion
- `market-over-team-analysis` - For evaluating if expanded market is attractive
- `feature-vs-product-test` - For assessing if solution can capture expansion