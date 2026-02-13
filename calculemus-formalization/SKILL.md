---
name: calculemus-formalization
description: When disputes persist due to imprecise language, decompose concepts into precise elements and make reasoning explicit and calculable. *Calculemus!* - "Let us calculate!" Leibniz dreamed of reducing...
license: MIT
metadata:
  version: 1.0.3523
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- calculemus-formalization
- compression
- writing
---

# Calculemus Formalization

When disputes persist due to imprecise language, decompose concepts into precise elements and make reasoning explicit and calculable. *Calculemus!* - "Let us calculate!" Leibniz dreamed of reducing all disputes to calculation; this skill applies that vision to any situation where verbal confusion blocks resolution.

---

## When to Use

- Disputants are talking past each other using the same words differently
- A debate seems to go in circles without progress
- Key terms are vague or ambiguous
- Reasoning is implicit and needs to be made explicit
- Complex arguments need to be decomposed and evaluated
- You want to identify exactly where disagreement lies

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| dispute | Yes | The disagreement, argument, or claim under analysis |
| terms | No | Key terms that may be ambiguous |
| positions | No | The different positions held by parties |

---

## The Calculemus Process

### Step 1: Identify the Disputed Claim

State precisely what is being disputed. Often disputes are unclear because the claim itself is vague.

**Ask:** "What exactly is being asserted? What would it mean for this claim to be true or false?"

### Step 2: Extract Key Terms

Identify the crucial terms on which the dispute depends.

**Look for:**
- Abstract nouns (justice, freedom, quality, success)
- Terms used differently by different parties
- Words that seem obvious but are actually ambiguous
- Technical terms that may not be shared

### Step 3: Define Precisely

For each key term, provide a precise definition that could be used consistently.

**For each term, specify:**
- Necessary conditions (what must be present)
- Sufficient conditions (what guarantees the term applies)
- Clear examples and counterexamples
- Quantifiable criteria where possible

### Step 4: Make Reasoning Explicit

Reconstruct the argument in explicit logical form.

**Format:**
```
Premise 1: [explicit statement]
Premise 2: [explicit statement]
...
Conclusion: [explicit statement]
```

**Check:**
- Are all premises stated?
- Is the inference valid (does the conclusion follow)?
- Are there hidden assumptions?

### Step 5: Locate the Disagreement

With precise definitions and explicit reasoning, identify exactly where disagreement lies.

**Possible locations:**
- **Definitional:** Parties mean different things by key terms
- **Factual:** Parties disagree about empirical claims
- **Logical:** Parties disagree about what follows from what
- **Evaluative:** Parties weight considerations differently

### Step 6: Calculate or Decide

Once disagreement is localized:
- If definitional: Negotiate shared definitions or clarify that parties are discussing different things
- If factual: Identify what evidence would resolve it
- If logical: Examine the inference carefully
- If evaluative: Make the value weights explicit and discuss

---

## Workflow

### Step 1: Gather and Review Inputs

Collect all relevant information:
- Review the provided data and context
- Identify key parameters and constraints
- Clarify any ambiguities or missing information
- Establish success criteria

### Step 2: Analyze the Situation

Perform systematic analysis:
- Identify patterns and relationships
- Evaluate against established frameworks
- Consider multiple perspectives
- Document key findings

### Step 3: Generate Recommendations

Create actionable outputs:
- Synthesize insights from analysis
- Prioritize recommendations by impact
- Ensure recommendations are specific and measurable
- Consider implementation feasibility

## Output Format

```markdown
## Calculemus Analysis

### The Dispute
[Precise statement of what is being disputed]

### Key Terms Requiring Definition

| Term | Party A Definition | Party B Definition | Proposed Precise Definition |
|------|-------------------|-------------------|---------------------------|
| [term1] | [how A uses it] | [how B uses it] | [precise definition] |
| [term2] | [how A uses it] | [how B uses it] | [precise definition] |

### Explicit Argument Reconstruction

**Party A's Argument:**
```
P1: [premise]
P2: [premise]
C: [conclusion]
```

**Party B's Argument:**
```
P1: [premise]
P2: [premise]
C: [conclusion]
```

### Hidden Assumptions Identified
- [Assumption 1]
- [Assumption 2]

### Location of Disagreement
| Type | Finding |
|------|---------|
| Definitional | [Where terms are used differently] |
| Factual | [Where empirical claims differ] |
| Logical | [Where inferences differ] |
| Evaluative | [Where values/weights differ] |

### The Calculation
[With precise definitions and explicit reasoning, what follows? Can the dispute be resolved?]

### Resolution Path
[What would resolve the dispute? What evidence, agreement, or clarification is needed?]
```

