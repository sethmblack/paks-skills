---
name: price-signal-analysis
description: Analyze how prices communicate dispersed information and coordinate behavior without central direction. Diagnose failures when price signals are suppressed or distorted.
license: MIT
metadata:
  version: 1.0.4734
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- price-signal-analysis
- economics
- markets
- writing
---

# Price Signal Analysis

Prices are not just measures of value - they are signals that communicate dispersed information and coordinate behavior across millions of actors who will never meet. Friedrich Hayek's fundamental insight: "We must look at the price system as a mechanism for communicating information if we want to understand its real function." A rising price tells producers to make more and consumers to economize - without any central authority needing to know why demand increased or supply decreased. This skill analyzes how price signals function in any market or coordination system, diagnoses what happens when signals are distorted or suppressed, and identifies why interventions that attack prices often worsen the problems they aim to solve.

---

## When to Use

- Understanding how markets coordinate without central direction
- Analyzing effects of price controls (rent control, minimum wage, price caps)
- Designing marketplaces, platforms, or incentive systems
- Diagnosing coordination failures in systems lacking price signals
- Evaluating proposed regulations or interventions that affect prices
- Understanding why shortages or surpluses persist

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| market_or_system | Yes | The market, platform, or coordination system to analyze |
| prices_or_signals | Yes | The relevant prices, rates, or signal mechanisms |
| intervention | No | Any proposed or actual price control or manipulation |
| desired_outcome | No | What the intervention aims to achieve |

---

## Core Principle

Prices aggregate dispersed knowledge that no central authority could collect. They communicate scarcity, coordinate supply and demand responses, and allocate resources to highest-valued uses - all without anyone needing to understand the whole system. When prices are controlled or suppressed, the information they carry is lost, and the coordination they enable breaks down. The price is not the problem - it's information about the problem.

---

## Methodology

### Phase 1: Identify Price Signals
1. Name the key prices in this market or system
2. Identify what each price measures (scarcity of what?)
3. Determine who responds to each price signal
4. Map the information flow: what knowledge is aggregated in this price?

### Phase 2: Analyze What Prices Communicate
1. **Scarcity information**: What does rising/falling price reveal?
2. **Opportunity costs**: What alternatives does the price make visible?
3. **Aggregated knowledge**: Whose information is embedded in this price?
4. **Future expectations**: What anticipations does the price reflect?

### Phase 3: Map Coordination Mechanism
1. **Demand-side response**: How do buyers/users respond to price changes?
2. **Supply-side response**: How do sellers/producers respond to price changes?
3. **Allocation effect**: How do resources flow based on price signals?
4. **Discovery function**: What new information does price competition reveal?

### Phase 4: Assess Signal Quality
1. Are externalities captured in the price?
2. Is information symmetric between buyers and sellers?
3. Is competition sufficient for price discovery?
4. Is price formation free or distorted by intervention?

### Phase 5: Analyze Intervention Effects (if applicable)
1. How does the intervention change the price signal?
2. What information is lost when the price is controlled?
3. What coordination failures result?
4. What predictable consequences follow from distorted signals?
5. What alternative approaches might achieve the goal without suppressing signals?

---

## Output Format

```markdown
## Price Signal Analysis: [Market/System]

### Market/System Under Analysis
[What is being examined]

### Key Price Signals
| Price/Signal | What It Measures | Who Responds |
|--------------|------------------|--------------|
| [Price] | [Scarcity of X] | [Buyers, sellers, etc.] |

### Information Communicated

**Scarcity Information:**
- [What the price reveals about scarcity/abundance]

**Opportunity Costs:**
- [What alternatives the price makes visible]

**Aggregated Knowledge:**
- [Whose knowledge is embedded in this price]

**Future Expectations:**
- [What anticipations the price reflects]

### Coordination Mechanism

**Demand-Side Response:**
- [How buyers/users respond to price signals]

**Supply-Side Response:**
- [How sellers/producers respond to price signals]

**Allocation Effect:**
- [How resources flow based on these signals]

### Signal Quality Assessment
| Factor | Assessment | Notes |
|--------|------------|-------|
| Externalities captured? | [Yes/No/Partial] | [Explanation] |
| Information symmetric? | [Yes/No/Partial] | [Explanation] |
| Competition present? | [Yes/No/Partial] | [Explanation] |
| Price formation free? | [Yes/No/Partial] | [Explanation] |

### Intervention Analysis (if applicable)

**Proposed/Actual Intervention:** [Description]

**Signal Distortion:**
- [How the intervention distorts the price signal]

**Coordination Failure:**
- [How actors can no longer coordinate effectively]

**Predictable Consequences:**
1. [Consequence]: [Why it follows from distorted signals]

### Alternative Approaches
[How to achieve the goal without suppressing price signals]

### The Hayekian Verdict
[Summary insight about price signals in this system]
```

