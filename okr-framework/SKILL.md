---
name: okr-framework
description: 'Implement Objectives and Key Results for goal-setting, alignment, and execution tracking. Based on Andy Grove''s methodology developed at Intel: "If you don''t know where you''re going, you won''t get ...'
license: MIT
metadata:
  author: sethmblack
  version: 1.0.1545
keywords:
- okr-framework
- transformation
- writing
---

# OKR Framework

Implement Objectives and Key Results for goal-setting, alignment, and execution tracking. Based on Andy Grove's methodology developed at Intel: "If you don't know where you're going, you won't get there."

---

## When to Use

- Setting goals for a team, department, or organization
- Annual or quarterly planning
- Team alignment is lacking
- Execution tracking is unclear
- Goals exist but are not driving behavior
- Question of "how do we measure success?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| scope | Yes | What entity is setting OKRs (team, department, company) |
| time_horizon | Yes | Period for these OKRs (quarter, year, other) |
| strategic_context | No | Higher-level goals or strategy these OKRs support |
| current_goals | No | Existing goals or OKRs being replaced/refined |
| known_priorities | No | Key initiatives or focus areas |

---

## Grove's OKR Framework

### What Are OKRs?

OKRs answer two questions:
1. **Objective:** Where do I want to go?
2. **Key Results:** How will I know if I am getting there?

> "The idea behind OKRs is simple: if you don't know where you're going, you won't get there."

### Core Principles

#### 1. Objectives Are Qualitative Destinations

**Good objectives are:**
- Significant - meaningful achievement, not busy work
- Concrete - clear enough to guide action
- Action-oriented - drive behavior, not describe states
- Inspirational - motivate rather than merely direct

**Objective template:** Start with a verb (Launch, Achieve, Transform, Build, Establish)

**Examples:**
- "Launch a world-class mobile experience"
- "Transform our sales process for enterprise clients"
- "Establish market leadership in [segment]"

#### 2. Key Results Are Quantitative Milestones

**Good key results are:**
- Specific - no ambiguity about what counts
- Time-bound - achievable within the OKR period
- Measurable - binary (done/not done) or numeric
- Ambitious but achievable - stretch goals, 60-70% achievement rate expected

**Key result template:** [Metric] from [X] to [Y] by [date]

**Examples:**
- "Increase mobile conversion rate from 2% to 4%"
- "Reduce average sales cycle from 90 days to 60 days"
- "Achieve 40% market share in [segment] (from 25%)"

#### 3. Less Is More

> "Keep your number of objectives small. If you focus on everything, you focus on nothing."

**Guidelines:**
- 3-5 objectives per entity per period (maximum)
- 2-5 key results per objective
- If you have more than 5 objectives, you lack focus

#### 4. Cascade, Don't Mandate

OKRs should cascade, meaning one level's key results become the next level's objectives:

```
Company OKR
   Objective: Achieve market leadership
   Key Result: Reach $100M ARR
           ↓
Department OKR
   Objective: Reach $100M ARR (cascaded from above)
   Key Result: Close 50 enterprise deals at $500K average
           ↓
Team OKR
   Objective: Close 50 enterprise deals
   Key Result: Build pipeline of 200 qualified opportunities
```

#### 5. Separate from Compensation

Grove explicitly separated OKRs from compensation to encourage ambitious goal-setting:

> "OKRs should be set for a relatively short period of time... A few well-chosen OKRs are what make the system work."

If people are punished for missing OKRs, they will set easily-achievable goals. The system breaks.

#### 6. Short Cycles

- Annual OKRs provide direction
- Quarterly OKRs drive execution
- Monthly check-ins track progress

---

## OKR Development Process

### Step 1: Clarify Strategic Context

Before writing OKRs, understand:

**Questions:**
- What is the higher-level objective these OKRs support?
- What are the key constraints (resources, time, dependencies)?
- What must be true at the end of this period for success?

**Context capture:**
| Element | Description |
|---------|-------------|
| Supporting strategy | [What higher-level goal do these OKRs serve?] |
| Key constraints | [What limits what we can do?] |
| Success definition | [What does winning look like?] |

### Step 2: Draft Objectives

Generate candidate objectives:

| Candidate Objective | Significance | Clarity | Alignment | Keep? |
|--------------------|--------------|---------|-----------|-------|
| [Objective 1] | [High/Med/Low] | [Clear/Fuzzy] | [With strategy?] | [Y/N] |
| [Objective 2] | | | | |

**Reduce to 3-5:** If more than 5 candidates remain, you lack focus. Force prioritization.

**Objective quality check:**
- [ ] Starts with an action verb
- [ ] Describes a meaningful destination
- [ ] Inspires the team
- [ ] Fits within the time horizon
- [ ] Aligns with strategic context

