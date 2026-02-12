---
name: design-integrity-check
description: Evaluate whether all elements of a design speak the same language—the
  same grammar of form, pattern, and detail—and recommend corrections to achieve unity.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- design-integrity-check
- storytelling
- structure
- writing
---

# Design Integrity Check

Evaluate whether all elements of a design speak the same language—the same grammar of form, pattern, and detail—and recommend corrections to achieve unity.

---

## When to Use

- Design feels like assembled parts rather than unified whole
- Different elements seem to come from different projects
- Request for "design integrity" or "unity" assessment
- Something feels inconsistent but hard to pinpoint
- Final review before implementation to ensure coherence

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| design | Yes | The design being evaluated (space, product, system) |
| elements | Yes | List of components/elements to assess |
| intent | No | Stated unifying principle or vision |
| context | No | Setting or application context |

---

## The Framework

### Part 1: Identify the Grammar

Every design should have its own language—a consistent vocabulary:

**Geometric Vocabulary:**
- What shapes recur? (Circles, squares, hexagons, organic curves?)
- What angles are characteristic? (90-degree, 60-degree, organic?)
- What proportional relationships define the design?

**Material Palette:**
- What materials are used?
- How are they combined?
- What is the hierarchy among them?

**Detail Language:**
- How do joints and connections work?
- What is the character of edges? (Sharp, rounded, beveled?)
- How do elements meet one another?

**Rhythm and Pattern:**
- What spacing and intervals recur?
- What patterns emerge?
- What is the scale relationship between elements?

### Part 2: Audit Each Element

For each element, assess whether it speaks the same language:

**Questions to Ask:**
- Does this element use the same geometric vocabulary?
- Does its material belong to the established palette?
- Do its details match the overall detail language?
- Does it respect the rhythm and proportional system?
- Could this element only belong to this design, or could it be from anywhere?

**Integrity Levels:**
| Level | Description |
|-------|-------------|
| Native | Element clearly speaks the same language; couldn't belong elsewhere |
| Compatible | Element doesn't violate the grammar but doesn't reinforce it |
| Discordant | Element speaks a different language; creates dissonance |
| Foreign | Element clearly from different design; disrupts unity |

### Part 3: Find the Violations

Identify specific grammar violations:

**Common Violation Patterns:**
- **Mixed geometries:** Rectilinear architecture with circular furniture
- **Material intrusion:** Plastic element in wood/stone vocabulary
- **Detail inconsistency:** Rounded corners throughout, one element with sharp edges
- **Scale misalignment:** Elements at incompatible proportional scales
- **Style mixing:** One element from different aesthetic tradition

### Part 4: Recommend Corrections

For each discordant element:
- What would bring it into grammar?
- Should it be modified or replaced?
- What native alternative exists?

---

## Output Format

```markdown
## Design Integrity Check

### The Design's Grammar

**Geometric Vocabulary:**
- Primary shapes: [shapes used throughout]
- Characteristic angles: [angle relationships]
- Proportional system: [e.g., 1:2 ratios, golden section, module-based]

**Material Palette:**
- Primary materials: [list]
- Secondary materials: [list]
- Material hierarchy: [how they relate]

**Detail Language:**
- Edge character: [sharp/rounded/beveled]
- Connection method: [how elements join]
- Surface treatment: [textures, finishes]

**Rhythm and Pattern:**
- Spacing intervals: [recurring distances]
- Scale relationships: [how sizes relate]
- Pattern motifs: [recurring patterns]

### Element Audit

| Element | Grammar Alignment | Assessment |
|---------|-------------------|------------|
| [Element 1] | [how it aligns or doesn't] | [Native/Compatible/Discordant/Foreign] |
| [Element 2] | ... | ... |
| ... | ... | ... |

### Integrity Score
**Elements Speaking Native Grammar:** [X of Y]
**Overall Integrity:** [High/Medium/Low]

### Violations Identified

#### [Violation 1]
- **Element:** [what element]
- **The Problem:** [how it violates grammar]
- **Evidence:** [specific discordance]
- **Recommendation:** [how to correct]

#### [Violation 2]
...

### Corrections Summary

| Element | Current State | Recommended Change | Result |
|---------|---------------|-------------------|--------|
| [Element] | [discordant aspect] | [specific change] | [how it achieves unity] |
| ... | ... | ... | ... |

### Unified Vision
[Paragraph describing what full integrity would look and feel like]
```

---

## Constraints

- Do not impose a grammar—discover what the design intends
- Unity does not mean monotony—variation within grammar is good
- Some intentional contrast can be valid—distinguish from accidental
- Context may justify certain exceptions
- The goal is coherent expression, not rigid conformity

---

## Example

