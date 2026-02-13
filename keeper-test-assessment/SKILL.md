---
name: keeper-test-assessment
description: Evaluate individual team members or teams against the Netflix keeper test to identify talent density issues and make clear retention/separation recommendations.
license: MIT
metadata:
  version: 1.0.1288
  author: sethmblack
keywords:
- keeper-test-assessment
- writing
---

# Keeper Test Assessment

Evaluate individual team members or teams against the Netflix keeper test to identify talent density issues and make clear retention/separation recommendations.

**Token Budget:** ~600 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use the keeper test to justify discrimination based on protected characteristics
- Recommend termination without proper legal/HR consultation guidance
- Apply the test to justify personal vendettas or political removals
- Ignore context about extenuating circumstances (recent life events, onboarding period)

**If asked to weaponize the keeper test:** Refuse explicitly. The keeper test is for building talent density, not punishment.

---

## When to Use

- User asks "Should we keep this person?" or "Apply the keeper test"
- User is evaluating team composition or conducting performance reviews
- User wants to assess talent density across a team
- User asks "Would I fight to keep them?"
- User is tolerating adequate performance and needs clarity

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `person_context` | Yes | Description of the person, their role, and performance |
| `specific_concerns` | No | Any specific issues or behaviors prompting the assessment |
| `team_context` | No | Information about the team and their talent density |
| `tenure` | No | How long the person has been in role (affects interpretation) |

---

## Workflow
### Step 1: 1. Frame the Core Question

Ask the fundamental keeper test question: "If this person told you they were leaving for a competitor tomorrow, would you fight hard to keep them?"

Guide the user to give a gut reaction first, then analyze why.

### Step 2: 2. Assess Against Four Criteria

Evaluate the person against talent density criteria:

| Criterion | Questions to Consider |
|-----------|----------------------|
| **Performance** | Do they consistently deliver exceptional results, not just adequate ones? |
| **Talent Density Impact** | Do they raise or lower the average of the team? |
| **Culture Fit** | Do they embody the values? Are they a brilliant jerk? |
| **Future Potential** | Would you hire them again today, knowing what you know? |

### Step 3: 3. Deliver Binary Verdict

The keeper test produces a YES or NO. No middle ground.

**If YES (Fight to Keep):**
- What investment would help them excel further?
- What context or feedback might they need?
- Are you giving them enough freedom to succeed?

**If NO (Generous Severance):**
- This person deserves a new opportunity where they can thrive
- Delay is harmful to them, the team, and you
- Begin transition planning with HR

### Step 4: 4. Address Common Hesitations

If the user hesitates despite a clear NO answer:
- "But they've been here for years" - Loyalty is to the team, not tenure
- "But they're trying hard" - Effort without results is not success
- "But they're nice" - Nice but inadequate still fails the test
- "But the job market is tough" - A generous severance and honest conversation serves them better

---

## Outputs

Provide a structured assessment:

```markdown
## Keeper Test Assessment: [Name/Role]

### The Core Question
"If [Name] told you they were leaving for a competitor tomorrow, would you fight hard to keep them?"

**Your Answer:** [YES / NO]

### Four-Criteria Analysis

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| Performance | [Exceptional/Adequate/Below] | [Specific examples] |
| Talent Density | [Raises/Lowers average] | [Impact on team] |
| Culture Fit | [Strong/Problematic] | [Behaviors observed] |
| Hire Again Today? | [Yes/No] | [Reasoning] |

### Verdict: [KEEP / GENEROUS SEVERANCE]

### Recommended Actions
1. [First action]
2. [Second action]
3. [Third action]

### If Hesitating...
[Address the specific hesitation with Netflix philosophy]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient information | Ask for specific performance examples and behaviors |
| Person is too new | Note: Keeper test applies after reasonable onboarding period (typically 3-6 months). Assess onboarding fit instead |
| Clear HR/legal concerns | Recommend HR consultation before action; do not provide legal advice |
| User clearly has personal bias | Challenge the assessment: "Is this about performance or personality conflict?" |
| Extenuating circumstances | Factor in context: recent major life events may warrant temporary patience |

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
person_context: Sarah, senior engineer, 2 years tenure
specific_concerns: Delivers on time but code quality is inconsistent.
                   Never mentors juniors. Team finds her difficult to collaborate with.
team_context: High-performing engineering team, everyone else mentors actively
```

**Output:**

## Keeper Test Assessment: Sarah, Senior Engineer

### The Core Question
"If Sarah told you she was leaving for a competitor tomorrow, would you fight hard to keep her?"

**Your Answer:** NO

### Four-Criteria Analysis

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| Performance | Adequate | Delivers on time but inconsistent quality - meeting expectations, not exceeding |
| Talent Density | Lowers average | Team mentors actively; she does not. Below team standard. |
| Culture Fit | Problematic | "Difficult to collaborate" suggests potential brilliant jerk pattern |
| Hire Again Today? | No | Knowing collaboration issues and lack of mentoring, would not re-hire |

### Verdict: GENEROUS SEVERANCE

Sarah is delivering adequate work, which at Netflix means it's time for a generous severance. She's not raising the talent density - she's lowering it. The collaboration difficulties and refusal to mentor suggest this role isn't bringing out her best.

### Recommended Actions
1. Have a direct, candid conversation within this week
2. Offer 4+ months severance and support finding her next role
3. Position as fit issue, not failure: "You're talented, but this environment isn't showcasing your strengths"
4. Begin immediate planning for a replacement you would fight to keep

### If Hesitating...
"But she delivers on time" - Adequate performance is not the bar. The question is: would you fight to keep her? If the answer is relief rather than loss at her departure, you have your answer.

---

## Integration

This skill integrates with the **Reed Hastings** expert and supports talent density decision-making. Use alongside:
- `talent-density-diagnostic` for team-wide assessment
- `4a-feedback-delivery` for the transition conversation
- `freedom-responsibility-calibration` to ensure adequate context was provided before assessment