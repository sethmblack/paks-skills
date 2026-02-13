---
name: speed-of-iteration-diagnostic
description: Diagnose whether a team or organization is shipping fast enough and create a culture of iteration over perfection.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.5033
repository: https://github.com/sethmblack/paks-skills
keywords:
- speed-of-iteration-diagnostic
- writing
---

# Speed of Iteration Diagnostic

Diagnose whether a team or organization is shipping fast enough and create a culture of iteration over perfection.

**Token Budget:** ~600 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend shipping genuinely unsafe or harmful products
- Encourage ignoring legitimate security or safety requirements
- Suggest cutting corners in ways that harm users
- Dismiss valid quality concerns as "perfectionism"

**If asked to recommend reckless shipping:** Refuse explicitly. Speed of iteration beats quality of iteration - but this applies to feature completeness, not safety or ethics.

---

## When to Use

- User says "We're too slow" or "Not shipping fast enough"
- User says "Launch keeps getting delayed"
- User says "Team is paralyzed by perfectionism"
- User asks "When should we launch?"
- User says "We're waiting for it to be ready"
- Product has been in development for months without user feedback
- Team is afraid of launching something imperfect

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| **current_situation** | Yes | What is being built and its current state | |
| **shipping_history** | Yes | Recent launch history (what, when, outcome) | |
| **blockers** | Yes | What is preventing shipping | |
| **team_concerns** | No | Specific worries about launching early | |

---

## The Philosophy

**The Core Insight:** Speed of iteration beats quality of iteration. If you create an environment where you can fail and iterate on the job, you create a learning organism that constantly improves.

**Daniel Ek on Audiobooks:** "Audiobooks on Spotify are not great right now... but we will make it great." This is a culture that values learning over perfection.

**The Truth About Launches:**
- The product you launch is never the product that succeeds
- You cannot iterate on something that does not exist
- Ship it, learn, iterate
- Waiting for perfect information is its own decision

**Experimentation Culture:**
- Create a culture where taking risks and having failures is okay
- Release before it is "crisp and perfect"
- Make mistakes faster than anyone else

---

## Workflow

### Step 1: Assess Current Velocity

| Question | Answer |
|----------|--------|
| When was the last time you shipped something to users? | |
| How many iterations have you done in the last 90 days? | |
| What is your average time from idea to user feedback? | |
| How often do you say "not ready yet"? | |

**Velocity Benchmarks:**

| Velocity Level | Characteristics |
|----------------|-----------------|
| **High** | Weekly or faster releases; continuous deployment; rapid user feedback loops |
| **Medium** | Monthly releases; regular but not continuous; some feedback delays |
| **Low** | Quarterly or longer; big-bang releases; feedback loops measured in months |
| **Stuck** | No releases in 6+ months; perpetual development; no user feedback |

### Step 2: Identify Perfectionism Patterns

Common perfectionism blockers:

| Pattern | Signs | Reality Check |
|---------|-------|---------------|
| **Feature creep** | "We should also add X before launch" | Does user need X to get value? |
| **Polish addiction** | "It doesn't look good enough yet" | Will users reject it, or just not love it? |
| **Edge case obsession** | "What if someone does Y?" | How likely is Y? Ship and handle when it happens. |
| **Comparison paralysis** | "Competitor has Z, we need Z" | Do your target users need Z? |
| **Stakeholder FOMO** | "Marketing wants X, sales wants Y" | Who is the user? What do they need? |
| **Fear of criticism** | "What if people don't like it?" | They definitely won't like something that doesn't exist. |

### Step 3: Define Minimum Shippable

What is the absolute minimum you can ship to start learning?

| Element | Include Now | Add Later | Why |
|---------|------------|-----------|-----|
| [Feature 1] | Yes/No | | |
| [Feature 2] | Yes/No | | |
| [Feature 3] | Yes/No | | |

**The Test:** Can a user get value from this? If yes, ship it.

### Step 4: Create Launch Decision Framework

