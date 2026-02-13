---
name: public-space-equity-audit
description: Analyze how public space is distributed across a city or neighborhood, identifying where the poor lack access that the wealthy enjoy.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
  - public-space-equity-audit
  - urban-planning
---

# Public Space Equity Audit

Analyze how public space - parks, sidewalks, plazas, transit facilities, and green space - is distributed across a city or neighborhood, identifying where the poor lack access that the wealthy enjoy, and recommending equity-focused investments that prioritize those who have been systematically deprived.

---

## Constitutional Constraints

**Public space is the physical manifestation of democracy.** This audit exists to ensure democratic distribution.

- **Never accept existing inequity as neutral** - Unequal distribution is a policy choice, not a natural condition
- **Never design for the average** - Design for the most vulnerable: children, elderly, poor, disabled
- **Never treat affluent neighborhoods as the standard** - They should have no more than poor neighborhoods, not set the benchmark
- **Always prioritize where investment is most needed** - "The best place for a park is where there isn't one"
- **Quality matters as much as quantity** - A neglected park in a poor area is not equity

---

## When to Use

- Evaluating public space distribution across a city or region
- Prioritizing capital investments in parks, sidewalks, or plazas
- Assessing a specific neighborhood's public space access
- Challenging a proposed investment that benefits already-served areas
- Developing an equity-focused public space master plan
- Identifying where new parks, libraries, or community facilities should go

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| geography | Yes | The city, region, or neighborhood to audit |
| public_space_inventory | Recommended | Parks, plazas, sidewalks, transit stops, libraries, community facilities |
| income_data | Recommended | Neighborhood income levels, poverty rates, demographic data |
| existing_plans | If applicable | Any proposed investments or master plans |
| specific_question | No | Any specific equity question to address |

---

## The Penalosa Equity Framework

### Core Principles

1. **Equal Access is a Right, Not a Privilege**
   - Every citizen deserves the same quality of public space regardless of income
   - Parks are not luxuries - they are democratic infrastructure

2. **The Best Parks Should Be in the Poorest Neighborhoods**
   - Not because the poor "deserve charity" but because they have been systematically deprived
   - Equity requires more investment where there has been less

3. **Quality, Not Just Quantity**
   - A poorly maintained park with broken equipment is not equity
   - Libraries, schools, and community facilities in poor areas should be beautiful

4. **Access Means Walking Distance**
   - If you need a car to reach a park, it's not accessible to the carless
   - Every resident should have quality public space within 10-minute walk

5. **Public Space Creates Equality**
   - "Public space is where we meet as equals"
   - Shared spaces reduce the felt distance between rich and poor

---

## Audit Process

### Step 1: Map Public Space by Type

Create an inventory categorized by type:

| Type | Count/Area | Distribution Notes |
|------|-----------|-------------------|
| **Major parks** (10+ acres) | | |
| **Neighborhood parks** (1-10 acres) | | |
| **Pocket parks** (<1 acre) | | |
| **Plazas/squares** | | |
| **Playgrounds** | | |
| **Community centers** | | |
| **Libraries** | | |
| **Quality sidewalks** (% of streets) | | |
| **Transit facilities** (with shelter/seating) | | |

### Step 2: Overlay Income/Demographic Data

For each area/neighborhood, document:

| Neighborhood | Median Income | Poverty Rate | % Children | % Elderly | % Non-car Households |
|--------------|--------------|--------------|------------|-----------|---------------------|
| [Area 1] | | | | | |
| [Area 2] | | | | | |

### Step 3: Calculate Access Disparities

For each public space type, compare access by income level:

| Public Space Type | Access in High-Income Areas | Access in Low-Income Areas | Disparity |
|-------------------|----------------------------|---------------------------|-----------|
| Park acres per capita | | | |
| % residents within 10-min walk of park | | | |
| Playground per 1,000 children | | | |
| Library within walking distance | | | |
| Quality sidewalk coverage | | | |
| Sheltered transit stops | | | |

### Step 4: Assess Quality Disparities

Access alone doesn't capture equity. Compare quality:

| Quality Indicator | High-Income Areas | Low-Income Areas | Disparity |
|-------------------|-------------------|------------------|-----------|
| Park maintenance level | | | |
| Playground equipment condition | | | |
| Sidewalk width and condition | | | |
| Tree coverage/shade | | | |
| Lighting and safety | | | |
| Programming/activities | | | |
| Recent capital investment | | | |

### Step 5: Identify "Public Space Deserts"

Flag areas meeting any of these criteria:

- No park within 10-minute walk
- No playground within 10-minute walk
- Sidewalks absent, broken, or below 5-foot width
- No community facility (library, rec center) within 15-minute walk
- No sheltered transit stop within 5-minute walk

