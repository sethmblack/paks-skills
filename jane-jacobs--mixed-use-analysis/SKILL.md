---
name: jane-jacobs--mixed-use-analysis
description: Evaluate how the separation or combination of uses (residential, commercial, industrial, civic) affects street life and neighborhood vitality.
version: 1.0.0
author: AI-Personas
tags: [mixed-use-analysis, writing]
---

# Mixed-Use Analysis

Evaluate how the separation or combination of uses (residential, commercial, industrial, civic) affects street life and neighborhood vitality.

---

## When to Use

- Evaluating a zoning proposal or development plan
- Someone asks "Why is this area dead?" or "Why doesn't this work?"
- Analyzing whether to approve single-use vs. mixed-use projects
- Diagnosing a neighborhood that was "planned" but fails
- Comparing why one district thrives while a similar one languishes
- Any decision about separating or combining land uses
- When "highest and best use" arguments ignore diversity

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| area | Yes | The district, neighborhood, or development to analyze |
| proposed_uses | No | What is being proposed (for prospective analysis) |
| current_uses | No | What currently exists in the area |
| hours_observed | No | Activity patterns observed at different times |
| zoning_context | No | Current zoning restrictions or proposals |

---

## The Mixed-Use Framework

Jane Jacobs identified mixed primary uses as the first of her four generators of urban diversity. Single-use zoning—separating where we live, work, shop, and play—creates areas that die when their one purpose isn't active. Mixed uses create all-day vitality.

### Core Principles

**"Districts must serve more than one primary function; preferably more than two."** - The fundamental requirement for street life.

**"Diversity of uses creates diversity of users."** - Different uses bring different people at different times for different purposes.

**"The more successfully a city mingles everyday diversity of uses and users in its everyday streets, the more successfully, casually (and economically) its people thereby enliven and support well-located parks."** - Mixing enables everything else.

---

## The Analysis Process

### Step 1: Map Primary Uses

Identify what brings people to this area:

| Use Category | Examples | Typical Active Hours |
|--------------|----------|---------------------|
| Residential | Apartments, houses | Evenings, early mornings, weekends |
| Office | Professional services, government | 9 AM - 5 PM weekdays |
| Retail | Shops, restaurants, services | 10 AM - 9 PM, varies |
| Industrial/Maker | Manufacturing, workshops | Varies by industry |
| Civic | Libraries, schools, churches | Scheduled programming |
| Entertainment | Theaters, bars, venues | Evenings and weekends |

**Key Question:** "What primary functions bring people here, and when?"

### Step 2: Chart the Hours of Activity

Map when each use generates presence:

```
Hour    Residential  Office  Retail  Civic  Entertainment
6 AM    +++          -       -       -      -
9 AM    +            +++     +       ++     -
12 PM   +            +++     +++     ++     -
3 PM    ++           +++     ++      +++    -
6 PM    +++          -       ++      +      ++
9 PM    ++           -       +       -      +++
12 AM   +            -       -       -      +
```

**Key Question:** "Are there dead hours when no primary use is active?"

### Step 3: Identify Dead Zones and Dead Hours

Find the gaps:

- **Dead Zones:** Areas dominated by single uses that shut down
- **Dead Hours:** Times when no primary use generates activity
- **Dead Frontage:** Ground floors that don't engage the street (parking, blank walls)

**Key Question:** "When and where does life disappear?"

### Step 4: Assess Use Complementarity

Evaluate whether uses support each other:

- Do residential and office uses share lunch spots?
- Do evening uses keep streets alive after offices close?
- Do weekend uses activate weekday-only areas?
- Do different users create continuous presence?

**Key Question:** "Do uses hand off activity to each other through the day?"

### Step 5: Diagnose and Prescribe

Based on the analysis:

- What uses are missing?
- What hours need coverage?
- What would complement existing uses without competing?
- How can mixing be introduced without displacement?

**Key Question:** "What's needed to achieve all-hours activity?"

---

## Output Format

```markdown
## Mixed-Use Analysis

### Area Analyzed
[District, neighborhood, or development]

### Primary Uses Inventory

| Use | Presence | Hours Active | Coverage |
|-----|----------|--------------|----------|
| [Type] | [Strong/Moderate/Weak/Absent] | [Time range] | [% of area] |

### Activity Heat Map

| Hour | Mon-Fri | Sat-Sun | Primary Driver |
|------|---------|---------|----------------|
| 6-9 AM | [Level] | [Level] | [What use] |
| 9-12 PM | [Level] | [Level] | [What use] |
| 12-3 PM | [Level] | [Level] | [What use] |
| 3-6 PM | [Level] | [Level] | [What use] |
| 6-9 PM | [Level] | [Level] | [What use] |
| 9-12 AM | [Level] | [Level] | [What use] |

### Dead Zones and Dead Hours

**Dead Hours:** [Times when activity collapses]
**Dead Zones:** [Specific areas that die]
**Dead Frontage:** [Ground floors that don't engage]

### Use Complementarity Assessment

| Use Pair | Relationship | Gap/Opportunity |
|----------|--------------|-----------------|
| [Use A + Use B] | [Complement/Compete/Ignore] | [What's missing] |

### Diagnosis
[Why this area has the vitality it does—or doesn't]

### Prescriptions for Mixing

| Missing Use | Would Cover | Integration Strategy |
|-------------|-------------|---------------------|
| [What's needed] | [Hours/Days it would fill] | [How to add it] |
```

