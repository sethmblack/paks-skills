---
name: unfolding-process-design
description: Create a step-by-step generative sequence for designing, building, or transforming something while preserving and extending wholeness at each step.
license: MIT
metadata:
  version: 1.0.2345
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- unfolding-process-design
- urban-planning
---

# Unfolding Process Design

Create a step-by-step generative sequence for designing, building, or transforming something while preserving and extending wholeness at each step. Based on Christopher Alexander's process of structure-preserving transformations from *The Nature of Order*.

---

## Constitutional Constraints

Before applying this skill, verify:
- The process serves constructive creation, not destruction
- Each step is evaluated for its effect on wholeness, not just efficiency
- Local conditions and feedback are respected, not overridden by the sequence
- The goal is increasing life, not completing a checklist

---

## When to Use

- Planning a design project (building, software, organization)
- Transforming an existing structure that must remain functional
- Facilitating participatory design processes
- Teaching design thinking that preserves wholeness
- Sequencing renovations or incremental improvements
- Any situation where "What order should we do this?" would be valuable

---

## Don't Use When

- The task is simple enough that sequencing is obvious
- A fixed plan must be followed regardless of feedback
- The user needs a pattern diagnosis rather than a process
- Speed matters more than wholeness

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| goal | Yes | What is being created or transformed |
| existing_whole | Yes | What already exists (even if "empty site" or "blank page") |
| constraints | No | Fixed requirements, budgets, timelines |
| participants | No | Who will be involved in the process |

---

## Understanding Unfolding

### The Core Principle

Living structure cannot be designed all at once and then built. It must unfold through a sequence of structure-preserving transformations, where each step:
1. Begins with the existing wholeness
2. Identifies the next differentiation that would most increase life
3. Makes that transformation
4. Pauses to feel the new wholeness
5. Lets the new whole guide the next step

### Structure-Preserving Transformation

A structure-preserving transformation is a change that:
- Maintains the existing centers and their relationships
- Strengthens rather than weakens the whole
- Adds new structure that belongs to what exists
- Could not be predicted in detail before the previous step

### Why Sequence Matters

The order of decisions affects the outcome:
- Large-scale decisions constrain small-scale possibilities
- Each step creates context for the next
- Early mistakes propagate; late mistakes can be absorbed
- Feedback at each step allows course correction

### The Difference from Master Planning

| Master Plan Approach | Unfolding Approach |
|---------------------|-------------------|
| Design everything first, then build | Design and build in interwoven steps |
| Details fixed before context exists | Details emerge from established context |
| Changes require redoing the plan | Changes are expected and welcomed |
| Building is execution | Building is continuation of design |
| Feels efficient but produces dead structure | Feels slow but produces living structure |

---

## Process Design Steps

### Step 1: Feel the Existing Wholeness

Before proposing any sequence, understand what exists:

**Questions:**
- What is already present? (Even empty land has patterns, history, context)
- What are the existing centers?
- What is the existing quality - alive or dead? Where?
- What wants to happen here? What is latent?

**Record:**
- Description of existing state
- Assessment of existing wholeness
- What is working / what is struggling
- What the situation seems to "want"

### Step 2: Identify the Largest Relevant Decision

The sequence must begin with the largest-scale decision that has not yet been made:

| If creating... | Largest decision might be... |
|---------------|------------------------------|
| A building | Where on the site? What orientation? |
| A room | Where in the building? Relation to other rooms? |
| A software system | What are the major components? How do they relate? |
| An organization | What is the core structure? Who reports to whom? |
| A garden | Where are the major zones? How do paths move? |

**Principle:** You cannot decide small things rightly until large things are settled. But don't decide large things in more detail than necessary.

### Step 3: Design the Sequence

For each step in the sequence, specify:

1. **What decision/transformation** - What is being determined
2. **Why this step now** - What makes it the right next step
3. **What existing wholeness it preserves** - What is being maintained
4. **What new structure it adds** - What differentiation occurs
5. **What feedback to gather** - How to test if the step was right
6. **What the step enables** - What subsequent decisions become possible

### Step 4: Build in Feedback Points

