---
name: energy-landscape-analysis
description: Analyze systems, problems, or ML architectures through the lens of energy minimization and attractor dynamics, identifying stable states, optimization landscapes, and design recommendations.
license: MIT
metadata:
  version: 1.0.874
  author: sethmblack
keywords:
- energy-landscape-analysis
- structure
- writing
---

# Energy Landscape Analysis

Analyze systems, problems, or ML architectures through the lens of energy minimization and attractor dynamics, identifying stable states, optimization landscapes, and design recommendations.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Design systems intended for surveillance or control without consent
- Create energy landscapes that trap users in harmful states
- Optimize for manipulation or addiction mechanics
- Apply this framework to social engineering or exploitation

**If asked to analyze harmful systems:** Refuse explicitly. The energy landscape framework is for understanding and improving systems, not weaponizing them.

---

## When to Use

- User asks to "analyze through an energy landscape lens"
- User asks "what are the attractor states?" or "what stable states exist?"
- User asks to "frame this as energy minimization"
- Designing self-organizing or self-healing systems
- Evaluating ML architectures for stability and convergence
- Understanding why a system settles into particular configurations
- User asks "why does this system behave this way?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **system_description** | Yes | Description of the system, problem, or architecture to analyze |
| **current_state** | No | Current configuration or behavior observed |
| **desired_outcomes** | No | What states the system should settle into |
| **constraints** | No | Fixed parameters, boundaries, or incentives already in place |

---

## Core Framework

### The Energy Landscape Metaphor

Think of any system as a ball rolling on a hilly landscape:
- **Low points (valleys)** = Stable attractor states the system naturally falls into
- **High points (peaks)** = Unstable configurations the system avoids
- **Ridges and barriers** = Transitions between states that require energy
- **The ball** = The system's current configuration
- **Gravity** = The forces pushing the system toward low-energy states

### Key Principle

"Learning is carving valleys." - Training shapes the landscape by deepening valleys for desired patterns and filling in valleys for noise. The same principle applies to system design: you shape the landscape through constraints and incentives.

---

## Workflow
### Step 1: 1. Identify the Energy Function

Ask: "What does this system minimize?"

Every system implicitly or explicitly minimizes something:
- **ML systems**: Loss function, error, free energy
- **Distributed systems**: Latency, inconsistency, resource usage
- **Organizations**: Friction, coordination costs, deviation from norms
- **Self-healing systems**: Divergence from healthy state

**Output:** State the energy function in one sentence.

### Step 2: 2. Map the Attractor States

Ask: "What stable configurations does this system naturally fall into?"

Identify:
- **Desired attractors**: States you want the system to reach
- **Undesired attractors**: Local minima that trap the system
- **Basin sizes**: How large is the region that flows to each attractor?

**Output:** List each attractor with:
- Description of the state
- Whether it's desired or undesired
- Estimated basin size (narrow/medium/wide)

### Step 3: 3. Analyze the Landscape Topology

Ask: "What barriers exist between states?"

Identify:
- **Barrier heights**: How much energy to escape each attractor?
- **Transition paths**: How does the system move between states?
- **Saddle points**: Configurations where small changes cause big effects

**Output:** Describe the topology - is it smooth? Rugged? Are there many local minima?

### Step 4: 4. Design Landscape Modifications

Ask: "How can we shape the landscape?"

Options:
- **Deepen desired valleys**: Strengthen incentives for good states
- **Fill undesired valleys**: Add costs/penalties to bad states
- **Lower barriers**: Make transitions easier where helpful
- **Raise barriers**: Prevent unwanted transitions
- **Add stochastic exploration**: Temperature/noise to escape local minima (simulated annealing)

**Output:** Specific recommendations for shaping the landscape.

---

## Outputs

### Energy Landscape Analysis Report

```markdown
## Energy Landscape Analysis: {System Name}

### Energy Function
{What the system minimizes}

### Attractor Map

| Attractor | Type | Basin Size | Description |
|-----------|------|------------|-------------|
| {state 1} | Desired/Undesired | Narrow/Medium/Wide | {description} |

### Landscape Topology
{Description of barriers, transitions, ruggedness}

### Current State Assessment
{Where the system currently sits in the landscape}

### Recommendations

1. **{Action 1}**: {How to modify the landscape}
   - Effect: {What this changes}

2. **{Action 2}**: ...

### Biological Parallel (if applicable)
{How brains or natural systems solve similar problems}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| System has no clear energy function | Help identify implicit optimization target; every system minimizes something |
| Too many attractors to enumerate | Focus on most prominent 3-5; note that landscape is complex |
| System is chaotic (no stable attractors) | Note this explicitly; recommend adding stabilizing constraints |
| User wants guaranteed optimal state | Explain that landscapes often have multiple minima; recommend exploration strategies |
| Non-computational system | Framework still applies - identify what the system "settles into" naturally |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Additional Notes

**Best practices:**
- Use this skill when the situation clearly matches its intended use cases
- Combine with related skills for comprehensive analysis
- Iterate on outputs if initial results don't fully meet requirements

**Common variations:**
- Adjust the depth of analysis based on available time and information
- Scale the approach for different levels of complexity
- Adapt the output format to audience needs

**When to skip this skill:**
- The situation doesn't match the core use cases
- Simpler approaches would be more appropriate
- Time constraints require faster methods

## Example

**Input:**
```
System: A microservices architecture with circuit breakers
Current state: Services keep oscillating between healthy and degraded
Desired outcome: Stable healthy operation
```

**Output:**

## Energy Landscape Analysis: Circuit Breaker Microservices

### Energy Function
The system implicitly minimizes response latency while avoiding cascading failures.

### Attractor Map

| Attractor | Type | Basin Size | Description |
|-----------|------|------------|-------------|
| All services healthy | Desired | Narrow | Normal operation, low latency |
| Partial degradation | Undesired | Wide | Some circuit breakers open, services routing around failures |
| Cascade failure | Undesired | Medium | Multiple services down, circuit breakers all open |

### Landscape Topology
The landscape has a narrow, shallow valley for "healthy" surrounded by a wide basin for "partial degradation." The barrier between them is low - small latency spikes push the system out of healthy state. Recovery requires coordinated reset, creating a high barrier back.

### Current State Assessment
System is trapped in the "partial degradation" attractor - the basin is wide enough that random fluctuations keep it there.

### Recommendations

1. **Deepen the healthy valley**: Add health check bonuses - services get priority routing when fully healthy
   - Effect: Makes healthy state more stable against perturbation

2. **Narrow the degradation basin**: Implement gradual circuit breaker recovery instead of binary open/closed
   - Effect: Creates smoother path back to healthy state

3. **Add coordinated annealing**: Implement periodic "health reset windows" where all services attempt recovery simultaneously
   - Effect: Allows escape from local minimum through coordinated exploration

### Biological Parallel
The brain uses similar attractor dynamics for memory recall - memories are valleys, and recall is rolling toward the nearest learned attractor. Sleep provides the "annealing" phase where the landscape is reorganized and weak attractors are pruned.

---

## Integration

This skill integrates with the **terry-sejnowski** expert voice. When using this skill, embody:
- Physics-based thinking about computation
- Bridging between biological and artificial systems
- Respect for how nature solves similar problems
- The insight that "there are few complex systems that scale this well"

---

## Success Criteria

Analysis is complete when:
- [ ] Energy function clearly identified
- [ ] Major attractors mapped with basin sizes
- [ ] Landscape topology described
- [ ] Actionable recommendations provided
- [ ] Biological parallel offered (when applicable)