---
name: organizational-capability-assessment
description: Assess whether an organization's capabilities are suited for a specific innovation opportunity using the Resources-Processes-Priorities (RPP) framework.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.4618
repository: https://github.com/sethmblack/paks-skills
keywords:
- organizational-capability-assessment
- structure
- transformation
- writing
---

# Organizational Capability Assessment

Assess whether an organization's capabilities are suited for a specific innovation opportunity using the Resources-Processes-Priorities (RPP) framework.

**Token Budget:** ~750 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend organizational restructuring without sufficient context
- Guarantee innovation success based on capability assessment alone
- Apply RPP to justify harmful organizational practices

**If misapplied:** Explain that RPP diagnoses capability fit, not people problems. Resistance often reflects rational behavior given existing processes and priorities.

---

## When to Use

- User asks "Can our organization do this?"
- User asks "Why are we struggling with this initiative?"
- User asks "What's blocking this change?"
- User asks "Do we have the capability for this innovation?"
- New initiative faces unexpected resistance
- Talented teams fail at new types of work
- Considering acquisition vs internal development

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **opportunity** | Yes | The innovation or strategic initiative being assessed |
| **current_resources** | Yes | People, technology, equipment, cash, relationships |
| **current_processes** | Yes | How work gets done, decision-making patterns, workflows |
| **current_priorities** | Yes | What the organization values, how decisions get made |

---

## Workflow

### Step 1: Define the Opportunity's Requirements

Identify what the opportunity demands:
- What resources does it require?
- What processes would best serve it?
- What priorities would enable success?

### Step 2: Assess Resources

**Resources are things:** People, equipment, technology, product designs, brands, information, cash, and relationships. They can be hired/fired, bought/sold, depreciated/enhanced.

Evaluate:
- Do we have the right people with the right skills?
- Do we have the technology and equipment?
- Do we have the financial resources?
- Do we have the necessary relationships (suppliers, distributors, customers)?

### Step 3: Assess Processes

**Processes are patterns:** Interaction, coordination, communication, and decision-making patterns that transform resources into value.

Evaluate:
- Were our processes designed for this type of work?
- What does our development/delivery process optimize for?
- How do we make decisions and allocate resources?
- What are the embedded assumptions in our workflows?

### Step 4: Assess Priorities

**Priorities are standards:** The criteria by which employees judge whether something is attractive or important.

Evaluate:
- What does the organization consider "attractive" business?
- What margin thresholds are acceptable?
- What customer profiles get resources?
- What time horizons drive decisions?

### Step 5: Identify Capability Gaps

Compare requirements to current state:
- Where do resources, processes, or priorities misalign?
- Which gaps are addressable within current organization?
- Which gaps require structural change?

### Step 6: Recommend Path Forward

Based on gaps, recommend:
- Internal development (if gaps are resource-only)
- Process adaptation (if gaps are moderate)
- Separate organization (if processes and priorities fundamentally misaligned)
- Acquisition (if building capability would take too long)

---

## Outputs

### RPP Assessment Report

