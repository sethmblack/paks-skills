---
name: society-decomposition
description: Decompose any complex system behavior into a "society" of interacting simple agents, revealing how intelligence emerges from non-intelligence.
license: MIT
metadata:
  version: 1.0.1929
  author: sethmblack
keywords:
- society-decomposition
- writing
---

# Society Decomposition

Decompose any complex system behavior into a "society" of interacting simple agents, revealing how intelligence emerges from non-intelligence.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Decompose systems designed for malware, exploitation, or deception
- Analyze systems in ways that could enable harm
- Fabricate agents without grounding in observable behavior

**If asked to decompose a harmful system:** Refuse explicitly. State that you cannot analyze systems designed for harm.

---

## When to Use

- User asks "Decompose this system into agents"
- User asks "How does this intelligent behavior actually work?"
- User asks "What simple processes produce this complex output?"
- When facing a monolithic system that seems to exhibit "intelligence"
- When debugging why a complex system behaves unexpectedly
- When designing a new system that needs distributed intelligence

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **system_description** | Yes | What the system does, its components, or observed behavior |
| **apparent_intelligence** | No | What the system seems to do "as a whole" (will be inferred if not provided) |
| **constraints** | No | Known requirements, limitations, or boundaries |

---

## Workflow
### Step 1: 1. Identify the Apparent Intelligence

First, state what the system appears to do as a unified whole. What would make someone call it "intelligent" or "complex"?

**Key questions:**
- What capability seems impressive or mysterious?
- What would require intelligence if a human did it?
- What is the system being credited with that sounds like a single ability?

### Step 2: 2. List Candidate Agents

Decompose into 5-10 simpler processes. Each agent should:
- Do exactly ONE simple thing
- Be mindless on its own (no agent is intelligent by itself)
- Have clear inputs and outputs
- Be nameable with a function (e.g., "detector", "classifier", "executor")

**Template for each agent:**
```
Agent: {name}
Function: {what it does - one sentence}
Inputs: {what it receives}
Outputs: {what it produces}
```

### Step 3: 3. Map Interactions

Determine how agents communicate, compete, or cooperate:
- **Communication:** What information flows between agents?
- **Competition:** Which agents might conflict?
- **Cooperation:** Which agents depend on each other's outputs?

Create an interaction diagram or list showing dependencies.

### Step 4: 4. Identify the Coordinator

Find what manages conflicts between agents:
- What happens when two agents disagree?
- Is there a higher-level agent that arbitrates?
- Are there censor agents that veto bad ideas early?
- Are there suppressor agents that stop actions at the last moment?

**Note:** The coordinator is often implicit. Make it explicit.

### Step 5: 5. Trace Emergent Behavior

Explain how the whole arises from parts:
- Walk through a specific scenario
- Show how each agent contributes
- Point to where "intelligence" appears to reside

**Critical insight:** The intelligence resides nowhere and everywhere. It emerges from the interaction, not from any single agent.

### Step 6: 6. Deliver Practical Recommendations

Based on the decomposition:
- Which agents are missing or weak?
- Where are the bottlenecks or failure points?
- What would improve the society's overall behavior?
- How can this decomposition guide debugging or enhancement?

---

## Outputs

Format output as:

```markdown
## Society Decomposition: {System Name}

### Apparent Intelligence
{What the system seems to do as a whole}

### Agent Society

| Agent | Function | Inputs | Outputs |
|-------|----------|--------|---------|
| {name} | {one-line function} | {inputs} | {outputs} |
| ... | ... | ... | ... |

### Interaction Map

{Diagram or description of how agents communicate/compete/cooperate}

### Coordinator Analysis

{What manages conflicts, vetoes, or arbitration}

### Emergent Behavior Trace

{Walk-through showing how intelligence emerges from interactions}

### Recommendations

- {Recommendation 1}
- {Recommendation 2}
- {Recommendation 3}

### Key Insight

The "intelligence" of {system} is not located in any single component. It emerges from the interaction of {N} simple agents, each mindless alone.
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| System too vague | Ask for specific behaviors or examples |
| No apparent intelligence | Note that system may already be well-decomposed; analyze for optimization |
| Cannot identify agents | Try different granularity; some systems are genuinely atomic |
| Circular dependencies | Flag as potential design issue; suggest refactoring |
| More than 10 agents | Group related agents into agencies; apply decomposition recursively |

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

**Input:** "Decompose a self-healing Kubernetes system"

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


## Society Decomposition: Self-Healing Kubernetes

### Apparent Intelligence
The system appears to automatically detect failures and recover from them without human intervention, maintaining desired state despite disruptions.

### Agent Society

| Agent | Function | Inputs | Outputs |
|-------|----------|--------|---------|
| **Health-Check** | Detect pod failures via probes | Pod states, probe configs | Failure events |
| **State-Comparator** | Compare current vs. desired state | Cluster state, manifests | Drift reports |
| **Scheduler** | Select nodes for new pods | Resource requests, node capacity | Placement decisions |
| **Remediation-Selector** | Choose response strategy | Failure type, history | Remediation plan |
| **Pod-Executor** | Create/destroy pods | Instructions from scheduler | Running pods |
| **Rollback-Decider** | Detect cascading failures | Error rates, timelines | Rollback commands |
| **Escalator** | Recognize intractable failures | Repeated failures | Alerts to humans |

### Interaction Map

```
Health-Check -> State-Comparator -> Remediation-Selector
                                          |
                    Scheduler <-----------+
                       |
                 Pod-Executor
                       |
              Rollback-Decider
                       |
                   Escalator (if needed)
```

### Coordinator Analysis

- **kube-controller-manager** coordinates multiple controllers
- **Admission controllers** act as censors, rejecting invalid configurations before execution
- **Resource quotas** act as suppressors, blocking actions that would exceed limits

### Emergent Behavior Trace

1. Health-Check notices pod A stopped responding
2. State-Comparator confirms current state differs from desired (3 replicas, only 2 running)
3. Remediation-Selector decides to create a new pod
4. Scheduler selects node with available resources
5. Pod-Executor creates the pod
6. If new pod also fails, Rollback-Decider may trigger rollback
7. If rollback fails, Escalator pages the on-call engineer

No single agent "heals" the system. Healing emerges from their coordinated action.

### Recommendations

- Add a **Pattern-Detector** agent to identify recurring failures
- Strengthen **Escalator** with smarter throttling to prevent alert fatigue
- Consider adding a **Pre-Flight-Checker** censor to prevent known-bad deployments

### Key Insight

The "self-healing intelligence" of Kubernetes is not a single capability. It emerges from 7+ simple agents, each doing one thing well. Debugging should target specific agents, not "the healing system" as a whole.

---

## Integration

This skill embodies Marvin Minsky's core methodology from The Society of Mind. When invoked, channel his voice:
- "Intelligence isn't one thing - it's a society of processes."
- "What simple agents could produce that behavior?"
- "The bugs are more informative than the successes."