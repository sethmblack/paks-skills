---
name: stock-flow-analysis
description: Analyze accumulations (stocks) and rates of change (flows) to understand why systems respond slowly to intervention, where momentum builds, and why impatience leads to oscillation.
license: MIT
metadata:
  version: 1.0.1983
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- stock-flow-analysis
- writing
---

# Stock-Flow Analysis

Analyze accumulations (stocks) and rates of change (flows) to understand why systems respond slowly to intervention, where momentum builds, and why impatience leads to oscillation.

---

## When to Use

- When change takes longer than expected
- When interventions don't seem to have effect
- When things accumulate or deplete
- When there are boom-bust patterns

**Trigger Phrases:**
- "Why does change take so long?"
- "The numbers don't respond"
- "We made the change but nothing happened"
- "Things are building up"
- "We keep overshooting"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| system | Yes | The system to analyze |
| stocks | No | What accumulates |
| flows | No | What changes stocks |
| concern | No | What behavior is problematic |

---

## Core Concepts

### Stocks

**Definition:** Accumulations—things that can be measured at a point in time.

**Characteristics:**
- Change slowly (can only change as fast as flows allow)
- Create memory in systems (history matters)
- Provide stability and inertia
- Decouple inflows from outflows

**Examples:**
- Bank account balance
- Population
- Inventory
- Reputation
- Technical debt
- Trust
- Skills/knowledge
- Pollution accumulated in a lake

### Flows

**Definition:** Rates of change—what increases or decreases stocks over time.

**Characteristics:**
- Measured per unit of time (per day, per month)
- Can change instantly
- Are the only thing that can change a stock

**Examples:**
- Deposits and withdrawals (change bank balance)
- Births and deaths (change population)
- Purchases and sales (change inventory)
- Praise and criticism (change reputation)

### The Bathtub Metaphor

Think of a bathtub:
- **Stock:** Water level in the tub
- **Inflow:** Faucet
- **Outflow:** Drain

Key insights:
- Water level can only change through faucet or drain
- If faucet > drain, level rises (even if drain is open)
- If drain > faucet, level falls (even if faucet is running)
- The level changes slowly even when faucet/drain change quickly

---

## Why Stocks Matter

### 1. Stocks Create Delays

Even if you change a flow immediately, the stock changes gradually.

**Example:** You fix the hiring problem (inflow), but employee count (stock) takes months to change.

### 2. Stocks Create Momentum

Accumulated stocks have inertia. A large stock takes a long time to deplete or build.

**Example:** A good reputation (stock) can survive some bad events (outflow) because there's a lot accumulated. But it takes years to rebuild once depleted.

### 3. Stocks Allow Decoupling

Stocks buffer inflows from outflows, allowing them to be independent.

**Example:** Inventory (stock) allows you to produce at one rate and sell at a different rate.

### 4. Stocks Make Flows Possible

Sometimes the stock enables the flow.

**Example:** A large bank account (stock) enables large investments (outflow) which generate returns (inflow).

---

## The Analysis Protocol

### Step 1: Identify the Key Stocks

What accumulates in this system?
- Physical: inventory, population, cash, equipment
- Intangible: reputation, trust, skills, knowledge, morale
- Problematic: debt, pollution, backlog, technical debt

**For each stock, ask:**
- What can I measure at a point in time?
- What has memory, history, inertia?
- What changes slowly?

### Step 2: Identify Flows

For each stock:
- **Inflows:** What increases this stock?
- **Outflows:** What decreases this stock?

**Create a flow inventory:**

| Stock | Inflows | Outflows |
|-------|---------|----------|
| Employee count | Hiring | Turnover, retirement, layoffs |
| Trust | Promises kept | Promises broken, bad experiences |
| Technical debt | Shortcuts, workarounds | Refactoring, rewrites |

### Step 3: Assess Current State

For each stock:
- Is the stock growing, shrinking, or stable?
- Which flows dominate?
- What determines the flow rates?

### Step 4: Calculate Time Constants

How long would it take to significantly change the stock at current flow rates?

**Residence time = Stock / Flow**

Example: If you have 100 employees and hire 10/year while losing 12/year, net flow is -2/year. But turnover of the entire stock takes 100/12 = 8+ years.

### Step 5: Find the Binding Constraints

What limits flow rates?
- Inflow limits: hiring capacity, capital, attention
- Outflow limits: demand, capacity, regulatory constraints

Which constraint is most binding?

### Step 6: Diagnose the Problem

Common stock-flow problems:
- **Ignoring stock:** Focusing on flows without understanding what's accumulated
- **Expecting instant change:** Not accounting for the time stocks need to change
- **Oscillation:** Overreacting to slow stock changes, causing overshoot
- **Depletion spirals:** Drawing down stock faster than it can replenish

---

## Common Patterns

### The Patience Problem

**Symptom:** "We made the change but nothing happened."

