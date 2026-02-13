---
name: six-page-memo
description: Structure complex proposals, strategic decisions, and business cases using narrative prose instead of bullet points. This forces complete thinking and eliminates the logical gaps that slide decks h...
license: MIT
metadata:
  version: 1.0.1915
  author: sethmblack
keywords:
- six-page-memo
- storytelling
- writing
---

# Six-Page Memo

Structure complex proposals, strategic decisions, and business cases using narrative prose instead of bullet points. This forces complete thinking and eliminates the logical gaps that slide decks hide.

---

## When to Use

- Complex proposal that needs executive buy-in
- Strategic decision requiring thorough analysis
- Business case that needs clear argumentation
- Request to "write this as a narrative" or "structure this properly"
- Replacing a slide deck with substance
- Any situation where bullet points hide sloppy thinking

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| topic | Yes | What the memo is about |
| key_points | No | Main arguments or decisions needed |
| data | No | Supporting evidence or metrics |
| recommendation | No | What action is being proposed |

---

## The Philosophy

### Why Narrative, Not Bullets

"PowerPoint-style presentations somehow give permission to gloss over ideas, flatten out any sense of relative importance, and ignore the interconnectedness of ideas."

Bullet points let you get away with fragments. They hide logical gaps. They don't require you to explain how A connects to B. They create the illusion of structure without the reality of thought.

Complete sentences force complete thinking. If you can't write a clear sentence explaining your reasoning, you don't actually understand your reasoning.

### The Amazon Practice

At Amazon, executives do not present PowerPoints. Instead, someone prepares a six-page narrative memo. Meetings begin with 15-30 minutes of silent reading. Everyone reads the memo together, then discussion happens.

"The reason writing a good 4 page memo is harder than 'writing' a 20 page PowerPoint is because the narrative structure of a good memo forces better thought and better understanding of what's more important than what."

### The Silent Reading Ritual

Why read silently together rather than pre-read?

1. **Ensures everyone actually reads it** - No faking having read it
2. **Fresh perspective** - Read it with fresh eyes, together
3. **Level playing field** - Fast readers and slow readers on equal footing
4. **Focused attention** - No phones, no multitasking, just the memo
5. **Immediate discussion** - Questions while content is fresh

---

## Memo Structure

### Standard Six-Page Structure

**Page 1: Introduction and Context**
- What is this memo about?
- Why does this matter now?
- What decision or action is needed?

**Pages 2-3: Current State Analysis**
- Where are we today?
- What are the key facts and data?
- What has changed or is changing?

**Pages 4-5: Proposal and Reasoning**
- What specifically is being proposed?
- Why is this the right approach?
- What alternatives were considered and rejected?
- What are the risks and mitigations?

**Page 6: Recommendation and Next Steps**
- Clear recommendation
- Specific actions requested
- Timeline and milestones
- Success metrics

### Alternative: PR/FAQ Structure

For new products or initiatives, the Working Backwards PR/FAQ format may be more appropriate. See the `working-backwards-prfaq` skill.

---

## Writing Guidelines

### Sentence Craft

- **Complete sentences only** - No fragments, no bullets
- **Active voice** - "We will launch" not "The launch will be done"
- **Specific numbers** - "$4.2M investment" not "significant investment"
- **Causal connections** - Explain why each point leads to the next
- **One idea per paragraph** - Clear topic sentences

### Structure Craft

- **Logical flow** - Each section builds on the previous
- **Explicit transitions** - "Therefore," "However," "As a result of this,"
- **Parallel construction** - Similar ideas in similar formats
- **Clear headings** - Signal what each section covers
- **Front-load conclusions** - Don't bury the recommendation

### What to Avoid

- Bullet points (except for truly parallel lists)
- Jargon without definition
- Assertions without evidence
- Hand-waving ("we believe," "it seems," "should be fine")
- Hidden assumptions
- Logical leaps

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
## [Memo Title]

**Author:** [Name]
**Date:** [Date]
**Classification:** [Decision Request / Information / Proposal]

---

### Introduction

