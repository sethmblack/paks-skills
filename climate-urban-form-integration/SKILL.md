---
name: climate-urban-form-integration
description: Quantify the climate implications of urban form decisions using Peter Calthorpe's framework. Connect land use patterns to transportation emissions, calculate VMT by neighborhood type, project carbon outcomes, and demonstrate how urban design is climate policy.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.2310
repository: https://github.com/sethmblack/paks-skills
keywords:
- climate-urban-form-integration
- urban-planning
---

# Climate-Urban Form Integration

Quantify the climate implications of urban form decisions using Peter Calthorpe's framework. Connect land use patterns to transportation emissions, calculate VMT by neighborhood type, project carbon outcomes, and demonstrate how urban design is climate policy.

---

## Constitutional Constraints

- **Do not** treat climate as separate from urbanism; urban form IS climate policy
- **Do not** accept technology-only climate solutions; land use determines 30%+ of emissions
- **Do not** ignore the cumulative impact of individual development decisions
- **Always** quantify: "The greenest mile is the one not driven"
- **Remember:** "Urbanism is, in fact, our single most potent weapon against climate change, rising energy costs, and environmental degradation."

---

## When to Use

- Climate action plan development
- Development project sustainability review
- Regional planning carbon analysis
- Transportation emissions reduction strategies
- Zoning policy carbon implications
- Net-zero community planning
- Green building vs. green urbanism debates
- Land use-transportation integration planning

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| development_pattern | Yes | Type of development or scenario to analyze |
| scale | Yes | Single project, neighborhood, or regional |
| units_or_population | Yes | Number of households, residents, or employees |
| location_context | Recommended | Urban, suburban, exurban; transit access |
| comparison_baseline | Optional | What to compare against (conventional, trend, alternative) |

---

## Calthorpe's Climate-Urban Form Framework

### The 88% Challenge

By 2050, each person in the US needs to emit on average just 12% of their current greenhouse gases - an 88% per capita reduction. This is not achievable through technology alone.

### The Two-Thirds Principle

The built environment accounts for over two-thirds of America's energy use and greenhouse gas emissions:
- **Transportation:** ~30% of US emissions (mostly car trips)
- **Buildings:** ~40% of US emissions (heating, cooling, lighting)

Urban form determines both:
- **Transportation:** Where we live and work determines how much we drive
- **Buildings:** Density affects building efficiency and energy demand

### The Urban Form Hierarchy

Carbon impact by development type (per household, per year):

| Development Type | VMT/Year | Transport Carbon | Building Carbon | Total Carbon |
|------------------|----------|------------------|-----------------|--------------|
| Urban infill (5+ stories) | ~7,000 | ~3 tons | ~4 tons | ~7 tons |
| Streetcar suburb (3-4 stories) | ~12,000 | ~5 tons | ~5 tons | ~10 tons |
| Suburban (1-2 stories) | ~20,000 | ~9 tons | ~6 tons | ~15 tons |
| Exurban sprawl | ~30,000 | ~13 tons | ~7 tons | ~20 tons |

**Key insight:** A household in urban infill produces roughly 1/3 the carbon of a household in exurban sprawl.

---

## Analysis Process

### Step 1: Classify Development Pattern

Categorize the development or scenario:

| Category | Characteristics | Transit Access | Density |
|----------|-----------------|----------------|---------|
| **Urban Core** | High-rise, full mixed-use, minimal parking | High-frequency rail | 50+ DU/acre |
| **Urban Infill** | Mid-rise, mixed-use, limited parking | Rail or frequent bus | 25-50 DU/acre |
| **Streetcar Suburb** | Low-rise, mixed-use, moderate parking | Good transit access | 12-25 DU/acre |
| **Suburban Transit** | Low-rise, auto-oriented with transit option | Some transit access | 8-15 DU/acre |
| **Suburban Auto** | Single-family dominant, auto-required | Minimal transit | 4-8 DU/acre |
| **Exurban** | Rural-residential, car-dependent | No transit | <4 DU/acre |

### Step 2: Calculate Transportation Carbon

**VMT Calculation:**

1. Determine VMT per household by development type (see table above)
2. Multiply by number of households
3. Convert to annual VMT

**Carbon Calculation:**

1. VMT x emissions factor (current: ~0.9 lbs CO2/mile for average vehicle)
2. Adjust for projected fleet electrification (reduces over time)
3. Include embodied carbon in vehicle manufacturing

**Example:**
- 1,000 households in suburban auto: 20,000 VMT each = 20M VMT/year
- 20M x 0.9 lbs/mile = 18M lbs = 9,000 tons CO2/year (transportation only)

### Step 3: Calculate Building Carbon

**Operating Carbon:**
- Energy use per square foot by building type
- Carbon intensity of electricity grid (varies by region)
- Heating fuel carbon content

**Key Relationships:**
- Multi-family uses 30-50% less energy per SF than single-family
- Attached units share walls, reducing heating/cooling load
- Smaller units use less energy (urban = smaller average unit size)

**Embodied Carbon:**
- Materials and construction carbon
- Generally amortized over building life (50+ years)

### Step 4: Calculate Total Carbon

Sum transportation and building carbon:
- Per household/year
- Per capita/year
- Total for development/scenario

Compare to:
- National average (~20 tons/capita)
- Climate target (~2-3 tons/capita for 88% reduction)
- Comparison scenario

### Step 5: Project Trajectory

Analyze whether development locks in or enables carbon reduction:

**Lock-in factors:**
- Long building lifespan (50-100 years)
- Infrastructure investment (roads vs. transit)
- Land use patterns difficult to change
- Household location determines transportation patterns for decades

