---
name: circumscription-default-reasoning
description: Apply circumscription to formalize default assumptions and abnormality predicates - enabling systems that assume normalcy, detect exceptions, and retract conclusions when new information arrives.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3597
repository: https://github.com/sethmblack/paks-skills
keywords:
- circumscription-default-reasoning
- writing
---

# Circumscription Default Reasoning

Apply circumscription to formalize default assumptions and abnormality predicates - enabling systems that assume normalcy, detect exceptions, and retract conclusions when new information arrives.

**Token Budget:** ~850 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Formalize defaults that encode harmful biases or discrimination
- Create abnormality predicates for malicious detection systems
- Design default reasoning for deception or manipulation
- Skip explicit documentation of retraction conditions

**If asked to formalize harmful defaults:** Refuse explicitly. State what you cannot formalize and why.

---

## When to Use

- User asks "What are the default assumptions here?"
- User says "When should we assume normal vs. abnormal?"
- User requests "Apply circumscription to..."
- User asks "Model default reasoning for..."
- When designing alerting and monitoring systems
- When creating exception handling policies
- When building systems that must act on incomplete information

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **domain_description** | Yes | The domain or system to analyze |
| **normal_cases** | No | What should be assumed in the absence of evidence |
| **known_exceptions** | No | Already-known abnormal cases |
| **information_sources** | No | How abnormalities will be detected |

**Input Validation:**
- If domain_description lacks context about what "normal" means, ask for clarification
- If exceptions list is empty, probe: "What could go wrong?"

---

## Core Concepts

**Circumscription:** Formalizing the assumption that things are normal unless stated otherwise. We minimize abnormality.

**Default Assumption:** What we conclude in the absence of information to the contrary. "Birds fly" is a default; penguins are exceptions.

**Abnormality Predicate:** `Ab(x, property)` marks x as abnormal with respect to property. If not Ab(tweety, flying), conclude tweety can fly.

**Nonmonotonic Reasoning:** Unlike classical logic, adding information can cause conclusions to be **withdrawn**. Learning tweety is a penguin retracts "tweety can fly."

---

## Workflow

### Step 1: Identify the Domain Defaults

What should be assumed true in the normal case?

```
Default Assumptions:
1. {default1}: In the absence of evidence to the contrary, assume {X}
   - Rationale: {why this is the reasonable default}

2. {default2}: In the absence of evidence to the contrary, assume {Y}
   - Rationale: {why this is the reasonable default}
```

Ask: "What would a reasonable person assume without being told otherwise?"

### Step 2: Define Abnormality Predicates

For each default, what makes something abnormal?

```
Abnormality Predicates:
- Ab({entity}, {property}): {entity} is abnormal with respect to {property}
  - Triggers: {conditions that set Ab to true}
  - Example: Ab(service, healthy) when healthcheck fails
```

### Step 3: Specify Detection Mechanisms

How do we learn about abnormalities?

```
Detection Sources:
1. {source1}: Detects {abnormality type}
   - Signal: {what we observe}
   - Confidence: {how reliable is this source}
   - Latency: {how quickly do we learn}

2. {source2}: Detects {abnormality type}
   ...
```

### Step 4: Define Retraction Conditions

When do we withdraw our conclusions?

```
Retraction Rules:
1. IF {new_information} THEN retract {previous_conclusion}
   - New conclusion: {what we now believe}
   - Reason: {why the new info changes things}

2. IF {abnormality_resolves} THEN retract Ab({entity}, {property})
   - New conclusion: {entity} is normal again
   - Evidence required: {what proves normality restored}
```

### Step 5: Identify Edge Cases

Where might default reasoning fail?

```
Edge Cases:
1. {scenario}: Default assumption leads to wrong conclusion
   - Why: {explanation}
   - Mitigation: {how to handle}

2. {scenario}: Detection mechanism misses abnormality
   - Why: {explanation}
   - Mitigation: {how to handle}
```

### Step 6: Document Minimization Strategy

How do we minimize abnormality?

```
Minimization:
- Only mark Ab(x, property) = true when evidence supports it
- Prefer explanations with fewer abnormalities
- If multiple explanations exist, choose the one minimizing Ab predicates
```

---

## Outputs

### Circumscription Analysis Report

