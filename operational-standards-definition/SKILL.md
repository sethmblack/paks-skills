---
name: operational-standards-definition
description: Define the non-negotiable fundamentals that must be perfect every time—the QSC&V (Quality, Service, Cleanliness, Value) of your system.
version: 1.0.0
author: sethmblack
tags: [comedy, operational-standards-definition, writing]
---

# Operational Standards Definition

Define the non-negotiable fundamentals that must be perfect every time—the QSC&V (Quality, Service, Cleanliness, Value) of your system.

---

## Purpose

You help users identify and define the operational standards that cannot slip. Not everything needs to be excellent—but the basics must be perfect every single time. Your goal is to create clear, measurable, enforceable standards for the fundamentals that matter most.

---

## When to Use

Invoke this skill when users need to:
- Define SLOs, SLAs, or quality standards
- Establish non-negotiable requirements for a system or process
- Create quality gates for releases, deployments, or operations
- Prevent fundamentals from eroding over time
- Build consistent user experiences across touch points

**Trigger phrases:** "define standards," "quality metrics," "non-negotiables," "SLOs," "what must never fail," "baseline requirements"

---



## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| input_data | Yes | The primary data or content to analyze |
| context | No | Additional background or constraints (default: none) |
| output_format | No | Preferred format for results (default: structured markdown) |

## The QSC&V Framework

Apply these four dimensions to any system:

### Quality
The product or output must be consistently excellent.

**Questions to answer:**
- What does "correct output" look like?
- What defect rate is acceptable? (Hint: for basics, often zero)
- How do you verify quality before delivery?
- What quality metrics will you track?

**Examples:**
- API returns correct data (not just any data)
- Builds pass all tests (not just compile)
- Documentation is accurate (not just present)

### Service
The experience must be reliably good.

**Questions to answer:**
- What does the user/customer experience from start to finish?
- What response times are required?
- How do you handle errors or failures gracefully?
- What support experience should users expect?

**Examples:**
- Page loads in under 2 seconds
- Errors include actionable guidance
- Support responds within defined SLA

### Cleanliness
The environment and systems must be maintained.

**Questions to answer:**
- What technical debt is acceptable?
- How do you maintain system health over time?
- What monitoring and alerting is required?
- How do you prevent degradation?

**Examples:**
- No critical vulnerabilities older than 30 days
- Logs are clean (no ignored errors)
- Dashboards reflect true system state
- Dead code is removed, not commented

### Value
The exchange must be fair—users get clear benefit for their investment.

**Questions to answer:**
- What value does the user receive?
- Is the cost (time, money, effort) proportionate to benefit?
- How do you measure whether users find it valuable?
- What would make users choose an alternative?

**Examples:**
- Feature saves users measurable time
- Cost is competitive with alternatives
- Users actively choose this over workarounds

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

## Outputs
When defining operational standards:

```markdown
## Operational Standards: [System/Process Name]

### Quality Standards
| Standard | Metric | Target | Measurement |
|----------|--------|--------|-------------|
| [What] | [How measured] | [Target value] | [How/when measured] |

### Service Standards
| Standard | Metric | Target | Measurement |
|----------|--------|--------|-------------|
| [What] | [How measured] | [Target value] | [How/when measured] |

### Cleanliness Standards
| Standard | Metric | Target | Measurement |
|----------|--------|--------|-------------|
| [What] | [How measured] | [Target value] | [How/when measured] |

### Value Standards
| Standard | Metric | Target | Measurement |
|----------|--------|--------|-------------|
| [What] | [How measured] | [Target value] | [How/when measured] |

### Enforcement
- How standards are monitored
- What happens when standards are missed
- Who is responsible for maintaining standards
- How exceptions are handled

### Review Cadence
- How often standards are reviewed
- How standards are updated
- How new standards are added
```

---

## The Discipline

Standards only matter if enforced. Define:

1. **Regular Inspection** - How and when you verify compliance
2. **Clear Metrics** - Quantitative measures, not opinions
3. **Consequences for Failure** - What happens when standards slip
4. **Recognition for Excellence** - How you celebrate consistent quality

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient input data | Request specific additional information needed for analysis |
| Ambiguous requirements | Ask clarifying questions before proceeding |
| Conflicting constraints | Highlight the conflicts and ask for prioritization |
| Out of scope request | Explain the skill's boundaries and suggest alternatives |
| Incomplete analysis | Acknowledge limitations and indicate what additional inputs would help |

## Constraints

- Do not define standards that cannot be measured or enforced
- Do not make everything a standard—focus on fundamentals that truly matter
- Be specific enough to be actionable (not "high quality" but "P99 latency < 200ms")
- Consider the cost of enforcement—standards without enforcement are wishes
- Start with fewer standards and add, rather than starting comprehensive and cutting

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails |
|--------------|--------------|
| Too many standards | Nothing is prioritized, enforcement is impossible |
| Unmeasurable standards | "High quality" means different things to different people |
| Unenforced standards | Standards become suggestions, then jokes |
| Static standards | What was good enough yesterday may not be tomorrow |
| Standards without ownership | Nobody is responsible means nobody is responsible |

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

## Additional Notes

**Best practices:**
- Use this skill when the situation clearly matches its intended use cases
- Combine with related skills for comprehensive analysis
- Iterate on outputs if initial results don't fully meet requirements

**Common variations:**
- Adjust the depth of analysis based on available time and information
- Scale the approach for different levels of complexity
- Adapt the output format to audience needs

**When to skip this skill:**
- The situation doesn't match the core use cases
- Simpler approaches would be more appropriate
- Time constraints require faster methods

## Integration

This skill is part of a broader analytical framework. Use it when you need systematic analysis following this specific methodology.

**Works well with:**
- Other analytical skills for comprehensive evaluation
- Creative skills when generating solutions based on insights
- Strategic planning skills when acting on recommendations

**When to prefer this over alternatives:**
- The situation matches this skill's specific use cases
- You need the particular perspective this framework provides
- Other approaches haven't yielded satisfactory results

**Integration with expert personas:**
- This skill can be invoked as part of a larger analysis workflow
- Combine with domain-specific expertise for deeper insights
- Use iteratively for complex, multi-faceted problems

## Examples

**API Service:**
- Quality: 99.9% of requests return correct data
- Service: P99 latency < 200ms, clear error messages
- Cleanliness: Zero critical security vulnerabilities, alerts actionable
- Value: Developers can integrate in < 1 hour

**On-Call Operations:**
- Quality: All incidents correctly categorized and resolved
- Service: Acknowledge in 5 min, communicate every 30 min
- Cleanliness: Runbooks current, no recurring incidents
- Value: MTTR under SLA, postmortems within 48 hours

**Documentation:**
- Quality: Accurate, complete, tested instructions
- Service: Findable, searchable, well-organized
- Cleanliness: No stale content, broken links, or outdated screenshots
- Value: Users can self-serve without filing tickets

---

*If I had a brick for every time I've repeated Quality, Service, Cleanliness, and Value, I'd bridge the Atlantic. What are the fundamentals that must never slip in your system?*