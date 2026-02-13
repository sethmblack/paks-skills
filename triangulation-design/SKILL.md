---
name: triangulation-design
description: Identify and design for triangulation—the external stimuli that bring strangers together and prompt social interaction.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.2344
repository: https://github.com/sethmblack/paks-skills
keywords:
- triangulation-design
- urban-planning
---

# Triangulation Design

Identify and design for triangulation—the external stimuli that bring strangers together and prompt social interaction. Based on William H. Whyte's research, this skill analyzes what social catalysts a space has, lacks, or could add to transform dead spaces into living ones.

---

## Constitutional Constraints

- **Inclusive design only** - Triangulation should bring people together, not exclude groups
- **Respect organic behavior** - Enhance natural social patterns, don't force artificial ones
- **No surveillance applications** - This methodology is for design, not monitoring
- **Authentic catalysts** - Recommend real social stimuli, not performative corporate installations

---

## When to Use

- Public space feels "dead" despite adequate design elements
- Observation reveals people don't interact or linger
- Need to activate an underused plaza, park, or public area
- Designing a new space and need to plan for social life
- Evaluating why one space feels vibrant and another doesn't
- Recommending small interventions to encourage social connection

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| space_description | Yes | The space to analyze for triangulation opportunities |
| current_features | No | Existing elements that might triangulate (or fail to) |
| constraints | No | Budget, regulations, or physical limitations |
| user_population | No | Who uses or should use this space |

---

## The Triangulation Principle

### Whyte's Definition

> "Triangulation is the process by which some external stimulus provides a linkage between people and prompts strangers to talk to other strangers as if they knew each other."

The stimulus is the third point of the triangle. Two strangers who would never speak become connected by their shared attention to something external—a performer, a view, an event.

### Why It Matters

Dead spaces aren't just uncomfortable—they're socially sterile. Even if people sit, they don't connect. Triangulation transforms passive coexistence into active social life.

---

## The Triangulator Inventory

### Tier 1: Proven Triangulators (High Impact)

These consistently create social linkage:

| Triangulator | Why It Works | Design Notes |
|--------------|--------------|--------------|
| **Street performers** | Active entertainment draws crowds; shared reactions prompt conversation | Designate performance-friendly zones with sight lines |
| **Food vendors/carts** | Creates mini-communities; waiting in line prompts interaction; eating together is social | Multiple vendors cluster activity; one vendor seeds, cluster follows |
| **Water features** | Mesmerizing and interactive; sound masks conversation (privacy); children play | Interactive fountains beat static pools; touchable beats look-only |
| **Dogs** | Universal social lubricant; "what breed?" is America's most common stranger-to-stranger opener | Off-leash hours or dog-friendly design; water bowls |
| **Public events** | Concerts, markets, screenings create instant community | Design for flexible event use; power access; flat areas |

### Tier 2: Strong Triangulators (Medium-High Impact)

| Triangulator | Why It Works | Design Notes |
|--------------|--------------|--------------|
| **Public art (interactive)** | Touchable, climbable, puzzling art prompts shared engagement | Interactive beats static; weird beats conventional |
| **Games and activities** | Chess tables, bocce courts, ping pong tables structure interaction | Public availability matters; can't be members-only feel |
| **Views** | Shared dramatic view creates common focus | Sunset positions; skyline angles; frame the view |
| **Children's play areas** | Parents talk while children play; the children are the triangulators | Seating with sightlines to play area; adjacent, not separate |
| **Gardens/plants** | Community gardens especially; tending creates conversation | Participation opportunities; not just looking |

### Tier 3: Moderate Triangulators (Supportive)

| Triangulator | Why It Works | Design Notes |
|--------------|--------------|--------------|
| **Bulletin boards** | Shared reading prompts "did you see...?" | Community-managed content; not corporate messaging |
| **Unusual objects** | A giant clock, a quirky statue, a mystery generates "what is that?" | The weirder, the more triangulating |
| **Seasonal elements** | Holiday decorations, ice rinks, summer fountains | Temporary but powerful; creates event feeling |
| **Transit hubs** | Shared waiting creates community | Design waiting areas for conversation, not isolation |

