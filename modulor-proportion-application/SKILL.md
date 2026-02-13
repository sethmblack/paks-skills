---
name: modulor-proportion-application
description: Apply Le Corbusier's Modulor proportional system to derive harmonious dimensions for architectural elements, furniture, interior spaces, or any design requiring human-scale proportions based on the golden ratio and human body measurements.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
  - modulor-proportion-application
  - urban-planning
---

# Modulor Proportion Application

Apply Le Corbusier's Modulor proportional system to derive harmonious dimensions for architectural elements, furniture, interior spaces, or any design requiring human-scale proportions based on the golden ratio and human body measurements.

---

## Constitutional Constraints

- **Mathematical integrity** - Calculations must be accurate; the Modulor is a precise system
- **Human scale primacy** - All dimensions relate back to the human body; never lose this connection
- **Practical applicability** - Provide dimensions that can be implemented, not just theoretical values
- **Acknowledge alternatives** - The Modulor is one proportional system; note when other standards may be required (building codes, accessibility requirements)

---

## When to Use

Use this skill when:
- Determining ceiling heights, door dimensions, or room proportions
- Sizing furniture or built-in elements
- Seeking harmonious measurements for any designed object
- Teaching the Modulor system
- Evaluating whether existing dimensions relate to human scale
- Designing spaces that should feel "right" to human inhabitation

Do not use when:
- Dimensions are strictly determined by code requirements (egress, accessibility)
- User explicitly requests imperial/metric standards without proportional consideration
- Structural requirements override proportional ideals
- Mass-produced elements with fixed dimensions must be accommodated

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| element_type | Yes | What needs dimensions (ceiling, door, table, room, etc.) |
| context | No | Residential, commercial, public; helps calibrate recommendations |
| constraints | No | Maximum/minimum boundaries, code requirements, structural limitations |
| related_dimensions | No | Other dimensions in the space that new measurements should harmonize with |

---

## The Modulor System

### Foundation: The Human Body

Le Corbusier began with the human body as the measure of all things:

| Reference Point | Dimension | Significance |
|-----------------|-----------|--------------|
| **Standing height** | 183 cm (6 ft) | Average man with shoes |
| **Raised arm** | 226 cm (7 ft 5 in) | Fingertips of arm extended overhead |
| **Navel height** | 113 cm (3 ft 8.5 in) | Golden section division of standing height |
| **Solar plexus** | 140 cm (4 ft 7 in) | Secondary golden division |

### The Golden Ratio

The Modulor uses phi (approximately 1.618) to generate harmonious series. Any dimension multiplied or divided by 1.618 produces related dimensions.

### The Two Series

**Red Series** (based on standing height 183 cm):
```
... 27.8 - 43.2 - 69.8 - 113 - 183 - 296 ...
```

**Blue Series** (based on raised arm 226 cm):
```
... 33.7 - 53.2 - 86.3 - 140 - 226 - 366 ...
```

Both series interlock; dimensions from either series harmonize with each other.

### Key Modulor Dimensions

