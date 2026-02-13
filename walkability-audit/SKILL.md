---
name: walkability-audit
description: "Systematically evaluate any place against Jeff Speck's General Theory of Walkability - for a walk to be favored, it must be useful, safe, comfortable, and interesting."
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
  - walkability-audit
  - urban-planning
---

# Walkability Audit

Systematically evaluate any place against Jeff Speck's General Theory of Walkability: for a walk to be favored, it must be **useful**, **safe**, **comfortable**, and **interesting**. Each condition is essential; none alone is sufficient.

---

## Constitutional Constraints

- **Evidence-based only** - Every assessment must be grounded in observable conditions or stated facts; do not invent conditions not mentioned
- **All four conditions required** - Do not skip conditions; a place that fails one test fails overall
- **Specific, not vague** - Recommendations must be actionable (lane widths, tree species, building requirements), not generic ("make it better")
- **Non-political framing** - Frame findings in terms of safety, economics, and practicality, not ideology

---

## When to Use

- Evaluating why a place doesn't feel walkable
- Assessing a downtown, neighborhood, corridor, or development proposal
- Diagnosing pedestrian-hostile conditions
- Prioritizing walkability improvements
- Reviewing site plans or street designs

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| place_description | Yes | Description of the place, street, or area being evaluated |
| photos | No | Images showing conditions (if provided, analyze visible elements) |
| context | No | City, population, climate, current policies, etc. |
| specific_concerns | No | Particular issues the user wants addressed |

---

## The Four-Condition Assessment

### Condition 1: USEFUL

**Core Question:** Are most aspects of daily life located close at hand and organized so walking serves them well?

**Assessment Criteria:**
- [ ] Daily destinations within 5-10 minute walk (groceries, coffee, services)
- [ ] Mixed-use zoning or de facto mixed use
- [ ] Connected street network (grid preferred over cul-de-sacs)
- [ ] Destinations distributed, not clustered in one inaccessible area
- [ ] Street connectivity ratio (intersections per square mile)

**Failure Indicators:**
- Single-use residential zoning with no services
- All commerce on highway strip, inaccessible by foot
- Dead-end street patterns requiring circuitous walking routes
- Destinations only accessible via high-speed arterials

**Scoring:**
- **Strong**: Multiple daily needs within 5-minute walk, connected grid
- **Moderate**: Some needs within walking distance, reasonable connectivity
- **Weak**: Few or no daily needs walkable, disconnected network
- **Failing**: Nothing to walk to; walking serves no practical purpose

---

### Condition 2: SAFE

**Core Question:** Has the street been designed to give pedestrians a fighting chance against automobiles?

**Assessment Criteria:**
- [ ] Travel lane widths (10 feet = good; 12+ feet = dangerous)
- [ ] Street configuration (two-way preferred over one-way)
- [ ] Crossing distances (shorter = safer)
- [ ] Curb extensions or bulb-outs at crossings
- [ ] Pedestrian refuge islands on wide streets
- [ ] Turning radii (tight = slower turns = safer)
- [ ] Speed: designed speed vs. posted speed vs. actual speed
- [ ] Sight lines at crossings

**Failure Indicators:**
- 12-foot or wider travel lanes
- Multiple lanes of fast, one-way traffic
- Long crossing distances with no refuge
- Wide turning radii allowing high-speed turns
- Missing crosswalks or crossing opportunities
- Streets that "feel like highways"

**Critical Insight:** "When children die at a crosswalk, it is natural to investigate the driver. Rarely do we investigate the crosswalk."

**Scoring:**
- **Strong**: Narrow lanes, two-way traffic, protected crossings, slow design speed
- **Moderate**: Some safety features but inconsistent; some dangerous crossings
- **Weak**: Wide lanes, fast traffic, difficult crossings; feels unsafe
- **Failing**: Pedestrians must take their lives in their hands to cross; highway-like conditions

---

### Condition 3: COMFORTABLE

**Core Question:** Does the street function as an outdoor living room with proper enclosure and climate modification?

**Assessment Criteria:**
- [ ] Street trees providing canopy (reduces perceived temperature by 15 degrees)
- [ ] Building height-to-street width ratio (1:3 to 1:1 ideal for enclosure)
- [ ] Buildings meeting sidewalk edge vs. setbacks with parking lots
- [ ] Sidewalk width adequate for walking plus lingering
- [ ] Protection from weather (awnings, arcades where appropriate)
- [ ] Seating opportunities (benches, ledges, outdoor dining)
- [ ] Absence of hostile design (anti-homeless features that make everyone uncomfortable)

**Failure Indicators:**
- No street trees; exposed to sun/wind/rain
- Buildings set back behind parking lots
- Wide street with low buildings = no sense of enclosure
- Narrow sidewalks squeezed between traffic and walls
- Blank walls or parking garages facing sidewalk
- No places to sit, rest, or linger

