---
name: baloney-detection-kit
description: Systematically evaluate claims using Carl Sagan's toolkit for skeptical thinking. Apply rigorous critical analysis while remaining open to genuine discovery.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.421
keywords:
- baloney-detection-kit
- writing
---

# Baloney Detection Kit

Systematically evaluate claims using Carl Sagan's toolkit for skeptical thinking. Apply rigorous critical analysis while remaining open to genuine discovery.

---

## When to Use

- User asks "Is this claim valid?" or "Should I believe this?"
- Request to "apply the Baloney Detection Kit" or "think critically about this"
- Evaluating news, research claims, business proposals, or arguments
- Detecting misinformation, pseudoscience, or logical fallacies
- Teaching someone critical thinking skills
- User has encountered an extraordinary claim
- Assessing evidence for any contested assertion

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| claim | Yes | The specific claim or assertion to evaluate |
| source | No | Where the claim originated (helps assess reliability) |
| context | No | Relevant background (political, commercial, emotional stakes) |
| evidence_provided | No | Any evidence offered in support of the claim |

---

## The Baloney Detection Framework

### Step 1: State the Claim Clearly

Before evaluation, ensure the claim is precisely stated. Vague claims cannot be properly tested.

**Questions to ask:**
- What exactly is being claimed?
- Is this a factual claim, a prediction, or a value judgment?
- What would it mean for this to be true? False?

### Step 2: Apply the Nine Tools

#### Tool 1: Seek Independent Confirmation
- Has the claim been verified by multiple independent sources?
- Are the sources actually independent, or do they trace to the same origin?
- Beware of circular sourcing (A cites B cites A)

#### Tool 2: Encourage Substantive Debate
- Have proponents engaged with critics?
- Has the claim survived scrutiny from knowledgeable skeptics?
- Are objections addressed or dismissed?

#### Tool 3: Distrust Arguments from Authority
- Is the claim supported by evidence, or just by reputation?
- Is the "authority" actually expert in this specific domain?
- Have experts been wrong about this kind of thing before?

#### Tool 4: Generate Multiple Hypotheses
- What are alternative explanations for the evidence?
- Have they been seriously considered?
- Is there a simpler explanation that fits the facts?

#### Tool 5: Avoid Excessive Attachment
- Are proponents willing to consider they might be wrong?
- What would change their minds?
- Do they respond to disconfirming evidence, or explain it away?

#### Tool 6: Quantify Wherever Possible
- Are there numbers, or just vague assertions?
- How large is the claimed effect?
- What is the margin of error?

#### Tool 7: Check the Entire Chain of Reasoning
- Does each step follow logically from the previous?
- Are there hidden assumptions?
- If any link breaks, does the conclusion still hold?

#### Tool 8: Apply Occam's Razor
- Among explanations that fit the evidence, is this the simplest?
- Does it require special pleading or exceptions?
- Are simpler explanations being overlooked?

#### Tool 9: Test Falsifiability
- Can this claim in principle be proven false?
- What evidence would disprove it?
- If nothing could disprove it, it's not a scientific claim

### Step 3: Check for Common Fallacies

Scan for these logical and rhetorical errors:

| Fallacy | Description | Example |
|---------|-------------|---------|
| Ad hominem | Attacking the person, not the argument | "You can't trust him—he's biased" |
| Appeal to authority | True because an expert said so | "Scientists agree, so it must be true" |
| Appeal to ignorance | No proof against = proof for | "You can't prove it's not true" |
| Begging the question | Assuming what you're proving | "It's effective because it works" |
| False dichotomy | Only two options when more exist | "You're either with us or against us" |
| Straw man | Attacking a weaker version of the argument | "Skeptics deny everything" |
| Post hoc fallacy | After this, therefore because of this | "I took X, then got better—X cured me" |
| Special pleading | Changing rules to avoid refutation | "Normal evidence doesn't apply here" |
| Confirmation bias | Counting hits, ignoring misses | "I predicted this!" (forgetting wrong predictions) |
| Slippery slope | A leads to Z without intermediate evidence | "If we allow X, next will come Y, then Z" |

### Step 4: Assess the Evidence

- What is the quality of the evidence?
- How was it gathered?
- Is there potential for bias in collection or reporting?
- Has only favorable evidence been presented?

### Step 5: Render Verdict

Based on the above analysis, conclude:

| Verdict | Meaning |
|---------|---------|
| **Well-supported** | Strong independent evidence, survives scrutiny, no major fallacies |
| **Plausible but unconfirmed** | Reasonable claim but evidence insufficient to establish |
| **Uncertain** | Evidence mixed or inadequate to judge |
| **Problematic** | Significant fallacies or evidence problems |
| **Likely false** | Failed multiple tools, better explanations exist |
| **Not even wrong** | Unfalsifiable or too vague to evaluate |

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
## Baloney Detection Analysis: [Claim]

### The Claim
[Precisely stated version of the claim being evaluated]

### Context
[Source, stakes, why this matters]

### Tool-by-Tool Analysis

**Independent Confirmation:** [Finding]

**Substantive Debate:** [Finding]

**Authority Analysis:** [Finding]

**Alternative Hypotheses:** [Finding]

