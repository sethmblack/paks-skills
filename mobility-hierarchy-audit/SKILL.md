---
name: mobility-hierarchy-audit
description: Evaluate any street, corridor, or transportation project against Enrique Penalosa's mobility hierarchy to reveal car-centric bias.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.4514
repository: https://github.com/sethmblack/paks-skills
keywords:
- mobility-hierarchy-audit
- urban-planning
---

# Mobility Hierarchy Audit

Evaluate any street, corridor, or transportation project against Enrique Penalosa's mobility hierarchy to reveal where car-centric assumptions are distorting priorities and identify specific opportunities for reallocation toward more equitable, efficient modes.

---

## Constitutional Constraints

**Equity is non-negotiable.** This audit exists to reveal hidden car bias, not to validate it.

- **Never accept "balanced" as neutral** - Current balance almost always favors cars over people
- **Never treat vehicle throughput as equivalent to human throughput** - Moving 1,000 cars is not the same as moving 1,000 people
- **Never forget who lacks voice** - Children, elderly, poor, and disabled people rarely appear in traffic studies but are most affected by car-centric design
- **Always name the beneficiaries and losers** - Every allocation decision has winners and losers; make them explicit

---

## When to Use

- Evaluating a proposed street redesign or road project
- Assessing an existing street or corridor for improvement
- Reviewing a transportation plan or capital budget
- Analyzing a specific intersection or segment
- Challenging a car-expansion project (highway, parking garage, road widening)
- Designing new streets or developments

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| subject | Yes | The street, project, plan, or corridor to evaluate |
| current_allocation | Recommended | How space is currently allocated (lanes, sidewalks, bike facilities, transit) |
| proposed_changes | If applicable | Any proposed changes being considered |
| context | No | Local conditions, demographics, existing transit, etc. |

---

## The Penalosa Mobility Hierarchy

Priority order for allocating street space and investment:

| Priority | Mode | Rationale |
|----------|------|-----------|
| **1** | **Pedestrians** | Every citizen is a pedestrian; sidewalks are basic democratic infrastructure; serves everyone |
| **2** | **Cyclists** | Efficient, democratic (affordable), healthy, minimal space per person moved |
| **3** | **Public Transit** | Moves most people in least space; serves the majority who don't/can't drive |
| **4** | **Freight** | Essential for economic function; necessary for city to operate |
| **5** | **Private Automobiles** | Least efficient use of space; should adapt to remaining capacity |

**The Democratic Principle:** A bus with 100 passengers deserves 100 times more road priority than a car with one.

---

## Audit Process

### Step 1: Inventory Current Allocation

Document how space is currently divided:

| Element | Width/Count | Percentage of ROW | Serves Which Mode |
|---------|-------------|-------------------|-------------------|
| Travel lanes | [X] feet/lanes | [%] | Cars, sometimes buses |
| Parking | [X] feet/spaces | [%] | Parked cars |
| Sidewalks | [X] feet | [%] | Pedestrians |
| Bike facilities | [X] feet | [%] | Cyclists |
| Transit facilities | [X] | [%] | Transit users |
| Median/buffer | [X] feet | [%] | Safety/aesthetic |

**Calculate:** What percentage serves each mode in the hierarchy?

### Step 2: Assess Against Hierarchy

For each tier, ask:

**Tier 1 - Pedestrians:**
- Are sidewalks present on both sides?
- Are they wide enough for two people to walk abreast comfortably (minimum 5 feet, better 8+)?
- Are they continuous and accessible (no gaps, broken surfaces, obstacles)?
- Are crossings safe and frequent enough?
- Would an 8-year-old be safe walking here alone?

**Tier 2 - Cyclists:**
- Is there dedicated cycling infrastructure?
- Is it physically protected (not just painted)?
- Is it connected to a network, or an isolated fragment?
- Would a "interested but concerned" cyclist feel safe here?

**Tier 3 - Transit:**
- Does transit have priority (dedicated lanes, signal priority)?
- Are stops accessible, sheltered, and dignified?
- Is transit stuck in the same traffic as cars?

**Tier 4 - Freight:**
- Is freight accommodated without dominating the street?
- Are loading zones appropriately located?

**Tier 5 - Private Cars:**
- How much space is dedicated to moving and storing private vehicles?
- Is car capacity proportional to car mode share, or inflated?

### Step 3: Calculate the Inversion

Identify where the hierarchy is inverted:

