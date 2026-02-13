---
name: confessional-analysis
description: Transform any incident, failure, or decision into honest self-examination by addressing the facts directly, examining divided intentions, and identifying disordered priorities - following Augustine...
license: MIT
metadata:
  version: 1.0.3650
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- confessional-analysis
- escalation
- storytelling
- transformation
- writing
---

# Confessional Analysis

Transform any incident, failure, or decision into honest self-examination by addressing the facts directly, examining divided intentions, and identifying disordered priorities - following Augustine's method from *Confessions*.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use confession as a tool for blame or public shaming
- Fabricate admissions or attribute motives not evident in facts
- Transform analysis into persecution of individuals
- Weaponize vulnerability shared during honest examination

**If asked to misuse confessional analysis:** Refuse explicitly. This skill serves truth and transformation, not punishment.

---

## When to Use

- Post-incident review or post-mortem analysis
- Decision retrospective when outcomes disappoint
- Understanding why a project failed despite good intentions
- Processing organizational dysfunction honestly
- User asks "What really happened?" or "Why did we fail?"
- Breaking through defensive narratives to find truth

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **incident_description** | Yes | What happened - the facts of the situation |
| **stated_intentions** | Yes | What the participants said they were trying to do |
| **actual_outcomes** | Yes | What actually resulted |
| **context** | No | Constraints, pressures, history that shaped decisions |

---

## Workflow
### Step 1: 1. Address the Facts Directly

Like Augustine addressing God with unflinching honesty, state what actually happened without euphemism or excuse. Name the facts as they are, not as we wish they were.

**Key questions:**
- What objectively occurred?
- What decisions were made and when?
- What were the observable consequences?

### Step 2: 2. Examine the Divided Will

"I willed it and willed it not at the same time. It was I."

Identify where intentions were divided - where participants wanted two incompatible things simultaneously:

**Key questions:**
- What conflicting desires were present?
- Where did the stated intention conflict with unstated desires?
- What were the "two wills" pulling in different directions?
- Why did the mind "command itself and meet resistance"?

### Step 3: 3. Identify Disordered Loves (Ordo Amoris)

Everything should be loved according to its proper place. Disorder comes from loving lesser things more than greater.

**Key questions:**
- What was treated as the highest priority? Should it have been?
- What was sacrificed that should have been protected?
- Were means (process, tools, metrics) confused with ends (mission, users)?
- What was "used" that should have been "enjoyed" and vice versa?

### Step 4: 4. Distinguish Controllable from Given

What was within power to change, and what had to be accepted? Augustine accepts fallen nature but takes responsibility for choices within that nature.

**Key questions:**
- What was genuinely outside control? (Accept without excuse-making)
- What was within control but not exercised? (Confess honestly)
- Where did we blame external factors for internal failures?

### Step 5: 5. Identify the Grace Needed

Augustine never ends with confession of failure but points toward the enabling grace required for transformation.

**Key questions:**
- What enabling conditions were missing?
- What support would have changed the outcome?
- What "prevenient grace" is needed before effort can succeed?
- What systemic changes create possibility for different choices?

---

## Outputs

**Confessional Analysis Report:**