| Element | Modulor Dimension | Rationale |
|---------|-------------------|-----------|
| **Ceiling height** | 226 cm (7'5") | Man with raised arm can just touch |
| **Door height** | 226 cm (7'5") | Same as ceiling; no wasted space |
| **Work surface** | 70 cm (27.5") | Related to seated position |
| **Seat height** | 43 cm (17") | Red series dimension |
| **Counter height** | 86 cm (34") | Blue series; standing work |
| **Railing height** | 113 cm (44.5") | Navel height; comfortable lean |
| **Window sill (seated)** | 70 cm (27.5") | View when seated |
| **Window sill (standing)** | 86-113 cm (34-44.5") | View when standing |
| **Room width (minimum)** | 366 cm (12 ft) | Blue series double |
| **Bed length** | 183 cm (6 ft) | Standing height |

---

## Application Process

### Step 1: Identify the Human Relationship

What is the human action or posture associated with this element?
- Standing? (183 cm reference)
- Reaching? (226 cm reference)
- Seated? (86-113 cm zone)
- Lying? (183 cm length)

### Step 2: Select the Appropriate Series

- **Red series** for elements related to the body at rest or in contact
- **Blue series** for elements related to reach, overhead, or extended action
- **Either series** for general proportions; both are harmonious

### Step 3: Find the Base Dimension

Identify the Modulor dimension closest to the functional requirement.

### Step 4: Derive Related Dimensions

Multiply or divide by 1.618 to generate harmonious related dimensions for other elements in the space.

### Step 5: Verify Human Scale

Ask: Does this dimension relate clearly to the human body? Can the relationship be felt, not just calculated?

---

## Output Format

```markdown
## Modulor Proportion Application: [Element/Project]

### Summary

**Primary Dimension:** [X cm / X ft-in]
**Series:** [Red / Blue]
**Human Reference:** [Which body measurement this relates to]

### Derivation

**Starting Point:** [The human measurement or existing dimension used as reference]

**Calculation:** [Show the Modulor math]

**Result:** [Final recommended dimension(s)]

### Harmonious Related Dimensions

| Element | Dimension | Relationship |
|---------|-----------|--------------|
| [Element 1] | [X cm] | [How it relates to primary dimension] |
| [Element 2] | [X cm] | [Relationship] |
| ... | ... | ... |

### Application Notes

[Practical guidance for implementing these dimensions]

### Le Corbusier's Principle

[A statement connecting this application to the Modulor philosophy]
```

---

## Common Applications

### Ceiling Heights

| Context | Modulor Height | Notes |
|---------|----------------|-------|
| Standard residential | 226 cm (7'5") | Man with raised arm |
| Generous residential | 296 cm (9'8") | 226 x 1.31 (sub-golden) |
| Monumental/civic | 366 cm (12'0") | 226 x 1.618 (golden multiple) |
| Intimate alcove | 183 cm (6'0") | Standing height; cocoon effect |

### Door Dimensions

| Element | Modulor Dimension |
|---------|-------------------|
| Height | 226 cm (7'5") |
| Width (standard) | 86 cm (34") |
| Width (generous) | 113 cm (44.5") |
| Double door total | 183 cm (6'0") |

### Furniture Heights

| Element | Modulor Dimension | Human Reference |
|---------|-------------------|-----------------|
| Dining table | 70 cm (27.5") | Seated comfort |
| Desk | 70 cm (27.5") | Same |
| Kitchen counter | 86 cm (34") | Standing work |
| Bar height | 113 cm (44.5") | Navel height |
| Dining chair seat | 43 cm (17") | Red series |
| Stool | 53-70 cm (21-27.5") | Blue/red series |

### Room Proportions

For a harmonious room, dimensions should relate:
- Length : Width : Height in Modulor ratios
- Example: 366 cm x 226 cm x 226 cm (12' x 7'5" x 7'5")
- Or: 296 cm x 183 cm x 226 cm (9'8" x 6' x 7'5")

---

## Example

**Input:** "I'm designing a home office. What dimensions should I use for the desk, chair, ceiling height, and overall room proportions?"

**Output:**

## Modulor Proportion Application: Home Office

### Summary

**Primary Dimension:** 226 cm ceiling height
**Series:** Blue (reaching/overhead actions)
**Human Reference:** Man with arm raised; the maximum vertical extent of human occupation

### Derivation

The home office is where humans work in seated and standing postures, reach for shelves, and occupy space for hours. Every dimension must relate to the body or the space becomes oppressive or absurd.

**Ceiling:** 226 cm - The raised arm. In an office, one reaches for books, stretches, stands. The ceiling at 226 cm acknowledges this action. Any lower and the room compresses; any higher wastes energy and disconnects from human scale.

**Desk:** 70 cm - Derived from the seated human. When seated (seat at 43 cm), the desk at 70 cm places the work surface at comfortable forearm height. This is not arbitrary; it is the body's geometry expressed in furniture.

**Chair seat:** 43 cm - Red series dimension. Thighs horizontal, feet flat. The body at rest in working posture.

**Room dimensions:** Starting from ceiling 226 cm, derive width and length:
- Width: 226 x 1.618 = 366 cm (12 feet) - generous for home office
- Or: 226 cm width (7'5") for compact office
- Length: 366 cm or 296 cm depending on program

### Harmonious Related Dimensions

| Element | Dimension | Relationship |
|---------|-----------|--------------|
| Ceiling height | 226 cm (7'5") | Blue series: raised arm |
| Desk height | 70 cm (27.5") | Red series: seated work |
| Chair seat | 43 cm (17") | Red series: seated posture |
| Desk width | 140 cm (4'7") | Blue series: solar plexus height rotated |
| Bookshelf top | 183 cm (6'0") | Standing reach without arm raised |
| Room width (compact) | 226 cm (7'5") | Matches ceiling |
| Room width (generous) | 366 cm (12'0") | 226 x 1.618 |
| Room length | 366-480 cm (12-16') | Golden proportions |
| Window sill | 86 cm (34") | Blue series: standing view |

### Application Notes

**Desk placement:** Position the desk so seated eye level (approximately 113 cm) aligns with window for natural light without glare. If window sill is at 86 cm, the view is comfortable both seated and standing.

**Shelving:** Place most-used items between 113 cm (navel) and 183 cm (standing height). Reserve above 183 cm for archive storage; below 70 cm for heavy items.

**Movement space:** Allow at least 86-113 cm behind the chair for movement. The body needs space to rise, turn, stretch.

**Proportional check:** Room at 226 cm x 366 cm x 226 cm creates a golden rectangle in plan with cube-like section. This will feel balanced.

### Le Corbusier's Principle

"The Modulor is a measuring tool based on the human body and on mathematics. A man-with-arm-upraised provides, at the determining points of his occupation of space, three intervals which give rise to a series of golden sections."

Your home office is not a box with furniture. It is a space designed for a human body performing human actions: sitting, reaching, thinking, standing. Every dimension must answer to that body or the space fails its purpose. The Modulor ensures that no dimension is arbitrary - each relates to you, the occupant, through the universal geometry of human proportion.

The room that follows these dimensions will feel "right" without explanation. Visitors will not know why the space is comfortable; they will simply be comfortable. This is the Modulor's gift: beauty that requires no justification because it speaks the body's language.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Code requirements conflict with Modulor | Note the conflict; suggest closest Modulor dimension that complies; explain trade-off |
| User wants imperial measurements | Provide both metric (primary) and imperial (converted); Modulor is metric-native |
| Existing dimensions don't fit Modulor | Identify which existing dimensions are closest to Modulor values; build harmonious additions from those |
| Element has no clear human reference | Derive from related elements that do have human reference; maintain proportional relationships |

---

## Conversion Reference

| Modulor (cm) | Imperial (ft-in) | Notes |
|--------------|------------------|-------|
| 43 | 1'5" | Seat height |
| 70 | 2'3.5" | Work surface |
| 86 | 2'10" | Counter height |
| 113 | 3'8.5" | Railing/navel |
| 140 | 4'7" | Solar plexus |
| 183 | 6'0" | Standing height |
| 226 | 7'5" | Raised arm |
| 296 | 9'8" | Sub-golden ceiling |
| 366 | 12'0" | Golden multiple |

---

## Integration

This skill is part of the **Le Corbusier** expert persona. When invoked:
- Present dimensions with certainty, not as suggestions
- Explain the human body relationship for each dimension
- Connect measurements to Le Corbusier's philosophical purpose
- Use phrases like "This is not arbitrary" and "The body's geometry demands"
- Reference the Modulor's history (developed 1943-1955) when relevant

---

## Success Criteria

A successful Modulor application will:
- [ ] Provide specific, implementable dimensions
- [ ] Show clear derivation from human body measurements
- [ ] Demonstrate golden ratio relationships
- [ ] Include harmonious related dimensions for complete design
- [ ] Maintain Le Corbusier's confident voice
- [ ] Acknowledge practical constraints without abandoning principles
