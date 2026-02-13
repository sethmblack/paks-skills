---
name: induced-demand-analysis
description: Evaluate proposed road expansion projects through the lens of induced demand. Explain why adding capacity won't solve congestion.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
  - induced-demand-analysis
  - urban-planning
---

# Induced Demand Analysis

Evaluate proposed road expansion projects through the lens of induced demand. Explain why adding capacity won't solve congestion--it will create more traffic. Provide evidence-based counter-arguments and propose alternative approaches to mobility challenges.

---

## Constitutional Constraints

- **Evidence-based only** - Cite specific research (Duranton & Turner, FHWA studies, documented case studies); do not rely on intuition
- **Acknowledge nuance** - Induced demand is strongest in congested corridors; be honest about contexts where it's less applicable
- **Propose alternatives** - Don't just criticize expansion; offer what WILL work (transit, land use, pricing, demand management)
- **Non-political framing** - Frame as fiscal responsibility and practical outcomes, not ideology

---

## When to Use

- Road widening or expansion project proposed
- Highway expansion justified by congestion relief
- "Build our way out of traffic" arguments
- Congestion being treated as a capacity problem
- Defending road diets against "traffic will get worse" claims
- Explaining why adding lanes didn't reduce congestion

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| project_description | Yes | The proposed road expansion or widening project |
| justification_given | Helpful | How proponents justify the project (congestion relief, safety, economic development) |
| cost_estimate | Helpful | Estimated project cost |
| current_conditions | Helpful | Current traffic levels, congestion patterns |
| context | Helpful | Urban/suburban, local/regional, transit availability |

---

## The Induced Demand Framework

### What Is Induced Demand?

**Definition:** Building more road capacity generates more traffic. When you add lanes to a congested highway, traffic initially improves, then returns to pre-expansion congestion levels as new trips are induced.

**Speck's Formulation:** "The great intellectual black hole in city planning, the one professional certainty that every thoughtful person seems to acknowledge, yet almost no one is willing to act upon."

**The Mechanism:** New road capacity makes driving faster/easier, which:
1. Shifts trips from other routes to the expanded road
2. Shifts trips from other times to peak hours
3. Shifts trips from other modes (transit, carpool) to driving alone
4. Induces entirely new trips that wouldn't have been made
5. Over time, shifts development to car-dependent locations

### The Research

**Duranton & Turner (2011):**
"Fundamental Law of Road Congestion" - A 10% increase in lane miles induces a 10% increase in vehicle miles traveled within a few years. "Roads cause traffic."

**FHWA Research:**
Adding capacity provides temporary relief (2-5 years), then traffic returns to congested levels.

**Key Insight:** "Just as more lanes invite more traffic, fewer lanes invite less. Congestion is the constant. Absent congestion pricing, it is the only real constraint to driving."

### The Inverse: Reduced Demand (Traffic Evaporation)

When road capacity is removed, traffic doesn't simply redistribute to other roads--some of it disappears. People:
- Change routes
- Change travel times
- Change modes (transit, bike, walk)
- Change destinations
- Combine trips or eliminate them
- Over time, change where they live and work

**Evidence:** When highways have closed for repairs or removal, predicted "carmageddon" rarely materializes. San Francisco's Embarcadero removal, Seoul's Cheonggyecheon removal, and dozens of other cases show traffic evaporation.

---

## Analysis Process

### Step 1: Understand the Proposed Project

| Question | Response |
|----------|----------|
| What is being built? | [Lanes, miles, interchange, etc.] |
| What is the justification? | [Congestion relief, safety, economic development] |
| What is the cost? | [$X million/billion] |
| What is the current traffic level? | [ADT, congestion rating] |
| What alternatives were considered? | [Transit, demand management, pricing, land use] |

### Step 2: Apply Induced Demand Analysis

**Projected Outcomes:**

| Time Horizon | Predicted Traffic | Evidence |
|--------------|-------------------|----------|
| Opening day | Temporary improvement | Standard pattern |
| Year 3-5 | Return to baseline congestion | Duranton & Turner research |
| Year 10+ | Worse than baseline (new development) | Land use response to capacity |

**What Will Actually Happen:**
1. Traffic initially improves (honeymoon period)
2. Word spreads that the route is faster
3. Drivers shift from other routes/times/modes
4. Congestion returns within 3-5 years
5. Development patterns adjust to new capacity
6. Congestion exceeds pre-expansion levels
7. Demand grows for the NEXT expansion

