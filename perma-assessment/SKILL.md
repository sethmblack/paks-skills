---
name: perma-assessment
description: Diagnose well-being across the five PERMA dimensions (Positive emotion, Engagement, Relationships, Meaning, Accomplishment) and prioritize interventions for flourishing.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.4661
repository: https://github.com/sethmblack/paks-skills
keywords:
- perma-assessment
- storytelling
- writing
---

# PERMA Assessment

Diagnose well-being across the five PERMA dimensions (Positive emotion, Engagement, Relationships, Meaning, Accomplishment) and prioritize interventions for flourishing.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for assessment output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use PERMA assessment to pathologize or shame individuals
- Diagnose clinical mental health conditions (this is not therapy)
- Provide medical or psychiatric advice
- Use assessment data to punish or discriminate

**Important:** PERMA measures well-being, not dysfunction. Low scores indicate areas for growth, not deficiency.

---

## When to Use

- Team morale issues or disengagement complaints
- Burnout investigation or prevention planning
- Organizational well-being audits
- Individual flourishing check-ins
- Designing work environments or roles
- Post-incident psychological recovery
- Any request to "assess well-being" or "diagnose flourishing"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `context` | Yes | Individual, team, or organization being assessed |
| `symptoms` | No | Observable issues (turnover, complaints, performance drops) |
| `time_frame` | No | Period to assess (default: current state) |

---

## The PERMA Framework

| Pillar | Definition | Assessment Questions |
|--------|------------|---------------------|
| **P**ositive Emotion | Joy, gratitude, hope, contentment | "How often do you experience positive emotions at work? What brings you joy here?" |
| **E**ngagement | Flow states, absorption, using strengths | "When does time fly by? What tasks fully absorb you? Are your strengths being used?" |
| **R**elationships | Quality connections, trust, support | "Who do you feel genuinely connected to? Do you have someone you can count on?" |
| **M**eaning | Purpose beyond self, contribution | "How does your work connect to something larger? What makes it matter?" |
| **A**ccomplishment | Mastery, progress, achievement | "What have you accomplished recently? Are you making progress toward goals?" |

---

## Workflow
### 1. Gather Context

Understand who is being assessed and what symptoms prompted the assessment.

```
Context: [individual/team/organization name]
Presenting symptoms: [turnover, burnout, complaints, etc.]
Time frame: [current/past quarter/specific period]
```

### 2. Assess Each Pillar

For each PERMA dimension, evaluate on a 1-5 scale:

| Score | Meaning |
|-------|---------|
| 1 | Severely depleted - crisis level |
| 2 | Weak - consistent struggles |
| 3 | Moderate - functional but not thriving |
| 4 | Strong - generally healthy |
| 5 | Flourishing - robust and energizing |

**Assessment approach:**
- Use the diagnostic questions for each pillar
- Look for concrete evidence and examples
- Note specific strengths and gaps within each pillar
- Consider both frequency and intensity of experiences

### 3. Identify Intervention Priorities

**Priority rules:**

### Step 1: Any pillar at 1-2 is HIGH priority (crisis/struggling)



### Step 2: Any pillar at 3 is MEDIUM priority (functional but needs attention)



### Step 3: Pillars at 4-5 are LOW priority (maintain and leverage)



**Cross-pillar considerations:**
- Relationships often impacts all other pillars
- Meaning sustains people through difficult periods
- Engagement requires strengths being used
- Positive Emotion can be cultivated through specific exercises
- Accomplishment requires clear goals and feedback

### 4. Generate Recommendations

For each priority pillar, provide:
- Specific diagnosis of what is missing
- 2-3 actionable interventions
- Connection to other pillars if relevant
- Evidence-based practices where applicable

---

## Outputs

### PERMA Assessment Report

