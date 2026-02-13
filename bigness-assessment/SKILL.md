---
name: bigness-assessment
description: Evaluate whether a project's scale has crossed the threshold where traditional architectural values break down and a new regime of complexity emerges.
license: MIT
metadata:
  version: 1.0.3479
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- bigness-assessment
- urban-planning
---

# Bigness Assessment

Evaluate whether a project's scale has crossed the threshold where traditional architectural values break down and a new regime of complexity emerges. Determine if Bigness applies and what strategic implications follow.

---

## Constitutional Constraints

- **Bigness is not a value judgment** - It is a description of a threshold, not a prescription for design
- **Scale is not size** - A large building is not automatically Big; Bigness refers to a regime of complexity
- **Beyond good and evil** - At the scale of Bigness, moral categories like "good architecture" or "contextual" become inadequate
- **Surrender is productive** - Acknowledging what cannot be controlled is the first step to working effectively at this scale

---

## When to Use

- Evaluating large-scale projects (typically 50,000+ m² or major urban impact)
- Determining whether traditional architectural approaches will apply
- Advising clients on expectations for design control
- Understanding why conventional criticism seems inadequate to a project
- Planning projects that will become "neighborhoods" or "cities" unto themselves

**Don't use when:**
- Project is clearly below Bigness threshold (most buildings)
- Scale is large but program is simple and unified
- Client needs reassurance, not confrontation with complexity
- The question is aesthetic rather than organizational

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| project_description | Yes | The building, development, or intervention being evaluated |
| scale_metrics | Recommended | Floor area, height, program diversity, occupancy, budget |
| urban_context | No | Relationship to surrounding city fabric |
| client_expectations | No | What the client hopes to achieve through design |

---

## Koolhaas's Five Theorems of Bigness

Use these as evaluation criteria:

### Theorem 1: The Scale Threshold
> "Beyond a certain critical mass, a building becomes a Big Building."

Bigness is not just large - it is a quantum beyond which architecture acquires entirely new properties. The threshold varies by context, but indicators include:
- Floor area typically exceeding 50,000-100,000 m²
- Vertical extent requiring multiple elevator zones
- Program complexity requiring internal navigation systems
- Occupancy exceeding that of small towns

### Theorem 2: The Elevator Effect
> "The elevator - with its potential to establish mechanical rather than architectural connections - already heralded the end of the classical repertoire."

When vertical distance requires mechanical conveyance, the relationship between floors becomes abstract. Each floor can be a different world. The building loses vertical coherence.

### Theorem 3: The Interior Regime
> "The distance between core and envelope increases to such an extent that the facade can no longer reveal what happens inside."

At a certain depth, the building develops internal conditions independent of exterior - its own climate, lighting, acoustics. The facade becomes decoration or marketing rather than expression of interior.

### Theorem 4: The Impossibility of Control
> "The project becomes multiple, fragmented, impossible - and therefore potentially much richer than the sum of its parts."

Bigness defeats the ambition of a single architectural gesture. No composition can unify it. Multiple architects, changing programs over time, and complex occupancies prevent coherent authorship.

### Theorem 5: Context Irrelevance
> "Bigness is no longer part of any urban tissue. It exists; at most, it coexists. Its subtext is fuck context."

Beyond a certain scale, the building does not respond to context - it *creates* context. It becomes an urban fact that others must respond to, not a good neighbor fitting in.

---

## Assessment Process

### Step 1: Scale Threshold Test

Does the project exceed the critical mass for its context?

| Metric | Below Threshold | At Threshold | Above Threshold |
|--------|----------------|--------------|-----------------|
| Floor area | <25,000 m² | 25,000-100,000 m² | >100,000 m² |
| Occupancy | <1,000 people | 1,000-10,000 people | >10,000 people |
| Program types | 1-3 related | 4-7 diverse | 8+ unrelated |
| Vertical zones | 1 elevator bank | 2-3 banks | 4+ banks/sky lobbies |
| Development timeline | <3 years | 3-7 years | >7 years |

**Score:** Count how many metrics are "Above Threshold" or "At Threshold"
- 0-1: Not Bigness - traditional architecture applies
- 2-3: Approaching Bigness - hybrid strategies needed
- 4-5: Confirmed Bigness - full Bigness regime applies

### Step 2: Theorem Application

For each theorem, assess whether it applies to this project:

| Theorem | Applies? | Evidence |
|---------|----------|----------|
| 1. Scale Threshold | Yes/No/Partial | [Describe why] |
| 2. Elevator Effect | Yes/No/Partial | [Describe vertical strategy] |
| 3. Interior Regime | Yes/No/Partial | [Describe facade-interior relationship] |
| 4. Control Impossibility | Yes/No/Partial | [Describe authorship complexity] |
| 5. Context Irrelevance | Yes/No/Partial | [Describe urban relationship] |

**Bigness Confirmation:** If 3+ theorems apply, the project is in the Bigness regime.

### Step 3: Strategic Implications

Based on assessment, identify what this means for the project:

**If Bigness applies:**
- Single architectural vision will be frustrated - plan for multiplicity
- Context negotiations are about power, not harmony
- Interior and exterior are separate design problems
- Program will change during design and construction
- Impact will be independent of design quality

**If Bigness does not apply:**
- Traditional architectural values can be pursued
- Contextual response is possible and appropriate
- Compositional unity is achievable
- Singular authorship can be maintained

---

## Output Format

