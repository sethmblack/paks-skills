---
name: public-life-survey
description: Conduct systematic observation and counting of human activity in public spaces using Jan Gehl's methodology. Establish baselines, measure activity levels, and categorize behaviors to provide an evidence base for urban design decisions.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.2330
repository: https://github.com/sethmblack/paks-skills
keywords:
- public-life-survey
- urban-planning
---

# Public Life Survey

Conduct systematic observation and counting of human activity in public spaces using Jan Gehl's methodology. Establish baselines, measure activity levels, and categorize behaviors to provide an evidence base for urban design decisions.

---

## Constitutional Constraints

- **Evidence-based only** - All conclusions must be grounded in observed or described data; do not speculate beyond what can be seen or measured
- **Non-judgmental observation** - Document what people actually do, not what you think they should do
- **Human dignity** - Observe public behavior respectfully; the goal is understanding, not surveillance
- **Acknowledge limitations** - When working from descriptions or images rather than direct observation, clearly state the limitations of the analysis

---

## When to Use

- Assessing a public space before redesign
- Establishing baseline data for future comparison
- Evaluating the success of an intervention
- Understanding why a space "works" or "doesn't work"
- Building evidence-based cases for urban transformation
- Comparing activity across different times, seasons, or locations

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| space_description | Yes | Description of the public space (location, type, size, surrounding context) |
| images | Recommended | Photos, plans, or satellite imagery of the space |
| time_context | Recommended | Time of day, day of week, season, weather conditions |
| specific_questions | No | Particular aspects to focus on (seating use, pedestrian flow, etc.) |
| comparison_baseline | No | Previous data to compare against |

---

## Survey Framework

### Step 1: Define the Observation Area

Clearly delineate the boundaries of the space being studied:
- Physical edges (buildings, streets, barriers)
- Logical boundaries (the "room" of the space)
- Entry and exit points

**Output:** Clear definition of study area with boundaries marked.

### Step 2: Count the Activity

**Flow Counts (Moving):**
- Number of pedestrians passing through
- Direction of movement
- Speed of movement (hurrying vs strolling)

**Stay Counts (Stationary):**
- Number of people staying (more than ~2 minutes)
- Duration of stay (short: 2-10 min, medium: 10-30 min, long: 30+ min)
- Location within space (edges, center, specific features)

**Activity Breakdown:**
- Walking through (necessary movement)
- Standing (waiting, observing, meeting)
- Sitting (on benches, steps, grass, cafe seating)
- Talking (in groups of 2+)
- Playing (children, sports, informal games)
- Other activities (eating, reading, working, performing)

### Step 3: Categorize Activities

Apply Gehl's three-category framework:

**Necessary Activities:**
- Walking to destination
- Waiting for transit
- Required errands
- *These happen regardless of space quality*

**Optional Activities:**
- Sitting to enjoy the space
- Lingering at a viewpoint
- Eating lunch outdoors
- *These indicate space quality*

**Social Activities:**
- Conversations between strangers
- Children playing together
- Public performances gathering crowds
- *These indicate space success*

**Key Metric:** The ratio of optional+social to necessary activities indicates quality. A space with mostly necessary activities is functioning as a corridor. A space with high optional/social activity is functioning as a destination.

### Step 4: Map Activity Locations

Document where activities occur:
- **Clustering patterns** - Where do people gather?
- **Edge use vs. center use** - Do people gravitate to edges?
- **Feature use** - Which benches, steps, or areas are used?
- **Avoided areas** - Where does no one go?
- **Movement patterns** - What paths do people take?

### Step 5: Note Environmental Factors

Document conditions that influence activity:
- Sun/shade patterns
- Wind exposure
- Noise levels
- Air quality
- Temperature/weather
- Time of day/week
- Seasonal factors

### Step 6: Synthesize Findings

Combine counts, categories, and locations into insights:
- What is this space primarily used for?
- What opportunities exist but are not being used?
- What barriers prevent optional/social activity?
- How does this compare to baseline or expectations?

---

## Output Format

```markdown
## Public Life Survey: [Space Name]

### Study Parameters

**Location:** [Address/description]
**Study Area:** [Boundaries defined]
**Observation Context:** [Time, day, season, weather]
**Methodology:** [Direct observation / analysis from images / described conditions]

---

### Activity Counts

| Category | Count | Notes |
|----------|-------|-------|
| **Flow (Moving)** | | |
| Pedestrians through | [number] | [direction, pace] |
| Cyclists | [number] | |
| **Staying (Stationary)** | | |
| Standing | [number] | [locations, duration] |
| Sitting | [number] | [where: benches, steps, ground, cafes] |
| Talking | [number of groups] | [sizes] |
| Playing/Active | [number] | [activities] |
| Other | [number] | [specify] |

**Total Staying:** [number]
**Stay Duration:** [short/medium/long distribution]

---

### Activity Classification

| Type | Count | % | Observations |
|------|-------|---|--------------|
| Necessary | [n] | [%] | [examples] |
| Optional | [n] | [%] | [examples] |
| Social | [n] | [%] | [examples] |

**Quality Indicator:** [High/Medium/Low optional+social activity]

---

### Spatial Distribution

**High Activity Zones:**
- [Location 1]: [What's happening, why this spot]
- [Location 2]: [What's happening, why this spot]

**Low Activity Zones:**
- [Location 1]: [Why avoided]
- [Location 2]: [Why avoided]

**Edge vs. Center Pattern:**
[Description of where people position themselves]

---

### Environmental Observations

| Factor | Condition | Impact on Activity |
|--------|-----------|-------------------|
| Sun/Shade | [description] | [impact] |
| Wind | [description] | [impact] |
| Noise | [description] | [impact] |
| Seating | [description] | [usage pattern] |

---

### Key Findings

1. [Primary observation about how the space is used]
2. [Secondary observation about activity patterns]
3. [Tertiary observation about missed opportunities or problems]

### Implications

**What's working:**
- [Positive finding 1]
- [Positive finding 2]

**What's not working:**
- [Problem finding 1]
- [Problem finding 2]

**Questions for further study:**
- [Unanswered question 1]
- [Unanswered question 2]
```

