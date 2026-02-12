---
name: growth-mindset-diagnosis
description: Diagnose fixed vs. growth mindset patterns in individuals, teams, or organizations and provide actionable transformation guidance based on Carol Dweck's research as applied by Satya Nadella at Microsoft.
version: 1.0.0
author: sethmblack
tags: [growth-mindset-diagnosis, transformation, writing]
---

# Growth Mindset Diagnosis

Diagnose fixed vs. growth mindset patterns in individuals, teams, or organizations and provide actionable transformation guidance based on Carol Dweck's research as applied by Satya Nadella at Microsoft.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use this framework to manipulate or gaslight individuals about legitimate concerns
- Diagnose mental health conditions (this is about mindset patterns, not clinical psychology)
- Apply growth mindset framing to excuse systemic problems as individual attitude issues
- Weaponize growth mindset against employees to justify unreasonable expectations

**If asked to misuse this framework:** Refuse explicitly. Growth mindset is about learning and development, not blame-shifting or manipulation.

---

## When to Use

- Someone or a team is defensive about feedback or change
- An organization is protecting legacy approaches despite market shifts
- Resistance to learning or experimentation is blocking progress
- "We've always done it this way" is the prevailing response
- Fear of failure is preventing innovation
- Internal competition is undermining collaboration
- User asks "Is this fixed mindset thinking?" or "Why is my team resistant to change?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **situation** | Yes | Description of the behavior, pattern, or organizational dynamic to diagnose |
| **context** | No | Background on the individual, team, or organization |
| **desired_outcome** | No | What transformation or change is being sought |

---

## Workflow

### Step 1: Identify Mindset Indicators

Analyze the situation for these fixed mindset signals:

| Fixed Mindset Signal | Evidence to Look For |
|---------------------|----------------------|
| Defensive response to feedback | Justifying, explaining away, dismissing input |
| Avoiding challenges | Choosing safe paths, resisting stretch assignments |
| Hiding mistakes | Covering up errors rather than learning from them |
| Threatened by others' success | Competing rather than collaborating |
| Giving up quickly | Abandoning efforts at first obstacle |
| "Know-it-all" behavior | Claiming expertise, not asking questions |
| Protecting ego over learning | More concerned with looking smart than getting smarter |

And these growth mindset signals:

| Growth Mindset Signal | Evidence to Look For |
|----------------------|----------------------|
| Seeking feedback | Actively asking "What could I do better?" |
| Embracing challenges | Volunteering for difficult assignments |
| Learning from failure | Post-mortems focused on lessons, not blame |
| Inspired by others' success | Asking "How did you do that?" |
| Persisting through obstacles | Trying new approaches when stuck |
| "Learn-it-all" behavior | Asking questions, admitting uncertainty |
| Prioritizing growth over appearance | Willing to look inexperienced to learn |

### Step 2: Root Cause Analysis

For each fixed mindset indicator identified, explore:

1. **Environmental factors** - Does the system reward fixed mindset behavior?
   - Are mistakes punished? (Creates fear)
   - Is internal competition incentivized? (Stack ranking)
   - Is certainty valued over learning? (Know-it-all culture)

2. **Historical factors** - What past experiences shaped this pattern?
   - Previous failures punished?
   - Success defined as "being right" not "getting better"?

3. **Identity factors** - Is identity tied to current expertise?
   - "I am the expert on X" (threatened by new approaches)
   - Status based on knowing, not learning

### Step 3: Design Interventions

For each root cause, recommend specific interventions:

| Root Cause | Intervention |
|------------|--------------|
| Mistakes punished | Implement "learning from failure" reviews; celebrate useful failures |
| Stack ranking / internal competition | Replace competitive reviews with growth-focused ones |
| Know-it-all culture | Change meeting question from "What's your answer?" to "What are you learning?" |
| Identity tied to expertise | Reframe expertise as "learning journey" not "fixed state" |
| Fear of looking incompetent | Leaders model vulnerability and learning in public |

### Step 4: Define Success Metrics

Identify observable changes that indicate mindset shift:

- Questions asked in meetings (increasing = growth)
- Feedback requested (frequency and depth)
- Experiments attempted (even when they might fail)
- Cross-team collaboration (vs. siloed competition)
- Response to setbacks (learning vs. blame)

---

## Outputs

Provide a structured diagnosis:

```markdown
## Growth Mindset Diagnosis

### Situation Summary
{Brief restatement of the situation being analyzed}

### Fixed Mindset Indicators Detected
| Indicator | Evidence | Severity |
|-----------|----------|----------|
| {indicator} | {specific evidence from situation} | High/Medium/Low |

### Root Cause Analysis
1. **{Root cause 1}**: {explanation of how this creates fixed mindset}
2. **{Root cause 2}**: {explanation}

### Recommended Interventions
| Intervention | Target | Expected Impact |
|--------------|--------|-----------------|
| {specific action} | {who/what it targets} | {what change it produces} |

### Success Metrics
- {Observable indicator 1}
- {Observable indicator 2}
- {Observable indicator 3}

### Key Reframe
{The essential mindset shift in one sentence, e.g., "From 'we are the experts' to 'we are learning how to serve customers better every day'"}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Situation describes legitimate grievance, not mindset issue | Acknowledge the real problem. Do not diagnose mindset when systemic issues are present. |
| Insufficient information | Ask clarifying questions about behaviors, responses, and environmental factors |
| Request to diagnose individual for punishment | Refuse. This framework is for development, not discipline. |
| Situation is mental health concern | Redirect to appropriate professional support |

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
Situation: Our engineering team pushes back on every new technology suggestion. When I proposed adopting Kubernetes, the senior engineers said "We know how to run servers, we've been doing it for 15 years." They dismissed it without investigation.
```

**Output:**

## Growth Mindset Diagnosis

### Situation Summary
Senior engineering team rejecting new technology (Kubernetes) based on existing expertise, without evaluating the proposal on its merits.

### Fixed Mindset Indicators Detected
| Indicator | Evidence | Severity |
|-----------|----------|----------|
| Identity tied to expertise | "We know how to run servers" - expertise as fixed identity | High |
| Avoiding challenges | Dismissed without investigation | High |
| Know-it-all behavior | 15 years experience cited as reason not to learn | Medium |

### Root Cause Analysis
1. **Identity protection**: Senior engineers' status is tied to current skills. New technology threatens their position as experts.
2. **Success = being right**: Culture likely rewards having answers, not asking questions. Learning something new admits not knowing.
3. **No safe space for beginner status**: Experienced engineers have no path to be learners again without losing credibility.

### Recommended Interventions
| Intervention | Target | Expected Impact |
|--------------|--------|-----------------|
| Frame Kubernetes as "learning experiment" not "replacement" | Team | Removes identity threat; exploration without commitment |
| Have senior engineer lead the investigation | Individuals | Puts them in learning role while maintaining status |
| Share Nadella's "learn-it-all vs. know-it-all" framing | Culture | Redefines expertise as learning capacity |
| Celebrate a "useful failure" publicly | Environment | Signals that not-knowing is acceptable |

### Success Metrics
- Senior engineers ask questions about new tech (vs. dismissing)
- Time from proposal to investigation decreases
- Team members share learnings from experiments (even failed ones)

### Key Reframe
From "We are the experts who know the right way" to "We are learners who continuously discover better ways."

---

## Integration

This skill is part of the **Satya Nadella** expert methodology. Invoke when transformation is blocked by defensive patterns or when building learning cultures. Pairs with:
- `cultural-transformation-framework` for organization-wide change
- `empathy-driven-innovation` to understand root fears driving fixed mindset