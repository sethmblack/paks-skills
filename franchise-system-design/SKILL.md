---
name: franchise-system-design
description: Transform any successful process, platform, or solution into a replicable system that others can operate independently with consistent results.
license: MIT
metadata:
  version: 1.0.4046
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- escalation
- franchise-system-design
- transformation
- writing
---

# Franchise System Design

Transform any successful process, platform, or solution into a replicable system that others can operate independently with consistent results.

---

## Purpose

You help users take something that works and turn it into a franchise-ready system. The value isn't in the thing itself—it's in the operating system that produces consistent results everywhere. Your goal is to create systems so clear that anyone can succeed with them.

---

## When to Use

Invoke this skill when users need to:
- Scale a successful process or platform to multiple teams
- Document how something works for others to replicate
- Create self-service systems that reduce dependency on experts
- Standardize operations across locations, teams, or instances
- Build internal platforms that teams will actually adopt

**Trigger phrases:** "scale this," "replicate," "franchise model," "standardize for others," "make this self-service," "document for handoff"

---



## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| input_data | Yes | The primary data or content to analyze |
| context | No | Additional background or constraints (default: none) |
| output_format | No | Preferred format for results (default: structured markdown) |

## The Franchise Formula

Apply these five steps to systematize any successful operation:

### 1. Create the Playbook
Document exactly how to succeed—every step, every decision point, every common problem and solution.

**Questions to answer:**
- What does someone need to know on day one?
- What are the exact steps to get from start to finish?
- What decisions must be made, and what criteria guide them?
- What are the most common failure modes and how do you prevent them?

### 2. Make It Teachable
The system must be learnable by people without your expertise. If it requires genius, it doesn't scale.

**Questions to answer:**
- Can someone with basic competence learn this in reasonable time?
- Are there training materials, examples, or reference implementations?
- Is the documentation written for the learner, not the expert?
- What hands-on practice will solidify understanding?

### 3. Enforce Standards
Identify the non-negotiables—the basics that must be perfect every time. These are not optional.

**Questions to answer:**
- What quality gates must every instance pass?
- What standards, if violated, would damage the whole system?
- How will you detect and correct deviations?
- What happens when someone fails to meet standards?

### 4. Enable Operators
Give operators the system and get out of the way. Trust them to execute. Remove blockers.

**Questions to answer:**
- Do operators have everything they need to succeed independently?
- What decisions can operators make without escalation?
- How do you provide support without creating dependency?
- What does success look like for operators?

### 5. Improve Centrally, Deploy Everywhere
Improvements to the system benefit all instances. Central innovation, distributed execution.

**Questions to answer:**
- How do improvements flow to all operators?
- How do you gather feedback from the field?
- What's the mechanism for rolling out upgrades?
- How do you balance standardization with local adaptation?

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
When analyzing a system for franchise potential:

```markdown
## Franchise Assessment: [System Name]

### Current State
- What works well
- What depends on specific people or context
- Replication readiness (1-10)

### Franchise Blueprint

#### 1. The Playbook
- Core processes to document
- Decision frameworks needed
- Common problems and solutions

#### 2. Teachability Plan
- Training requirements
- Time to competence estimate
- Learning materials needed

#### 3. Non-Negotiable Standards
- Quality gates
- Compliance requirements
- Enforcement mechanisms

#### 4. Operator Enablement
- Self-service capabilities needed
- Support model
- Success metrics for operators

#### 5. Central Improvement System
- Feedback collection mechanism
- Upgrade deployment process
- Version management approach

### Recommended Actions
1. [Immediate action]
2. [Short-term action]
3. [Long-term action]
```

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

- Do not recommend franchising systems that are inherently non-replicable (require rare expertise, unique circumstances, or cannot be standardized)
- Always identify what must remain centralized vs. what can be distributed
- Be honest about the effort required—franchising done poorly is worse than not franchising
- Consider the operator's perspective, not just the franchisor's

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

**Platform Engineering:**
- The "franchise" is your internal platform
- Operators are the teams using it
- Playbook is your documentation and golden paths
- Standards are your security, reliability, and compliance requirements
- Central improvement is your platform team shipping enhancements

**Runbook Standardization:**
- The "franchise" is your operational procedure
- Operators are on-call engineers
- Playbook is the runbook itself
- Standards are the expected response times and escalation paths
- Central improvement is post-incident learnings rolled back into runbooks

**Internal Tools:**
- The "franchise" is your tool or service
- Operators are teams self-serving
- Playbook is your getting-started guide
- Standards are your API contracts and SLAs
- Central improvement is your release process

---

*The value isn't in the hamburger—it's in the system that produces consistent hamburgers everywhere. What's your hamburger, and what's your system?*