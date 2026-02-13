---
name: public-space-assessment
description: Evaluate public spaces using behavioral observation methods pioneered by William H. Whyte.
license: MIT
metadata:
  version: 1.0.2331
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- public-space-assessment
- urban-planning
---

# Public Space Assessment (Whyte Method)

Evaluate public spaces using behavioral observation methods pioneered by William H. Whyte. Assess how people actually use spaces - where they sit, how they move, what makes them stay or leave - to diagnose why spaces succeed or fail and identify specific improvements.

---

## Constitutional Constraints

- **Evidence over opinion** - Base assessments on observed behavior, not aesthetic preferences
- **People-centered** - The measure of success is human use, not design awards
- **Specific recommendations** - Diagnoses must lead to actionable improvements
- **No elitism** - Good public space serves everyone, not just design professionals

---

## When to Use

- Evaluating an existing public space that feels "empty" or "dead"
- Diagnosing why a plaza, park, or waterfront isn't working
- Establishing baseline before redesign or renovation
- Comparing successful vs. unsuccessful spaces
- Understanding what makes particular spaces work

## Don't Use When

- Designing new spaces from scratch (use for inspiration, not as design tool)
- Evaluating private spaces not intended for public use
- Space is too new to have established usage patterns (wait 6+ months)
- Assessment is purely aesthetic rather than behavioral

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| space_description | Yes | Location, size, type (plaza, park, waterfront), surrounding context |
| observations | Recommended | What you've seen: user counts, behaviors, patterns, photos |
| time_of_observation | Recommended | Day, time, weather conditions when observed |
| design_elements | Optional | Seating, landscaping, edges, adjacent uses, sun exposure |
| comparison_spaces | Optional | Similar spaces that work better or worse |

---

## The Whyte Method Framework

William H. Whyte's research on public spaces revealed key principles:

### 1. Sit-ability Determines Success

**Key Questions:**
- How many places are there to sit?
- Are seats comfortable? (height 17-18 inches, with backs where possible)
- Do people have choices? (sun vs. shade, facing vs. back-to-crowd)
- Can people move seats to face each other?

**What to Look For:**
- People sitting on ledges, steps, planters (sign of insufficient seating)
- Empty benches while standing crowds nearby (seating in wrong location)
- People angling chairs toward sun, views, or activity

### 2. Edge Quality Matters

**Key Questions:**
- What happens at the edges where space meets buildings?
- Are there active ground-floor uses? (cafes, retail, entries)
- Are edges "sticky" (invite lingering) or "slippery" (encourage passing)?

**What to Look For:**
- Dead edges (blank walls, loading docks, parking)
- Active edges (outdoor seating, window shopping, people-watching spots)
- Edge usage patterns (people standing near edges vs. middle)

### 3. Sun, Wind, and Comfort

**Key Questions:**
- Where is sunny vs. shaded at different times?
- Is wind channeled uncomfortably through the space?
- Is there choice (can people find both sun and shade)?

**What to Look For:**
- People clustered in sunny spots even when seats are in shade
- Unused areas that are windy or uncomfortably exposed
- Seasonal variation (summer shade-seeking vs. winter sun-seeking)

### 4. Triangulation Creates Life

**Key Questions:**
- What external stimuli bring strangers into contact?
- Is there a focal point that encourages gathering? (performer, fountain, food cart)
- Do elements create social interaction?

**What to Look For:**
- People gathering around performers, vendors, or interesting objects
- Strangers in conversation (rare in dead spaces, common in good ones)
- Children playing (children are sensitive indicators of space quality)

### 5. Food and Activity

**Key Questions:**
- Is there food available? (vendors, cafes, restaurants)
- Is the space programmed with activities?
- Is there variety (things to do beyond sitting)?

**What to Look For:**
- Food carts or vendors drawing crowds
- People eating, even on uncomfortable surfaces
- Lunchtime peaks vs. evening deadness (or vice versa)

---

## Analysis Process

### Step 1: Baseline Count

Count users at multiple times:

| Time | Day | Weather | Total Users | Sitting | Standing | Walking Through | Dwell Time Est. |
|------|-----|---------|-------------|---------|----------|-----------------|-----------------|
| [Time] | [Day] | [Conditions] | [Count] | [Count] | [Count] | [Count] | [Avg minutes] |

**Benchmark:** A successful plaza should have 1+ person per 100 sq ft during peak periods.

### Step 2: Behavior Mapping

Sketch or describe:
- Where do people sit?
- Where do people stand and linger?
- Where do people walk?
- Where do people avoid?

### Step 3: Element Assessment

