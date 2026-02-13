---
name: pattern-language-application
description: Analyze any design, system, or situation through Christopher Alexander's pattern language methodology.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.4649
repository: https://github.com/sethmblack/paks-skills
keywords:
- pattern-language-application
- urban-planning
---

# Pattern Language Application

Analyze any design, system, or situation through Christopher Alexander's pattern language methodology - identifying which patterns are present, which are missing, how they relate across scales, and how to strengthen the whole.

---

## Constitutional Constraints

Before applying this skill, verify:
- The analysis serves constructive design purposes
- Pattern identification is used to understand and improve, not to impose rigid rules
- Local context and adaptation are respected - patterns are relationships, not templates
- The goal is increasing life and wholeness, not mechanical compliance

---

## When to Use

- Analyzing any physical space, building, neighborhood, or urban setting
- Evaluating software architecture, organizational structure, or process design
- Diagnosing why a designed system feels "dead" or dysfunctional
- Seeking to strengthen existing configurations rather than replace them
- Teaching others to see recurring solutions to recurring problems
- Any situation where "What patterns apply here?" would be valuable

---

## Don't Use When

- The user needs pure aesthetic judgment without structural analysis
- Quick surface-level feedback is more appropriate than deep pattern analysis
- The situation is so novel that no recurring patterns apply
- The user has explicitly rejected pattern-based approaches

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| subject | Yes | The design, space, system, or situation to analyze |
| scale_focus | No | Specific scale to emphasize (region, building, room, detail) |
| known_problems | No | Issues the user has already identified |
| constraints | No | Limitations on what can be changed |

---

## Pattern Analysis Process

### Step 1: Identify the Scale

Determine which scale levels are relevant to the analysis:

| Scale Level | Pattern Range | Applies When |
|-------------|---------------|--------------|
| Regional | 1-26 | Analyzing cities, regions, large-scale planning |
| Neighborhood | 27-48 | Analyzing districts, communities, neighborhoods |
| Building Complex | 49-94 | Analyzing groups of buildings, campuses |
| Individual Building | 95-126 | Analyzing single buildings, their siting |
| Interior Space | 127-178 | Analyzing rooms, spatial relationships |
| Detail | 179-253 | Analyzing windows, alcoves, materials, light |

**Multi-scale analysis is usually necessary.** Problems at one scale often stem from failures at larger scales.

### Step 2: Identify Present Patterns

For each relevant scale, identify patterns that are already present and functioning:

**Questions to ask:**
- What recurring configurations support life in this situation?
- What is working? Where do people naturally gather, linger, feel at home?
- What existing elements could be named as patterns?

**Document present patterns:**
- Pattern number and name (if from the 253)
- How it manifests in this specific context
- How strongly it is implemented (strong/moderate/weak)

### Step 3: Identify Missing Patterns

For each relevant scale, identify patterns that are absent or broken:

**Questions to ask:**
- What tensions remain unresolved?
- What human needs are not being met?
- What configurations would address the identified problems?
- What patterns at larger scales would create context for smaller improvements?

**Document missing patterns:**
- Pattern number and name
- Why it is needed (what tension it would resolve)
- What is currently there instead (if anything)

### Step 4: Map Pattern Relationships

Patterns don't exist in isolation. Map how they connect:

**Vertical relationships (scale):**
- Which larger patterns set context for this pattern?
- Which smaller patterns would complete this pattern?

**Horizontal relationships (within scale):**
- Which patterns at the same scale support each other?
- Are any patterns in conflict?

### Step 5: Diagnose Root Causes

Often surface problems stem from missing patterns at larger scales:

**Questions to ask:**
- If a room feels wrong, is the building sited correctly?
- If a building feels wrong, is the neighborhood structured well?
- What upstream patterns, if implemented, would make downstream patterns possible?

### Step 6: Propose Pattern Application

Suggest specific patterns to apply, in sequence from large to small:

**For each proposed pattern:**
- State the pattern and why it applies
- Describe how it might manifest in this specific context
- Note what adaptations local conditions require
- Connect to patterns at adjacent scales

---

## Output Format

```markdown
## Pattern Language Analysis: [Subject]

### Scale Assessment

**Relevant scales:** [List scales analyzed]
**Primary focus:** [Main scale of analysis]

### Patterns Present

| Pattern | Name | Implementation | Notes |
|---------|------|----------------|-------|
| [#] | [Name] | Strong/Moderate/Weak | [How it appears] |

**Strongest patterns:** [Which patterns are most alive]
**What's working:** [Summary of functional configurations]

### Patterns Missing or Broken

| Pattern | Name | Why Needed | Current State |
|---------|------|------------|---------------|
| [#] | [Name] | [Tension to resolve] | [What exists now] |

**Most critical gaps:** [Patterns most urgently needed]

### Pattern Relationships

**Scale connections:**
- [How larger patterns set context for smaller]
- [How smaller patterns would complete larger]

**Within-scale relationships:**
- [Patterns that support each other]
- [Any conflicts or tensions]

### Root Cause Diagnosis

[Analysis of upstream patterns that create downstream problems]

### Recommended Pattern Sequence

Apply in this order (large to small):

1. **[Pattern #: Name]**
   - Why: [Tension resolved]
   - How: [Specific adaptation to context]
   - Enables: [What smaller patterns this makes possible]

2. **[Pattern #: Name]**
   - Why:
   - How:
   - Enables:

[Continue sequence...]

### Integration Notes

**Local adaptations needed:** [Context-specific modifications]
**Constraints to respect:** [Limitations on change]
**Next diagnostic step:** [If deeper analysis needed]
```

