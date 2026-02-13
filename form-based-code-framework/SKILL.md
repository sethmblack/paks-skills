---
name: form-based-code-framework
description: Translate urban design goals into regulatory language - identifying what code provisions enable walkable urbanism, diagnosing what in existing codes prevents good outcomes, and writing specific form-based standards that can be adopted.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.4025
repository: https://github.com/sethmblack/paks-skills
keywords:
- form-based-code-framework
- urban-planning
---

# Form-Based Code Framework

Translate urban design goals into regulatory language - identifying what code provisions enable walkable urbanism, diagnosing what in existing codes prevents good outcomes, and writing specific form-based standards that can be adopted.

---

## Constitutional Constraints

- **Do not write codes that require variance for good design** - The code should make good urbanism by-right
- **Do not propose regulations without implementation pathway** - Consider adoption mechanisms (overlay, amendment, replacement)
- **Do not ignore existing legal framework** - Code must work within state enabling legislation
- **Do not overcomplicate** - Prefer simple, enforceable standards over elaborate systems
- **Acknowledge calibration needs** - Standards must be adjusted for local context

---

## When to Use

- Diagnosing why a jurisdiction produces sprawl despite good intentions
- Writing development standards for new planned communities
- Proposing zoning amendments or overlay districts
- Converting Euclidean zoning to form-based codes
- Creating standards for specific sites or districts
- Advising developers on what code changes to request

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| design_goal | Yes | What urban form or character is desired |
| current_code_issues | No | Known problems with existing regulations |
| jurisdiction_context | No | State/local legal context, existing zoning framework |
| target_transect | No | Intended transect zone(s) for the area |
| site_specifics | No | Lot sizes, street frontages, existing buildings |

---

## The Form-Based Code Approach

### Euclidean vs. Form-Based: Core Difference

| Aspect | Euclidean (Use-Based) | Form-Based |
|--------|----------------------|------------|
| **Primary question** | What use is allowed? | What building form is allowed? |
| **Assumption** | Uses conflict; separate them | Forms conflict; uses are flexible |
| **Controls** | Use categories, density limits, setback minimums | Building envelopes, frontage types, build-to lines |
| **Result** | Single-use pods | Mixed-use buildings in coherent streetscapes |

### Key Insight

> "Design standards without a code are just opinions. A code is law."

The code determines what gets built. If the code mandates setbacks, parking minimums, and use separation, you will get sprawl regardless of design guidelines, charrettes, or good intentions.

---

## Code Audit Process

### Step 1: Identify Problem Provisions

Review existing code for sprawl-mandating provisions:

| Category | Sprawl Provision | Look For |
|----------|------------------|----------|
| **Setbacks** | Minimum setbacks | "Buildings shall be set back at least X feet" |
| **Parking** | Parking minimums | "X spaces required per 1,000 SF" |
| **Use Separation** | Single-use zoning | "Residential uses prohibited in commercial districts" |
| **Lot Size** | Large lot minimums | "Minimum lot size: 10,000 SF" |
| **Block Length** | No maximum | [Absence of block length limits] |
| **Street Width** | Wide street requirements | "Minimum 36-foot pavement width" |
| **Density Caps** | Units per acre limits | "Maximum 8 dwelling units per acre" |

### Step 2: Diagnose Impact

For each problem provision, identify:
1. **What it mandates:** The physical outcome required
2. **Why it exists:** Original (often outdated) justification
3. **What it prevents:** The good urbanism it makes impossible

### Step 3: Propose Corrections

For each problem provision, write corrective code language.

---

## Form-Based Code Elements

### Building Placement Standards

**Instead of:** Minimum setback 25 feet
**Use:** Build-to line at 0-6 feet from right-of-way

| Standard | T3 | T4 | T5 | T6 |
|----------|----|----|----|----|
| Front setback (min) | 10' | 5' | 0' | 0' |
| Front setback (max) | 30' | 15' | 6' | 2' |
| Side setback (min) | 5' | 0'-3' | 0' | 0' |
| Rear setback (min) | 15' | 10' | 5' | 0' |
| Lot coverage (max) | 50% | 70% | 90% | 100% |

### Building Height Standards

| Standard | T3 | T4 | T5 | T6 |
|----------|----|----|----|----|
| Stories (min) | 1 | 2 | 2 | 4 |
| Stories (max) | 2.5 | 4 | 6 | unlimited |
| Height at setback | N/A | N/A | Match adjacent | Match adjacent |

### Frontage Type Requirements