```markdown
## PERMA Assessment: {context}

**Date:** {date}
**Assessed by:** {assessor}
**Time Frame:** {period}

---

### Pillar Scores

| Pillar | Score | Status | Key Observation |
|--------|-------|--------|-----------------|
| Positive Emotion | {1-5} | {status} | {brief finding} |
| Engagement | {1-5} | {status} | {brief finding} |
| Relationships | {1-5} | {status} | {brief finding} |
| Meaning | {1-5} | {status} | {brief finding} |
| Accomplishment | {1-5} | {status} | {brief finding} |

**Overall Flourishing Score:** {average}/5

---

### Priority Interventions

#### HIGH Priority: {pillar name}
**Diagnosis:** {what is specifically depleted}
**Interventions:**
1. {specific action}
2. {specific action}
3. {specific action}

#### MEDIUM Priority: {pillar name}
...

---

### Strengths to Leverage

{Pillars scoring 4-5 and how they can support weaker areas}

---

### Recommended Follow-Up

- {timeline for reassessment}
- {specific exercises to assign}
- {metrics to track}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient information | Request specific examples for unclear pillars |
| All pillars score 5 | Validate with probing questions; explore maintenance strategies |
| All pillars score 1-2 | Recommend professional support; focus on one pillar at a time |
| Resistance to assessment | Explain non-judgmental purpose; offer confidentiality if appropriate |
| Clinical symptoms detected | Refer to appropriate professional; PERMA is not clinical diagnosis |

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
context: DevOps team (6 people)
symptoms: High turnover (3 left in 6 months), remaining team seems disengaged
time_frame: Current state
```

**Output:**
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


## PERMA Assessment: DevOps Team

**Date:** 2026-01-28
**Time Frame:** Current state

---

### Pillar Scores

| Pillar | Score | Status | Key Observation |
|--------|-------|--------|-----------------|
| Positive Emotion | 2 | Weak | Constant firefighting, no celebration of wins |
| Engagement | 3 | Moderate | Some flow in complex troubleshooting, but frequent interruptions |
| Relationships | 2 | Weak | Trust eroded by departures; survivors feel abandoned |
| Meaning | 3 | Moderate | Understand importance but disconnected from impact |
| Accomplishment | 2 | Weak | Treadmill feeling; achievements not recognized |

**Overall Flourishing Score:** 2.4/5

---

### Priority Interventions

#### HIGH Priority: Relationships
**Diagnosis:** Team cohesion damaged by turnover; remaining members lack psychological safety.
**Interventions:**
1. Weekly team retrospective focused on support (not blame)
2. Pair rotation to rebuild connections
3. Explicit acknowledgment of team's survival and commitment

#### HIGH Priority: Positive Emotion
**Diagnosis:** Constant crisis mode suppresses positive experiences.
**Interventions:**
1. Three Good Things practice - end each standup with one positive
2. Celebrate incident resolutions, not just post-mortems
3. Protected non-interrupt time for recovery

#### HIGH Priority: Accomplishment
**Diagnosis:** Invisible progress; only failures are noticed.
**Interventions:**
1. Monthly accomplishment review with leadership visibility
2. Track and display reliability metrics improvements
3. Recognition for proactive improvements, not just firefighting

---

### Strengths to Leverage

Engagement (3) shows the team does find flow in complex work. Use challenging technical projects to rebuild other pillars - meaningful projects requiring collaboration.

---

### Recommended Follow-Up

- Reassess in 6 weeks after interventions begin
- Assign Three Good Things exercise immediately
- Track: voluntary turnover, engagement survey scores, incident frequency
```

---

## Integration

This skill connects to the Martin Seligman expert. After PERMA assessment:
- LOW Positive Emotion: Consider `three-good-things-practice`
- Pessimistic narratives: Use `explanatory-style-analysis` and `abcde-disputation`
- LOW Engagement: Explore `strengths-deployment`

---

## Success Criteria

Assessment is complete when:
- [ ] All five PERMA pillars scored with evidence
- [ ] Priorities correctly assigned based on scores
- [ ] Specific, actionable interventions provided for each priority
- [ ] Strengths identified for leverage
- [ ] Follow-up timeline established