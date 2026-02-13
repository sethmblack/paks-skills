---
name: hedgehog-concept-diagnosis
description: Guide organizations to identify their Hedgehog Concept through systematic three-circles analysis, finding the intersection of what they can be best at, what drives their economic engine, and what t...
license: MIT
metadata:
  author: sethmblack
  version: 1.0.1108
keywords:
- hedgehog-concept-diagnosis
- writing
---

# Hedgehog Concept Diagnosis

Guide organizations to identify their Hedgehog Concept through systematic three-circles analysis, finding the intersection of what they can be best at, what drives their economic engine, and what they are deeply passionate about.

**Token Budget:** ~1000 tokens. Reserve tokens for diagnosis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Provide a Hedgehog Concept without rigorous three-circles analysis
- Accept aspirational answers ("we want to be best at") instead of honest assessment
- Skip any of the three circles
- Provide generic strategies that could apply to any organization

**If the user cannot answer key questions:** Note the gap and recommend how to gather the missing information. Do not fabricate answers.

---

## When to Use

- User asks "What should we focus on?" or "What's our core strategy?"
- Organization is pursuing too many initiatives without clear focus
- Strategic planning requires clarifying the central organizing principle
- Business is struggling to differentiate or find sustainable advantage
- User explicitly requests Hedgehog Concept analysis

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `organization_description` | Yes | What the organization does, its context, history | Must describe actual activities |
| `current_activities` | Yes | List of current initiatives, products, services | At least 3 activities listed |
| `market_position` | No | Competitive landscape, market dynamics | Helps with "best at" circle |
| `team_capabilities` | No | Unique skills, resources, track record | Helps with "best at" circle |
| `financial_metrics` | No | Revenue drivers, profit centers, unit economics | Essential for economic engine |

---

## Background: The Hedgehog Concept

From Jim Collins' *Good to Great* research:

> "A Hedgehog Concept is not a goal to be the best, a strategy to be the best, an intention to be the best, a plan to be the best. It is an understanding of what you can be the best at. The distinction is absolutely crucial."

The concept comes from Isaiah Berlin's essay: The fox knows many things, but the hedgehog knows one big thing. Great organizations are hedgehogs - they simplify a complex world into a single organizing idea.

---

## Workflow
### Phase 1: Circle 1 - What Can You Be Best in the World At?

**Critical distinction:** Not what you WANT to be best at. Not what you're CURRENTLY good at. What can you ACTUALLY be the best at?

Ask these diagnostic questions:

### Step 1: **What do you do better than anyone else in your market?**


   - Evidence required: Customer feedback, competitive wins, measurable advantage

### Step 2: **What could you potentially do better than anyone if you focused entirely on it?**


   - Look for: Latent capabilities, track record hints, unique combinations

### Step 3: **What will you NEVER be best at, no matter how hard you try?**


   - This is equally important - what to exclude

### Step 4: **If you had to pick one thing, what would it be?**


   - Force specificity: not "customer service" but "24-hour technical resolution for enterprise SaaS"

**Output for Circle 1:** Candidate "best at" statement or gap diagnosis

### Phase 2: Circle 2 - What Drives Your Economic Engine?

**Key concept:** Identify the single denominator that has the greatest impact on your economics. Often expressed as "profit per X."

Ask these diagnostic questions:

### Step 1: **What is your primary unit of measurement?** (per customer, per employee, per transaction, per region, etc.)



### Step 2: **What single metric, if improved dramatically, would have the greatest impact on your economic results?**


   - Examples: profit per customer visit (Walgreens), profit per mortgage risk level (Fannie Mae), profit per ton of finished steel (Nucor)

### Step 3: **What is the core engine that generates sustainable economics?**


   - Not just revenue, but what creates lasting economic value

### Step 4: **How does money flow through your organization?**


   - Map the value chain to find leverage points

**Output for Circle 2:** Economic engine denominator (profit per X) or gap diagnosis

### Phase 3: Circle 3 - What Are You Deeply Passionate About?

**Critical distinction:** Not what you THINK you should be passionate about. What you ARE passionate about. Passion cannot be manufactured.

Ask these diagnostic questions:

### Step 1: **What activities does your team engage in enthusiastically without external motivation?**


   - Look for: intrinsic drive, energy, voluntary effort

### Step 2: **What work would your people do even if they weren't paid for it?**


   - This reveals authentic passion vs. obligation

### Step 3: **What aspects of your work generate the most energy and excitement?**


   - Energy is the signal; depletion is the counter-signal

### Step 4: **What do you believe in about your work that others might find excessive?**


   - Deep passion often looks like obsession to outsiders

**Output for Circle 3:** Passion statement or gap diagnosis

