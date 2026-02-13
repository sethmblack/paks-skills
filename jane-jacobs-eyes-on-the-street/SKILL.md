---
name: jane-jacobs-eyes-on-the-street
description: Analyze natural surveillance and street life as the primary source of urban safety, and design for conditions that create continuous watching.
version: 1.0.0
author: AI-Personas
repository: https://github.com/sethmblack/paks-skills
tags: [eyes-on-the-street, structure, writing]
---

# Eyes on the Street

Analyze natural surveillance and street life as the primary source of urban safety, and design for conditions that create continuous watching.

---

## When to Use

- Someone says "This area feels unsafe" or asks "How do we make it safer?"
- Evaluating a development proposal's impact on street safety
- Diagnosing why a place feels threatening despite police presence
- Analyzing why crime concentrates in certain locations
- Designing public spaces, streetscapes, or buildings
- When security solutions focus on policing rather than design
- Any situation requiring understanding of natural surveillance

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| location | Yes | The street, block, or area to analyze |
| safety_concerns | No | Specific incidents or perceptions of danger |
| current_design | No | Existing building configuration, streetscape |
| proposed_changes | No | Development plans or redesigns to evaluate |
| activity_patterns | No | Observed presence at different hours |

---

## The Eyes on the Street Theory

Jane Jacobs argued that urban safety comes primarily not from police but from natural surveillance—the continuous watching by shopkeepers, residents, and pedestrians who have reason to be present. Streets are safe when they're used, and they're used when design creates reasons to be there and watch.

### Core Principles

**"There must be eyes upon the street, eyes belonging to those we might call the natural proprietors of the street."** - Safety comes from watching, and watching comes from presence.

**"A well-used city street is apt to be a safe street. A deserted city street is apt to be unsafe."** - Use creates safety; emptiness invites danger.

**"The bedrock attribute of a successful city district is that a person must feel safe and secure on the sidewalk among all these strangers."** - Strangers aren't threatening when they're observed by other strangers.

---

## The Analysis Process

### Step 1: Inventory the Watchers

Identify who provides natural surveillance:

| Watcher Type | Example | Quality of Watching |
|--------------|---------|---------------------|
| Shopkeepers | Store owners with windows on street | Excellent—present for hours, invested |
| Residents | Apartments facing street | Good—present evenings/weekends, invested |
| Workers | Office buildings | Moderate—present business hours only |
| Pedestrians | Passers-by | Fair—momentary but continuous |
| Institutional | Schools, libraries | Variable—scheduled hours only |

**Key Question:** "Who is watching this street, for how long, and with what stake in its safety?"

### Step 2: Map the Sightlines

Assess what watchers can actually see:

- Do windows face the street or turn away?
- Are ground floors active (retail) or dead (parking, blank walls)?
- Do trees or structures block views?
- Is lighting adequate for night watching?
- Are there hiding spots invisible to watchers?

**Key Question:** "Can the watchers actually see what happens on this street?"

### Step 3: Chart Hours of Coverage

Map when eyes are present:

| Time | Who's Watching | Quality of Surveillance |
|------|----------------|------------------------|
| 6-9 AM | Early commuters, coffee shop | Sparse to moderate |
| 9-5 PM | Shopkeepers, office workers | Strong (if present) |
| 5-9 PM | Residents returning, diners | Moderate to strong |
| 9 PM-12 AM | Entertainment venues, late retail | Variable |
| 12-6 AM | Residents (from windows) | Weak—most sleeping |

**Key Question:** "When does surveillance fail? Are there dark hours?"

### Step 4: Identify Design Failures

Find what destroys eyes on the street:

| Design Element | Problem Created |
|----------------|-----------------|
| Blank walls | Nothing to see, no one watching |
| Surface parking lots | Dead zones, no presence |
| Set-back buildings | Distance from street, no engagement |
| Inward-facing buildings | Eyes turned away from public space |
| Single-use zoning | Nobody present for half the day |
| Superblocks | No through-traffic, no casual watchers |
| Fortress architecture | Walls, gates signal "stay away" |

**Key Question:** "What design choices have eliminated watchers or blocked their view?"

### Step 5: Design for Eyes

Prescribe changes that create surveillance:

- Ground-floor retail with windows
- Street-facing residential
- Active uses that span hours
- Continuous building frontage
- Lighting that supports watching
- Reasons to be present (benches, cafes, transit)

**Key Question:** "What would create continuous presence and clear sightlines?"

---

## Output Format

```markdown
## Eyes on the Street Analysis

### Location
[Street, block, or area analyzed]

### Watcher Inventory

| Watcher Type | Presence | Hours Active | Sight Quality | Stake |
|--------------|----------|--------------|---------------|-------|
| [Type] | [Strong/Moderate/Weak/None] | [Hours] | [Clear/Partial/Blocked] | [High/Medium/Low] |

### Surveillance Coverage Map

| Time Block | Coverage Level | Primary Watchers | Gaps |
|------------|----------------|------------------|------|
| [Time range] | [Strong/Moderate/Weak/None] | [Who] | [Vulnerabilities] |

### Design Assessment

| Element | Eyes Created/Destroyed | Impact |
|---------|----------------------|--------|
| [Feature] | [Creates eyes / Destroys eyes] | [Effect on safety] |

### Dark Spots and Dead Hours
**Physical dark spots:** [Locations without surveillance]
**Temporal dark spots:** [Hours without adequate watching]
**Structural blind spots:** [What design prevents watching]

### Diagnosis
[Why this place feels safe or unsafe—the eyes present or absent]

### Prescription for More Eyes

| Intervention | Eyes Created | Hours Covered |
|--------------|--------------|---------------|
| [Change] | [Who would watch] | [When] |
```