**Trajectory Assessment:**
- Does this development pattern allow for future carbon reduction?
- Does it require technology improvements to meet targets?
- Or does it lock in high-carbon patterns regardless of technology?

### Step 6: Identify Urban Form Interventions

What urban form changes would reduce carbon?

**Site Level:**
- Increase density
- Add transit access
- Mix uses to reduce trip distances
- Improve walkability

**Neighborhood Level:**
- Complete the neighborhood (add missing daily needs)
- Connect street network (reduce circuity)
- Add transit service

**Regional Level:**
- Redirect growth to transit-served locations
- Preserve natural lands (carbon sinks)
- Reduce VMT through land use coordination

---

## Output Format

```markdown
## Climate-Urban Form Integration: [Development/Scenario Name]

### Summary

**Scale:** [Project/Neighborhood/Regional]
**Development Type:** [Category from classification]
**Households/Population:** [X] households, [X] residents

**Carbon Intensity:** [X] tons CO2 per household per year
**Climate Assessment:** [On Track / Needs Improvement / Incompatible with Climate Goals]

### Carbon Calculation

#### Transportation Carbon

| Metric | Value | Notes |
|--------|-------|-------|
| VMT per household/year | [X] | Based on [development type] |
| Total VMT | [X] million | [X] households |
| Transportation CO2 | [X] tons/year | At [X] lbs CO2/mile |
| Per capita | [X] tons | |

#### Building Carbon

| Metric | Value | Notes |
|--------|-------|-------|
| Building energy (kWh/SF) | [X] | [Building type] average |
| Total energy use | [X] kWh | |
| Building CO2 | [X] tons/year | At [X] lbs CO2/kWh |
| Per capita | [X] tons | |

#### Total Carbon

| Source | Tons CO2/Year | % of Total |
|--------|---------------|------------|
| Transportation | [X] | [X%] |
| Buildings | [X] | [X%] |
| **Total** | [X] | 100% |

**Per Household:** [X] tons/year
**Per Capita:** [X] tons/year

### Comparison to Alternatives

| Scenario | Transport Carbon | Building Carbon | Total | Difference |
|----------|------------------|-----------------|-------|------------|
| **This development** | [X] | [X] | [X] | Baseline |
| Urban alternative | [X] | [X] | [X] | [X%] lower |
| Suburban alternative | [X] | [X] | [X] | [X%] higher |

**Key Finding:** [One-sentence comparison]

### Climate Trajectory Analysis

**88% Reduction Target:** [X] tons per capita by 2050

| Path | Achievable? | Requirements |
|------|-------------|--------------|
| This development | [Yes/Challenging/No] | [What would be needed] |
| With full EV adoption | [Yes/Challenging/No] | [Technology assumptions] |
| With urban form change | [Yes/Challenging/No] | [Urban form changes needed] |

**Lock-in Assessment:** [Does this development lock in high-carbon patterns?]

### The Technology vs. Urbanism Question

Calthorpe: "The greatest and most innovative source of renewable energy rests within urban design, not solar panels or wind turbines."

| Approach | Carbon Reduction | Certainty | Cost |
|----------|------------------|-----------|------|
| Better urban form | [X%] reduction | High | [Low/Medium/High] |
| Full electrification | [X%] reduction | Dependent on grid | [High] |
| Behavior change | [X%] reduction | Uncertain | [Low] |

**Bottom Line:** [Assessment of technology vs. urbanism balance]

### Urban Form Recommendations

**To improve climate performance:**

1. **[Intervention]:** [Impact]
2. **[Intervention]:** [Impact]
3. **[Intervention]:** [Impact]

**Avoided carbon from recommendations:** [X] tons/year

### Regional Climate Context

[One paragraph connecting this development to regional carbon trajectory]

> "We obsess over vehicle efficiency while ignoring that a compact, mixed-use neighborhood eliminates vehicle trips entirely. The greenest mile is the one not driven."

### Final Assessment

| Criterion | Rating | Notes |
|-----------|--------|-------|
| Current carbon intensity | [High/Medium/Low] | |
| Path to 88% reduction | [Clear/Possible/Blocked] | |
| Lock-in risk | [High/Medium/Low] | |
| Urban form quality | [Good/Fair/Poor] | |

**Overall Climate Grade:** [A/B/C/D/F]

**Recommendation:** [Approve / Modify / Reject from climate perspective]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Development type unclear | Request clarification or assess most likely type |
| Regional grid carbon unknown | Use national average or regional EPA data |
| Future technology assumptions vary | Show range of scenarios |
| Scale too small for meaningful analysis | Note limitations; provide directional guidance |

---

## Example Application

**Input:** "Compare climate impact of building 500 homes in a TOD vs. a greenfield subdivision."

**Summary Finding:**

| Scenario | Transport Carbon | Building Carbon | Total | Per Household |
|----------|------------------|-----------------|-------|---------------|
| TOD (500 homes) | 2,500 tons/yr | 2,000 tons/yr | 4,500 tons/yr | 9 tons |
| Subdivision (500 homes) | 6,500 tons/yr | 3,000 tons/yr | 9,500 tons/yr | 19 tons |

**Difference:** TOD produces 53% less carbon than subdivision - for the same population.

**Over 50 years:** 250,000 tons of avoided carbon by choosing TOD.

**Climate Assessment:** Only TOD scenario is compatible with regional climate targets. Subdivision locks in high-carbon patterns for generations.

---

## Integration

This skill is part of the **Peter Calthorpe** expert persona. Use it to quantify climate implications of urban form decisions. It pairs well with:
- **transit-oriented-development-audit** (carbon-efficient development type)
- **walkability-diagnostic** (walkable = lower VMT = lower carbon)
- **regional-growth-scenario-analysis** (aggregate climate impacts of growth patterns)