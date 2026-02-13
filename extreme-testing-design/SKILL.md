---
name: extreme-testing-design
description: 'Design stress tests that push systems to breaking points, compressing months of learning into days through extreme conditions. Racing is R&D: the track teaches what the workshop cannot.'
license: MIT
metadata:
  author: sethmblack
  version: 1.0.936
repository: https://github.com/sethmblack/paks-skills
keywords:
- compression
- extreme-testing-design
- structure
- writing
---

# Extreme Testing Design

Design stress tests that push systems to breaking points, compressing months of learning into days through extreme conditions. Racing is R&D: the track teaches what the workshop cannot.

**Token Budget:** ~650 tokens
**Origin:** Soichiro Honda methodology (Isle of Man TT / Racing as R&D)

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Design tests that risk production data or user safety without explicit safeguards
- Recommend extreme testing without rollback and recovery plans
- Push systems past safe limits without isolation from real users
- Use extreme testing to intentionally cause outages presented as accidents
- Design tests that could expose sensitive data or create security vulnerabilities

**If asked to design unsafe extreme tests:** Refuse explicitly. Honda raced on the Isle of Man, not on public roads. Extreme testing requires controlled conditions and safety boundaries.

---

## When to Use

- Pre-launch reliability validation needed
- Chaos engineering program design
- Game day planning
- User says "how do we know it's reliable?"
- System has not been tested under extreme conditions
- New architecture or major changes need validation
- Team is overconfident about system resilience

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| system | Yes | The system, service, or process to test |
| known_weaknesses | No | Suspected or known failure modes |
| production_conditions | No | Normal load, traffic patterns, usage |
| risk_tolerance | No | What failures are acceptable during testing |

---

## Workflow

### Step 1: Define the Racing Conditions

Identify what "extreme" means for this system:

| Dimension | Normal | Extreme | TT-Level |
|-----------|--------|---------|----------|
| Load (requests/sec) | | 2x normal | 10x normal |
| Data volume | | 2x normal | 10x normal |
| Failure rate (dependencies) | | 10% failure | 50% failure |
| Latency (dependencies) | | 2x normal | 10x normal |
| Resource constraints | | 50% capacity | 25% capacity |

The Isle of Man TT compressed years of learning into days because conditions were extreme: speeds, road surfaces, weather, and duration far exceeded normal use.

### Step 2: Identify Learning Objectives

What do we want the test to teach us?

| Objective | Question to Answer |
|-----------|-------------------|
| Failure modes | Where does the system break first? |
| Degradation patterns | How does it fail? Gracefully or catastrophically? |
| Recovery behavior | How does it recover after failure? |
| Observability gaps | What did we fail to monitor? |
| Capacity limits | What are the actual limits vs. theoretical? |

### Step 3: Design Safety Boundaries

Extreme testing requires safety rails:

| Boundary | Specification |
|----------|---------------|
| Isolation | How is this separated from production? |
| Blast radius | Maximum impact if test causes failure |
| Kill switch | How to stop the test immediately |
| Rollback plan | How to recover if something goes wrong |
| Communication | Who knows the test is running |

Honda raced at the TT, but he brought a team, spare parts, and a pit crew. Extreme testing is controlled extremity.

### Step 4: Build the Test Scenarios

Design specific scenarios to execute:

| Scenario | Conditions | Expected Behavior | Learning if Fails |
|----------|------------|-------------------|-------------------|
| Load spike | [Specific conditions] | [What should happen] | [What we learn] |
| Dependency failure | [Specific conditions] | [What should happen] | [What we learn] |
| Resource exhaustion | [Specific conditions] | [What should happen] | [What we learn] |
| Cascading failure | [Specific conditions] | [What should happen] | [What we learn] |

### Step 5: Plan Post-Test Analysis

The race is only valuable if you analyze the results:

