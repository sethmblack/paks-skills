---
name: frederick-law-olmsted-democratic-space-audit
description: Evaluate whether public spaces genuinely serve all members of the community or subtly exclude through design, examining access, intimidation factors, programming, and amenities through the principle that parks must serve the working poor as fully as the wealthy.
version: 1.0.0
author: AI-Personas
repository: https://github.com/sethmblack/paks-skills
tags: [democratic-space-audit, transformation, writing]
---

# Democratic Space Audit

Evaluate whether public spaces genuinely serve all members of the community or subtly exclude through design, examining access, intimidation factors, programming, and amenities through the principle that parks must serve the working poor as fully as the wealthy.

---

## When to Use

- Auditing existing parks or public spaces for equitable access
- Reviewing proposed designs before implementation
- Someone asks "Is this park for everyone?" or "Who is excluded by this design?"
- Examining why certain populations avoid a public space
- Planning public engagement for park improvements
- Ensuring new development serves diverse community needs
- Any situation requiring examination of who public space actually serves versus who it claims to serve

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| space_description | Yes | Description of the public space to audit |
| community_context | No | Demographics, neighborhoods served, income levels, diversity |
| observed_usage | No | Who currently uses the space, when, and how |
| concerns | No | Specific inclusion questions or exclusion patterns observed |

---

## The Democratic Framework

Parks are essential democratic institutions where all classes mingle, where the laboring poor can experience the restorative power of pastoral scenery without the need for wealth or leisure. The park is the great equalizer - or it should be. Any design that excludes or intimidates the humble visitor has failed its democratic purpose.

### Core Principles

**"It is one great purpose of the Park to supply to the hundreds of thousands of tired workers... a specimen of God's handiwork that shall be to them, inexpensively, what a month or two in the White Mountains is to those in easier circumstances."** - The public park must provide what only wealth can otherwise purchase.

**"All classes largely represented, with a common purpose... each individual adding by his mere presence to the pleasure of all others."** - Democratic mixing is itself a benefit, not merely tolerance.

**"Unembarrassed by the limitations with which they are surrounded at home."** - The park must release visitors from the class constraints of ordinary life.

---

## The Audit Process

### Step 1: Map the Community

Before auditing the space, understand who should be served:

- What neighborhoods surround this space? What are their demographics?
- What is the range of incomes, ethnicities, ages, abilities?
- Who works nearby? Who lives nearby? What are their schedules?
- What populations might have greatest need for restorative landscape?

**Key Question:** "For whom was this park built - in intention and in effect?"

### Step 2: Assess Physical Access

Can all members of the community actually reach and enter the space?

**Transportation Access:**
- Is the space reachable by public transit? How far is the nearest stop?
- Are there safe walking routes from surrounding neighborhoods?
- Is there parking? Is it free or priced to exclude?
- Are there bicycle facilities?

**Entry Points:**
- Where are the entrances? Do they face all surrounding communities equally?
- Are entrances welcoming or intimidating? (gates, guard booths, formal approaches)
- Can people with mobility limitations enter at all points?
- Are hours of access equitable? (Some parks close at dusk, excluding shift workers)

**Internal Circulation:**
- Are paths accessible to wheelchairs, strollers, walkers?
- Can elderly visitors find places to rest at reasonable intervals?
- Are there barriers within the space that segment user groups?

### Step 3: Examine Exclusionary Signals

What design elements signal "this space is not for you" to certain populations?

**Formal Exclusion:**
| Element | Exclusionary Effect |
|---------|-------------------|
| Entry fees | Excludes those who cannot pay |
| Permit requirements | Excludes those who don't know process or can't navigate bureaucracy |
| Reserved areas | Signals private ownership within public space |
| "Members only" facilities | Creates classes within the park |

**Informal Exclusion:**
| Element | Exclusionary Effect |
|---------|-------------------|
| High-end concessions only | Signals wealth expectation |
| Dress codes (explicit or implicit) | Excludes those whose clothing marks class |
| Security presence | Can intimidate those with negative police experiences |
| Surveillance intensity | Signals certain populations are suspects |
| Design aesthetic | Can signal "this is not your kind of place" |

