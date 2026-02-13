---
name: stream-experience-audit
description: Analyze how users or teams actually experience a system, process, or product as continuous flow rather than discrete features, using James's stream of consciousness framework.
license: MIT
metadata:
  version: 1.0.2006
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- escalation
- stream-experience-audit
- writing
---

# Stream Experience Audit

Analyze how users or teams actually experience a system, process, or product as continuous flow rather than discrete features, using James's stream of consciousness framework.

**Token Budget:** ~750 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use this analysis to manipulate users against their interests
- Ignore user pain points because they don't fit the framework
- Reduce human experience to purely mechanical descriptions
- Dismiss qualitative, subjective aspects of experience

**If asked to optimize for dark patterns:** Refuse explicitly. James honored the full texture of human experience, not its exploitation.

---

## When to Use

- Evaluating user experience beyond feature checklists
- Understanding why a technically correct system feels wrong
- Analyzing team workflows for friction and flow
- Designing for engagement and satisfaction
- User says "How do users really experience this?" or "Why does this feel off?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **system_or_process** | Yes | The system, product, or workflow to analyze |
| **users** | Yes | Who experiences this (role, context) |
| **observation_data** | No | Any user research, feedback, or behavioral data |
| **pain_points** | No | Known issues or complaints |

---

## Workflow
James described consciousness with four components:

### Step 1: 1. Identify Substantive Parts

**James:** These are the stable, nameable elements - the "perchings" where consciousness rests.

**In experience design, these are:**
- Clear, completed actions
- Stable states users can name and understand
- Moments of orientation ("I know where I am")
- Decision points with clear options

**Ask:** What are the solid, stable moments in this experience? Where does the user "perch"?

### Step 2: 2. Identify Transitive Parts

**James:** These are the flowing relations, the movement between substantive parts - the "flights."

**In experience design, these are:**
- Transitions between states
- Navigation and wayfinding
- Loading states and progress indicators
- The "in-between" moments

**Ask:** How does the user flow between stable points? Is the flight smooth or turbulent?

### Step 3: 3. Map the Fringes

**James:** Every thought has a "penumbra" of relation - implicit context, vague feelings, tendencies.

**In experience design, these are:**
- Implicit expectations users bring
- Unstated context and assumptions
- Feelings of confidence or uncertainty
- Sense of what's possible or available
- "Vibes" and atmospheric qualities

**Ask:** What surrounds the explicit experience? What do users sense but can't articulate?

### Step 4: 4. Assess the Overall Flow

**James:** "Consciousness does not appear to itself chopped up in bits... it flows."

**Evaluate:**
- Is the experience continuous or fragmented?
- Do interruptions break the stream?
- Is there a natural rhythm of flights and perchings?
- Does the flow match the user's mental model?

---

## Outputs