### Step 3: Calculate True Costs

**Direct Costs:**
- Construction: $[X]
- Maintenance (20-year lifecycle): $[X]
- Land acquisition: $[X]

**Induced Costs (often ignored):**
- Increased VMT -> increased crashes
- Increased VMT -> increased emissions
- Sprawl-inducing development patterns
- Decreased transit viability
- Decreased property values near highway

**Per-Outcome Cost:**
- Cost per temporary congestion relief mile: $[X]
- Cost per permanent congestion relief mile: N/A (congestion returns)
- Alternative investment that would provide permanent relief: $[X]

### Step 4: Propose Alternatives

**What Actually Works:**

| Solution | How It Works | Evidence |
|----------|--------------|----------|
| **Congestion Pricing** | Charges for road use at peak times, shifting trips to other times/modes | Stockholm, London, Singapore all reduced congestion 20-30% permanently |
| **Transit Investment** | Provides alternative to driving, especially on congested corridors | Rail and BRT in congested corridors permanently reduce road demand |
| **Land Use Changes** | Mixed-use development reduces trip lengths and enables walking/biking | Walkable neighborhoods generate 50% fewer car trips |
| **Demand Management** | Employer programs, flexible schedules, remote work policies | Shifts demand without building anything |
| **Road Diets** | Converting excess lanes to other uses, accepting congestion as constraint | Maintains mobility while improving safety |

---

## Output Format

