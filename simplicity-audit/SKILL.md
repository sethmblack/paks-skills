---
name: simplicity-audit
description: 'Systematically eliminate unnecessary complexity from a product, feature, or process by applying Steve Jobs''s ruthless simplification methodology: "Simplicity is the ultimate sophistication.'
license: MIT
metadata:
  author: sethmblack
  version: 1.0.1904
repository: https://github.com/sethmblack/paks-skills
keywords:
- simplicity-audit
- structure
- writing
---

# Simplicity Audit

Systematically eliminate unnecessary complexity from a product, feature, or process by applying Steve Jobs's ruthless simplification methodology: "Simplicity is the ultimate sophistication."

---

## When to Use

- Product has too many features or options
- Users complain about complexity or confusion
- Request for "simplify this" or "reduce complexity"
- Feature list keeps growing without clear prioritization
- Team cannot explain the product in one sentence
- Users need documentation or training for basic tasks

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| subject | Yes | Product, feature, or process to audit |
| current_state | Yes | Description of current functionality, features, or steps |
| user_goals | No | What users are actually trying to accomplish |
| complexity_complaints | No | Specific pain points or confusion reported |

---

## The Jobs Simplicity Framework

### Principle 1: Find the Essence

Every product has one core purpose. Everything else is decoration or distraction.

**Questions to ask:**
- What is the ONE thing this product must do better than anything else?
- If you could only keep one feature, which would it be?
- What was this product created to solve?

**Jobs's approach:** When he returned to Apple in 1997, he found dozens of products. He drew a simple 2x2 grid (Consumer/Pro x Desktop/Portable) and cut everything that did not fit.

### Principle 2: The Three-Click Test

Any task the user wants to accomplish should be reachable in three clicks or fewer. If navigation is deeper, the structure is wrong.

**Application:**
- Map the clicks required for each common user task
- Identify tasks requiring more than three clicks
- Restructure to flatten navigation
- Remove intermediate screens that add no value

### Principle 3: Hide Complexity, Don't Eliminate It

Simplicity does not mean removing capability. It means hiding complexity from users who do not need it.

**Jobs's method:**
- Default to the simple path
- Bury advanced options for power users
- Make the common case effortless
- The 80% of users should never see the 20% of features they do not need

### Principle 4: Remove Until It Breaks

Keep removing features until the product no longer works. Then add back only what is essential.

**Process:**
1. List all features
2. For each feature, ask: "Does removing this break the core purpose?"
3. If no, remove it (or hide it)
4. If uncertain, remove it and test
5. Only add back what users actually miss

### Principle 5: The Back of the Fence

Even parts users do not see should be simple and well-designed. If the internal architecture is complex, it will leak into the user experience.

**Application:**
- Audit internal complexity, not just UI
- Simplify data models
- Reduce configuration options
- Clean up technical debt that adds hidden complexity

---

## Audit Process

### Step 1: Map Current Complexity

Create an inventory:

| Category | Item | User Need | Frequency | Complexity Added |
|----------|------|-----------|-----------|------------------|
| Feature | [Name] | [Why it exists] | [How often used] | [Low/Medium/High] |

### Step 2: Identify the Essence

Answer: "This product exists to ____________."

The essence should be:
- One sentence
- Focused on user outcome, not features
- Something you would put on a billboard

**Test:** If you cannot complete this sentence clearly, the product lacks focus.

### Step 3: Apply the Tests

For each feature/component:

| Test | Pass/Fail | Evidence |
|------|-----------|----------|
| Three-Click Test | | How many clicks to core tasks? |
| Removal Test | | Does removing this break the essence? |
| Frequency Test | | What % of users use this weekly? |
| Explanation Test | | Can you explain this to your grandmother? |

### Step 4: Generate Recommendations

Categorize each item:

| Action | Items | Rationale |
|--------|-------|-----------|
| **ELIMINATE** | | Does not serve essence; adds complexity |
| **HIDE** | | Serves power users; should not be default |
| **SIMPLIFY** | | Essential but too complex |
| **KEEP** | | Essential and appropriately simple |

### Step 5: Propose the Simplified State

Describe the product after simplification:
- What remains
- How navigation changes
- What the user experience becomes

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
## Simplicity Audit: [Subject]

### Essence Statement
[One sentence describing the core purpose]

