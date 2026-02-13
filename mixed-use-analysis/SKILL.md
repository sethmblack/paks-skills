---
name: mixed-use-analysis
description: 'Evaluate how the separation or combination of uses (residential, commercial, industrial, civic) affects street life and neighborhood vitality. Based on Jane Jacobs''s first generator of diversity: m...'
license: MIT
metadata:
  author: sethmblack
  version: 1.0.1457
keywords:
- mixed-use-analysis
- writing
---

# Mixed-Use Analysis

Evaluate how the separation or combination of uses (residential, commercial, industrial, civic) affects street life and neighborhood vitality. Based on Jane Jacobs's first generator of diversity: mixed primary uses.

---

## When to Use

- Evaluating zoning proposals
- Diagnosing dead or declining areas
- Understanding why some streets thrive
- Planning new developments
- Fighting single-use zoning

**Trigger Phrases:**
- "Should we zone this for residential only?"
- "Why is this area dead at night?"
- "The commercial district is struggling"
- "We need more vibrancy"
- "Should we allow mixed-use here?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| area | Yes | The neighborhood, district, or street to analyze |
| proposed_use | No | Any change being considered |
| time_patterns | No | When activity occurs |

---

## Core Principle

> "The district must serve more than one primary function; preferably more than two. These must insure the presence of people who go outdoors on different schedules and are in the place for different purposes, but who are able to use many facilities in common."
> — Jane Jacobs, *The Death and Life of Great American Cities*

**The Insight:** Single-use areas die when that use isn't active. Mixed-use areas support continuous activity because different uses bring people at different times for different reasons.

---

## Primary Uses Defined

Primary uses are the main reasons people come to an area:

| Use Type | Who It Brings | When |
|----------|---------------|------|
| Residential | Residents | Mornings, evenings, weekends |
| Office/Commercial | Workers | Weekdays 8-6 |
| Retail | Shoppers | Varies by type |
| Restaurants/Bars | Diners, drinkers | Lunch, evenings, late night |
| Entertainment | Visitors | Evenings, weekends |
| Industrial | Workers | Shifts vary |
| Civic (schools, libraries) | Students, citizens | Specific hours |
| Hotels | Guests | All hours |

---

## The Analysis Framework

### Step 1: Inventory Primary Uses

List every primary use in the area:
- What's there?
- How much of each?
- Where located?

### Step 2: Map Time Coverage

For each use, when are people present?

| Hour | Residents | Workers | Shoppers | Diners | Visitors |
|------|-----------|---------|----------|--------|----------|
| 6am  | ✓ | | | | |
| 9am  | ✓ | ✓ | | | |
| 12pm | ✓ | ✓ | ✓ | ✓ | |
| 3pm  | ✓ | ✓ | ✓ | | |
| 6pm  | ✓ | | ✓ | ✓ | |
| 9pm  | ✓ | | | ✓ | ✓ |
| 12am | ✓ | | | | ✓ |

### Step 3: Identify Dead Zones

Where are gaps?
- Financial districts at night
- Residential areas during workdays
- Industrial areas after shifts end
- Retail areas at night if no restaurants

### Step 4: Assess Cross-Support

Do uses support each other?
- Do residents use local shops?
- Do workers eat at local restaurants?
- Do visitors stay at local hotels?

Or are uses isolated?
- Workers drive in and out without stopping
- Residents shop elsewhere
- Visitors never leave the hotel

### Step 5: Evaluate Changes

For any proposed change:
- Does it add a missing use?
- Does it fill a time gap?
- Does it support existing uses?
- Or does it compete with/displace them?

---

## The Use Mix Scorecard

| Criterion | Poor | Fair | Good | Excellent |
|-----------|------|------|------|-----------|
| Number of primary uses | 1 | 2 | 3-4 | 5+ |
| Hours of coverage | 8 | 12 | 16 | 20+ |
| Cross-support | None | Weak | Moderate | Strong |
| Dead zones | Many | Some | Few | None |

---

## Common Patterns

### The Office Monoculture
- **Problem:** Only workers, only weekdays 8-6
- **Result:** Dead nights and weekends, struggling retail
- **Fix:** Add residential, evening entertainment