---

## Example

**Input:** "Our office has a break room that nobody uses. People eat at their desks instead. What's wrong?"

**Output:**

## Pattern Language Analysis: Unused Break Room

### Scale Assessment

**Relevant scales:** Building (95-126), Interior Space (127-178), Detail (179-253)
**Primary focus:** Interior Space - how rooms relate to each other

### Patterns Present

| Pattern | Name | Implementation | Notes |
|---------|------|----------------|-------|
| 130 | Entrance Room | Weak | There is a small vestibule, but it serves as storage |
| 146 | Flexible Office Space | Strong | Open plan allows various configurations |

**Strongest patterns:** The workspace itself is reasonably configured for work.
**What's working:** People can work at their desks. The fundamental work function is supported.

### Patterns Missing or Broken

| Pattern | Name | Why Needed | Current State |
|---------|------|------------|---------------|
| 127 | Intimacy Gradient | Critical | Break room is at far end of office; no gradient from public to private |
| 129 | Common Areas at the Heart | Critical | Break room is peripheral, not central; paths don't pass through it |
| 147 | Communal Eating | Missing | No sense of shared meal; just a room with appliances |
| 159 | Light on Two Sides | Missing | Break room has one window (or none?) |
| 179 | Alcoves | Missing | No varied spaces within; one undifferentiated room |
| 181 | The Fire | Missing | No gathering focal point |
| 252 | Pools of Light | Missing | Uniform fluorescent lighting |

**Most critical gaps:** 129 (Common Areas at the Heart), 127 (Intimacy Gradient)

### Pattern Relationships

**Scale connections:**
- The break room fails because of building-scale decisions (its location)
- Detail improvements (better lighting, alcoves) won't fix the fundamental problem

**Within-scale relationships:**
- 129 and 127 work together: central common area needs to sit at the transition point in the intimacy gradient
- 147, 181, and 252 create the atmosphere but require 129 first

### Root Cause Diagnosis

The break room fails not because of what's in it, but where it is. Pattern 129 (Common Areas at the Heart) states: "Place the common areas at the heart of the house, where all paths cross."

Your break room is peripheral. People must make a special trip to use it. There is no natural reason to pass through it. It sits outside the flow of daily movement.

This is a building-scale problem. No amount of comfortable furniture, good coffee, or nice lighting will fix a room that is in the wrong place.

### Recommended Pattern Sequence

Apply in this order (large to small):

1. **Pattern 129: Common Areas at the Heart**
   - Why: The fundamental problem - break room is peripheral
   - How: If possible, move communal functions to where paths already cross. If the break room cannot move, consider: Can a satellite coffee station be placed at the heart? Can the meeting-point for daily standups be near the break room, creating traffic?
   - Enables: All other patterns become viable once people naturally pass through

2. **Pattern 127: Intimacy Gradient**
   - Why: Eating is semi-private; the break room should not be in the most public zone nor the most private
   - How: If moving rooms, place it between workspace and entrance, at moderate publicness. If not moving, consider visual screening that creates transition.
   - Enables: People feel comfortable lingering rather than rushing back

3. **Pattern 181: The Fire**
   - Why: A gathering needs a focal point
   - How: Not a literal fire in an office, but: a coffee station everyone faces, a window with comfortable seating around it, a shared table oriented to a view
   - Enables: Communal eating (147) because people orient to shared center

4. **Pattern 179: Alcoves**
   - Why: One undifferentiated room feels institutional
   - How: Create sub-spaces: a coffee alcove, a sitting alcove, a standing-chat area by the window
   - Enables: Different modes of break (quick coffee vs. lingering lunch)

5. **Pattern 252: Pools of Light**
   - Why: Uniform lighting feels like work, not rest
   - How: Replace overhead fluorescents with task lighting, table lamps, pendant over gathering spot
   - Enables: Psychological transition from work mode to rest mode

### Integration Notes

**Local adaptations needed:** The ideal is to move the break room. If this is impossible, compensate by creating reasons for traffic to pass by/through: locate printer there, hold short meetings there, place the best coffee machine there.

**Constraints to respect:** If major renovation is impossible, prioritize patterns 181, 179, 252 - they can improve atmosphere even in a poorly located room, though they won't fully compensate.

**Next diagnostic step:** Walk the space. Where do people actually gather informally now? That location has something the break room lacks. Study it.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Subject too vague | Request specific description of the space/system |
| Scale unclear | Analyze all potentially relevant scales, note which is primary |
| No clear patterns apply | The 253 patterns are architectural; adapt concepts or note limitation |
| User rejects pattern approach | Respect preference; offer alternative framing if appropriate |

---

## Integration

This skill is part of the **Christopher Alexander** expert persona. It operationalizes the pattern language methodology from *A Pattern Language* (1977). Use it in conjunction with:

- **fifteen-properties-analysis** - for deeper diagnosis of why patterns feel alive or dead
- **center-analysis** - for understanding the structure of wholeness
- **unfolding-process-design** - for sequencing changes to preserve wholeness

The goal is not mechanical pattern application but understanding the forces at work in a situation and finding configurations that resolve them. Patterns are the vocabulary; the language is spoken by feeling for what creates life.