---

## Constraints

- **Eyes require presence.** You cannot design "passive surveillance" without people
- **Quality matters.** Cameras are not eyes; invested watchers are eyes
- **Continuity matters.** Six hours of watching and six dark hours still creates danger
- **Sightlines matter.** Present watchers who can't see accomplish nothing
- **Design precedes behavior.** People watch when design gives them reason and ability
- **Do not substitute policing for eyes.** Police patrol; communities watch

---

## Example

**Input:** "We have a new mixed-use development with a public plaza, but it's become a gathering spot for drug dealing. Security wants to install cameras and hire guards. Will this work?"

**Output:**

## Eyes on the Street Analysis

### Location
Central Plaza, mixed-use development (ground-floor retail, residential above, office building adjacent)

### Watcher Inventory

| Watcher Type | Presence | Hours Active | Sight Quality | Stake |
|--------------|----------|--------------|---------------|-------|
| Ground-floor retail | Weak | 10 AM - 6 PM | Blocked—storefronts face AWAY from plaza | Low—not their space |
| Residential (above) | Moderate | Evenings | Partial—4th floor and up, too high for detail | Medium |
| Office workers | Weak | 9-5 | Blocked—building has no windows on plaza side | None |
| Plaza users | None | N/A | N/A | None—no reason to linger |
| Pedestrians | Weak | Sporadic | Clear but momentary | Low |

### Surveillance Coverage Map

| Time Block | Coverage Level | Primary Watchers | Gaps |
|------------|----------------|------------------|------|
| 6-9 AM | None | Nobody | Plaza empty, retail closed |
| 9 AM-12 PM | Weak | Few pedestrians | Retail faces away, office has no view |
| 12-2 PM | Weak | Lunch pedestrians | Pass through, don't stay |
| 2-6 PM | None | Nobody | Worst period—office workers inside, retail ignores plaza |
| 6-9 PM | Weak | Residential (distant) | Too high up, no ground engagement |
| 9 PM-12 AM | None | Nobody | Dark, empty, invisible from residential |

### Design Assessment

| Element | Eyes Created/Destroyed | Impact |
|---------|----------------------|--------|
| Retail storefronts face interior corridor, not plaza | Destroys eyes | Shopkeepers watch indoors, not plaza |
| Office building has blank wall on plaza side | Destroys eyes | Hundreds of workers see nothing |
| Plaza has decorative boulders, raised planters | Destroys sightlines | Creates hiding spots, blocks views |
| No seating, no cafe, no vendor space | Destroys presence | No reason to linger, so no lingering |
| Plaza is "open" but has no activation | Destroys eyes | Empty space isn't watched space |

### Dark Spots and Dead Hours
**Physical dark spots:** Behind raised planters, in corner by office blank wall, entire perimeter at night
**Temporal dark spots:** 6-9 AM, 2-6 PM, 9 PM-6 AM (majority of hours)
**Structural blind spots:** Retail oriented away; office presents blank wall; residential too high to engage

### Diagnosis
This plaza fails because nobody watches it. The development's design systematically eliminated natural surveillance: retail faces a corridor instead of the plaza, the office presents a fortress wall, and residential is too elevated to engage. There are no reasons to be in the plaza (no seating, no food, no programming), so no legitimate users linger. Drug dealers moved into the vacuum because nobody else was there to claim the space. The plaza is public in name but unoccupied in practice.

**Cameras and guards will not work.** They address symptoms while the design continues to repel watchers. Guards cannot be present 24/7; cameras are not eyes—they observe after the fact but don't create the social presence that deters.

### Prescription for More Eyes

| Intervention | Eyes Created | Hours Covered |
|--------------|--------------|---------------|
| Reorient 2-3 retail spaces to open onto plaza with outdoor seating | Shopkeepers, customers | 10 AM - 9 PM |
| Add cafe/food kiosk in plaza center | Vendor, customers, staff | 7 AM - 10 PM |
| Install moveable seating (tables, chairs) | Lingering users | Daytime |
| Remove planters that block sightlines | All watchers | All hours |
| Negotiate with office for window cuts in blank wall, or mural with lighting | Workers (if windows), lighting reduces hiding | 9-5 (if windows) |
| Program plaza: farmers market, food trucks, music | Diverse users, vendors | Event hours |
| Add residential entrance from plaza side | Residents coming/going | Evenings, mornings |

**Critical principle:** The plaza needs people with reason to be there and ability to see it. Design brought this problem; design must solve it. Surveillance technology substitutes for the community watching that was designed out.

---

## Integration

This skill is part of the **Jane Jacobs** expert persona. It applies Jacobs's "eyes on the street" theory from *The Death and Life of Great American Cities*—the insight that urban safety comes from natural surveillance by people who are present and watching.

For related analysis:
- Use **street-level-observation** to see who is actually present and when
- Use **mixed-use-analysis** to understand how use mixing creates continuous presence
- Use **emergent-order-recognition** to find existing informal surveillance systems
