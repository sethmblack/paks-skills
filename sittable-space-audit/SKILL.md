---
name: sittable-space-audit
description: Evaluate seating design against William H. Whyte's empirical criteria—ledge depth, step height, sun orientation, movability, and street relationship.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.2338
repository: https://github.com/sethmblack/paks-skills
keywords:
- sittable-space-audit
- urban-planning
---

# Sittable Space Audit

Evaluate seating design against William H. Whyte's empirical criteria—ledge depth, step height, sun orientation, movability, and street relationship. This skill diagnoses why seating is or isn't being used and recommends specific, measurable improvements.

---

## Constitutional Constraints

- **Design for all bodies** - Sittability criteria should accommodate diverse users
- **No hostile design** - Never recommend modifications to exclude people (spikes, dividers, sloped surfaces)
- **Accessibility matters** - Note when seating excludes wheelchair users, elderly, or disabled
- **Function over aesthetics** - Beautiful seating that no one uses is failed seating

---

## When to Use

- Benches or ledges in a public space go unused
- Observation reveals people sit in unexpected places (ground, planters, steps) instead of provided seating
- Evaluating a seating design before construction
- Diagnosing why a plaza feels unwelcoming despite having "enough" seating
- Calculating whether a space has adequate sitting capacity
- Recommending seating improvements with specific dimensions

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| space_description | Yes | The space and seating to audit |
| seating_details | Recommended | Types of seating, dimensions if known, locations |
| observations | Recommended | What has been observed about seating use |
| constraints | No | Budget, preservation rules, or physical limitations |

---

## The Whyte Sittability Criteria

### The Fundamental Insight

> "People tend to sit where there are places to sit."

This seems obvious. But Whyte found it routinely violated by designs that prioritize appearance over function. Beautiful ledges that are too narrow. Elegant benches that face walls. Handsome planters with edges that hurt to sit on.

**The human backside is a dimension architects often ignore.** This skill applies Whyte's empirical findings to ensure seating actually works.

---

## Dimension Criteria

### Sitting Height

| Height | Usability |
|--------|-----------|
| Under 12 inches | Awkward to sit; too low |
| **12-17 inches** | **Optimal range; 16-17" ideal** |
| 18-24 inches | Usable but legs dangle for shorter people |
| 24-36 inches | Usable but requires hopping up; perching |
| Over 36 inches | Not practical as seating |

**Note:** Steps in the 12-17" range function as natural seating. This is by design or by happy accident.

### Ledge/Seat Depth

| Depth | Usability |
|-------|-----------|
| Under 16 inches | Too narrow for comfort; minimal perching only |
| **16-20 inches** | **Minimum functional depth for single-sided seating** |
| **20-30 inches** | **Comfortable single-sided; narrow two-sided** |
| **30+ inches** | **Fully usable on both sides; count each side as seating** |

**Critical finding:** "The minimum-depth ledge we came across that was consistently used on both sides was 30 inches deep. Ledges and spaces two backsides deep seat more people."

### Seat Width (Per Person)

| Width | Usability |
|-------|-----------|
| Under 16 inches | Cramped |
| **16-20 inches** | **Standard per-person width** |
| 24+ inches | Comfortable; allows spreading out |

### Surface Material

| Material | Considerations |
|----------|----------------|
| Wood | Warm; comfortable year-round |
| Stone | Cold in winter; hot in summer if in sun |
| Metal | Extreme temperature variation; often uncomfortable |
| Concrete | Moderate temperature; texture matters |

**Key insight:** Material temperature affects use. A metal bench in summer sun is unusable. A wooden bench in the same spot works.

---

## Orientation Criteria

### The Street Edge Principle

> "The most popular spot in every plaza we studied was the edge nearest the sidewalk."

| Orientation | Appeal |
|-------------|--------|
| **Facing street** | **Highest appeal; watching the passing parade** |
| Facing open plaza | Moderate appeal if plaza has activity |
| Facing other people | Good for conversation; social seating |
| Facing blank wall | Almost never used; feels like punishment |
| Facing building entrance | Low appeal unless entrance is active |
| Back to street | Surprisingly acceptable if there's something to face |

### Sun Position

| Sun Relationship | Impact |
|------------------|--------|
| **In sun (spring/fall/winter)** | **Highest use** |
| Movable into sun | Enables following sun through day |
| Permanent shade | Lower use except in summer heat |
| Full summer sun, no shade option | Can be too hot; needs alternative |

**Whyte's observation:** People follow the sun across a plaza through the day. Movable chairs let them; fixed seating doesn't.

### Wind Exposure

| Wind Condition | Impact |
|----------------|--------|
| Protected from wind | Increases usability significantly |
| Wind tunnel / exposed corner | Dramatically decreases use |
| Variable (some shelter available) | People self-select sheltered spots |