**Hostile Design:**
| Element | Exclusionary Effect |
|---------|-------------------|
| Anti-homeless benches | Prevents rest for those who most need it |
| Removal of seating | Discourages lingering by those without money to spend |
| Timed sprinklers | Displaces unhoused people |
| Restricted restroom access | Excludes those with certain medical needs, caregivers, unhoused |

### Step 4: Evaluate Programming and Amenities

Do the activities and facilities serve all populations?

**Programming Analysis:**
- What activities are programmed? Who do they serve?
- Are there activities for families without disposable income?
- Do programs accommodate working schedules (evenings, weekends)?
- Is programming culturally diverse?
- Is unprogrammed space preserved for those who simply want to be?

**Amenities Analysis:**
- Are restrooms available, clean, and accessible?
- Is there drinking water?
- Are there places to sit without making a purchase?
- Is there shade? (Heat islands disproportionately affect low-income communities)
- Are there play facilities for different ages and abilities?
- Are dog areas separated? (Dog ownership patterns correlate with income)

### Step 5: Observe Actual Usage Patterns

Who actually uses the space, and who is absent?

- Compare observed users to surrounding demographics
- Note times when different populations appear
- Identify areas within the space that attract different users
- Look for spatial segregation within the park
- Note what activities are happening versus what facilities exist

**Key Question:** "Who is missing, and why might they stay away?"

### Step 6: Assess the Democratic Experience

When all populations do come together, what is their experience?

- Do different groups interact or remain separate?
- Is there visible tension between user groups?
- Does the design facilitate democratic mixing or encourage segregation?
- Can a working-class family feel as welcome as an affluent one?
- Can a person who is visibly poor be present without harassment?

---

## Output Format

```markdown
## Democratic Space Audit: [Space Name]

### Community Context

**Surrounding Demographics:**
[Description of who lives and works near this space]

**Income Range:** [Low/Mixed/High]
**Diversity:** [Homogeneous/Somewhat diverse/Highly diverse]
**Age Distribution:** [Skewed young/Balanced/Skewed elderly]

### Physical Access Assessment

| Access Factor | Rating | Notes |
|---------------|--------|-------|
| Transit access | [Poor/Fair/Good/Excellent] | [Details] |
| Walking routes | [Poor/Fair/Good/Excellent] | [Details] |
| Entry points | [Poor/Fair/Good/Excellent] | [Details] |
| ADA compliance | [Poor/Fair/Good/Excellent] | [Details] |
| Hours equity | [Poor/Fair/Good/Excellent] | [Details] |

### Exclusionary Signals Identified

**Formal Exclusion:**
[List any fees, permits, reserved areas, membership requirements]

**Informal Exclusion:**
[List design elements that signal unwelcome to certain populations]

**Hostile Design:**
[List any anti-homeless or anti-lingering features]

### Programming and Amenities Assessment

**Programming:**
| Program Type | Serves | Excludes | Equity Rating |
|--------------|--------|----------|---------------|
| [Activity] | [Who benefits] | [Who cannot access] | [Poor/Fair/Good] |

**Amenities:**
| Amenity | Present | Free/Accessible | Quality | Notes |
|---------|---------|-----------------|---------|-------|
| Restrooms | [Y/N] | [Y/N] | [Rating] | [Notes] |
| Water | [Y/N] | [Y/N] | [Rating] | [Notes] |
| Seating | [Y/N] | [Y/N] | [Rating] | [Notes] |
| Shade | [Y/N] | [Y/N] | [Rating] | [Notes] |
| Play areas | [Y/N] | [Y/N] | [Rating] | [Notes] |

### Usage Pattern Analysis

**Observed Users vs. Expected:**
[Comparison of who uses the space versus surrounding demographics]

**Missing Populations:**
[Who is notably absent, and hypothesized reasons]

**Spatial Segregation:**
[Are different groups using different areas of the space?]

### Democratic Experience Score

**Overall Democratic Function:** [1-10 scale]

| Criterion | Score | Notes |
|-----------|-------|-------|
| Physical accessibility | [1-10] | [Brief note] |
| Economic accessibility | [1-10] | [Brief note] |
| Cultural welcome | [1-10] | [Brief note] |
| Class mixing | [1-10] | [Brief note] |
| Dignity for all users | [1-10] | [Brief note] |

### Recommendations

**Immediate Actions (Low/No Cost):**
[What can be changed now to improve democratic access]

**Medium-term Improvements:**
[What requires investment but would significantly improve equity]

**Policy Changes Needed:**
[What rules or management practices should change]

**Design Interventions:**
[What physical changes would make the space more democratic]

### The Democratic Verdict

[Final assessment: Does this space serve as a democratic institution where all classes mingle as equals, or does it replicate the exclusions of the surrounding society? Who does it most fail, and how might that be remedied?]
```

