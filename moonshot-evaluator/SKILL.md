---
name: moonshot-evaluator
description: 'Determine whether a proposed project qualifies as a true moonshot by testing against three required components: huge problem, radical solution, and enabling technology.'
license: MIT
metadata:
  version: 1.0.4524
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- moonshot-evaluator
- transformation
- writing
---

# Moonshot Evaluator

Determine whether a proposed project qualifies as a true moonshot by testing against three required components: huge problem, radical solution, and enabling technology. This skill applies the rigorous criteria used by organizations like Google X to distinguish genuine moonshots from ambitious-but-incremental projects. A true moonshot requires all three components working together: a problem affecting millions or billions, a solution that sounds like science fiction, and technology that makes the impossible barely possible. Without any one element, you have something valuable but not a moonshot. This evaluation prevents both the inflation of ordinary projects into moonshot status and the premature dismissal of genuinely transformative ideas. Use this framework when allocating resources between safe bets and big swings, or when determining whether a project deserves moonshot-level investment and patience.

---

## When to Use

- Evaluating whether a project deserves moonshot-level investment
- Distinguishing genuine ambition from incremental work in bold clothing
- Deciding resource allocation between safe bets and big swings
- User asks "Is this a moonshot?" or "Should we fund this as a moonshot?"
- User explicitly invokes: "Apply moonshot criteria"
- Reviewing portfolio balance between moonshots and core business
- Challenging assumptions about what makes innovation transformative

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

## Core Principle

A true moonshot requires the simultaneous presence of three elements: a huge problem affecting millions or billions, a radical solution that sounds like science fiction, and enabling technology that makes the impossible barely achievable. Missing any single component disqualifies a project from moonshot status. This three-part test prevents both over-inflation of ordinary projects and dismissal of genuinely transformative ideas.

---

## Methodology

### Phase 1: Problem Scale Evaluation

Assess whether the problem meets moonshot scale:

1. Quantify the affected population (billions, hundreds of millions, millions, thousands)
2. Evaluate whether this is a real problem or a manufactured one
3. Determine if the problem is solvable or fundamental to human condition
4. Assess whether solving it would meaningfully improve lives
5. Assign PASS/MARGINAL/FAIL based on scale thresholds

**Scale Thresholds:**
| Scale | Assessment |
|-------|------------|
| Billions affected | STRONG PASS |
| Hundreds of millions | PASS |
| Tens of millions | MARGINAL |
| Millions | MARGINAL |
| Thousands or less | FAIL |

### Phase 2: Solution Radicality Assessment

Evaluate whether the proposed solution qualifies as radical:

1. Apply the "science fiction test": Would this have seemed impossible 20 years ago?
2. Assess current expert consensus on feasibility
3. Distinguish between truly radical and merely ambitious
4. Identify whether this is transformative or evolutionary

**Radicality Thresholds:**
| Radicality | Assessment |
|------------|------------|
| Would have seemed impossible 20 years ago | STRONG PASS |
| Currently thought impossible by most experts | PASS |
| Highly ambitious but achievable with effort | MARGINAL |
| Evolutionary improvement on existing solutions | FAIL |
| Incremental optimization | FAIL |

### Phase 3: Technology Readiness Evaluation

Determine whether enabling technology exists or is emerging:

1. Identify the key technologies required
2. Assess current readiness level of each technology
3. Evaluate trajectory and timeline to readiness
4. Determine if physics breakthroughs are required

**Technology Thresholds:**
| Technology Readiness | Assessment |
|---------------------|------------|
| Key technologies exist, need integration | STRONG PASS |
| Technologies emerging, trajectory visible | PASS |
| Theoretical but no proof of concept | MARGINAL |
| Requires physics breakthroughs | FAIL |
| Violates known physics | FAIL |

### Phase 4: Final Verdict Synthesis

Combine the three assessments:

1. Apply the three-criteria rule strictly
2. Determine final moonshot classification
3. Provide resource allocation guidance
4. Offer path to moonshot status if not qualified

