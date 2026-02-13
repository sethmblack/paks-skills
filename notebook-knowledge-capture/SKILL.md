---
name: notebook-knowledge-capture
description: 'Create and maintain personal or team knowledge bases that enable cross-domain synthesis over time. Apply Leonardo da Vinci''s notebook methodology: multi-domain pages, observation-annotation integra...'
license: MIT
metadata:
  version: 1.0.1530
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- notebook-knowledge-capture
- structure
- writing
---

# Notebook Knowledge Capture

Create and maintain personal or team knowledge bases that enable cross-domain synthesis over time. Apply Leonardo da Vinci's notebook methodology: multi-domain pages, observation-annotation integration, and iterative refinement over years.

---

## When to Use

- Setting up a personal knowledge management system
- User asks "How should I document this?"
- Building team knowledge bases or wikis
- Pattern of learning things and losing them
- Preparing for long-term projects requiring accumulated knowledge
- Request for "knowledge capture" or "documentation strategy"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| knowledge_domain | Yes | What kind of knowledge will be captured (technical, research, project-specific) |
| capture_frequency | No | How often new knowledge arrives (daily, weekly, per-project) |
| use_cases | No | How the knowledge will be used (reference, synthesis, sharing) |
| collaboration | No | Solo or team; if team, how many and what roles |
| existing_systems | No | Current tools or practices in use |

---

## The Four-Step Framework

Leonardo left approximately 7,000+ pages of notebooks over 40+ years. Only ~25% survive, yet they represent one of history's greatest knowledge capture achievements—enabling cross-domain synthesis that produced revolutionary insights in art, anatomy, engineering, and science.

### Step 1: Establish Structure

Design a notebook structure that enables both capture and retrieval:

**Core Principles:**
- **Multi-domain pages:** Leonardo's pages mixed anatomy sketches, mechanical designs, and philosophical notes. Don't over-categorize; connections emerge when diverse knowledge lives together.
- **Capture-first, organize-later:** Make capture frictionless. Heavy organization upfront kills capture; let structure emerge from content.
- **Temporal spine:** Date everything. The sequence of discoveries matters. Leonardo's notebooks can be dated; this enables tracing his evolving understanding.

**Structure Options:**

| Pattern | Best For | Description |
|---------|----------|-------------|
| **Daily Log** | High-frequency capture | Date-based entries, link to topic pages |
| **Zettelkasten** | Long-term synthesis | Atomic notes, dense linking, emergent structure |
| **Project Notebook** | Bounded projects | One notebook per project, archived at completion |
| **Topic Garden** | Reference material | Topic-organized, continuously updated |

**Leonardo's approach:** He maintained multiple notebooks simultaneously for different purposes (topology, anatomy, painting), but within each, content flowed freely across subjects.

### Step 2: Define Capture Workflow

Make capture so easy it happens without friction:

**Capture Triggers:**
- Something surprising or unexpected
- A solution to a problem (even if obvious later)
- A connection between two domains
- A question that emerged from work
- An error and what fixed it
- A technique or pattern worth remembering

**Capture Format:**
```
[Date] [Context tag]

## Observation
[What was seen/learned/discovered]

## Source
[Where this came from: experience, reading, conversation]

## Connections
[Related notes, if any come to mind]

## Questions
[What this raises, if anything]
```

**Leonardo's insight:** "All our knowledge has its origins in our perceptions." Capture observations, not just conclusions. The observation is the primary data; interpretations can be revised.

### Step 3: Create Cross-Referencing System

Enable finding connections you didn't know to look for:

**Linking Strategies:**
| Strategy | Description | When to Apply |
|----------|-------------|---------------|
| **Forward links** | Link from new note to related existing notes | During capture |
| **Backlinks** | System shows all notes linking to current note | Automatic (tool-dependent) |
| **Tags** | Topic labels that group notes | During capture + periodic review |
| **Index pages** | Curated entry points into topic clusters | Periodic creation |
| **Proximity** | Related notes physically/temporally near each other | Implicit in daily log style |

**The goal:** Serendipitous rediscovery. When working on problem X, stumble upon note Y that you forgot but is relevant.

**Leonardo's practice:** His notebooks show the same subjects revisited across years, each return adding depth. The physical proximity of diverse subjects on single pages enabled unexpected connections (water currents and hair, muscles and levers).

### Step 4: Schedule Synthesis Reviews

Capture without synthesis becomes a graveyard. Schedule regular review:

**Review Cadence:**

| Review Type | Frequency | Activity |
|-------------|-----------|----------|
| **Daily closure** | End of day | Quick scan of day's captures; add missing links |
| **Weekly review** | Weekly | Read week's notes; identify themes; create index entries |
| **Monthly synthesis** | Monthly | Look for patterns across weeks; write synthesis notes |
| **Quarterly retrospective** | Quarterly | Assess what's useful; prune what's not; evolve structure |

**Synthesis Activities:**
- Write "synthesis notes" that connect multiple observations
- Update index pages with new patterns
- Identify questions that multiple notes raise
- Flag notes that are now outdated
- Celebrate insights that proved valuable

**Leonardo's insight:** "Learning never exhausts the mind." But it does require integration. Raw capture is not knowledge; synthesized capture becomes wisdom.

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
## Knowledge Capture System Design

