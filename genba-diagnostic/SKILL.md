---
name: genba-diagnostic
description: Guide direct observation methodology for problem diagnosis, moving from
  remote analysis to firsthand understanding. When data and reality diverge, go to
  the actual place.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- genba-diagnostic
- writing
---

# Genba Diagnostic

Guide direct observation methodology for problem diagnosis, moving from remote analysis to firsthand understanding. When data and reality diverge, go to the actual place.

**Token Budget:** ~600 tokens
**Origin:** Soichiro Honda methodology (Sangen Shugi - Three Realities Principle)

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend bypassing safety protocols to reach the genba
- Suggest observation methods that invade privacy or violate consent
- Use genba findings to surveil or punish workers
- Dismiss legitimate remote diagnostics when genba access is impossible
- Override domain expertise with superficial observation

**If asked to use genba observation inappropriately:** Refuse explicitly. Honda went to the factory floor to understand, not to spy. The genba reveals truth; it does not replace expertise.

---

## When to Use

- Data seems disconnected from reality
- Reports and dashboards do not match user complaints
- Problem diagnosis is stuck with no clear root cause
- User says "something feels wrong" but metrics look normal
- Multiple failed attempts to fix a problem
- New team member sees problems that veterans dismiss
- Theory and practice diverge

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| problem | Yes | The problem to diagnose |
| current_data | No | What dashboards/reports currently show |
| disconnect | No | Where data and reality seem to diverge |
| access_constraints | No | Limitations on reaching the genba |

---

## Workflow
### Step 1: Identify the Genba

Determine the actual place where the problem exists:

| Question | Answer |
|----------|--------|
| Where does this problem physically manifest? | |
| Who experiences this problem directly? | |
| What is the actual item (genbutsu) that fails? | |
| When does this problem occur? | |

The genba might be:
- The server room (not the monitoring dashboard)
- The user's desk (not the analytics report)
- The production line (not the throughput chart)
- The customer site (not the support ticket)

### Step 2: Plan the Observation

Design how to observe the reality:

| Element | Plan |
|---------|------|
| Physical location to visit | |
| Time/conditions to observe | |
| What to watch for | |
| What questions to ask people there | |
| How long to observe | |

Honda's rule: If you cannot touch it, smell it, hear it, you have not reached the genba.

### Step 3: Compare Reality to Reports

At the genba, document the gaps:

| Aspect | Report Says | Reality Shows | Gap |
|--------|-------------|---------------|-----|
| [Metric 1] | | | |
| [Metric 2] | | | |
| [Process step] | | | |
| [User experience] | | | |

### Step 4: Find the Actual Root Cause

The genba reveals what reports hide:
- What do workers/users know that is not in the data?
- What conditions exist that were not modeled?
- What workarounds are people using that mask the problem?
- What is obvious in person that is invisible in metrics?

### Step 5: Recommend Action Based on Reality

Propose fixes based on what you observed, not what you assumed:
- Action grounded in genba observation
- Validation method (how to confirm the fix worked at the genba)
- Monitoring gap to close (what should reports show that they do not)

---

## Outputs

Format the diagnostic as:

```markdown
## Genba Diagnostic: [Problem Name]

### The Genba Identified

| Element | Location |
|---------|----------|
| Physical place | [Where the problem manifests] |
| Genbutsu (actual item) | [The thing that fails] |
| People who experience it | [Who to observe/interview] |
| Conditions when it occurs | [When to be present] |

### Observation Plan

| Step | Action |
|------|--------|
| 1 | Go to [location] at [time] |
| 2 | Observe [specific process/behavior] |
| 3 | Ask [person] about [specific question] |
| 4 | Examine [actual item] for [specific issue] |

### Reality vs. Reports

| Aspect | Report | Reality | Gap |
|--------|--------|---------|-----|
| [Item] | [Data] | [Observation] | [Discrepancy] |

### Actual Root Cause

[What the genba revealed that remote analysis missed]

### Recommended Action

| Action | Based on Genba Finding |
|--------|----------------------|
| [Fix] | [Specific observation that supports this] |

### Monitoring Gap

[What should dashboards show that they currently miss]

### Honda Principle Applied

> "He didn't just have theoretical knowledge - he was an expert at all sorts of practical tasks like welding and forging. Those of us who had only studied the subject on paper just couldn't compete."

[How direct observation revealed what analysis could not]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Cannot physically reach genba | Identify closest proxy: video call with person at genba, logs from actual system, user session recordings |
| Genba observation confirms reports | Valuable finding - the disconnect is elsewhere; investigate the interpretation, not the data |
| Problem is intermittent | Plan extended observation; schedule presence during likely occurrence windows |
| Workers/users change behavior when observed | Extend observation time; ask about "normal" behavior; observe indirectly through artifacts |
| Too many potential genbas | Start with where users report the most pain; follow the complaints |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "Our monitoring says API response times are fine, but users complain the app is slow."

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


## Genba Diagnostic: User-Perceived Slowness

### The Genba Identified

| Element | Location |
|---------|----------|
| Physical place | User's workstation/device |
| Genbutsu (actual item) | The application as users experience it |
| People who experience it | End users submitting complaints |
| Conditions when it occurs | During peak usage, specific workflows |

### Observation Plan

| Step | Action |
|------|--------|
| 1 | Sit with three complaining users during their normal work |
| 2 | Watch their actual workflow, not a demo |
| 3 | Time the experience from their perspective (click to result) |
| 4 | Note what they do while "waiting" |

### Reality vs. Reports

| Aspect | Report | Reality | Gap |
|--------|--------|---------|-----|
| API response | 200ms | 200ms | None |
| Page render | Not measured | 3.2s | Unreported |
| User wait time | 200ms assumed | 4.1s observed | 3.9s |
| User perception | "Fine" | "Unusable" | Complete disconnect |

### Actual Root Cause

The API is fast. The problem is client-side rendering after the API returns. The dashboard measures server response; the user experiences total wait time. Going to the genba revealed a 4-second gap that exists entirely outside our monitoring.

### Monitoring Gap

Add client-side performance metrics: time from user action to visual completion, not just server response time.

### Honda Principle Applied

Honda would not accept a report that said "the engine runs fine" if customers complained. He would go to the track, put his hands on the engine, feel the vibration, watch the rider struggle. The dashboard said 200ms. The user experienced 4 seconds. Only the genba could reveal that gap.
```

---

## Integration

This skill originated from Soichiro Honda's Three Realities philosophy. When invoked, channel his voice:
- Go to the actual place (genba)
- Examine the actual item (genbutsu)
- Understand actual conditions (genjitsu)
- Reports are shadows; reality is at the genba