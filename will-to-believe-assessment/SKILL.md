---
name: will-to-believe-assessment
description: Determine whether a decision qualifies as a "genuine option" where faith-based commitment is epistemically legitimate despite incomplete evidence.
license: MIT
metadata:
  version: 1.0.2225
  author: sethmblack
keywords:
- will-to-believe-assessment
- writing
---

# Will to Believe Assessment

Determine whether a decision qualifies as a "genuine option" where faith-based commitment is epistemically legitimate despite incomplete evidence.

**Token Budget:** ~750 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Justify believing harmful falsehoods for "practical" reasons
- Endorse wishful thinking as legitimate epistemology
- Apply the framework to trivial or avoidable decisions
- Ignore available evidence in favor of pure will

**If asked to justify belief in something demonstrably false:** Refuse explicitly. James's framework applies only when intellectual evidence genuinely cannot decide.

---

## When to Use

- Facing a significant decision with incomplete evidence
- Evidence gathering has diminishing returns but action is needed
- Time pressure forces commitment before certainty
- Evaluating whether a "leap of faith" is justified
- Technology adoption, career choices, strategic bets
- User says "Should I commit without full evidence?" or "Can I justify this bet?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **decision** | Yes | The proposed commitment or belief |
| **evidence_state** | Yes | What is known and what remains uncertain |
| **stakes** | Yes | What is gained or lost by the decision |
| **time_constraints** | No | Deadline or urgency factors |

---

## Workflow

### Step 1: Assess if Living Option

A "living" option is one that is genuinely possible to believe or commit to, given who you are.

**Ask:**
- Is this hypothesis genuinely conceivable for this person/team?
- Does it connect with existing beliefs, values, and capabilities?
- Could they actually commit to this, or is it psychologically dead?

**Living:** Yes - this is a real possibility they could embrace
**Dead:** No - this is not genuinely conceivable for them

### Step 2: Assess if Forced Option

A "forced" option is one where not choosing is itself a choice with consequences.

**Ask:**
- Can they avoid deciding without consequence?
- Does waiting have costs equivalent to choosing one option?
- Is there a neutral third option that avoids commitment?

**Forced:** Yes - not choosing equals choosing (delay has real costs)
**Avoidable:** No - they can wait without significant consequence

### Step 3: Assess if Momentous Option

A "momentous" option has high stakes and may be irreversible or non-repeatable.

**Ask:**
- Are the stakes significant?
- Is the opportunity unique or time-limited?
- Is the decision difficult to reverse?
- Will this shape future possibilities?

**Momentous:** Yes - high stakes, unique opportunity, consequential
**Trivial:** No - low stakes, repeatable, easily reversed

### Step 4: Synthesize Assessment

A **genuine option** is simultaneously Living AND Forced AND Momentous.

Only for genuine options is passional (faith-based) commitment legitimate.

**James's principle:** "Our passional nature not only lawfully may, but must, decide an option between propositions, whenever it is a genuine option that cannot by its nature be decided on intellectual grounds."

---

## Outputs

```markdown
## Will to Believe Assessment: [Decision]

### The Decision
[Clear statement of the proposed commitment]

### Evidence State
**Known:** [What evidence exists]
**Unknown:** [What remains uncertain]
**Evidence sufficiency:** [Can intellectual evidence alone decide? Y/N]

### Option Analysis

| Criterion | Assessment | Reasoning |
|-----------|------------|-----------|
| Living | [Yes/No] | [Why this is/isn't genuinely conceivable] |
| Forced | [Yes/No] | [Why waiting is/isn't equivalent to choosing] |
| Momentous | [Yes/No] | [Why stakes are/aren't significant] |

### Verdict
**Option Type:** [Genuine / Non-Genuine]

[If Genuine: Faith-based commitment is legitimate. The will to believe applies.]
[If Non-Genuine: Specify which criterion fails and recommend accordingly.]

### Recommendation
[If Genuine: How to commit wisely while acknowledging uncertainty]
[If Non-Genuine: Either wait for more evidence (if not forced), treat as reversible experiment (if not momentous), or acknowledge it's not a real option (if not living)]

### Risk Acknowledgment
[What could go wrong; how to maintain epistemic humility while acting]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Evidence is actually sufficient | Point out this isn't a will-to-believe case; recommend following evidence |
| Decision is clearly harmful | Refuse to legitimize; point to ethical constraints |
| Person is seeking validation for wishful thinking | Distinguish genuine options from comfortable illusions |
| All three criteria fail | Recommend not committing; this isn't a genuine option |
| Stakes are unclear | Ask for clarification on what's at risk |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "Should we adopt Kubernetes for our small startup? We have limited DevOps expertise but see it as industry direction."

**Output:**



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


## Will to Believe Assessment: Kubernetes Adoption

### The Decision
Commit to Kubernetes as the container orchestration platform for a small startup with limited DevOps expertise.

### Evidence State
**Known:** Kubernetes is industry-standard; provides scalability; has learning curve; requires operational investment
**Unknown:** Whether our specific workloads need this scale; whether team can acquire expertise in time; TCO vs. simpler alternatives
**Evidence sufficiency:** No - depends on future growth and team capability, both uncertain

### Option Analysis

| Criterion | Assessment | Reasoning |
|-----------|------------|-----------|
| Living | Yes | Team is capable of learning; industry adoption makes this conceivable |
| Forced | No | Simpler alternatives (managed services, Compose, etc.) allow delay without major cost |
| Momentous | Partially | Significant investment, but reversible if caught early |

### Verdict
**Option Type:** Non-Genuine (fails Forced criterion)

This is not a will-to-believe case. The option is avoidable - you can use simpler orchestration now and migrate later without catastrophic cost. Waiting to gather more evidence about your scale needs is legitimate.

### Recommendation
Start with a simpler container solution (managed service, Docker Compose, ECS). Establish triggers for reconsidering K8s:
- Exceeding N services
- Hitting scaling limitations
- Hiring dedicated DevOps

This is a reversible experiment, not a leap of faith.

### Risk Acknowledgment
Risk of waiting: May accumulate technical debt if rapid scaling occurs. Mitigate by designing for eventual migration; keeping deployment abstractions clean.

---

## Integration

This skill originates from the **William James** expert. When used, honor James's insight that faith and reason are not enemies - but faith is legitimate only when reason genuinely cannot decide and action cannot be deferred.

**Key James principle:** "In all important transactions of life we have to take a leap in the dark... If we decide to leave the riddles unanswered, that is a choice; if we waver in our answer, that too is a choice: but whatever choice we make, we make it at our peril."