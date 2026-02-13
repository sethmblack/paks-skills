---
name: center-analysis
description: Identify the centers that give a structure its life, map how they strengthen or weaken each other, and diagnose where center relationships need transformation.
license: MIT
metadata:
  version: 1.0.3093
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- center-analysis
- urban-planning
---

# Center Analysis

Identify the centers that give a structure its life, map how they strengthen or weaken each other, and diagnose where center relationships need transformation. Based on Christopher Alexander's theory of centers from *The Nature of Order*.

---

## Constitutional Constraints

Before applying this skill, verify:
- Analysis serves constructive design purposes
- Centers are understood as fields of organization, not geometric points
- The goal is understanding wholeness, not imposing mechanical structure
- Feeling guides the identification of centers; analysis illuminates feeling

---

## When to Use

- Diagnosing why a space, design, or system lacks coherence
- Understanding the structure beneath surface appearance
- Finding the strongest and weakest points in any configuration
- Planning transformations that strengthen rather than disrupt
- Comparing designs to understand which has stronger center structure
- Any situation where "What are the centers here?" would be valuable

---

## Don't Use When

- Simple functional analysis is sufficient
- The configuration is too small or simple for center analysis
- Quick impressionistic feedback is more appropriate
- User needs pattern identification rather than wholeness analysis

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| subject | Yes | The space, design, or configuration to analyze |
| boundary | No | What defines the system's limits |
| scale | No | What level of detail to analyze |
| known_issues | No | Problems the user has already identified |

---

## Understanding Centers

### What Is a Center?

A center is a region of space or configuration that has presence, coherence, and holds attention. Centers are not geometric points - they are fields of organization with fuzzy boundaries.

**Examples of centers:**
- A window that draws the eye
- A fireplace around which a room organizes
- A town square that anchors a neighborhood
- A doorway that mediates between spaces
- An empty courtyard that calms what surrounds it
- A button on a website that draws action

### How Centers Create Life

Life arises when centers support each other. A strong center:
- Has clear identity and presence
- Is supported by surrounding centers
- Supports the centers that surround it
- Belongs to a hierarchy of centers at different scales
- Intensifies the wholeness of the larger configuration

### How Centers Fail

