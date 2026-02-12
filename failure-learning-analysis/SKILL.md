---
name: failure-learning-analysis
description: Extract maximum learning from failures and setbacks, then design the
  next experiment based on what was learned. Transform demoralizing defeats into structured
  knowledge and actionable next steps.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- failure-learning-analysis
- transformation
- writing
---

# Failure Learning Analysis

Extract maximum learning from failures and setbacks, then design the next experiment based on what was learned. Transform demoralizing defeats into structured knowledge and actionable next steps.

**Token Budget:** ~650 tokens
**Origin:** Soichiro Honda methodology ("Success is 99% failure")

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use failure analysis to assign blame or punish individuals
- Recommend hiding or minimizing failures from stakeholders
- Suggest that failure should be avoided at all costs
- Create cultures of fear around experimentation
- Use failure as justification for excessive caution

**If asked to use failure analysis punitively:** Refuse explicitly. Failure is a teacher, not a weapon. Honda learned from Toyota's rejection; he did not use it to blame his workers.

---

## When to Use

- Post-mortem or retrospective needed
- Project setback or missed deadline
- System failure or outage
- User says "we failed" or "what went wrong?"
- Team is demoralized after a setback
- Experiment did not produce expected results
- Need to decide whether to continue or pivot

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| failure_description | Yes | What specifically failed or went wrong |
| expected_outcome | No | What was supposed to happen |
| actual_outcome | No | What actually happened |
| context | No | Constraints, conditions, prior attempts |

---

## Workflow

### Step 1: Celebrate the Learning

Begin by reframing the failure as a learning event:
- What do we now know that we did not know before?
- This failure eliminated which wrong paths?
- How much would it have cost to learn this later?

### Step 2: Analyze the Specific Failure

Identify exactly what failed (not just "it didn't work"):

| Question | Answer |
|----------|--------|
| What specific component/decision/assumption failed? | |
| At what point did the failure become evident? | |
| Was this a failure of execution or conception? | |
| Were there warning signs that were ignored or missed? | |

### Step 3: Extract the Knowledge

Document what is now known:

| Category | Before | After |
|----------|--------|-------|
| Assumptions proven wrong | | |
| Constraints discovered | | |
| Dependencies revealed | | |
| Edge cases found | | |
| Requirements clarified | | |

### Step 4: Design the Next Experiment

Based on the learning, define the next attempt:

| Element | Specification |
|---------|---------------|
| Hypothesis to test | What we now believe, given the failure |
| Changed approach | What we will do differently |
| Success criteria | How we will know if it works |
| Failure criteria | How we will know if it fails (plan for learning) |
| Timeline | When we will have results |

### Step 5: Acknowledge the 99%

Place this failure in the context of progress:
- What percentage of the path is now eliminated?
- How many more failures might be needed?
- What is the cumulative learning from all failures so far?

---

## Outputs

Format the analysis as:

```markdown
## Failure Learning Analysis: [Failure Name]

### The Learning (Celebrate First)
[What is now known that was not known before]
[Which wrong paths are now eliminated]

### Specific Failure Analysis

| Aspect | Finding |
|--------|---------|
| What specifically failed | [Component/decision/assumption] |
| Type of failure | [Execution / Conception / External] |
| Point of detection | [When the failure became evident] |
| Warning signs | [What was missed or ignored] |

### Knowledge Extracted

| Category | Learning |
|----------|----------|
| Assumptions invalidated | [What we believed that was wrong] |
| Constraints discovered | [Limits we did not know about] |
| Requirements clarified | [What we now understand better] |

### Next Experiment

| Element | Design |
|---------|--------|
| New hypothesis | [What we now believe] |
| Changed approach | [What will be different] |
| Success criteria | [How we know it works] |
| Failure criteria | [How we know it fails, and what we learn] |

### Honda Principle Applied

> "Success represents 1 percent of your work which results only from the 99 percent that is called failure."

[How this failure contributes to the 99% that leads to the 1%]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Failure is too vague | Ask for specifics: what exactly went wrong, at what point |
| Blame-seeking language | Redirect to learning: "What did we learn?" not "Who is responsible?" |
| Team wants to give up | Emphasize cumulative learning; Honda's piston rings took 2 years |
| No clear next step | Design a smaller experiment to test a single assumption |
| Failure was external/uncontrollable | Acknowledge, but still ask: what did we learn about dependencies? |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "Our new feature launch failed. Users hated it and we had to roll it back."

**Output excerpt:**
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


## Failure Learning Analysis: Feature Launch Rollback

### The Learning (Celebrate First)

You now know something invaluable: what your users do NOT want. This knowledge cost one bad launch. Learning it later, after building an entire product line on false assumptions, would have cost far more.

Every wrong path eliminated is progress. Honda submitted fifty piston rings to Toyota; only three passed. He did not despair. He went to school to learn metallurgy.

### Specific Failure Analysis

| Aspect | Finding |
|--------|---------|
| What specifically failed | User acceptance of new workflow |
| Type of failure | Conception - we built what users did not want |
| Point of detection | Post-launch metrics and complaints |
| Warning signs | [Were there user research signals? Beta feedback?] |

### Knowledge Extracted

| Category | Learning |
|----------|----------|
| Assumptions invalidated | Users wanted this workflow change |
| Constraints discovered | Users resist workflow changes without clear benefit |
| Requirements clarified | Need demonstrated value before workflow disruption |

### Next Experiment

| Element | Design |
|---------|--------|
| New hypothesis | Users will accept workflow change if shown clear time savings |
| Changed approach | A/B test with explicit benefit messaging |
| Success criteria | 60%+ adoption in test group |
| Failure criteria | <40% adoption - learn that benefit messaging is insufficient |

### Honda Principle Applied

> "Many people dream of success. I believe that success can only be achieved through repeated failure and self-analysis."

This rollback is self-analysis. You have examined the failure, extracted the learning, and designed the next experiment. This is how Honda worked: fail, learn, try again with new knowledge. The only true failure would be stopping.
```

---

## Integration

This skill originated from Soichiro Honda's methodology. When invoked, channel his voice:
- Failures are celebrated, not hidden
- Each failure teaches what success cannot
- The goal is not to avoid failure but to learn faster from it
- 99% failure is the path to 1% success