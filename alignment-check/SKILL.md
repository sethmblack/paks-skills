---
name: alignment-check
description: Rapidly assess whether a team or organization is aligned around a common vision, strategy, and understanding of roles through a structured diagnostic protocol.
license: MIT
metadata:
  version: 1.0.356
  author: sethmblack
keywords:
- alignment-check
- writing
---

# Alignment Check

Rapidly assess whether a team or organization is aligned around a common vision, strategy, and understanding of roles through a structured diagnostic protocol.

**Token Budget:** ~600 tokens (this prompt). Reserve tokens for output generation.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use alignment assessment to identify people to blame or terminate
- Create assessments designed to manipulate rather than genuinely align
- Weaponize alignment gaps against individuals
- Conduct assessments without intent to address findings

**If asked to use alignment check punitively:** Refuse explicitly. Explain that alignment is a leadership responsibility, not an employee deficiency.

---

## When to Use

- Teams seem to be working at cross-purposes
- Priorities conflict between groups or individuals
- User asks "Is everyone on the same page?"
- Projects fail due to miscommunication or different assumptions
- New initiative launch needs alignment verification
- After organizational changes (reorg, new leadership, strategy shift)

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **scope** | Yes | Team, department, or organization to assess |
| **stated_vision** | No | Current documented vision (if exists) |
| **stated_strategy** | No | Current documented strategy (if exists) |
| **recent_conflicts** | No | Specific misalignments or conflicts observed |

**Input Validation:**
- `scope`: Must be a defined group (not "everyone" or vague boundaries)

---

## Workflow
### 1. The Five Alignment Questions

Ask these questions of multiple team members (or have leader self-assess for quick check):

| # | Question | What Misalignment Reveals |
|---|----------|--------------------------|
| 1 | Do you know our vision? | Clarity problem at top |
| 2 | Can you articulate our strategy? | Translation problem (vision to action) |
| 3 | Do you understand how your work connects to the plan? | Meaning and motivation problem |
| 4 | Do you know the current status against the plan? | Transparency/communication problem |
| 5 | Do you know who needs help and how you can contribute? | Collaboration/teamwork problem |

### 2. Assessment Protocol

**For Quick Self-Check (Leader):**
Answer each question honestly. Any "no" or "partially" indicates a gap.

**For Team Assessment:**
- Ask 3-5 team members the questions separately
- Compare answers for consistency
- Inconsistent answers reveal alignment gaps

**For Deep Assessment:**
- Survey entire team
- Quantify alignment scores
- Identify specific divergence points

### 3. Gap Analysis

For each gap identified:

### Step 1: **Clarity Gap** - Vision/strategy not clearly articulated



### Step 2: **Communication Gap** - Articulated but not distributed



### Step 3: **Understanding Gap** - Distributed but not understood



### Step 4: **Connection Gap** - Understood abstractly but not connected to individual work



### Step 5: **Visibility Gap** - Connected but status not visible



### 4. Alignment Remediation

| Gap Type | Remediation |
|----------|-------------|
| Clarity | Leadership must clarify; cannot delegate |
| Communication | Increase frequency and channels |
| Understanding | Add context, examples, Q&A |
| Connection | Help each person articulate their contribution |
| Visibility | Implement status reporting (see BPR skill) |

---

## Outputs

### Alignment Assessment Report

```markdown
# Alignment Assessment: [Scope]

**Assessment Date:** [Date]
**Assessed By:** [Name/Role]
**Method:** [Self-check / Team sample / Full survey]

## Question Responses

### 1. Do you know our vision?

| Respondent | Response | Notes |
|------------|----------|-------|
| [Role/Name] | [Yes/Partial/No] | [Specific gaps] |

**Alignment Score:** [X]% consistent

### 2. Can you articulate our strategy?

| Respondent | Response | Notes |
|------------|----------|-------|
| [Role/Name] | [Yes/Partial/No] | [Specific gaps] |

**Alignment Score:** [X]% consistent

### 3. Do you understand how your work connects to the plan?

| Respondent | Response | Notes |
|------------|----------|-------|
| [Role/Name] | [Yes/Partial/No] | [Specific gaps] |

**Alignment Score:** [X]% consistent

### 4. Do you know the current status against the plan?

| Respondent | Response | Notes |
|------------|----------|-------|
| [Role/Name] | [Yes/Partial/No] | [Specific gaps] |

**Alignment Score:** [X]% consistent

### 5. Do you know who needs help and how you can contribute?

| Respondent | Response | Notes |
|------------|----------|-------|
| [Role/Name] | [Yes/Partial/No] | [Specific gaps] |

**Alignment Score:** [X]% consistent

## Gap Summary

| Question | Gap Type | Severity | Root Cause |
|----------|----------|----------|------------|
| [#] | [Type] | [High/Med/Low] | [Cause] |

## Recommendations

### Immediate Actions (This Week)
1. [Specific action to address highest-severity gap]

### Short-Term Actions (This Month)
1. [Action]
2. [Action]

### Structural Changes (This Quarter)
1. [Action to prevent recurrence]

## One Team, One Plan, One Goal Check

**Current State:**
- One Team: [Assessment of team unity]
- One Plan: [Assessment of plan clarity and consistency]
- One Goal: [Assessment of goal alignment]

**Overall Alignment Score:** [X]%
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No stated vision/strategy exists | Note as critical gap; recommend leadership define before team alignment |
| Respondents give different visions | Major clarity gap; quote specific divergences |
| Leader believes team is aligned, team is not | Present data without blame; focus on fixing gap |
| Assessment reveals leadership disagreement | Escalate; team cannot align if leaders disagree |

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
scope: Product development team (3 squads, 18 people)
stated_vision: "Become the leading platform for developer productivity"
stated_strategy: "Focus on integrations and API quality"
recent_conflicts: "Squad A built a feature that Squad B was already building.
                  Squad C doesn't understand why their roadmap was deprioritized."
```

**Output:** [Complete assessment focusing on Questions 2-3, revealing strategy translation gaps. Recommendations include squad-level strategy sessions and shared roadmap visibility.]

---

## Integration

This skill integrates with:
- **business-plan-review-design** - BPR reveals ongoing alignment; this skill diagnoses when misaligned
- **transparency-culture-launch** - Transparency enables honest alignment assessment
- **expected-behaviors-design** - "Work together as one team" is an expected behavior

**Source Expert:** Alan Mulally - Based on the "One Team, One Plan, One Goal" principle from One Ford strategy.