---
name: transit-oriented-development-audit
description: Evaluate a proposed or existing development near transit against TOD best practices using Peter Calthorpe's framework. Assess compliance with the six core elements of successful TOD and generate specific recommendations with projected performance metrics.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
  - transit-oriented-development-audit
  - urban-planning
---

# Transit-Oriented Development Audit

Evaluate a proposed or existing development near transit against TOD best practices using Peter Calthorpe's framework. Assess compliance with the six core elements of successful TOD and generate specific recommendations with projected performance metrics.

---

## Constitutional Constraints

- **Do not** approve developments that merely claim "transit-oriented" without meeting substantive criteria
- **Do not** ignore parking placement or density gradient - these are non-negotiable
- **Do not** treat TOD as an aesthetic style; it is a performance standard
- **Always** connect site-level evaluation to regional outcomes
- **Always** apply the human-scale test: can the grandmother, the child, the commuter use this place without a car?

---

## When to Use

- Station area planning for new transit investments
- Evaluation of proposed TOD projects
- Compliance review of existing "transit-oriented" developments
- Pre-development assessment of transit station areas
- Comparison of TOD proposals against best practices
- Guidance for zoning or design guidelines near transit

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| station_location | Yes | Type and location of transit station (rail, BRT, ferry, etc.) |
| development_proposal | Yes | Proposed or existing development program (uses, densities, parking) |
| site_conditions | Recommended | Existing conditions: land uses, street network, barriers |
| regional_context | Recommended | Metropolitan area, transit system, growth pressures |

---

## The Six TOD Criteria (Calthorpe Framework)

### 1. Transit Station as Center

The station should be the heart of the neighborhood, not an edge condition or afterthought.

**Assessment Questions:**
- Is the station visually and functionally the focal point?
- Do major pedestrian paths lead to/from the station?
- Is there a plaza, gathering space, or civic presence at the station?
- Does the development embrace the station or turn its back?

**Scoring:**
- **Pass:** Station is the clear organizing center with active frontages and public space
- **Partial:** Station is accessible but not celebrated; secondary to other elements
- **Fail:** Station is at edge, behind parking, or disconnected from development

### 2. Density Gradient

Highest density at the station, tapering outward to the quarter-mile edge.

**Assessment Questions:**
- What is the density at the station (dwelling units per acre, FAR)?
- Does density decrease as distance from station increases?
- Is the highest-intensity use closest to the platform?
- Are there appropriate transitions to surrounding neighborhoods?

**Scoring:**
- **Pass:** Clear gradient with 4+ stories at station tapering to 2-3 at edge
- **Partial:** Some density near station but gradient is inconsistent
- **Fail:** Uniform low density OR highest density away from station

### 3. Mixed Use

Residential, retail, office, and civic uses integrated vertically and horizontally.

**Assessment Questions:**
- Are there multiple use types within the quarter-mile radius?
- Is there vertical mixing (ground-floor retail with housing above)?
- Can residents meet daily needs without leaving the area?
- Are uses integrated or segregated into pods?

**Scoring:**
- **Pass:** True mixed-use with daily needs accessible on foot; vertical integration
- **Partial:** Multiple uses present but segregated or incomplete
- **Fail:** Single-use development or uses separated by parking/arterials

### 4. Pedestrian Priority

Streets designed for walking first, with narrow lanes, wide sidewalks, and street trees.

**Assessment Questions:**
- Are sidewalks continuous, wide (10+ feet), and shaded?
- Are street crossings frequent, safe, and marked?
- Are vehicle speeds controlled through design (narrow lanes, tight curves)?
- Is the pedestrian experience interesting (active frontages, windows, doors)?

**Scoring:**
- **Pass:** Streets designed for pedestrians; cars are guests; walking is pleasant
- **Partial:** Sidewalks exist but streets prioritize vehicles; walking is tolerable
- **Fail:** Auto-dominated design; pedestrians are afterthought

### 5. Parking Placement

Parking behind or below buildings, at the perimeter, never between building and street.

**Assessment Questions:**
- Where is parking located relative to buildings and streets?
- Are parking structures wrapped with active uses?
- Is surface parking minimized and screened?
- Does anyone walk past a parking lot to reach their destination?

**Scoring:**
- **Pass:** Parking invisible from street; behind buildings, below grade, or wrapped
- **Partial:** Some parking visible but minimized and screened
- **Fail:** Parking lots between buildings and street; park-and-ride dominance

### 6. Housing Diversity

Mix of housing types and price points serving varied demographics.

**Assessment Questions:**
- Are there multiple housing types (apartments, townhomes, condos)?
- Is there a range of unit sizes (studios to family-sized)?
- Are affordability requirements included?
- Can people at different life stages and incomes live here?

**Scoring:**
- **Pass:** Diverse housing types and price points; inclusionary requirements met
- **Partial:** Some variety but limited income diversity
- **Fail:** Mono-culture (all luxury condos, all affordable, all one bedroom)

---

## Analysis Process

### Step 1: Map the Geography