---

## Capacity Calculation

### The Whyte Ratio

> One linear foot of sitting space per 30 square feet of plaza.

**Example:** A 6,000 square foot plaza should have at least 200 linear feet of sitting space.

### How to Count

| Seating Type | How to Measure |
|--------------|----------------|
| Bench | Length in feet (one side only unless 30"+ deep) |
| Ledge <30" deep | Length in feet (one side only) |
| Ledge 30"+ deep | Length x 2 (both sides count) |
| Steps (12-17" high) | Length of usable step edge |
| Movable chairs | Count chairs x 1.5 feet per chair |

### Effective vs. Nominal Capacity

**Nominal capacity:** Total linear feet of "seating surface"

**Effective capacity:** Linear feet actually usable per Whyte criteria:
- Deduct surfaces that are wrong height
- Deduct ledges that are too narrow (<16")
- Deduct seating facing blank walls
- Deduct surfaces with hostile materials or temperatures
- Deduct seating blocked by planters or barriers

**The real question:** What's the effective capacity? Many plazas have "enough" nominal seating that fails the usability tests.

---

## Movable vs. Fixed Assessment

### The Movable Chair Advantage

> "Users feel a sense of ownership because they can arrange movable chairs to suit themselves."

| Factor | Movable Chairs | Fixed Benches |
|--------|----------------|---------------|
| User control | High - arrange for sun, conversation, view | None |
| Personalization | Inches of movement = psychological ownership | Forced to accept placement |
| Group flexibility | Can cluster for groups, separate for privacy | Fixed social distance |
| Sun following | Can move through day | Stuck in original orientation |
| Maintenance | Requires management; some loss expected | Low maintenance |
| Theft concern | Often overstated; Bryant Park proved it works | Non-issue |

**Recommendation:** Where possible, include movable chairs. Even 20-30 chairs transforms a space.

---

## Audit Checklist

### Physical Measurements

- [ ] Seat/ledge heights (measure in inches)
- [ ] Seat/ledge depths (measure in inches)
- [ ] Total linear feet of seating surfaces
- [ ] Surface materials for each seating type
- [ ] Orientation of each seating element (what does it face?)

### Environmental Factors

- [ ] Sun pattern at peak use time (noon)
- [ ] Wind exposure assessment
- [ ] Proximity to food (within 100 feet?)
- [ ] Street edge relationship (distance, elevation, sightlines)

### Observational Data

- [ ] Which seating is actually used?
- [ ] Which seating is avoided?
- [ ] Do people sit elsewhere (ground, planters, steps) instead?
- [ ] Average dwell time on used seating
- [ ] Peak occupancy of seating

---

## Output Format

```markdown
## Sittable Space Audit: [Space Name]

### Seating Inventory

| Seating Type | Location | Height | Depth | Length | Faces | Material | Effective? |
|--------------|----------|--------|-------|--------|-------|----------|------------|
| [Type] | [Where] | [X"] | [X"] | [X ft] | [What] | [Material] | [Y/N + reason] |

### Capacity Analysis

**Plaza area:** [X] square feet
**Whyte ratio requirement:** [X ÷ 30 = Y] linear feet
**Nominal seating:** [Z] linear feet
**Effective seating:** [A] linear feet (after deductions)
**Verdict:** [Over/Under capacity by X linear feet]

### Dimension Failures

| Element | Issue | Measurement | Standard | Impact |
|---------|-------|-------------|----------|--------|
| [What] | [Problem] | [Actual] | [Should be] | [Effect on use] |

### Orientation Failures

| Element | Current Orientation | Better Orientation | Expected Improvement |
|---------|--------------------|--------------------|---------------------|
| [What] | [Faces what] | [Should face] | [Why it would help] |

### Environmental Issues

| Factor | Status | Recommendation |
|--------|--------|----------------|
| Sun access | [Good/Poor/Mixed] | [Action if needed] |
| Wind exposure | [Good/Poor/Mixed] | [Action if needed] |
| Food proximity | [Good/Poor/Mixed] | [Action if needed] |
| Street relationship | [Good/Poor/Mixed] | [Action if needed] |

### Priority Recommendations

#### Immediate (Low Cost)
1. [Recommendation with specific measurements]
2. [Recommendation]

#### Short-Term (Medium Investment)
1. [Recommendation with specific measurements]
2. [Recommendation]

#### Long-Term (Capital Investment)
1. [Recommendation]

### The Core Problem
[Single most impactful finding, if one dominates]

### Before/After Calculation
**Current effective capacity:** [X] linear feet
**After recommendations:** [Y] linear feet
**Improvement:** [Z]% increase
```

---

## Example Application

**Input:** "Our building's plaza has granite benches but people sit on the steps instead. What's wrong with the benches?"

**Output:**

## Sittable Space Audit: Building Plaza

### Initial Assessment

The symptom—people choosing steps over benches—suggests the benches fail on usability while the steps accidentally succeed. Let's diagnose.

### Common Bench Failures (Likely Issues)

Based on the pattern described, check these first:

| Possible Issue | What to Measure | Likely Finding |
|----------------|-----------------|----------------|
| Height | Measure bench seat height | May be too high (>18") |
| Depth | Measure bench seat depth | May be too narrow (<16") |
| Orientation | What do benches face? | May face blank wall or inward |
| Material | Granite in sun/shade? | May be uncomfortable temperature |
| Location | Where are benches vs. steps? | Benches may be in dead zone |

### Why Steps Work

Steps in the 12-17" height range are naturally sittable. They often:
- Face outward (toward street or plaza action)
- Offer depth flexibility (sit on edge or lean back)
- Cluster activity (people sit near each other on steps)
- Feel less formal (steps = casual seating)

**Key insight:** People aren't avoiding benches because they're difficult. They're choosing steps because steps are better sittable space.

### Diagnostic Questions

1. **What do the benches face?**
   - If they face the building entrance or a blank wall, people will avoid them.
   - Steps likely face outward toward activity.

2. **Where is the sun at noon?**
   - Steps may be in sun while benches are in shadow.
   - Or benches in full sun may be too hot (granite absorbs heat).

3. **How deep are the bench seats?**
   - Granite benches often prioritize aesthetics over depth.
   - Measure: under 16" = uncomfortable.

4. **How high are the benches?**
   - Formal granite benches are sometimes 18-20" (too high for comfort).
   - Steps in 12-17" range feel more natural.

5. **Are benches isolated or clustered?**
   - Scattered single benches discourage use.
   - Steps create continuous seating that feels social.

### Hypothetical Audit (Based on Common Patterns)

| Element | Likely Measurement | Whyte Standard | Verdict |
|---------|-------------------|----------------|---------|
| Bench height | 19-20" | 16-17" optimal | Too high |
| Bench depth | 14-16" | 16-20" minimum | Too shallow |
| Bench faces | Building entrance | Street or plaza | Wrong orientation |
| Bench material | Granite in shadow | Warm or sun-exposed | Cold |
| Step height | 14-16" | 12-17" optimal | Good |
| Step orientation | Outward to plaza | Outward | Good |

### Recommended Actions

#### Immediate (Validate This Analysis)
1. **Measure benches** - Height and depth in inches
2. **Document orientation** - What does each bench face?
3. **Observe for 1 hour at noon** - Where do people actually sit?
4. **Check sun pattern** - Are benches in sun or shadow at peak time?

#### Based on Likely Findings

**If benches are too shallow (<16"):**
- Can't fix without replacing; this is a design failure
- Alternative: Add movable chairs elsewhere in plaza

**If benches face wrong direction:**
- Can sometimes reposition if not permanently installed
- If fixed, add new seating with correct orientation

**If sun/temperature issue:**
- Add movable chairs in sunny zone
- Benches may be usable in summer when shade is desirable

### The Core Problem

"People sit on the steps instead of the benches" = **the benches fail the sittability test.**

This is common. Architects design handsome benches that photograph well. Users choose ugly steps that actually work.

**The solution is not to make steps less appealing.** The solution is to make formal seating as functional as the steps already are:
- 16-17" height
- 16"+ depth
- Facing the action
- In or near the sun
- Clustered, not scattered

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Dimensions not available | Provide criteria so client can measure; offer to analyze once measured |
| Historic or protected seating | Note constraints; recommend adding supplemental seating rather than modifying |
| No observations available | Provide the audit framework; findings are hypotheses until observed |
| Seating technically adequate but unused | Look beyond dimensions to orientation, sun, street relationship, triangulation |
| Budget prohibits changes | Prioritize movable chairs (low cost); reposition existing if possible |

---

## Integration

This skill is part of the **William Whyte** expert persona. Use it when seating exists but isn't working.

Use with:
- **plaza-observation-method** - First observe to confirm which seating is/isn't used
- **triangulation-design** - Good seating supports triangulation; position seating near social catalysts

---

## Success Criteria

A complete sittable space audit produces:
- [ ] Measured inventory of all seating (height, depth, length)
- [ ] Capacity calculation (nominal vs. effective)
- [ ] Identification of specific dimension failures
- [ ] Assessment of orientation relative to street and activity
- [ ] Environmental factors documented (sun, wind, food)
- [ ] Prioritized recommendations with specific measurements
- [ ] Before/after capacity estimate if recommendations implemented