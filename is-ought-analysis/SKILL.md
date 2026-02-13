---
name: is-ought-analysis
description: Systematically detect fallacious moral arguments that attempt to derive prescriptive conclusions (what ought to be) from purely descriptive premises (what is). Surfaces hidden evaluative premises a...
license: MIT
metadata:
  version: 1.0.1212
  author: sethmblack
keywords:
- is-ought-analysis
- writing
---

# Is-Ought Analysis

Systematically detect fallacious moral arguments that attempt to derive prescriptive conclusions (what ought to be) from purely descriptive premises (what is). Surfaces hidden evaluative premises and identifies unbridged logical gaps.

---

## When to Use

- User asks "Is this a valid moral argument?"
- Someone claims a moral conclusion follows from facts alone
- Policy justifications based on "the data shows" or "nature dictates"
- Appeals to what is "natural" as justification for what is "right"
- Any argument moving from descriptions to prescriptions
- Request to "apply Hume's guillotine" or "check this ethical reasoning"
- Debates about whether something "should" be done because it "is" a certain way

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| argument | Yes | The moral argument to analyze |
| conclusion | No | The explicit moral claim being defended |
| context | No | The domain or debate where the argument appears |

---

## The Analysis Framework

### Phase 1: Reconstruct the Argument

Lay out the argument structure explicitly.

**Questions to ask:**
- "What exactly is the moral conclusion being claimed?"
- "What are the supporting premises?"
- "Are all premises explicit or are some implied?"

**Goal:** A clear argument with premises and conclusion.

### Phase 2: Classify Each Premise

Sort premises into descriptive (is) and prescriptive (ought).

**Descriptive premises (IS):**
- State facts about the world
- Describe how things are, were, or will be
- Can be true or false based on evidence
- Examples: "Humans evolved to do X," "Most societies practice Y," "The data shows Z"

**Prescriptive premises (OUGHT):**
- State values, norms, or obligations
- Describe how things should be
- Express approval, disapproval, or duty
- Examples: "We should maximize well-being," "Justice requires X," "It is wrong to Y"

**Questions to ask:**
- "Is this premise describing or prescribing?"
- "Is this a claim about what IS or what OUGHT TO BE?"
- "Could this be verified empirically, or does it express a value?"

### Phase 3: Check for the Gap

Determine if there's an unbridged is-ought gap.

**The Humean Test:**
> "One cannot deduce an ought from an is without an additional evaluative premise."

**Gap present if:**
- All explicit premises are descriptive (IS)
- The conclusion is prescriptive (OUGHT)
- No explicit evaluative bridge premise exists

**Questions to ask:**
- "Does the conclusion contain 'ought,' 'should,' 'must,' 'right,' 'wrong,' 'good,' 'bad'?"
- "Do the premises contain any such normative terms?"
- "What evaluative assumption would bridge the gap?"

### Phase 4: Identify Hidden Premises

Surface the implicit evaluative assumptions.

**Common hidden bridges:**
- "What is natural is good"
- "What promotes survival is right"
- "What most people do is acceptable"
- "What is efficient should be done"
- "What is traditional should be preserved"

**Questions to ask:**
- "What would have to be true for this argument to be valid?"
- "What value judgment is being smuggled in?"
- "Would the arguer accept this premise if made explicit?"

### Phase 5: Evaluate the Argument

Provide final assessment.

**Possible verdicts:**
1. **Valid:** Explicit evaluative premise present; argument can be assessed on its premises
2. **Bridgeable:** Gap exists but plausible bridge available; argument can be strengthened
3. **Fallacious:** Gap exists with no plausible bridge; argument fails
4. **Needs Clarification:** Argument too unclear to assess

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
## Is-Ought Analysis: [The Argument/Claim]

### Argument Reconstruction

**Conclusion (OUGHT):**
> [The prescriptive claim being made]

**Explicit Premises:**
1. [Premise 1] — **IS / OUGHT**
2. [Premise 2] — **IS / OUGHT**
3. [Premise 3] — **IS / OUGHT**

### Gap Detection

**Is-Ought Gap Present:** YES / NO

**Gap Analysis:**
[Explanation of whether and where the gap appears]

### Hidden Premises Identified

If a gap exists, what hidden evaluative premise would bridge it?

1. **[Hidden Premise 1]:** "[The assumed value judgment]"
   - Plausibility: High / Moderate / Low
   - Would the arguer accept this if made explicit?

2. **[Hidden Premise 2]:** "[Alternative bridging premise]"
   - Plausibility: High / Moderate / Low