Critical: The sequence is not a fixed plan. It is a guide that must be modified based on what emerges.

**At each major step:**
- Pause and feel: Does this increase life?
- Gather feedback: From users, from observation, from the material itself
- Be willing to go back: If a step decreased life, undo or modify it
- Let the new whole guide: Don't force the next planned step if something else wants to happen

### Step 5: Plan for Adaptation

Anticipate where the sequence might need to change:
- What decisions might reveal unexpected constraints?
- What steps might produce surprises (good or bad)?
- Where is local adaptation most important?
- What can be fixed late vs. what must be right early?

---

## Output Format

```markdown
## Unfolding Process: [Goal]

### Existing Wholeness

**Current state:** [Description of what exists]
**Existing centers:** [What already has presence]
**Quality assessment:** [Alive/dead spectrum]
**What wants to happen:** [Latent potential]

### Sequence Overview

| Step | Decision | Scale | Enables |
|------|----------|-------|---------|
| 1 | [Brief description] | [Large/Medium/Small] | [What it makes possible] |
| 2 | [Brief description] | [Scale] | [What it makes possible] |
| ... | ... | ... | ... |

### Detailed Sequence

#### Step 1: [Decision Name]

**What:** [Precise description of what is being decided/made]

**Why now:** [Why this must come before other decisions]

**Preserves:** [What existing wholeness is maintained]

**Adds:** [What new structure/differentiation occurs]

**Feedback:** [How to test if this step worked]
- [ ] [Specific check]
- [ ] [Specific check]

**Enables:** [What subsequent decisions become possible]

**If this step reveals problems:** [What to do if feedback is negative]

---

#### Step 2: [Decision Name]

[Same structure...]

---

[Continue for all steps...]

### Feedback Points

| After Step | Pause to... | Key Questions |
|------------|-------------|---------------|
| [Step #] | [Type of review] | [What to ask] |

### Adaptation Anticipation

**Likely branch points:** [Where sequence might need to change]
**High-uncertainty steps:** [Where surprises are most likely]
**Can be fixed late:** [Decisions that can be revised]
**Must be right early:** [Decisions that propagate forward]

### Success Criteria

At completion, the whole should feel:
- [Quality 1]
- [Quality 2]
- [Quality 3]

The test: Does someone feel more themselves in this place/system?
```

---

## Example

**Input:** "Design an unfolding process for renovating a small urban backyard into a garden. Currently it's a concrete patio with a few overgrown shrubs along the fence."

**Output:**

## Unfolding Process: Urban Backyard Garden

### Existing Wholeness

**Current state:** Rectangular concrete patio, approximately 15x20 feet. Chain-link fence on three sides with overgrown shrubs (ligustrum, possibly). Back wall of house forms fourth side with a sliding door. One outdoor outlet. Neighbors visible over fence. Northeast orientation.

**Existing centers:**
- The sliding door (strong) - the threshold between house and yard
- The concrete slab (moderate) - has presence as a surface, but dead
- The shrub mass (weak) - has some life but formless, neglected

**Quality assessment:** Mostly dead. The concrete creates flat, hard deadness. The shrubs have biological life but no designed life. The fence and neighbors create exposure, lack of enclosure.

**What wants to happen:** This space wants to be a refuge - a small private world connected to the house. The sliding door is the beginning; the garden should pull you out. Something green, enclosed, intimate.

### Sequence Overview

| Step | Decision | Scale | Enables |
|------|----------|-------|---------|
| 1 | Define the garden's relationship to the house | Large | All subsequent spatial decisions |
| 2 | Establish zones (where to sit, where to plant) | Large | Hardscape vs. softscape decisions |
| 3 | Create the threshold/transition | Medium | Connection between house and garden |
| 4 | Establish the primary seating center | Medium | Where the garden gathers |
| 5 | Define planting beds and edges | Medium | What goes where |
| 6 | Create enclosure/screening | Medium | Privacy and intimacy |
| 7 | Add secondary centers (focal points) | Small | Visual interest and movement |
| 8 | Plant and detail | Small | The living material |

### Detailed Sequence