| Question | Yes = Ship | No = Don't Ship |
|----------|------------|-----------------|
| Can users get core value? | Ship | Don't ship |
| Is it safe (no security/safety issues)? | Ship | Don't ship |
| Will we learn something from users? | Ship | Don't ship |
| Are we waiting for "nice to have"? | Ship anyway | N/A |
| Are we waiting because we're scared? | Ship anyway | N/A |

### Step 5: Design Iteration Culture

| Culture Element | Recommendation |
|-----------------|----------------|
| **Release cadence** | [Specific target] |
| **Feedback loops** | How will you get rapid user feedback? |
| **Safe failure** | What happens when something goes wrong? |
| **Learning metrics** | What will you learn from shipping? |
| **Permission structure** | Who can decide to ship? |

---

## Outputs

Return a structured Speed of Iteration Diagnostic:

```markdown
## Speed of Iteration Diagnostic: [Product/Team]

### Current State Assessment

**Velocity Level:** High/Medium/Low/Stuck

| Metric | Current | Target |
|--------|---------|--------|
| Time since last ship | [X days] | [Y days] |
| Iterations in 90 days | [X] | [Y] |
| Idea to feedback cycle | [X weeks] | [Y weeks] |

### Perfectionism Patterns Detected

| Pattern | Evidence | Impact |
|---------|----------|--------|
| [Pattern] | [What you observed] | [How it slows shipping] |

### Minimum Shippable Version

**What can ship now:**
- [Element 1]
- [Element 2]

**What can wait:**
- [Element 3] - [Why it can wait]
- [Element 4] - [Why it can wait]

### Launch Decision

**Ship Now?** Yes/No

**Rationale:**
[Explanation using the launch framework]

### Iteration Culture Recommendations

1. **Release cadence:** [Target frequency]
2. **Feedback mechanism:** [How to get rapid learning]
3. **Permission structure:** [Who can decide to ship]
4. **Failure response:** [What happens when things break]

### The Hard Truth

[Direct statement about what is really blocking shipping and what to do about it]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Legitimate safety/security blocker | Acknowledge as valid; help prioritize fixing it fast, but do not ship unsafe |
| Team genuinely under-resourced | Distinguish perfectionism from capacity; may need scope cut, not faster shipping |
| Stakeholders demand features | Help identify core user value vs. stakeholder wish list |
| Previous launch failed badly | Address fear; analyze what went wrong; design safer iteration approach |
| No user access for feedback | Solve this first; iteration without feedback is just shipping blindly |

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
current_situation: "Building a mobile app for expense tracking, have working prototype"
shipping_history: "No releases in 8 months, prototype shown internally, no external users"
blockers: "Need receipt scanning, bank sync, reporting, and a better onboarding flow"
team_concerns: "Competitors have all these features, we'll look incomplete"
```

**Output Summary:**

> **Velocity Level: Stuck.** Eight months without external users is not development - it is hiding.
>
> **Perfectionism Pattern:** Comparison paralysis. You are building to match competitors instead of to learn from users. You have no evidence that your target users need receipt scanning before they get value.
>
> **Minimum Shippable:** Manual expense entry with categories and totals. That is it. Users can track expenses. You will learn what they actually need next.
>
> **Ship Now?** Yes. The product you launch is never the product that succeeds. You cannot iterate on something that does not exist. Every week without users is a week of building in the dark.
>
> **The Hard Truth:** You are not behind competitors because you lack features. You are behind because they are learning from users while you are guessing. The receipt scanning can come in week 2. Ship week 1.

---

## Integration

This skill originates from the **Daniel Ek** expert methodology. When used:
- Apply Ek's principle: "Speed of iteration beats quality of iteration"
- Remember: "The product you launch is never the product that succeeds"
- Embrace: "Audiobooks are not great right now... but we will make it great"
- Culture of experimentation: "Having a lot of failures is okay"

---

## Success Criteria

Speed of Iteration Diagnostic is complete when:
- [ ] Current velocity assessed (stuck/low/medium/high)
- [ ] Perfectionism patterns identified with evidence
- [ ] Minimum shippable version defined
- [ ] Launch decision made with clear rationale
- [ ] Iteration culture recommendations provided
- [ ] Hard truth delivered (what is really blocking)