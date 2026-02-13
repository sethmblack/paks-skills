---
name: walkability-diagnostic
description: Assess a neighborhood or development's walkability using Peter Calthorpe's five-minute (quarter-mile) standard. Map walk circles from key origins, inventory destinations within reach, catalog barriers, assess street design, and generate specific improvement recommendations.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.2347
repository: https://github.com/sethmblack/paks-skills
keywords:
- walkability-diagnostic
- urban-planning
---

# Walkability Diagnostic

Assess a neighborhood or development's walkability using Peter Calthorpe's five-minute (quarter-mile) standard. Map walk circles from key origins, inventory destinations within reach, catalog barriers, assess street design, and generate specific improvement recommendations.

---

## Constitutional Constraints

- **Do not** accept "walkable" as marketing language without verification
- **Do not** evaluate walkability in isolation from destinations - walkability requires somewhere to walk TO
- **Do not** confuse sidewalk presence with true walkability
- **Always** apply the human test: the grandmother, the child, the parent with a stroller
- **Always** connect walkability findings to broader urban form outcomes

---

## When to Use

- First-order test of any neighborhood or development
- Development review for pedestrian access
- Neighborhood retrofit planning
- TOD station area assessment (feeds into TOD audit)
- Complete streets planning
- Health and equity impact assessments
- Site selection analysis

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| site_location | Yes | Address or area to assess |
| key_origins | Yes | Starting points for walk analysis (transit stops, residential clusters, employment centers) |
| existing_conditions | Recommended | Street network, sidewalks, crossings, land uses |
| user_groups | Optional | Specific populations to consider (seniors, children, mobility-impaired) |

---

## Calthorpe's Walkability Standard

> "My short and simple answer is that a well-designed city is walkable. It's a place where your destinations are close enough to walk to and where you feel safe enough to walk. And it's a place that is interesting enough socially to make you feel that walking is perhaps something more than just getting from point A to point B."

**The Three Requirements:**
1. **Proximity** - Destinations within five-minute walk (quarter-mile)
2. **Safety** - Physical security and traffic safety
3. **Interest** - Engaging environment worth walking through

---

## Analysis Process

### Step 1: Draw Walk Circles

From each key origin, draw:
- **5-minute walk circle** (quarter-mile radius, ~1,320 feet)
- **10-minute walk circle** (half-mile radius, ~2,640 feet)

Note: These are "as the crow flies" circles. Actual walk distances may be longer due to barriers and circuitous routes.

### Step 2: Calculate Walk Shed

Adjust circles for real walking conditions:
- **Street connectivity:** More connected grid = closer to circle; cul-de-sacs = much smaller shed
- **Barriers:** Subtract areas cut off by highways, railroads, water, large parking lots
- **Topography:** Steep slopes effectively increase walking distance

Estimate the actual "walk shed" - the area truly accessible on foot in 5 minutes.

### Step 3: Inventory Destinations

Within the 5-minute walk shed, count and categorize:

| Category | Essential Destinations |
|----------|----------------------|
| **Daily Needs** | Grocery, pharmacy, bank, post office, coffee shop |
| **Education** | Schools, daycare, library |
| **Health** | Medical clinic, fitness, park |
| **Transit** | Bus stop, rail station, bike share |
| **Services** | Restaurants, dry cleaner, hardware |
| **Employment** | Office, retail jobs, commercial |

**Completeness Score:**
- **Complete:** 5+ categories represented
- **Partial:** 3-4 categories
- **Incomplete:** 1-2 categories
- **None:** No destinations within walk shed

### Step 4: Identify Barriers

Catalog obstacles that prevent or discourage walking:

**Physical Barriers:**
- Major arterials (4+ lanes)
- Highways and interchanges
- Railroads without crossings
- Water bodies without bridges
- Large parking lots
- Dead-end streets and cul-de-sacs
- Gated communities

**Safety Barriers:**
- High-speed traffic
- Missing sidewalks
- Unsafe crossings
- Poor lighting
- Crime/perceived danger

**Comfort Barriers:**
- No shade/tree canopy
- No weather protection
- Unpleasant environment (noise, pollution)
- Long blank walls
- Surface parking lots to walk past

### Step 5: Assess Street Design

Evaluate pedestrian infrastructure:

| Element | Good Practice | Poor Practice |
|---------|---------------|---------------|
| **Sidewalk width** | 10+ feet; room for two-way passing | <5 feet; single file only |
| **Buffer from traffic** | Tree lawn, parked cars, planting | Directly adjacent to travel lanes |
| **Crossing frequency** | Every 300-400 feet; mid-block options | Only at major intersections |
| **Crossing safety** | Marked, signalized, median refuge | Unmarked, no signal, wide crossings |
| **Street width** | Narrow lanes (10-11 feet) | Wide lanes (12+ feet) |
| **Vehicle speeds** | Design for 20-25 mph | Designed for 35+ mph |
| **Building frontage** | Windows, doors, active uses | Blank walls, parking, loading docks |
| **Tree canopy** | Continuous shade | No trees, full sun exposure |

### Step 6: Apply the Human Test