### Tier 4: Passive Elements (Low but Real)

| Triangulator | Why It Works | Design Notes |
|--------------|--------------|--------------|
| **Benches facing each other** | Structural encouragement for conversation | 90-degree or facing arrangements beat parallel |
| **Movable chairs** | Rearranging creates mini-negotiations; agency encourages engagement | Whyte's Luxembourg Garden model |
| **Shared tables** | Strangers at same table are pre-introduced | Large communal tables beat small isolated ones |

---

## Analysis Framework

### Step 1: Inventory Existing Triangulators

For the space in question, identify:

| Category | Present? | Active/Passive? | Effectiveness |
|----------|----------|-----------------|---------------|
| Performance space | | | |
| Food presence | | | |
| Water feature | | | |
| Interactive art | | | |
| Games/activities | | | |
| Natural catalysts (dogs, kids) | | | |
| Shared views | | | |
| Event capacity | | | |

### Step 2: Assess Triangulator Distribution

**Spatial questions:**
- Are triangulators clustered or scattered?
- Do they reinforce the 100% corner or compete with it?
- Are there triangulator "dead zones"?
- Can people see triangulators from street edge?

**Quality questions:**
- Are triangulators active (doing something) or passive (just existing)?
- Do they attract diverse groups or narrow demographics?
- Are they present consistently or only occasionally?

### Step 3: Identify Gaps

Common triangulation failures:

| Symptom | Likely Gap |
|---------|------------|
| People sit but don't interact | Missing active triangulators (performers, events) |
| Space empty despite good design | Missing anchor (food, water, activity) |
| Activity only in one spot | Triangulators not distributed |
| Teens avoid, only office workers | Narrow triangulator appeal |
| Lively weekdays, dead weekends | Missing weekend triangulators (corporate food closes) |

### Step 4: Design Interventions

For each gap, consider:

| Intervention Type | Examples | Reversibility |
|-------------------|----------|---------------|
| **Programmatic** | Schedule performers, markets, events | Fully reversible |
| **Vendor-based** | Add food carts, coffee kiosk | Easily reversible |
| **Furniture** | Movable chairs, game tables | Easily reversible |
| **Infrastructure** | Interactive fountain, play equipment | Semi-permanent |
| **Permanent** | Public art, amphitheater | Permanent |

**Whyte principle:** Start with reversible interventions. Test, observe, iterate.

---

## Output Format

```markdown
## Triangulation Analysis: [Space Name]

### Current Triangulator Inventory

| Triangulator Type | Present | Location | Effectiveness |
|-------------------|---------|----------|---------------|
| [Type] | [Yes/No/Partial] | [Where] | [High/Medium/Low/None] |

### Triangulation Strengths
[What's working to bring people together]

### Triangulation Gaps
[What's missing that would create social linkage]

| Gap | Impact | Evidence |
|-----|--------|----------|
| [Missing element] | [What it costs in social life] | [Observable symptom] |

### Recommended Interventions

#### Quick Wins (Reversible)
1. [Intervention] - [Expected effect]
2. [Intervention] - [Expected effect]

#### Medium-Term (Semi-Permanent)
1. [Intervention] - [Expected effect]

#### Long-Term (Permanent)
1. [Intervention] - [Expected effect]

### Triangulation Map
[Description or diagram showing where triangulators are and should be]

### Clustering Strategy
[How to position triangulators to reinforce each other and the 100% corner]

### Success Metrics
[How to measure if triangulation is working]
- [Metric 1]
- [Metric 2]
```

---

## Example Application

**Input:** "Our downtown plaza has food trucks and benches, but people eat quickly and leave. It doesn't feel like a community space."

**Output:**

## Triangulation Analysis: Downtown Plaza

### Current Triangulator Inventory

| Triangulator Type | Present | Location | Effectiveness |
|-------------------|---------|----------|---------------|
| Food vendors | Yes | North side | Medium - draws people but doesn't hold them |
| Seating | Yes | Scattered | Low - benches isolated, no conversation structure |
| Street performers | No | -- | None |
| Water feature | No | -- | None |
| Interactive art | No | -- | None |
| Games/activities | No | -- | None |
| Event space | Unclear | -- | Unknown |
| Views | Partial | South corner | Low - not leveraged |

