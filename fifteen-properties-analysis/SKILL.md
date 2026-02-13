---
name: fifteen-properties-analysis
description: Systematically evaluate any configuration using Christopher Alexander's fifteen fundamental properties of wholeness from The Nature of Order.
license: MIT
metadata:
  version: 1.0.4001
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- fifteen-properties-analysis
- urban-planning
---

# Fifteen Properties Analysis

Systematically evaluate any configuration using Christopher Alexander's fifteen fundamental properties of wholeness from *The Nature of Order*. These properties describe the structural features that give things life.

---

## Constitutional Constraints

Before applying this skill, verify:
- Analysis serves constructive purposes (understanding, improving, creating)
- The fifteen properties are used as diagnostic lenses, not rigid rules
- Feeling and observation guide analysis, not mechanical scoring
- The goal is increasing life and wholeness, not achieving arbitrary metrics

---

## When to Use

- Diagnosing why a space, design, or system feels "dead" or "alive"
- Evaluating design proposals against principles of living structure
- Understanding what makes traditional or vernacular designs work
- Teaching others to see the properties that create life
- Comparing alternatives to determine which has more life
- Any situation where "Why does this feel dead/alive?" would be valuable

---

## Don't Use When

- Quick impressionistic feedback is more appropriate
- The user needs functional analysis only (does it work?)
- The context is purely technical with no human experience dimension
- Analysis would be pedantic or overkill for the situation

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| subject | Yes | The design, space, or configuration to analyze |
| comparison | No | Alternative design to compare against |
| focus_properties | No | Specific properties to emphasize |
| context | No | Surrounding environment or constraints |

---

## The Fifteen Properties

### 1. Levels of Scale
Centers exist at multiple scales, with geometric ratios between adjacent levels (roughly 2:1 to 3:1). Empty scale gaps create deadness.

**Signs of life:** Continuous hierarchy from large to small, each scale populated
**Signs of deadness:** Missing intermediate scales, jumps from very large to very small

### 2. Strong Centers
Some regions function as centers - they have presence, hold attention. Centers are fields of organization, not geometric points.

**Signs of life:** Clear focal points that draw the eye and anchor attention
**Signs of deadness:** No center dominates; attention wanders aimlessly

### 3. Boundaries
Living structures have boundaries that are zones, not lines. Boundaries belong to both inside and outside.

**Signs of life:** Thick boundaries with presence, transitional zones
**Signs of deadness:** Sharp edges, thin lines, no transition

### 4. Alternating Repetition
Elements repeat but alternate - ABAB rather than AAAA. Rhythm and variation within unity.

**Signs of life:** Pattern with variation, rhythm that breathes
**Signs of deadness:** Monotonous repetition or complete randomness

### 5. Positive Space
Every space is positive - shaped, convex, useful. No leftover space.

**Signs of life:** All spaces are figures, not grounds; every area has presence
**Signs of deadness:** Leftover spaces, negative shapes, areas that feel accidental

### 6. Good Shape
Centers have shapes that are themselves strong - lobed, notched, arrow-like.

**Signs of life:** Shapes with character, distinct and memorable
**Signs of deadness:** Amorphous blobs, shapes without identity

### 7. Local Symmetries
Symmetry occurs locally (within each center) rather than globally. Perfect global symmetry often deadens.

**Signs of life:** Each part has its own balance; asymmetry at large scale
**Signs of deadness:** Rigid global symmetry imposed on everything

### 8. Deep Interlock and Ambiguity
Centers hook into each other. Boundaries are ambiguous; elements belong to multiple centers.

**Signs of life:** Parts are woven together; unclear where one ends and another begins
**Signs of deadness:** Parts are isolated; clear separation everywhere

### 9. Contrast
Living structures have contrast: light/dark, solid/void, ornate/plain.

**Signs of life:** Strong differentiation, drama, visual tension
**Signs of deadness:** Everything at same level, no differentiation

### 10. Gradients
Properties change gradually across space. No abrupt jumps.

**Signs of life:** Smooth transitions, gradual changes
**Signs of deadness:** Sudden shifts, jarring transitions

### 11. Roughness
Living structures are slightly irregular - not mechanical perfection.

**Signs of life:** Handmade quality, small irregularities
**Signs of deadness:** Machine-perfect uniformity, sterile precision

### 12. Echoes
Similar shapes, angles, or motifs repeat throughout, creating family resemblance.

**Signs of life:** Elements relate to each other, family likeness
**Signs of deadness:** Every element different, no underlying unity

### 13. The Void
At the heart of living structure is a zone of stillness - empty center that anchors activity.

**Signs of life:** Central calm, emptiness that holds meaning
**Signs of deadness:** Everything filled, no rest for the eye, or chaotic center

### 14. Simplicity and Inner Calm
No unnecessary complexity. Everything present is necessary.