Can these people comfortably walk this environment?
- **The 8-year-old:** Can a child walk to school or a friend's house safely?
- **The 80-year-old:** Can a senior walk to daily needs with limited mobility?
- **The parent with stroller:** Can a caregiver navigate with a child?
- **The person in wheelchair:** Is the environment ADA-accessible beyond minimum compliance?

If any of these groups cannot safely and comfortably walk, the environment fails the walkability test.

---

## Output Format

```markdown
## Walkability Diagnostic: [Location Name]

### Summary

**Overall Walkability Rating:** [Excellent/Good/Fair/Poor/Unwalkable]
**Destination Completeness:** [Complete/Partial/Incomplete/None]
**Primary Finding:** [One-sentence assessment]

### Walk Circles from Key Origins

| Origin | 5-Min Walk Shed | 10-Min Walk Shed | Key Barriers |
|--------|-----------------|------------------|--------------|
| [Origin 1] | [X] acres | [X] acres | [List barriers] |
| [Origin 2] | [X] acres | [X] acres | [List barriers] |

**Walk Shed Reduction:** [X%] of theoretical circle is actually walkable due to barriers

### Destination Inventory (5-Minute Walk)

| Category | Available | Missing | Notes |
|----------|-----------|---------|-------|
| Daily Needs | [List] | [List] | |
| Education | [List] | [List] | |
| Health | [List] | [List] | |
| Transit | [List] | [List] | |
| Services | [List] | [List] | |
| Employment | [List] | [List] | |

**Completeness Score:** [X/6] categories

### Barrier Catalog

**Physical Barriers:**
1. [Barrier]: [Impact]
2. [Barrier]: [Impact]

**Safety Barriers:**
1. [Barrier]: [Impact]

**Comfort Barriers:**
1. [Barrier]: [Impact]

### Street Design Assessment

| Element | Current Condition | Rating | Notes |
|---------|-------------------|--------|-------|
| Sidewalk width | [X] feet | Good/Fair/Poor | |
| Buffer from traffic | [Description] | Good/Fair/Poor | |
| Crossing frequency | Every [X] feet | Good/Fair/Poor | |
| Vehicle speeds | [X] mph design | Good/Fair/Poor | |
| Building frontage | [Description] | Good/Fair/Poor | |
| Tree canopy | [X]% coverage | Good/Fair/Poor | |

### Human Test Results

| User Group | Can Walk Safely? | Key Issues |
|------------|------------------|------------|
| 8-year-old child | Yes/No | [Issues] |
| 80-year-old senior | Yes/No | [Issues] |
| Parent with stroller | Yes/No | [Issues] |
| Person in wheelchair | Yes/No | [Issues] |

### Priority Recommendations

**Quick Wins (Low cost, high impact):**
1. [Recommendation]
2. [Recommendation]

**Medium-Term Improvements:**
1. [Recommendation]
2. [Recommendation]

**Long-Term/Structural Changes:**
1. [Recommendation]

### Connection to Urban Form

[One paragraph connecting walkability findings to larger questions: Is this a complete neighborhood? What land use changes would improve walkability? How does this relate to regional transportation patterns?]

### Calthorpe's Standard

> "If you cannot walk it, it is not urbanism."

[Final assessment: Does this place qualify as urbanism, or is it car-dependent development that happens to have sidewalks?]
```

---

## Walkability Rating Scale

| Rating | Description | Typical Characteristics |
|--------|-------------|------------------------|
| **Excellent** | Urban walking environment | Complete destinations, frequent crossings, active frontages, passes all human tests |
| **Good** | Walkable with minor gaps | Most destinations present, some barriers, generally safe and pleasant |
| **Fair** | Walkable with effort | Limited destinations, notable barriers, safety concerns for some users |
| **Poor** | Marginally walkable | Few destinations, major barriers, unpleasant or unsafe for most |
| **Unwalkable** | Car-required environment | No meaningful destinations on foot, dangerous conditions, fails human tests |

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No key origins specified | Use logical origins: transit stops, residential centroid, school locations |
| Detailed street data unavailable | Use satellite imagery and street view for assessment |
| Mixed conditions within area | Report zone-by-zone findings; avoid averaging |
| New development (not built) | Assess plans against criteria; note assumptions |

---

## Example Application

**Input:** "Assess walkability for a suburban shopping center that wants to become more walkable."

**Key Findings:**
- 5-minute walk shed covers only 40% of theoretical circle due to arterial barriers
- Destinations limited to retail; no housing, schools, or daily services within walk
- Sidewalks exist but are 4 feet wide, no buffer, no shade
- Crossings only at major intersections (800+ feet apart)
- 8-year-old and 80-year-old tests: Fail (unsafe crossings, no shade, long distances)

**Rating:** Poor (barely walkable for able-bodied adults; car-required for most trips)

**Primary Recommendation:** Land use change required before pedestrian infrastructure improvements. Adding sidewalks to car-oriented development does not create walkability.

---

## Integration

This skill is part of the **Peter Calthorpe** expert persona. Use it as a first-order test before detailed planning analysis. It pairs well with:
- **transit-oriented-development-audit** (walkability feeds into TOD assessment)
- **regional-growth-scenario-analysis** (walkability aggregates to regional VMT)
- **climate-urban-form-integration** (walkable = lower carbon)