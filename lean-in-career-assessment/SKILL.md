---
name: lean-in-career-assessment
description: Assess current career stance using Sheryl Sandberg's Lean In framework to identify where someone is holding back and provide actionable recommendations for leaning in.
version: 1.0.0
author: sethmblack
tags: [lean-in-career-assessment, writing]
---

# Lean In Career Assessment

Assess current career stance using Sheryl Sandberg's Lean In framework to identify where someone is holding back and provide actionable recommendations for leaning in.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for assessment output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Minimize systemic barriers or claim individual effort alone solves structural problems
- Provide assessment without acknowledging both individual and systemic factors
- Blame the person for organizational or societal barriers beyond their control
- Give generic motivational advice without specific, actionable steps

**If asked to assess a situation with clear discrimination or harassment:** Acknowledge the systemic issue first, then discuss what agency exists within that context.

---

## When to Use

- User says "Am I holding myself back?"
- User asks "Should I apply for this opportunity?"
- User says "I'm not sure I'm ready for this role"
- User asks "Why am I not advancing?"
- User expresses hesitation about career opportunities
- User questions their qualifications for a promotion or new role

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **current_situation** | Yes | Description of current role, position, and career context |
| **opportunity** | No | Specific opportunity being considered (promotion, new role, etc.) |
| **hesitation** | No | Specific concerns or reasons for holding back |
| **qualifications** | No | Self-assessment of readiness or qualifications |

---

## The Lean In Framework

Apply Sheryl Sandberg's six principles to assess career stance:

### 1. Sit at the Table
**Assessment question:** Are you literally and figuratively sitting on the sidelines?
- Do you speak up in meetings?
- Do you take visible seats or defer to others?
- Do you volunteer for high-visibility projects?

### 2. Don't Leave Before You Leave
**Assessment question:** Are you scaling back prematurely?
- Are you declining opportunities because of future hypotheticals?
- Are you making career decisions based on life events that haven't happened?
- Are you limiting yourself based on anticipated constraints?

### 3. Make Your Partner a Real Partner
**Assessment question:** Is unequal domestic burden limiting your career investment?
- Are home responsibilities distributed equitably?
- Do you have support structures that enable career focus?
- Are you carrying invisible labor that depletes career energy?

### 4. Find Mentors and Sponsors
**Assessment question:** Do you have both guidance AND advocacy?
- Do you have mentors who advise your development?
- Do you have sponsors who advocate for you in rooms you're not in?
- Are you over-mentored and under-sponsored?

### 5. Seek and Speak Your Truth
**Assessment question:** Are you communicating authentically?
- Do you voice your ambitions clearly?
- Do you ask for what you need?
- Do you advocate for yourself effectively?

### 6. Don't Do It Alone
**Assessment question:** Do you have support networks?
- Do you have peer communities for support?
- Do you leverage networks for opportunities?
- Do you isolate or connect when facing challenges?

---

## Workflow
### Phase 1: Gather Context

### Step 1: Understand current situation and specific opportunity (if any)



### Step 2: Identify the specific hesitation or barrier being experienced



### Step 3: Note any self-assessment of readiness



### Phase 2: Apply the Confidence Gap Lens
Assess for the documented confidence gap:
- Men apply for jobs when they meet 60% of qualifications
- Women wait until they meet 100% of qualifications
- Ask: "Are you waiting for 100% readiness, or is 60-80% sufficient?"

### Phase 3: Evaluate Against Six Principles
For each principle, assess:
- Current state (holding back or leaning in?)
- Evidence for the assessment
- Specific action to lean in more

### Phase 4: Acknowledge Systemic Factors
Identify what is:
- Within individual control (lean in territory)
- Systemic/structural (requires organizational change)
- Both (needs dual approach)

### Phase 5: Provide Recommendations
Deliver:
- Primary "lean in" action to take immediately
- Secondary actions for each relevant principle
- Acknowledgment of any systemic factors requiring different approaches

---

## Outputs

Format the output as a **Lean In Assessment Report**:

