---
name: formal-problem-specification
description: Transform vague problem descriptions into precise formal specifications with defined domains, states, actions, and constraints before attempting solutions.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.989
repository: https://github.com/sethmblack/paks-skills
keywords:
- formal-problem-specification
- transformation
- writing
---

# Formal Problem Specification

Transform vague problem descriptions into precise formal specifications with defined domains, states, actions, and constraints before attempting solutions.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for specification output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Formalize problems designed to cause harm (exploitation, deception, damage)
- Create specifications that bypass security controls
- Formalize social engineering or manipulation tactics
- Skip the precision step and provide vague specifications

**If asked to formalize a harmful problem:** Refuse explicitly. State what you cannot specify and why.

---

## When to Use

- User asks "What exactly do we mean by...?"
- User says "Define this problem precisely"
- User requests "Formally specify this problem"
- Before designing a solution to an ambiguous problem
- When disagreements arise from unclear terminology
- When building systems that require precise specifications

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **problem_description** | Yes | The informal, vague, or ambiguous problem statement |
| **domain_context** | No | What area this applies to (infrastructure, software, business) |
| **constraints** | No | Known requirements or limitations |
| **stakeholders** | No | Who cares about this problem being solved |

**Input Validation:**
- If problem_description is empty or too vague to analyze, ask for clarification
- If domain is unclear, ask: "What domain is this problem in?"

---

## Workflow

### Step 1: Identify Undefined Terms

List every term in the problem description that could be interpreted multiple ways:
- What does "{X}" mean exactly?
- Is "{Y}" the same as "{Z}"?
- What are the boundaries of "{concept}"?

**Output:** List of ambiguous terms with questions.

### Step 2: Define the Domain

Specify the entities and their properties:

```
Domain: {name}
Entities:
- {Entity1}: {definition}
  Properties: {property1}, {property2}
- {Entity2}: {definition}
  Properties: {property1}, {property2}

Relationships:
- {Entity1} relates to {Entity2} via {relationship}
```

### Step 3: Define Initial State

What do we know at the start?

```
Initial State (S0):
- {proposition1} is true
- {proposition2} is true
- Unknown: {what we don't know}
```

### Step 4: Define Goal State

What does success look like, precisely?

```
Goal State (Sg):
- {goal_proposition1} must be true
- {goal_proposition2} must be true
- Acceptance criteria: {measurable criteria}
```

### Step 5: Enumerate Actions

What operations can we perform?

```
Actions:
1. {Action1}
   - Preconditions: {what must be true before}
   - Effects: {what changes after}
   - Postconditions: {what must be true after}

2. {Action2}
   - Preconditions: ...
   - Effects: ...
   - Postconditions: ...
```

### Step 6: Identify Constraints (Frame Axioms)

What must remain true throughout?

```
Invariants:
- {constraint1}: {description}
- {constraint2}: {description}

Frame Axioms (what doesn't change):
- {property} persists unless explicitly modified by {action}
```

### Step 7: Resolve Ambiguities

For each ambiguous term from Step 1:
- Proposed definition: {definition}
- Rationale: {why this definition}
- Alternative interpretations: {what we're NOT including}

---

## Outputs

### Formal Problem Specification

```markdown
## Formal Problem Specification: {Problem Name}

### 1. Problem Statement (Precise)
{One paragraph restating the problem with all ambiguities resolved}

### 2. Domain
**Entities:**
| Entity | Definition | Properties |
|--------|------------|------------|
| {E1} | {def} | {props} |

**Relationships:**
- {relationship descriptions}

### 3. States
**Initial State (S0):**
- {propositions}

**Goal State (Sg):**
- {propositions}
- Acceptance Criteria: {measurable}

### 4. Actions
| Action | Preconditions | Effects |
|--------|---------------|---------|
| {A1} | {pre} | {eff} |

### 5. Constraints
**Invariants:** {what must always be true}
**Frame Axioms:** {what persists}

### 6. Resolved Ambiguities
| Term | Definition | Rationale |
|------|------------|-----------|
| {term} | {def} | {why} |

### 7. Open Questions
- {questions that still need stakeholder input}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Problem too vague to start | Ask 3 specific clarifying questions |
| Multiple valid interpretations | Present alternatives and ask stakeholder to choose |
| Domain unknown | Ask for domain context |
| Constraints conflict | Highlight the conflict and ask for resolution |
| Problem changes during specification | Re-run from Step 1 with updated description |

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
problem_description: "We need to make deployments more reliable"
domain_context: "Kubernetes-based microservices"
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


## Formal Problem Specification: Deployment Reliability

### 1. Problem Statement (Precise)
Given a Kubernetes cluster running N microservices, when a new version of service S is deployed, the deployment should complete without causing service degradation (defined as >1% error rate or >500ms p99 latency increase) for existing traffic, and should automatically roll back if degradation is detected within M minutes.

### 2. Domain
**Entities:**
| Entity | Definition | Properties |
|--------|------------|------------|
| Service | A deployable unit with version V | version, replicas, healthCheck |
| Cluster | K8s cluster hosting services | services[], loadBalancer |
| Deployment | Act of updating service version | targetVersion, strategy |
| HealthCheck | Validation of service state | endpoint, threshold, interval |

**Relationships:**
- Cluster contains Services
- Deployment targets one Service
- Service has HealthChecks

### 3. States
**Initial State (S0):**
- Service S running version V1 with R replicas
- All replicas passing health checks
- Error rate < 1%, p99 latency < baseline

**Goal State (Sg):**
- Service S running version V2 with R replicas
- All replicas passing health checks
- Error rate < 1%, p99 latency < baseline + 500ms
- Deployment marked "successful"

### 4. Actions
| Action | Preconditions | Effects |
|--------|---------------|---------|
| StartRollingUpdate | Service healthy, image exists | Begins replacing pods |
| WaitForHealthy | Pods starting | Blocks until health checks pass |
| PromoteCanary | Canary healthy for N minutes | Increases canary percentage |
| Rollback | Degradation detected | Reverts to previous version |
| MarkComplete | All pods V2, healthy | Records success |

### 5. Constraints
**Invariants:** At least 1 healthy replica available at all times
**Frame Axioms:** Other services unaffected by this deployment; persistent volumes unchanged

### 6. Resolved Ambiguities
| Term | Definition | Rationale |
|------|------------|-----------|
| "reliable" | <1% error rate, <500ms latency increase, auto-rollback | Measurable SLO |
| "deployment" | Rolling update with canary, not big-bang | Industry practice |
| "degradation" | Error rate or latency exceeds threshold | Observable metrics |

### 7. Open Questions
- What is the rollback timeout (M minutes)?
- What percentage of traffic should go to canary initially?
- Who should be notified on rollback?

---

## Integration

This skill is part of the **john-mccarthy** expert methodology. It embodies McCarthy's insistence that:
- "If you cannot write it down formally, you do not yet understand it"
- Problems must be precisely defined before solutions are attempted
- Vagueness is not depth; precision reveals what actually needs to be solved

When using this skill, channel McCarthy's commitment to **definitional rigor**: every term should have a meaning you can point to.