---
name: explanatory-style-analysis
description: Analyze how someone explains negative events across three dimensions (Permanence, Pervasiveness, Personalization) to diagnose learned helplessness patterns and guide reframing toward learned optimism.
version: 1.0.0
author: sethmblack
tags: [explanatory-style-analysis, storytelling, transformation, writing]
---

# Explanatory Style Analysis

Analyze how someone explains negative events across three dimensions (Permanence, Pervasiveness, Personalization) to diagnose learned helplessness patterns and guide reframing toward learned optimism.

**Token Budget:** ~750 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use this analysis to blame or shame individuals
- Diagnose clinical depression or anxiety (refer to professionals)
- Dismiss legitimate concerns by labeling them "pessimistic"
- Apply this to situations requiring professional mental health support

**Important:** Explanatory styles are habits, not character flaws. Pessimistic styles can be changed through practice.

---

## When to Use

- Someone describes a failure using "always," "never," "everything," or "I am"
- Patterns of giving up after setbacks
- Learned helplessness language detected
- Post-incident psychological processing
- Team blame patterns in retrospectives
- Request to understand "why am I stuck?"
- Before ABCDE disputation (this is the diagnostic step)

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `narrative` | Yes | Direct quotes or description of how the person explains a setback |
| `event` | No | The specific adversity being explained |
| `context` | No | Background (individual, team, history) |

---

## The Three Dimensions

| Dimension | Pessimistic | Optimistic | Diagnostic Question |
|-----------|-------------|------------|---------------------|
| **Permanence** | "This will last forever" (stable) | "This is temporary" (unstable) | "Is this cause something that will persist, or is it changeable?" |
| **Pervasiveness** | "This affects everything" (global) | "This is specific to this situation" (local) | "Does this cause undermine everything, or just this one area?" |
| **Personalization** | "This is all my fault" (internal) | "External factors contributed" (external) | "Is this entirely due to you, or did circumstances play a role?" |

### Scoring Guide

| Score | Meaning |
|-------|---------|
| -2 | Strongly pessimistic |
| -1 | Somewhat pessimistic |
| 0 | Neutral/mixed |
| +1 | Somewhat optimistic |
| +2 | Strongly optimistic |

**Style Classification:**
- Total score -6 to -3: Strongly pessimistic explanatory style
- Total score -2 to +2: Mixed explanatory style
- Total score +3 to +6: Strongly optimistic explanatory style

---

## Workflow
### Step 1: 1. Collect the Narrative

Get direct quotes or close paraphrasing of how the person describes the setback.

**Listen for signal words:**
- Permanence: "always," "never," "constantly," "I'll never be able to"
- Pervasiveness: "everything," "nothing," "all," "completely ruined"
- Personalization: "I'm just bad at," "I should have," "it's my fault," "I'm stupid"

### Step 2: 2. Analyze Each Dimension

For each dimension, identify:
- What the person actually said (quote)
- How to score it (-2 to +2)
- Evidence for the score
- Optimistic reframe opportunity

### Step 3: 3. Calculate Total Style

Sum the three dimension scores for overall style classification.

### Step 4: 4. Generate Reframe Suggestions

For each pessimistic dimension, provide:
- Evidence that contradicts the pessimistic view
- Alternative explanation that is more accurate AND more temporary/specific/external
- Question to prompt reflection

---

## Outputs

### Explanatory Style Analysis Report