**Signs of life:** Elegant simplicity, nothing extraneous
**Signs of deadness:** Cluttered, busy, or stripped to blankness

### 15. Not-Separateness
Living structures belong to their context - extensions of what is already there.

**Signs of life:** Seamless connection to surroundings, belonging
**Signs of deadness:** Object dropped in, alien to context

---

## Analysis Process

### Step 1: Initial Feeling

Before analyzing, feel:
- What is your immediate sense of this place/thing?
- Does it feel alive or dead? Where on the spectrum?
- What draws you? What repels you?

Record this feeling as baseline. Analysis should illuminate, not replace, felt sense.

### Step 2: Property-by-Property Evaluation

For each of the fifteen properties, assess:

| Rating | Meaning |
|--------|---------|
| **Strong** | Property clearly present and contributing to life |
| **Moderate** | Property partially present or unevenly implemented |
| **Weak** | Property barely present or working against life |
| **Absent** | Property missing entirely |

Note specific evidence for each rating.

### Step 3: Identify Strongest Properties

Which 3-5 properties are most alive in this configuration? These are strengths to preserve and build from.

### Step 4: Identify Weakest Properties

Which 3-5 properties are most lacking? These are opportunities for improvement. Note which weak properties cause the most damage to overall life.

### Step 5: Find Property Interactions

Properties interact. Strong properties can compensate for weak ones; weak properties can undermine strong ones.

**Questions:**
- Which weak properties prevent strong ones from fully working?
- Which property, if strengthened, would unlock others?
- Are any properties in tension with each other?

### Step 6: Synthesis

Combine analysis into overall assessment:
- Where is life strongest?
- Where is it weakest?
- What are the root causes of deadness?
- What would most increase life?

---

## Output Format

```markdown
## Fifteen Properties Analysis: [Subject]

### Initial Feeling

**First impression:** [Immediate felt sense]
**Life/death spectrum:** [Where does this fall?]
**What draws attention:** [Positive attractors]
**What creates unease:** [Negative elements]

### Property Evaluation

| # | Property | Rating | Evidence |
|---|----------|--------|----------|
| 1 | Levels of Scale | [Rating] | [Specific observations] |
| 2 | Strong Centers | [Rating] | [Specific observations] |
| 3 | Boundaries | [Rating] | [Specific observations] |
| 4 | Alternating Repetition | [Rating] | [Specific observations] |
| 5 | Positive Space | [Rating] | [Specific observations] |
| 6 | Good Shape | [Rating] | [Specific observations] |
| 7 | Local Symmetries | [Rating] | [Specific observations] |
| 8 | Deep Interlock | [Rating] | [Specific observations] |
| 9 | Contrast | [Rating] | [Specific observations] |
| 10 | Gradients | [Rating] | [Specific observations] |
| 11 | Roughness | [Rating] | [Specific observations] |
| 12 | Echoes | [Rating] | [Specific observations] |
| 13 | The Void | [Rating] | [Specific observations] |
| 14 | Simplicity | [Rating] | [Specific observations] |
| 15 | Not-Separateness | [Rating] | [Specific observations] |

### Strongest Properties

1. **[Property]:** [Why it's strong and how it contributes to life]
2. **[Property]:** [Why it's strong and how it contributes to life]
3. **[Property]:** [Why it's strong and how it contributes to life]

### Weakest Properties

1. **[Property]:** [Why it's weak and how it reduces life]
2. **[Property]:** [Why it's weak and how it reduces life]
3. **[Property]:** [Why it's weak and how it reduces life]

### Property Interactions

**Reinforcing strengths:** [How strong properties support each other]
**Compounding weaknesses:** [How weak properties undermine each other]
**Key leverage point:** [Which property, if strengthened, would unlock most improvement]

### Synthesis

**Where life is strongest:** [Summary]
**Where life is weakest:** [Summary]
**Root cause of deadness:** [If applicable]
**Highest-impact improvement:** [What would most increase life]

### Return to Feeling

Does the analysis illuminate the initial feeling? [Reflection on whether analytical findings explain felt sense]
```

---

## Example

**Input:** "Analyze this hotel lobby: large open space with marble floors, modern furniture in geometric arrangements, uniform recessed lighting, floor-to-ceiling windows on one wall, a single large reception desk in the center."

**Output:**

## Fifteen Properties Analysis: Hotel Lobby

### Initial Feeling

**First impression:** Impressive but cold. I admire it but don't want to linger.
**Life/death spectrum:** More toward dead. Respects, but doesn't invite.
**What draws attention:** The scale, the windows, the clean lines.
**What creates unease:** Nowhere comfortable to wait. Exposed. Echoey.

### Property Evaluation

