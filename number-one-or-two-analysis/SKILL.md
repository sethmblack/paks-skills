---
name: number-one-or-two-analysis
description: 'Evaluate a business unit or product line''s market position and determine whether to fix, sell, or close based on competitive position. Based on Jack Welch''s doctrine: "If you''re not #1 or #2 in you...'
license: MIT
metadata:
  version: 1.0.4587
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- '#1-or-#2-analysis'
- writing
---

# #1 or #2 Analysis

Evaluate a business unit or product line's market position and determine whether to fix, sell, or close based on competitive position. Based on Jack Welch's doctrine: "If you're not #1 or #2 in your market, fix it, sell it, or close it. Period."

---

## When to Use

- Portfolio review deciding where to invest or divest
- Business unit consistently underperforms despite effort
- Strategic planning to allocate limited resources
- Acquisition target evaluation (are they #1 or #2?)
- Question of "should we stay in this business?"
- New competitor threatening market position
- Request for "which businesses should we keep?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| business_unit | Yes | The business, product line, or market segment to evaluate |
| market_definition | Yes | How is the market defined? (Critical - can be gamed) |
| market_position | Yes | Current rank and market share |
| competitors | Yes | Who are the other players and their positions |
| financial_performance | No | Revenue, margins, growth, profitability |
| strategic_importance | No | Role in overall company strategy |

---

## The Welch #1 or #2 Framework

### The Core Principle

> "If you're not #1 or #2 in your market, you have no right to exist. When a recession comes - and recessions always come - the #3 and #4 players get killed. The leaders take share, the followers lose it."

**Why #1 or #2 matters:**
- Market leaders have pricing power
- Leaders attract the best talent
- Leaders get the best partnerships
- Leaders survive downturns; followers don't
- Leaders have resources to invest in the next generation

### The Three Options

For any business not #1 or #2:

| Option | When to Choose | Action Required |
|--------|---------------|-----------------|
| **FIX** | Path to #1/#2 exists and is achievable | Invest heavily to gain share |
| **SELL** | Business has value to others but not to you | Find acquirer and exit |
| **CLOSE** | No path to leadership, no buyer, just bleeding | Shut down and redeploy resources |

### The Market Definition Problem

**Warning:** The #1 or #2 test can be gamed through creative market definition.

**Bad:** "We're #1 in red widgets sold on Tuesdays in the Northeast"
- Market defined so narrowly that being #1 is meaningless

**Good:** "We're #2 in the enterprise CRM market competing with Salesforce"
- Market defined by actual competitive dynamics

**Test:** Define the market as your customers see it, not as your strategy deck wishes it.

---

## Analysis Process

### Step 1: Define the Market Honestly

| Question | Answer |
|----------|--------|
| Who are our actual competitors? | [List] |
| How do customers describe this market? | [Their words] |
| What do customers compare when choosing? | [Decision criteria] |
| What is the total addressable market? | [$] |
| Is this market growing, stable, or declining? | [Trend] |

**Red flags for self-deception:**
- Market definition requires explanation
- Competitors you exclude are ones customers compare you to
- "Our segment is different" (is it really?)

### Step 2: Assess Current Position

| Metric | Our Business | #1 Competitor | #2 Competitor |
|--------|-------------|---------------|---------------|
| Market share | [%] | [%] | [%] |
| Revenue | [$] | [$] | [$] |
| Growth rate | [%] | [%] | [%] |
| Profitability | [Margin %] | [Est.] | [Est.] |
| Brand strength | [H/M/L] | [H/M/L] | [H/M/L] |

**Position assessment:**
- [ ] Clearly #1 (dominant share, pricing power)
- [ ] Clearly #2 (strong challenger, viable path to #1)
- [ ] Weak #2 (second place but gap is large)
- [ ] #3 or lower (not a leader, fighting for scraps)

### Step 3: Evaluate Path to Leadership

If not #1 or #2, can you get there?

| Factor | Assessment | Implication |
|--------|-----------|-------------|
| **Cost to achieve** | [$ investment required] | Do we have resources? |
| **Time to achieve** | [Years] | Can we wait that long? |
| **Probability of success** | [%] | Realistic or wishful? |
| **Competitive response** | [What will leaders do?] | Will they let us win? |
| **Market trend** | [Growing/Stable/Declining] | Is the prize worth winning? |

**Welch's test:** "If we have to ask whether we can become #1 or #2, we probably can't."

### Step 4: Calculate Opportunity Cost

| Scenario | Investment | Expected Return | Risk | Alternative Use |
|----------|-----------|----------------|------|-----------------|
| Fix this business | [$] | [$] | [H/M/L] | What else could this fund? |
| Sell this business | Proceeds: [$] | Exit at [$] | [H/M/L] | What would buyer pay? |
| Close this business | Costs: [$] | Savings: [$] | [H/M/L] | Resource redeployment |

**The real question:** What would you do with these resources if you weren't subsidizing a #3 or #4 player?

### Step 5: Make the Decision

| Decision | Criteria | Your Assessment |
|----------|----------|-----------------|
| **FIX** | Clear path to #1/#2 within 2-3 years with affordable investment | [Met/Not Met] |
| **SELL** | Business has strategic value to potential acquirer | [Met/Not Met] |
| **CLOSE** | No path to leadership and no acquirer | [Met/Not Met] |

**Default rule:** If FIX criteria aren't clearly met, default to SELL or CLOSE. Hope is not a strategy.

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
## #1 or #2 Analysis: [Business Unit Name]

### Market Definition

**Market:** [How we define it]
**Validation:** [How customers/competitors define it]
**Market size:** [$TAM]
**Growth trend:** [Growing/Stable/Declining at X%]

### Competitive Position

| Player | Market Share | Rank | Trend |
|--------|-------------|------|-------|
| [Leader] | [%] | #1 | [Growing/Stable/Declining] |
| [Challenger] | [%] | #2 | [Growing/Stable/Declining] |
| **Our Business** | [%] | **#[X]** | [Growing/Stable/Declining] |
| [Others] | [%] | #[X] | [Growing/Stable/Declining] |

### Position Assessment

**Current position:** [#1 / Strong #2 / Weak #2 / #3 or below]

**Gap to leadership:** [% share needed, $ revenue gap]

**Honest evaluation:** [Are we a leader or a follower?]

### Fix Assessment

| Factor | Analysis | Verdict |
|--------|----------|---------|
| Path to #1/#2 | [Describe the path] | [Viable/Questionable/Impossible] |
| Investment required | [$X over Y years] | [Affordable/Stretch/Unaffordable] |
| Time horizon | [X years] | [Acceptable/Too long] |
| Probability of success | [X%] | [Good bet/Long shot] |
| Market trajectory | [Growing/Declining] | [Prize worth winning?] |

**FIX VERDICT:** [VIABLE / NOT VIABLE]

### Sell Assessment

| Factor | Analysis |
|--------|----------|
| Potential acquirers | [Who would buy this?] |
| Strategic value to buyer | [Why they would want it] |
| Estimated sale value | [$] |
| Sale complexity | [Simple/Moderate/Complex] |

**SELL VERDICT:** [VIABLE / NOT VIABLE]

### Close Assessment

| Factor | Analysis |
|--------|----------|
| Wind-down costs | [$] |
| Customer impact | [Description] |
| Employee impact | [#] |
| Resource redeployment | [Where would resources go?] |

**CLOSE VERDICT:** [VIABLE / NOT VIABLE]

### Recommendation

**Decision:** [FIX / SELL / CLOSE]

**Rationale:** [2-3 sentence justification]

**Timeline:** [When to execute]

**Resources freed:** [$ or people that can be redeployed]

### Action Plan

**If FIX:**
1. [Investment plan]
2. [Milestones for progress]
3. [Kill criteria - when do we revisit?]

**If SELL:**
1. [Potential buyers to approach]
2. [Preparation needed]
3. [Timeline for process]

**If CLOSE:**
1. [Wind-down plan]
2. [Customer transition]
3. [Resource reallocation]

### Welch Principle Applied

> "Don't subsidize losers with profits from winners. That's not kindness - that's killing your winners."
```

---

## Constraints

- Market definition must be honest (how customers see it, not how strategy wishes)
- Acknowledge emotional attachment to legacy businesses
- "Fix" requires genuine path to leadership, not just hope
- Consider strategic interdependencies (does this business enable others?)
- Recognize that some businesses serve purposes beyond direct profitability (but be honest about the cost)

---

## Failure Modes to Avoid

| Failure Mode | Symptom | Prevention |
|--------------|---------|------------|
| **Market gerrymandering** | Define market narrowly to claim #1 | Test: how do customers define the market? |
| **Eternal turnaround** | "Fix" plan never succeeds but never ends | Set time-bound milestones; kill if not met |
| **Sacred cow protection** | "We can't exit this; it's who we are" | Ask: what would a new CEO do? |
| **Sunk cost fallacy** | "We've invested too much to quit" | Ignore past investment; evaluate future only |
| **Optimism bias** | "We'll gain share" without evidence | Require specific, funded plan for share gain |

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Market definition disputed | Document multiple definitions; analyze position in each |
| Position is borderline #2 | Set milestone: must be clear #2 within 12 months or reclassify |
| "Fix" requires more resources than available | That's a SELL or CLOSE, not a FIX |
| Strategic interdependencies claimed | Quantify the interdependency; challenge if not measurable |
| Emotional resistance to closing | Name the attachment; apply "new CEO" test |

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

**Input:** "We have a mobile app business that's been around for 8 years. We're probably #4 or #5 in our category. We've never been profitable but it 'supports our ecosystem.' Should we keep investing?"

**Output:**

## #1 or #2 Analysis: Mobile App Business

### Market Definition

**Market:** Consumer mobile apps in [category]
**Validation:** Users compare us to [competitor apps] when choosing
**Market size:** $500M in app revenue, growing 8% annually
**Growth trend:** Growing, but dominated by top 2-3 players

### Competitive Position

| Player | Market Share | Rank | Trend |
|--------|-------------|------|-------|
| Market Leader | 35% | #1 | Growing |
| Strong Challenger | 22% | #2 | Growing |
| Established Player | 15% | #3 | Stable |
| Another Player | 10% | #4 | Declining |
| **Our Business** | 6% | **#5** | Stable |
| Others | 12% | N/A | Fragmented |

### Position Assessment

**Current position:** #5 - not a market leader, fighting for scraps

**Gap to leadership:** Would need to more than triple share to reach #2

**Honest evaluation:** After 8 years at 6% share, this business is a permanent follower. The market has spoken.

### Fix Assessment

| Factor | Analysis | Verdict |
|--------|----------|---------|
| Path to #1/#2 | Would require 3x share gain against entrenched leaders | Impossible without acquisition |
| Investment required | Estimated $50M+ over 3 years | Massive bet |
| Time horizon | 3-5 years minimum | Very long |
| Probability of success | <10% - leaders will defend | Long shot |
| Market trajectory | Growing but consolidating to leaders | Prize is shrinking for followers |

**FIX VERDICT:** NOT VIABLE

Eight years of trying has produced 6% share. The definition of insanity is doing the same thing and expecting different results.

### Sell Assessment

| Factor | Analysis |
|--------|----------|
| Potential acquirers | #3 or #4 player might want our user base; adjacent company might want entry point |
| Strategic value to buyer | User base, technology, team |
| Estimated sale value | $10-20M (technology and users, no profitability premium) |
| Sale complexity | Moderate - need to find right buyer |

**SELL VERDICT:** VIABLE - but don't expect a premium

### Close Assessment

| Factor | Analysis |
|--------|----------|
| Wind-down costs | $5M (severance, customer transition) |
| Customer impact | Users would migrate to alternatives |
| Employee impact | 40 people need redeployment or exit |
| Resource redeployment | Engineers could strengthen #1 business |

**CLOSE VERDICT:** VIABLE - cleaner than endless investment

### Recommendation

**Decision:** SELL (first choice) or CLOSE (if no buyer in 6 months)

**Rationale:** Eight years at #5 position proves this business will never be a leader. "Supports our ecosystem" is a common rationalization for subsidizing failure. Every dollar invested here is a dollar not invested in businesses where you CAN be #1 or #2.

**Timeline:**
- Month 1-2: Explore sale to strategic acquirers
- Month 3-4: Broaden to financial buyers
- Month 5-6: Decision point - if no acceptable offer, close
- Month 7-12: Execute sale or wind-down

**Resources freed:** $10M+ annual investment, 40 engineers

### Addressing "Supports Our Ecosystem"

This is the most common argument for keeping weak businesses. Challenge it:

1. **Quantify the support:** What specific revenue/users does this drive to other businesses?
2. **Alternative delivery:** Could another product provide this support?
3. **True cost:** Is the ecosystem benefit worth the full investment?

If "supports ecosystem" were worth the cost, this business would be profitable. It's not. The ecosystem benefit is smaller than you want to believe.

### The Hard Truth

You have subsidized a #5 player for 8 years. Your best engineers are working on something that doesn't matter in the market. Your competitors have consolidated while you've stood still.

Welch: "The cruelest thing you can do is keep investing in a loser while your winners starve for resources."

Sell it, close it, and put those resources somewhere you can actually win.

---

## Integration

This skill is part of the **Jack Welch** expert persona. Use it for portfolio strategy and investment allocation decisions. It pairs well with:
- **vitality-curve-assessment** for people decisions within business units
- **strategic-inflection-point-diagnosis** when market change is driving position decline
- **high-output-management-audit** if the issue is execution, not position