**Cause:** You changed a flow, but the stock hasn't had time to respond.

**Example:** You improved hiring practices last month. Why isn't culture better?
- Culture (stock) changes slowly
- New hires (inflow) are a small fraction of total employees
- It will take years for culture stock to shift significantly

**Solution:** Wait. Measure the flow (are you hiring better people?) not just the stock.

### The Oscillation Problem

**Symptom:** Boom-bust cycles. Overshooting and undershooting.

**Cause:** Impatience with stock delays leads to overreaction.

**Example:** Inventory management
- Stock low → Order aggressively
- Delay before orders arrive
- Impatience → Order more
- All orders arrive at once → Overstocked
- Stop ordering → Stock depletes → Repeat

**Solution:** Factor in delays. Adjust flows gradually. Don't overcorrect.

### The Depletion Problem

**Symptom:** Resource running out faster than it can replenish.

**Cause:** Outflow > inflow for an extended period.

**Example:** Employee burnout
- Energy (stock) depleted by work (outflow)
- Recovery (inflow) inadequate
- Stock depleted → person quits or burns out

**Solution:** Either reduce outflow or increase inflow. Preferably both.

### The Invisible Accumulation

**Symptom:** Sudden crisis that seems to come from nowhere.

**Cause:** A stock was accumulating unnoticed until it hit a threshold.

**Example:** Technical debt
- Small shortcuts (inflow) accumulate
- No visible problem day-to-day
- Suddenly: major failure, massive refactor needed

**Solution:** Monitor stocks, not just flows. What's accumulating?

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

## Outputs

| Output | Description |
|--------|-------------|
| Stock inventory | Key accumulations in the system |
| Flow diagram | What changes each stock |
| Rate analysis | How fast stocks are changing |
| Delay assessment | How long changes take |
| Constraint identification | What limits flows |
| Problem diagnosis | Which stock-flow dynamic causes the issue |

---



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


## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Additional Notes

**Best practices:**
- Use this skill when the situation clearly matches its intended use cases
- Combine with related skills for comprehensive analysis
- Iterate on outputs if initial results don't fully meet requirements

**Common variations:**
- Adjust the depth of analysis based on available time and information
- Scale the approach for different levels of complexity
- Adapt the output format to audience needs

**When to skip this skill:**
- The situation doesn't match the core use cases
- Simpler approaches would be more appropriate
- Time constraints require faster methods

## Example

**User:** "We launched a customer success program 6 months ago. We're doing all the right things—onboarding, check-ins, training. But churn is the same. Was this a waste?"

**Stock-Flow Analysis response:**

Let's analyze the stocks and flows.

**Key stocks:**
- Customer count
- Customer health (satisfaction, engagement, value received)
- Customer relationship depth

**Flows affecting customer count:**
- Inflow: New customer acquisition
- Outflow: Churn

**Your intervention:**
You're trying to reduce the outflow (churn) by improving the customer health stock.

**The timing problem:**

Customer health is a stock that changes slowly:
- Onboarding affects new customers (small fraction of total)
- Check-ins and training build relationship gradually
- Trust and value perception accumulate over months

**Six months is too short to see the effect in churn.**

Here's why:

1. **Existing customers:** The customers who churn today were acquired 1-2 years ago. Their health stock was already low before your program started. Your program affects *future* churn, not immediate churn.

2. **New customers:** Customers who joined since your program started haven't reached the typical churn point yet. You won't see their improved retention for another 6-18 months.

3. **The lag:** There's a delay between improved customer health (stock) and reduced churn (flow). Customers decide to leave based on accumulated experience, not recent improvements.

**What to measure instead:**

Don't measure churn (the outcome you're waiting for). Measure the leading indicators:

| Metric | What It Shows |
|--------|---------------|
| Onboarding completion rate | Inflow to customer health stock |
| NPS/CSAT for recent cohorts | Customer health stock for new customers |
| Feature adoption | Engagement inflow |
| Support ticket sentiment | Relationship health |

**The diagnosis:**

This isn't a failed program—it's a stock-flow timing problem. You're changing the inflows (onboarding, training, check-ins). The stock (customer health) is probably improving. But the outflow (churn) won't show that for 12-18 months.

**Recommendation:**

1. Keep the program running—you're building a stock
2. Measure the inflows (are you doing the activities?)
3. Measure the stock (is customer health improving for new cohorts?)
4. Be patient on the outflow (churn will follow, with delay)
5. Communicate the time constant to stakeholders so they don't kill the program prematurely

---

## Integration

This skill pairs with:
- **feedback-loop-mapping** - Understand loops that connect stocks and flows
- **leverage-point-analysis** - Buffer sizes and flow structures are leverage points
- **systems-archetype-recognition** - Many archetypes involve stock-flow dynamics

---

## Source Expert

Donella Meadows - `experts/donella-meadows/`