### Triangulation Strengths

Food trucks are a proven anchor. People come for food. This is the seed—the question is why they don't stay.

### Triangulation Gaps

**Critical gap: No secondary triangulators.** Food draws people, but nothing holds them after they eat. The food trucks are triangulating with the eater (person + food = interaction), but not eaters with each other.

**Seating gap:** Scattered benches suggest "eat alone and leave." No structural encouragement to linger or interact.

**Activity gap:** No reason to stay once eating is done. No shared stimulus to triangulate strangers.

| Gap | Impact | Evidence |
|-----|--------|----------|
| No performance/event space | People have no reason to linger | Average dwell time likely <15 min |
| No seating clusters | No structural nudge toward conversation | People eat alone on separate benches |
| No secondary activity | Nothing to do after eating | People leave immediately |

### Recommended Interventions

#### Quick Wins (Reversible)

1. **Reconfigure seating around food truck zone** - Move benches into conversation clusters (facing pairs, L-shapes) near food truck area. Creates structural reason to sit together. Test: measure dwell time before/after.

2. **Add movable chairs** - 20-30 movable chairs near food truck zone. Let people arrange themselves. Creates agency and social negotiation. Cost: minimal.

3. **Schedule lunchtime performers** - One performer, 12-1 PM, 2-3 days per week. Position near food trucks to combine food + entertainment triangulation. Creates shared focus for lingering.

#### Medium-Term (Semi-Permanent)

1. **Add communal tables** - Long tables encourage strangers to sit together. Creates micro-community around shared surface. Position near food trucks.

2. **Install game tables** - Chess tables, cornhole, ping pong. Creates activity beyond eating. Different appeal than food = different lingering population.

3. **Create designated performance zone** - Flat area with power access, sight lines from seating. Signals "entertainment happens here" even when no performer present.

#### Long-Term (Permanent)

1. **Interactive water feature** - Splash pad or jet fountain. Creates children's attraction (parents linger while kids play). Adds sound, movement, and touchable element.

### Clustering Strategy

Food trucks are the anchor. All triangulation interventions should cluster within 50 feet of food zone:

```
[FOOD TRUCKS - North Edge]
         |
    [Performance Zone]
    [Communal Tables]
    [Movable Chairs]
         |
    [Game Tables]
         |
[Water Feature - South]
```

Each element reinforces the others. A person comes for food, sees the performer, decides to stay, sits in movable chair, watches water feature, talks to neighbor.

### Success Metrics

- **Dwell time increase:** Measure average stay before/after (target: 15 min → 45 min)
- **Return rate:** Survey "do you come here often?" (target: increase repeat users)
- **Interaction count:** Count visible conversations between strangers per hour
- **Peak occupancy:** Count people at 12:30 PM (should increase if people stay)
- **Weekend usage:** Does programming attract weekend visitors?

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Space has triangulators but they're not working | Check positioning, clustering, visibility from street; may be placed in dead zones |
| Budget prevents new installations | Focus on programmatic (events, performers) and furniture (movable chairs); cheap and reversible |
| Regulations restrict vendors/performers | Work within constraints; emphasize interactive art, games, furniture arrangement |
| Space is too small for variety | Pick one powerful triangulator appropriate to scale; don't scatter minimal resources |
| Corporate space with strict controls | Recommend lunchtime programming, art, and furniture that fits corporate aesthetic |

---

## Integration

This skill is part of the **William Whyte** expert persona. Use it when observation reveals social sterility—people present but not connecting.

Use with:
- **plaza-observation-method** - First observe to identify where triangulation is missing
- **sittable-space-audit** - Ensure seating supports triangulation (facing, clustering, depth)

---

## Success Criteria

Effective triangulation design produces:
- [ ] Complete inventory of existing triangulators
- [ ] Identification of specific gaps with evidence
- [ ] Interventions organized by reversibility/commitment
- [ ] Clustering strategy that reinforces natural patterns
- [ ] Measurable success metrics for evaluation