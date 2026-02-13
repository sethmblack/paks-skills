---
name: human-scale-audit
description: Evaluate whether an urban environment was designed for human speed (5 km/hour walking) or machine speed (60 km/hour driving), identifying specific mismatches that create hostile pedestrian experiences.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.2322
repository: https://github.com/sethmblack/paks-skills
keywords:
- human-scale-audit
- urban-planning
---

# Human Scale Audit

Evaluate whether an urban environment was designed for human speed (5 km/hour walking) or machine speed (60 km/hour driving), identifying specific mismatches that create hostile pedestrian experiences. Based on Jan Gehl's speed/scale diagnostic methodology.

---

## Constitutional Constraints

- **Diagnostic, not dismissive** - The goal is to identify problems and possibilities, not to condemn car-oriented design
- **Evidence-based assessment** - Ground conclusions in observable features, not aesthetic preferences
- **Acknowledge context** - Some environments genuinely require car access; note trade-offs rather than demanding pure pedestrian priority
- **Human-centered framing** - The standard is human experience at walking pace, not architectural theory

---

## When to Use

- A street or area feels uncomfortable to walk in but you can't pinpoint why
- Diagnosing why a new development feels "dead" despite good intentions
- Evaluating a proposed street redesign for pedestrian experience
- Explaining to stakeholders why people avoid certain areas
- Identifying retrofit opportunities in car-oriented environments
- Building the case for human-scale interventions

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| environment_description | Yes | Description of the street, district, or space to audit |
| images | Recommended | Street-level photos showing the pedestrian experience |
| measurements | Helpful | Street widths, building setbacks, block lengths if known |
| context | Helpful | Purpose of the area, intended users, history |

---

## The Speed/Scale Diagnostic

### Core Principle

At 5 km/hour (walking pace), humans experience the world through all senses:
- We see fine details, read facial expressions, notice textures
- We hear conversations, music, nature sounds
- We smell food, flowers, pollution
- We feel temperature, wind, surfaces

At 60 km/hour (driving pace), humans can only perceive:
- Large shapes and bold colors
- Big signs with simple messages
- Gross spatial organization

**The Problem:** Much post-war urban design was created for the 60 km/hour experience while people must actually navigate it at 5 km/hour. This creates environments that are:
- Monotonous (nothing to engage the senses)
- Disorienting (landmarks too far apart)
- Uncomfortable (too exposed, too noisy)
- Hostile (prioritizing cars over pedestrians)

---

## Audit Process

### Step 1: Identify Design Speed

Examine the environment for clues about what speed it was designed for:

**Designed for 5 km/hour:**
- Frequent doorways (every 15-25 feet)
- Detailed facades with texture, relief, human-scale elements
- Small signs at eye level
- Narrow sidewalks feel adequate
- Street trees and street furniture create rhythm
- Ground floors engage pedestrians

**Designed for 60 km/hour:**
- Long blank walls (30+ feet without entrances)
- Monotonous facades with repetitive or no detail
- Large signs meant to be read from cars
- Wide setbacks with parking between building and sidewalk
- Few or no street trees
- Ground floors inactive (parking, service, blank)

### Step 2: Evaluate Key Dimensions

Score each dimension as Human Scale (H), Transitional (T), or Car Scale (C):

**Building Frontage:**
- H: Active ground floors, frequent doors, varied facades
- T: Some activity but long gaps between entrances
- C: Blank walls, parking garages, loading docks

**Signage Scale:**
- H: Small signs at eye level, subtle identification
- T: Mix of scales
- C: Large signs meant to be read at driving speed

**Street Proportions:**
- H: Buildings frame the street; feels enclosed
- T: Some enclosure but too wide in places
- C: Wide open; buildings far apart; no sense of "room"

**Setbacks:**
- H: Buildings at sidewalk edge
- T: Small setbacks with active use (cafe seating)
- C: Large setbacks with parking or empty landscaping

**Block Length:**
- H: Short blocks (200-400 feet) with frequent turns
- T: Medium blocks (400-600 feet)
- C: Long blocks (600+ feet) creating monotony

**Pedestrian Amenities:**
- H: Benches, trees, lighting at pedestrian scale
- T: Some amenities but sparse or poorly placed
- C: No amenities; pedestrians are afterthought

**Crossing Opportunities:**
- H: Frequent, short crossings with pedestrian priority
- T: Crossings exist but inconvenient or infrequent
- C: Long wait times, long crossing distances, pedestrian feels unwelcome