### Step 3: Define Key Results

For each objective, define 2-5 key results:

| Objective | Key Result | Baseline | Target | Stretch? | Measurable? |
|-----------|-----------|----------|--------|----------|-------------|
| [Obj 1] | [KR 1.1] | [Current] | [Goal] | [Y/N] | [Y/N] |
| | [KR 1.2] | | | | |

**Key result quality check:**
- [ ] Specific metric identified
- [ ] Current baseline known
- [ ] Target is ambitious (expect 60-70% achievement)
- [ ] Achievable within period (with effort)
- [ ] Completion can be objectively verified

### Step 4: Test the OKR Set

**Alignment test:** Do the key results, if achieved, guarantee the objective is met?

**Coverage test:** Are there important outcomes not captured by key results?

**Conflict test:** Do any OKRs conflict with each other?

**Ambition test:** If everything is easily achievable, goals are not ambitious enough.

**Focus test:** Can a new team member understand priorities from these OKRs alone?

### Step 5: Establish Cadence

Define how OKRs will be tracked and reviewed:

| Activity | Frequency | Owner | Format |
|----------|-----------|-------|--------|
| OKR setting | [Quarterly/Annual] | [Who] | [Meeting/Doc] |
| Progress check | [Weekly/Biweekly] | [Who] | [Meeting/Dashboard] |
| Full review | [End of period] | [Who] | [Retrospective] |

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
## OKRs: [Entity Name] - [Period]

### Strategic Context

**Supporting strategy:** [Higher-level goal these OKRs serve]

**Period:** [Q1 2024, FY2024, etc.]

**Success definition:** [What winning looks like at end of period]

---

### Objective 1: [Objective Statement]

| Key Result | Baseline | Target | Owner | Status |
|------------|----------|--------|-------|--------|
| [KR 1.1] | [Current] | [Goal] | [Name] | [Not started/On track/At risk/Complete] |
| [KR 1.2] | [Current] | [Goal] | [Name] | |
| [KR 1.3] | [Current] | [Goal] | [Name] | |

**Why this objective matters:** [Brief rationale]

---

### Objective 2: [Objective Statement]

| Key Result | Baseline | Target | Owner | Status |
|------------|----------|--------|-------|--------|
| [KR 2.1] | [Current] | [Goal] | [Name] | |
| [KR 2.2] | [Current] | [Goal] | [Name] | |

**Why this objective matters:** [Brief rationale]

---

### Objective 3: [Objective Statement]

| Key Result | Baseline | Target | Owner | Status |
|------------|----------|--------|-------|--------|
| [KR 3.1] | [Current] | [Goal] | [Name] | |
| [KR 3.2] | [Current] | [Goal] | [Name] | |

**Why this objective matters:** [Brief rationale]

---

### Cascade Structure

[If applicable, show how these OKRs cascade from or to other levels]

```
[Higher level objective]
    ↓
[This level's objective] ← You are here
    ↓
[Lower level objectives these enable]
```

---

### Tracking Cadence

| Activity | Frequency | Owner | Format |
|----------|-----------|-------|--------|
| Progress update | [Weekly] | [Name] | [Slack/Meeting] |
| Review meeting | [Monthly] | [Name] | [30 min team meeting] |
| Period retrospective | [End of quarter] | [Name] | [60 min retrospective] |

---

### OKR Quality Assessment

| Test | Result | Notes |
|------|--------|-------|
| Focus (3-5 objectives) | [Pass/Fail] | |
| Alignment (KRs guarantee objective) | [Pass/Fail] | |
| Ambition (stretch goals) | [Pass/Fail] | |
| Measurability (all KRs quantifiable) | [Pass/Fail] | |
| Coverage (key outcomes captured) | [Pass/Fail] | |

---

### Grove Principle

