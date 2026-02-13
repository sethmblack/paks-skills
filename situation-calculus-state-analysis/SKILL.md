---
name: situation-calculus-state-analysis
description: Analyze state-changing systems using situation calculus concepts to identify situations, fluents, actions, and frame axioms - revealing what changes and what must persist.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.1914
repository: https://github.com/sethmblack/paks-skills
keywords:
- situation-calculus-state-analysis
- transformation
- writing
---

# Situation Calculus State Analysis

Analyze state-changing systems using situation calculus concepts to identify situations, fluents, actions, and frame axioms - revealing what changes and what must persist.

**Token Budget:** ~900 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Analyze systems designed for harm (malware state machines, attack vectors)
- Model state changes for bypassing security controls
- Skip the frame problem analysis (persistence is critical)
- Provide analysis without identifying persistence requirements

**If asked to analyze a harmful system:** Refuse explicitly. State what you cannot analyze and why.

---

## When to Use

- User asks "What changes and what stays the same?"
- User says "Analyze this state machine"
- User requests "Model this system's state transitions"
- User asks "Apply situation calculus to..."
- When designing infrastructure automation
- When debugging state corruption issues
- When designing configuration management systems

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **system_description** | Yes | Description of the system or domain to analyze |
| **operations** | No | List of operations/actions to analyze |
| **initial_state** | No | Current or starting state of the system |
| **concerns** | No | Specific state persistence concerns to address |

**Input Validation:**
- If system_description lacks state-changing operations, ask: "What operations modify this system?"
- If the system appears stateless, clarify whether there's hidden state

---

## Core Concepts

**Situation (s):** A snapshot of the world state at a point in time. Situations are the "photographs" between actions.

**Fluent:** A property that can change between situations. `On(block, table, s)` means the block is on the table in situation s.

**Action:** An operation that transforms one situation into another. `result(action, s)` gives the new situation.

**Frame Axiom:** A statement about what does NOT change when an action occurs. The frame problem is the challenge of representing all the things that stay the same.

---

## Workflow

### Step 1: Identify Situations

Enumerate the distinct world states relevant to this system:

```
Situations:
- S0: {initial state description}
- S1: {state after action A}
- S2: {state after action B}
...
```

Ask: What are the meaningful "snapshots" of this system?

### Step 2: Identify Fluents

List all properties that can change between situations:

```
Fluents (Properties that Change):
- {fluent1}(entity, situation): {description}
- {fluent2}(entity, situation): {description}
...
```

Ask: What properties are NOT constant? What can be in different states at different times?

### Step 3: Map Actions

For each operation, specify:

```
Action: {action_name}
- Preconditions: {what must be true in s for action to be possible}
- Effects: {what becomes true in result(action, s)}
- Affected Fluents: {which fluents change}
```

### Step 4: Analyze Frame Problem

This is critical. For each fluent:

```
Frame Analysis for {fluent}:
- Changes when: {list of actions that affect this fluent}
- Persists when: {all other actions - explicitly state this}
- Frame axiom: "If action A does not affect {fluent}, then {fluent}(x, result(A, s)) = {fluent}(x, s)"
```

Ask: "For this action, what unexpectedly might NOT persist?"

### Step 5: Identify Potential Frame Violations

Look for cases where persistence assumptions might fail:

```
Potential Frame Violations:
1. {scenario where something unexpectedly changes}
   - Expected: {fluent} persists
   - Risk: {why it might not}
   - Mitigation: {how to ensure persistence}
```

### Step 6: Summarize State Transition Table

```
| Situation | Action | Result | Changed Fluents | Preserved Fluents |
|-----------|--------|--------|-----------------|-------------------|
| S0 | A1 | S1 | f1, f2 | f3, f4, f5 |
| S1 | A2 | S2 | f3 | f1, f2, f4, f5 |
```

---

## Outputs

### Situation Calculus Analysis Report