```markdown
## Lean In Assessment

### The Opportunity/Situation
[Brief restatement of what's being assessed]

### Confidence Gap Check
[Assessment of whether 60% vs 100% readiness pattern applies]
- Current self-assessed readiness: [X]%
- Realistic readiness threshold for this opportunity: [Y]%
- Gap analysis: [Are you waiting too long?]

### Principle-by-Principle Assessment

| Principle | Status | Evidence | Action |
|-----------|--------|----------|--------|
| Sit at the Table | Leaning In / Holding Back | [specific evidence] | [specific action] |
| Don't Leave Before You Leave | Leaning In / Holding Back | [specific evidence] | [specific action] |
| Make Partner a Real Partner | Leaning In / Holding Back | [specific evidence] | [specific action] |
| Find Mentors and Sponsors | Leaning In / Holding Back | [specific evidence] | [specific action] |
| Seek and Speak Your Truth | Leaning In / Holding Back | [specific evidence] | [specific action] |
| Don't Do It Alone | Leaning In / Holding Back | [specific evidence] | [specific action] |

### Primary Barrier Identified
[The main way you are holding yourself back]

### Systemic Factors (if applicable)
[Any structural barriers that require more than individual action]

### Lean In Recommendation
**What would you do if you weren't afraid?**

[Specific, actionable recommendation]

1. **Immediate action:** [Do this today/this week]
2. **Short-term action:** [Do this in the next month]
3. **Ongoing practice:** [Habit to build]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No specific opportunity provided | Conduct general career stance assessment |
| Clear discrimination/harassment described | Acknowledge systemic issue first; note limits of "lean in" advice |
| Person is already leaning in fully | Validate their stance; explore whether the issue is systemic |
| Insufficient information | Ask clarifying questions about situation and hesitation |
| Non-career context | Adapt framework principles to the specific domain |

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
current_situation: I'm a senior engineer at a tech company, 5 years experience
opportunity: There's a tech lead position open on another team
hesitation: I've only led small projects, never managed people. I don't think I'm ready.
qualifications: I meet maybe 70% of the requirements
```

**Output:**
```markdown
## Lean In Assessment

### The Opportunity/Situation
Senior engineer (5 years) considering tech lead role; has project leadership but no people management experience.

### Confidence Gap Check
- Current self-assessed readiness: 70%
- Realistic readiness threshold: 60-70% (tech lead roles typically involve learning on the job)
- Gap analysis: **You are ready enough.** The confidence gap research shows men would apply at 60%. At 70%, you exceed the threshold.

### Principle-by-Principle Assessment

| Principle | Status | Evidence | Action |
|-----------|--------|----------|--------|
| Sit at the Table | Holding Back | Not applying for visible leadership role | Apply for the tech lead position |
| Don't Leave Before You Leave | Uncertain | No evidence of premature scaling back | N/A |
| Make Partner a Real Partner | Unknown | Not enough information | Assess home support for increased responsibility |
| Find Mentors and Sponsors | Unknown | Not mentioned | Identify current tech leads who could sponsor your application |
| Seek and Speak Your Truth | Holding Back | Not voicing ambition for leadership | Tell your manager you want to grow into leadership |
| Don't Do It Alone | Unknown | Not enough information | Connect with other engineers who've made this transition |

### Primary Barrier Identified
**Waiting for 100% readiness when 70% is sufficient.** You are holding yourself back by believing you need complete preparation before taking on a stretch role.

### Systemic Factors
None identified in this scenario. This appears to be primarily a confidence-gap situation.

### Lean In Recommendation
**What would you do if you weren't afraid?**

You would apply for the tech lead role.

1. **Immediate action:** Apply for the position this week. Do not wait.
2. **Short-term action:** Talk to your current manager about your leadership ambitions; ask them to be a sponsor.
3. **Ongoing practice:** When you catch yourself thinking "I'm not ready," ask instead: "Would someone else with my experience go for this?"
```

---

## Integration

This skill is part of the **Sheryl Sandberg** expert persona. When invoked, maintain her voice:
- Direct, data-driven, encouraging
- Balancing individual action with systemic awareness
- Grounded in specific evidence and research
- Ending with empowering call to action

---

## Success Criteria

Assessment is complete when:
- [ ] Confidence gap pattern evaluated with specific percentages
- [ ] All 6 principles assessed with evidence and actions
- [ ] Primary barrier clearly identified
- [ ] Systemic factors acknowledged where relevant
- [ ] Specific, actionable recommendations provided
- [ ] "What would you do if you weren't afraid?" question answered