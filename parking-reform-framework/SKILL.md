---
name: parking-reform-framework
description: Analyze parking policies and requirements, drawing on Donald Shoup's research and Jeff Speck's practical implementation framework.
license: MIT
metadata:
  version: 1.0.4641
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- parking-reform-framework
- urban-planning
---

# Parking Reform Framework

Analyze parking policies and requirements, drawing on Donald Shoup's research and Jeff Speck's practical implementation framework. Diagnose how current parking policy undermines walkability and affordability, and recommend specific reforms.

---

## Constitutional Constraints

- **Evidence-based** - Cite Shoup's research and documented reform outcomes; do not rely on intuition
- **Acknowledge political reality** - Parking is emotional; reforms must be phased and communicated strategically
- **Complete picture** - Address supply, pricing, requirements, and management as interconnected system
- **Non-ideological framing** - Frame as fiscal responsibility, housing affordability, and market efficiency
- **Context sensitivity** - Downtown requirements differ from suburban; dense urban differs from small town

---

## When to Use

- Evaluating minimum parking requirements
- Analyzing downtown parking policy
- Housing affordability discussions (parking drives up costs)
- Discussing "free" parking costs
- Proposing parking reforms for walkability
- Defending elimination of parking minimums
- Analyzing parking's impact on urban form

---

## Don't Use When

- Diagnosing overall walkability (use `walkability-audit`)
- Redesigning specific streets (use `street-redesign-toolkit`)
- Opposing road expansion (use `induced-demand-analysis`)
- Non-urban contexts where parking is genuinely abundant

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| context | Yes | City type, downtown vs. suburban, current conditions |
| current_policy | Helpful | Minimum requirements, pricing, management |
| specific_issue | Helpful | What prompted the analysis (new development, downtown struggles, housing costs) |
| comparable_cities | No | Similar cities that have reformed |
| political_context | Helpful | Receptiveness to reform, stakeholder concerns |

---

## The Parking Problem Framework

### How Parking Requirements Destroy Walkability

**The Mechanism:**

| Requirement | Effect | Result |
|-------------|--------|--------|
| Minimum spaces per unit | Forces developers to build parking | Adds $5,000-$50,000 per space to development costs |
| Parking lots required | Buildings set back from street | Destroys street wall; creates dead zones |
| "Free" parking expectation | Driving subsidized; alternatives disadvantaged | More driving, more demand for parking |
| Oversupply of parking | Land dedicated to cars, not people | Lower density, worse walkability |

**Speck's formulation:** "Your downtown has 18 surface parking lots per square mile--more land dedicated to parked cars than to people. The parking lots create dead zones that make walking unpleasant, which drives more people to drive, which demands more parking. It's a death spiral."

### The Economics of "Free" Parking

