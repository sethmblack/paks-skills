---
name: regional-growth-scenario-analysis
description: Compare alternative growth patterns using Peter Calthorpe's three ecologies framework to evaluate environmental, social, and economic outcomes. Project VMT, carbon emissions, infrastructure costs, and land consumption for competing scenarios.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
  - regional-growth-scenario-analysis
  - urban-planning
---

# Regional Growth Scenario Analysis

Compare alternative growth patterns using Peter Calthorpe's three ecologies framework to evaluate environmental, social, and economic outcomes. Project VMT, carbon emissions, infrastructure costs, and land consumption for competing scenarios to inform regional planning decisions.

---

## Constitutional Constraints

- **Do not** present sprawl as neutral or equivalent to compact growth; quantify the differences
- **Do not** ignore regional scale - parcel-by-parcel analysis obscures cumulative impacts
- **Do not** dismiss either scenario without data; let metrics speak
- **Always** evaluate against all three ecologies (environmental, social, economic)
- **Always** connect scenarios to climate outcomes
- **Remember:** "You can't really solve the problem at the scale of the individual, town or county, but the regional scale is actually the important one."

---

## When to Use

- Metropolitan comprehensive planning
- Growth boundary decisions
- Infrastructure investment prioritization
- Climate action plan development
- Housing policy debates (where to build)
- Transportation planning (transit vs. highways)
- Greenfield vs. infill debates
- Regional visioning processes

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| region_definition | Yes | Metropolitan area boundaries |
| growth_projections | Yes | Population and job growth expected (e.g., +500,000 residents by 2040) |
| existing_conditions | Yes | Current development pattern, transit network, density distribution |
| scenarios_to_compare | Recommended | Named alternatives (e.g., "trend," "compact," "sprawl") |
| policy_constraints | Optional | Political or legal constraints affecting scenarios |

---

## The Three Ecologies Framework

### Environmental Ecology

Natural systems, habitat preservation, carbon reduction, air and water quality.

**Key Metrics:**
- Land consumption (acres developed)
- Habitat/farmland preserved
- Vehicle miles traveled (VMT)
- Carbon emissions (transportation + buildings)
- Water runoff and impervious surface
- Air quality impacts

### Social Ecology

Community, equity, accessibility, public life, health outcomes.

**Key Metrics:**
- Housing affordability (housing + transportation costs)
- Access to jobs within X minutes
- Access to transit
- Walkability of neighborhoods
- Social interaction opportunities
- Health outcomes (active transportation, air quality)
- Equity distribution of amenities

### Economic Ecology

Fiscal sustainability, tax revenue, infrastructure costs, productivity.

**Key Metrics:**
- Tax revenue per acre
- Infrastructure cost per capita
- Fiscal balance (revenue vs. service costs)
- Economic productivity (agglomeration benefits)
- Housing production costs
- Transportation system costs

---

## Analysis Process

### Step 1: Define the Region and Time Horizon

Establish:
- Geographic boundary (metropolitan statistical area, regional planning boundary)
- Base year and target year (typically 20-30 years)
- Population and job growth to accommodate
- Major infrastructure already planned/committed

### Step 2: Define Scenarios to Compare

Typical scenario set:

| Scenario | Description | Development Pattern |
|----------|-------------|---------------------|
| **Trend** | Continue current policies | Wherever zoning allows; follows market |
| **Sprawl** | Expand outward | Greenfield, low-density, auto-oriented |
| **Compact** | Concentrate growth | Infill, TOD, mixed-use centers |
| **Hybrid** | Targeted density | Focus on transit corridors; preserve edges |

Each scenario must accommodate the same population and job growth.

### Step 3: Map Growth Distribution

For each scenario, determine:
- Where new housing is located (by subarea or traffic zone)
- Where new jobs are located
- Density of new development (dwelling units per acre, FAR)
- Transit access of new development
- Greenfield vs. infill share

### Step 4: Calculate Environmental Metrics

**Land Consumption:**
- Acres of new development by scenario
- Acres of farmland/habitat preserved
- Infill percentage

**VMT and Transportation:**
- Apply VMT rates by development type:
  - Urban infill: ~7,000 VMT/household/year
  - Streetcar suburb: ~12,000 VMT/household/year
  - Suburban sprawl: ~25,000-30,000 VMT/household/year
- Calculate total regional VMT by scenario
- Project VMT growth rate

**Carbon Emissions:**
- Transportation carbon (VMT x emissions factor)
- Building energy carbon (varies by density and building type)
- Total per capita and regional

### Step 5: Calculate Social Metrics

**Housing + Transportation Costs:**
- Housing costs by location
- Transportation costs by location (auto ownership, fuel, transit)
- Combined H+T burden as % of income

**Access Metrics:**
- % of population within 1/2 mile of transit
- Jobs accessible within 30/45/60 minutes by transit and car
- Daily needs within walking distance

**Health and Equity:**
- Active transportation mode share
- Air quality by subarea
- Distribution of amenities by income level

### Step 6: Calculate Economic Metrics

**Fiscal Analysis:**
- Tax revenue generated by development type
  - Downtown: $1M+/acre/year
  - Mixed-use urban: $500K-1M/acre/year
  - Strip commercial: $100-300K/acre/year
  - Single-family suburban: $20-50K/acre/year
- Infrastructure costs per capita
- Net fiscal impact by scenario

**Infrastructure Needs:**
- Road miles required
- Water/sewer extensions
- School construction
- Transit investment

