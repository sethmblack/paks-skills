---
name: extended-phenotype-mapping
description: Map the effects of replicators (genes, memes, cultural patterns, code) beyond their immediate containers into environmental modifications, artifacts, and actions at a distance. Understand how organ...
license: MIT
metadata:
  version: 1.0.3964
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- extended-phenotype-mapping
- structure
- writing
---

# Extended Phenotype Mapping

Map the effects of replicators (genes, memes, cultural patterns, code) beyond their immediate containers into environmental modifications, artifacts, and actions at a distance. Understand how organizations, teams, and systems express their "genes" through the things they build.

---

## When to Use

- Understanding how organizational culture manifests in artifacts and processes
- Analyzing documentation, tools, and infrastructure as expressions of underlying patterns
- Diagnosing why certain outcomes persist despite personnel changes
- User asks "Why does this artifact exist?" or "What does this tool reveal about the org?"
- Understanding parasitic manipulation (patterns that change host behavior for their benefit)
- Tracing how decisions in one place affect outcomes elsewhere

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| system | Yes | The organism, team, organization, or codebase to analyze |
| artifacts | No | Specific environmental modifications to examine |
| scope | No | How far to extend the analysis (immediate, local, distant) |

---

## Dawkins's Foundation

"An animal's behaviour tends to maximize the survival of the genes 'for' that behaviour, whether or not those genes happen to be in the body of the particular animal performing it."

Dawkins considers *The Extended Phenotype* (1982) his most important contribution to evolutionary biology. The core insight: genes don't just express themselves in the bodies of organisms. They express themselves in effects on the environment.

**Classic examples:**
- Beaver dams are expressions of beaver genes
- Spider webs are expressions of spider genes
- Bird nests are expressions of bird genes
- Caddis fly cases are expressions of caddis fly genes

The phenotype—the observable expression of genetic information—extends beyond the body into environmental modifications that affect the gene's survival chances.

**The radical extension:** Parasite genes express themselves in the behavior of their hosts. A liver fluke's genes express themselves in an ant's suicidal behavior (climbing grass to be eaten by sheep). The gene's phenotypic expression happens in another organism's body.

---

## The Extended Phenotype Framework

### Step 1: Identify the Replicators

What information patterns are being expressed?

**In organizations:**
- Cultural values and assumptions
- Standard practices and procedures
- Architectural patterns and decisions
- Team beliefs about what's important

**In software:**
- Configuration patterns
- Coding conventions
- Architectural assumptions
- Error handling philosophies

**Key question:** What "genes" does this system carry that might express themselves in its environment?

### Step 2: Map Immediate Phenotypic Effects

What does the replicator directly produce?

**Body-level expression:**
- In biology: physical traits
- In organizations: team structure, internal processes
- In software: the codebase itself

**List the direct products** of the replicator's activity.

### Step 3: Trace Extended Phenotypic Effects

Where do the replicator's effects extend beyond the immediate container?

**Environmental modifications:**
| Artifact | Replicator Expression | Distance from Source |
|----------|----------------------|---------------------|
| [Artifact] | [What pattern it expresses] | [How far from origin] |

**Categories of extension:**
- **Built artifacts:** Tools, documentation, infrastructure created
- **Modified environments:** Changed conditions in surrounding systems
- **Behavioral effects:** How other entities change their behavior
- **Standard setting:** Norms that spread to other teams/systems

### Step 4: Identify Action at a Distance

The most radical extended phenotypes: effects on other organisms/systems.

**Parasitic patterns:**
- Does any pattern in System A express itself by modifying System B's behavior?
- Are there "manipulated hosts" doing things that benefit patterns elsewhere?

**Mutualistic patterns:**
- Are there patterns that benefit multiple systems?
- Are there symbiotic artifacts that express genes from multiple sources?

### Step 5: Assess Phenotype Fitness

How do these extended phenotypic expressions affect replicator survival?

**For each extended phenotype:**
- Does it increase replicator copying (spread)?
- Does it increase replicator survival (persistence)?
- Does it increase replicator fidelity (accurate reproduction)?

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
## Extended Phenotype Map: [System Name]