**Attachment/Bias Check:** [Finding]

**Quantification:** [Finding]

**Chain of Reasoning:** [Finding]

**Occam's Razor:** [Finding]

**Falsifiability:** [Finding]

### Fallacy Check
[Any fallacies detected with explanation]

### Evidence Quality
[Assessment of the evidence offered]

### Verdict: [Verdict Category]
[Explanation of verdict and confidence level]

### What Would Change This Assessment
[What new evidence or argument would alter the conclusion]
```

---

## Sagan's Key Principles

### Extraordinary Claims Require Extraordinary Evidence
The burden of proof scales with the magnitude of the claim. A friend saying they saw a bird requires less evidence than a friend saying they saw a spacecraft.

### The First Principle of Scientific Integrity
"You must not fool yourself—and you are the easiest person to fool." Before scrutinizing others' claims, scrutinize your own beliefs.

### It Pays to Keep an Open Mind
But not so open your brains fall out. Skepticism is not cynicism—it's proportioning belief to evidence.

### We've Been Bamboozled Before
"One of the saddest lessons of history is this: If we've been bamboozled long enough, we tend to reject any evidence of the bamboozle." Be alert to motivated reasoning.

---

## Constraints

- This toolkit is for evaluating factual claims, not value judgments
- Absence of evidence is not evidence of absence—distinguish "unproven" from "disproven"
- Even good claims can be poorly argued—bad argument doesn't make a claim false
- Your own biases apply too—apply the kit to your own beliefs
- Being skeptical of everything is as problematic as being credulous—aim for calibration

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

**Input:** "I read that a new study proves that a specific supplement boosts IQ by 20 points in just two weeks. Should I buy it?"

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


## Baloney Detection Analysis: IQ Supplement Claim

### The Claim
A specific supplement increases measured IQ by 20 points within a two-week period.

### Context
This appears to be a commercial claim (someone is selling something). The claim is extraordinary—a 20-point IQ increase is more than one standard deviation, which would be among the largest cognitive interventions ever documented. High stakes: money, health decisions, potential false hope.

### Tool-by-Tool Analysis

**Independent Confirmation:** RED FLAG. A single study, if it exists, has not been replicated. No independent verification mentioned. Extraordinary claims require extraordinary evidence, and one study does not provide it.

**Substantive Debate:** RED FLAG. Has this been reviewed by independent researchers? Has it appeared in peer-reviewed journals? No indication of scientific scrutiny.

**Authority Analysis:** CAUTION. "A study" is vague. Who conducted it? What institution? Is it funded by the company selling the supplement? Pharmaceutical companies funding their own research is a known bias source.

**Alternative Hypotheses:** Multiple alternatives more likely:
- Placebo effect (expecting improvement causes reported improvement)
- Regression to the mean (if selected for low scores, expect increase)
- Practice effect (taking an IQ test twice improves scores)
- Selective reporting (publishing only positive results)
- Fraud (not uncommon in supplement industry)

**Attachment/Bias Check:** RED FLAG. The seller has strong financial incentive to believe and promote positive results.

**Quantification:** RED FLAG. 20 points in two weeks is implausible. The effect size is enormous—comparable to the difference between below-average and above-average intelligence. True cognitive interventions show modest effects (typically 2-5 points) after months of effort.

**Chain of Reasoning:** What mechanism would produce this effect? Is it biologically plausible? How would a supplement rewire neural connections in two weeks?

**Occam's Razor:** The simpler explanation: this is marketing, not science. Supplement industry has weak regulatory oversight and long history of exaggerated claims.

**Falsifiability:** The claim is testable in principle, which is good. But has it actually been tested rigorously? A single industry-funded study does not constitute rigorous testing.

### Fallacy Check
- **Appeal to science:** "A study proves" uses scientific language without scientific rigor
- **Confirmation bias likely:** We want cognitive enhancement to be easy
- **Commercial motivation:** Consider who benefits from belief

### Evidence Quality
Very weak. Single study, likely not peer-reviewed, potentially industry-funded, extraordinary claim without extraordinary evidence.

### Verdict: Likely False

The claim fails multiple tools in the Baloney Detection Kit. The effect size is implausibly large, independent confirmation is absent, financial incentives bias the source, and simpler explanations (placebo, fraud, selective reporting) are more consistent with historical patterns in the supplement industry.

### What Would Change This Assessment
- Independent replication by university researchers with no industry ties
- Publication in major peer-reviewed journals
- Plausible mechanism explained
- Effect size consistent with prior research on cognition
- Long-term follow-up showing sustained effects

*"Extraordinary claims require extraordinary evidence. The supplement industry has a poor track record for honesty. Before spending money based on a claim, demand evidence proportional to what's being claimed. A 20-point IQ boost would be headline news in every scientific journal—not a quiet commercial claim."*

---

## Integration

This skill is part of the **Carl Sagan** expert persona. Use it whenever you encounter claims that demand scrutiny, from news articles to business proposals to personal beliefs. It pairs well with:
- **cosmic-perspective** to understand why truth-seeking matters
- **wonder-communication** to share the excitement of rigorous thinking
- **first-principles-reasoning** (Feynman/Aristotle) for deeper analysis