| # | Property | Rating | Evidence |
|---|----------|--------|----------|
| 1 | Levels of Scale | Weak | Large space, furniture, then nothing. Missing middle scales. |
| 2 | Strong Centers | Moderate | Reception desk is a center, but competes with window wall. |
| 3 | Boundaries | Weak | Hard edges everywhere. No transitional zones. |
| 4 | Alternating Repetition | Weak | Furniture in identical arrangements. Monotonous. |
| 5 | Positive Space | Weak | Furniture groupings feel like islands in vast emptiness. |
| 6 | Good Shape | Moderate | Overall room shape is clear. Furniture shapes generic. |
| 7 | Local Symmetries | Weak | Rigid global symmetry dominates. No local variety. |
| 8 | Deep Interlock | Absent | Everything separated. Elements don't hook into each other. |
| 9 | Contrast | Strong | Marble/glass contrast works. Light/shadow through windows. |
| 10 | Gradients | Absent | Uniform lighting. Abrupt transition at entrance. |
| 11 | Roughness | Absent | Perfectly machined. Sterile. No human touch. |
| 12 | Echoes | Weak | Geometric theme repeats but mechanically. |
| 13 | The Void | Strong | Central open space has presence. Could be stronger. |
| 14 | Simplicity | Moderate | Clean but perhaps too bare. Simplicity without warmth. |
| 15 | Not-Separateness | Weak | Generic international style. Could be anywhere. |

### Strongest Properties

1. **Contrast (9):** The marble/glass material contrast creates visual interest. The window wall brings strong light that creates shadow play. This is the source of whatever life the space has.

2. **The Void (13):** The large central open space does function as a void - it creates the feeling of arrival, of importance. But it's so large it becomes intimidating rather than centering.

3. **Good Shape (6):** The room's overall proportions are well-considered. There's architectural competence here.

### Weakest Properties

1. **Levels of Scale (1):** This is the core problem. The space jumps from monumental (the room) to human (the furniture) with nothing in between. No alcoves, no secondary spaces, no medium-scale elements. People feel exposed.

2. **Roughness (11):** Everything is perfectly machined. The marble is flawless, the furniture is factory-perfect. There is no evidence of human hands. This creates psychological distance.

3. **Deep Interlock (8):** Nothing hooks into anything else. The furniture sits on the floor but doesn't connect to walls, columns, or each other. The reception desk is an island. Everything is isolated.

### Property Interactions

**Reinforcing strengths:** Contrast and Void work together - the light from the windows dramatizes the central space.

**Compounding weaknesses:** Missing Levels of Scale + Absent Roughness + Absent Deep Interlock = nowhere for humans to find a scale that fits them, nothing that welcomes their presence, no way to feel connected to the space.

**Key leverage point:** Levels of Scale. If intermediate scales were introduced - alcoves, raised areas, ceiling variations, partial partitions - the space would gain places for humans to inhabit. This would also create opportunities for Local Symmetries (each alcove could have its own balance) and Deep Interlock (alcoves could hook into the main space).

### Synthesis

**Where life is strongest:** The material contrast and the dramatic window wall. The void of the central space has potential but is currently too vast.

**Where life is weakest:** The human scale. There is nowhere in this lobby that a person can feel comfortable, enclosed, held. The space is designed to impress, not to welcome.

**Root cause of deadness:** The modernist desire for purity has stripped away the intermediate scales and irregularities that make spaces livable. This is architecture for photographs, not for people waiting for their room.

**Highest-impact improvement:** Introduce alcoves or sub-spaces at the edges where people can sit with some enclosure. Add one or two pieces of handmade furniture or art to break the machine perfection. Create pools of light with floor lamps rather than uniform overhead lighting.

### Return to Feeling

Yes - the analysis confirms the initial feeling. The lobby is impressive (Contrast, Void, Good Shape) but cold (missing Levels of Scale, Roughness, Deep Interlock). The feeling of "admire but don't linger" maps directly onto "life in the dramatic elements, death in the human-scale elements."

The lobby was designed to say "important" and "expensive." It succeeds. But it was not designed to say "welcome" and "rest here." No analysis was needed to feel this - but now we can name why.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Subject too vague | Request specific description or image |
| Cannot observe subject directly | Note that analysis is based on description; recommend direct observation |
| User wants only specific properties | Focus analysis on requested properties, note what's missing |
| Properties seem inapplicable | Adapt concepts to domain; note limitations |

---

## Integration

This skill is part of the **Christopher Alexander** expert persona. It operationalizes the fifteen properties framework from *The Nature of Order* (2002-2004). Use it in conjunction with:

- **pattern-language-application** - for identifying specific patterns that might strengthen weak properties
- **center-analysis** - for deeper diagnosis of center structures
- **unfolding-process-design** - for sequencing changes that strengthen properties while preserving wholeness

The fifteen properties are not a checklist but a way of seeing. The goal is to develop the capacity to feel what makes things alive and to name what you feel.