---
name: edge-quality-analysis
description: Analyze the ground-floor interfaces between buildings and public space, distinguishing soft edges (that invite activity) from hard edges (that repel), and identifying interventions to improve street life.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3876
repository: https://github.com/sethmblack/paks-skills
keywords:
- edge-quality-analysis
- urban-planning
---

# Edge Quality Analysis

Analyze the ground-floor interfaces between buildings and public space, distinguishing soft edges (that invite activity) from hard edges (that repel), and identifying interventions to improve street life. Based on Jan Gehl's edge effect research.

---

## Constitutional Constraints

- **Respect property rights** - Recommendations should acknowledge that ground floor changes often require cooperation from building owners
- **Functional realism** - Some hard edges serve necessary functions (loading, parking, utilities); note when softening is impractical
- **Context sensitivity** - What works as a soft edge varies by neighborhood, culture, and climate
- **Safety awareness** - Transparency can conflict with security needs; acknowledge trade-offs

---

## When to Use

- Diagnosing why a street feels "dead" despite pedestrian traffic
- Planning ground floor requirements for new development
- Identifying retrofit opportunities for existing buildings
- Understanding why certain blocks thrive while others struggle
- Building the case for active frontage policies
- Evaluating the impact of specific ground floor uses

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| street_description | Yes | Description of the street or block to analyze |
| images | Recommended | Street-level photos showing building frontages |
| ground_floor_uses | Helpful | Known uses (retail, office lobby, parking, residential) |
| activity_observations | Helpful | Where people currently gather, linger, or avoid |

---

## The Edge Effect

### Core Principle

People gravitate to edges, not centers. In public spaces:
- They stand with their backs to walls, facing the action
- They sit along building frontages, not in exposed centers
- They linger where there's something to engage with
- They hurry past blank walls

**The edge zone** - the first few meters where buildings meet public space - disproportionately influences street life. This is where people pause, where activities spill out, where the indoor and outdoor worlds connect.

### Soft vs. Hard Edges

**Soft Edges** create conditions for lingering:
- Transparency (windows to see through)
- Variety (different shops, uses, facades)
- Permeability (frequent entrances)
- Activity (things happening inside visible from outside)
- Spill-out space (cafes, displays, seating)
- Human scale (details, textures, elements at eye level)

**Hard Edges** repel activity:
- Blank walls (nothing to see)
- Uniformity (repetitive, monotonous facades)
- Impermeability (few or no entrances)
- Inactivity (dark windows, empty spaces)
- Barriers (fences, grade changes, landscaping walls)
- Hostile architecture (surfaces designed to prevent sitting)

---

## Analysis Process

### Step 1: Map the Frontages

Walk (or examine images of) both sides of the street, documenting ground floor conditions block by block.

**Frontage Types:**
- **Active Retail** - Shops, cafes, restaurants with display windows and frequent entrances
- **Active Service** - Banks, salons, offices with walk-in access and visible activity
- **Residential** - Stoops, front yards, small apartment entrances
- **Lobby/Institutional** - Office building lobbies, hotel entrances, institutional fronts
- **Blank Wall** - No openings, no activity, solid surface
- **Parking/Service** - Garage entrances, loading docks, back-of-house
- **Vacant** - Empty storefronts, boarded windows

### Step 2: Score Edge Quality

For each frontage segment, assess:

**Transparency (Can you see in?)**
- High: Full display windows, clear visibility of activity
- Medium: Partial windows, some obscuring
- Low: Opaque, blocked, or no windows

**Permeability (Can you enter?)**
- High: Entrances every 15-25 feet
- Medium: Entrances every 25-50 feet
- Low: Entrances 50+ feet apart or none

**Activation (Is something happening?)**
- High: Visible activity, merchandise, people
- Medium: Some activity but low energy
- Low: Dark, empty, or unused

**Spill-Out (Does activity extend outside?)**
- High: Outdoor seating, displays, signs of life
- Medium: Some exterior presence
- Low: Hard boundary at building face

**Human Scale (Are there engaging details?)**
- High: Varied facades, awnings, planters, texture
- Medium: Some variation
- Low: Monotonous, institutional, large-scale only

### Step 3: Calculate Edge Scores

For each street segment:
- Count linear feet of soft edge vs. hard edge
- Calculate percentage of soft edge
- Identify gaps and concentrations

**Thresholds:**
- 70%+ soft edge: Vibrant street potential
- 50-70% soft edge: Mixed, some dead zones
- <50% soft edge: Struggling street life

### Step 4: Identify Problem Spots