```markdown
## Situation Calculus Analysis: {System Name}

### 1. System Overview
{One paragraph describing the system and why state analysis matters}

### 2. Situations
| Situation | Description | Key Properties |
|-----------|-------------|----------------|
| S0 | {desc} | {props} |
| S1 | {desc} | {props} |

### 3. Fluents
| Fluent | Type | Description |
|--------|------|-------------|
| {fluent}(entity, s) | {boolean/value} | {what it represents} |

### 4. Actions
| Action | Preconditions | Effects | Affected Fluents |
|--------|---------------|---------|------------------|
| {A1} | {pre} | {eff} | {fluents} |

### 5. Frame Axioms
| Fluent | Persists Unless |
|--------|-----------------|
| {f1} | {actions that change it} |

### 6. Frame Problem Analysis
**Potential Issues:**
- {issue 1}: {description and risk}
- {issue 2}: {description and risk}

**Mitigations:**
- {mitigation 1}
- {mitigation 2}

### 7. State Transition Summary
{Diagram or table showing situation transitions}

### 8. Recommendations
- {recommendation for ensuring state consistency}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No clear state changes | Ask what operations modify the system |
| Too many fluents to enumerate | Focus on user-specified concerns first |
| Circular dependencies | Flag them and recommend resolution |
| Missing preconditions | Note actions that might fail silently |
| Frame violations inevitable | Document them as known risks |

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
system_description: "A Kubernetes deployment controller"
operations: ["scale", "rollout", "rollback"]
concerns: "We keep losing environment variables after rollouts"
```

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


## Situation Calculus Analysis: K8s Deployment Controller

### 1. System Overview
The deployment controller manages pods for a service, transitioning between versions while maintaining availability. State analysis is critical because rollouts involve multiple intermediate states where pods of different versions coexist.

### 2. Situations
| Situation | Description | Key Properties |
|-----------|-------------|----------------|
| S0 | Stable V1 | All pods V1, healthy |
| S1 | Rollout started | Mixed V1/V2 pods |
| S2 | Rollout complete | All pods V2, healthy |
| S3 | Rollback triggered | Reverting to V1 |

### 3. Fluents
| Fluent | Type | Description |
|--------|------|-------------|
| PodVersion(pod, v, s) | string | Version running on pod in situation s |
| PodCount(deployment, n, s) | int | Number of pods in situation s |
| EnvVars(pod, vars, s) | map | Environment variables on pod in s |
| ConfigMapRef(deployment, cm, s) | ref | ConfigMap referenced by deployment |
| SecretRef(deployment, sec, s) | ref | Secret referenced by deployment |

### 4. Actions
| Action | Preconditions | Effects | Affected Fluents |
|--------|---------------|---------|------------------|
| Scale(n) | n >= 0 | PodCount := n | PodCount |
| Rollout(v2) | Image exists | PodVersion of new pods := v2 | PodVersion |
| Rollback | Previous version known | PodVersion := v_prev | PodVersion |

### 5. Frame Axioms
| Fluent | Persists Unless |
|--------|-----------------|
| EnvVars | **PROBLEM: May NOT persist across Rollout if defined inline** |
| ConfigMapRef | Persists (external resource) |
| SecretRef | Persists (external resource) |
| PodCount | Scale |

### 6. Frame Problem Analysis
**Potential Issues:**
- **EnvVars Loss on Rollout**: If environment variables are defined inline in the pod spec rather than via ConfigMapRef, a new deployment manifest might not include them. The Rollout action affects PodVersion but the **implicit assumption** that EnvVars persists is FALSE.
  - Root cause: Frame axiom violation - EnvVars is coupled to manifest, not just pod
  - Risk: Production outage from missing config

**Mitigations:**
- Define all EnvVars via ConfigMap/Secret references (externalize state)
- Add validation webhook that rejects deployments removing existing EnvVars
- Implement deployment diff check before rollout

### 7. State Transition Summary
```
S0 (V1 stable) --[Rollout(V2)]--> S1 (mixed) --[complete]--> S2 (V2 stable)
       ^                                                            |
       +----------------------[Rollback]----------------------------+
```

### 8. Recommendations
1. **Externalize all configuration** to ConfigMaps/Secrets so they persist independently of deployment manifests
2. **Add frame axiom enforcement**: Pre-rollout check that all fluents expected to persist are still present in new manifest
3. **Implement state audit**: After rollout, verify EnvVars match expected set

---

## Integration

This skill is part of the **john-mccarthy** expert methodology. It applies McCarthy's situation calculus - the formal language he developed for reasoning about actions and change - to practical infrastructure problems.

The key insight is the **frame problem**: most things stay the same when actions occur, but we must explicitly identify what persists. McCarthy showed this is surprisingly difficult, and infrastructure outages often result from violated persistence assumptions.

Channel McCarthy: "For each action, ask: what stays the same? If you cannot answer precisely, you do not understand the action."