---

## Constraints

- **Mixing is not random.** Uses must complement, not just coexist
- **Primary uses matter most.** Secondary uses follow primaries
- **All-hours is the goal.** Partial coverage creates partial life
- **Ground floors are decisive.** Upper-floor mixing helps less than ground-floor mixing
- **Avoid false diversity.** Ten restaurants is single-use, not mixed-use
- **Proximity matters.** Uses must be close enough that users cross paths

---

## Example

**Input:** "We're planning a new transit-oriented development around our commuter rail station. The developer wants mostly residential with some ground-floor retail. Will this work?"

**Output:**

## Mixed-Use Analysis

### Area Analyzed
Proposed transit-oriented development, 12-acre site adjacent to commuter rail station

### Primary Uses Inventory (Proposed)

| Use | Presence | Hours Active | Coverage |
|-----|----------|--------------|----------|
| Residential | Strong | 6-9 AM, 6 PM-12 AM | 85% (floors 2-6) |
| Retail | Moderate | 10 AM - 8 PM | 10% (ground floor) |
| Office | Absent | N/A | 0% |
| Civic | Absent | N/A | 0% |
| Entertainment | Weak | Evening | 5% (one restaurant) |

### Activity Heat Map (Projected)

| Hour | Mon-Fri | Sat-Sun | Primary Driver |
|------|---------|---------|----------------|
| 6-9 AM | Medium | Low | Residents leaving for work |
| 9-12 PM | Low | Low | Retail shoppers (few) |
| 12-3 PM | Low | Medium | Retail, weekend residents |
| 3-6 PM | Low | Medium | Retail, residents returning |
| 6-9 PM | Medium | Medium | Residents home, restaurant |
| 9-12 AM | Low | Low | Residents only |

### Dead Zones and Dead Hours

**Dead Hours:** 9 AM - 5 PM weekdays. Residents commute out; retail alone cannot sustain activity.
**Dead Zones:** Interior courtyards face residential (no activation). Station plaza lacks programming.
**Dead Frontage:** Parking garage entrance dominates one full block face.

### Use Complementarity Assessment

| Use Pair | Relationship | Gap/Opportunity |
|----------|--------------|-----------------|
| Residential + Retail | Weak complement | Residents commute out; can't support daytime retail |
| Residential + Office | Missing | No daytime population to use retail, watch streets |
| Station + Development | Ignore | Commuters pass through, don't stay |
| Retail + Entertainment | Weak | One restaurant insufficient for evening destination |

### Diagnosis
This development repeats the classic TOD mistake: residential density without daytime activity. The 85% residential program means the site empties every weekday from 9-5 as residents commute OUT. The ground-floor retail will struggle without daytime customers. The station brings commuters who leave, not visitors who stay. By 10 AM on a Tuesday, this will feel like a ghost town despite its density.

### Prescriptions for Mixing

| Missing Use | Would Cover | Integration Strategy |
|-------------|-------------|---------------------|
| Office (15-20% of development) | 9 AM - 5 PM weekdays | Replace one residential building with office; workers support retail, provide eyes |
| Civic (library branch, community space) | Afternoons, weekends, evenings | Ground floor of residential building; programming draws diverse users |
| Childcare | 7 AM - 6 PM weekdays | Near station for drop-off; parents + staff add daytime presence |
| Maker/Workshop space | Varied hours | Affordable space in "aged" portion if any; different rhythm than office |

**Critical recommendation:** Reduce residential from 85% to 60%. Add 20% office, 10% civic, 10% ground-floor active uses. The station's commuters should arrive TO this place, not depart FROM it. A TOD that sends its residents away and receives no one in return is single-use development with a train.

---

## Integration

This skill is part of the **Jane Jacobs** expert persona. It applies Jacobs's first generator of diversity from *The Death and Life of Great American Cities*—the requirement for mixed primary uses.

For related analysis:
- Use **street-level-observation** to see what's actually happening now
- Use **eyes-on-the-street** to assess how mixing affects safety
- Use **emergent-order-recognition** to find self-organizing patterns in existing mixed areas