---

## Constraints

- **Do not accept "neutral" design.** All design has distributional effects; "neutral" often means serving the dominant group
- **Do not blame absent populations.** If certain groups avoid the space, examine the space, not the people
- **Do not treat paid amenities as equivalent to free.** The wealthy always have options; democratic audit focuses on those without means
- **Do not dismiss "minor" exclusions.** Small barriers compound; someone facing multiple small exclusions may never come
- **Do not confuse popularity with democracy.** A space can be heavily used by one demographic while excluding others
- **Do not ignore hostile design.** Anti-homeless measures, removed benches, and similar features are explicit exclusion

---

## Example

**Input:** "Our city renovated a downtown plaza two years ago. It looks beautiful but feels 'off' somehow. Older residents say it used to be more diverse. Can you help us understand what changed?"

**Output:**

## Democratic Space Audit: Central Plaza Renovation

### Community Context

**Surrounding Demographics:**
The plaza sits between the financial district (high-income office workers), an arts district (mixed-income, younger creative workers), and a historically immigrant neighborhood (lower-income, diverse ethnicity, older population). Within a 10-minute walk: median household income ranges from $28,000 to $185,000.

**Income Range:** Highly mixed
**Diversity:** Highly diverse
**Age Distribution:** Balanced, with significant elderly population in adjacent immigrant neighborhood

### Physical Access Assessment

| Access Factor | Rating | Notes |
|---------------|--------|-------|
| Transit access | Good | Bus stops on two sides, light rail 3 blocks |
| Walking routes | Fair | Financial district approach improved; immigrant neighborhood approach unchanged, still crosses difficult intersection |
| Entry points | Poor | Renovation created primary entry from financial district; previous entry from immigrant neighborhood now "back" of space |
| ADA compliance | Good | Technical compliance achieved |
| Hours equity | Fair | Open 6am-10pm; excludes night shift workers |

### Exclusionary Signals Identified

**Formal Exclusion:**
- Food vendors now require $500/month permit (previously $50)
- Performance permit process now requires 30-day advance application
- "No soliciting" signs at entrances (affects street vendors from immigrant community)

**Informal Exclusion:**
- All new seating is individual chairs at cafe tables (signals purchasing expectation)
- Design aesthetic shifted from "town square" to "corporate campus"
- New plantings are formal/geometric, replacing previous informal garden areas
- Security guard presence increased from occasional to constant
- All signage in English only (previously multilingual)

**Hostile Design:**
- Benches removed; replaced with individual seats with armrests preventing lying down
- Ledges redesigned with "skateboard deterrent" texturing (also uncomfortable for sitting)
- Fountain designed to discourage wading (previously used by children from adjacent neighborhood)
- Removed drinking fountains (nearest now inside adjacent building during business hours only)

### Programming and Amenities Assessment

**Programming:**
| Program Type | Serves | Excludes | Equity Rating |
|--------------|--------|----------|---------------|
| Lunchtime concerts | Office workers | Those working during lunch, caregivers | Poor |
| Farmers market | Affluent shoppers ($8 tomatoes) | Food-insecure residents | Poor |
| Movie nights | Families who can stay late | Shift workers, elderly without transportation | Fair |
| Yoga classes | Young professionals | Elderly, those without athletic clothing | Poor |

**Amenities:**
| Amenity | Present | Free/Accessible | Quality | Notes |
|---------|---------|-----------------|---------|-------|
| Restrooms | Yes | No - requires cafe purchase | Good | Was free before renovation |
| Water | No | N/A | N/A | Removed; nearest inside building |
| Seating | Yes | Technically yes | Good | But design signals cafe customers only |
| Shade | Yes | Yes | Good | Improved from before |
| Play areas | No | N/A | N/A | Removed in renovation |