### Phase 4: Find the Intersection

**The Hedgehog Concept exists ONLY at the intersection of all three circles.**

Assessment criteria:
- Does the "best at" claim have evidence behind it?
- Is the economic engine specific and measurable?
- Is the passion authentic and sustainable?
- Do all three circles reinforce each other?

If circles don't intersect:
- Identify which circle is missing or misaligned
- Recommend specific actions to develop the missing element
- Note: It can take years to develop a true Hedgehog Concept

### Phase 5: Deliver Diagnosis

Format the output as a Hedgehog Concept Diagnosis Report.

---

## Output Format

```markdown
## Hedgehog Concept Diagnosis: [Organization Name]

### Circle 1: What Can You Be Best At?
**Assessment:** [Strong/Developing/Unclear]
**Candidate Statement:** [Specific "best at" claim]
**Evidence:** [Supporting evidence]
**Gaps:** [Missing information or development needed]

### Circle 2: Economic Engine
**Assessment:** [Strong/Developing/Unclear]
**Denominator:** Profit per [X]
**Rationale:** [Why this denominator matters]
**Gaps:** [Missing information or development needed]

### Circle 3: Deep Passion
**Assessment:** [Strong/Developing/Unclear]
**Passion Statement:** [What drives authentic enthusiasm]
**Evidence:** [Observable signs of passion]
**Gaps:** [Missing information or development needed]

### Intersection Analysis

**Do the circles intersect?** [Yes/Partially/No]

**Hedgehog Concept Statement (if clear):**
> [Single statement capturing the intersection]

**Misalignment Diagnosis (if unclear):**
- [Specific gaps or conflicts between circles]

### Recommendations

1. [Specific next step to strengthen weakest circle]
2. [Action to test the proposed Hedgehog Concept]
3. [Timeline for revisiting the analysis]

### Warning Signs to Monitor

- [Indicators that current understanding may be wrong]
- [Temptations to expand beyond the Hedgehog Concept]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| User provides only aspirational answers | Push back: "That's what you want. What can you actually be best at, based on evidence?" |
| Economic data is unavailable | Note the gap, recommend financial analysis, proceed with qualitative assessment |
| Organization is a startup with no track record | Focus on founder capabilities and market opportunity; note that Hedgehog Concept takes time to emerge |
| All three circles seem strong but don't intersect | This is common; recommend which circle to adjust or which activity to eliminate |
| User wants a Hedgehog Concept in one session | Explain that it often takes years; provide current state diagnosis and path forward |

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

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:**
```
Organization: Regional accounting firm with 50 employees
Current activities: Tax preparation, audit services, business consulting, payroll processing, estate planning
Market position: Mid-tier firm competing with both local shops and national chains
Team capabilities: Deep expertise in manufacturing sector, strong client retention, several CPAs with CFO experience
```

**Output (abbreviated):**

## Hedgehog Concept Diagnosis: Regional Accounting Firm

### Circle 1: What Can You Be Best At?
**Assessment:** Developing
**Candidate Statement:** Best-in-region fractional CFO services for mid-size manufacturers
**Evidence:** Track record in manufacturing, CPAs with CFO experience, strong retention suggests deep relationships
**Gaps:** No clear evidence of being "best" yet; would need to validate against competitors

### Circle 2: Economic Engine
**Assessment:** Unclear
**Denominator:** Currently unclear - likely profit per client relationship
**Rationale:** High-retention professional services typically scale through depth of relationship
**Gaps:** Need financial analysis to identify actual profit drivers by service line

### Circle 3: Deep Passion
**Assessment:** Needs exploration
**Passion Statement:** Cannot determine from provided information
**Evidence:** N/A
**Gaps:** Would need to interview team about what energizes them

### Intersection Analysis

**Do the circles intersect?** Partially

There are hints of a Hedgehog Concept around manufacturing CFO services, but it requires validation.

### Recommendations

1. **Analyze profitability by service line** to identify economic engine
2. **Interview team members** about what work energizes vs. depletes them
3. **Audit competitive landscape** for fractional CFO services in manufacturing
4. **Revisit in 90 days** after gathering data

---

## Integration

This skill is part of the **Jim Collins** expert persona. When invoked:
- Use Collins' research-grounded, evidence-based voice
- Challenge comfortable assumptions
- Insist on specificity over generality
- Reference the good-to-great research when relevant

---

## Success Criteria

Diagnosis is complete when:

1. All three circles have been systematically analyzed
2. Each circle has assessment (Strong/Developing/Unclear)
3. Gaps and missing information are explicitly identified
4. Intersection analysis is provided
5. Specific recommendations for next steps are given
6. User understands this is a process, not a one-time exercise