### Step 3: Identify Specific Mismatches

Where the environment was designed for one speed but is experienced at another:

- **"Drive-through architecture"** - Buildings with car-oriented features facing pedestrian sidewalks
- **Stranded pedestrians** - Sidewalks present but hostile (narrow, exposed, noisy, nothing to look at)
- **Missing rhythm** - Too much distance between points of interest
- **Scale intimidation** - Proportions that make humans feel small and exposed
- **Sensory deprivation** - Nothing to engage eyes, ears, or nose

### Step 4: Assess Impact on Experience

For each mismatch, describe the effect on someone walking:

- How does this make walking feel? (Tedious? Unsafe? Confusing?)
- What would a walker experience at this point?
- Why would someone choose to drive instead of walk?
- What is missing that would make this comfortable?

---

## Output Format

```markdown
## Human Scale Audit: [Location Name]

### Summary

**Dominant Design Speed:** [5 km/hr (Human) / 60 km/hr (Car) / Mixed]

**Pedestrian Comfort Level:** [High / Medium / Low / Hostile]

**Key Issue:** [One sentence summary of the primary mismatch]

---

### Design Speed Indicators

| Indicator | Observed Condition | Design Speed |
|-----------|-------------------|--------------|
| Building frontage | [description] | [H/T/C] |
| Signage scale | [description] | [H/T/C] |
| Street proportions | [description] | [H/T/C] |
| Setbacks | [description] | [H/T/C] |
| Block length | [description] | [H/T/C] |
| Pedestrian amenities | [description] | [H/T/C] |
| Crossing opportunities | [description] | [H/T/C] |

**Overall Pattern:** [X of 7 indicators at car scale]

---

### Specific Mismatches

**Mismatch 1: [Name]**
- Location: [Where in the environment]
- What's wrong: [The car-scale feature]
- Pedestrian impact: [How it feels to walk here]
- Severity: [High/Medium/Low]

**Mismatch 2: [Name]**
- Location: [Where]
- What's wrong: [Feature]
- Pedestrian impact: [Experience]
- Severity: [Level]

[Additional mismatches as relevant]

---

### The Walking Experience

**What a pedestrian encounters:**
[Narrative description walking through the space - what they see, hear, feel]

**Pain points:**
- [Specific moment 1]
- [Specific moment 2]
- [Specific moment 3]

**Why someone might choose not to walk here:**
[Summary of deterrents]

---

### Retrofit Opportunities

**Quick wins (low cost, high impact):**
- [Intervention 1]
- [Intervention 2]

**Medium-term improvements:**
- [Intervention 3]
- [Intervention 4]

**Structural changes (require major investment):**
- [Intervention 5]
- [Intervention 6]

---

### Conclusion

**Diagnosis:** [Summary of the speed/scale problem]

**Prognosis:** [How fixable is this? What would transformation require?]

**Gehl Principle:** "In the last 50 years, architects have forgotten what a good human scale is. For cities to be friendly to people, they must be built on a human scale - so that the experiences of the senses can be interesting."
```

---

## Constraints

