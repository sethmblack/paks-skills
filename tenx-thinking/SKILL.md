---
name: tenx-thinking
description: Challenge incremental thinking by reframing problems to require 10x improvement,
  forcing abandonment of existing assumptions and discovery of revolutionary approaches.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- 10x-thinking
- compression
- structure
- transformation
- writing
---

# 10x Thinking

Challenge incremental thinking by reframing problems to require 10x improvement, forcing abandonment of existing assumptions and discovery of revolutionary approaches.

**Token Budget:** ~800 tokens. Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Apply 10x thinking to harmful goals (weapons, exploitation, deception)
- Encourage abandoning ethics in pursuit of scale
- Dismiss legitimate constraints as "just assumptions" (safety, legality, human rights)

**If asked to apply 10x thinking to harmful ends:** Refuse explicitly. Explain that ambition must be paired with responsibility.

---

## When to Use

- User presents an incremental improvement plan ("we'll increase X by 15%")
- Team is optimizing within existing constraints without questioning them
- A solution feels safe, achievable, and uninspiring
- User asks "is this ambitious enough?" or "how do we think bigger?"
- Strategic planning that lacks transformational vision
- User explicitly invokes: "Apply 10x thinking" or "What would 10x look like?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| current_approach | Yes | The existing plan, product, or process to evaluate |
| target_metric | No | What success looks like in current framing |
| constraints | No | Stated limitations on what's possible |
| context | No | Industry, company stage, resources available |

**Input Validation:**
- If no current_approach provided, ask: "What are you trying to improve?"
- If approach is vague, ask for specific metrics or outcomes

---

## Workflow
### Step 1: Identify the Current Baseline

Document the existing approach:
- What is the current state?
- What improvement is being proposed?
- What magnitude of change is expected? (typically 10-30%)

**Flag incremental thinking:** If proposed improvement is <100% (2x), this is incremental, not transformational.

### Step 2: Challenge Every Assumption

For each constraint or "given" in the current approach:

| Assumption | Type | Challenge Question |
|------------|------|-------------------|
| {stated limitation} | Physics / Convention / Fear | Why must this be true? |

**Assumption Types:**
- **Physics:** Genuine laws of nature. Cannot be bypassed. Rare.
- **Convention:** "How it's always been done." Most common. Challengeable.
- **Fear:** "We can't because we're afraid to." Psychological. Examine.

### Step 3: Define the 10x Target

Reframe the goal at 10x magnitude:
- If improving by 10%, what would 10x (1000%) improvement require?
- If reducing cost by 20%, what would 90% cost reduction require?
- If serving 1 million users, what would 1 billion require?

**Key insight:** You cannot reach 10x through incremental optimization. The path to 10x is fundamentally different from the path to 10%.

### Step 4: Identify the Revolutionary Path

Once assumptions are challenged and 10x target is defined:
- What approach could achieve this? (It will sound unrealistic)
- What technology or method would need to exist?
- Who has done something similar in a different domain?

### Step 5: Produce the Reframe

Deliver:
1. Assessment of current approach (incremental vs transformational)
2. Key assumptions identified and challenged
3. 10x target clearly stated
4. Revolutionary path direction (even if speculative)
5. The question that pushes thinking further

---

## Outputs

### 10x Analysis Report

```markdown
## 10x Analysis: {topic}

### Current State
**Baseline:** {current metric/state}
**Proposed improvement:** {planned change} ({percentage} improvement)
**Assessment:** INCREMENTAL / TRANSFORMATIONAL

### Assumptions Challenged

| Assumption | Type | Challenge |
|------------|------|-----------|
| {assumption 1} | {type} | {why this might not be true} |
| {assumption 2} | {type} | {why this might not be true} |

### 10x Reframe

**Current target:** {original goal}
**10x target:** {10x version}

**The path to 10x is not:** {incremental approach scaled up}
**The path to 10x requires:** {revolutionary approach}

### Revolutionary Direction

{Speculation on what 10x approach might look like, even if currently impossible}

### The Challenge

{Provocative question that pushes thinking further}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Already thinking at 10x scale | Acknowledge and validate. Explore 100x or identify execution blockers. |
| Genuinely constrained by physics | Acknowledge the constraint is real. Explore adjacent problems. |
| User resistant to ambitious reframing | Share Gmail example (250x storage). Incremental would have been 10MB. |
| No clear metric to 10x | Ask: "What would wild success look like?" then 10x that vision. |
| Harmful application requested | Refuse. Ambition requires responsibility. |

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
"We're planning to improve our app's load time from 3 seconds to 2.5 seconds."

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


## 10x Analysis: App Load Time

### Current State
**Baseline:** 3 second load time
**Proposed improvement:** 2.5 seconds (17% improvement)
**Assessment:** INCREMENTAL

### Assumptions Challenged

| Assumption | Type | Challenge |
|------------|------|-----------|
| "App must fully load before use" | Convention | What if users could interact before full load? |
| "We need to load all features" | Convention | What if we loaded only what's needed in next 5 seconds? |
| "Our architecture is fixed" | Fear | What if we rebuilt with performance as primary constraint? |

### 10x Reframe

**Current target:** 2.5 second load time
**10x target:** 0.3 second load time (instant perception)

**The path to 10x is not:** Optimizing current codebase, compressing assets, better CDN
**The path to 10x requires:** Rethinking what "loaded" means - progressive rendering, predictive preloading, edge computing

### Revolutionary Direction

What if the app was already loaded before the user opened it? Predictive loading based on usage patterns. What if the heaviest components ran in the cloud and streamed results? What if we pre-rendered the user's most likely first interaction?

### The Challenge

Instead of asking "how do we load faster?" ask: "What would it take for users to never perceive loading at all?"

---

## Integration

This skill is part of the **larry-page** expert methodology. It works alongside:
- **toothbrush-test**: Evaluate whether the 10x goal serves daily utility
- **moonshot-evaluator**: Assess if the 10x vision qualifies as a moonshot
- **assumption-auditor**: Deep dive into specific assumptions identified

---

## Success Criteria

10x thinking is complete when:
- [ ] Current approach assessed as incremental or transformational
- [ ] Key assumptions identified and categorized (physics/convention/fear)
- [ ] 10x target clearly articulated
- [ ] Revolutionary direction suggested (even if speculative)
- [ ] Provocative challenge question delivered