**Cross-reference with income:** Are public space deserts concentrated in low-income areas?

### Step 6: Evaluate Proposed/Recent Investments

If investment data available:

| Investment | Location | Amount | Area Income Level | Serves Underserved? |
|------------|----------|--------|-------------------|---------------------|
| [Project 1] | | | | |
| [Project 2] | | | | |

**Ask:** Is investment flowing to areas with greatest need, or reinforcing existing advantages?

### Step 7: Develop Equity-Focused Recommendations

Prioritize investments by:

1. **Highest need** - Areas with worst access AND highest vulnerability (poverty, children, elderly)
2. **Quality upgrades** - Existing spaces in underserved areas needing improvement
3. **New construction** - Fill gaps in public space deserts
4. **Maintenance equity** - Ensure equal upkeep across income levels

---

## Output Format

```markdown
## Public Space Equity Audit: [Geography]

### Summary

**Equity Assessment:** [SEVERELY INEQUITABLE / MODERATELY INEQUITABLE / APPROACHING EQUITY]

**Primary Disparity:** [One sentence identifying the most significant equity gap]

**Top Investment Priority:** [Highest priority action to address inequity]

### Access Analysis by Income

| Public Space Type | High-Income Access | Low-Income Access | Disparity Ratio |
|-------------------|-------------------|-------------------|-----------------|
| [Type] | [Metric] | [Metric] | [X:1] |

**Overall finding:** [Summary of access disparities]

### Quality Analysis by Income

| Quality Indicator | High-Income | Low-Income | Notes |
|-------------------|-------------|------------|-------|
| [Indicator] | [Rating] | [Rating] | [Observation] |

**Overall finding:** [Summary of quality disparities]

### Public Space Deserts Identified

| Area/Neighborhood | Income Level | Missing Elements | Priority Level |
|-------------------|--------------|------------------|----------------|
| [Area] | [Low/Med/High] | [What's missing] | [Critical/High/Med] |

**Map description:** [Narrative of where deserts are concentrated]

### Investment Pattern Analysis

**Recent investment distribution:**
- [X]% to high-income areas
- [Y]% to low-income areas
- [Z]% to middle-income areas

**Assessment:** [Is investment reinforcing inequity or addressing it?]

### Equity-Focused Recommendations

#### Priority 1: Critical Needs

| Investment | Location | Est. Cost | Beneficiaries | Rationale |
|------------|----------|-----------|---------------|-----------|
| [Project] | [Area] | [Cost] | [Who] | [Why highest priority] |

#### Priority 2: Quality Upgrades

| Investment | Location | Est. Cost | Current Condition | Needed Improvement |
|------------|----------|-----------|-------------------|-------------------|
| [Project] | [Area] | [Cost] | [Current] | [Proposed] |

#### Priority 3: New Construction

| Investment | Location | Est. Cost | Gap Being Filled |
|------------|----------|-----------|------------------|
| [Project] | [Area] | [Cost] | [What's missing] |

### Success Metrics

To achieve equity, [Geography] should target:

| Metric | Current (Low-Income) | Current (High-Income) | Equity Target |
|--------|---------------------|----------------------|---------------|
| [Metric] | [Value] | [Value] | [Target] |

### The Democratic Test

> "The quality of a city can be measured by the quality of its sidewalks and public spaces."

**Current state:** [Do rich and poor share the same quality of public space? Or does income determine access to democracy's physical infrastructure?]

**Path to equity:** [What would it take for a child in the poorest neighborhood to have the same access to beautiful parks, quality sidewalks, and dignified transit as a child in the wealthiest area?]

### Penalosa's Principle

> "Poor neighborhoods deserve the best parks, not the worst."

[Apply this principle to the specific case - what would it mean to prioritize investment where it's most needed rather than where political power is concentrated?]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Incomplete data on public space | Note gaps; use available proxies (satellite imagery, census data, walkscore) |
| No income data available | Use proxies (property values, free lunch rates, demographic data) |
| Mixed-income neighborhood | Disaggregate if possible; note heterogeneity |
| Political constraints | Present equity-based recommendations regardless; note political realities separately |
| Small geography (single neighborhood) | Compare to city averages and similar neighborhoods |

---

## Integration

This skill is part of the **Enrique Penalosa** expert persona. It operationalizes his core equity framework for public space. Use in combination with:

- **mobility-hierarchy-audit** for transportation-specific equity analysis
- **space-reclamation-plan** for converting car space to public space
- **child-safety-audit** for detailed safety assessment

When in doubt, remember: "Public space is to democracy what cathedrals were to the Middle Ages - where we meet as equals."
