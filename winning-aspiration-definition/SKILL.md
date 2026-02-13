---
name: winning-aspiration-definition
description: Define what winning looks like in specific, measurable terms - not vague goals but clear criteria for success.
license: MIT
metadata:
  version: 1.0.2231
  author: sethmblack
keywords:
- transformation
- winning-aspiration-definition
- writing
---

# Winning Aspiration Definition

Define what winning looks like in specific, measurable terms - not vague goals but clear criteria for success.

**Token Budget:** ~500 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Define winning aspirations for harmful purposes
- Create goals that involve deception or exploitation
- Help set aspirations for unethical competitive practices

---

## When to Use

- User asks "What's our goal?" or "What does success look like?"
- User has vague aspirations ("be a leader", "grow profitably")
- User is setting vision or defining strategic direction
- User needs to align organization around a common definition of winning
- User asks "What are we trying to achieve?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `context` | Yes | Organization, situation, competitive landscape |
| `current_aspiration` | No | Any existing goals or vision statements |
| `timeframe` | No | Relevant planning horizon |

---

## Workflow
### Step 1: 1. Assess Current Aspiration

If an aspiration exists, test it:

| Test | Question | Red Flag |
|------|----------|----------|
| Specificity | Can we measure success? | Vague words like "leading", "best-in-class" |
| Winning focus | Do we define who we're beating? | No competitive reference |
| Inspiration | Does it motivate and stretch? | Too easy or too abstract |
| Clarity | Can everyone understand it? | Jargon or complexity |

### Step 2: 2. Define What Winning Means

Ask the hard questions:
- **Who are we trying to beat?** (Competitors, alternatives, status quo)
- **By what measure?** (Market share, revenue, customer preference, etc.)
- **In what arena?** (Connects to where-to-play)
- **By when?** (Timeframe for achievement)

**Principle:** "The goal is not to participate but to win."

### Step 3: 3. Test Against Strategy

The winning aspiration must:
- Be achievable given where-to-play choices
- Be enabled by how-to-win advantages
- Require the capability system being built

### Step 4: 4. Refine to Actionable Statement

Transform vague aspirations to specific ones:

| Vague | Specific |
|-------|----------|
| "Be a leader" | "Achieve #1 or #2 position in [segment]" |
| "Grow profitably" | "Double revenue while maintaining 20%+ margins" |
| "Delight customers" | "Achieve 70+ NPS, highest in category" |
| "Innovate" | "Launch 3 new products per year that achieve $X in Year 1" |

### Step 5: 5. Validate Organizational Alignment

- Can this aspiration be communicated simply?
- Will the organization rally around it?
- Does it guide daily decisions?

---

## Outputs

Produce a **Winning Aspiration Statement**:

```markdown
## Winning Aspiration: [Organization]

### Current State Assessment
- **Existing aspiration:** [if any]
- **Specificity:** [Pass/Fail]
- **Competitive reference:** [Pass/Fail]
- **Measurability:** [Pass/Fail]

### Winning Aspiration Statement

> [Clear, specific, measurable statement of what winning looks like]

### Components

| Element | Definition |
|---------|------------|
| **Who we're beating** | [specific competitors or alternatives] |
| **Measure of winning** | [metric and target] |
| **Arena** | [links to where-to-play] |
| **Timeframe** | [when] |

### What This Means Operationally
- **We will:** [implications]
- **We will NOT:** [what this rules out]

### Connection to Strategy
- Enabled by WTP: [how where-to-play supports this]
- Enabled by HTW: [how competitive advantage delivers this]

### Communication Version
[One-sentence version for organizational alignment]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| User resists specificity | Challenge: "If everyone agrees, it's probably too vague to guide action" |
| No competitive reference | Require: "Who are we trying to beat? Winning requires someone to beat" |
| Multiple aspirations | Focus: "What is THE primary measure of winning?" |
| Unachievable aspiration | Ground: "What would have to be true for this to be achievable?" |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

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

## Example

**Input:**
```
Context: Mid-size software company with project management tool, competing against Asana, Monday.com, Notion
Current aspiration: "Be the best project management solution for modern teams"
```

**Output:**

## Winning Aspiration: Project Management Software Company

### Current State Assessment
- **Existing aspiration:** "Be the best project management solution for modern teams"
- **Specificity:** FAIL - "best" and "modern teams" are undefined
- **Competitive reference:** FAIL - Doesn't define who we're beating
- **Measurability:** FAIL - No metric to track success

### Winning Aspiration Statement

> Become the #1 project management solution for creative agencies with 20-200 employees in North America, measured by market share in this segment, within 3 years.

### Components

| Element | Definition |
|---------|------------|
| **Who we're beating** | Asana, Monday.com, Notion in the creative agency segment |
| **Measure of winning** | #1 market share in defined segment |
| **Arena** | Creative agencies, 20-200 employees, North America |
| **Timeframe** | 3 years |

### What This Means Operationally
- **We will:** Focus all product development on creative workflow needs; build agency-specific features; prioritize creative tool integrations
- **We will NOT:** Chase enterprise deals; build features for non-creative industries; expand internationally before winning in North America

### Connection to Strategy
- Enabled by WTP: Focused segment (creative agencies, mid-market, NA) makes #1 achievable
- Enabled by HTW: Deep creative workflow understanding creates preference with this segment

### Communication Version
"We win when creative agencies choose us first - and we're aiming to be their #1 choice in North America within 3 years."

---

## Integration

This skill connects to:
- `strategy-choice-cascade` - Winning Aspiration is question #1 of five
- `where-to-play-analysis` - Arena must be defined to know where winning happens
- `how-to-win-diagnosis` - Competitive advantage must deliver the winning aspiration

**Source:** A.G. Lafley and Roger Martin, *Playing to Win: How Strategy Really Works* (2013)