---
name: transect-analysis
description: Diagnose any place, site, neighborhood, or development proposal by identifying its position on the rural-to-urban transect, then revealing mismatches between context, building type, street design, and land use that explain why the place succeeds or fails.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.2343
repository: https://github.com/sethmblack/paks-skills
keywords:
- transect-analysis
- urban-planning
---

# Transect Analysis

Diagnose any place, site, neighborhood, or development proposal by identifying its position on the rural-to-urban transect, then revealing mismatches between context, building type, street design, and land use that explain why the place succeeds or fails.

---

## Constitutional Constraints

- **Do not impose urban forms on rural contexts** - T1-T2 zones have different rules than T4-T6
- **Do not treat the transect as prescriptive ideology** - It is a diagnostic framework, not an aesthetic preference
- **Do not ignore local calibration** - What constitutes T4 in Miami differs from T4 in Vermont
- **Acknowledge when transect does not apply** - Special districts (airports, industrial areas) operate outside normal transect logic

---

## When to Use

- Evaluating why a place "feels wrong" despite individual elements being acceptable
- Planning mixed-use developments and calibrating appropriate intensity
- Diagnosing mismatch between building types and their context
- Assessing whether street design matches the intended character
- Recommending corrections to development proposals
- Understanding why certain uses fail in certain locations

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| place_description | Yes | Description of the site, neighborhood, or proposal being analyzed |
| intended_character | No | What the place is supposed to be (if different from current state) |
| specific_concerns | No | Particular issues to focus on (traffic, retail viability, walkability) |
| regional_context | No | Surrounding transect context and regional patterns |

---

## The Transect Framework

### The Six Zones

| Zone | Name | Character | Key Indicators |
|------|------|-----------|----------------|
| **T1** | Natural | Wilderness | No buildings, natural systems, preservation areas |
| **T2** | Rural | Agricultural | Large lots (5+ acres), barns, farmhouses, minimal infrastructure |
| **T3** | Sub-Urban | Low-density residential | Single-family homes, lawns, wide streets, informal plantings |
| **T4** | General Urban | Mixed residential | Rowhouses, small apartments, corner stores, street trees |
| **T5** | Urban Center | Mixed-use core | Main streets, apartments over shops, civic buildings, sidewalk dining |
| **T6** | Urban Core | High-density downtown | Towers, minimal setbacks, maximum intensity, transit hubs |
| **SD** | Special District | Unique conditions | Airports, campuses, hospitals, industrial (outside normal transect) |

### Zone Calibration Indicators

**T3 (Sub-Urban):**
- Building setbacks: 15-30 feet
- Lot coverage: 30-50%
- Building height: 1-2 stories
- Street width: 28-36 feet
- Parking: on-site, visible from street
- Uses: primarily residential, limited retail

**T4 (General Urban):**
- Building setbacks: 5-15 feet
- Lot coverage: 50-70%
- Building height: 2-4 stories
- Street width: 24-32 feet
- Parking: behind buildings, on-street
- Uses: residential with neighborhood retail

**T5 (Urban Center):**
- Building setbacks: 0-6 feet (build-to line)
- Lot coverage: 70-90%
- Building height: 3-6 stories
- Street width: 24-30 feet
- Parking: structured, on-street, rear lots
- Uses: mixed-use ground floor retail required

---

## Analysis Process

### Step 1: Zone Identification

**Question:** What transect zone does this place occupy OR should it occupy?

Examine:
- Current building types and their setbacks
- Street design and pedestrian infrastructure
- Parking location and quantity
- Land use mix
- Density (units per acre, FAR)
- Regional position (distance from urban core, transit access)

**Output:** "This site is currently [T_] but should be [T_] based on [regional position / planning intent / market demand]."

### Step 2: Element-by-Element Analysis

For each urban element, identify which zone it belongs to:

| Element | Current Zone | Target Zone | Mismatch? |
|---------|--------------|-------------|-----------|
| **Building Type** | [T_] | [T_] | [Yes/No] |
| **Building Placement** | [T_] | [T_] | [Yes/No] |
| **Street Design** | [T_] | [T_] | [Yes/No] |
| **Parking Treatment** | [T_] | [T_] | [Yes/No] |
| **Land Use Mix** | [T_] | [T_] | [Yes/No] |
| **Density** | [T_] | [T_] | [Yes/No] |
| **Civic Space** | [T_] | [T_] | [Yes/No] |

### Step 3: Mismatch Diagnosis

For each mismatch identified, explain:
1. **What is wrong:** The specific element that does not belong
2. **Why it fails:** How the mismatch causes dysfunction
3. **What belongs:** The appropriate element for the target zone

**Common Mismatch Patterns:**

| Pattern | Example | Consequence |
|---------|---------|-------------|
| **T3 Building in T5 Context** | Strip mall with surface parking on main street | Dead pedestrian environment, no street wall |
| **T5 Use in T3 Context** | Big box retail in residential area | Traffic overwhelms streets, no walkable customer base |
| **T3 Street in T5 Context** | Wide arterial with setback buildings downtown | Walkability destroyed, retail fails |
| **T5 Parking in T3 Context** | Structured parking in low-density suburb | Overbuilt, underutilized infrastructure |

### Step 4: Correction Recommendations

Provide specific changes to resolve mismatches:

**To raise a zone (intensify):**
- Reduce setbacks
- Increase building height limits
- Add build-to requirements
- Reduce parking requirements
- Allow mixed use by right