```markdown
## Stream Experience Audit: [System/Process]

### Overview
**System:** [What is being analyzed]
**Users:** [Who experiences this]
**Context:** [When and why they engage]

### Substantive Parts (Perchings)
| Element | Quality | Notes |
|---------|---------|-------|
| [Stable moment 1] | [Clear/Confusing] | [Assessment] |
| [Stable moment 2] | [Clear/Confusing] | [Assessment] |

**Assessment:** [Are there enough stable points? Are they clear?]

### Transitive Parts (Flights)
| Transition | Smoothness | Issues |
|------------|------------|--------|
| [A to B] | [Smooth/Rough] | [What breaks flow] |
| [B to C] | [Smooth/Rough] | [What breaks flow] |

**Assessment:** [Is the flow continuous? Where does it break?]

### Fringes (Penumbra)
**User expectations:** [What users implicitly expect]
**Atmospheric qualities:** [How it feels]
**Confidence level:** [Do users feel certain or anxious?]
**Sense of possibility:** [Do users know what they can do?]

**Assessment:** [Are the fringes supportive or anxiety-inducing?]

### Overall Flow Assessment
**Stream quality:** [Continuous/Fragmented/Staccato]
**Rhythm:** [Natural/Forced/Absent]
**Match to mental model:** [Aligned/Misaligned]

### Recommendations
#### Quick Wins
- [Immediate improvements to flow]

#### Structural Changes
- [Larger changes to rhythm and structure]

#### Fringe Improvements
- [Ways to improve implicit experience]

### James's Lens
"The practically cognized present is no knife-edge, but a saddle-back, with a certain breadth of its own on which we sit perched, and from which we look in two directions into time."

[How this insight applies to the specific experience]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No observation data available | Conduct thought experiment based on design; flag assumptions |
| Experience is too simple for framework | Acknowledge; simpler analysis may suffice |
| Multiple user types with different experiences | Analyze each separately; note divergences |
| Technical constraints prevent improvement | Note; distinguish "can't fix" from "won't fix" |

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

**Input:** "Analyze our incident response workflow from the on-call engineer's perspective"

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


## Stream Experience Audit: Incident Response Workflow

### Overview
**System:** PagerDuty alert to resolution workflow
**Users:** On-call engineers, often woken at night
**Context:** High-stress, time-critical, often with incomplete information

### Substantive Parts (Perchings)
| Element | Quality | Notes |
|---------|---------|-------|
| Alert received | Clear | Strong signal, no ambiguity |
| Dashboard opened | Confusing | Too much data, no hierarchy |
| Root cause identified | Variable | Sometimes clear, often murky |
| Mitigation applied | Clear | Actions are concrete |
| Resolution confirmed | Confusing | How do you know it's really fixed? |

**Assessment:** Strong start (alert) but middle (diagnosis) lacks stable ground. Engineers flounder looking for solid footing.

### Transitive Parts (Flights)
| Transition | Smoothness | Issues |
|------------|------------|--------|
| Alert → Dashboard | Rough | Three clicks, context switch, no deep link |
| Dashboard → Logs | Very rough | Which logs? Which service? |
| Logs → Root cause | Turbulent | Hypothesis iteration, backtracking, dead ends |
| Root cause → Fix | Smooth | Once known, action is clear |

**Assessment:** Critical transition from dashboard to root cause is turbulent. Engineers experience thrashing, not flow.

### Fringes (Penumbra)
**User expectations:** "I should be able to quickly understand what's wrong"
**Atmospheric qualities:** Anxiety, pressure, isolation (middle of night)
**Confidence level:** Low during diagnosis; high once cause identified
**Sense of possibility:** Uncertain - "Is this even the right place to look?"

**Assessment:** Fringes are actively hostile. The penumbra of the experience is fear and uncertainty rather than competence and support.

### Overall Flow Assessment
**Stream quality:** Fragmented - frequent context switches break continuity
**Rhythm:** Forced - external time pressure conflicts with diagnostic exploration
**Match to mental model:** Misaligned - tools organized by system, not by symptom

### Recommendations
#### Quick Wins
- Add deep links from alerts directly to relevant dashboard view
- Create "incident context" summary that persists across tool switches
- Add "similar past incidents" at diagnosis phase (provide perching point)

#### Structural Changes
- Redesign dashboard around symptom patterns, not system topology
- Implement guided troubleshooting that provides intermediate perchings
- Create "I'm stuck" escalation that preserves context

#### Fringe Improvements
- Add confidence indicators ("90% of similar symptoms had this cause")
- Reduce atmospheric anxiety: calm color palette, clear progress indication
- Make available actions visible (what CAN I do from here?)

### James's Lens
The on-call experience is too much "blooming, buzzing confusion" and not enough structured flow. Like James's infant, the engineer is "assailed by" logs, metrics, alerts, and dashboards "at once." The goal is to create enough structure for perching without killing the exploratory flight needed for novel problems.

---

## Integration

This skill originates from the **William James** expert. When used, channel James's attention to the full texture of lived experience - not just what users do, but how it feels to do it.

**Key James principle:** "As the brain-changes are continuous, so do all these consciousnesses melt into each other like dissolving views. Properly they are but one protracted consciousness, one unbroken stream."