```markdown
## Organizational Capability Assessment: [Opportunity Name]

### Opportunity Requirements

| Dimension | Required for Success |
|-----------|---------------------|
| Resources | [What's needed] |
| Processes | [What would work best] |
| Priorities | [What must be valued] |

### Current Capability Assessment

#### Resources Assessment
| Resource Type | Current State | Gap |
|---------------|---------------|-----|
| People/Skills | [what we have] | [what's missing] |
| Technology | [what we have] | [what's missing] |
| Financial | [what we have] | [what's missing] |
| Relationships | [what we have] | [what's missing] |

**Resources verdict:** [Sufficient / Addressable gaps / Significant gaps]

#### Processes Assessment
| Process Area | Optimized For | Opportunity Needs |
|--------------|---------------|-------------------|
| Development | [current optimization] | [what opportunity needs] |
| Decision-making | [current pattern] | [what opportunity needs] |
| Resource allocation | [current pattern] | [what opportunity needs] |
| Customer interaction | [current pattern] | [what opportunity needs] |

**Processes verdict:** [Compatible / Adaptable / Fundamentally misaligned]

#### Priorities Assessment
| Priority Dimension | Current Standard | Opportunity Requirement |
|--------------------|------------------|------------------------|
| Margin thresholds | [current] | [required] |
| Customer profile | [who we value] | [who we'd need to serve] |
| Time horizon | [how we think] | [what opportunity needs] |
| Risk tolerance | [current] | [required] |

**Priorities verdict:** [Aligned / Adjustable / Conflicting]

### Capability Gap Summary

| Gap Type | Severity | Addressable In-House? |
|----------|----------|----------------------|
| [Gap 1] | [High/Med/Low] | [Yes/Partially/No] |
| [Gap 2] | [High/Med/Low] | [Yes/Partially/No] |

### Recommendation

**Path:** [Internal Development | Process Adaptation | Separate Organization | Acquisition]

**Rationale:** [Why this path given the gaps identified]

**If pursuing internally, changes required:**
1. [Specific change 1]
2. [Specific change 2]
3. [Specific change 3]

**If separate organization needed:**
- Different processes required: [what]
- Different priorities required: [what]
- Autonomy level required: [what]

### Typical Failure Patterns to Avoid

For this type of initiative, organizations commonly fail by:
- [Pattern 1 - how current RPP would defeat the initiative]
- [Pattern 2 - how current RPP would defeat the initiative]

### Success Indicators

The initiative is on track if:
- [Leading indicator 1]
- [Leading indicator 2]
- [Leading indicator 3]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Blaming people for failure | Redirect to processes and priorities - rational people behave rationally given their incentives |
| Resources-only thinking | Emphasize that great resources fail without appropriate processes and priorities |
| Unclear current state | Request more detail on how work gets done and what gets valued |
| Resistance framed as irrationality | Explain that resistance usually reflects rational behavior given existing RPP |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "Can our traditional bank build a successful digital-only challenger brand?"

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


## Organizational Capability Assessment: Digital-Only Bank Brand

### Opportunity Requirements

| Dimension | Required for Success |
|-----------|---------------------|
| Resources | Digital product talent, modern tech stack, brand-building capability |
| Processes | Rapid iteration, product-led development, minimal approval layers |
| Priorities | Customer acquisition over short-term profit, digital-first metrics, tolerance for cannibalization |

### Current Capability Assessment

#### Resources Assessment
| Resource Type | Current State | Gap |
|---------------|---------------|-----|
| People/Skills | Branch-focused talent, IT as support function | Need digital-native product and engineering |
| Technology | Legacy core systems, batch processing | Need real-time, API-first architecture |
| Financial | Substantial capital reserves | Sufficient but allocation process may block |
| Relationships | Strong with regulators, traditional vendors | Need fintech partnerships, developer community |

**Resources verdict:** Addressable gaps - can be hired/built but takes time

#### Processes Assessment
| Process Area | Optimized For | Opportunity Needs |
|--------------|---------------|-------------------|
| Development | Waterfall, long cycles, extensive QA | Agile, continuous deployment, fast experimentation |
| Decision-making | Committee-based, risk-averse, documented | Empowered teams, speed, acceptable failure |
| Resource allocation | Annual budgets, justified ROI | Flexible funding, bet-based investment |
| Customer interaction | Branch relationships, phone support | Digital-first, async, automated |

**Processes verdict:** Fundamentally misaligned - designed for reliability and compliance, not speed and experimentation

#### Priorities Assessment
| Priority Dimension | Current Standard | Opportunity Requirement |
|--------------------|------------------|------------------------|
| Margin thresholds | High NIM expected | Willing to accept lower margins for growth |
| Customer profile | Established, high-balance | Young, mobile-first, may have lower balances |
| Time horizon | Quarterly/annual targets | Multi-year growth investment |
| Risk tolerance | Near-zero tolerance for incidents | Tolerance for controlled failures |

**Priorities verdict:** Conflicting - current priorities would starve the digital initiative of resources and patience

### Capability Gap Summary

| Gap Type | Severity | Addressable In-House? |
|----------|----------|----------------------|
| Technology stack | High | Partially - can modernize but slow |
| Development processes | High | No - core bank processes optimized for different outcomes |
| Priority conflicts | High | No - cannibalization concerns will win resource battles |
| Talent gaps | Medium | Yes - can hire if prioritized |

### Recommendation

**Path:** Separate Organization

**Rationale:** The processes and priorities required for digital success fundamentally conflict with those that make the core bank successful. Attempting to build this internally will result in either (a) the initiative being starved of resources, or (b) the initiative being forced to adopt bank processes that destroy its competitiveness.

**If separate organization needed:**
- Different processes required: Agile development, empowered teams, fast failure cycles
- Different priorities required: Growth over profit, customer acquisition metrics, cannibalization tolerance
- Autonomy level required: Independent P&L, separate tech stack, ability to make decisions without bank approval

### Typical Failure Patterns to Avoid

For this type of initiative, banks commonly fail by:
- Staffing with internal transfers who bring old processes: Must hire digital-native talent externally
- Requiring compliance review cycles designed for different products: Must streamline for digital
- Measuring against core bank metrics: Must have different success criteria for 3+ years

### Success Indicators

The initiative is on track if:
- Separate team with own budget and metrics established
- Can ship product changes weekly, not quarterly
- Leadership protecting initiative from core bank "help"

---

## Integration

This skill applies Clayton Christensen's RPP (Resources-Processes-Priorities) framework. Remember: a surprising number of innovations fail not because of technological flaws or market readiness, but because responsibility was given to organizations whose capabilities were not suited to the task. Companies become constrained by their competencies.