**Hidden Costs (Shoup's research):**

| Cost | Amount | Who Pays |
|------|--------|----------|
| Surface parking space construction | $5,000-$15,000 | Everyone (built into prices) |
| Structured parking space construction | $25,000-$50,000 | Everyone (built into prices) |
| Land cost (opportunity cost) | Varies; often > construction | Everyone (reduced tax base) |
| Maintenance (annual) | $200-$500 per space | Everyone (built into prices) |

**The Subsidy Math:**

If parking costs $15,000 to build and is provided "free," that cost is passed to:
- Renters (higher rents, smaller apartments)
- Shoppers (higher retail prices)
- Employees (lower wages)
- Taxpayers (reduced tax base from parking lots vs. buildings)

**Key insight:** "Free parking makes the parking situation worse." By subsidizing driving, we increase demand for parking while using land for parking instead of productive uses.

---

## Parking Analysis Workflow

### Step 1: Document Current Policy

**Minimum Requirements Inventory:**

| Use | Current Requirement | Typical Ratio |
|----|---------------------|---------------|
| Residential (per unit) | [X] spaces | 1.0-2.0 typical |
| Retail (per 1,000 SF) | [X] spaces | 3.0-5.0 typical |
| Office (per 1,000 SF) | [X] spaces | 2.0-4.0 typical |
| Restaurant (per seat) | [X] spaces | 10-20 per 1,000 SF typical |
| Downtown exemptions? | [Yes/No] | Best practice: no minimums downtown |

**Street Parking Management:**

| Element | Current Status |
|---------|---------------|
| Pricing | [Free / Metered / Variable] |
| Time limits | [None / 2 hours / etc.] |
| Utilization monitoring | [Yes / No] |
| Revenue use | [General fund / Parking fund / District] |

**Supply Inventory (if available):**

| Type | Spaces | Utilization |
|------|--------|-------------|
| Street parking | [X] | [X]% |
| Surface lots | [X] | [X]% |
| Structured parking | [X] | [X]% |
| Private (required) | [X] | Often <50% |

### Step 2: Diagnose Problems

**Common Problems:**

| Problem | Indicator | Consequence |
|---------|-----------|-------------|
| **Oversupply** | <85% utilization | Land wasted; price signals broken |
| **Undersupply** | >95% utilization | Cruising for parking; double-parking |
| **Mispricing** | Price doesn't vary with demand | Peak overflow, off-peak emptiness |
| **Requirements too high** | Developers request variances | Housing more expensive; buildings set back |
| **Requirements mismatch location** | Same rules downtown as highway strip | Downtown can't function as downtown |
| **"Free" street parking** | No meters or very low rates | Subsidizes driving; reduces turnover |

### Step 3: Calculate Costs of Current Policy

**Cost to Housing:**

| Element | Calculation |
|---------|-------------|
| Required spaces per unit | [X] |
| Construction cost per space | $[X] |
| Added cost per unit | [X] x $[X] = $[X] |
| % increase in unit cost | [X]% |
| Rent impact (30-year mortgage equivalent) | +$[X]/month |

**Cost to Urban Form:**

| Element | Impact |
|---------|--------|
| % of downtown land as surface parking | [X]% |
| Tax revenue loss vs. development | $[X] per acre |
| Walking distance increase | [X] feet between destinations |
| Building setbacks required | [X] feet (destroys street wall) |

**Cost to Transportation:**

| Element | Impact |
|---------|--------|
| Driving subsidy per space | $[X]/year |
| Additional VMT induced | [X] miles |
| Transit disadvantage | [X] trips shifted to driving |

### Step 4: Develop Reform Recommendations

**The Reform Menu:**

| Reform | What It Does | Difficulty | Impact |
|--------|--------------|------------|--------|
| **Eliminate minimums** | Let market determine parking | Medium | Transformative long-term |
| **Reduce minimums** | Lower requirements 25-50% | Low | Incremental improvement |
| **Downtown exemption** | No minimums in core | Medium | Enables downtown development |
| **Transit proximity exemption** | No minimums near transit | Low | Supports transit investment |
| **Price street parking** | Charge market-rate at meters | Medium | Reduces cruising, generates revenue |
| **Demand-responsive pricing** | Vary price to maintain 85% occupancy | Higher | Optimal management |
| **Parking maximums** | Cap parking rather than require it | Higher | Limits oversupply |
| **Shared parking allowances** | Let different uses share spaces | Low | Reduces total spaces needed |
| **Unbundle parking** | Sell/rent parking separately from housing | Medium | Reduces housing costs for non-drivers |
| **In-lieu fees** | Pay fee instead of building parking | Medium | Enables shared structures |

### Step 5: Phase Implementation

**Typical Phasing:**

| Phase | Timeframe | Actions |
|-------|-----------|---------|
| **1: Low-hanging fruit** | 0-6 months | Price street parking; allow shared parking; reduce minimums 25% |
| **2: Downtown focus** | 6-18 months | Eliminate minimums downtown; parking district management |
| **3: Citywide reform** | 18-36 months | Eliminate minimums citywide; implement maximums in dense areas |
| **4: Optimization** | Ongoing | Demand-responsive pricing; manage system holistically |

---

## Output Format

```markdown
## Parking Policy Analysis: [City/District Name]

### Current Policy Summary

**Minimum Requirements:**

| Use | Requirement | Problem |
|-----|-------------|---------|
| [Use 1] | [X] spaces per [unit] | [Analysis] |
| [Use 2] | [X] spaces per [unit] | [Analysis] |

**Street Parking:**
- Pricing: [Current status]
- Management: [Current status]
- Utilization: [If known]

**Supply Condition:**
- Total spaces: [X]
- Estimated utilization: [X]%
- Oversupply/undersupply: [Assessment]

---

### Problem Diagnosis

**1. Cost to Housing:**
- Required parking adds $[X] per unit
- This increases rents by approximately $[X]/month
- [X]% of unit cost is parking

**2. Cost to Urban Form:**
- [X]% of downtown is surface parking
- Building setbacks of [X] feet required
- Street wall broken at [specific locations]

**3. Cost to Transportation:**
- "Free" parking subsidizes driving by $[X] per space annually
- Encourages [X] additional VMT
- Undermines transit competitiveness

**4. Death Spiral Dynamic:**
> "The parking lots create dead zones that make walking unpleasant, which drives more people to drive, which demands more parking."

---

### Reform Recommendations

**Tier 1: Immediate (0-6 months)**

| Reform | Rationale | Expected Outcome |
|--------|-----------|------------------|
| [Reform 1] | [Why now] | [What changes] |
| [Reform 2] | [Why now] | [What changes] |

**Tier 2: Short-Term (6-18 months)**

| Reform | Rationale | Expected Outcome |
|--------|-----------|------------------|
| [Reform 1] | [Why this timing] | [What changes] |
| [Reform 2] | [Why this timing] | [What changes] |

**Tier 3: Medium-Term (18-36 months)**

| Reform | Rationale | Expected Outcome |
|--------|-----------|------------------|
| [Reform 1] | [Why phased] | [What changes] |

---

### Addressing Common Objections

| Objection | Response |
|-----------|----------|
| "Businesses need parking" | Businesses need customers. Walkable downtowns generate more spending per acre than parking-surrounded retail. |
| "People will park in neighborhoods" | Implement residential permit parking where needed. Price street parking to manage demand. |
| "There's not enough parking now" | Perception vs. reality. Measure actual utilization before adding supply. |
| "Developers will still build parking" | Yes, market-appropriate amounts. The goal is removing the mandate, not banning parking. |
| "This hurts low-income residents" | Parking requirements raise housing costs. Low-income households are least likely to own cars but pay for parking anyway. |

---

### Comparable City Reforms

| City | Reform | Outcome |
|------|--------|---------|
| [City 1] | [What they did] | [Results] |
| [City 2] | [What they did] | [Results] |
| [City 3] | [What they did] | [Results] |

---

### Implementation Notes

**Political Strategy:**
- [Key stakeholders to engage]
- [Framing recommendations]
- [Sequencing considerations]

**Measurement:**
- [How to track utilization]
- [How to measure housing cost impacts]
- [Success metrics]

---

### The Bottom Line

[Summary statement connecting parking reform to broader walkability/affordability goals]
```

---

## Example Summary

**Input:** "Our downtown has a lot of surface parking lots but business owners say there's not enough parking. We require 2 spaces per residential unit and 4 per 1,000 SF retail. Should we reduce parking requirements?"

**Output summary:**

**Diagnosis:**
- 2 spaces per unit adds ~$30,000-$60,000 to each unit cost (+$200-400/month rent)
- Surface lots likely underutilized (typical: 50-60% occupancy)
- "Not enough parking" perception often means "not enough parking directly in front of my store for free"
- Parking lots create walking dead zones that suppress the foot traffic businesses actually need

**Recommended Reforms:**

1. **Immediate:** Price street parking ($1-2/hour) to improve turnover; the "not enough parking" complaint is usually about turnover, not total supply
2. **6 months:** Eliminate parking minimums downtown; allow shared parking between uses
3. **18 months:** Reduce minimums citywide by 50%; allow unbundled parking in multifamily

**Comparable success:**
- Buffalo eliminated minimums citywide (2017): housing development increased, no parking crisis
- Minneapolis reduced minimums, then eliminated (2021): downtown development accelerated
- Austin eliminated minimums (2023): new transit-adjacent housing now viable

**Framing:** This isn't about taking away parking. It's about letting the market decide how much parking to build instead of mandating oversupply that makes housing unaffordable and downtowns unwalkable.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Business owner opposition | Lead with turnover/pricing; "you don't have a supply problem, you have a management problem" |
| Suburban context | Acknowledge different conditions; focus on reducing minimums rather than eliminating |
| No utilization data | Recommend parking study before major decisions; use rules of thumb cautiously |
| Political resistance | Propose pilot district (downtown only); emphasize reversibility |
| Genuinely undersupplied | Rare, but possible; recommend pricing and management before adding supply |

---

## Integration

This skill is part of the **Jeff Speck** expert persona. It operationalizes the parking reform component of the walkability framework.

**Speck's core insight:** "Free parking makes the parking situation worse."

The skill draws heavily on **Donald Shoup's** research (*The High Cost of Free Parking*) and applies it within Speck's practical reform framework.

Pairs with:
- **walkability-audit** - Parking problems often surface in "comfortable" and "interesting" condition failures
- **street-redesign-toolkit** - Reclaiming surface lots enables street wall reconstruction

---

## Success Criteria

A successful parking reform analysis:
- [ ] Documented current requirements and their costs
- [ ] Calculated housing cost impact of parking mandates
- [ ] Identified the parking-walkability death spiral
- [ ] Proposed phased reforms appropriate to political context
- [ ] Addressed common objections with evidence
- [ ] Referenced comparable cities that have successfully reformed
- [ ] Connected parking reform to broader walkability and affordability goals