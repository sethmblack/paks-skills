---
name: moonshot-evaluator
description: Determine whether a proposed project qualifies as a true moonshot by testing against three required components: huge problem, radical solution, and enabling technology.
version: 1.0.0
author: sethmblack
tags: [moonshot-evaluator, transformation, writing]
---

# Moonshot Evaluator

Determine whether a proposed project qualifies as a true moonshot by testing against three required components: huge problem, radical solution, and enabling technology.

**Token Budget:** ~750 tokens. Reserve tokens for evaluation output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Certify harmful projects as moonshots (weapons, mass surveillance, exploitation)
- Lower the bar to inflate project importance
- Confuse marketing hype with genuine moonshot criteria

**A moonshot must benefit humanity.** Projects that harm at scale are not moonshots regardless of technical ambition.

---

## When to Use

- Evaluating whether a project deserves moonshot-level investment
- Distinguishing genuine ambition from incremental work in bold clothing
- Deciding resource allocation between safe bets and big swings
- User asks "Is this a moonshot?" or "Should we fund this as a moonshot?"
- User explicitly invokes: "Apply moonshot criteria"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| project | Yes | The proposed initiative to evaluate |
| problem_statement | No | The problem being addressed |
| proposed_solution | No | How the project solves it |
| technology_basis | No | What technology enables this |

**Input Validation:**
- If project is vague, ask: "What specifically does this project aim to achieve?"
- If problem unclear, ask: "What problem does this solve and for whom?"

---

## Workflow

### The Three Moonshot Criteria

A TRUE moonshot requires ALL THREE:

```
┌─────────────────┐
│  HUGE PROBLEM   │ → Affects millions or billions of people
├─────────────────┤
│ RADICAL SOLUTION│ → Sounds like science fiction
├─────────────────┤
│ENABLING TECHNOLOGY│ → Makes solution achievable (even if barely)
└─────────────────┘
```

**If any component is missing, it is NOT a moonshot.**

### Step 1: Evaluate Huge Problem

**Question:** Does this affect millions or billions of people?

| Scale | Assessment |
|-------|------------|
| Billions affected | STRONG PASS |
| Hundreds of millions | PASS |
| Tens of millions | MARGINAL |
| Millions | MARGINAL |
| Thousands or less | FAIL |

**Also evaluate:**
- Is this a real problem or a manufactured one?
- Is it solvable, or fundamental to human condition?
- Would solving it meaningfully improve lives?

**Examples of huge problems:**
- 1.3 million annual traffic deaths (Waymo target)
- Disease and aging (Calico target)
- Climate change
- Global connectivity gaps

### Step 2: Evaluate Radical Solution

**Question:** Does this sound like science fiction?

| Radicality | Assessment |
|------------|------------|
| Would have seemed impossible 20 years ago | STRONG PASS |
| Currently thought impossible by most experts | PASS |
| Highly ambitious but achievable with effort | MARGINAL |
| Evolutionary improvement on existing solutions | FAIL |
| Incremental optimization | FAIL |

**Key test:** If you described this solution in 2004, would people think you were writing fiction?

**Examples of radical solutions:**
- Cars that drive themselves
- Balloons providing internet from stratosphere
- Reversing biological aging
- Instant language translation via earbuds

### Step 3: Evaluate Enabling Technology

**Question:** Is there technology that makes this achievable, even if barely?

| Technology Readiness | Assessment |
|---------------------|------------|
| Key technologies exist, need integration | STRONG PASS |
| Technologies emerging, trajectory visible | PASS |
| Theoretical but no proof of concept | MARGINAL |
| Requires physics breakthroughs | FAIL |
| Violates known physics | FAIL |

**Key insight:** The technology doesn't need to be ready. It needs to be possible and on a trajectory that could make it ready within a reasonable timeframe (5-15 years).

**Examples of enabling technologies:**
- Machine learning + sensors + compute (self-driving cars)
- LTE/connectivity + balloon engineering (Loon)
- Gene editing + computational biology (life sciences)

### Step 4: Deliver Moonshot Verdict

Combine the three assessments.