### Context
**Domain:** [What kind of knowledge]
**Frequency:** [How often new knowledge arrives]
**Users:** [Solo/team; roles]
**Use cases:** [How it will be used]

### Recommended Structure
**Pattern:** [Daily Log / Zettelkasten / Project Notebook / Topic Garden / Hybrid]
**Rationale:** [Why this pattern fits]

**Folder/Section Organization:**
```
[Suggested structure]
```

### Capture Workflow

**Triggers:** When to capture
- [Trigger 1]
- [Trigger 2]

**Template:**
```
[Capture format template]
```

**Tools:** [Recommended tools based on context]

### Cross-Referencing Strategy
| Strategy | Implementation |
|----------|---------------|
| [Strategy] | [How to do it] |

### Review Schedule
| Review | Frequency | Duration | Activity |
|--------|-----------|----------|----------|
| [Type] | [When] | [Time] | [What to do] |

### Getting Started
1. [First step]
2. [Second step]
3. [Third step]

### Evolution Plan
**After 1 month:** [Assessment/adjustment]
**After 3 months:** [Assessment/adjustment]
**After 1 year:** [Assessment/adjustment]
```

---

## Constraints

- Do not over-design; start simple and evolve
- Do not prioritize organization over capture
- Do not expect perfect structure from day one
- Acknowledge that different knowledge domains may need different approaches
- Recognize when existing systems should be evolved vs. replaced
- Accept that some captured knowledge will prove useless (that's okay)

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

**Input:**
```
knowledge_domain: DevOps and SRE practices, incident learnings, architecture decisions
capture_frequency: Daily operational learnings, weekly project discoveries
use_cases: Personal reference, onboarding new team members, incident post-mortems
collaboration: Team of 5 SREs, but primary user is capturing personal knowledge
existing_systems: Confluence (team wiki, underused), Slack bookmarks (chaotic)
```

**Output:**

## Knowledge Capture System Design

### Context
**Domain:** DevOps/SRE practices, incidents, architecture decisions
**Frequency:** Daily operational, weekly project
**Users:** Primary: individual SRE. Secondary: team of 5 for sharing
**Use cases:** Personal reference, onboarding, post-mortems

### Recommended Structure
**Pattern:** Hybrid - Daily Log (for capture) + Topic Garden (for reference)
**Rationale:** Daily operational work produces frequent small learnings; topic pages allow accumulation into coherent references. Confluence stays for official team docs; personal system for working knowledge.

**Folder/Section Organization:**
```
/log/
  2026-01-18.md
  2026-01-19.md
  ...
/topics/
  kubernetes/
    resource-limits.md
    debugging-pods.md
  postgres/
    query-optimization.md
  incidents/
    2026-01-incident-db-failover.md
/indexes/
  troubleshooting-playbooks.md
  architecture-decisions.md
  onboarding-guide.md
```

### Capture Workflow

**Triggers:** When to capture
- Fixed something non-obvious
- Learned a command or technique
- Encountered surprising behavior
- Made or discovered an architecture decision
- Had an insight during an incident
- Read something worth remembering

**Template:**
```markdown
## [Brief title]
*[Date] [Tags: kubernetes, postgres, incident, architecture, etc.]*

### What happened / What I learned
[2-5 sentences]

### How I figured it out / Source
[Command sequence, link, colleague name]

### Connections
[[Related topic page]] [[Related incident]]

### Questions this raises
- [Optional: what to investigate further]
```

**Tools:** Obsidian (local, markdown, backlinks, graph view). Obsidian Sync for backup. Keep separate from team Confluence; sync selected content to Confluence when mature.

### Cross-Referencing Strategy
| Strategy | Implementation |
|----------|---------------|
| Forward links | [[double bracket]] syntax during capture |
| Backlinks | Obsidian automatic; review in sidebar |
| Tags | Front-matter tags for filtering |
| Index pages | Manually curated in /indexes/ |

### Review Schedule
| Review | Frequency | Duration | Activity |
|--------|-----------|----------|----------|
| Daily closure | End of shift | 5 min | Add links to day's captures, tag |
| Weekly review | Friday | 20 min | Update topic pages from week's learnings; identify patterns |
| Monthly synthesis | First Monday | 1 hr | Write synthesis notes; update indexes; share 1 thing to team |
| Quarterly retro | Quarterly | 2 hr | Prune dead notes; evolve structure; assess what's useful |

### Getting Started
1. Install Obsidian, create vault with folder structure above
2. Create first log entry today with anything you learned this week
3. Set calendar reminder for Friday review
4. After 1 week, create first topic page from accumulated log entries
5. After 1 month, assess: what's working? What's friction?

### Evolution Plan
**After 1 month:** Assess capture friction. Are you actually capturing daily? If not, simplify template. If yes, start building first index page.
**After 3 months:** Review topic pages. Are they useful references? Identify your most-referenced pages; consider sharing with team via Confluence.
**After 1 year:** Knowledge base should have 200+ notes. Graph view becomes valuable for seeing connections. Consider building an onboarding guide from accumulated knowledge.

---

## Integration

This skill is part of the **Leonardo da Vinci** expert persona. Use it when establishing systems for long-term knowledge accumulation.

Leonardo's notebooks enabled his unique cross-domain genius. The same observations about water flow that informed his paintings also informed his engineering designs. Knowledge captured systematically compounds over time. "Learning never exhausts the mind"—but only if learning is retained and synthesized.