Deadness arises when centers:
- Are weak (no presence, no attention-holding)
- Compete with each other (no clear hierarchy)
- Are isolated (don't connect to surrounding centers)
- Are missing at certain scales (scale gaps)
- Are in wrong relationship to context

---

## Analysis Process

### Step 1: Feel the Whole First

Before identifying individual centers:
- What is your overall sense of this configuration?
- Where does your attention naturally go?
- What feels organized? What feels chaotic?
- Where is there calm? Where is there tension?

This feeling is data. Analysis should illuminate it, not replace it.

### Step 2: Identify Centers at Each Scale

Working from large to small, identify centers at each scale level:

| Scale | What to Look For |
|-------|------------------|
| Largest | The configuration as a whole - is it a center in its context? |
| Major | The largest sub-regions with distinct identity |
| Intermediate | Significant elements that organize space around them |
| Detail | Small elements that hold attention |

For each center identified:
- Name it (descriptively)
- Note its relative strength (strong/moderate/weak)
- Note what gives it presence (or what weakens it)

### Step 3: Map Center Relationships

Centers don't exist in isolation. For each significant center:

**Support relationships:**
- Which centers support this one? (make it stronger)
- Which centers does this one support? (which does it strengthen)

**Competition relationships:**
- Does this center compete with other centers for attention?
- Is there confusion about which center dominates?

**Containment relationships:**
- Which larger centers contain this one?
- Which smaller centers does this one contain?

### Step 4: Find the Strongest Center

Every living configuration has a strongest center - the center that all other centers support and that gives the whole its unity.

**Questions:**
- Which center, if removed, would most damage the whole?
- Which center do all paths lead to?
- Which center gives the configuration its identity?

If there is no clear strongest center, this may be the root problem.

### Step 5: Identify Missing or Weak Centers

Look for:
- Scale gaps (missing intermediate sizes)
- Contested dominance (multiple centers fighting for primacy)
- Isolated centers (not connected to hierarchy)
- Misplaced centers (strong center in wrong location)
- Absent centers (where a center wants to be but isn't)

### Step 6: Diagnose the Center Structure

Synthesize findings into a diagnosis:
- Is the center hierarchy clear and coherent?
- Do centers mutually support each other?
- Is the strongest center truly at the heart?
- What transformations would strengthen the structure?

---

## Output Format

```markdown
## Center Analysis: [Subject]

### Initial Feeling

**Overall sense:** [What does the configuration feel like as a whole?]
**Attention patterns:** [Where does the eye/mind go naturally?]
**Organization vs. chaos:** [What feels structured? What feels random?]

### Centers Identified

#### Major Centers (Largest Scale)

| Center | Strength | Notes |
|--------|----------|-------|
| [Name] | Strong/Moderate/Weak | [What gives it presence or weakness] |

#### Intermediate Centers

| Center | Strength | Notes |
|--------|----------|-------|
| [Name] | Strong/Moderate/Weak | [What gives it presence or weakness] |

#### Detail Centers

| Center | Strength | Notes |
|--------|----------|-------|
| [Name] | Strong/Moderate/Weak | [What gives it presence or weakness] |

### Center Relationships

#### Support Network
```
[Visual or textual map showing which centers support which]
```

**Key support relationships:**
- [Center A] supports [Center B] by [how]
- [Center C] supports [Center D] by [how]

#### Competitions and Conflicts

- [Centers in competition and why]

#### Containment Hierarchy

```
[Nesting structure from largest to smallest]
```

### The Strongest Center

**Identified strongest center:** [Name]
**Why it's strongest:** [What gives it dominance]
**How others support it:** [The support network around it]

*If no clear strongest center exists:*
**Competing candidates:** [Centers fighting for primacy]
**Why hierarchy is unclear:** [Root cause of confusion]

### Missing, Weak, or Problematic Centers

| Issue | Location | Impact |
|-------|----------|--------|
| Scale gap | [Where] | [Effect on wholeness] |
| Weak center | [Which] | [What it fails to provide] |
| Contested center | [Which] | [The confusion it creates] |
| Misplaced center | [Which] | [Why it's in wrong location] |

### Diagnosis

**Center structure health:** [Overall assessment]
**Root cause of any deadness:** [Primary structural issue]
**What the configuration needs:** [Key transformations]

### Recommended Transformations

1. **[Transformation]:** [What center to strengthen and how]
2. **[Transformation]:** [What center to add or reposition]
3. **[Transformation]:** [What relationship to strengthen]

Order matters: strengthen from large to small, establishing context before detail.
```

---

## Example

**Input:** "Analyze the center structure of a living room that feels uncomfortable despite nice furniture. It's rectangular, with a large TV on one wall, a fireplace on another, a sliding door to a patio on a third wall, and the entrance from the hallway on the fourth."

**Output:**

## Center Analysis: Uncomfortable Living Room

### Initial Feeling

**Overall sense:** Contested, uncertain. The room doesn't know what it is.
**Attention patterns:** Eyes jump between TV, fireplace, and patio view - no rest.
**Organization vs. chaos:** Furniture is organized but the organization doesn't resolve the underlying confusion. The room is well-decorated chaos.

### Centers Identified

#### Major Centers (Largest Scale)

| Center | Strength | Notes |
|--------|----------|-------|
| The room itself | Moderate | Clear boundaries, good size, but internally confused |
| TV wall zone | Strong | Large TV dominates attention; furniture likely faces it |
| Fireplace wall zone | Strong | Traditional focal point; has architectural presence |
| Patio door zone | Strong | Natural light, view, connection to outdoors |

#### Intermediate Centers

| Center | Strength | Notes |
|--------|----------|-------|
| Seating group | Moderate | Organized but doesn't know what to orient to |
| Entrance threshold | Weak | Probably just a door, no transition space |
| Fireplace mantel | Moderate | Secondary center within fireplace zone |

#### Detail Centers

| Center | Strength | Notes |
|--------|----------|-------|
| Coffee table | Weak | Utility but not presence |
| Lamps | Unknown | Could be centers or mere fixtures |
| Art/objects | Unknown | Not described but potentially relevant |

### Center Relationships

#### Support Network

The problem: three strong centers (TV, fireplace, patio) that should support one center each compete for primacy. None clearly dominates.

**What should happen:**
- One major center dominates
- Other major centers become supporting, secondary
- Furniture creates hierarchy through orientation

**What actually happens:**
- Three centers of equal strength pull in different directions
- Furniture probably compromises, facing none fully
- The room has three personalities and can't commit to one

#### Competitions and Conflicts

- **TV vs. Fireplace:** Classic modern dilemma. Both claim the "gathering around" function. Neither wants to yield.
- **Patio vs. Interior:** The outdoor view competes with indoor focal points. Strong natural light can overpower interior centers.
- **Everything vs. Entrance:** The entrance is not integrated. It's a fourth wall that just happens to have a door.

#### Containment Hierarchy

```
Room (the whole)
├── TV zone (competing major center)
│   └── TV, entertainment equipment
├── Fireplace zone (competing major center)
│   └── Mantel, hearth
├── Patio zone (competing major center)
│   └── View, outdoor connection
├── Seating area (confused intermediate)
│   └── Sofa, chairs, table
└── Entrance (orphan)
    └── Door, threshold
```

The hierarchy is flat at the top. No center clearly contains the others.

### The Strongest Center

**Identified strongest center:** NONE - this is the problem.

**Competing candidates:**
- TV: Has technological dominance and probably the most wall space
- Fireplace: Has traditional authority and architectural permanence
- Patio: Has natural light and the power of the outdoors

**Why hierarchy is unclear:** Modern life put a TV in a room designed for a fireplace, and modern architecture added a glass wall to a room that needs interior focus. Each addition was reasonable; together they create chaos.

### Missing, Weak, or Problematic Centers

| Issue | Location | Impact |
|-------|----------|--------|
| No clear strongest center | Room level | No organizing principle for the whole |
| Weak entrance | Fourth wall | Arrival has no presence; you walk into confusion |
| Missing intermediate | Between major zones | No smaller centers that could mediate |
| Scale gap | Detail level | Unknown if detail centers exist to humanize |

### Diagnosis

**Center structure health:** Poor. The room has structure, but it's structure in conflict.

**Root cause of deadness:** Three equally strong centers compete for the "gathering around" function. The room cannot decide what kind of room it is: TV room? Hearth room? Sun room? It tries to be all three and fails at each.

**What the configuration needs:** A decision. One center must dominate; the others must support. The furniture arrangement must commit to this decision.

### Recommended Transformations

1. **Choose the strongest center.** This is a design decision, not an analysis finding. Options:
   - **Fireplace as center:** Traditional, warm, anchors the room to architecture. TV becomes secondary, perhaps in a cabinet. Patio becomes a light source, not a competitor.
   - **Patio view as center:** Modern, light-filled, connects to nature. Furniture orients to the view. Fireplace becomes a cozy secondary for cold nights. TV moves to another room or becomes very small.
   - **TV as center:** Modern reality. Accept it. Make the fireplace decorative/seasonal. Use the patio light but don't compete with it.

2. **Strengthen the entrance.** Whatever center dominates, create an entrance transition that prepares you for it. A threshold - a rug, a change in ceiling height, a partial screen - that says "you are arriving."

3. **Create supporting intermediate centers.** Once the main center is chosen:
   - A reading alcove that relates to the secondary center
   - A window seat that gives the patio presence without competition
   - Pools of light (lamps) that create intimate sub-spaces

4. **Let the furniture commit.** Arrange seating to face the chosen center fully, not in a compromise orientation. The body should know where to look.

The discomfort will resolve when the room decides what it is. The furniture is fine. The architecture is fine. The confusion is in the center structure - and that is a decision to make, not a problem to solve.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Subject too abstract | Request concrete description or boundaries |
| Too many centers to map | Focus on strongest and weakest; note where simplification occurred |
| User disagrees with center identification | Centers involve judgment; discuss and refine |
| No clear centers at all | This itself is a diagnosis - the configuration lacks organization |

---

## Integration

This skill is part of the **Christopher Alexander** expert persona. It operationalizes the theory of centers from *The Nature of Order* (2002-2004). Use it in conjunction with:

- **fifteen-properties-analysis** - for understanding WHY centers are strong or weak
- **pattern-language-application** - for finding patterns that strengthen center structure
- **unfolding-process-design** - for sequencing transformations that build center hierarchy

The fundamental insight: life arises not from individual centers but from centers supporting centers. The task is not to create impressive elements but to create mutual support among all elements at all scales.