Draw two circles centered on the transit station platform:
- **Primary zone:** Quarter-mile radius (5-minute walk, ~1,320 feet)
- **Secondary zone:** Half-mile radius (10-minute walk, ~2,640 feet)

Everything within the primary zone is critical. The secondary zone matters for transit ridership but can have lower intensity.

### Step 2: Inventory Existing Conditions

Within the quarter-mile radius, document:
- Current land uses and densities
- Street network and block sizes
- Barriers (arterials, parking lots, railroads, water)
- Pedestrian infrastructure condition
- Parking supply and location

### Step 3: Evaluate Against Six Criteria

For each of the six criteria, assess the current/proposed conditions and assign:
- **Pass** (2 points)
- **Partial** (1 point)
- **Fail** (0 points)

Calculate total score (0-12 points).

### Step 4: Project Performance Outcomes

Based on TOD compliance level, estimate:
- **VMT reduction** vs. conventional suburban: 40-60% for full TOD
- **Transit ridership multiplier:** 2-5x vs. non-TOD
- **Tax revenue per acre:** Premium for well-designed TOD
- **Infrastructure cost savings:** Per capita reductions

### Step 5: Generate Recommendations

For each criterion scoring Partial or Fail, provide specific recommendations:
- What physical change is needed?
- What policy/zoning change is required?
- What is the implementation sequence?

---

## Output Format

```markdown
## Transit-Oriented Development Audit: [Station Name]

### Summary

**Station Type:** [Rail/BRT/Ferry]
**TOD Score:** [X/12] - [Rating: Exemplary/Compliant/Deficient/Not TOD]
**Primary Finding:** [One-sentence assessment]

### Station Area Geography

**Primary Zone (Quarter-Mile):**
- Area: [X] acres
- Current population: [X] / Projected: [X]
- Key destinations within walk circle: [List]

**Secondary Zone (Half-Mile):**
- Area: [X] acres
- Major barriers: [List]

### Six Criteria Assessment

| Criterion | Score | Key Finding |
|-----------|-------|-------------|
| 1. Station as Center | Pass/Partial/Fail | [Brief finding] |
| 2. Density Gradient | Pass/Partial/Fail | [Brief finding] |
| 3. Mixed Use | Pass/Partial/Fail | [Brief finding] |
| 4. Pedestrian Priority | Pass/Partial/Fail | [Brief finding] |
| 5. Parking Placement | Pass/Partial/Fail | [Brief finding] |
| 6. Housing Diversity | Pass/Partial/Fail | [Brief finding] |

**Total Score:** [X/12]

### Detailed Findings

[For each criterion, provide 2-3 sentence analysis with specific observations]

### Projected Performance

| Metric | Conventional | With TOD | Improvement |
|--------|--------------|----------|-------------|
| VMT per household/year | [X] | [X] | [X%] reduction |
| Transit mode share | [X%] | [X%] | [X]x multiplier |
| Tax revenue per acre | $[X] | $[X] | [X%] increase |

### Priority Recommendations

**Immediate (before development approval):**
1. [Recommendation]
2. [Recommendation]

**Near-term (design development):**
1. [Recommendation]

**Long-term (future phases):**
1. [Recommendation]

### Regional Context Note

[One paragraph connecting this station area to regional growth strategy and climate outcomes]

### Calthorpe's Standard

> "A transit station without transit-oriented development is a parking lot with tracks."

[Assessment of whether this development meets the spirit, not just letter, of TOD]
```

---

## Scoring Interpretation

| Score | Rating | Interpretation |
|-------|--------|----------------|
| 10-12 | Exemplary | Best-practice TOD; model for others |
| 7-9 | Compliant | Meets TOD standards with minor gaps |
| 4-6 | Deficient | Claims TOD status but significant failures |
| 0-3 | Not TOD | Transit-adjacent at best; fundamentally car-oriented |

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Station type unclear | Assume rail station standards; note assumption |
| No development proposal | Audit existing conditions; provide development recommendations |
| Regional context missing | Note gap; provide generic regional framing |
| Political constraints mentioned | Acknowledge but do not lower standards; note trade-offs |

---

## Example Application

**Input:** "We have a new light rail station opening in two years. Currently the area is a strip mall and park-and-ride lot. Developer proposes 400 apartments and 20,000 SF retail."

**Assessment Highlights:**
- Station as Center: Partial - station exists but proposal doesn't organize around it
- Density Gradient: Fail - uniform density proposed; no gradient
- Mixed Use: Partial - residential + retail but limited daily needs coverage
- Pedestrian Priority: Fail - existing strip mall design; wide arterials
- Parking Placement: Fail - park-and-ride dominates; parking between building and station
- Housing Diversity: Partial - one building type proposed

**Score:** 3/12 (Not TOD)

**Primary Recommendation:** Reject current proposal. Require master plan organizing density around station, eliminating surface parking between station and buildings, and creating pedestrian-first street design.

---

## Integration

This skill is part of the **Peter Calthorpe** expert persona. Use it when evaluating any development near transit. It pairs well with:
- **walkability-diagnostic** for detailed pedestrian analysis
- **regional-growth-scenario-analysis** for metropolitan context
- **climate-urban-form-integration** for carbon impact quantification