---

## Constraints

- Acknowledge legitimate market failures (externalities, public goods, information asymmetry)
- Do not assume all price signals are perfect or unbiased
- Consider distributional effects of prices and interventions
- Recognize that some goods may have non-market values
- Distinguish between improving price signals and suppressing them
- Do not conflate market analysis with policy prescription

---

## Anti-Patterns to Avoid

- **Attacking the Thermometer**: Treating the price as the problem rather than information about the problem. High rents signal housing scarcity; controlling rents doesn't create housing.

- **Ignoring Market Failures**: Assuming all prices perfectly capture all costs and benefits. Externalities, information asymmetry, and public goods are real. Acknowledge where price signals are incomplete.

- **Ignoring Distribution**: Prices coordinate efficiently but not necessarily equitably. "The market works" doesn't address whether the resulting distribution is acceptable.

- **Central Planning Impulse**: Assuming that because we can identify what prices "should" be, we can set them without losing the information they aggregate. We cannot.

- **Static Analysis**: Analyzing prices at one moment without considering how supply and demand respond over time. Price effects unfold dynamically.

---

## Examples

### Example 1: Rent Control

**Situation**: City implements rent control to make housing affordable.

**Application**:
- Price signal: Market rent signals scarcity of housing relative to demand
- Information communicated: High rents say "build more here, this is where people want to live"
- Intervention: Cap rents below market clearing
- Signal distortion: Controlled rent tells developers "not much demand" when reality is opposite

**Output**:
Coordination failures:
- Supply signal suppressed: Developers see capped returns, don't build
- Allocation distorted: Tenants stay in mismatched units (empty nesters in 3BR)
- Quality degrades: Landlords can't recoup improvement costs
- Shortage institutionalized: Below-market prices guarantee permanent shortage

Alternative approaches: Supply-side (reduce building barriers), demand-side subsidies (vouchers that let prices function), land value taxation.

Hayekian verdict: Rent control attacks the signal rather than the scarcity. The price that would call forth supply is silenced, while demand remains.

### Example 2: Surge Pricing

**Situation**: Ride-share company uses surge pricing during high demand periods. Politicians propose banning "price gouging."

**Application**:
- Price signal: Surge price signals temporary scarcity of drivers relative to riders
- Information communicated: High price says "more drivers needed now, here"
- Without surge: Fixed price gives no signal that more drivers are needed
- With surge: Drivers see opportunity, shift to high-demand area

**Output**:
Coordination mechanism:
- Demand-side: Higher price causes some riders to wait, share rides, or use alternatives
- Supply-side: Higher earnings attract more drivers to the area
- Net effect: Supply increases, demand moderates, shortage clears

If surge banned:
- No signal to attract drivers
- Shortage persists until demand naturally declines
- Those who most need rides can't get them at any price

Alternative: Income support for those who can't afford surge prices, while preserving signal function.

### Example 3: Minimum Wage

**Situation**: Government raises minimum wage to ensure living wages.

**Application**:
- Price signal: Wage signals value of marginal labor relative to alternatives
- Information communicated: Low wage signals "more workers available than jobs for this skill level"
- Intervention: Floor price above market clearing for some workers

**Output**:
Signal analysis (nuanced):
- For workers whose productivity exceeds new minimum: No effect on employment, higher wages
- For workers whose productivity is below new minimum: Price signal suppressed
- Employers respond: Automation, reduced hours, higher skill requirements, fewer entry-level jobs

Signal quality factors:
- Monopsony (single buyer) can suppress wages below productivity - intervention may correct this
- Information asymmetry about productivity may mean wages are "wrong"
- Context matters: labor market tightness affects outcomes significantly

Alternative approaches: EITC (subsidizes low wages without suppressing price signal), job training (increases worker productivity above minimum).

Hayekian observation: Where labor markets are competitive, minimum wage above market-clearing creates unemployment signal that can't clear. Where markets are monopsonistic, intervention may improve outcomes. Analysis must be context-specific.

---

## Integration

**Works with:**
- **coordination-failure-diagnosis**: Identifies when price suppression causes coordination breakdown
- **unintended-consequences-analysis**: Traces how price distortions cascade through systems
- **incentive-analysis**: Prices are powerful incentives; changing them changes behavior

**When to prefer this skill:**
- When analyzing market interventions
- When designing pricing for platforms or marketplaces
- When diagnosing shortages or surpluses

**Cautions:**
- Price analysis is not policy prescription
- Markets can fail; externalities and public goods are real
- Distributional concerns are legitimate even when markets "work"
- Not all goods should be allocated by price