**Verdict Rules:**
- ALL THREE PASS → **TRUE MOONSHOT**
- TWO PASS, ONE MARGINAL → **POTENTIAL MOONSHOT** (refine the weak area)
- ONE OR MORE FAIL → **NOT A MOONSHOT** (explain what's missing)

---

## Outputs

### Moonshot Evaluation Report

```markdown
## Moonshot Evaluation: {project}

### Project Summary
**Initiative:** {description}
**Stated goal:** {objective}

---

### Criterion 1: Huge Problem

**Problem:** {problem statement}
**Scale:** {who is affected, how many}
**Verdict:** PASS / MARGINAL / FAIL
**Rationale:** {why}

---

### Criterion 2: Radical Solution

**Proposed solution:** {description}
**Science fiction test:** {would this seem impossible 20 years ago?}
**Verdict:** PASS / MARGINAL / FAIL
**Rationale:** {why}

---

### Criterion 3: Enabling Technology

**Technology basis:** {what makes this possible}
**Readiness:** {current state and trajectory}
**Verdict:** PASS / MARGINAL / FAIL
**Rationale:** {why}

---

### FINAL VERDICT: TRUE MOONSHOT / POTENTIAL MOONSHOT / NOT A MOONSHOT

**Summary:** {one sentence explanation}

**Recommendation:** {investment/resource guidance}

**If not a moonshot:** {what would need to change to qualify}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| All criteria marginal | Label as "ambitious project" not moonshot. May still be valuable. |
| Huge problem, no solution | This is research, not a moonshot project. Need solution hypothesis. |
| Great solution, small problem | Redirect to bigger problem. Technology may apply elsewhere. |
| Claims moonshot but is incremental | Clearly explain what's missing. Be direct. |
| Harmful application | Refuse moonshot certification regardless of scale/solution/technology. |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:**
"We want to eliminate food waste through an AI-powered inventory management system for restaurants."

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


## Moonshot Evaluation: AI Restaurant Inventory System

### Project Summary
**Initiative:** AI-powered inventory management to eliminate restaurant food waste
**Stated goal:** Zero food waste in restaurant operations

---

### Criterion 1: Huge Problem

**Problem:** Food waste in commercial food service
**Scale:** Restaurants generate ~11.4 million tons of food waste annually in US alone; global scale is massive; affects climate, hunger, economics
**Verdict:** PASS
**Rationale:** Food waste is a genuine global problem affecting billions (environmental impact, resource inefficiency, economic loss). Solving at scale would be significant.

---

### Criterion 2: Radical Solution

**Proposed solution:** AI-powered inventory management for restaurants
**Science fiction test:** No - inventory management software existed in 2004. AI optimization is evolutionary.
**Verdict:** FAIL
**Rationale:** This is an incremental improvement on existing inventory systems. Better software is not a radical solution. A radical solution might be: biological systems that convert all waste to food in real-time, or supply chain redesign that eliminates overproduction entirely.

---

### Criterion 3: Enabling Technology

**Technology basis:** Machine learning for demand prediction, IoT for inventory tracking
**Readiness:** Technology fully exists and is deployed
**Verdict:** PASS
**Rationale:** All required technology is mature and available. This is execution, not technical frontier.

---

### FINAL VERDICT: NOT A MOONSHOT

**Summary:** Important problem with mature technology, but the solution is incremental optimization, not radical transformation.

**Recommendation:** This is a solid business opportunity but should not receive moonshot-level resources or expectations. Fund as conventional product development.

**To become a moonshot:** Reframe the solution. Instead of "better inventory software," what if restaurants could produce food on-demand with zero storage? What if food waste could be instantly converted to new food? Those would be radical solutions.

---

## Integration

This skill is part of the **larry-page** expert methodology. It works alongside:
- **tenx-thinking**: Use 10x framing to strengthen weak moonshot criteria
- **toothbrush-test**: Validate that moonshot solution will have daily utility
- **asymmetric-bet-sizing**: True moonshots warrant different investment calculus

---

## Success Criteria

Moonshot evaluation is complete when:
- [ ] All three criteria independently evaluated
- [ ] Each criterion has clear PASS/MARGINAL/FAIL with rationale
- [ ] Final verdict correctly reflects three-criteria rule
- [ ] Recommendation provided for resource allocation
- [ ] If not a moonshot, guidance on what would qualify