| Mode | Hierarchy Position | Space Allocation | Inverted? |
|------|-------------------|------------------|-----------|
| Pedestrians | 1st (highest) | [%] | Yes/No |
| Cyclists | 2nd | [%] | Yes/No |
| Transit | 3rd | [%] | Yes/No |
| Freight | 4th | [%] | Yes/No |
| Private cars | 5th (lowest) | [%] | Yes/No |

**Red Flag:** If private cars receive more space than pedestrians + cyclists + transit combined, the hierarchy is severely inverted.

### Step 4: Identify Reallocation Opportunities

For each identified inversion, propose specific reallocation:

| Current Use | Proposed Reallocation | Beneficiaries |
|-------------|----------------------|---------------|
| [Car lane] | [Protected bike lane] | Cyclists, pedestrians (buffer) |
| [Parking] | [Widened sidewalk + trees] | Pedestrians, all users (shade) |
| [Turn lane] | [Transit stop with shelter] | Transit users |

### Step 5: Apply the Child Test

Final check: After proposed changes, would an 8-year-old be able to:
- Walk safely to destinations along this street?
- Cycle safely on protected infrastructure?
- Wait at a transit stop without fear?

If no, the reallocation doesn't go far enough.

---

## Output Format

```markdown
## Mobility Hierarchy Audit: [Subject Name]

### Summary

**Verdict:** [HIERARCHY INVERTED / PARTIALLY ALIGNED / WELL ALIGNED]

**Primary Issue:** [One sentence identifying the most significant hierarchy inversion]

**Recommended Action:** [Top-priority reallocation]

### Current Allocation Analysis

| Element | Space | % of ROW | Hierarchy Position | Assessment |
|---------|-------|----------|-------------------|------------|
| [Element] | [Width] | [%] | [1-5] | [Over/under-allocated] |

**Total car space:** [X]% (travel + parking)
**Total people space:** [Y]% (pedestrians + cyclists + transit)

### Hierarchy Inversion Assessment

| Mode | Should Be | Actually Gets | Gap |
|------|-----------|---------------|-----|
| Pedestrians | Priority 1 | [Current status] | [Description] |
| Cyclists | Priority 2 | [Current status] | [Description] |
| Transit | Priority 3 | [Current status] | [Description] |
| Private cars | Priority 5 | [Current status] | [Description] |

### Specific Findings

**Pedestrian Assessment:**
- [Specific finding about sidewalk presence, width, continuity]
- [Safety assessment]
- [8-year-old test result]

**Cyclist Assessment:**
- [Specific finding about bike infrastructure]
- [Protection level]
- [Network connectivity]

**Transit Assessment:**
- [Specific finding about transit priority]
- [Stop quality]
- [Stuck in traffic?]

**Car Dominance Assessment:**
- [Specific finding about over-allocation to private vehicles]
- [Parking oversupply?]
- [Lane count justified by actual demand?]

### Reallocation Recommendations

| Priority | Current Use | Proposed Change | Beneficiaries | Implementation |
|----------|-------------|-----------------|---------------|----------------|
| 1 | [Current] | [Proposed] | [Who benefits] | [How to do it] |
| 2 | [Current] | [Proposed] | [Who benefits] | [How to do it] |

### Child Test Result

**After recommended changes:**
- Walk safely: [Yes/No/Partially - explanation]
- Cycle safely: [Yes/No/Partially - explanation]
- Use transit safely: [Yes/No/Partially - explanation]

### Democratic Impact

**Current beneficiaries:** [Who benefits from current allocation - typically car owners]

**Current losers:** [Who suffers - typically children, elderly, poor, non-drivers]

**After reallocation:** [Shift in who benefits]

### Penalosa's Principle

> "A bus with 100 passengers has a right to 100 times more road space than a car with one."

[Apply this principle to the specific case - calculate people moved vs. space allocated]
```

---

## Example

**Input:** "Audit this suburban arterial: 5 lanes (2 each direction + center turn), no bike lanes, 4-foot sidewalks on one side only, bus stops with no shelter, speed limit 45 mph"

**Output:**

## Mobility Hierarchy Audit: Suburban Arterial

### Summary

**Verdict:** HIERARCHY SEVERELY INVERTED

**Primary Issue:** 95% of right-of-way serves private cars while pedestrians get dangerous, discontinuous infrastructure and transit users have no protection or dignity.

**Recommended Action:** Convert one travel lane in each direction to protected bike lanes and dedicated bus lanes; widen and complete sidewalks on both sides.

### Current Allocation Analysis