```markdown
## Induced Demand Analysis: [Project Name]

### Project Summary

**Proposal:** [What's being built]
**Justification:** [Why proponents say it's needed]
**Cost:** $[X]
**Timeline:** [Construction period]

---

### The Induced Demand Reality

**The Claim:** [What proponents promise - congestion relief, faster travel times]

**The Research:**
> "Just as more lanes invite more traffic, fewer lanes invite less. Congestion is the constant."

Duranton & Turner's "Fundamental Law of Road Congestion" demonstrates that a 10% increase in lane miles induces a 10% increase in vehicle miles traveled. This project proposes [X]% increase in capacity; evidence predicts [X]% increase in traffic within 5 years.

**What Will Actually Happen:**

| Year | Condition | Evidence |
|------|-----------|----------|
| 0 | Project opens, temporary improvement | Standard honeymoon period |
| 3-5 | Congestion returns to pre-expansion levels | Duranton & Turner, 75 years of highway data |
| 10+ | Congestion exceeds baseline; new development induces more traffic | Land use response to capacity |

**The History:**
- [Comparable expansion project 1] - promised relief, congestion returned in [X] years
- [Comparable expansion project 2] - [outcome]
- [Local example if available] - [outcome]

---

### True Cost Analysis

**What You're Buying:**

| Item | Cost | What You Get |
|------|------|--------------|
| Construction | $[X] | 3-5 years of relief |
| 20-year maintenance | $[X] | Maintained congestion |
| Land acquisition | $[X] | Lost tax base |
| **Total** | **$[X]** | **Temporary improvement, permanent induced demand** |

**Cost Per Outcome:**
- Cost per year of congestion relief: $[X] (until congestion returns)
- Cost per permanent congestion reduction: **Not achievable through capacity expansion**

**Induced Costs (Not in Budget):**
- Increased crashes from higher VMT
- Increased emissions from higher VMT
- Sprawl-inducing development shifts
- Reduced transit ridership/viability
- Neighborhood impacts from wider highway

---

### What Would Actually Work

**Alternative 1: Congestion Pricing**
- **How it works:** Charge variable tolls based on congestion levels
- **Cost:** $[X] (mostly electronic infrastructure)
- **Evidence:** Stockholm reduced congestion 22%, London 30%, Singapore maintains free-flow conditions
- **Bonus:** Generates revenue to fund alternatives

**Alternative 2: Transit Investment**
- **How it works:** Provide competitive alternative on the corridor
- **Cost:** $[X] (compare to highway expansion)
- **Evidence:** [Local or comparable transit success]
- **Bonus:** Serves people who can't or don't want to drive

**Alternative 3: Land Use Reform**
- **How it works:** Allow mixed-use development that reduces trip distances
- **Cost:** Policy change (near zero)
- **Evidence:** Walkable neighborhoods generate 50% fewer car trips per household
- **Bonus:** Increases tax base, improves public health

**Alternative 4: Accept Congestion as Constraint**
- **How it works:** Acknowledge that congestion is the only real check on driving demand
- **Cost:** $0
- **Evidence:** Congestion levels are remarkably stable across cities regardless of road supply
- **Bonus:** Stop spending billions on temporary relief

---

### The Real Question

This project proposes spending $[X] to achieve [stated goal].

**If the goal is congestion relief:** This will fail. Induced demand will return traffic to congested levels within 5 years. The money is wasted.

**If the goal is economic development:** Sprawl-inducing highway expansion doesn't create economic activity--it redistributes it. Walkable places generate more tax revenue per acre and create more jobs per dollar invested.

**If the goal is political cover:** This is the real reason most highway expansions happen. Officials can point to "doing something" even though the something doesn't work.

---

### Recommendation

**Do not approve this project as proposed.**

Instead:
1. [Specific alternative 1]
2. [Specific alternative 2]
3. [Specific alternative 3]

**The choice:** Spend $[X] for 3-5 years of temporary relief, or invest in solutions that provide permanent mobility improvements.

---

### Comparable Cases

| Project | Promise | Reality |
|---------|---------|---------|
| [Highway expansion 1] | Congestion relief | Congestion returned in [X] years |
| [Highway expansion 2] | Congestion relief | Now widening again |
| [Transit/pricing project] | [Promise] | [Success - permanent improvement] |

---

### Sources

- Duranton, G., & Turner, M. A. (2011). The fundamental law of road congestion. American Economic Review, 101(6), 2616-2652.
- Hymel, K. (2019). If you build it, they will drive: Measuring induced demand for vehicle travel in urban areas. Transport Policy, 76, 57-66.
- [Additional sources relevant to this analysis]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Rural highway (not congested) | Induced demand applies less in uncongested areas; focus on fiscal responsibility and alternative investments |
| Safety justification (not congestion) | Acknowledge safety concerns; propose lane narrowing and design changes instead of widening |
| "We've already committed funds" | Focus on sunk cost fallacy; compare future spending to alternatives |
| Political inevitability | Propose modifications: demand management, transit investment, congestion pricing to mitigate induced demand |
| Bridge/bottleneck removal | This is one case where capacity increase can provide lasting benefit--acknowledge the distinction |

---

## Example

**Input:** "The state DOT wants to widen I-95 from 6 to 10 lanes through our metro area. They say it will reduce congestion and improve travel times. The project costs $3 billion. Should we support it?"

**Output:**

## Induced Demand Analysis: I-95 Widening Project

### Project Summary

**Proposal:** Widen I-95 from 6 lanes to 10 lanes (add 2 lanes each direction)
**Justification:** Reduce congestion, improve travel times
**Cost:** $3 billion
**Timeline:** 5-7 years construction

---

### The Induced Demand Reality

**The Claim:** Adding 4 lanes will reduce congestion and improve travel times for commuters.

**The Research:**
> "Just as more lanes invite more traffic, fewer lanes invite less. Congestion is the constant."

Duranton & Turner's "Fundamental Law of Road Congestion" demonstrates that a 10% increase in lane miles induces a 10% increase in vehicle miles traveled. This project proposes a 67% increase in capacity (6 to 10 lanes); evidence predicts traffic will grow to fill every new lane within 5 years.

**What Will Actually Happen:**

| Year | Condition | Evidence |
|------|-----------|----------|
| 0 | Project opens with fanfare; travel times improve | Standard honeymoon period |
| 3-5 | Traffic grows 40-67%; congestion returns | Duranton & Turner; 75 years of US highway data |
| 10+ | Traffic exceeds pre-expansion; region demands 12+ lanes | Houston, Atlanta, Los Angeles patterns |

**The History:**
- **Houston Katy Freeway** - Widened to 26 lanes (world's widest). Within 3 years, worse congestion than before expansion.
- **Los Angeles I-405** - $1.1 billion widening. Travel times worse 5 years after completion.
- **Atlanta I-75/I-85** - Multiple widenings. Metro Atlanta has longest commutes in the country.

The pattern is universal: widen, fill, widen again, fill again. No American metro has ever built its way out of congestion.

---

### True Cost Analysis

**What You're Buying:**

| Item | Cost | What You Get |
|------|------|--------------|
| Construction | $3 billion | 3-5 years of relief |
| 20-year maintenance | $600 million | Maintained congestion |
| Land acquisition | Included | Lost tax base, displaced residents |
| **Total** | **$3.6 billion** | **Temporary improvement, permanent induced demand** |

**Cost Per Outcome:**
- Cost per year of congestion relief: $600-900 million (until congestion returns)
- Cost per permanent congestion reduction: **Not achievable through capacity expansion**

**Induced Costs (Not in Budget):**
- 67% more VMT = 67% more crashes, injuries, deaths
- 67% more VMT = 67% more emissions
- Sprawl acceleration as development follows highway capacity
- Transit ridership collapse (car trips faster during honeymoon period)
- Noise, pollution, community severance along corridor

---

### What Would Actually Work

**Alternative 1: Congestion Pricing ($200 million)**
- **How it works:** Dynamic tolls on I-95 that vary with congestion levels
- **Cost:** $200 million (electronic infrastructure)
- **Evidence:** Stockholm reduced peak congestion 22% permanently. Singapore maintains free-flow conditions on all expressways.
- **Bonus:** Generates $500+ million annually in revenue to fund alternatives
- **ROI:** Self-funding within 1 year

**Alternative 2: Regional Rail Expansion ($2 billion)**
- **How it works:** Parallel transit service on congested corridor
- **Cost:** $2 billion (same order as highway project)
- **Evidence:** Washington Metro removes 500,000+ daily car trips from regional roads
- **Bonus:** Serves population regardless of driving ability; generates transit-oriented development
- **ROI:** Permanent capacity expansion that doesn't induce highway traffic

**Alternative 3: Employer Demand Management ($50 million)**
- **How it works:** Incentives for flexible schedules, remote work, carpool matching
- **Cost:** $50 million over 5 years
- **Evidence:** Portland's SMART Trips program reduces drive-alone rates 10-15%
- **Bonus:** Reduces demand without building anything
- **ROI:** Cheapest intervention per trip reduced

**Alternative 4: Land Use Reform ($0)**
- **How it works:** Allow mixed-use development in currently single-use zones; reduce parking requirements
- **Cost:** Policy change only
- **Evidence:** Walkable neighborhoods generate 50% fewer car trips per household
- **Bonus:** Increases tax base, improves health, reduces infrastructure costs
- **ROI:** Net positive fiscal impact

---

### The Real Question

This project proposes spending $3.6 billion to achieve congestion relief that will disappear within 5 years.

**The math:**
- $3.6 billion / 5 years of relief = $720 million per year of temporary improvement
- After 5 years: back to current conditions (or worse)
- In 10 years: demands for 12-lane widening

**The alternative math:**
- $200 million congestion pricing: permanent 20%+ congestion reduction, generates revenue
- $2 billion rail: permanent capacity expansion, transit-oriented development
- $50 million demand management: immediate trip reduction
- $0 land use reform: generational transportation shift

For the cost of 5 years of temporary highway relief, you could permanently transform regional mobility.

---

### Recommendation

**Do not approve this project.**

Instead:
1. Implement congestion pricing on I-95 ($200M) - reduces demand 20%+, generates funding for alternatives
2. Accelerate regional rail project ($2B) - provides permanent parallel capacity
3. Reform land use to enable mixed-use, walkable development ($0) - reduces trip generation over time
4. Invest in employer demand management ($50M) - immediate trip reduction through behavior change

**The choice:** Spend $3.6 billion for 5 years of temporary relief, or spend less for permanent mobility transformation.

---

### Comparable Cases

| Project | Promise | Reality |
|---------|---------|---------|
| Houston Katy Freeway | Widest highway = no congestion | 26 lanes, worse traffic than before |
| LA I-405 Widening | $1.1B for relief | Travel times worse after 5 years |
| Stockholm Congestion Pricing | Reduce traffic 20% | Achieved. Still working 20 years later. |
| Seoul Cheonggyecheon | Removed highway | Traffic evaporated. Park created. Economy thrived. |

---

### The Bottom Line

> "The great intellectual black hole in city planning, the one professional certainty that every thoughtful person seems to acknowledge, yet almost no one is willing to act upon."

Everyone involved in this project knows induced demand is real. The research is clear. The precedents are unanimous. And yet the project moves forward because building highways is what DOTs do.

The question for your community: Do you want to spend $3.6 billion learning the same lesson Houston, LA, and Atlanta have already learned? Or do you want to be the metro that finally did something different?

---

## Integration

This skill is part of the **Jeff Speck** expert persona. Use it to counter road expansion projects and "build our way out" arguments. It pairs well with:
- **walkability-audit** for showing what communities could build instead
- **road-diet-design** for showing how existing capacity could be reallocated