- Focus on the pedestrian experience, not the driver experience
- Distinguish between car-oriented design and car-accessible design (they're different)
- Don't assume all car-scale design can or should be changed
- Identify the most impactful mismatches, not every minor issue
- Acknowledge trade-offs when relevant (delivery access, transit routes)

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Mixed-use environment with both scales | Identify which zones serve which function; note transitions |
| Historic car-oriented area | Acknowledge the era of construction; focus on retrofit possibilities |
| New construction that mimics old but fails | Identify "faux human scale" - surface details without functional engagement |
| Image quality insufficient | Note limitations; describe what can be observed, flag what needs verification |

---

## Example

**Input:** "Audit this suburban office park entrance. There's a wide road leading to several large office buildings set back behind parking lots. The sidewalk exists but nobody walks on it."

**Output:**

## Human Scale Audit: Suburban Office Park

### Summary

**Dominant Design Speed:** 60 km/hr (Car Scale)

**Pedestrian Comfort Level:** Hostile

**Key Issue:** This environment was designed entirely for the driving experience; pedestrian infrastructure exists only for code compliance, not actual use.

---

### Design Speed Indicators

| Indicator | Observed Condition | Design Speed |
|-----------|-------------------|--------------|
| Building frontage | Buildings set far back; lobbies only visible from parking | C |
| Signage scale | Large monument signs at entrance; building ID signs for cars | C |
| Street proportions | Wide road, no enclosure, buildings don't define the street | C |
| Setbacks | 100+ feet of parking between sidewalk and buildings | C |
| Block length | Single mega-block; no intersections within development | C |
| Pedestrian amenities | Minimal sidewalk, no seating, sparse landscaping | C |
| Crossing opportunities | Crosswalks at entry only; parking lot is no-man's-land | C |

**Overall Pattern:** 7 of 7 indicators at car scale. Complete car-oriented design.

---

### Specific Mismatches

**Mismatch 1: Stranded Sidewalk**
- Location: Along entrance road
- What's wrong: Sidewalk exists but leads nowhere useful; terminates at parking lot edge
- Pedestrian impact: A walker would reach the building perimeter then face a parking lot crossing with no marked path
- Severity: High

**Mismatch 2: Building Orientation**
- Location: Building entrances
- What's wrong: Main entrances face parking, not the street; service areas face pedestrian route
- Pedestrian impact: Walking to a building means approaching the "back" and navigating to find the entrance
- Severity: High

**Mismatch 3: Sensory Desert**
- Location: Entire corridor
- What's wrong: Nothing to engage senses - no retail, no ground floor activity, no street trees, no variety
- Pedestrian impact: Walking here is boring and feels endless; distances seem longer than they are
- Severity: High

---

### The Walking Experience

**What a pedestrian encounters:**

Starting from the public sidewalk, a walker would see a wide entrance road flanked by manicured but empty lawns. Large signs identify the office park but provide no wayfinding for pedestrians. The sidewalk is narrow, directly adjacent to moving traffic, with no buffer of trees or parked cars.

After several hundred feet, the sidewalk terminates at the edge of a parking lot. There are no marked pedestrian paths through the lot. The walker must navigate between parked cars, watching for backing vehicles, to reach a building entrance - which faces the parking lot, not the walking approach.

Along the way, there is nothing to see: no shop windows, no cafes, no public seating, no interesting facades. The buildings are set so far back that their architecture is barely perceptible. The experience is one of exposure, monotony, and feeling unwelcome.

**Pain points:**
- The sidewalk that leads nowhere (code compliance without function)
- The parking lot crossing (no pedestrian consideration)
- The sensory monotony (nothing to engage attention for several minutes of walking)
- The scale intimidation (buildings too far away, spaces too open)

**Why someone might choose not to walk here:**
Even for short trips within the park, driving feels safer and faster. The environment actively discourages walking.

---

### Retrofit Opportunities

**Quick wins (low cost, high impact):**
- Add shade trees along sidewalk to create buffer and rhythm
- Paint pedestrian paths through parking areas
- Add benches and wayfinding signage for pedestrians
- Ground floor tenants could add outdoor seating areas

**Medium-term improvements:**
- Convert some parking to pocket parks at building entries
- Add mixed-use (cafe, convenience, fitness) to ground floors
- Create internal pedestrian network connecting buildings
- Reduce road width to slow traffic and add pedestrian space

**Structural changes (require major investment):**
- Relocate parking to structures behind buildings
- Add new buildings at street edge to create enclosure
- Create true mixed-use with retail and residential
- Connect to surrounding neighborhood with bike/pedestrian paths

---

### Conclusion

**Diagnosis:** Classic suburban office park designed entirely for the car at 60 km/hour. Pedestrian infrastructure exists only on paper - it satisfies code but serves no actual function. The human scale is completely absent.

**Prognosis:** Transformation is possible but requires significant investment and likely changes to parking ratios. Incremental improvements (trees, paths, wayfinding) can help at margins, but fundamental change requires bringing buildings to the street and creating reasons to walk.

**Gehl Principle:** "When you do things for cars, cars come. When you do things for people, people come." This environment was built for cars, and unsurprisingly, only cars use it. The empty sidewalk is not a mystery - it's a predictable outcome of design that ignored human experience.

---

## Integration

This skill is part of the **Jan Gehl** expert persona. It diagnoses speed/scale mismatches that explain why environments feel hostile to pedestrians. It pairs with:

- **public-life-survey** - To document who is (or isn't) using the space
- **edge-quality-analysis** - To examine ground floor interfaces
- **12-quality-criteria** - For comprehensive space evaluation

The human scale audit explains WHY spaces fail; other skills document the failure and identify specific solutions.