**The Enclosure Principle:** "Humans need a sense of defined space to feel comfortable. Streets without buildings at the edge feel exposed and hostile."

**Scoring:**
- **Strong**: Full tree canopy, buildings at edge, comfortable proportions, places to linger
- **Moderate**: Some trees, some enclosure, adequate but not inviting
- **Weak**: Few trees, setbacks or gaps, uncomfortable proportions
- **Failing**: No enclosure, no shade, hostile to human presence

---

### Condition 4: INTERESTING

**Core Question:** Are sidewalks lined by buildings with friendly faces--transparency, variety, and signs of life?

**Assessment Criteria:**
- [ ] Ground-floor transparency (windows, not blank walls)
- [ ] Entry frequency (something interesting every 15-20 feet ideal)
- [ ] Facade variety (narrow lots with different buildings vs. long monotonous walls)
- [ ] Signs of life (outdoor seating, planters, activity, displays)
- [ ] Vertical articulation (architectural detail, not flat surfaces)
- [ ] Signage and wayfinding that rewards attention
- [ ] Absence of dead zones (parking garages, blank walls, service areas)

**Failure Indicators:**
- Blank walls, tinted glass, or reflective surfaces at street level
- Long stretches without entries or windows
- Identical or monotonous facades
- No activity visible from sidewalk
- Parking structures or service areas facing street
- "Could be anywhere" architecture with no local character

**The Pedestrian's Visual Budget:** "Walkers need something interesting every 15-20 feet to maintain engagement."

**Scoring:**
- **Strong**: Transparent facades, frequent entries, varied and active frontage
- **Moderate**: Some transparency and variety, occasional dead zones
- **Weak**: Mostly inactive frontage, limited interest, many dead zones
- **Failing**: Nothing to look at; walking feels like a chore through a hostile environment

---

## Output Format

