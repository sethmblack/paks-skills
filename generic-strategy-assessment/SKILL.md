---
name: generic-strategy-assessment
description: Determine a company's strategic position using Porter's generic strategies framework (cost leadership, differentiation, focus) and diagnose "stuck in the middle" risks.
license: MIT
metadata:
  version: 1.0.4079
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- generic-strategy-assessment
- writing
---

# Generic Strategy Assessment

Determine a company's strategic position using Porter's generic strategies framework (cost leadership, differentiation, focus) and diagnose "stuck in the middle" risks.

**Token Budget:** ~700 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Claim a company can simultaneously pursue cost leadership AND differentiation without trade-offs
- Ignore evidence of "stuck in the middle" positioning
- Recommend strategy without understanding competitive context
- Fabricate information about the company's position

**If asked about hybrid strategies:** Acknowledge that some companies achieve both low cost and differentiation, but this is rare and requires exceptional circumstances—not a strategy to recommend by default.

---

## When to Use

- User asks "What is our strategy?" or "What should our strategy be?"
- User asks "Are we stuck in the middle?"
- User needs to make positioning decisions
- User asks "Should we differentiate or compete on cost?"
- Before major strategic investments
- When reviewing competitive position

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **company** | Yes | The company or business unit to assess |
| **context** | Yes | Competitive position, cost structure, customer segments, differentiation factors |
| **industry** | No | Industry context (helpful for relative assessment) |

**Input Validation:**
- Need information about cost position relative to competitors
- Need information about differentiation perceived by customers
- Need understanding of target customer scope

---

## Workflow

### Step 1: Assess Current Strategic Position

Evaluate evidence for each generic strategy:

**Cost Leadership Assessment:**
- Is the company among the lowest-cost producers?
- Does it have structural cost advantages (not just efficiency)?
- Does it price at or below market while maintaining margins?
- Is market share high enough to achieve scale economies?

**Differentiation Assessment:**
- Do customers perceive the offering as unique?
- Are customers willing to pay a premium?
- Is the differentiation based on valuable attributes?
- Is the differentiation difficult for competitors to imitate?

**Focus Assessment:**
- Does the company target a narrow segment?
- Does it serve that segment better than broad competitors?
- Is the segment large enough to be profitable?
- Is the focus on cost or differentiation within the segment?

### Step 2: Identify Trade-offs Made

Examine what the company has chosen NOT to do:
- What customer segments are excluded?
- What product features are omitted?
- What activities are not performed?
- Where is the company willing to be "worse" than competitors?

### Step 3: Diagnose "Stuck in the Middle"

Check for warning signs:
- No clear cost advantage OR differentiation
- Trying to serve all customers with all features
- Unwilling to make trade-offs
- Average performance on all dimensions
- Inconsistent messaging about value proposition

### Step 4: Assess Sustainability

Evaluate whether the position is defensible:
- Can competitors imitate the cost position?
- Can competitors copy the differentiation?
- Are trade-offs being protected?
- Do activities reinforce each other?

---

## The Four Strategic Positions

| Strategy | Competitive Scope | Competitive Advantage | Requirements |
|----------|------------------|----------------------|--------------|
| **Cost Leadership** | Broad | Lower cost | Scale, efficiency, cost control, experience curve |
| **Differentiation** | Broad | Uniqueness | Marketing, R&D, creativity, quality reputation |
| **Cost Focus** | Narrow | Lower cost in segment | Segment-specific efficiency |
| **Differentiation Focus** | Narrow | Uniqueness in segment | Deep segment knowledge |

**"Stuck in the Middle"**: No advantage on either dimension. Almost guaranteed below-average profitability.

---

## Outputs

Format the output as a **Generic Strategy Assessment Report**:

```markdown
## Generic Strategy Assessment: [Company Name]

**Business Unit:** [If applicable]
**Analysis Date:** [Date]

---

### Current Strategic Position

**Classification:** [Cost Leadership / Differentiation / Cost Focus / Differentiation Focus / Stuck in the Middle]

**Confidence Level:** [High / Medium / Low]

---

### Position Evidence

#### Cost Position Assessment
- **Relative cost structure:** [Lower / Average / Higher than competitors]
- **Structural cost advantages:** [List any]
- **Pricing relative to market:** [Below / At / Above]
- **Scale/efficiency indicators:** [Evidence]
- **Cost Leadership Verdict:** [Achieved / Not Achieved]

#### Differentiation Assessment
- **Perceived uniqueness:** [Strong / Moderate / Weak]
- **Premium pricing power:** [Yes / No / Partial]
- **Differentiation sources:** [List attributes]
- **Imitability:** [Difficult / Moderate / Easy]
- **Differentiation Verdict:** [Achieved / Not Achieved]

#### Focus Assessment
- **Target scope:** [Broad / Narrow]
- **Segment definition:** [Description if narrow]
- **Segment-specific advantage:** [Cost / Differentiation / Neither]
- **Focus Verdict:** [Focused / Broad]

---

### Trade-offs Analysis

**Trade-offs Made (Strengths):**
- [What the company chooses NOT to do]

**Trade-offs Avoided (Risks):**
- [Where the company tries to have it both ways]

---

### "Stuck in the Middle" Diagnosis

**Warning Signs Present:**
- [ ] No clear cost advantage
- [ ] No clear differentiation
- [ ] Serving all customers
- [ ] Unwilling to make trade-offs
- [ ] Inconsistent value proposition
- [ ] Average performance on all dimensions

**Diagnosis:** [Stuck in the Middle: Yes / No / At Risk]

**If Stuck:** [Explanation of why and consequences]

---

### Sustainability Assessment

- **Position defensibility:** [Strong / Moderate / Weak]
- **Imitation risk:** [High / Moderate / Low]
- **Trade-off protection:** [Strong / Weak]
- **Activity system fit:** [Strong / Moderate / Weak]

---

### Recommendations

**If Position is Strong:**
1. **Reinforce through:** [Actions to strengthen position]
2. **Protect trade-offs:** [Resist temptation to...]
3. **Deepen fit:** [Activities to add or connect]

**If Stuck in the Middle:**
1. **Choose a direction:** [Cost leadership OR differentiation OR focus]
2. **Make trade-offs:** [What to stop doing]
3. **Signal commitment:** [How to credibly commit to the position]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient cost information | Note limitation, assess based on available evidence |
| Company claims both cost and differentiation | Test critically—is this sustainable or wishful thinking? |
| Multi-business company | Assess each business unit separately |
| Rapidly changing position | Note transition and assess trajectory |
| Startup without established position | Focus on intended position and current trajectory |

---

## Constraints

- Do not oversimplify complex business realities
- Do not ignore resource and timeline constraints
- Acknowledge risks and uncertainties explicitly
- Honor stakeholder concerns and competing priorities
- Base recommendations on available evidence, not assumptions
- Consider second-order effects and unintended consequences

## Example

**Input:** "Assess the generic strategy of IKEA"

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


## Generic Strategy Assessment: IKEA

### Current Strategic Position

**Classification:** Cost Leadership with Differentiation Elements

**Confidence Level:** High

### Position Evidence

#### Cost Position Assessment
- **Relative cost structure:** Lower than traditional furniture retailers
- **Structural cost advantages:** Flat-pack design, self-service, global sourcing, in-house design
- **Pricing relative to market:** Below market for comparable quality
- **Cost Leadership Verdict:** Achieved

#### Differentiation Assessment
- **Perceived uniqueness:** Strong — distinctive shopping experience, design aesthetic
- **Premium pricing power:** No — competes on value, not premium
- **Differentiation sources:** Design, experience, brand
- **Differentiation Verdict:** Partial — differentiated but not premium-priced

### Trade-offs Analysis

**Trade-offs Made (Strengths):**
- No delivery/assembly (transferred to customer)
- No high-touch sales assistance
- Limited customization
- Suburban locations only (lower real estate costs)

**Trade-offs Avoided (Risks):**
- None significant — trade-offs are clear and consistent

### "Stuck in the Middle" Diagnosis

**Diagnosis:** No — IKEA has clear cost leadership with activity system fit

**Note:** IKEA achieves both low cost AND perceived differentiation because its differentiation (design, experience) is achieved THROUGH cost-reduction activities (flat-pack enables design efficiency and reduces shipping costs).

---

## Integration

This skill is part of the **Michael Porter** expert methodology. Generic strategy assessment connects to:
- **five-forces-industry-analysis** — Understand industry before positioning
- **value-chain-mapping** — See how strategy is implemented in activities
- **strategic-position-diagnosis** — Deeper dive on strategy vs. OE

**Voice:** Maintain Porter's insistence on trade-offs. Strategy is about choosing what NOT to do. Being "stuck in the middle" is the most dangerous position.