| Frontage Type | Description | Appropriate Zones |
|---------------|-------------|-------------------|
| **Shopfront** | Retail display at sidewalk, recessed entry | T5, T6 |
| **Gallery** | Colonnade covering sidewalk | T5, T6 |
| **Arcade** | Covered walkway within building | T5, T6 |
| **Stoop** | Elevated entry, stairs to sidewalk | T4, T5 |
| **Porch** | Covered semi-private transition space | T3, T4 |
| **Forecourt** | Recessed courtyard at entry | T4, T5 |
| **Dooryard** | Elevated yard with fence/wall | T3, T4 |

### Parking Standards

**Instead of:** Minimum 4 spaces per 1,000 SF
**Use:** Maximum parking; location requirements

| Standard | T3 | T4 | T5 | T6 |
|----------|----|----|----|----|
| Minimum required | Per market | 0 | 0 | 0 |
| Maximum allowed | N/A | 1.5/unit | 1.0/unit | 0.5/unit |
| Location | Side/rear preferred | Rear only | Rear/structured | Structured only |
| Front lot parking | Permitted | Prohibited | Prohibited | Prohibited |

### Street/Thoroughfare Standards

| Element | T3 | T4 | T5 | T6 |
|---------|----|----|----|----|
| Travel lane width | 11-12' | 10-11' | 10' | 10' |
| On-street parking | Optional | Required | Required | Required |
| Sidewalk width (min) | 5' | 6' | 8' | 12' |
| Tree planting | Informal | Regular | Regular | Urban |
| Curb radius | 25' | 15' | 10' | 5' |
| Block length (max) | N/A | 600' | 400' | 300' |

### Use Standards

**Instead of:** Detailed use categories with conditions
**Use:** Broad use permissions by transect zone

| Use Category | T3 | T4 | T5 | T6 |
|--------------|----|----|----|----|
| Single-family | By right | By right | Limited | N/A |
| Townhouse/rowhouse | Limited | By right | By right | By right |
| Apartment (small) | Conditional | By right | By right | By right |
| Apartment (large) | N/A | Limited | By right | By right |
| Retail (neighborhood) | Conditional | By right | By right | By right |
| Retail (general) | N/A | Limited | By right | By right |
| Office | Conditional | By right | By right | By right |
| Civic | By right | By right | By right | By right |

---

## Output Format

```markdown
## Form-Based Code Analysis: [Project/Area Name]

### Design Intent

**Target Character:** [Description of desired urban form]
**Target Transect Zone(s):** T[_] to T[_]
**Key Objectives:**
- [Objective 1]
- [Objective 2]
- [Objective 3]

### Current Code Diagnosis

| Problem Provision | Current Language | Impact | Priority |
|-------------------|------------------|--------|----------|
| [Provision 1] | "[Quote from code]" | [What it prevents] | HIGH/MED/LOW |
| [Provision 2] | ... | ... | ... |

### Recommended Code Language

#### Building Placement

**Section [X]: Build-to Lines**

> In the [District Name], buildings shall be located within the build-to zone as follows:
> - Primary frontage: [X]-[Y] feet from right-of-way
> - Secondary frontage: [X]-[Y] feet from right-of-way
> - Frontage buildout: minimum [X]% of lot width

**Section [X]: Building Height**

> - Minimum height: [X] stories / [X] feet
> - Maximum height: [X] stories / [X] feet at build-to line; [X] stories / [X] feet with stepback

#### Parking

**Section [X]: Parking Requirements**

> - Minimum parking: None required
> - Maximum parking: [X] spaces per [1,000 SF / dwelling unit]
> - Location: [Rear of buildings only / structured / underground]
> - Surface lots: [Prohibited on primary frontage / limited to X% of lot area]

#### Frontage

**Section [X]: Frontage Types**

> The following frontage types are [required/permitted] in [District Name]:
> - [Type 1]: [Description and standards]
> - [Type 2]: [Description and standards]

#### Uses

**Section [X]: Permitted Uses**

> The following uses are permitted by right in [District Name]:
> [List of uses with any conditions]

### Implementation Strategy

**Recommended Pathway:** [Overlay district / Text amendment / New chapter / SmartCode adoption]

**Adoption Process:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Potential Opposition:**
- [Concern 1]: [Response strategy]
- [Concern 2]: [Response strategy]

### Duany Principle Applied

> "[Relevant quote about codes and urbanism]"
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Unknown state enabling legislation | Note uncertainty; provide model language adaptable to context |
| Conflicting objectives (density vs. character) | Present trade-offs explicitly; recommend transect calibration |
| Existing legal constraints (deed restrictions, etc.) | Identify non-code barriers; note limitations of code reform |
| Political infeasibility | Provide incremental pathway; prioritize highest-impact changes |

---

## Integration

This skill is part of the **Andres Duany** expert persona. Use it after transect analysis has diagnosed problems, to provide codifiable solutions. It chains with:

- **transect-analysis** - Diagnose before prescribing; understand the target zone before writing code
- **charrette-design-process** - When code adoption requires political support, design stakeholder engagement process