```markdown
## Circumscription Analysis: {Domain Name}

### 1. Domain Overview
{One paragraph describing why default reasoning matters here}

### 2. Default Assumptions
| # | Default | Rationale | Applicable When |
|---|---------|-----------|-----------------|
| 1 | {default} | {why} | {conditions} |

### 3. Abnormality Predicates
| Predicate | Meaning | Triggers |
|-----------|---------|----------|
| Ab(x, property) | {meaning} | {what sets it true} |

### 4. Detection Mechanisms
| Source | Detects | Confidence | Latency |
|--------|---------|------------|---------|
| {source} | {what} | {high/med/low} | {time} |

### 5. Retraction Rules
| Trigger | Retract | New Conclusion |
|---------|---------|----------------|
| {info} | {old} | {new} |

### 6. Edge Cases and Mitigations
| Edge Case | Risk | Mitigation |
|-----------|------|------------|
| {case} | {risk} | {mitigation} |

### 7. Implementation Recommendations
- {recommendation 1}
- {recommendation 2}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No clear defaults exist | Ask what should be assumed without information |
| Defaults conflict | Flag the conflict and ask for priority ordering |
| Detection unreliable | Document confidence levels; recommend redundant sources |
| Retraction impossible | Flag as "sticky state" - once abnormal, manual reset needed |
| Too many abnormality types | Group into categories; prioritize high-impact ones |

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
domain_description: "Service health monitoring and alerting"
normal_cases: "Services are healthy"
known_exceptions: "Network partitions, resource exhaustion, dependency failures"
information_sources: "Prometheus metrics, health endpoints, log aggregation"
```

**Output:**

## Circumscription Analysis: Service Health Monitoring

### 1. Domain Overview
Service health monitoring must balance two concerns: not alerting on transient issues (alert fatigue) and not missing genuine problems (silent failures). Circumscription provides a principled approach: assume services are healthy unless evidence indicates otherwise, with well-defined retraction when issues resolve.

### 2. Default Assumptions
| # | Default | Rationale | Applicable When |
|---|---------|-----------|-----------------|
| 1 | Services are healthy | The purpose of services is to serve; unhealthy is the exception | No alerts firing |
| 2 | Network is connected | Partitions are rare; most requests succeed | No connectivity alerts |
| 3 | Dependencies are available | Upstream services designed for high availability | No dependency alerts |
| 4 | Resources are sufficient | Capacity planning targets normal load | Usage < 80% threshold |

### 3. Abnormality Predicates
| Predicate | Meaning | Triggers |
|-----------|---------|----------|
| Ab(service, healthy) | Service is unhealthy | Failed health check (3 consecutive) |
| Ab(service, connected) | Service has network issues | Connection timeout to dependencies |
| Ab(service, resourced) | Service lacks resources | CPU/memory > 90% for 5 minutes |
| Ab(dependency, available) | Upstream is down | Dependency health check fails |

### 4. Detection Mechanisms
| Source | Detects | Confidence | Latency |
|--------|---------|------------|---------|
| Health endpoint | Ab(service, healthy) | High | 10s |
| Prometheus CPU/mem | Ab(service, resourced) | High | 60s |
| Connection metrics | Ab(service, connected) | Medium | 30s |
| Error rate spike | Ab(service, healthy) | Medium | 60s |
| Log patterns | Multiple | Low-Medium | 120s |

### 5. Retraction Rules
| Trigger | Retract | New Conclusion |
|---------|---------|----------------|
| 3 consecutive healthy checks | Ab(service, healthy) | Service is healthy |
| Resource usage < 70% for 5m | Ab(service, resourced) | Resources sufficient |
| No connection errors for 2m | Ab(service, connected) | Network normal |
| Dependency recovers | Ab(dependency, available) | Dependency available |

### 6. Edge Cases and Mitigations
| Edge Case | Risk | Mitigation |
|-----------|------|------------|
| Flapping service (rapid healthy/unhealthy) | Alert storm | Add hysteresis: 3 failures to alert, 5 successes to clear |
| Partial failure (some pods unhealthy) | Missed detection | Alert on percentage threshold, not all-or-nothing |
| Silent corruption (serving wrong data) | Default assumption wrong | Add semantic health checks, not just liveness |
| Cascading failures | Root cause obscured | Alert on first abnormality; correlate dependencies |

### 7. Implementation Recommendations
1. **Implement hysteresis**: Require multiple consecutive signals before changing Ab state
2. **Use confidence weighting**: High-confidence sources (health checks) override low-confidence (logs)
3. **Log all state transitions**: Record when Ab predicates change and why
4. **Define SLOs as defaults**: "99.9% available" is the default; violations trigger Ab
5. **Automate retraction**: Don't require manual intervention to clear Ab when evidence supports normalcy

---

## Integration

This skill is part of the **john-mccarthy** expert methodology. It applies McCarthy's circumscription - his formalization of default reasoning and the "closed world assumption" - to practical monitoring and alerting systems.

The key insight is **nonmonotonic reasoning**: conclusions can be withdrawn when new information arrives. This is how human common sense works (we assume normalcy until proven otherwise) and how robust systems should work.

Channel McCarthy: "Assume things are normal unless you have evidence to the contrary. But be precise about what 'normal' means and what evidence would change your mind."