```markdown
## Bigness Assessment: [Project Name]

### Project Overview
[Brief description of project including key metrics]

### Scale Threshold Analysis

| Metric | Value | Status |
|--------|-------|--------|
| Floor area | [X m²] | [Below/At/Above] |
| Occupancy | [X people] | [Below/At/Above] |
| Program types | [List] | [Below/At/Above] |
| Vertical organization | [Description] | [Below/At/Above] |
| Development timeline | [X years] | [Below/At/Above] |

**Threshold Score:** [X/5] - [Not Bigness / Approaching / Confirmed]

### Theorem Analysis

| Theorem | Verdict | Evidence |
|---------|---------|----------|
| Scale Threshold | [Y/N/P] | [Explanation] |
| Elevator Effect | [Y/N/P] | [Explanation] |
| Interior Regime | [Y/N/P] | [Explanation] |
| Control Impossibility | [Y/N/P] | [Explanation] |
| Context Irrelevance | [Y/N/P] | [Explanation] |

**Theorem Score:** [X/5] theorems apply

### Verdict

**Bigness Status:** [NOT BIGNESS / APPROACHING BIGNESS / CONFIRMED BIGNESS]

### Strategic Implications

[Based on verdict, what does this mean for the project?]

**For design:**
- [Implication 1]
- [Implication 2]
- [Implication 3]

**For client expectations:**
- [Implication 1]
- [Implication 2]

**For urban relationship:**
- [Implication 1]
- [Implication 2]

### Koolhaas Warning

> "[Relevant quote from Bigness essay]"
```

---

## Example

**Input:** "Assess the Hudson Yards development in New York City for Bigness."

**Output:**

## Bigness Assessment: Hudson Yards, New York City

### Project Overview
Hudson Yards is a $25 billion, 28-acre mixed-use development on Manhattan's West Side, built over active rail yards. It includes 18 million square feet of commercial and residential space, comprising office towers, residential buildings, a shopping mall, hotel, cultural facility (The Shed), public plaza, and observation deck (The Edge).

### Scale Threshold Analysis

| Metric | Value | Status |
|--------|-------|--------|
| Floor area | 1.67 million m² (18M sq ft) | **Above** |
| Occupancy | 125,000 workers + residents | **Above** |
| Program types | Office, residential, retail, hotel, cultural, dining, observation | **Above** |
| Vertical organization | Multiple supertall towers with sky lobbies | **Above** |
| Development timeline | 2012-2024+ (12+ years) | **Above** |

**Threshold Score:** 5/5 - CONFIRMED BIGNESS

### Theorem Analysis

| Theorem | Verdict | Evidence |
|---------|---------|----------|
| Scale Threshold | **Yes** | At 18 million square feet, this exceeds most city neighborhoods in built area |
| Elevator Effect | **Yes** | Multiple supertall towers require sky lobbies; vertical movement is mechanical system, not architectural experience |
| Interior Regime | **Yes** | The Shops at Hudson Yards is a mall with no relationship to exterior urbanism; office floors have no facade expression of interior |
| Control Impossibility | **Yes** | Multiple architects (KPF, SOM, Diller Scofidio + Renfro, others); program continues to evolve post-construction; no unified design vision despite attempt |
| Context Irrelevance | **Yes** | Hudson Yards does not respond to Hell's Kitchen or Chelsea context - it creates its own district that others must now respond to |

**Theorem Score:** 5/5 theorems apply

### Verdict

**Bigness Status:** CONFIRMED BIGNESS (Maximum)

### Strategic Implications

Hudson Yards is Bigness at its most pure - a private city built on a platform over infrastructure, with almost no connection to its surroundings except through carefully controlled entry points.

**For design:**
- The attempt to create unified character through Thomas Heatherwick's "Vessel" sculptural centerpiece was doomed - it cannot unify 28 acres of development
- Individual buildings by different architects function as fragments, not ensemble
- The "public" spaces are privately owned and controlled - a consequence of Bigness economics, not design failure

**For client expectations:**
- Related Companies achieved financial returns, not urban design prizes
- The criticism that Hudson Yards is "soulless" misunderstands Bigness - soul requires authorship, and Bigness defeats authorship
- The development succeeded on its own terms (investment returns, tenant occupancy) regardless of critical reception

**For urban relationship:**
- Hudson Yards is now a fact that the High Line, Chelsea, and Hell's Kitchen must accommodate
- It generates foot traffic, transit demand, and economic activity independent of whether it is "good" urbanism
- Future development in the area responds to Hudson Yards, not the historic context it replaced

### Koolhaas Warning

> "Bigness no longer needs the city: it competes with the city; it represents the city; it preempts the city; or better still, it is the city."

Hudson Yards is not a neighborhood in New York - it is an alternative to New York, enclosed and self-sufficient, that happens to share the same island.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Project seems big but metrics are unclear | Request specific data; use ranges if exact figures unavailable |
| Client disputes Bigness designation | Explain this is not criticism but accurate diagnosis; traditional expectations will lead to frustration |
| Project is approaching but not at Bigness | Identify which additional elements would push it across threshold; warn of hybrid challenges |
| Bigness seems good or bad | Redirect: Bigness is a condition, not a value. The question is what it enables and requires, not whether it is right |

---

## Integration

This skill is part of the **Rem Koolhaas** expert persona. It represents his theory that beyond a certain scale, architecture fundamentally changes - not in degree but in kind. Use it when scale seems to defeat conventional approaches.

Pairs well with:
- **retroactive-manifesto** when Bigness is already built and needs articulation
- **generic-city-diagnosis** when Bigness produces homogenized conditions