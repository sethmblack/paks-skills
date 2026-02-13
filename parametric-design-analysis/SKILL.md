---
name: parametric-design-analysis
description: Analyze any design challenge through parametric principles—identifying the parameters (site, structure, program, movement, light, material) that should drive form generation through systematic rela...
license: MIT
metadata:
  author: sethmblack
  version: 1.0.4640
repository: https://github.com/sethmblack/paks-skills
keywords:
- compression
- parametric-design-analysis
- writing
---

# Parametric Design Analysis

Analyze any design challenge through parametric principles—identifying the parameters (site, structure, program, movement, light, material) that should drive form generation through systematic relationships rather than arbitrary aesthetic choices. Based on Zaha Hadid's methodology: "Parametric design is not about making things curvy for the sake of curves. It is about discovering forms that emerge from the logic of the problem itself."

---

## When to Use

- Designing anything where form should emerge from constraints
- Moving from arbitrary aesthetic decisions to systematic exploration
- Creating complex geometries that respond to multiple factors
- Developing designs that need internal consistency and logic
- Breaking free from default shapes that do not serve the problem
- Seeking innovation through constraint-driven form generation

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| design_challenge | Yes | What is being designed and its primary purpose |
| known_constraints | Yes | Physical, functional, or contextual limitations |
| performance_requirements | No | What the design must achieve (structural, thermal, acoustic, etc.) |
| site_context | No | Location, climate, surroundings, existing conditions |
| user_flows | No | How people will move through or interact with the design |

---

## The Parametric Principle

### What Is Parametric Design?

Parametric design treats form not as something imposed but as something that **emerges** from the systematic relationships between parameters. A parameter is any factor that influences form:

> "Parameters—structural loads, circulation flows, environmental factors—generate form through algorithmic processes rather than arbitrary aesthetic choices."

The designer's role shifts from "drawing a shape" to "defining relationships between forces."

### Parameters vs. Arbitrary Choices

| Arbitrary Design | Parametric Design |
|------------------|-------------------|
| "Make it curved because curves look modern" | "Curve follows structural force distribution" |
| "Put windows here because that's typical" | "Window placement responds to solar angle and view corridors" |
| "Use this height because zoning allows it" | "Height varies to optimize daylight penetration" |
| "Rectangular rooms because that's buildable" | "Room geometry emerges from circulation flow and acoustic needs" |

---

## Analysis Process

### Step 1: Identify All Parameters

Map every factor that should influence form:

**Site Parameters:**
| Parameter | Description | Form Influence |
|-----------|-------------|----------------|
| Topography | Ground slopes, levels, features | [How it affects form] |
| Solar path | Sun angles throughout day/year | [How it affects form] |
| Wind | Prevailing directions, intensities | [How it affects form] |
| Views | What to frame, screen, or ignore | [How it affects form] |
| Context | Adjacent buildings, streets, landscapes | [How it affects form] |

**Structural Parameters:**
| Parameter | Description | Form Influence |
|-----------|-------------|----------------|
| Span requirements | Distances to cross without support | [How it affects form] |
| Load distribution | Where forces concentrate | [How it affects form] |
| Material properties | What each material does best | [How it affects form] |
| Seismic/wind loads | Dynamic forces to resist | [How it affects form] |

**Program Parameters:**
| Parameter | Description | Form Influence |
|-----------|-------------|----------------|
| Circulation flows | How people move through space | [How it affects form] |
| Functional adjacencies | What needs to be near what | [How it affects form] |
| Flexibility needs | What must change over time | [How it affects form] |
| Privacy/openness | What needs enclosure vs. exposure | [How it affects form] |

**Experiential Parameters:**
| Parameter | Description | Form Influence |
|-----------|-------------|----------------|
| Daylight quality | Where natural light is needed | [How it affects form] |
| Acoustics | Sound control requirements | [How it affects form] |
| Thermal comfort | Heating, cooling, ventilation needs | [How it affects form] |
| Emotional journey | What feelings to evoke where | [How it affects form] |

### Step 2: Establish Parameter Relationships

Parameters do not act independently. Map how they interact:

**Relationship Matrix:**
| Parameter A | Parameter B | Relationship | Form Implication |
|-------------|-------------|--------------|------------------|
| Solar angle | Window placement | Direct | Windows orient/size to optimize light |
| Circulation | Structure | Inverse | Structure avoids circulation paths |
| Span | Material | Constraining | Material choice limits/enables span |
| [Parameter] | [Parameter] | [Type] | [Implication] |

