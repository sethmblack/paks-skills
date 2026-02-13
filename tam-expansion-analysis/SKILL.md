---
name: tam-expansion-analysis
description: Calculate potential market size by analyzing how software removes existing constraints, using Marc Andreessen's insight that technology expands markets rather than just capturing existing share.
license: MIT
metadata:
  version: 1.0.2054
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- storytelling
- tam-expansion-analysis
- market-analysis
- venture-capital
- writing
---

# TAM Expansion Analysis

Calculate potential market size by considering how software removes existing constraints, using Marc Andreessen's insight that technology expands markets rather than just capturing existing share. Traditional market sizing measures current behavior under current constraints, dramatically understating opportunity when technology can eliminate those constraints entirely. Uber did not capture the $11B taxi market—they created a $100B+ ride market by making it easier, cheaper, and more reliable to get a ride. This skill applies the expansion lens to any market where software might unlock latent demand that current solutions cannot serve.

---

## When to Use

- Evaluating startup market opportunity when conventional TAM seems small
- Challenging conventional market sizing in investment pitches
- Understanding why a market looks small but could be enormous
- Investment due diligence when standard TAM analysis feels inadequate
- Explaining why comparisons to existing markets are misleading
- Building conviction in a contrarian market thesis

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| market_description | Yes | The market or industry being analyzed |
| existing_tam | No | Current conventional market size estimate |
| proposed_solution | No | The software or technology solution being considered |
| constraints_observed | No | Known limitations of current solutions |

---

## Core Principle

Traditional market sizing measures what exists, not what could exist. When software removes the constraints that limit current market participation—price, access, friction, information, quality, or customization—the addressable market expands far beyond conventional estimates. The key insight: non-consumption is not absence of demand but presence of constraint.

---

## Methodology

### Phase 1: Constraint Identification

**Step 1: Map Current Market Constraints**

Identify what limits the current market size:

| Constraint Type | Question to Ask | Example |
|-----------------|-----------------|---------|
| Price | Who cannot afford current solutions? | Personal financial advisors require $250K+ minimum |
| Access | Who cannot reach current solutions? | Limited geography, business hours, credentials required |
| Friction | Who finds current solutions too hard? | Complex signup, long sales cycles, difficult UX |
| Information | Who cannot find or evaluate options? | Opaque pricing, hard to compare, trust barriers |
| Quality | Who is underserved by inconsistent delivery? | Variable service quality, unreliable availability |
| Customization | Who needs something current solutions cannot offer? | One-size-fits-all does not fit their use case |

**Step 2: Quantify Constraint Impact**

For each constraint, estimate:
- How many potential users are excluded?
- How much usage is suppressed among current users?
- What adjacent use cases are blocked entirely?

### Phase 2: Expansion Analysis

**Step 3: Model Constraint Removal**

For each constraint, ask: What if software reduced this to near-zero?

| Constraint | Current Impact | After Software | Market Effect |
|------------|---------------|----------------|---------------|
| Price | X buyers | Y buyers (larger) | Y/X multiplier |
| Access | Limited reach | Universal reach | Geographic multiplier |
| Friction | High effort | Zero effort | Frequency multiplier |
| Information | Opacity | Transparency | Conversion multiplier |

**Step 4: Identify Adjacent Use Cases**

What becomes possible that was not before?

Questions to ask:
- Who does not use this today because of constraints?
- What substitute behaviors would convert to this?
- What use cases are "too small" for current solutions?
- What becomes viable at lower price or friction?

### Phase 3: Comparable Analysis

**Step 5: Find Historical Expansion Patterns**

Reference similar market expansions:

| Market | Before Software | After Software | Expansion |
|--------|-----------------|----------------|-----------|
| Taxis to Rideshare | $11B (2009) | $100B+ (2020) | ~10x |
| Hotels to Short-term rentals | $100B | $300B+ | 3x+ |
| Retail to E-commerce | Constrained by stores | Infinite selection | 10%+ annual growth |
| Music distribution | $15B physical | $25B streaming | Still expanding |
| Tax prep to DIY software | $10B (CPAs) | $15B+ (DIY) | 1.5x+ |

### Phase 4: Calculation

**Step 6: Calculate Expanded TAM**

Apply expansion formula:

```
Expanded TAM = (Current TAM x Access Multiplier x Price Multiplier x Frequency Multiplier) + Adjacent Markets
```

Multiplier guidance:

| Factor | Conservative | Moderate | Aggressive |
|--------|--------------|----------|------------|
| Access | 1.5x | 3x | 10x |
| Price | 1.5x | 2x | 5x |
| Frequency | 1.5x | 2x | 3x |

---

## Output Format

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
- [Segment 1]: [Why they do not participate today]
- [Segment 2]: [Why they do not participate today]

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

- Expansion analysis is not magic—real constraints may persist even with software
- Market timing matters: too early and adoption is slow, too late and incumbents adapt
- Regulatory barriers may not yield to technology
- Consumer behavior change takes time even when friction is removed
- Network effects and supply constraints may limit expansion speed
- Present findings with appropriate confidence levels given uncertainty

---

## Anti-Patterns to Avoid