[1-2 paragraphs: What is this about? Why does it matter? What decision is needed?]

---

### Context and Background

[2-3 paragraphs: Current state. Key facts. What has changed?]

---

### Analysis

[3-4 paragraphs: Deep dive on the problem or opportunity. Data and evidence. What do we know and what do we not know?]

---

### Alternatives Considered

[2-3 paragraphs: What other options exist? Why were they rejected?]

---

### Proposal

[2-3 paragraphs: Specific recommendation. Clear actions. Why this is the right path?]

---

### Risks and Mitigations

[2 paragraphs: What could go wrong? How do we address it?]

---

### Resource Requirements

[1-2 paragraphs: What do we need to execute? People, budget, time?]

---

### Success Metrics

[1 paragraph: How will we know if this worked?]

---

### Recommendation and Next Steps

[1-2 paragraphs: Clear ask. Specific timeline. Who needs to do what?]

---

**Appendix (if needed):**
[Supporting data, detailed analysis, supplementary information]
```

---

## Constraints

- Maximum 6 pages (excluding appendix)
- No bullet points in the main narrative
- Every claim must be supported or clearly marked as assumption
- The recommendation must be explicit, not implied
- If you can't fill 6 pages, the thinking isn't complete
- If you need more than 6 pages, the thinking isn't clear

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

**Input:** "We need to propose expanding our engineering team from 50 to 75 people over the next year. Help me structure this as a memo."

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


## Engineering Team Expansion Proposal

**Author:** [Your Name]
**Date:** January 2026
**Classification:** Decision Request - Budget Approval

---

### Introduction

This memo proposes expanding the engineering team from 50 to 75 engineers over the next twelve months, requiring approximately $3.2M in additional annual compensation and $400K in recruiting costs. This expansion is necessary to deliver the three platform initiatives in our 2026 roadmap while maintaining our current product velocity. Without this investment, we will need to delay at least one major initiative by 6-9 months, creating competitive risk in the enterprise segment.

The decision requested is budget approval for 25 new engineering hires, with recruiting beginning in Q1 2026.

---

### Context and Background

Our engineering team has grown from 30 to 50 engineers over the past eighteen months while our product surface area has more than doubled. We now maintain three major product lines, serve customers across 12 time zones, and operate infrastructure that handles 50x the traffic of two years ago. Team productivity, measured by features shipped per engineer, has remained constant during this growth, suggesting healthy team dynamics. However, we are now fully allocated with no capacity for new initiatives.

The 2026 roadmap includes three strategic platform initiatives: enterprise SSO integration, real-time collaboration features, and the API platform. Each initiative was sized by engineering leads at 4-5 engineer-years of effort. With current capacity fully allocated to maintenance and incremental improvements, we have approximately 5 engineer-years of available capacity for new development in 2026. The math does not work without expansion.

Customer demand signals are clear. Enterprise SSO has been the number one requested feature for fourteen consecutive months. Collaboration features are table stakes for the enterprise segment we are targeting. The API platform represents our expansion strategy into the developer ecosystem. Each quarter of delay reduces our first-mover advantage and allows competitors to close the gap we have established.

---

### Analysis

We analyzed three approaches to delivering the 2026 roadmap: expanding the team, contracting portions of the work, and reducing scope. Each approach was evaluated on delivery timeline, quality risk, and long-term capability building.

The contractor approach was rejected for several reasons. Our platform requires deep context that takes 3-6 months to build. Contractors would spend half their engagement ramping up. More importantly, the initiatives we are building represent core capabilities we need to own long-term. Outsourcing would save short-term cost but create long-term dependency and quality risk.

Scope reduction was considered but rejected by the executive team. The competitive analysis presented in November showed that delaying any of the three initiatives would open significant vulnerability. Enterprise SSO delay loses the Acme Corp deal ($2.4M ARR). Collaboration delay loses the competitive differentiation that drove our last three enterprise wins. API platform delay surrenders the developer ecosystem opportunity to competitors already moving in this space.

The capacity gap is real and cannot be addressed through productivity improvements alone. Our engineers are already working at sustainable but high utilization. Pushing harder would increase turnover risk among our most experienced team members, creating a capability loss that would take years to recover.

---

### Alternatives Considered

We evaluated a slower hiring pace of 15 engineers rather than 25. This would deliver two of the three initiatives on time while delaying the API platform by two quarters. The financial savings would be approximately $1.5M in year one. However, the API platform delay was deemed unacceptable given competitive dynamics - three competitors have announced developer platforms in the past six months.

We also considered a phased approach: hire 15 in H1, evaluate, then hire 10 more in H2. This reduces risk if our roadmap changes but also reduces our ability to deliver. Recruiting in Q3-Q4 is historically 40% harder than Q1-Q2 due to candidate availability. A phased approach would likely result in 20 hires rather than 25, pushing us back toward the slower pace scenario.

The full expansion to 75 engineers represents the minimum viable team to execute the approved roadmap without unacceptable delays or quality compromises.

---

### Proposal

We propose authorizing 25 new engineering hires to bring the team from 50 to 75 over the next twelve months. Hiring would proceed in three waves: 10 engineers in Q1, 10 in Q2, and 5 in Q3. This front-loads hiring when candidate availability is highest and allows new engineers to ramp before the heaviest development phases of each initiative.

The new hires would be distributed as follows: 8 engineers for the enterprise SSO team, 8 for the collaboration features team, 6 for the API platform team, and 3 for platform infrastructure to support the increased development velocity. Each team would be led by an existing senior engineer promoted to tech lead, with the new hires filling senior and mid-level positions.

We are not proposing expanding engineering management. The current ratio of 8 engineers per manager can accommodate this growth. However, we may need to revisit this in late Q3 if span of control issues emerge.

---

### Risks and Mitigations

The primary risk is hiring quality degradation under volume pressure. Mitigation: We will not lower the hiring bar. Each candidate must pass the same five-interview loop with the same criteria. If we cannot find qualified candidates, we will delay hiring rather than compromise quality. This may result in fewer than 25 hires, which would require roadmap re-prioritization.

The secondary risk is integration challenges. Adding 25 people to a 50-person team is a 50% increase. Mitigation: We will extend onboarding from 2 weeks to 4 weeks, assign each new hire a dedicated buddy, and create team-specific documentation that doesn't currently exist. Engineering management will dedicate 20% of their time to onboarding support in Q1-Q2.

---

### Resource Requirements

Total investment requested: $3.6M in year one. This breaks down as: $3.2M in additional annual compensation (average fully-loaded cost of $128K per engineer), $400K in recruiting costs (agency fees, recruiting tools, candidate travel, signing bonuses).

Recruiting resources: We need one additional technical recruiter for six months to support this volume. Current recruiting capacity can handle 15-18 engineering hires per year; this plan requires 25.

Office space: Our current lease accommodates up to 80 employees. No expansion needed.

---

### Success Metrics

We will measure success on four dimensions. Hiring: 25 qualified engineers hired by September 30, 2026, with less than 10% first-year attrition. Delivery: All three platform initiatives launched by December 31, 2026, with quality metrics meeting or exceeding current standards. Productivity: Features shipped per engineer remains within 15% of current baseline during the growth period. Culture: Engineering NPS remains above 40 (currently 52) as measured in Q4 survey.

---

### Recommendation and Next Steps

We recommend approving the $3.6M investment to expand the engineering team from 50 to 75 over the next twelve months. This is the minimum investment required to execute the approved 2026 roadmap without unacceptable delays.

Requested actions: CFO approval of the budget by January 31. HR approval to open 25 requisitions by February 7. Recruiting kickoff meeting scheduled for February 14. First offers extended by March 15.

If this proposal is not approved, we need an executive decision on which of the three 2026 initiatives to delay or cancel. This decision should be made by February 15 to allow roadmap communication and team reallocation.

---

## Integration

This skill is part of the **Jeff Bezos** expert persona. Use it when proposals need rigorous structure, when slide decks are hiding weak thinking, or when decisions require the discipline of complete sentences.