```markdown
## Walkability Audit: [Place Name/Description]

### Summary Scorecard

| Condition | Score | Key Issues |
|-----------|-------|------------|
| **Useful** | [Strong/Moderate/Weak/Failing] | [One-line summary] |
| **Safe** | [Strong/Moderate/Weak/Failing] | [One-line summary] |
| **Comfortable** | [Strong/Moderate/Weak/Failing] | [One-line summary] |
| **Interesting** | [Strong/Moderate/Weak/Failing] | [One-line summary] |

**Overall Assessment:** [Summary statement - remember, if any condition fails, the walk fails]

---

### Condition 1: USEFUL

**Score:** [Strong/Moderate/Weak/Failing]

**What's Working:**
- [Specific positive findings]

**What's Failing:**
- [Specific failures with evidence]

**Priority Interventions:**
1. [Specific, actionable recommendation]
2. [Specific, actionable recommendation]

---

### Condition 2: SAFE

**Score:** [Strong/Moderate/Weak/Failing]

**What's Working:**
- [Specific positive findings]

**What's Failing:**
- [Specific failures with evidence]

**Priority Interventions:**
1. [Specific intervention with dimensions, e.g., "Narrow lanes from 12 to 10 feet"]
2. [Specific intervention]

---

### Condition 3: COMFORTABLE

**Score:** [Strong/Moderate/Weak/Failing]

**What's Working:**
- [Specific positive findings]

**What's Failing:**
- [Specific failures with evidence]

**Priority Interventions:**
1. [Specific intervention, e.g., "Plant street trees at 30-foot intervals"]
2. [Specific intervention]

---

### Condition 4: INTERESTING

**Score:** [Strong/Moderate/Weak/Failing]

**What's Working:**
- [Specific positive findings]

**What's Failing:**
- [Specific failures with evidence]

**Priority Interventions:**
1. [Specific intervention]
2. [Specific intervention]

---

### Priority Recommendations (Ranked)

1. **[Most critical intervention]** - [Why this is priority #1; which conditions it addresses]
2. **[Second priority]** - [Rationale]
3. **[Third priority]** - [Rationale]

### Quick Wins (Low-cost, high-impact)

- [Actions that can be done immediately with minimal investment]
- [E.g., "Restripe for narrower lanes - can be done with scheduled maintenance"]

### Comparable Success Stories

- [City that addressed similar issues] - [What they did, what results they achieved]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient information | Note which conditions cannot be assessed; ask for specific missing information |
| Photos provided without description | Analyze visible conditions in photos; note what cannot be determined from images alone |
| Single-condition focus requested | Provide full four-condition audit anyway; explain interdependence |
| Defensive user ("this is fine") | Lead with safety data; "Nobody likes seeing people get hurt" is hardest to argue with |

---

## Example

**Input:** "Our main street has four lanes plus turn lanes, parking lots in front of most businesses, and people complain there's nowhere good to eat downtown even though we have restaurants."

**Output:**

## Walkability Audit: Main Street Downtown

### Summary Scorecard

| Condition | Score | Key Issues |
|-----------|-------|------------|
| **Useful** | Moderate | Restaurants exist but parking-lot pattern discourages walking between them |
| **Safe** | Failing | Four lanes + turn lanes = highway conditions through downtown |
| **Comfortable** | Weak | Parking lots destroy enclosure; likely minimal tree canopy |
| **Interesting** | Weak | Buildings set back; street-level experience is parking lots, not storefronts |

**Overall Assessment:** Your downtown has useful destinations but has been designed to be approached only by car. The four-lane configuration and parking-lot frontages make walking feel dangerous and unpleasant. Even though restaurants exist, people "can't find anywhere to eat" because the walking experience is hostile--they drive through without stopping.

---

### Condition 1: USEFUL

**Score:** Moderate

**What's Working:**
- Restaurants and destinations exist downtown
- Some concentration of uses in one area

**What's Failing:**
- Parking-lot-fronted pattern means destinations are scattered behind asphalt
- Even short walks between businesses require crossing parking lots
- Likely missing key daily needs (groceries, services) that would generate regular foot traffic

**Priority Interventions:**
1. Require new development to build to sidewalk edge, not behind parking
2. Allow mixed-use development to add housing and daily services downtown
3. Consider small-format grocery or market to create daily walking destination

---

### Condition 2: SAFE

**Score:** Failing

**What's Working:**
- [None identified based on description]

**What's Failing:**
- Four travel lanes + turn lanes = approximately 60-70 feet of roadway
- This is highway design, not downtown design
- Crossing distances are dangerous; high speeds likely
- Pedestrians must "take their lives in their hands" to cross

**Priority Interventions:**
1. **Road diet**: Convert four lanes to three (two travel + center turn lane) - studies show this reduces crashes by 19-47% without reducing capacity
2. Narrow lanes from likely 12 feet to 10 feet (NACTO standard)
3. Use reclaimed space for protected bike lanes and wider sidewalks
4. Add curb extensions at crosswalks to reduce crossing distance
5. Consider converting to two-way if currently one-way

---

### Condition 3: COMFORTABLE

**Score:** Weak

**What's Working:**
- [Cannot assess tree canopy from description; likely minimal if parking-lot pattern]

**What's Failing:**
- Parking lots in front of businesses destroy street enclosure
- Wide roadway + setback buildings = no sense of "outdoor room"
- Pedestrians exposed to weather with no shade or protection

**Priority Interventions:**
1. Plant street trees at 30-foot intervals on both sides (creates canopy in 10-15 years)
2. Require parking behind or beside buildings, not in front
3. Add street furniture: benches, planters, bike racks at sidewalk level
4. Long-term: Encourage infill development that closes gaps in building wall

---

### Condition 4: INTERESTING

**Score:** Weak

**What's Working:**
- Restaurants exist and presumably have some storefront presence

**What's Failing:**
- Parking-lot pattern means street experience is asphalt, not storefronts
- Buildings set back = blank or distant facades
- Walking from restaurant to restaurant means crossing parking lots, not strolling past shops

**Priority Interventions:**
1. Incentivize facade improvements: transparency, signage, outdoor seating
2. Require new construction to have entries directly on sidewalk
3. Add wayfinding signage to make destinations legible to pedestrians
4. Consider tactical urbanism: temporary planters, seating, events in parking spaces

---

### Priority Recommendations (Ranked)

1. **Road diet (4 lanes to 3)** - Addresses safety immediately; creates space for comfort improvements; restriping costs almost nothing
2. **Street trees** - Addresses comfort; creates visual interest; long-term investment that pays compound returns
3. **Parking-to-rear requirements** - Addresses comfort and interest; rebuilds street wall over time

### Quick Wins (Low-cost, high-impact)

- Restripe main street with narrower lanes during scheduled maintenance (Cedar Rapids did this for nearly zero additional cost)
- Add curb extensions with paint and planters as tactical pilot
- Allow restaurants to expand outdoor seating onto parking spaces

### Comparable Success Stories

- **Lancaster, California** - Transformed car-dominated main street into walkable plaza; $11.5M investment generated $280M economic impact
- **Cedar Rapids, Iowa** - Restriped downtown streets for narrower lanes and parking at near-zero additional cost

---

**The Bottom Line:** Your downtown has destinations. It doesn't have walkability. Fix the street, and people will find the restaurants that were there all along.

---

## Integration

This skill is part of the **Jeff Speck** expert persona. Use it to diagnose any place against the four conditions of walkability. It pairs well with:
- **road-diet-design** for detailed street reconfiguration after audit identifies safety as a failing condition
- **induced-demand-analysis** when audit recommendations face "but traffic!" objections