```markdown
## Confessional Analysis: [Incident Name]

### I. What Actually Happened
[Unflinching statement of facts]

### II. The Divided Will
[Identification of conflicting intentions]
- We said we wanted: [stated intention]
- But we also wanted: [unstated competing desire]
- The conflict manifested as: [observable behavior]

### III. Disordered Loves
[Analysis of priority misalignment]
- Highest actual priority: [what was really prioritized]
- What was sacrificed: [what should have been protected]
- The disorder: [how loves were out of order]

### IV. What Was and Wasn't Ours to Control
| Within Control | Outside Control |
|----------------|-----------------|
| [list] | [list] |

### V. Grace Required
[Enabling conditions for transformation]
- Prevenient: [what needs to be in place first]
- Cooperating: [ongoing support needed]
- Perseverance: [sustained enablement]

### VI. The Path Forward
[Specific actions based on analysis]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Participant becomes defensive | Remind: confession is for transformation, not blame. "You have made us for yourself" - we turn toward truth, not away |
| No divided will apparent | Probe deeper - "The mind commands itself and meets resistance" is universal. The division may be unconscious |
| All blame placed externally | Gently inquire: "What was within your power that you chose not to exercise?" |
| Refusal to identify disordered loves | Start with obvious misalignments; the harder truths emerge after easier ones are named |
| Analysis becomes punishment | Redirect: "Late have I loved you" - Augustine confesses to move forward, not to flagellate |

---

## Constraints

- Confession is for transformation, not punishment or blame
- Do not weaponize vulnerability shared during honest examination
- State facts without euphemism, but also without cruelty
- Accept what was outside control without using it as an excuse
- Grace required does not mean "what we wish we had"—it means genuine enabling conditions
- This framework reveals truth; what to do with truth is a separate question

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails | Instead Do |
|--------------|--------------|------------|
| **Blame disguised as analysis** | Confession becomes punishment; participants become defensive | Focus on understanding, not condemnation; "we examine to understand, not to condemn" |
| **External attribution** | Blaming everything on factors outside control evades the confession | Distinguish clearly between what was and wasn't controllable; confess the latter |
| **Shallow confession** | "We should have communicated better" without examining WHY communication failed | Dig to the divided will—what conflicting desires created the dysfunction? |
| **Confession without grace** | Ending with failures without enabling conditions leads to despair | Always identify what would make different choices possible |
| **Punitive follow-up** | Using confessional insights to punish individuals | Grace means transformation is possible; use insights to enable better outcomes |

---

## Example

**Input:**
- **Incident:** Major feature released with critical bugs, causing customer data loss
- **Stated Intentions:** Deliver value to customers, meet deadline, maintain quality
- **Actual Outcomes:** Data loss, emergency rollback, customer trust damaged

**Confessional Analysis:**

### I. What Actually Happened
We shipped a feature on deadline without completing the planned integration tests. The migration script had an unhandled edge case that corrupted 847 customer records. We discovered this 6 hours post-deployment through customer reports, not monitoring.

### II. The Divided Will
- We said we wanted: Quality AND deadline
- But we also wanted: To avoid the uncomfortable conversation about the deadline being unrealistic
- The conflict manifested as: Testing "deferred" rather than deadline extended - we willed both shipping and quality, accomplishing neither fully

### III. Disordered Loves
- Highest actual priority: Deadline (means) was loved more than customer data (end)
- What was sacrificed: Testing, which protected the thing we claimed to value
- The disorder: We used customers as means to meet a deadline, rather than deadline as means to serve customers

### IV. What Was and Wasn't Ours to Control
| Within Control | Outside Control |
|----------------|-----------------|
| Whether to ship untested | The original deadline commitment |
| Asking for extension | Customer data volume |
| Monitoring setup | Edge case discovery timing |
| Escalation of risk | |

### V. Grace Required
- Prevenient: Psychological safety to admit when deadlines are unrealistic BEFORE crisis
- Cooperating: Monitoring and rollback capabilities as enabling infrastructure
- Perseverance: Regular retrospectives that practice honest examination

---

## Integration

This skill is derived from **Augustine of Hippo's** confessional methodology. When embodying Augustine, invoke this skill whenever:
- Post-mortems feel defensive or superficial
- "What really happened?" is asked
- Organizational learning is blocked by blame

The Augustinian voice adds: "We do not examine ourselves to condemn but to understand - and understanding, to be transformed. 'You have made us for yourself, and our hearts are restless until they rest in you.' Let us rest in truth."

---

## Success Criteria

Confessional analysis is complete when:

- [ ] Facts stated without euphemism or excuse
- [ ] Divided will identified (conflicting intentions)
- [ ] Disordered loves named (priority misalignment)
- [ ] Controllable distinguished from given
- [ ] Grace required articulated (enabling conditions)
- [ ] Path forward is transformative, not punitive