### Replicator Identification
**Core replicators:**
- [Pattern/gene 1]: [What it encodes]
- [Pattern/gene 2]: [What it encodes]

### Immediate Phenotype (Body)
**Direct expressions:**
- [Internal structure or direct product 1]
- [Internal structure or direct product 2]

### Extended Phenotype (Environment)

#### Built Artifacts
| Artifact | Expresses | Function | Distance |
|----------|-----------|----------|----------|
| [Artifact] | [Which replicator] | [What it does] | [Immediate/Local/Distant] |

#### Environmental Modifications
| Modification | Expresses | Effect | Distance |
|--------------|-----------|--------|----------|
| [Change] | [Which replicator] | [Impact on environment] | [Immediate/Local/Distant] |

#### Action at a Distance
| Target System | Effect | Benefit to Replicator |
|---------------|--------|----------------------|
| [Other system] | [How its behavior changes] | [How this helps original replicator] |

### Parasitic/Mutualistic Patterns
[Any patterns that manipulate other systems or create mutual benefit]

### Phenotype Fitness Assessment
| Extended Phenotype | Survival Impact | Spread Impact | Notes |
|-------------------|-----------------|---------------|-------|
| [Artifact/effect] | [+/-/0] | [+/-/0] | [Why] |

### Implications
[What this mapping reveals about the system's nature and likely evolution]
```

---

## Extended Phenotype Categories

### Documentation as Phenotype
Documentation is not neutral description—it's phenotypic expression:
- What gets documented reveals what the team's "genes" consider important
- How it's documented reflects underlying assumptions about users
- What's missing reveals blind spots encoded in the culture

### Tooling as Phenotype
Tool choices express organizational genes:
- Technology stack reveals values (move fast vs. stability, innovation vs. compatibility)
- Internal tools show what problems the organization's "genes" prioritize
- Abandoned tools show selection pressure against certain patterns

### APIs as Phenotype
APIs are extended phenotypes affecting other systems:
- API design constrains how other teams can work (action at a distance)
- Breaking changes force adaptation in dependent systems (parasitic manipulation)
- Well-designed APIs create mutualistic relationships

### Process as Phenotype
Processes are behavioral phenotypes:
- Meeting structures express assumptions about decision-making
- Approval workflows express assumptions about trust and control
- Rituals (standups, retros) express cultural genes

---

## Constraints

- Extended phenotype analysis is descriptive, not teleological—effects weren't "designed," they were selected
- Not every artifact is phenotypic; some are environmental features not created by replicators
- Tracing causation at a distance is difficult; correlation isn't expression
- The analysis reveals what is, not what should be
- Multiple replicators may express through the same artifact (distinguish them)

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

**Input:** "Map the extended phenotypes of our platform team. They're a small team but seem to have outsized influence on how every other team operates."

**Output:**



**Why this works:**

This example demonstrates the key principles of the skill in action. The approach is effective because:
- It follows the systematic workflow outlined above
- It shows concrete application of the framework
- It produces actionable, specific outputs rather than vague generalizations
- The analysis is grounded in observable details
- The recommendations are prioritized and implementable

**Alternative applications:**

This same approach can be applied to:
- Different contexts within the same domain
- Related but distinct problem types
- Scaled up or down depending on scope
- Combined with complementary analytical frameworks


## Extended Phenotype Map: Platform Team

### Replicator Identification
**Core replicators:**
- **Efficiency meme:** "Standardization reduces cognitive load and enables scale"
- **Control meme:** "Guardrails prevent incidents; teams shouldn't have to think about infrastructure"
- **Craft meme:** "Clean abstractions are worth the investment"
- **Speed meme:** "Developer velocity is the primary metric"

### Immediate Phenotype (Body)
**Direct expressions:**
- Small, senior team (8 engineers)
- Strong internal documentation culture
- High code quality standards
- Long planning cycles before implementation
- "Golden path" philosophy

### Extended Phenotype (Environment)

#### Built Artifacts
| Artifact | Expresses | Function | Distance |
|----------|-----------|----------|----------|
| Internal PaaS | Control + Efficiency memes | Abstracts infrastructure from product teams | Local |
| CI/CD pipelines | Speed + Control memes | Enforces deployment standards | Local |
| Service template | Efficiency + Craft memes | Standardizes how services are built | Local |
| Monitoring dashboards | Control meme | Makes system behavior visible | Local |
| Tech radar | Efficiency + Craft memes | Controls technology choices | Distant |
| Architecture decision records | Craft meme | Preserves rationale, constrains future | Distant |

#### Environmental Modifications
| Modification | Expresses | Effect | Distance |
|--------------|-----------|--------|----------|
| Blocked cloud console access | Control meme | Product teams can't touch infrastructure directly | Distant |
| Required PR templates | Craft meme | Shapes how all engineers communicate changes | Distant |
| Deployment windows | Control meme | Restricts when anyone can ship | Distant |
| Approved language list | Efficiency meme | Constrains technology choices org-wide | Distant |

#### Action at a Distance
| Target System | Effect | Benefit to Replicator |
|---------------|--------|----------------------|
| Product Team A | Must use service template, can't customize | Standardization makes platform team's job easier |
| Product Team B | Deployment blocked outside windows | Reduces incident surface during low-coverage periods |
| All teams | Must request infrastructure changes through tickets | Control meme propagates; platform team remains essential |
| New hires | Learn platform team's patterns as "the way things are done" | Memes replicate into new hosts |

### Parasitic/Mutualistic Patterns

**Mutualistic:**
- Golden path genuinely accelerates teams that fit the pattern
- Standardized monitoring reduces debugging time for everyone
- Template services reduce boilerplate for all teams

**Parasitic:**
- Control patterns persist even when they slow down teams that need flexibility
- Approval processes benefit platform team's control meme at the expense of product team velocity
- Tech radar constrains innovation in ways that benefit standardization over experimentation

**Key insight:** The platform team's genes express themselves throughout the organization. Eight engineers influence how 200 engineers work—not through management authority, but through extended phenotype.

### Phenotype Fitness Assessment
| Extended Phenotype | Survival Impact | Spread Impact | Notes |
|-------------------|-----------------|---------------|-------|
| Service template | + | + | Teams adopt willingly; reduces their work |
| Deployment windows | + | 0 | Reduces incidents (survival) but teams don't spread it enthusiastically |
| Tech radar | + | - | Teams comply but resist; creates shadow IT pressure |
| Blocked console access | + | - | Protects platform team's role but generates resentment |

### Implications

**What this mapping reveals:**
1. Platform team wields influence far beyond their headcount through extended phenotype
2. Their artifacts literally shape how every other team works
3. Some phenotypes are mutualistic (service templates), others parasitic (approval bottlenecks)
4. The team's survival depends on these extended phenotypes—if removed, their role shrinks
5. Selection pressure: phenotypes that generate too much resistance will eventually be challenged

**Predictions:**
- Teams with atypical needs will create workarounds (shadow infrastructure)
- Platform team will defend control patterns even when they're costly
- Mutualistic phenotypes will strengthen; parasitic ones will face selection pressure
- New team members will inherit these patterns as "how things work"

**For intervention:**
- To change organizational behavior, target the extended phenotypes, not the platform team
- To reduce parasitic patterns, create alternative expressions that serve the same genes differently
- To accelerate change, help the platform team evolve their genes, not just their artifacts

*"An animal's behaviour tends to maximize the survival of the genes 'for' that behaviour, whether or not those genes happen to be in the body of the particular animal performing it."* The platform team's influence is exactly this: their cultural genes expressing themselves in other teams' behavior.

---

## Integration

This skill is part of the **Richard Dawkins** expert persona. Use it to understand how patterns express themselves beyond their immediate containers. It pairs with:
- **genes-eye-view-analysis** for identifying replicators and their interests
- **meme-propagation-analysis** for understanding cultural transmission
- **selection-pressure-analysis** (Darwin) for understanding what selects among phenotypes
- **cumulative-selection-argument** for explaining how extended phenotypes evolved