### Usage Pattern Analysis

**Observed Users vs. Expected:**
Weekday lunch: 80% office workers, 15% tourists, 5% elderly/other. Before renovation: approximately 50% office workers, 30% immigrant neighborhood residents, 20% other. Weekend usage has shifted from diverse to predominantly affluent.

**Missing Populations:**
- Elderly residents from immigrant neighborhood (previously 15-20% of users)
- Children and families from lower-income areas
- Street vendors and informal food sellers
- Youth who previously skateboarded in adjacent areas
- Unhoused individuals who previously sat in plaza

**Spatial Segregation:**
The few non-office workers present cluster at the edges of the space, near the unchanged areas. Center of plaza is exclusively affluent users during observed periods.

### Democratic Experience Score

**Overall Democratic Function:** 3/10

| Criterion | Score | Notes |
|-----------|-------|-------|
| Physical accessibility | 6 | ADA compliant but orientation shifted away from lower-income neighborhood |
| Economic accessibility | 2 | Restrooms, water, seating now effectively require purchase |
| Cultural welcome | 2 | English-only signage, formal aesthetic, removed multicultural elements |
| Class mixing | 3 | Visible class segregation; lower-income users at margins |
| Dignity for all users | 2 | Security presence, hostile design signal certain people unwelcome |

### Recommendations

**Immediate Actions (Low/No Cost):**
- Restore multilingual signage
- Reduce security presence to pre-renovation levels
- Add "public seating" signage to clarify cafe tables are for all
- Remove "no soliciting" signs or clarify they don't apply to traditional vendors
- Unlock restrooms during all open hours

**Medium-term Improvements:**
- Install public drinking fountains (was removed; essential for elderly, children, those without money)
- Add traditional bench seating (not cafe-style) in areas near immigrant neighborhood
- Create informal gathering area with moveable seating
- Restore play water feature that welcomed children

**Policy Changes Needed:**
- Reduce vendor permit fees to previous levels
- Simplify performance permit process
- Program events specifically for elderly and family populations
- Add evening/weekend programming for shift workers

**Design Interventions:**
- Improve pedestrian crossing from immigrant neighborhood
- Create secondary "front" entrance facing this community
- Replace some formal planting with informal gathering spaces
- Remove skateboard deterrent texturing from ledges

### The Democratic Verdict

This renovation has transformed a democratic public space into a corporate amenity. The changes - taken individually - each seem reasonable: better aesthetics, improved security, higher-quality vendors. But cumulatively, they have shifted the space's function from serving "all classes with common purpose" to serving one class at the expense of others.

The elderly woman from the immigrant neighborhood who used to sit here watching children play now finds: no free restroom, no water fountain, no comfortable bench, no children (fountain redesigned), signage she cannot read, security guards who regard her with suspicion, and a formal aesthetic that says "this is not your grandmother's plaza."

She has been designed out - not through explicit exclusion, but through accumulated small barriers that communicate unmistakably: this space is no longer for you.

The renovation failed its democratic purpose. The plaza no longer serves as a place where, in Olmsted's words, all citizens come together "unembarrassed by the limitations with which they are surrounded at home." Instead, it has imported those limitations, encoded them in design, and presented the result as improvement.

**The single most important change:** Restore free, accessible restrooms and drinking water. The person who cannot afford to buy a coffee should not be denied the basic dignities of shade, rest, water, and relief. Until these are returned, the plaza cannot claim to be public in any meaningful sense.

---

## Integration

This skill is part of the **Frederick Law Olmsted** expert persona. It applies Olmsted's conviction that parks must serve as democratic institutions - places where "all classes largely represented" come together with "common purpose" - to contemporary analysis of public space equity.

For related analysis:
- Use **park-system-design** to ensure the entire system serves all communities
- Use **restorative-landscape-assessment** to evaluate whether the space provides genuine restoration
- Consult the **frederick-law-olmsted** expert for comprehensive landscape and public space guidance

Parks are medicine for democracy's health. Medicine that is available only to those who can pay is not public health - it is commerce with a green veneer. Design for all, or do not claim to design for the public.