### Step 7: Synthesize Three Ecologies

| Scenario | Environmental | Social | Economic | Overall |
|----------|---------------|--------|----------|---------|
| Trend | [Score] | [Score] | [Score] | [Score] |
| Sprawl | [Score] | [Score] | [Score] | [Score] |
| Compact | [Score] | [Score] | [Score] | [Score] |

---

## Output Format

```markdown
## Regional Growth Scenario Analysis: [Region Name]

### Summary

**Region:** [Name and geographic scope]
**Time Horizon:** [Base year] to [Target year]
**Growth to Accommodate:** [X] additional residents, [X] additional jobs

**Primary Finding:** [One-sentence comparative assessment]

**Recommended Scenario:** [Name] because [key reason]

### Growth Distribution Comparison

| Metric | Trend | Sprawl | Compact |
|--------|-------|--------|---------|
| Total land consumed (acres) | [X] | [X] | [X] |
| Infill share (%) | [X%] | [X%] | [X%] |
| Greenfield share (%) | [X%] | [X%] | [X%] |
| Average density (DU/acre) | [X] | [X] | [X] |
| % within 1/2 mile of transit | [X%] | [X%] | [X%] |

### Environmental Ecology

| Metric | Trend | Sprawl | Compact |
|--------|-------|--------|---------|
| Land consumption (acres) | [X] | [X] | [X] |
| Farmland/habitat preserved | [X] | [X] | [X] |
| Regional VMT (daily) | [X]M | [X]M | [X]M |
| VMT per capita | [X] | [X] | [X] |
| Transportation carbon (tons/yr) | [X] | [X] | [X] |
| Building energy carbon | [X] | [X] | [X] |
| **Total carbon** | [X] | [X] | [X] |

**Environmental Winner:** [Scenario] with [X%] lower carbon emissions

### Social Ecology

| Metric | Trend | Sprawl | Compact |
|--------|-------|--------|---------|
| H+T costs (% of median income) | [X%] | [X%] | [X%] |
| Jobs within 45 min transit | [X%] | [X%] | [X%] |
| Population near transit | [X%] | [X%] | [X%] |
| Walkable neighborhoods (%) | [X%] | [X%] | [X%] |
| Active transportation share | [X%] | [X%] | [X%] |

**Social Winner:** [Scenario] with [key advantage]

### Economic Ecology

| Metric | Trend | Sprawl | Compact |
|--------|-------|--------|---------|
| Tax revenue per acre (avg) | $[X] | $[X] | $[X] |
| Infrastructure cost per capita | $[X] | $[X] | $[X] |
| Net fiscal impact (annual) | $[X] | $[X] | $[X] |
| Road miles needed | [X] | [X] | [X] |
| Transit investment | $[X] | $[X] | $[X] |

**Economic Winner:** [Scenario] with [key advantage]

### Three Ecologies Summary

| Scenario | Environmental | Social | Economic | Combined |
|----------|---------------|--------|----------|----------|
| Trend | [1-5 rating] | [1-5] | [1-5] | [Total] |
| Sprawl | [1-5 rating] | [1-5] | [1-5] | [Total] |
| Compact | [1-5 rating] | [1-5] | [1-5] | [Total] |

### Climate Implications

**By 2050, each person in the US needs to emit on average just 12% of their current greenhouse gases - an 88% per capita reduction.**

| Scenario | Per Capita Carbon Trajectory | Path to 88% Reduction |
|----------|------------------------------|----------------------|
| Trend | [Trajectory] | [Achievable/Challenging/Impossible] |
| Sprawl | [Trajectory] | [Achievable/Challenging/Impossible] |
| Compact | [Trajectory] | [Achievable/Challenging/Impossible] |

### Implementation Requirements

**To achieve [Recommended Scenario]:**

1. **Land Use/Zoning:** [Required changes]
2. **Transit Investment:** [Required investment]
3. **Incentives/Regulations:** [Policy tools needed]
4. **Regional Coordination:** [Governance needs]

### Political Reality Check

[One paragraph acknowledging political constraints while maintaining that the data supports a clear direction]

### Calthorpe's Frame

> "Sprawl fails on all three ecologies: it destroys natural habitat, isolates people in automobile dependence, and bankrupts municipalities with infrastructure costs that tax revenues cannot sustain. Compact development succeeds on all three."

[Assessment of whether regional choice reflects this understanding]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Precise data unavailable | Use ranges and analogous regions; note assumptions |
| Only two scenarios requested | Include "trend" as implicit third for comparison |
| Political scenario excluded | Note exclusion; analyze what data shows regardless |
| Growth projections uncertain | Run sensitivity analysis with high/low ranges |

---

## Example Application

**Input:** "Our region expects 200,000 new residents by 2040. Compare sprawl outward versus focusing growth in transit corridors."

**Summary Finding:** Compact scenario (transit corridors) consumes 60% less land, generates 45% less VMT, costs $2 billion less in infrastructure, and produces $500 million more in annual tax revenue than sprawl scenario - while housing the same population.

**Climate Implication:** Only compact scenario puts the region on trajectory for state climate targets. Sprawl scenario locks in carbon-intensive development for decades.

---

## Integration

This skill is part of the **Peter Calthorpe** expert persona. Use it for metropolitan-scale planning decisions. It pairs well with:
- **transit-oriented-development-audit** (implement compact scenario through TOD)
- **walkability-diagnostic** (assess neighborhoods within scenarios)
- **climate-urban-form-integration** (detailed carbon analysis for scenarios)