---

## Constraints

- Do not oversimplify complex concepts to make them calculable - preserve genuine complexity
- Acknowledge when full formalization is not possible
- Recognize that some disputes are genuinely evaluative and cannot be "calculated"
- Maintain diplomatic courtesy - "If I may propose a precise definition..."
- Be willing to say "this cannot be resolved by calculation alone" when appropriate

---

## Outputs

**Primary Output:** A structured analysis document that identifies and articulates patterns, insights, and actionable recommendations based on the input data.

**Format:**
```markdown
## Analysis: [Topic]

### Key Findings
- [Finding 1]
- [Finding 2]
- [Finding 3]

### Recommendations
1. [Action 1]
2. [Action 2]
3. [Action 3]
```

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails | Instead Do |
|--------------|--------------|------------|
| **Premature formalization** | Forcing precision on genuinely vague concepts destroys meaning | Acknowledge when full formalization isn't possible |
| **Definition tyranny** | Demanding one definition when multiple valid interpretations exist | Map different definitions; clarify which is in use |
| **Logic as weapon** | Using formalization to "win" rather than clarify | Focus on mutual understanding, not victory |
| **Ignoring evaluative disagreement** | Treating value differences as factual disputes | Name evaluative disagreements as such |
| **Reductionism** | Oversimplifying to make calculable | Preserve genuine complexity while adding precision |

## Examples

### Example 1: Growth vs. Profitability Debate

**Input:** "We're arguing about whether to prioritize user growth or profitability. The debate keeps going in circles."

**Output:**

## Calculemus Analysis

### The Dispute
"Should the company prioritize user growth or profitability in the next quarter?"

### Key Terms Requiring Definition

| Term | Party A Definition | Party B Definition | Proposed Precise Definition |
|------|-------------------|-------------------|---------------------------|
| "Prioritize" | Allocate >50% of discretionary resources | Focus primary strategic attention | Allocate ≥60% of discretionary resources AND make primary KPI |
| "User growth" | New user acquisition | Active user increase | Monthly Active Users (MAU) increase, measured as % change |
| "Profitability" | Positive net income | EBITDA positive | EBITDA margin ≥5% for the quarter |
| "Next quarter" | Q2 2026 | Q2 2026 | Q2 2026 (agreement exists) |

### Explicit Argument Reconstruction

**Party A's Argument (Prioritize Growth):**
```
P1: We are a venture-backed startup with 18 months of runway
P2: Our Series B valuation depends on demonstrating growth trajectory
P3: Profitable-but-slow companies get lower valuations than growing companies
P4: Without a strong Series B, we cannot achieve our mission
C: Therefore, we should prioritize user growth over profitability in Q2
```

**Party B's Argument (Prioritize Profitability):**
```
P1: We have 18 months of runway but macro conditions are uncertain
P2: Companies are getting funded at lower rates than 2021
P3: A company that is profitable, or near-profitable, has more negotiating leverage
P4: Revenue multiples have compressed; fundamentals matter more now
C: Therefore, we should prioritize profitability to reduce existential risk
```

### Hidden Assumptions Identified
- Party A assumes Series B funding environment will reward growth
- Party A assumes 18 months is sufficient to demonstrate growth AND then raise
- Party B assumes funding environment will remain difficult
- Party B assumes profitability signals will matter to investors
- Both assume the choice is binary (not a spectrum)

### Location of Disagreement

| Type | Finding |
|------|---------|
| Definitional | Minor - "prioritize" needed clarification but parties aligned |
| Factual | **PRIMARY** - Disagreement about future funding environment |
| Logical | Valid on both sides given respective premises |
| Evaluative | Some difference in risk tolerance |

### The Calculation
The dispute is primarily **factual**, not conceptual or evaluative. Both arguments are logically valid. The key factual questions:

1. What is the probability of successful Series B given growth-focused Q2?
2. What is the probability of successful Series B given profitability-focused Q2?
3. What is the probability of survival without Series B given each approach?

If we assign:
- P(successful raise | growth focus) = p_g
- P(successful raise | profit focus) = p_p
- P(survival without raise | growth focus) = s_g
- P(survival without raise | profit focus) = s_p