Flag specific locations that undermine street life:
- Long blank walls (30+ feet continuous)
- Parking garage entrances at sidewalk
- Service areas facing pedestrian routes
- Vacant storefronts in otherwise active stretches
- Grade changes that separate building from sidewalk

### Step 5: Diagnose Patterns

Look for larger patterns:
- Does one side of street work while the other doesn't?
- Are problems clustered at certain building types?
- Is there a "dead zone" breaking an otherwise active stretch?
- Do certain uses correlate with activity?

---

## Output Format

```markdown
## Edge Quality Analysis: [Street/Block Name]

### Summary

**Overall Edge Quality:** [Soft / Mixed / Hard]

**Soft Edge Percentage:** [X]%

**Key Finding:** [One sentence on what's driving street life or killing it]

---

### Frontage Inventory

**[Side 1 - e.g., East Side]:**

| Segment | Address/Description | Type | Length | Edge Quality | Notes |
|---------|---------------------|------|--------|--------------|-------|
| 1 | [location] | [type] | [feet] | [Soft/Hard] | [notes] |
| 2 | [location] | [type] | [feet] | [Soft/Hard] | [notes] |
| ... | | | | | |

**Subtotal:** [X] feet soft / [Y] feet hard = [Z]% soft

**[Side 2 - e.g., West Side]:**

| Segment | Address/Description | Type | Length | Edge Quality | Notes |
|---------|---------------------|------|--------|--------------|-------|
| 1 | [location] | [type] | [feet] | [Soft/Hard] | [notes] |
| 2 | [location] | [type] | [feet] | [Soft/Hard] | [notes] |
| ... | | | | | |

**Subtotal:** [X] feet soft / [Y] feet hard = [Z]% soft

---

### Edge Quality Scoring

| Factor | Side 1 Score | Side 2 Score | Notes |
|--------|--------------|--------------|-------|
| Transparency | [H/M/L] | [H/M/L] | [observation] |
| Permeability | [H/M/L] | [H/M/L] | [observation] |
| Activation | [H/M/L] | [H/M/L] | [observation] |
| Spill-Out | [H/M/L] | [H/M/L] | [observation] |
| Human Scale | [H/M/L] | [H/M/L] | [observation] |

---

### Problem Spots

**Critical Issues:**

1. **[Location 1]:** [Description of hard edge problem]
   - Impact: [How this affects street life]
   - Severity: [High/Medium/Low]

2. **[Location 2]:** [Description]
   - Impact: [Effect]
   - Severity: [Level]

**Secondary Issues:**

- [Issue 3]
- [Issue 4]

---

### Opportunity Zones

**High Potential for Improvement:**

1. **[Location]:** [Current condition] -> [Possible improvement]
   - Feasibility: [Easy/Moderate/Difficult]
   - Impact: [High/Medium/Low]

2. **[Location]:** [Current] -> [Possible]
   - Feasibility: [Level]
   - Impact: [Level]

---

### Recommendations

**For Building Owners:**
- [Specific recommendation 1]
- [Specific recommendation 2]

**For City/Public Realm:**
- [Specific recommendation 3]
- [Specific recommendation 4]

**For New Development:**
- [Design guideline 1]
- [Design guideline 2]

---

### Conclusion

**Diagnosis:** [Summary of edge quality and its impact]

**Priority Intervention:** [Single most impactful change]

**Gehl Principle:** "Ground floors have a disproportionately large impact on the life and appeal of city space. If ground floors are friendly, soft and populated, pedestrians are surrounded by human activity."
```

---

## Constraints

- Distinguish between edges that COULD be softened and those that realistically can't
- Acknowledge that some hard edges serve necessary functions
- Focus on ground floors (first 15-20 feet vertically); upper floors matter less
- Consider both sides of the street - one dead side can kill the whole street
- Note seasonal/time variations when relevant (cafe seating only in summer)

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Can't determine ground floor use | Note as "Unknown" with visible characteristics; recommend verification |
| Mixed use within single frontage | Break into segments or note the mix |
| Historic building with inherent hard edges | Acknowledge historic value; focus on feasible interventions |
| New construction not yet occupied | Analyze based on design; note that activation depends on tenant |

---

## Integration

This skill is part of the **Jan Gehl** expert persona. It analyzes the critical building-street interface that determines whether streets have life. It pairs with:

- **public-life-survey** - To document activity patterns related to edge quality
- **human-scale-audit** - To assess the overall pedestrian experience
- **12-quality-criteria** - For comprehensive space evaluation

Edge quality analysis identifies WHERE to intervene; public life surveys measure the impact.