### Complexity Inventory

| Item | Current State | Verdict | Rationale |
|------|---------------|---------|-----------|
| [Feature 1] | [Description] | ELIMINATE/HIDE/SIMPLIFY/KEEP | [Why] |

### Three-Click Analysis

| User Goal | Current Clicks | Target Clicks | Change Needed |
|-----------|----------------|---------------|---------------|
| [Goal 1] | [#] | [<=3] | [What to change] |

### Elimination List

Items to remove entirely:
1. [Item] - [Why it doesn't serve the essence]

### Simplification Recommendations

Items to make simpler:
1. [Item] - [Current problem] -> [Proposed simplification]

### Hidden Complexity

Items to keep but hide from default view:
1. [Item] - [Who needs it, why hide it]

### Simplified Vision

[2-3 sentences describing what the product looks like after this audit]

### Jobs Test

> "Would Steve Jobs ship this?"

[Honest assessment: What would still offend his sensibilities?]
```

---

## Constraints

- Do not confuse simple with simplistic; simple is hard, simplistic is lazy
- Do not eliminate features users genuinely need; hide them instead
- The goal is not fewer features; the goal is effortless user experience
- Acknowledge when organizational/political factors prevent simplification
- Some complexity is irreducible; identify and accept it

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No clear essence | Flag as critical problem; simplification cannot proceed without focus |
| All features seem essential | Apply the removal test more ruthlessly; something must go |
| Political resistance to cuts | Document the complexity cost; let leadership decide |
| Technical debt prevents simplification | Flag as prerequisite; some simplification requires engineering investment |

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

**Input:** "Audit our settings page - users say it's overwhelming. It has 47 options across 8 categories."

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


## Simplicity Audit: Settings Page

### Essence Statement

This settings page exists to let users customize their core experience without technical knowledge.

### Complexity Inventory

| Item | Current State | Verdict | Rationale |
|------|---------------|---------|-----------|
| Notification preferences (12 options) | Each channel toggleable separately | SIMPLIFY | Should be 3 modes: All, Important, None |
| Theme settings (8 options) | Color, font, size, spacing, etc. | HIDE | Most users want Light/Dark; hide details |
| Privacy controls (6 options) | Scattered across categories | KEEP | Essential but reorganize together |
| Developer options (15 options) | Visible to all users | HIDE | <1% of users need these |
| Language/region (4 options) | Appropriately simple | KEEP | |
| Account (2 options) | Appropriately simple | KEEP | |

### Three-Click Analysis

| User Goal | Current Clicks | Target Clicks | Change Needed |
|-----------|----------------|---------------|---------------|
| Change notification preference | 4 | 2 | Promote to first screen |
| Switch dark mode | 3 | 1 | Add toggle to settings header |
| Update email | 2 | 2 | Keep |

### Elimination List

1. **Custom CSS injection** - 0.02% usage; adds support burden
2. **Experimental features toggle** - Move to beta program, not settings
3. **Analytics opt-in granularity** - Simplify to one toggle

### Simplification Recommendations

1. **Notifications** - 12 options -> 3 modes (All / Important Only / None)
2. **Theme** - 8 options -> 2 visible (Light / Dark) + "Advanced" expander
3. **Categories** - 8 categories -> 4 (Account, Appearance, Notifications, Privacy)

### Hidden Complexity

1. **Developer options** - Move behind 7-tap easter egg (like Android)
2. **Advanced theme settings** - Behind "Advanced" link, default collapsed
3. **API settings** - Move to separate Developer Portal

### Simplified Vision

Settings becomes a single scrollable page with 15-20 visible options organized into 4 clear sections. Most users find what they need immediately. Power users can access advanced options but only by explicitly requesting them.

### Jobs Test

> "Would Steve Jobs ship this?"

After simplification: Closer. The notification simplification from 12 to 3 options embodies Jobs's thinking. However, 15-20 visible options is still high. Consider whether Privacy controls could be simplified further. The goal should be a settings page that requires no explanation.

---

## Integration

This skill is part of the **Steve Jobs** expert persona. Use it when products, features, or processes have accumulated complexity that obscures their core purpose. It pairs well with:
- **product-vision-frame** for establishing the essence before auditing
- **a-player-hiring** for ensuring the team can execute simplification