**Relationship Types:**
- **Direct:** When A increases, B increases
- **Inverse:** When A increases, B decreases
- **Constraining:** A sets limits on B
- **Enabling:** A creates possibilities for B
- **Competing:** A and B want different things

### Step 3: Identify Dominant Parameters

Not all parameters matter equally. Rank by importance:

**Parameter Hierarchy:**

1. **Primary Parameters** (non-negotiable, drive major form decisions):
   - [List the 2-3 most important parameters]

2. **Secondary Parameters** (important, influence refinement):
   - [List parameters that shape details]

3. **Tertiary Parameters** (desirable, optimize if possible):
   - [List nice-to-have considerations]

### Step 4: Generate Form Logic

Based on parameter relationships, define the rules that will generate form:

**Form Generation Rules:**

| Rule | Based On | Description |
|------|----------|-------------|
| 1 | [Parameters] | [How form responds to these parameters] |
| 2 | [Parameters] | [How form responds to these parameters] |
| 3 | [Parameters] | [How form responds to these parameters] |

**Example Rules:**
- "Roof curvature follows structural force distribution, minimizing material while spanning the required distance"
- "Floor levels step down following topography, maintaining constant relationship to ground"
- "Facade porosity increases where views are desirable and decreases where privacy is needed"

### Step 5: Identify Tensions and Trade-offs

Where parameters conflict, document the trade-off decisions:

**Tension Analysis:**

| Conflict | Parameter A Wants | Parameter B Wants | Resolution |
|----------|-------------------|-------------------|------------|
| [Conflict 1] | [A's preference] | [B's preference] | [How to resolve] |
| [Conflict 2] | [A's preference] | [B's preference] | [How to resolve] |

### Step 6: Validate Parametric Logic

Check that the form logic is truly parametric:

**Validation Checklist:**
- [ ] Form decisions can be traced to specific parameters
- [ ] Changes in parameters would produce different forms
- [ ] No arbitrary aesthetic choices remain unexplained
- [ ] Relationships between parameters are consistent
- [ ] The logic could be expressed algorithmically

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

## Output Format

```markdown
## Parametric Design Analysis: [Design Challenge]

### Design Brief
[Clear statement of what is being designed and its purpose]

### Parameter Inventory

#### Primary Parameters (Form Drivers)
| Parameter | Current Value/Condition | Form Influence |
|-----------|------------------------|----------------|
| [Parameter 1] | [Value] | [How it drives form] |
| [Parameter 2] | [Value] | [How it drives form] |

#### Secondary Parameters (Refinement)
| Parameter | Current Value/Condition | Form Influence |
|-----------|------------------------|----------------|
| [Parameter 3] | [Value] | [How it shapes details] |

#### Tertiary Parameters (Optimization)
| Parameter | Current Value/Condition | Form Influence |
|-----------|------------------------|----------------|
| [Parameter 4] | [Value] | [Nice-to-have influence] |

### Parameter Relationships
[Diagram or matrix of how parameters interact]

Key relationships:
- [Parameter A] and [Parameter B]: [Relationship type and implication]
- [Continue for important relationships]

### Form Generation Logic

**Rule 1: [Name]**
[Parameters involved] → [Form response]
*"The [element] does [action] because [parameter logic]"*

**Rule 2: [Name]**
[Parameters involved] → [Form response]
*"The [element] does [action] because [parameter logic]"*

[Continue for all major form decisions]

### Tensions and Resolutions

| Conflict | Resolution Approach |
|----------|---------------------|
| [Tension 1] | [How resolved] |
| [Tension 2] | [How resolved] |

### Non-Parametric Elements
[Any elements that remain arbitrary, with justification]

### Hadid Principle Applied
> "There are 360 degrees, so why stick to one?"

[How this analysis expands beyond conventional assumptions]

### Recommended Next Steps
1. [First action to develop the parametric logic]
2. [Second action]
3. [Third action]
```

---

## Constraints

- Do not treat parametric design as an excuse for arbitrary complexity
- Parameters must be real factors, not invented to justify a preconceived form
- Acknowledge when aesthetic choices cannot be fully parametrized
- The goal is form emergence from logic, not complexity for its own sake
- Not all design problems benefit from parametric thinking; recognize when simpler approaches suffice

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No clear parameters identified | Ask for more context about constraints and requirements |
| Parameters conflict irreconcilably | Document the trade-off; recommend user prioritization |
| Design seems to lack meaningful parameters | Question whether parametric approach is appropriate |
| Too many parameters to manage | Focus on hierarchy; primary parameters first |
| Parameters are vague | Request specificity; quantify where possible |

---

## Outputs

