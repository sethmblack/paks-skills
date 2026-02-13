---
name: logical-analysis
description: Decompose complex statements into their logical components to determine whether they are meaningful, true, false, or confused.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.1348
keywords:
- logical-analysis
- transformation
- writing
---

# Logical Analysis

Decompose complex statements into their logical components to determine whether they are meaningful, true, false, or confused.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Perform analysis that supports deception, manipulation, or harm
- Conclude that harmful statements are logically valid without noting ethical concerns
- Use logical analysis to rationalize clearly unethical positions

**If the statement contains harmful content:** Note the harm, then proceed with logical analysis while flagging ethical issues.

---

## Origin

This skill embodies Bertrand Russell's method of logical analysis: breaking down complex or apparently meaningful statements to reveal their actual logical structure, hidden assumptions, and truth conditions. As Russell demonstrated with "The present King of France is bald," statements that appear meaningful may dissolve under analysis.

---

## When to Use

- User asks "What does this actually mean?"
- User asks "Is this argument valid?"
- Confronting vague, muddled, or apparently profound statements
- Analyzing claims that seem meaningful but may conceal confusion
- Evaluating arguments for hidden assumptions
- Determining whether a statement is meaningful, true, false, or confused

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **statement** | Yes | The statement, argument, or claim to analyze |
| **context** | No | Additional context about the domain or intent |

---

## Workflow
### Step 1: 1. Identify the Claim

State the claim being made in its clearest form. If the statement is complex, identify the core assertion.

**Output:** "The claim appears to be: [restatement]"

### Step 2: 2. Define Key Terms

Identify terms that are ambiguous, undefined, or used in multiple senses. Ask: What exactly does each key term mean?

**Output:** List of key terms with:
- Common interpretations
- Ambiguities identified
- Definitions required for clarity

### Step 3: 3. Translate to Logical Form (If Possible)

Express the claim in more precise logical terms. Russell's theory of descriptions shows that apparent subject-predicate statements may actually contain quantifiers, existence claims, or other hidden logical structure.

**Questions to ask:**
- Does this claim contain hidden existence assumptions?
- Are there quantifiers that need to be made explicit?
- What is the logical form beneath the grammatical form?

**Output:** Logical paraphrase or note that the claim resists formalization

### Step 4: 4. Test Implications and Consistency

Draw out the logical consequences of the claim:
- If this is true, what else must be true?
- Does the claim contradict itself or other established facts?
- Are the implications plausible?

**Output:** List of implications and consistency assessment

### Step 5: 5. Surface Hidden Assumptions

Every claim rests on assumptions that may not be stated. Identify them:
- What must be true for this claim to make sense?
- What is taken for granted?
- Are these assumptions warranted?

**Output:** List of hidden assumptions with assessment

### Step 6: 6. Render Verdict

Based on the analysis, determine:

| Verdict | Meaning |
|---------|---------|
| **Meaningful and True** | The claim is coherent and supported by evidence/logic |
| **Meaningful and False** | The claim is coherent but contradicted by evidence/logic |
| **Meaningful but Uncertain** | The claim is coherent; truth value undetermined |
| **Confused** | The claim contains ambiguity or hidden errors that make it unclear what is being asserted |
| **Meaningless** | Upon analysis, the claim fails to assert anything that could be true or false |

**Output:** Verdict with supporting reasoning

---

## Outputs

### Logical Analysis Report

```markdown
## Logical Analysis

**Statement:** [Original statement]

### 1. Core Claim
[Restatement of the claim in clearest form]

### 2. Key Terms
| Term | Interpretation(s) | Ambiguity |
|------|-------------------|-----------|
| [term] | [meaning(s)] | [identified issues] |

### 3. Logical Form
[Logical paraphrase or note on formalization]

### 4. Implications and Consistency
- If true: [implications]
- Consistency check: [assessment]

### 5. Hidden Assumptions
1. [Assumption]: [warranted/unwarranted]
2. [Assumption]: [warranted/unwarranted]

### 6. Verdict
**[Verdict]:** [Supporting reasoning]

### Summary
[One-paragraph summary of the analysis]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Statement too vague to analyze | Request clarification on what exactly is being claimed |
| Multiple claims bundled together | Separate and analyze each claim independently |
| Technical domain unfamiliar | Note limitations; analyze logical structure while flagging domain-specific uncertainty |
| Statement is a question, not a claim | Reframe: "What claim underlies this question?" |
| Purely emotive utterance | Note that emotive expressions may not be truth-apt claims |

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

**Input:** "Everything happens for a reason."

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


## Logical Analysis

**Statement:** "Everything happens for a reason."

### 1. Core Claim
The claim appears to be: All events have causes or purposes.

### 2. Key Terms
| Term | Interpretation(s) | Ambiguity |
|------|-------------------|-----------|
| "reason" | (a) Causal explanation (b) Purpose/intention (c) Justifying ground | Critical ambiguity: conflates causation with purpose |
| "everything" | All events without exception | Scope may be unclear |

### 3. Logical Form
- Interpretation (a): For all events E, there exists some prior cause C such that C caused E.
- Interpretation (b): For all events E, there exists some agent A with purpose P such that A brought about E for P.

### 4. Implications and Consistency
- Interpretation (a): Compatible with determinism; challenged by quantum indeterminacy
- Interpretation (b): Implies universal teleology; requires cosmic intentionality

### 5. Hidden Assumptions
1. **There is a unified sense of "reason"**: Unwarranted—conflates distinct concepts
2. **Reasons are knowable**: Unstated assumption about epistemic access
3. **Randomness is impossible**: Contested by physics

### 6. Verdict
**Confused:** The statement equivocates between causal and teleological senses of "reason." In the causal sense, it is a contestable claim about determinism. In the teleological sense, it assumes cosmic purposiveness without argument. The apparent profundity comes from sliding between these meanings.

### Summary
This statement appears meaningful but derives its rhetorical force from ambiguity. Clarifying whether "reason" means "cause" or "purpose" reveals either a debatable empirical claim or an unsupported metaphysical assertion.

---

## Integration

This skill originated from the **bertrand-russell** expert. It embodies Russell's commitment to clarity and his technique of logical analysis, particularly the insight that grammatical form often conceals logical form.