**To lower a zone (de-intensify):**
- Increase setbacks
- Reduce height limits
- Add landscape buffers
- Separate uses
- Increase lot size minimums

---

## Output Format

```markdown
## Transect Analysis: [Place Name/Description]

### Zone Determination

**Current State:** T[_] ([Zone Name])
**Target State:** T[_] ([Zone Name])
**Primary Issue:** [Brief statement of the fundamental mismatch]

### Element Analysis

| Element | Current | Target | Status |
|---------|---------|--------|--------|
| Building Type | T[_] | T[_] | [Match/Mismatch] |
| Building Placement | T[_] | T[_] | [Match/Mismatch] |
| Street Design | T[_] | T[_] | [Match/Mismatch] |
| Parking Treatment | T[_] | T[_] | [Match/Mismatch] |
| Land Use Mix | T[_] | T[_] | [Match/Mismatch] |
| Density | T[_] | T[_] | [Match/Mismatch] |

### Mismatch Diagnosis

**[Element 1]:** [What is wrong, why it fails, what belongs]

**[Element 2]:** [What is wrong, why it fails, what belongs]

### Recommended Corrections

1. **[Specific code change or design intervention]**
   - Current: [what exists]
   - Required: [what should replace it]
   - Impact: [what this fixes]

2. **[Next correction]**
   - ...

### Transect Integrity Score

**[_/6 elements aligned]** - [Brief assessment of overall transect coherence]

### Duany Principle Applied

> "[Relevant quote about transect, codes, or urban form]"
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient information about place | Request photos, maps, or site description; use available context clues |
| Place spans multiple zones | Analyze transition points; identify where zone changes should occur |
| Special district elements present | Note SD elements and exclude from transect scoring |
| Dispute about target zone | Present arguments for multiple scenarios; defer to planning intent |

---

## Example

**Input:** "We have a downtown block that was redeveloped in the 1970s. It has a bank with a drive-through, a one-story retail strip with parking in front, and a surface parking lot. It's surrounded by historic three-story buildings. Why doesn't it work?"

**Output:**

## Transect Analysis: 1970s Downtown Block Redevelopment

### Zone Determination

**Current State:** T3 (Sub-Urban) - despite downtown location
**Target State:** T5 (Urban Center) - based on surrounding historic fabric and regional position
**Primary Issue:** Suburban building patterns were inserted into an urban context, destroying the street wall and pedestrian environment

### Element Analysis

| Element | Current | Target | Status |
|---------|---------|--------|--------|
| Building Type | T3 (one-story strip) | T5 (3+ story mixed-use) | MISMATCH |
| Building Placement | T3 (setback from street) | T5 (at sidewalk) | MISMATCH |
| Street Design | T4 (reasonable) | T5 (needs enhancement) | PARTIAL |
| Parking Treatment | T3 (surface lot in front) | T5 (rear/structured) | MISMATCH |
| Land Use Mix | T4 (retail only) | T5 (mixed-use required) | MISMATCH |
| Density | T3 (0.3 FAR estimate) | T5 (2.0+ FAR) | MISMATCH |

### Mismatch Diagnosis

**Building Type (T3 in T5):** A one-story strip building belongs in a suburban shopping center, not downtown. It wastes valuable land, provides no housing, and creates dead frontage. Downtown requires minimum 2-3 story buildings with ground-floor retail.

**Building Placement (T3 in T5):** Buildings set back behind parking destroy the street wall that the historic buildings create. This breaks the "outdoor room" of the downtown street and makes walking unpleasant.

**Parking Treatment (T3 in T5):** Surface parking in front of buildings is the signature of suburban sprawl. It guarantees an unwalkable environment. Downtown parking must be behind buildings, in structures, or on-street.

**Density (T3 in T5):** At approximately 0.3 FAR, this block has perhaps 10% of the density of the surrounding historic fabric. It is an economic and urbanistic black hole in the middle of downtown.

### Recommended Corrections

1. **Eliminate surface parking lot; require infill development**
   - Current: Approximately 0.5 acre surface lot
   - Required: 3-4 story mixed-use building at sidewalk
   - Impact: Restores street wall, adds housing, increases tax base

2. **Remove drive-through; relocate bank to multi-story building**
   - Current: Single-story bank with drive-through destroying corner
   - Required: Ground-floor bank in mixed-use building; ATM only
   - Impact: Eliminates suburban auto-orientation, activates corner

3. **Redevelop strip retail as liner building**
   - Current: One-story setback strip with front parking
   - Required: 3-story building at build-to line; parking behind
   - Impact: Recreates street enclosure, adds residential above

4. **Form-based code overlay**
   - Current: Zoning allows T3 patterns by right
   - Required: T5 standards - 0-6' setback, 3-story minimum, no front parking
   - Impact: Prevents future T3 insertions

### Transect Integrity Score

**1/6 elements aligned** - This block is a suburban island in an urban sea. The 1970s redevelopment systematically violated every transect principle, replacing urban fabric with suburban patterns.

### Duany Principle Applied

> "The reason we have bad urbanism is that we have bad codes. Change the code and you change the outcome."

The current zoning permitted - perhaps required - this suburban development downtown. Without code reform, any redevelopment could repeat these errors.

---

## Integration

This skill is part of the **Andres Duany** expert persona. Use it as the primary diagnostic framework for any urban analysis. It chains with:

- **form-based-code-framework** - Once mismatches are diagnosed, use to write corrective code provisions
- **charrette-design-process** - When corrections require stakeholder buy-in, use to design collaborative process