**Primary Output:** A structured analysis document that identifies and articulates patterns, insights, and actionable recommendations based on the input data.

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

**Example output:** See the Example section below for a complete demonstration.

## Example

**Input:** "We're designing a community library. It's a single-story building on a flat site with a fixed rectangular footprint due to property boundaries. How do we apply parametric thinking when we seem to have so many fixed constraints?"

**Output:**

## Parametric Design Analysis: Community Library

### Design Brief
A single-story community library on a flat site with fixed rectangular footprint. While the boundary constraints seem to limit parametric exploration, significant parameters remain for form generation within and above the footprint.

### Parameter Inventory

#### Primary Parameters (Form Drivers)
| Parameter | Current Value/Condition | Form Influence |
|-----------|------------------------|----------------|
| Natural daylight | Libraries need even, glare-free reading light | Roof form and fenestration placement |
| Acoustic zones | Quiet study vs. active children's area vs. meeting rooms | Internal volume shaping and material surfaces |
| Circulation logic | Browse → Select → Read/Study flow | Spatial sequence and visual connections |

#### Secondary Parameters (Refinement)
| Parameter | Current Value/Condition | Form Influence |
|-----------|------------------------|----------------|
| Solar angles | [Site latitude and orientation] | Roof slope, clerestory positions |
| Thermal mass | Climate requires [heating/cooling] | Wall thickness, material choice |
| Collection visibility | Users should see across collections | Shelving heights, sight lines |

#### Tertiary Parameters (Optimization)
| Parameter | Current Value/Condition | Form Influence |
|-----------|------------------------|----------------|
| Future flexibility | Collection may digitize; spaces may repurpose | Structural grid, partition options |
| Community identity | Neighborhood character | Material palette, entrance gesture |

### Parameter Relationships

Key relationships:
- **Daylight** and **Acoustic zones**: Competing—skylights provide light but can transmit noise. Resolution: acoustic skylights, or skylight placement over non-quiet zones.
- **Circulation** and **Visibility**: Direct—open circulation enables visual browsing; both want openness.
- **Thermal mass** and **Flexibility**: Inverse—heavy thermal mass limits reconfiguration. Resolution: concentrate mass at perimeter, flexibility at interior.

### Form Generation Logic

**Rule 1: Daylight Distribution**
[Solar angles + Reading light needs] → Roof undulates to provide consistent daylight
*"The roof rises and falls to admit northern clerestory light while screening harsh southern sun. The form follows the sun's path."*

**Rule 2: Acoustic Topography**
[Quiet zones + Active zones + Children's area] → Ceiling height varies by acoustic need
*"The ceiling compresses over quiet study to create intimacy and absorb sound; it rises over children's area to allow energy without echo."*

**Rule 3: Visual Flow**
[Browsing circulation + Collection visibility] → Shelving heights and angles respond to sight lines
*"Standing at the entrance, you see across the entire collection. Shelving angles follow your natural scan pattern, revealing rather than hiding."*

**Rule 4: Thermal Envelope**
[Thermal mass needs + Solar exposure] → Wall thickness and material vary by orientation
*"The south wall is thick and dense, storing heat; the north wall is thin and glazed, admitting light without thermal penalty."*

### Tensions and Resolutions

| Conflict | Resolution Approach |
|----------|---------------------|
| Daylight vs. Acoustics | Acoustic skylight systems; zone separation |
| Visual openness vs. Noise control | Strategic sound absorption in materials; volume shaping |
| Thermal mass vs. Flexibility | Perimeter mass, interior lightness |

### Non-Parametric Elements
- **Rectangular footprint**: Fixed by site constraint (not arbitrary)
- **Single story**: Fixed by brief (could be parametrized if questioned)

### Hadid Principle Applied
> "There are 360 degrees, so why stick to one?"

The footprint is fixed, but nothing requires the roof to be flat, the ceiling to be uniform, or the interior to be a box. Within the fixed boundary, every surface can respond to the parameters of light, sound, movement, and human experience. A rectangle in plan becomes a landscape in section.

### Recommended Next Steps
1. Develop solar analysis for specific site orientation
2. Map acoustic zones with program requirements
3. Create sectional studies showing roof/ceiling undulation responding to parameters
4. Test thermal performance of variable wall strategies

---

## Integration

This skill is part of the **Zaha Hadid** expert persona. Use it when seeking systematic form generation from constraints. It pairs with:
- **fluid-space-design** for creating continuous spatial experiences within parametric forms
- **anti-orthogonal-challenge** for questioning whether rectangular constraints are truly fixed
- **landscape-integration-assessment** for ensuring parametric forms respond to site context