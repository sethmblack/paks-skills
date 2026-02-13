---
name: abcde-disputation
description: Guide systematic cognitive restructuring through the Adversity-Belief-Consequence-Disputation-Energization framework, transforming pessimistic beliefs about setbacks into constructive responses.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.303
keywords:
- abcde-disputation
- compression
- transformation
- writing
---

# ABCDE Disputation

Guide systematic cognitive restructuring through the Adversity-Belief-Consequence-Disputation-Energization framework, transforming pessimistic beliefs about setbacks into constructive responses.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for disputation output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Dismiss legitimate emotions or concerns as "just pessimism"
- Apply disputation to trauma that requires professional support
- Use this to invalidate someone's experience
- Replace professional mental health treatment

**Important:** Disputation challenges beliefs, not feelings. Feelings are valid; interpretations are what we examine.

---

## When to Use

- After explanatory-style-analysis identifies pessimistic patterns
- Processing failures or setbacks
- Building resilience after incidents
- Someone stuck in rumination
- Team retrospectives with blame dynamics
- Request to "help me reframe this" or "process this setback"
- Persistent negative self-talk about performance

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `adversity` | Yes | The triggering event or setback |
| `belief` | Yes | The person's interpretation of the event |
| `consequences` | No | Observed feelings and behaviors (will be inferred if not provided) |
| `prior_analysis` | No | Explanatory style analysis results (if available) |

---

## The ABCDE Framework

| Component | Definition | Key Question |
|-----------|------------|--------------|
| **A**dversity | The objective event that happened | "What actually occurred, stated as fact?" |
| **B**elief | Your interpretation of the event | "What do you tell yourself about this?" |
| **C**onsequences | Feelings and behaviors resulting from the belief | "What did you feel and do as a result?" |
| **D**isputation | Evidence-based challenges to the belief | "What evidence contradicts this belief?" |
| **E**nergization | The outcome of successful disputation | "How do you feel now? What will you do differently?" |

---

## Workflow
### Step 1: 1. Clarify the Adversity

Get the objective facts of what happened, stripped of interpretation.

**Good adversity statement:** "The deployment failed at 3 PM and required 4 hours to roll back."
**Too interpretive:** "The deployment was a disaster because I messed up."

### Step 2: 2. Identify the Belief

Extract the specific interpretation. Listen for:
- Self-attribution ("I should have...")
- Permanent framing ("I'll never be able to...")
- Global scope ("Everything is ruined...")
- Catastrophizing ("This is terrible...")

### Step 3: 3. Document Consequences

What did the belief lead to?
- **Emotional consequences:** Shame, anxiety, hopelessness, anger
- **Behavioral consequences:** Withdrawal, avoidance, over-monitoring, blame

### Step 4: 4. Conduct Disputation

Apply four disputation strategies:

| Strategy | Description | Question Form |
|----------|-------------|---------------|
| **Evidence** | What facts contradict the belief? | "What evidence suggests this belief isn't completely true?" |
| **Alternatives** | What other explanations exist? | "What else could have contributed to this outcome?" |
| **Implications** | Even if true, so what? | "Even if this belief were true, what would be the realistic implications?" |
| **Usefulness** | Is this belief helping? | "Is holding this belief serving you well? What would be more useful?" |

**For each disputation, provide:**
- The specific challenge
- Supporting evidence or reasoning
- The reframed belief

### Step 5: 5. Generate Energization

After successful disputation:
- How has the emotional state shifted?
- What constructive action becomes possible?
- What will you do differently?

---

## Outputs

### ABCDE Disputation Worksheet

```markdown
## ABCDE Disputation: {brief title}

**Date:** {date}
**Subject:** {person/team}

---

### A - Adversity
**What happened (facts only):**
{objective description of the event}

---

### B - Belief
**Your interpretation:**
"{direct quote of the belief}"

**Belief type:** {permanent/pervasive/personal - from explanatory style analysis if available}

---

### C - Consequences
**Emotional:**
- {feeling 1}
- {feeling 2}

**Behavioral:**
- {behavior 1}
- {behavior 2}

---

### D - Disputation

#### Evidence Challenge
**Question:** What facts contradict this belief?
**Evidence:** {specific facts that don't fit the belief}
**Reframe:** "{adjusted belief based on evidence}"

#### Alternatives Challenge
**Question:** What other explanations exist?
**Alternatives:**
1. {alternative explanation 1}
2. {alternative explanation 2}
3. {alternative explanation 3}
**Reframe:** "{adjusted belief acknowledging alternatives}"

#### Implications Challenge
**Question:** Even if true, what are the realistic implications?
**Reality check:** {what would actually happen, not catastrophized}
**Reframe:** "{belief that accounts for realistic implications}"

#### Usefulness Challenge
**Question:** Is this belief helping you?
**Cost of belief:** {what the belief costs you}
**More useful belief:** "{replacement belief that serves better}"

---

### E - Energization

**Emotional shift:**
{how feelings have changed after disputation}

**Constructive action:**
{what the person will do now that the belief has shifted}

**Commitment:**
"{specific commitment statement}"

---

### Summary

**Original belief:** "{the starting belief}"
**Reframed belief:** "{the belief after disputation}"
**Key insight:** {the core shift that happened}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Belief is actually accurate | Acknowledge accuracy; focus on Implications and Usefulness challenges |
| Strong emotional resistance | Validate feelings first; slow down; focus on Evidence only |
| Cannot identify belief | Ask: "What are you telling yourself about this?" |
| Multiple beliefs entangled | Address one at a time; start with the most distressing |
| Trauma indicators | Refer to professional support; ABCDE is not trauma therapy |
| Disputation feels dismissive | Emphasize: "We're examining interpretations, not your feelings" |

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
adversity: System outage affecting customers for 2 hours
belief: "I should have caught this in code review. I'm failing at my job."
consequences: Feeling ashamed, avoiding team, obsessively monitoring dashboards
```