**Input:** "Check integrity of a restaurant design: exposed brick walls, industrial pendant lights, reclaimed wood tables, Eames molded plastic chairs, marble bar top, brass hardware, neon sign."

**Output:**

## Design Integrity Check

### The Design's Grammar

**Geometric Vocabulary:**
- Primary shapes: Rectilinear (brick modules, table edges, bar form)
- Characteristic angles: 90-degree dominant; some curves in seating
- Proportional system: Industrial scale—substantial, chunky proportions

**Material Palette:**
- Primary materials: Brick (warm earth tones), reclaimed wood (warm, aged)
- Secondary materials: Metal (industrial), glass, marble
- Material hierarchy: Warm organic materials (brick, wood) dominant; metal as accent

**Detail Language:**
- Edge character: Raw, exposed, honest
- Connection method: Visible, industrial (exposed bolts, simple joints)
- Surface treatment: Textured, aged, patinated

**Rhythm and Pattern:**
- Spacing intervals: Brick module rhythm, wood plank widths
- Scale relationships: Substantial, not delicate
- Pattern motifs: Linear horizontals (wood planks, brick courses)

### Element Audit

| Element | Grammar Alignment | Assessment |
|---------|-------------------|------------|
| Exposed brick walls | Establishes warm, textured, honest material foundation | Native |
| Industrial pendant lights | Metal, exposed bulbs, honest mechanics | Native |
| Reclaimed wood tables | Warm material, substantial scale, aged character | Native |
| Eames molded plastic chairs | Mid-century modern, plastic, organic curves | Discordant |
| Marble bar top | Natural material, but refined/polished vs. raw aesthetic | Compatible |
| Brass hardware | Warm metal, develops patina, honest aging | Native |
| Neon sign | 20th-century industrial, but specific aesthetic | Compatible |

### Integrity Score
**Elements Speaking Native Grammar:** 4 of 7 (Native), 2 Compatible, 1 Discordant
**Overall Integrity:** Medium—one significant discordance undermines otherwise coherent vocabulary

### Violations Identified

#### Violation 1: Eames Molded Plastic Chairs
- **Element:** Seating
- **The Problem:** The Eames molded plastic chair speaks Mid-Century Modern language: organic curves, molded plastic, refined proportions, designer pedigree. The rest of the space speaks industrial-reclaimed language: raw materials, substantial scale, honest age, anonymous origins.
- **Evidence:**
  - Material: Plastic in a palette of brick/wood/metal
  - Form: Organic curves in a rectilinear vocabulary
  - Character: Designed refinement vs. found/reclaimed authenticity
  - Scale: Lightweight, delicate vs. substantial, chunky
- **Recommendation:** Replace with seating that speaks industrial-reclaimed language:
  - Option A: Vintage industrial metal chairs (Tolix-style) with aged patina
  - Option B: Simple wood chairs with reclaimed wood to match tables
  - Option C: Metal-frame chairs with reclaimed wood seats
  - All options: Substantial scale, raw/honest materials, visible construction

### Secondary Observations

**Marble Bar Top:**
- Not discordant but could be more native
- Current state: Polished marble reads refined, upscale
- Consider: Honed/matte finish would be more consistent with raw aesthetic; alternatively, concrete or zinc bar top would speak native grammar

**Neon Sign:**
- Compatible but contextual
- Works if content relates to industrial/working-class heritage
- Would be discordant if content is precious or ironic

### Corrections Summary

| Element | Current State | Recommended Change | Result |
|---------|---------------|-------------------|--------|
| Chairs | Eames molded plastic (mid-century) | Vintage industrial metal or simple reclaimed wood | Seating joins material/form vocabulary |
| Bar top | Polished marble | Consider honed finish or zinc | More consistent with raw, honest aesthetic |

### Unified Vision

With the chair substitution, the restaurant achieves integrity: a vocabulary of reclaimed, industrial, honest materials throughout. Brick walls establish the warm, textured foundation. Reclaimed wood tables and (now) industrial or wood chairs create seating that belongs to this space and could belong to no other. Industrial pendant lights illuminate with honest mechanics—bulbs exposed, fixtures utilitarian. Brass hardware ages gracefully alongside the patinated surroundings. Even the neon sign, if well-chosen, joins the industrial heritage narrative.

Every element speaks the same language: substantial scale, honest materials, visible construction, graceful aging. A guest experiencing this space feels coherence—not the assembled-from-catalog feeling of a space where a designer mixed "industrial" mood boards with convenient furniture orders, but the integrity of a space where each element reinforces every other. The Eames chair, beautiful in the right context, would here feel like a tourist; its replacement feels like it has always belonged.

---

## Integration

This skill is part of the **Frank Lloyd Wright** expert persona. Use it when designs feel assembled rather than unified, when elements seem to speak different languages.
