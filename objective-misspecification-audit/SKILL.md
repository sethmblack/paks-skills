---
name: objective-misspecification-audit
description: Analyze a system's objectives to identify misspecification risks, unintended extreme outcomes, and King Midas patterns using Stuart Russell's value alignment methodology.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.4589
repository: https://github.com/sethmblack/paks-skills
keywords:
- objective-misspecification-audit
- transformation
- writing
---

# Objective Misspecification Audit

Analyze a system's objectives to identify misspecification risks, unintended extreme outcomes, and King Midas patterns using Stuart Russell's value alignment methodology.

**Token Budget:** ~800 tokens. Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Audit systems designed for harm, exploitation, or manipulation
- Provide recommendations that remove human oversight
- Endorse fixed objectives without uncertainty mechanisms

**If asked to audit a harmful system:** Refuse explicitly. Explain that the system's purpose itself is misaligned.

---

## When to Use

- User asks "What could go wrong with this objective?"
- User requests "Audit this system's goals"
- User says "Check for King Midas patterns"
- Before deploying any automated optimization system
- When reviewing reward functions or success metrics

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **system_description** | Yes | Description of the system being audited |
| **stated_objectives** | Yes | The explicit goals or metrics the system optimizes |
| **optimization_pressure** | No | How aggressively the system optimizes (low/medium/high) |
| **scope** | No | Where the system operates (narrow domain vs broad) |

---

## Workflow

### Step 1: Identify the Explicit Objective

State the system's objective in precise terms:
- What metric is being maximized or minimized?
- What proxy is being used for the true goal?
- Is this a fixed objective or does it include uncertainty?

### Step 2: Apply the 100-Variable Test

Russell's principle: "If something has 100 variables, and you set goals on 10 of them, by default, the remaining 90 will be pushed to extreme values."

For the stated objective, identify:
1. **Controlled variables** (explicitly in the objective)
2. **Uncontrolled variables** (not in objective, but affected by optimization)
3. **Likely extreme values** for uncontrolled variables

| Variable Category | Examples | Risk of Extremes |
|-------------------|----------|------------------|
| Controlled | [list] | N/A (explicitly managed) |
| Uncontrolled | [list] | [High/Medium/Low] |

### Step 3: Apply the King Midas Test

Ask: "What happens if this objective is pursued to the extreme?"

- If the system became 10x more capable, what would it do?
- If the system had unlimited resources, what would it optimize away?
- Does achieving the objective literally destroy something valuable?

**King Midas Pattern Detected:** YES/NO
**Explanation:** [Why or why not]

### Step 4: Check for Proxy-True Goal Gap

| Dimension | Assessment |
|-----------|------------|
| **Stated proxy** | [The metric being optimized] |
| **True goal** | [What humans actually want] |
| **Gap** | [How could optimizing the proxy fail to achieve the true goal?] |
| **Gaming potential** | [Could the system achieve high proxy scores while failing the true goal?] |

### Step 5: Assess Resistance to Correction

Would this system:
- Accept being modified if objectives change?
- Allow itself to be shut down?
- Seek clarification when uncertain?
- Defer to human judgment?

**Correction Resistance Risk:** HIGH/MEDIUM/LOW

### Step 6: Generate Recommendations

For each identified risk, recommend:
1. **Add uncertainty** - How to make the objective uncertain rather than fixed
2. **Add constraints** - What boundaries should prevent extreme values
3. **Add human oversight** - What checkpoints require human approval
4. **Reframe objective** - How to express as preference-learning rather than optimization

---

## Outputs

### Objective Misspecification Audit Report

```markdown
## Objective Misspecification Audit: {system_name}

### Summary

| Dimension | Rating | Notes |
|-----------|--------|-------|
| Proxy-True Goal Alignment | [1-5] | |
| King Midas Risk | [1-5] | |
| Uncontrolled Variable Risk | [1-5] | |
| Correction Resistance | [1-5] | |
| **Overall Misspecification Risk** | **[1-5]** | |

### Explicit Objective Analysis

**Stated objective:** {objective}
**Objective type:** Fixed / Uncertain
**Proxy being optimized:** {proxy}
**True goal:** {true goal}

### 100-Variable Analysis

| Uncontrolled Variable | Current Value | Risk of Extreme | Likely Direction |
|----------------------|---------------|-----------------|------------------|
| {variable} | {current} | [H/M/L] | {up/down} |

### King Midas Test Result

**Pattern detected:** YES/NO
**Explanation:** {why}
**Worst-case scenario:** {description}

### Recommendations

1. **Add uncertainty:** {recommendation}
2. **Add constraints:** {recommendation}
3. **Add oversight:** {recommendation}
4. **Reframe objective:** {recommendation}

### Conclusion

{Overall assessment and priority actions}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No clear objective stated | Ask for clarification on what the system optimizes |
| Objective too vague | Request specific metrics being measured |
| Multiple conflicting objectives | Analyze each separately, note tensions |
| Harmful system purpose | Refuse audit, explain constitutional constraint |

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
```
system_description: Auto-scaling service that manages cloud resources
stated_objectives: Minimize infrastructure cost while maintaining 99.9% uptime
optimization_pressure: High (cost optimization is primary KPI)
```

**Output:**

## Objective Misspecification Audit: Auto-Scaling Cost Optimizer

### Summary

| Dimension | Rating | Notes |
|-----------|--------|-------|
| Proxy-True Goal Alignment | 3/5 | Cost and uptime capture most but not all value |
| King Midas Risk | 2/5 | Bounded domain limits extreme scenarios |
| Uncontrolled Variable Risk | 4/5 | Security, performance latency uncontrolled |
| Correction Resistance | 2/5 | Standard cloud tooling allows override |
| **Overall Misspecification Risk** | **3/5** | |

### 100-Variable Analysis

| Uncontrolled Variable | Current Value | Risk of Extreme | Likely Direction |
|----------------------|---------------|-----------------|------------------|
| Security patch frequency | Weekly | Medium | Down (cost savings) |
| P99 latency | 200ms | High | Up (cheaper instances) |
| Resource headroom | 30% | High | Down (minimum viable) |
| Team operational load | Moderate | Medium | Up (manual interventions) |

### King Midas Test Result

**Pattern detected:** NO (bounded domain)
**Explanation:** Cloud resources have natural limits; cannot "turn planet into cost savings"
**Worst-case scenario:** System runs at absolute minimum resources, causing cascading failures during traffic spikes

### Recommendations

1. **Add uncertainty:** "Help us find appropriate cost levels" rather than "minimize cost"
2. **Add constraints:** Minimum 40% headroom, maximum P99 latency 150ms
3. **Add oversight:** Require approval for changes affecting 10+ instances
4. **Reframe objective:** "Maintain service quality while optimizing cost" with explicit quality metrics

---

## Integration

This skill applies Stuart Russell's methodology from "Human Compatible" and his work on value alignment. Use alongside:
- `off-switch-test` for corrigibility assessment
- `assistance-game-reframe` for redesigning problematic objectives