**1. Confusing Potential with Probability**
A 10x expansion is possible does not mean it is likely. Weight your analysis by execution difficulty and market readiness.

**2. Ignoring Incumbent Response**
Established players will not sit idle. Factor in competitive response to constraint removal.

**3. Assuming All Constraints Are Software-Solvable**
Some constraints are regulatory, behavioral, or physical. Software cannot solve everything.

**4. Cherry-Picking Comparables**
Choosing only the most dramatic expansions (Uber, Airbnb) while ignoring markets that did not expand as expected.

**5. Neglecting Supply-Side Constraints**
Demand expansion analysis is useless if supply cannot scale. Consider both sides of the market.

---

## Examples

### Example 1: AI Financial Advisory

**Situation:** Evaluating market size for AI-powered financial advisor accessible to everyone, with conventional wealth management TAM of $50B.

**Application:**

#### Current Market Constraints

| Constraint | Impact on Market | Evidence |
|------------|------------------|----------|
| Minimum account size | Only serves wealthy ($250K+ typical minimum) | 90% of Americans do not use financial advisors |
| High fees | 1% AUM prices out small accounts | $10K account = $100/year value |
| Access/appointments | Limited advisor time, inconvenient | Hours of operation, waiting for appointments |
| Complexity | Advice is hard to understand | Most Americans financially illiterate |

#### Constraint Removal Analysis

| Constraint | Current State | After AI Advisor | Market Effect |
|------------|---------------|------------------|---------------|
| Minimum | $250K+ | $0 | 10x more people served |
| Cost | 1% AUM | $10-50/month flat | 20x cheaper for small accounts |
| Access | Business hours | 24/7 instant | 3x more interactions |
| Complexity | Expert jargon | Plain language | Higher conversion |

#### TAM Calculation

```
Current TAM: $50B (wealth management)
x Access Multiplier: 3x (10x more people, lower spend per person)
x Frequency Multiplier: 2x (daily vs. annual engagement)
+ Adjacent Markets: $50B (insurance, tax, lending integration)
= Expanded TAM: $350B
```

**Key Insight:** The $50B wealth management TAM dramatically understates the opportunity because it only measures people wealthy enough to use current services. Financial advice is a universal need constrained by delivery economics.

---

### Example 2: Remote Monitoring for Chronic Disease

**Situation:** Evaluating market for continuous health monitoring devices, with current chronic disease management market of $30B.

**Application:**

#### Current Market Constraints

| Constraint | Impact on Market | Evidence |
|------------|------------------|----------|
| Episodic care | Only captures snapshots, misses between-visit changes | Patients see doctors 2-4x per year |
| Manual tracking | Patient compliance low for logging | Most patients do not track consistently |
| Reactive treatment | Problems caught late | Hospitalizations from preventable escalation |

#### Adjacent Use Cases Unlocked

- Pre-diabetics: 88M Americans who could prevent progression with monitoring
- Medication adherence: Real-time tracking enables intervention
- Insurance risk pricing: Continuous data enables personalized premiums

#### TAM Calculation

```
Current TAM: $30B (chronic disease management)
x Frequency Multiplier: 3x (continuous vs. episodic)
x Access Multiplier: 2x (pre-disease population included)
+ Adjacent Markets: $20B (insurance, pharma data)
= Expanded TAM: $200B
```

**Key Insight:** Current market measures treatment of diagnosed conditions. Continuous monitoring expands to prevention and early intervention, a fundamentally larger category.

---

### Example 3: Legal Services Democratization

**Situation:** Evaluating AI legal assistant market against $300B legal services industry.

**Application:**

#### Current Market Constraints

| Constraint | Impact on Market | Evidence |
|------------|------------------|----------|
| Hourly rates | $200-1000/hour excludes most consumers | 80% of civil legal needs go unmet |
| Complexity | People do not know when they need legal help | Rights unexplored, contracts unsigned |
| Access | Limited to business hours, appointments | No instant availability |

#### Comparable Market Expansions

| Comparable | Before | After | Expansion | Relevance |
|------------|--------|-------|-----------|-----------|
| Tax prep to TurboTax | $10B | $15B+ | 1.5x | Similar democratization |
| LegalZoom | $300B lawyers | $500M DIY | Slice only | Created new market |

**Key Insight:** Unlike wealth management, legal services may not fully expand because much legal need is either unnecessary complexity or truly requires human judgment. Expect market slice creation (new $10-20B segment) rather than full market expansion.

---

## Integration

This skill integrates with the **marc-andreessen** expert persona. The analysis should emphasize the expansion narrative and challenge conventional TAM assumptions.

**Works with:**
- `software-disruption-analysis` for understanding how software enables expansion
- `market-over-team-analysis` for evaluating if expanded market is attractive
- `feature-vs-product-test` for assessing if solution can capture expansion

**When to prefer this skill:**
- When conventional TAM analysis yields surprisingly small numbers
- When software clearly removes historical constraints
- When building contrarian investment thesis

**Cautions:**
- Do not use to justify any market size desired
- Ground in comparable expansions, not wishful thinking
- Acknowledge execution risk alongside opportunity size