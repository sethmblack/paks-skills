---
name: plaza-observation-method
description: Teach and apply William H. Whyte's systematic observation methodology for evaluating public spaces.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
  - plaza-observation-method
  - urban-planning
---

# Plaza Observation Method

Teach and apply William H. Whyte's systematic observation methodology for evaluating public spaces. This skill provides the foundational framework for understanding how people actually use plazas, parks, and urban spaces—replacing assumptions with evidence.

---

## Constitutional Constraints

- **Observe, don't judge** - Document behavior patterns without moralizing about them
- **Respect privacy** - Focus on aggregate patterns, not individual identification
- **No hostile design advice** - Do not recommend observations for the purpose of excluding people
- **Evidence over opinion** - All recommendations must be tied to observable data

---

## When to Use

- Evaluating why a public space works or fails
- Before redesigning an existing space
- Teaching observation methodology to planning teams
- Challenging assumptions about public behavior
- Creating a baseline for measuring intervention impact
- Comparing multiple spaces systematically

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| space_description | Yes | The public space to be observed or evaluated |
| observation_type | No | "teaching" (methodology focus) or "diagnostic" (evaluate specific space) |
| time_constraints | No | How much observation time is available |
| specific_concerns | No | Particular behaviors or design elements to focus on |

---

## The Whyte Observation Framework

### Core Principle

> "Design should follow observation, not precede it."

Before you redesign, before you recommend, before you assume—watch. The behavior of actual users is the truest test of any design.

---

## Phase 1: Establish the Observation Protocol

### When to Observe

Time-lapse thinking requires systematic coverage:

| Period | Why Important |
|--------|---------------|
| **Weekday lunch (11:30 AM - 1:30 PM)** | Peak corporate plaza use; most revealing single period |
| **Morning (7:30 - 9:00 AM)** | Commuter patterns; who passes through vs. who lingers |
| **Afternoon (3:00 - 5:00 PM)** | Second activity peak; different user mix |
| **Evening (6:00 - 8:00 PM)** | Transition period; social vs. transient use |
| **Weekend midday** | Different population entirely; tests true public nature |

**Minimum viable observation:** Station someone at 11:30 AM on a weekday. This single snapshot reveals more than any plan.

### Weather Conditions

Note conditions for each observation period:
- Sunny vs. overcast (sun patterns are critical)
- Temperature range
- Wind conditions
- Recent weather (rain affects surfaces)

Weather changes behavior. Document it so patterns can be compared fairly.

---

## Phase 2: What to Count

### People Count

**The fundamental metric.** Count people at regular intervals:

| Interval | Method |
|----------|--------|
| Snapshot counts | Every 15 minutes, count all people in space |
| Flow counts | Count people entering/exiting over 5-minute periods |
| Stationary vs. moving | Distinguish lingerers from passers-through |

**Benchmark:** Whyte found successful plazas have roughly 1 person per 100 square feet at peak times. Below that, the space feels empty and self-perpetuates emptiness.

### Sitting Behavior

Track where people sit:

| Category | What to Note |
|----------|--------------|
| **Location** | Map exactly where each sitter is positioned |
| **Furniture type** | Bench, ledge, steps, movable chair, ground |
| **Orientation** | Facing street? Facing interior? Facing other people? |
| **Duration** | How long do they stay? Time a sample |
| **Group size** | Alone, pairs, groups |
| **Sun position** | Are they in sun or shade? Does it change? |

**Key pattern:** People cluster. Mark clusters on your map. Where clusters form tells you where the space is working.

### Standing Conversations

Whyte found 57% of conversations at the Saks corner happened at the most congested spot.

| Element | Track |
|---------|-------|
| **Location** | Where do people stop to talk? Map it. |
| **Duration** | How long do conversations last? |
| **Flow impact** | Do they block pedestrian flow? Do people flow around them? |
| **Group formation** | How do groups form and dissolve? |

**Counter-intuitive finding:** People stop to talk at the busiest, most congested spots—not quiet corners. This is intentional, not accidental.

---

## Phase 3: What to Map

Create physical documentation:

### Activity Map

On a plan of the space, mark:
- Where people sit (with symbols for singles, pairs, groups)
- Where people stand talking
- Movement paths (desire lines)
- Areas that remain empty
- The sun pattern at observation time

### Time-Lapse Thinking

If actual time-lapse isn't possible, create a series of maps:
- Map at 11:30 AM
- Map at 12:00 PM
- Map at 12:30 PM
- Map at 1:00 PM

Overlay these mentally. Where does activity consistently cluster? Where is consistently empty?

### The Empty Zones

Pay special attention to what people avoid:
- Areas that look usable but go unused
- Seating that never fills
- Spaces that block or repel

**Key question:** Why is this empty? The answer often reveals design failure.

---

## Phase 4: What to Interview

Brief, non-intrusive questions:

| Question | What It Reveals |
|----------|-----------------|
| "Do you come here often?" | Repeat vs. first-time use patterns |
| "Why did you choose this spot?" | User logic that designers miss |
| "What would make this better?" | Direct user feedback |
| "Is there anything you avoid about this space?" | Hidden problems |