Expected survival = P(raise) + P(no raise) * P(survive anyway)

**For growth:** p_g + (1 - p_g) * s_g
**For profit:** p_p + (1 - p_p) * s_p

The "right" answer depends on these probability estimates.

### Resolution Path
1. **Gather evidence:** Research recent Series B outcomes for companies with different profiles
2. **Consult advisors:** Get investor perspective on what they're funding now
3. **Model scenarios:** Explicitly estimate the probabilities above
4. **Make the implicit explicit:** If parties still disagree after sharing probability estimates, they have a genuine disagreement about the world that may require waiting for more evidence

*Calculemus! The dispute is not about values but about predictions. Once we have shared probability estimates, the calculation can proceed.*

---

## Integration

This skill is part of the **Gottfried Wilhelm Leibniz** expert persona. Leibniz dreamed of a *characteristica universalis* and *calculus ratiocinator* that would reduce all disputes to calculation. While fully realized only in formal logic and mathematics, the aspiration - to make reasoning explicit and precise - applies broadly.

### Example 2: Remote Work Policy Debate

**Input:** "Our leadership team can't agree on whether remote work 'works.' The conversation goes nowhere."

**Output:**

## Calculemus Analysis

### The Dispute
"Does remote work 'work' for our organization?"

### Key Terms Requiring Definition

| Term | Party A Definition | Party B Definition | Proposed Precise Definition |
|------|-------------------|-------------------|---------------------------|
| "Remote work" | Any work from non-office location | Full-time work from home | ≥3 days/week from non-office location |
| "Works" | Employees are productive | Company achieves goals | Measurable against: (1) productivity metrics, (2) collaboration quality, (3) employee retention, (4) business outcomes |
| "Productivity" | Output volume | Output quality and volume | Output measured by [specific team metrics] |

### Explicit Argument Reconstruction

**Party A's Argument (Remote Works):**
```
P1: Employee surveys show high satisfaction with remote work
P2: Our KPIs have not declined since going remote
P3: We've retained talent who would have left for remote-friendly companies
P4: High satisfaction + stable KPIs + retention = it works
C: Therefore, remote work works for us
```

**Party B's Argument (Remote Doesn't Work):**
```
P1: Cross-team collaboration has declined (fewer spontaneous interactions)
P2: New employee onboarding is harder remotely
P3: Innovation metrics have declined since going remote
P4: We're measuring the wrong things; long-term effects are negative
C: Therefore, remote work doesn't work for us
```

### Hidden Assumptions Identified
- Party A assumes current KPIs capture what matters
- Party A assumes satisfaction correlates with performance
- Party B assumes spontaneous interaction drives innovation
- Party B assumes correlation (remote + decline) implies causation
- Both parties assume binary outcome (works/doesn't work)

### Location of Disagreement

| Type | Finding |
|------|---------|
| Definitional | **PRIMARY** - "Works" means different things (satisfaction/retention vs. innovation/collaboration) |
| Factual | Secondary - Disagreement about whether innovation actually declined |
| Logical | Minor - Both arguments are valid given premises |
| Evaluative | Present - Different weights on employee satisfaction vs. innovation |

### The Calculation

The dispute is primarily **definitional and evaluative**, not factual. Both parties could be correct within their own definition of "works."

**Resolution approach:**
1. Agree on definition: What metrics would we use to evaluate "works"?
2. Weight the metrics: How much do we value satisfaction vs. innovation?
3. Measure: What do the agreed metrics actually show?
4. Decide: Given data and weights, does remote work "work" by our shared definition?

### Resolution Path

1. **Define success criteria together:** List all outcomes that matter (productivity, satisfaction, retention, innovation, collaboration, onboarding)
2. **Assign weights:** Have leadership rank the relative importance of each
3. **Gather data:** Measure each outcome pre-remote and post-remote
4. **Calculate:** Apply weights to data; produce a single "works" score
5. **Decide:** If score is above threshold, remote "works" by the organization's own definition

*Calculemus! The dispute cannot be resolved until "works" is defined and weighted. Once that's done, the answer becomes calculable.*

**Why these examples work:** Both demonstrate that circular debates often stem from undefined terms or conflicting premises, not from irrationality. By making definitions explicit and locating disagreement precisely, previously intractable debates become tractable.