| Element | Status | Evidence | Recommendation |
|---------|--------|----------|----------------|
| **Seating** | [Working/Failing] | [Observed behavior] | [Specific fix] |
| **Edges** | [Active/Dead] | [Edge activities] | [Specific fix] |
| **Sun/Shade** | [Balanced/Problematic] | [Usage patterns] | [Specific fix] |
| **Food** | [Present/Absent] | [Vendor activity] | [Specific fix] |
| **Triangulation** | [Present/Absent] | [Social interaction] | [Specific fix] |
| **Sight Lines** | [Good/Poor] | [View blockages] | [Specific fix] |
| **Ground Plane** | [Quality/Issues] | [Surface condition] | [Specific fix] |

### Step 4: Diagnosis

Identify the root causes of success or failure:

**Primary Success Factors:**
- [What's working and why]

**Primary Failure Factors:**
- [What's failing and why]

### Step 5: Recommendations

Prioritize improvements by impact and feasibility:

| Priority | Recommendation | Impact | Feasibility | Notes |
|----------|----------------|--------|-------------|-------|
| 1 | [Specific action] | High/Med/Low | Easy/Moderate/Hard | [Explanation] |
| 2 | ... | | | |

---

## Output Format

```markdown
## Public Space Assessment: [Space Name]

### Summary

**Verdict:** [SUCCEEDING / STRUGGLING / FAILING]
**Primary Issue:** [One-sentence diagnosis]
**Quick Win:** [Highest-impact, easiest improvement]

### Space Description

[Location, size, context, surrounding uses]

### Observation Conditions

- **Date(s):** [When observed]
- **Times:** [Morning/midday/evening/weekend]
- **Weather:** [Conditions]
- **Observer:** [Who conducted assessment]

### Usage Analysis

**User Count:**
[Table of counts at different times]

**Behavior Patterns:**
- People tend to [behavior]
- Popular spots: [locations]
- Avoided areas: [locations]
- Dwell time: [estimate]

### Whyte Method Assessment

#### Sit-ability: [Score 1-5]
[Evidence and analysis]

#### Edge Quality: [Score 1-5]
[Evidence and analysis]

#### Sun/Shade/Comfort: [Score 1-5]
[Evidence and analysis]

#### Triangulation: [Score 1-5]
[Evidence and analysis]

#### Food/Activity: [Score 1-5]
[Evidence and analysis]

### Root Cause Diagnosis

**Why this space [succeeds/fails]:**
[Analysis connecting observations to design elements]

**Comparison to successful spaces:**
[What works elsewhere that's missing here]

### Recommendations

| Priority | Action | Why | How |
|----------|--------|-----|-----|
| 1 | [Action] | [Diagnosis it addresses] | [Implementation notes] |
| 2 | ... | | |
| 3 | ... | | |

### The Burden Test

*Would Amanda Burden want to spend time here?*

[Honest assessment applying the "would I want to be here?" standard]
```

---

## Example

**Input:** "Our city hall plaza is empty. It's a large paved space with some benches, a fountain, and a few trees. Even at lunch, hardly anyone uses it. What's wrong?"

**Output:**

## Public Space Assessment: City Hall Plaza

### Summary

**Verdict:** FAILING
**Primary Issue:** No edge activation and seating positioned for aesthetics, not use
**Quick Win:** Add movable chairs facing the fountain and permit a food vendor

### Space Description

Large civic plaza (~1 acre) between city hall and office buildings. Hard paved surface with geometric bench placement. Decorative fountain at center. Few trees providing limited shade. Surrounded by building entrances but no ground-floor retail or cafes.

### Observation Conditions

- **Date(s):** Tuesday, Thursday
- **Times:** 7:30am, 12:15pm, 5:30pm
- **Weather:** Clear, 72F
- **Observer:** Planning staff

### Usage Analysis

**User Count:**

| Time | Day | Weather | Total Users | Sitting | Standing | Walking Through | Dwell Time Est. |
|------|-----|---------|-------------|---------|----------|-----------------|-----------------|
| 7:30am | Tue | Clear | 12 | 0 | 2 | 10 | <1 min |
| 12:15pm | Tue | Clear | 45 | 8 | 15 | 22 | 5 min |
| 5:30pm | Thu | Clear | 18 | 2 | 4 | 12 | <2 min |

**Benchmark failure:** At ~43,000 sq ft, peak usage of 45 people = 0.1 persons/100 sq ft. Successful plazas achieve 1+ persons/100 sq ft. This plaza is operating at 10% of potential.

**Behavior Patterns:**
- People walking directly through, not lingering
- Office workers eating lunch on steps (avoiding benches)
- Smokers clustered at far edge near building entrance
- Children: zero observed

### Whyte Method Assessment

#### Sit-ability: 2/5

**Evidence:** 12 fixed benches arranged geometrically around fountain. Backless design. Positioned in full sun with no shade. Nobody observed using benches despite availability; lunch-eaters chose building steps instead.

**Diagnosis:** Benches are positioned for visual symmetry, not human comfort. No backs, no shade, and facing inward toward fountain rather than toward activity. People instinctively seek edges and views; these benches offer neither.

#### Edge Quality: 1/5

**Evidence:** All four edges are building walls with minimal activation. City hall entrance on north (occasional door traffic). Office building on south (blank lobby wall). East and west edges are windowless service areas.

**Diagnosis:** Dead edges kill plazas. There's no reason to linger at the edges, so people only pass through. A coffee cart on the corner would triple edge usage.

#### Sun/Shade/Comfort: 2/5

**Evidence:** Minimal tree canopy provides inadequate shade. At noon, entire plaza in full sun except narrow building shadow at east edge. Wind observed channeling through gap between buildings.

**Diagnosis:** No shade options during summer; space is uncomfortably hot. Wind channel makes spring and fall uncomfortable. People choosing steps over benches partly because steps offer building-shadow shade.

#### Triangulation: 2/5

**Evidence:** Fountain provides visual focal point but no auditory draw (not operating during observation). No performers, vendors, or interactive elements. No spontaneous gatherings observed.

**Diagnosis:** The fountain could be a triangulation element but isn't functioning as one. Nothing in the plaza draws strangers into contact or creates reasons to gather.

#### Food/Activity: 1/5

**Evidence:** No food vendors permitted. Nearest cafe is inside city hall (not visible or accessible from plaza). No programming observed.

**Diagnosis:** Food is the number one attractor of public space use. The complete absence of food explains the lunch-hour emptiness. Office workers are going elsewhere to eat.

### Root Cause Diagnosis

**Why this space fails:**

This plaza was designed as a visual amenity, not as a place for people. The design priorities were: symmetry, monumentality, and maintenance simplicity. None of these serve human use.

Specific failures:
1. **No food** - The single biggest predictor of plaza success is absent
2. **Dead edges** - Every edge discourages lingering
3. **Seating for symmetry** - Benches positioned decoratively, not functionally
4. **No shade choice** - Summer use impossible without shade options
5. **No triangulation** - Nothing draws people into gathering

**Comparison to successful spaces:**

The small parklet two blocks east has 3x the usage in 1/10 the space. It has: one food cart, movable chairs, a single tree providing shade, and faces an active retail frontage. Everything this plaza lacks.

### Recommendations

| Priority | Action | Why | How |
|----------|--------|-----|-----|
| 1 | Permit food vendor at SE corner | Food is #1 attractor; creates reason to linger | Issue vendor permit; designate location with utilities |
| 2 | Add 50 movable chairs | Let people choose where to sit | Purchase Fermob-style metal chairs; store in city hall overnight |
| 3 | Add shade structures/trees at south edge | Create usable summer space | Install shade sails or plant fast-growing trees |
| 4 | Activate fountain with sound | Create triangulation element | Repair fountain; add auditory component |
| 5 | Program weekly lunch concert | Draw crowds, build habit | Partner with local arts org; start with Fridays |

**Cost estimate:** Items 1-2 can be implemented for <$20,000 and would likely triple usage within 3 months.

### The Burden Test

*Would Amanda Burden want to spend time here?*

No. This plaza fails every test. There's nowhere comfortable to sit, nothing to eat, nothing to watch, and no shade. The design treats people as viewers of architecture rather than users of space. The good news: the problems are solvable. Add food, add movable seating, add shade - and this could become the civic gathering place it should be.

---

## Constraints

- Do not assess spaces without behavioral evidence (observations, counts, patterns)
- Do not confuse design quality with usage quality - beautiful spaces can fail
- Do not recommend removing features that people actually use, even if ugly
- Acknowledge when more observation time is needed for reliable diagnosis

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No usage data provided | Request observation data or note limitations of assessment without behavioral evidence |
| Space is new (<6 months) | Note that patterns may not be established; recommend reassessment |
| Conflicting observations | Note conflicts; recommend systematic observation at multiple times |
| Space success unclear | Use comparison method - what do successful nearby spaces have that this lacks? |

---

## Integration

This skill is part of the **Amanda Burden** expert persona. Use it when evaluating existing public spaces. It pairs well with:
- **coalition-building-playbook** for building support for improvements
- **detail-quality-review** for assessing specific design elements after diagnosis
- **rezoning-transformation-design** when space issues relate to surrounding land use