**Interview etiquette:**
- Approach only people who seem relaxed and stationary
- Keep it under 2 minutes
- Accept "no" gracefully
- Note demographic patterns in responses

---

## Phase 5: Analysis Framework

### The Key Questions

After observation, answer:

1. **Where do people actually sit?**
   - Is it where the designers intended?
   - What makes those spots attractive?

2. **Where is the 100% corner?**
   - The spot with maximum activity and congregation
   - Is it supported or blocked by design?

3. **What's the sun pattern?**
   - Do sunny spots have seating?
   - Can people follow the sun (movable chairs)?

4. **Is there food?**
   - Within 100 feet?
   - Vendors? Carts? Adjacent restaurants?

5. **What's the street relationship?**
   - Can users see and be seen from the street?
   - Is the plaza elevated, sunken, or at grade?

6. **What do people avoid?**
   - Empty zones?
   - Uncomfortable seating?
   - Wind tunnels?

---

## Output Format

### Teaching Mode

```markdown
## Plaza Observation Methodology

### Purpose
[What this observation method reveals that assumptions miss]

### Observation Protocol
**When:** [Specific times and duration]
**What to count:** [Metrics appropriate to this space]
**What to map:** [Physical documentation needed]
**What to interview:** [Key questions for users]

### Analysis Questions
[The 6 key questions applied to this space type]

### Common Pitfalls to Avoid
[Mistakes observers often make]

### Expected Insights
[What properly conducted observation typically reveals]
```

### Diagnostic Mode

```markdown
## Plaza Observation Report: [Space Name]

### Observation Summary
**Date/Time:** [When observed]
**Duration:** [How long]
**Weather:** [Conditions]
**Peak count:** [People per square foot]

### Key Findings

#### What's Working
[Observed behaviors indicating success]
- [Finding with specific location/metric]
- [Finding with specific location/metric]

#### What's Failing
[Observed behaviors indicating problems]
- [Finding with specific location/metric]
- [Finding with specific location/metric]

### User Clusters
[Map or description of where activity concentrates]

### Empty Zones
[Map or description of avoided areas + hypotheses why]

### The Core Problem
[Single biggest finding, based on observation]

### Recommended Observations
[If more data needed, what specifically to track]

### Preliminary Hypotheses
[What might be tested with small interventions]
```

---

## Example Application

**Input:** "Our corporate campus plaza is dead at lunchtime. Can you help us understand why?"

**Output (abbreviated):**

## Plaza Observation Report: Corporate Campus Plaza

### Observation Summary
**Note:** This analysis is based on description only. The methodology below should be applied through actual observation.

### Observation Protocol Recommended

**When to observe:**
- Station observers at 11:30 AM weekday for 2 hours
- Repeat on 3 different days minimum

**What to count:**
- Total people every 15 minutes
- Sitters vs. passers-through
- Where specifically people sit (map it)

**What to map:**
- Sun pattern at noon
- Where seating is located relative to sun
- Paths people actually take vs. designed paths
- The 100% corner (if one exists)

### Preliminary Hypotheses to Test

Based on common corporate plaza failures:

1. **Food hypothesis:** Is there food within 100 feet? If not, there's no anchor for activity. Test: Add a coffee cart for one week and observe change.

2. **Sun hypothesis:** Where does sun fall at noon? Is there seating there? Test: Add movable chairs in sunny spots and count usage.

3. **Street edge hypothesis:** Is the plaza set back from the street? Elevated? If so, it lacks visual connection to passing life.

4. **Sittability hypothesis:** Measure ledges and benches:
   - Are ledges 30+ inches deep?
   - Are seats 16-17 inches high?
   - Are benches facing the action or facing walls?

### The Whyte Test

Before any redesign:
> "Spend a week watching. Count the people. Where do they sit? How long do they stay? Where do they look?"

The data will tell you what the plan missed.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Can't observe in person | Provide the protocol for client/team to execute; analyze their data |
| Limited observation time | Prioritize weekday lunch (11:30 AM-1:30 PM); single most revealing period |
| No baseline data | First observation becomes baseline; recommend second observation after any intervention |
| Space is completely empty | Empty itself is data; focus on WHY (sun, food, seating, connection) |
| Client wants design before observation | Emphasize that observation prevents costly mistakes; 1 week watching saves months of rebuilding |

---

## Integration

This skill is foundational for the **William Whyte** expert persona. It embodies the core principle: **observe what people actually do before designing what you think they should do.**

Use with:
- **triangulation-design** - Once observation reveals dead zones, this skill identifies social catalysts
- **sittable-space-audit** - When observation shows seating isn't used, this skill diagnoses why

---

## Success Criteria

A properly executed observation produces:
- [ ] Quantified people counts at multiple time intervals
- [ ] Map showing where people cluster and avoid
- [ ] Identification of the 100% corner (or its absence)
- [ ] Sun pattern documentation
- [ ] Food availability assessment
- [ ] Street relationship evaluation
- [ ] Specific, testable hypotheses for improvement