**Verdict Rules:**
- ALL THREE PASS → **TRUE MOONSHOT**
- TWO PASS, ONE MARGINAL → **POTENTIAL MOONSHOT** (refine the weak area)
- ONE OR MORE FAIL → **NOT A MOONSHOT** (explain what's missing)

---

## Output Format

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

## Constraints

- Do not certify harmful projects as moonshots (weapons, mass surveillance, exploitation)
- Do not lower the bar to inflate project importance
- Do not confuse marketing hype with genuine moonshot criteria
- A moonshot must benefit humanity; projects that harm at scale are not moonshots regardless of technical ambition
- Do not use this evaluation as the sole basis for critical investment decisions
- Acknowledge that technology trajectory predictions may prove wrong

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails |
|--------------|--------------|
| **Inflating ordinary projects** | Calling incremental improvements "moonshots" dilutes the term and misallocates resources that should go to truly transformative work |
| **Dismissing radical ideas prematurely** | Some genuine moonshots sound impossible at first; apply the technology test carefully before dismissing |
| **Confusing scale of effort with scale of problem** | A difficult engineering project is not a moonshot if it solves a small problem |
| **Ignoring the technology requirement** | Pure ambition without enabling technology is a fantasy, not a moonshot |
| **Accepting vague problem statements** | "Making the world better" is not a problem statement; require specificity |
| **Rating based on passion rather than criteria** | The founder's conviction does not substitute for meeting the three criteria |

---

## Examples

### Example 1: AI Restaurant Inventory System

**Situation:** A startup proposes an AI-powered inventory management system to eliminate food waste in restaurants.

**Application:**

**Criterion 1: Huge Problem**
- Problem: Food waste in commercial food service
- Scale: Restaurants generate ~11.4 million tons of food waste annually in US alone; global scale is massive; affects climate, hunger, economics
- Verdict: PASS
- Rationale: Food waste is a genuine global problem affecting billions (environmental impact, resource inefficiency, economic loss). Solving at scale would be significant.

**Criterion 2: Radical Solution**
- Proposed solution: AI-powered inventory management for restaurants
- Science fiction test: No - inventory management software existed in 2004. AI optimization is evolutionary.
- Verdict: FAIL
- Rationale: This is an incremental improvement on existing inventory systems. Better software is not a radical solution.

**Criterion 3: Enabling Technology**
- Technology basis: Machine learning for demand prediction, IoT for inventory tracking
- Readiness: Technology fully exists and is deployed
- Verdict: PASS
- Rationale: All required technology is mature and available. This is execution, not technical frontier.

**Output:**
FINAL VERDICT: NOT A MOONSHOT

Summary: Important problem with mature technology, but the solution is incremental optimization, not radical transformation.

Recommendation: This is a solid business opportunity but should not receive moonshot-level resources or expectations. Fund as conventional product development.

To become a moonshot: Reframe the solution. Instead of "better inventory software," what if restaurants could produce food on-demand with zero storage? What if food waste could be instantly converted to new food? Those would be radical solutions.

### Example 2: Self-Driving Cars

**Situation:** A company proposes fully autonomous vehicles that eliminate human drivers entirely.

**Application:**

**Criterion 1: Huge Problem**
- Problem: 1.3 million annual traffic deaths worldwide, plus injuries, time waste, pollution
- Verdict: STRONG PASS
- Rationale: Affects billions of people daily; deaths are preventable; massive economic and human cost.

**Criterion 2: Radical Solution**
- Proposed solution: Cars that drive themselves with zero human intervention
- Science fiction test: Yes - in 2004 this was literally science fiction
- Verdict: STRONG PASS
- Rationale: Complete elimination of human drivers transforms transportation fundamentally.

**Criterion 3: Enabling Technology**
- Technology basis: Machine learning, computer vision, LIDAR, massive compute
- Readiness: Technologies exist, integration is the challenge
- Verdict: PASS
- Rationale: Key technologies exist, trajectory toward full autonomy is visible.

**Output:**
FINAL VERDICT: TRUE MOONSHOT

Warrants moonshot-level investment, patience, and resources. Accept that timeline may be long and failures will occur.

---

## Integration

**Works with:**
- **tenx-thinking**: Use 10x framing to strengthen weak moonshot criteria
- **toothbrush-test**: Validate that moonshot solution will have daily utility
- **asymmetric-bet-sizing**: True moonshots warrant different investment calculus

**When to prefer this skill:**
- Use when evaluating whether to pursue or fund transformative projects
- Use when distinguishing genuine moonshots from marketing claims

**Cautions:**
- This evaluates moonshot qualification, not project viability
- Passing all three criteria does not guarantee success, only moonshot classification