> "[Relevant Grove quote about goal-setting, focus, or execution]"
```

---

## Constraints

- Do not create more than 5 objectives; if more seem necessary, force prioritization
- Key results must be measurable; avoid subjective assessments
- OKRs are for direction and alignment, not performance review
- Achieving 100% of OKRs suggests goals were not ambitious enough
- OKRs should focus on outcomes, not activities (what to achieve, not what to do)

---

## Common Mistakes to Avoid

| Mistake | Why It's a Problem | Correction |
|---------|-------------------|------------|
| Too many objectives | Dilutes focus | Force to 3-5 maximum |
| Key results are activities | Confuses doing with achieving | Reframe as outcomes |
| Sandbagging (easy targets) | Defeats purpose of stretch | Set 60-70% achievability |
| Annual-only OKRs | Too long for meaningful tracking | Add quarterly OKRs |
| No baseline | Cannot measure progress | Establish current state first |
| Tying to compensation | Discourages ambition | Separate OKRs from bonuses |
| Set and forget | No behavior change | Establish regular cadence |

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Cannot measure key result | Find proxy metric or reframe KR; if truly unmeasurable, question if it matters |
| Objective too vague | Ask "what would we see if this succeeded?" |
| Too many priorities | Force stack rank; something must be #1 |
| Team cannot influence key result | Reframe to what team can control |
| Inherited OKRs don't make sense | Challenge upstream; alignment requires understanding |

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

**Input:** "We're an engineering team of 12 people. Our company objective is to 'become the market leader in our category.' We need Q1 OKRs that support this. We've been struggling with reliability and shipping speed."

**Output:**

## OKRs: Engineering Team - Q1 2024

### Strategic Context

**Supporting strategy:** Company objective to become market leader in category

**Period:** Q1 2024 (January - March)

**Success definition:** By end of Q1, we ship faster than competitors and our reliability enables customer confidence

---

### Objective 1: Ship features at industry-leading velocity

| Key Result | Baseline | Target | Owner | Status |
|------------|----------|--------|-------|--------|
| Reduce average cycle time from commit to production | 5 days | 1 day | Platform lead | Not started |
| Ship 15 customer-requested features (from backlog) | 0 | 15 | Product eng lead | Not started |
| Achieve 0 rollbacks due to quality issues | 2/month avg | 0 in Q1 | QA lead | Not started |

**Why this objective matters:** Market leadership requires shipping faster than competitors. Our current 5-day cycle time is uncompetitive. We cannot lead the market if we cannot ship.

---

### Objective 2: Achieve reliability that builds customer trust

| Key Result | Baseline | Target | Owner | Status |
|------------|----------|--------|-------|--------|
| Maintain 99.9% uptime (< 8.7 hours downtime in quarter) | 99.2% | 99.9% | SRE lead | Not started |
| Reduce P1 incidents from 4/month to 0 | 4/month | 0 | Engineering manager | Not started |
| Achieve <100ms p95 latency on core API endpoints | 250ms | 100ms | Backend lead | Not started |

**Why this objective matters:** We cannot be market leader if customers do not trust us. Reliability issues drive churn and damage reputation. Enterprise customers require demonstrated reliability.

---

### Objective 3: Build engineering team capacity for market leadership

| Key Result | Baseline | Target | Owner | Status |
|------------|----------|--------|-------|--------|
| Hire and onboard 3 senior engineers | 12 team members | 15 team members | Engineering manager | Not started |
| Reduce engineer time spent on incidents from 30% to 10% | 30% | 10% | SRE lead | Not started |
| Achieve 100% of team trained on new CI/CD platform | 0% | 100% | Platform lead | Not started |

**Why this objective matters:** We cannot sustain market-leading velocity with current capacity and firefighting load. Hiring and reducing toil are prerequisites for the other objectives.

---

### Cascade Structure

```
Company: Become market leader in category
    ↓
Engineering: Ship at industry-leading velocity + Achieve trusted reliability
    ↓
[Squad-level OKRs would cascade from here]
```

---

### Tracking Cadence

| Activity | Frequency | Owner | Format |
|----------|-----------|-------|--------|
| KR metric update | Weekly | KR owners | Slack channel update |
| OKR review | Bi-weekly | Engineering manager | 30 min team meeting |
| Q1 retrospective | End of March | Engineering manager | 90 min retrospective |

---

### OKR Quality Assessment

| Test | Result | Notes |
|------|--------|-------|
| Focus (3-5 objectives) | Pass | 3 objectives |
| Alignment (KRs guarantee objective) | Pass | KRs are measurable proof of objectives |
| Ambition (stretch goals) | Pass | 99.9% uptime and 1-day cycle time are ambitious |
| Measurability (all KRs quantifiable) | Pass | All KRs have clear metrics |
| Coverage (key outcomes captured) | Pass | Velocity, reliability, and capacity all addressed |

---

### Grove Principle

> "Move towards long term plans using short-term Objectives and corresponding Key Results. Cascade OKRs across organizations, so one manager's key results might make up the objectives of their direct reports."

These Q1 OKRs break the company's market leadership goal into engineering-specific, time-bound milestones. If achieved, they will demonstrably contribute to market leadership. If missed, the shortfall will be immediately visible and actionable.

---

## Integration

This skill is part of the **Andy Grove** expert persona. Use it when teams or organizations need clear goal-setting and alignment. It pairs well with:
- **high-output-management-audit** for ensuring the organization can execute OKRs
- **strategic-inflection-point-diagnosis** to ensure OKRs aim at the right strategy
- **10x-force-analysis** to understand external forces OKRs must address