---

## Constraints

- Do not prescribe solutions in the survey phase - this is observation, not design
- Acknowledge when data is estimated from images rather than directly counted
- Note time-specific limitations (a noon survey doesn't capture evening use)
- Distinguish between what is observed and what is inferred
- Be specific with numbers where possible; use ranges when uncertain

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Only images available, no direct observation | Conduct "image-based analysis" - estimate visible counts, note limitations clearly |
| Space appears completely empty | This is valuable data - document what conditions are present, hypothesize why abandoned |
| Space is crowded beyond counting | Use sampling methods - count a section, extrapolate; note methodology |
| Weather/time significantly affects activity | Document conditions, note that repeat observations in different conditions would be valuable |

---

## Example

**Input:** "Assess this downtown plaza. It's a concrete square about 50x50 meters between two office buildings. There are four benches in the center. It's a Tuesday at noon."

**Output:**

## Public Life Survey: Downtown Office Plaza

### Study Parameters

**Location:** Downtown between two office buildings
**Study Area:** ~50x50 meter concrete plaza, bounded by buildings on two sides, streets on two sides
**Observation Context:** Tuesday noon (weekday lunch hour - peak potential for office worker activity)
**Methodology:** Analysis from description; direct observation recommended for verification

---

### Activity Counts

| Category | Count (Estimated) | Notes |
|----------|-------------------|-------|
| **Flow (Moving)** | | |
| Pedestrians through | ~150/hour | Likely crossing pattern between streets |
| Cyclists | 5-10/hour | Probably avoiding plaza |
| **Staying (Stationary)** | | |
| Standing | 5-10 | Near building entrances, smoking |
| Sitting | 4-8 | Four benches, likely partial use |
| Talking | 2-4 groups | Small groups, brief interactions |
| Playing/Active | 0 | No facilities, no children likely at this hour |
| Other (eating) | 5-10 | Lunch hour - but likely few, see analysis |

**Total Staying:** 15-25 estimated
**Stay Duration:** Predominantly short (smoke breaks, quick lunch)

---

### Activity Classification

| Type | Count | % | Observations |
|------|-------|---|--------------|
| Necessary | ~150 | 85% | Pedestrians crossing to destinations |
| Optional | ~15 | 8% | Sitting on benches, standing in sun |
| Social | ~10 | 7% | Small groups talking |

**Quality Indicator:** LOW optional+social activity
This space is functioning as a corridor, not a destination.

---

### Spatial Distribution

**High Activity Zones:**
- Building entrances: Smokers, people waiting
- If sunny side exists: Likely concentration of bench users there

**Low Activity Zones:**
- Center of plaza: Exposed, no reason to stop
- Shaded areas: Likely avoided in cooler weather
- Any bench in full wind exposure

**Edge vs. Center Pattern:**
Classic underperforming plaza pattern: activity hugs the edges (building entrances, smoker zones) while the center remains empty. Benches in the center are psychologically exposed - people prefer edges.

---

### Environmental Observations

| Factor | Condition | Impact on Activity |
|--------|-----------|-------------------|
| Sun/Shade | Unknown, likely harsh at noon | May drive people to edges or away entirely |
| Wind | Likely channeled between buildings | Reduces comfort, shortens stay duration |
| Noise | Traffic from two streets | Conversations difficult |
| Seating | 4 benches in center | Poor placement - exposed, not facing activity |

---

### Key Findings

1. **The plaza functions as passage, not place.** High through-traffic, low staying activity. People cross but do not linger.

2. **Center benches are underutilized.** Four benches for a 2,500 sq meter space is inadequate, and center placement violates edge-seeking behavior.

3. **Missing: soft edges.** Ground floors of adjacent buildings likely offer nothing (lobbies, parking) - no cafes, shops, or activity to anchor the space.

4. **Missing: microclimate control.** Noon sun, wind channeling, and traffic noise create hostile conditions for optional activity.

### Implications

**What's working:**
- Space exists and is accessible
- Some pedestrian flow (potential audience for better space)
- Lunch hour provides potential user base

**What's not working:**
- No reasons to stay beyond necessity
- Seating placement discourages use
- Environmental conditions are uncomfortable
- Ground floors are likely inactive

**Questions for further study:**
- What are the ground floor uses? (Confirm hard vs soft edges)
- What is activity like in morning, evening, weekend?
- What is the microclimate - wind patterns, sun tracking?

---

## Integration

This skill is part of the **Jan Gehl** expert persona. It provides the observation and data collection phase that precedes design recommendations. It pairs with:

- **human-scale-audit** - For evaluating the speed/scale design of the space
- **edge-quality-analysis** - For examining ground floor interfaces
- **12-quality-criteria** - For comprehensive evaluation

The public life survey establishes the evidence base. Other skills provide diagnosis and recommendations.