### The Residential Island
- **Problem:** Only residents, no commercial
- **Result:** Everyone drives elsewhere for everything
- **Fix:** Allow ground-floor retail, add civic uses

### The Suburban Strip
- **Problem:** Only retail, car-oriented, no residents
- **Result:** Dead at night, no street life
- **Fix:** Add residential above, reduce parking requirements

### The Healthy Mix
- **Example:** Greenwich Village
- **Uses:** Residents + retail + restaurants + offices + entertainment
- **Result:** Activity from 6am to 2am, seven days

---

## Workflow

### Step 1: Gather and Review Inputs

Collect all relevant information:
- Review the provided data and context
- Identify key parameters and constraints
- Clarify any ambiguities or missing information
- Establish success criteria

### Step 2: Analyze the Situation

Perform systematic analysis:
- Identify patterns and relationships
- Evaluate against established frameworks
- Consider multiple perspectives
- Document key findings

### Step 3: Generate Recommendations

Create actionable outputs:
- Synthesize insights from analysis
- Prioritize recommendations by impact
- Ensure recommendations are specific and measurable
- Consider implementation feasibility

## Outputs

| Output | Description |
|--------|-------------|
| Use inventory | What primary uses exist |
| Time coverage map | When each use brings people |
| Dead zone analysis | Where and when activity drops |
| Mix score | Overall assessment |
| Recommendations | What uses to add/change |

---



**Format:**
```markdown
## Analysis: [Topic]

### Key Findings
- [Finding 1]
- [Finding 2]
- [Finding 3]

### Recommendations
1. [Action 1]
2. [Action 2]
3. [Action 3]
```


## Additional Notes

**Best practices:**
- Use this skill when the situation clearly matches its intended use cases
- Combine with related skills for comprehensive analysis
- Iterate on outputs if initial results don't fully meet requirements

**Common variations:**
- Adjust the depth of analysis based on available time and information
- Scale the approach for different levels of complexity
- Adapt the output format to audience needs

**When to skip this skill:**
- The situation doesn't match the core use cases
- Simpler approaches would be more appropriate
- Time constraints require faster methods

## Example

**User:** "Our downtown is dead after 6pm. The business improvement district wants to add more parking. Will that help?"

**Mixed-Use Analysis response:**

More parking won't help. Here's why:

**Step 1: What are your primary uses?**
From your description, downtown is primarily:
- Offices (workers 8-6)
- Some retail (dependent on workers)
- Government/civic (8-5)

**Step 2: Map the time coverage**

| Time | Who's there |
|------|-------------|
| 6am-8am | Almost no one |
| 8am-12pm | Workers, some shoppers |
| 12pm-1pm | Workers at lunch |
| 1pm-5pm | Workers, fewer shoppers |
| 5pm-6pm | Workers leaving |
| 6pm-10pm | Almost no one |
| 10pm-6am | No one |

You have ~10 hours of activity, all the same people.

**Step 3: Identify the dead zone**

Your dead zone is 6pm-8am and weekends—that's 70% of the week.

**Step 4: Why parking won't help**

Parking makes it easier for workers to drive in and out. It doesn't add:
- Reasons to come after 6pm
- People who stay overnight
- Weekend activity

More parking = more car-oriented = less street life.

**Step 5: What would help**

Add residential:
- People who are there at night
- People who are there on weekends
- People who walk to existing shops

Add evening uses:
- Restaurants that serve dinner
- Entertainment venues
- Cultural facilities with evening programs

Allow existing buildings to add residential above:
- Office on lower floors
- Apartments above
- 24-hour presence

**The diagnosis:**

Your downtown is a single-use district pretending to be mixed-use. The solution isn't making it easier to come and go—it's giving people reasons to stay. That means residents and evening uses, not parking.

---

## Integration

This skill pairs with:
- **street-level-observation** - See the mix (or lack thereof) in person
- **eyes-on-the-street** - Mixed use creates natural surveillance
- **emergent-order-recognition** - Healthy mixes often emerge organically

---

## Constraints

- Some uses conflict (heavy industry + residential)
- Market conditions affect what's viable
- Existing zoning may prohibit mixing
- Building types may limit adaptability

---

## Source Expert

Jane Jacobs - `experts/jane-jacobs/`