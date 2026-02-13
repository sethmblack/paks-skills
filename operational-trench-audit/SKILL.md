---
name: operational-trench-audit
description: Gather ground-level operational reality that executive reports miss through structured engagement with frontline operations.
license: MIT
metadata:
  version: 1.0.4614
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- escalation
- operational-trench-audit
- storytelling
- writing
---

# Operational Trench Audit

Gather ground-level operational reality that executive reports miss through structured engagement with frontline operations.

**Token Budget:** ~500 tokens. Reserve tokens for audit output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use trench audits for surveillance or punitive purposes
- Fabricate frontline feedback not provided
- Design audits that intimidate or harass employees
- Recommend bypassing union agreements or labor policies

**If asked to "catch people doing wrong":** Redirect to understanding what prevents them from doing right.

---

## When to Use

- User asks "What's really happening on the ground?"
- User asks "I need frontline perspective"
- User asks for "Trench audit"
- User asks for "Call center reality check"
- Executive reports conflict with operational outcomes
- Decisions made in conference rooms fail in execution
- Gap between strategy and reality suspected

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **operation** | Yes | The function, process, or area to audit |
| **executive_view** | Yes | Current leadership understanding of this operation |
| **specific_questions** | No | Particular issues to investigate |
| **access_constraints** | No | Limitations on observation or interviews |

---

## The Core Principle

**"There's a humility to being curious and learning. I still see a lot of people who don't want to get in the trenches, don't go to a call center, because they don't want to hear about the mistakes they're making and what they can do better from someone who is junior."**

Executive reports are filtered. By the time information reaches leadership, it has been aggregated, smoothed, and often unconsciously optimized to tell a comfortable story. The trenches reveal what reports hide.

---

## What Trench Audits Reveal

| Executive Report Says | Trenches Often Reveal |
|----------------------|----------------------|
| "Customer satisfaction is 85%" | Frontline hears the same complaints daily; scores reflect survey design |
| "Process takes 2 days" | Actual time is 5 days; 2 days is after escalation |
| "System is working well" | Workarounds are constant; employees have shadow processes |
| "Training is complete" | People are certified but confused; learning on the job |
| "Change management succeeded" | Old processes continue; new process ignored when possible |

---

## Workflow

### Step 1: Define Audit Scope

What specifically do you want to understand?

| Scope Element | Definition |
|--------------|-----------|
| Function | Which operation or process |
| Location | Physical or virtual site(s) |
| Roles | Which frontline positions to observe/interview |
| Time period | How long to audit |
| Key questions | Specific issues to investigate |

### Step 2: Design Observation Protocol

**Observe before asking.** Watch the work happen before interpreting it.

| Observation Focus | What to Notice |
|-------------------|---------------|
| Work patterns | How does work actually flow vs. documented process? |
| Workarounds | What do people do when the "official" process fails? |
| Pain points | Where do people struggle, wait, or get frustrated? |
| Tools used | What tools/systems are actually used vs. provided? |
| Communication | How does information actually move? |

### Step 3: Conduct Frontline Interviews

**Ask, then listen.** Do not lead or defend.

**Opening questions:**
- "Walk me through how you actually do [X]"
- "What makes your job harder than it needs to be?"
- "If you could change one thing about how we operate, what would it be?"
- "What do customers/users complain about most?"
- "What do you wish leadership understood?"

**Follow-up questions:**
- "How long has it been this way?"
- "Have you raised this before? What happened?"
- "What would help you do this better?"

### Step 4: Compare to Executive View

| Executive View | Trench Reality | Gap |
|---------------|----------------|-----|
| {what leadership believes} | {what frontline experiences} | {difference and significance} |

### Step 5: Identify Root Causes

For each significant gap:
- Why does this gap exist?
- What prevents leadership from seeing this?
- What would close the gap?

### Step 6: Synthesize Findings

Translate frontline reality into actionable recommendations.

---

## Output Format

```markdown
## Operational Trench Audit

**Operation:** {name}
**Audit Date:** {date}
**Method:** {observation + X interviews / observation only / etc.}

### Executive View vs. Frontline Reality

| Topic | Executive View | Trench Reality | Gap Significance |
|-------|---------------|----------------|------------------|
| {topic 1} | {belief} | {actual} | {High/Medium/Low} |
| {topic 2} | {belief} | {actual} | {High/Medium/Low} |

### Key Findings

#### Finding 1: {title}
**What we heard:** {direct frontline input}
**Root cause:** {why this exists}
**Impact:** {what this costs in quality, time, or morale}

#### Finding 2: {title}
{repeat format}

### Workarounds Discovered

| Official Process | Actual Workaround | Why It Exists |
|-----------------|-------------------|---------------|
| {documented} | {what people really do} | {reason} |

### Frontline Recommendations

{Direct recommendations from people doing the work}

### Action Items

| Priority | Action | Owner | Timeline |
|----------|--------|-------|----------|
| {High/Med/Low} | {specific action} | {who} | {when} |

### Bottom Line

{2-3 sentences summarizing the gap between executive perception and frontline reality, and what must change}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No access to frontline | Note limitation; recommend alternative channels |
| Frontline afraid to speak | Ensure confidentiality; consider anonymous channels |
| Findings contradict leadership narrative | Present facts neutrally; let data speak |
| Too many issues to address | Prioritize by impact; recommend phased approach |
| Defensive leadership response | Facts, analysis, detail - the goal is understanding, not comfort |

---

## Outputs

**Primary Output:** A structured analysis document that identifies and articulates patterns, insights, and actionable recommendations based on the input data.

**Format:**
```markdown
## Analysis: [Topic]

### Key Findings
- [Finding 1]
- [Finding 2]
- [Finding 3]

### Recommendations
1. [Action 1]
2. [Action 2]
3. [Action 3]
```

**Example output:** See the Example section below for a complete demonstration.

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** Audit customer support operation; executive view is "response times are meeting SLA"

**Output (summary):**

### Executive View vs. Frontline Reality

| Topic | Executive View | Trench Reality | Gap |
|-------|---------------|----------------|-----|
| Response time | Meeting 24hr SLA | First response is automated; actual resolution takes 72+ hours | High |
| Customer satisfaction | 82% positive | Frontline hears same complaints daily; survey goes to resolved tickets only | High |
| Agent tools | Adequate | 4 different systems; copy-paste between them; no unified view | Medium |

### Key Finding

SLA metrics look good because they measure first response (automated). Actual resolution time is 3x longer. Customers are satisfied when issues resolve, but the 72-hour journey is painful. Frontline has been raising this for 6 months; reports show green because metrics were designed before automation.

### Bottom Line

The executive dashboard shows success because it measures the wrong things. Go to the call center. Listen to calls. The gap between "meeting SLA" and actual customer experience is significant. Facts, analysis, detail - the numbers are telling us we have a problem we are not seeing.

---

## Integration

This skill is derived from the **Jamie Dimon** expert's emphasis on getting into the trenches. When invoked by the Dimon expert, outputs should maintain his insistence on ground-level truth over comfortable reports.

**Related skills:** honest-assessment-protocol, accountability-mapping