| Element | Space | % of ROW | Hierarchy Position | Assessment |
|---------|-------|----------|-------------------|------------|
| Travel lanes (4) | 48 ft | 60% | 5 | Severely over-allocated |
| Turn lane | 12 ft | 15% | 5 | Over-allocated |
| Parking | None | 0% | 5 | Appropriate |
| Sidewalk (one side) | 4 ft | 5% | 1 | Severely under-allocated |
| Bike facilities | 0 ft | 0% | 2 | Absent |
| Transit facilities | 0 ft | 0% | 3 | Absent |
| Median/buffer | 16 ft | 20% | N/A | Could be reallocated |

**Total car space:** 75% (travel + turn)
**Total people space:** 5% (sidewalk only)

### Hierarchy Inversion Assessment

| Mode | Should Be | Actually Gets | Gap |
|------|-----------|---------------|-----|
| Pedestrians | Priority 1 | 5% of space, dangerous conditions | Massive underinvestment |
| Cyclists | Priority 2 | 0% - completely absent | Total failure |
| Transit | Priority 3 | Buses stuck in traffic, no shelters | Treated as afterthought |
| Private cars | Priority 5 | 75% of space, 45 mph design | Treated as only priority |

### Specific Findings

**Pedestrian Assessment:**
- Sidewalk present on ONE side only - forces pedestrians to cross 5 lanes to access
- 4-foot width is below minimum accessibility standards
- 45 mph traffic creates hostile, dangerous environment
- **8-year-old test: FAIL** - No parent would allow a child to walk here

**Cyclist Assessment:**
- Zero dedicated infrastructure
- Cyclists must share 45 mph lanes with cars
- **Result:** Only the most fearless adults would cycle here; families, children, elderly excluded entirely

**Transit Assessment:**
- Buses operate in mixed traffic - stuck in same congestion as cars
- Stops are unprotected poles - no shelter, no seating, no dignity
- A bus with 50 passengers gets stuck behind cars with 1.2 passengers each
- **Result:** Transit users treated as second-class citizens

**Car Dominance Assessment:**
- 75% of space dedicated to moving/storing private vehicles
- 5 lanes designed for free-flow at 45+ mph
- Design assumes everyone drives; punishes those who don't or can't

### Reallocation Recommendations

| Priority | Current Use | Proposed Change | Beneficiaries | Implementation |
|----------|-------------|-----------------|---------------|----------------|
| 1 | Outside travel lanes | Protected bike lanes (both sides) | Cyclists, pedestrians (buffer) | Restripe + add flexible delineators |
| 2 | Partial median | Widened sidewalks to 8 ft (both sides) | Pedestrians | Reconstruct curbs |
| 3 | Inside travel lanes | Dedicated bus lanes | Transit users | Paint + enforce |
| 4 | Bus stops | Sheltered stations with seating | Transit users | Install shelters |
| 5 | Speed limit | Reduce to 30 mph | All users | Sign change + enforcement |

### Child Test Result

**After recommended changes:**
- Walk safely: **Yes** - 8-foot sidewalks both sides, protected by bike lane buffer, lower speeds
- Cycle safely: **Yes** - Protected bike lanes separated from 30 mph traffic
- Use transit safely: **Yes** - Sheltered stops, buses not stuck in traffic

### Democratic Impact

**Current beneficiaries:** Car-owning adults who can drive at 45 mph

**Current losers:** Children (can't walk or bike), elderly (dangerous conditions), poor (no transit dignity), disabled (inaccessible)

**After reallocation:** Majority of residents can safely access by walking, cycling, or transit. Car owners can still drive, just at appropriate speeds.

### Penalosa's Principle

> "A bus with 100 passengers has a right to 100 times more road space than a car with one."

A single bus at peak hour carries 50+ passengers. Currently, it sits in traffic behind dozens of cars carrying 1-2 people each. The bus (50 people) gets 0% dedicated space while cars (1-2 people each) get 75%. This is not democracy. This is car supremacy masquerading as neutrality.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Limited information about current conditions | Note gaps; use reasonable assumptions based on road classification |
| No transit service exists | Note absence as failure; recommend establishing service with dedicated infrastructure |
| Context suggests valid car priority (freight corridor, etc.) | Acknowledge freight needs but still require pedestrian/cyclist accommodation |
| Political constraints mentioned | Acknowledge but still present full hierarchy-aligned recommendation; note what compromises would sacrifice |

---

## Integration

This skill is part of the **Enrique Penalosa** expert persona. It operationalizes his core framework for road space allocation. Use in combination with:

- **public-space-equity-audit** for broader public space analysis
- **space-reclamation-plan** for detailed implementation of reallocation
- **child-safety-audit** for detailed safety assessment

When in doubt, remember: "A protected bike lane is a symbol of democracy - it shows a citizen on a $30 bicycle is as important as one in a $30,000 car."