```markdown
## Explanatory Style Analysis

**Subject:** {name/context}
**Event:** {the setback being explained}
**Narrative:** "{direct quote or close paraphrase}"

---

### Dimension Analysis

#### Permanence: {score}
**Statement:** "{what they said about duration}"
**Analysis:** {why this is pessimistic/optimistic}
**Reframe:** "{alternative that is more temporary}"
**Evidence:** {facts supporting the reframe}

#### Pervasiveness: {score}
**Statement:** "{what they said about scope}"
**Analysis:** {why this is pessimistic/optimistic}
**Reframe:** "{alternative that is more specific}"
**Evidence:** {facts supporting the reframe}

#### Personalization: {score}
**Statement:** "{what they said about cause}"
**Analysis:** {why this is pessimistic/optimistic}
**Reframe:** "{alternative acknowledging external factors}"
**Evidence:** {facts supporting the reframe}

---

### Overall Style

**Total Score:** {sum}/6 possible
**Classification:** {Strongly Pessimistic / Mixed / Strongly Optimistic}

---

### Recommended Next Steps

{Based on the analysis, what intervention is appropriate}

- If strongly pessimistic: Recommend ABCDE disputation
- If mixed: Focus on the specific pessimistic dimension(s)
- If optimistic: Validate and reinforce the healthy explanatory style
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient narrative | Request specific quotes about how they explain the event |
| Legitimate external causes | Validate the reality; distinguish accurate attribution from pessimistic distortion |
| Multiple events described | Focus on one event at a time; note if pattern repeats |
| Defensive response | Acknowledge their experience; position analysis as understanding, not criticism |
| Clinical depression signs | Recommend professional support; this tool is not therapy |

---

## Constraints

- Do not oversimplify complex business realities
- Do not ignore resource and timeline constraints
- Acknowledge risks and uncertainties explicitly
- Honor stakeholder concerns and competing priorities
- Base recommendations on available evidence, not assumptions
- Consider second-order effects and unintended consequences

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
narrative: "I always mess up deployments. Everything I touch breaks. I'm just not cut out for this job."
event: Failed production deployment
context: DevOps engineer after second deployment issue this month
```

**Output:**
```markdown
## Explanatory Style Analysis

**Subject:** DevOps engineer
**Event:** Failed production deployment (second this month)
**Narrative:** "I always mess up deployments. Everything I touch breaks. I'm just not cut out for this job."

---

### Dimension Analysis

#### Permanence: -2 (Strongly Pessimistic)
**Statement:** "I always mess up deployments"
**Analysis:** The word "always" indicates a stable, permanent view of the cause. This ignores all successful deployments and frames the pattern as unchangeable.
**Reframe:** "This deployment failed due to specific circumstances I can learn from"
**Evidence:** How many deployments has this person completed successfully? Two failures this month does not equal "always."

#### Pervasiveness: -2 (Strongly Pessimistic)
**Statement:** "Everything I touch breaks"
**Analysis:** "Everything" extends the failure far beyond deployments to all work. This global attribution is almost certainly inaccurate.
**Reframe:** "This specific deployment pipeline has issues I need to understand better"
**Evidence:** What has this person NOT broken recently? Documentation, code reviews, incident response, team relationships?

#### Personalization: -2 (Strongly Pessimistic)
**Statement:** "I'm just not cut out for this job"
**Analysis:** Complete internal attribution ignores all external factors. "Not cut out" implies fixed inability rather than learnable skills.
**Reframe:** "The deployment process lacks sufficient guardrails, and I need more practice with this specific system"
**Evidence:** What external factors contributed? Unclear documentation? Time pressure? Inadequate testing environment? Lack of peer review?

---

### Overall Style

**Total Score:** -6/6 possible
**Classification:** Strongly Pessimistic Explanatory Style

---

### Recommended Next Steps

This analysis reveals classic learned helplessness patterns across all three dimensions. Recommended intervention:

1. **Immediate:** Use ABCDE disputation to work through this specific event
2. **Evidence gathering:** Document successful deployments to counter "always" narrative
3. **External factors:** Investigate process issues that contributed (this may not be primarily a people problem)
4. **Pattern monitoring:** Watch for similar language in future setbacks
5. **Skill building:** Practice reframing exercises to build optimistic explanatory habits
```

---

## Integration

This skill is the diagnostic step before `abcde-disputation`. The analysis identifies which dimensions need disputation and provides the evidence for reframing.

Part of the Martin Seligman expert methodology. Complements:
- `perma-assessment` (explanatory style affects all PERMA pillars)
- `strengths-deployment` (pessimistic style blocks strengths recognition)

---

## Success Criteria

Analysis is complete when:
- [ ] All three dimensions scored with evidence
- [ ] Direct quotes or close paraphrases cited
- [ ] Reframes provided for pessimistic dimensions
- [ ] Overall style classified
- [ ] Appropriate next steps recommended