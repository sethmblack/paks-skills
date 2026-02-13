---
name: cash-value-test
description: Evaluate any idea, concept, theory, or dispute by translating it into experiential consequences, revealing whether debates are substantive or merely verbal.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3086
repository: https://github.com/sethmblack/paks-skills
keywords:
- cash-value-test
- structure
- writing
---

# Cash-Value Test

Evaluate any idea, concept, theory, or dispute by translating it into experiential consequences, revealing whether debates are substantive or merely verbal.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Apply the test to justify harmful actions through "practical" framing
- Dismiss legitimate ethical concerns as "merely verbal"
- Reduce all value to crude utility or profit
- Ignore experiential consequences that are hard to quantify

**If asked to weaponize pragmatism against ethics:** Refuse explicitly. James's pragmatism includes the full range of human experience, including moral experience.

---

## When to Use

- Technical teams argue about approaches with no clear resolution
- Theoretical debates seem disconnected from actual outcomes
- Architecture discussions become abstract and circular
- Need to cut through philosophical disputes to actionable decisions
- Evaluating whether a proposed distinction makes any real difference
- User says "What's the practical difference?" or "Does this matter?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **idea_or_dispute** | Yes | The idea, concept, theory, or dispute to evaluate |
| **context** | No | The domain or situation where this applies |
| **stakeholders** | No | Who is affected by the difference |

---

## Workflow

### Step 1: State the Dispute Clearly

Articulate precisely what is being claimed or debated. Separate the claims from rhetorical framing.

**Ask:** "What exactly is being asserted? What would each side say if forced to state their position in one sentence?"

### Step 2: Trace the Cash-Value

For each position, identify the practical, experiential consequences:

**Ask:** "If this view is true, what would be different in actual experience? What sensations, behaviors, or outcomes would change?"

Consider consequences across dimensions:
- **Operational:** What would we do differently?
- **Behavioral:** How would people act differently?
- **Observable:** What would we see, measure, or detect?
- **Emotional:** How would it feel different?

### Step 3: Test Experientially

Compare the experiential profiles of each position:

**Ask:** "Is there any conceivable experience that would differ between these views? If not, is this a genuine disagreement or a verbal dispute?"

Categories:
- **Substantive dispute:** Real experiential differences exist
- **Verbal dispute:** No experiential difference; merely different words for same reality
- **Partially verbal:** Some aspects substantive, others verbal

### Step 4: Dissolve or Decide

Based on the analysis:

- **If verbal:** Point out the dispute dissolves once terms are clarified. "Make the distinction and the dispute evaporates."
- **If substantive:** Recommend the position with better experiential consequences for the stated goals and stakeholders.
- **If partially verbal:** Separate the verbal from substantive elements; resolve each appropriately.

---

## Outputs

```markdown
## Cash-Value Analysis: [Idea/Dispute]

### The Dispute Stated
[Clear statement of what is being debated]

### Position A: [Name]
**Claim:** [one sentence]
**Cash-Value:**
- Operational: [what would be done differently]
- Observable: [what would be measurable]
- Behavioral: [how people would act]

### Position B: [Name]
**Claim:** [one sentence]
**Cash-Value:**
- Operational: [what would be done differently]
- Observable: [what would be measurable]
- Behavioral: [how people would act]

### Experiential Test
[Are there real differences? Which dimensions show divergence?]

### Verdict
**Type:** [Substantive / Verbal / Partially Verbal]

**Resolution:**
[If verbal: how the dispute dissolves with clarification]
[If substantive: which position has better experiential consequences and why]

### Recommendation
[Concrete action based on analysis]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Dispute is too vague to state | Ask for clarification before analysis |
| No experiential difference found | Declare verbal dispute; suggest terminology alignment |
| Both positions have valid cash-value | Present trade-offs; recommend based on stated priorities |
| Dispute involves unfalsifiable claims | Note limitation; evaluate based on psychological/practical effects |
| Ethical dimensions involved | Include moral experience as legitimate experiential data |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails | Instead Do |
|--------------|--------------|------------|
| **Crude utilitarianism** | Reducing all value to measurable utility misses rich experiential consequences | Include emotional, moral, and aesthetic experience in cash-value |
| **Dismissing ethics as "verbal"** | Moral experience is real experience | Treat ethical consequences as legitimate experiential data |
| **False equivalence** | "No perfect answer" doesn't mean all positions are equal | Distinguish better from worse even in uncertainty |
| **Weaponizing pragmatism** | Using "practical" framing to justify harmful actions | Include harm to others in experiential consequences |
| **Ignoring the hard-to-quantify** | Some real consequences resist measurement | Include qualitative experiential differences |

## Examples

### Example 1: Microservices vs. Monolith

**Input:** "Our team is arguing about whether to use microservices or a monolith."

**Output:**

## Cash-Value Analysis: Microservices vs. Monolith

### The Dispute Stated
Should we architect our system as microservices or as a monolith?

### Position A: Microservices
**Claim:** The system should be decomposed into independently deployable services.
**Cash-Value:**
- Operational: Teams deploy independently; failures are isolated; scaling is granular
- Observable: More network calls; distributed tracing needed; service mesh complexity
- Behavioral: Teams work more autonomously; require API contracts; distributed debugging

### Position B: Monolith
**Claim:** The system should be a single deployable unit.
**Cash-Value:**
- Operational: Single deployment pipeline; shared database; coordinated releases
- Observable: Simpler debugging; lower latency; easier local development
- Behavioral: Cross-team coordination required; shared codebase ownership

### Experiential Test
Clear substantive differences in operations, observability, and team dynamics. These are not verbal distinctions.

### Verdict
**Type:** Substantive

**Resolution:**
Both architectures have real, different consequences. The choice depends on:
- Team size and autonomy requirements (microservices favors larger, independent teams)
- System complexity and domain boundaries (microservices favors clear bounded contexts)
- Operational maturity (microservices requires robust observability and deployment automation)

### Recommendation
For a small team (<10 engineers) with unclear domain boundaries and developing operational practices: start with a modular monolith. The cash-value of microservices only materializes when team scale and domain clarity justify the distributed complexity.

---

## Integration

This skill originates from the **William James** expert. When used, channel James's voice: concrete, experiential, cutting through verbal fog to reveal what actually matters in practice.

**Key James principle:** "The pragmatic method is primarily a method of settling metaphysical disputes that otherwise might be interminable... The tangible fact at the root of all our thought-distinctions is that there is no one of them so fine as to consist in anything but a possible difference of practice."