| Analysis | Method |
|----------|--------|
| Failure point identification | [How to find where it broke] |
| Degradation documentation | [How to capture failure sequence] |
| Recovery time measurement | [How to measure MTTR] |
| Observability audit | [What metrics were missing] |
| Team retrospective | [How to capture human learnings] |

---

## Outputs

Format the test design as:

```markdown
## Extreme Testing Design: [System Name]

### Racing Conditions

| Dimension | Normal | Test Level | Justification |
|-----------|--------|------------|---------------|
| [Dimension] | [Baseline] | [Extreme value] | [Why this extreme] |

### Learning Objectives

| # | Question to Answer |
|---|-------------------|
| 1 | [What the test will teach us] |
| 2 | [What the test will teach us] |

### Safety Boundaries

| Boundary | Specification |
|----------|---------------|
| Isolation | [How test is separated from production] |
| Blast radius | [Maximum possible impact] |
| Kill switch | [How to stop immediately] |
| Rollback | [Recovery procedure] |

### Test Scenarios

| Scenario | Conditions | Expected | Learning if Fails |
|----------|------------|----------|-------------------|
| [Name] | [Setup] | [Behavior] | [What we learn] |

### Post-Test Analysis Plan

| Analysis | Method |
|----------|--------|
| [Type] | [How to perform] |

### Honda Principle Applied

> "The race track teaches in one weekend what would take ten years to learn in ordinary use."

[How this test design compresses learning through extreme conditions]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No safe isolation available | Start smaller: synthetic load in staging, not chaos in production |
| Stakeholders resist extreme testing | Frame as risk reduction: better to find breaks in tests than production |
| Unknown failure modes | Good - that is what the test will reveal; design for observation, not prediction |
| Previous tests passed easily | Tests were not extreme enough; increase severity until failure occurs |
| Test reveals too many problems | Prioritize by blast radius; fix the catastrophic failures first |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "Design a stress test for our payment processing service before Black Friday."

**Output excerpt:**
```markdown


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


## Extreme Testing Design: Payment Processing Service

### Racing Conditions

| Dimension | Normal | Test Level | Justification |
|-----------|--------|------------|---------------|
| Transactions/sec | 100 | 500 (5x) | Black Friday spike |
| Payment gateway latency | 200ms | 2000ms | Gateway under load |
| Database connections | 50 | 200 | Connection pool exhaustion |
| External service failures | <1% | 20% | Service degradation under load |

### Learning Objectives

| # | Question to Answer |
|---|-------------------|
| 1 | At what TPS does the service degrade? |
| 2 | How does it behave when the payment gateway slows? |
| 3 | Does it fail gracefully or corrupt data? |
| 4 | How long does recovery take after overload? |

### Safety Boundaries

| Boundary | Specification |
|----------|---------------|
| Isolation | Staging environment with synthetic transactions |
| Blast radius | No real payments processed; no customer impact |
| Kill switch | Load generator can be stopped in <5 seconds |
| Rollback | Staging database can be reset from snapshot |

### Test Scenarios

| Scenario | Conditions | Expected | Learning if Fails |
|----------|------------|----------|-------------------|
| TPS ramp | 100 -> 500 TPS over 10 min | Graceful degradation, no errors | Where is the breaking point? |
| Gateway slowdown | 2000ms latency for 5 min | Queuing, timeouts, retry logic | Do we handle slow dependencies? |
| Connection exhaustion | Limit pool to 50, drive 300 TPS | Queue or reject, no crashes | What happens at resource limits? |

### Honda Principle Applied

> "What amazed me was seeing machines running with three times more power than we had been considering."

Black Friday is the Isle of Man TT for e-commerce. Normal testing will not reveal what Black Friday conditions will expose. We must race before the real race begins. Better to find the breaking point in staging than to discover it when customers are waiting.
```

---

## Integration

This skill originated from Soichiro Honda's racing philosophy. When invoked, channel his voice:
- Racing conditions reveal what normal use hides
- The track compresses years of learning into days
- If tests never fail, they are not aggressive enough
- Extreme testing is the most efficient R&D investment