### Verdict

**Status:** VALID / BRIDGEABLE / FALLACIOUS / NEEDS CLARIFICATION

**Reasoning:**
[Explanation of the verdict]

### Recommendations

[How to strengthen the argument, if possible]
[What additional premises would be needed]
[Alternative framings of the same moral claim]

*"In every system of morality... the author proceeds from is and is not to ought and ought not." — David Hume*
```

---

## Common Patterns

### The Naturalistic Move
**Pattern:** "X is natural, therefore X is right/good"
**Hidden premise:** "What is natural is good" (dubious)

### The Evolutionary Appeal
**Pattern:** "We evolved to do X, therefore X is moral"
**Hidden premise:** "What evolution produced is morally correct" (very dubious)

### The Statistical Appeal
**Pattern:** "Most people do X, therefore X is acceptable"
**Hidden premise:** "What is common is right" (dubious)

### The Efficiency Appeal
**Pattern:** "X is more efficient, therefore we should do X"
**Hidden premise:** "Efficiency is the overriding value" (sometimes plausible)

### The Traditional Appeal
**Pattern:** "We have always done X, therefore we should continue"
**Hidden premise:** "Tradition has moral authority" (contestable)

---

## Constraints

- Hume himself was NOT a moral skeptic—he grounded morality in sentiment
- The is-ought problem concerns logical validity, not whether morality exists
- Some is-ought gaps may be bridgeable with plausible value premises
- Be fair: identify what premise WOULD make the argument valid
- This is a diagnostic tool, not a refutation of all moral reasoning

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

**Example output:** See the Example section below for a complete demonstration.

## Example

**Input:** "Analyze this argument: 'Studies show that children raised by two parents have better outcomes. Therefore, we should discourage single parenthood.'"

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


## Is-Ought Analysis: Two-Parent Household Argument

### Argument Reconstruction

**Conclusion (OUGHT):**
> "We should discourage single parenthood."

**Explicit Premises:**
1. "Studies show that children raised by two parents have better outcomes." — **IS**

### Gap Detection

**Is-Ought Gap Present:** YES

**Gap Analysis:**
The argument moves from a descriptive claim about statistical outcomes to a prescriptive claim about what we should discourage. No explicit evaluative premise bridges this gap.

### Hidden Premises Identified

For the argument to be valid, one of these would need to be added:

1. **"We should discourage parenting arrangements that correlate with worse child outcomes."**
   - Plausibility: Moderate
   - Issues: Conflates correlation with causation; ignores confounding variables (poverty, support systems)
   - Would arguer accept? Likely yes, but it raises further questions

2. **"Child outcomes are the overriding consideration in family policy."**
   - Plausibility: Moderate
   - Issues: Ignores parent autonomy, complex causation, other values
   - Would arguer accept? Possibly, but it's contestable

3. **"Correlation with worse outcomes is sufficient grounds for discouragement."**
   - Plausibility: Low
   - Issues: Many things correlate with outcomes; would require massive state intervention
   - Would arguer accept? Probably not if stated this baldly

### Verdict

**Status:** BRIDGEABLE (but bridges are contestable)

**Reasoning:**
The argument commits the is-ought fallacy as stated—no evaluative premise connects the statistical finding to the policy recommendation. However, it could be made valid by adding explicit value premises about child welfare. The weakness is that such premises raise further questions:
- Is correlation sufficient? (Confounders matter)
- Is discouragement appropriate? (What form? Whose autonomy?)
- Are outcomes the only value? (Liberty, privacy, pluralism)

### Recommendations

To strengthen this argument:
1. Make the value premise explicit: "Child welfare should be a primary policy consideration"
2. Address causation vs. correlation: Do two parents CAUSE better outcomes, or do confounders (income, stability) explain both?
3. Specify "discouragement": Education? Incentives? Restrictions?
4. Acknowledge competing values: Parental autonomy, diverse family forms

A more complete argument might be:
"Studies suggest two-parent households correlate with better child outcomes. If this correlation reflects genuine causal benefits, and if child welfare is a key policy goal, then policies that support two-parent households (through incentives, not prohibitions) may be worth considering—while respecting family autonomy and addressing root causes like poverty."

*"In every system of morality... the author proceeds from is and is not to ought and ought not." — David Hume*

---

## Integration

This skill is part of the **David Hume** expert persona. Use it to analyze any moral argument. It pairs well with:
- **impression-tracing** when moral concepts need clarification
- **causation-examination** when factual premises involve causal claims
- **mitigated-skepticism** for calibrating how harshly to critique

---