**Output:**
```markdown
## ABCDE Disputation: Production Outage Self-Blame

**Date:** 2026-01-28
**Subject:** Senior engineer

---

### A - Adversity
**What happened (facts only):**
A system outage occurred that affected customers for 2 hours. The root cause was a code change that passed code review.

---

### B - Belief
**Your interpretation:**
"I should have caught this in code review. I'm failing at my job."

**Belief type:** Personal (internal attribution) + Permanent ("failing" = ongoing state)

---

### C - Consequences
**Emotional:**
- Shame and guilt
- Anxiety about future reviews

**Behavioral:**
- Avoiding team interactions
- Obsessively monitoring dashboards (hypervigilance)

---

### D - Disputation

#### Evidence Challenge
**Question:** What facts contradict this belief?
**Evidence:**
- The change was authored by another engineer, not you
- Code review caught 3 other issues in that same PR
- No single reviewer catches everything - that's why we have multiple review stages
- You have successfully caught issues in the past that prevented outages
**Reframe:** "I contributed to review but code review is one of many safeguards, and no single person catches everything."

#### Alternatives Challenge
**Question:** What other explanations exist?
**Alternatives:**
1. The bug was subtle and would have required specific domain knowledge to catch
2. The testing environment didn't expose the failure condition
3. The monitoring didn't alert until customer impact occurred
4. Time pressure may have compressed the review cycle
**Reframe:** "Multiple factors contributed to this outage; code review was one checkpoint among many that could have caught it."

#### Implications Challenge
**Question:** Even if you should have caught it, what are realistic implications?
**Reality check:**
- Missing something in code review does not mean "failing at job"
- Every experienced engineer has stories of things they missed
- The realistic implication is: learn from it and improve the process
**Reframe:** "Even if I could have caught this, missing it means I have a learning opportunity, not that I'm failing overall."

#### Usefulness Challenge
**Question:** Is this belief helping you?
**Cost of belief:**
- Shame is causing withdrawal from the team that needs collaboration
- Obsessive monitoring is unsustainable and shows lack of trust in systems
- Self-blame prevents systemic improvements
**More useful belief:** "I'll lead the effort to improve our review checklist and add a test case for this failure mode. That turns this setback into a contribution."

---

### E - Energization

**Emotional shift:**
From shame and anxiety to determination and ownership of improvement

**Constructive action:**
1. Propose review checklist addition for this failure class
2. Write the test case that would have caught this
3. Share learning with team (model learning from failure)

**Commitment:**
"I will draft the review checklist improvement by end of week and present it at our next team meeting."

---

### Summary

**Original belief:** "I should have caught this in code review. I'm failing at my job."
**Reframed belief:** "Code review is one safeguard among many. Missing something is an opportunity to improve the process, not evidence of overall failure."
**Key insight:** Personal blame blocked systemic improvement. Shifting from "I failed" to "we can improve" enables constructive action.
```

---

## Integration

This skill follows `explanatory-style-analysis` (which diagnoses the pessimistic dimensions to dispute).

Part of the Martin Seligman expert methodology. Often used after:
- `perma-assessment` reveals low well-being due to pessimistic patterns
- Incidents trigger self-blame spirals
- Team retrospectives surface blame dynamics

---

## Success Criteria

Disputation is complete when:
- [ ] Adversity stated as objective fact (no interpretation)
- [ ] Belief explicitly identified and quoted
- [ ] Consequences documented (emotional and behavioral)
- [ ] At least 3 of 4 disputation strategies applied
- [ ] Each disputation includes evidence and reframe
- [ ] Energization captures emotional shift and action commitment
- [ ] Summary shows clear before/after belief transformation