#### Step 1: Define the Garden's Relationship to the House

**What:** Decide whether the garden extends the interior outward or whether it is a separate world. Stand at the sliding door. Where does the garden begin? Is the patio "inside extended" or "outside beginning"?

**Why now:** This fundamental relationship determines everything else - sight lines, materials, planting density near the house, formality gradient.

**Preserves:** The existing sliding door as primary threshold.

**Adds:** An intentional relationship. A decision about what kind of place this is.

**Feedback:**
- [ ] Stand in the kitchen looking out. What do you want to see?
- [ ] Stand in the yard looking back. What do you want the house to feel like from here?

**Enables:** If "extended interior" - more hardscape near house, formal near door, wilder at edges. If "separate world" - immediate transition to garden at threshold, enclosure emphasized, the house recedes.

**If this step reveals problems:** This is a values question more than a design question. If you can't decide, try both for a day. Which feeling is more needed in your life?

---

#### Step 2: Establish Zones (Where to Sit, Where to Plant)

**What:** Using stakes, string, or chalk on the concrete, mark out zones. Where is the primary sitting/gathering zone? Where are planting beds? Where are paths? Don't decide details - just proportions and locations.

**Why now:** Zone decisions precede all specific choices. You cannot design a planting bed before you know where it is.

**Preserves:** The existing slab (for now) - it becomes the substrate for zone mapping. The existing shrubs along the fence - assume they stay until proven otherwise.

**Adds:** Spatial differentiation. The beginning of centers.

**Feedback:**
- [ ] Sit in the proposed sitting zone. Does it feel like the right place?
- [ ] Is there morning sun for coffee? Evening shade for dinner?
- [ ] Are the proportions pleasing? (Too much hardscape? Too little?)

**Enables:** All subsequent decisions - where to remove concrete, where to build, where to plant.

**If this step reveals problems:** Zones are easy to move at this stage. If sitting in the sitting zone feels wrong, move the zone. This is why we use stakes, not concrete.

---

[Additional steps would continue with the same detailed structure...]

### Feedback Points

| After Step | Pause to... | Key Questions |
|------------|-------------|---------------|
| 2 | Live with zones | Spend a weekend with stakes in place. How does it feel? |
| 4 | Test seating | Actually sit there. At different times of day. |
| 6 | Experience enclosure | Does it feel private? Restful? |
| 8 | Inhabit | Spend time in the finished garden before "finishing" details |

### Adaptation Anticipation

**Likely branch points:**
- Step 2: Zones might need to shift based on sun patterns you didn't anticipate
- Step 6: Enclosure might reveal that you want more or less light than expected

**High-uncertainty steps:**
- Step 1: The relationship decision is philosophical and might need revision
- Step 8: Plant performance is unpredictable; plan for replacement

**Can be fixed late:**
- Secondary centers, details, specific plants
- Enclosure density

**Must be right early:**
- Zone proportions (removing more concrete later is costly)
- Seating location (the heart of the garden must be right)

### Success Criteria

At completion, the whole should feel:
- Private - a refuge from the city
- Connected - an extension of your home, not separate
- Alive - growing, changing, inhabited
- Inviting - you want to be there

The test: Do you find yourself going outside more? Does morning coffee want to happen in the garden? Do you show it to visitors with pride?

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Goal is vague | Clarify what kind of outcome is desired before sequencing |
| Existing wholeness unclear | Do center analysis first before sequencing transformation |
| User wants to skip steps | Explain what risks skipping creates; allow if they accept |
| Sequence stalls mid-process | Return to most recent step that felt right; diagnose what went wrong |

---

## Integration

This skill is part of the **Christopher Alexander** expert persona. It operationalizes the unfolding process from *The Nature of Order* (2002-2004). Use it in conjunction with:

- **fifteen-properties-analysis** - to test whether each step increases life
- **center-analysis** - to understand existing wholeness before sequencing
- **pattern-language-application** - to identify patterns relevant to each step

The fundamental insight: living structure emerges from process, not from plan. The sequence creates the conditions for each step to be right. Trust the process - and trust yourself to feel when a step is wrong.