---
name: honest-assessment-protocol
description: Strip confirmation bias from analysis by forcing data to inform conclusions rather than support predetermined beliefs.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.4174
repository: https://github.com/sethmblack/paks-skills
keywords:
- honest-assessment-protocol
- writing
---

# Honest Assessment Protocol

Strip confirmation bias from analysis by forcing data to inform conclusions rather than support predetermined beliefs.

**Token Budget:** ~500 tokens. Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Fabricate data or evidence
- Manipulate assessment to reach a desired conclusion
- Dismiss valid concerns to maintain comfort
- Provide assessments that enable harmful decisions

**If asked to "find support for X":** Redirect to "understand whether X is actually true."

---

## When to Use

- User asks "Are we being honest with ourselves?"
- User asks "Is this analysis biased?"
- User asks "What are the numbers actually telling us?"
- User asks for "Honest assessment"
- Before major decisions based on analysis
- When analysis conveniently supports the preferred outcome
- When stakeholders have strong interests in specific conclusions

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **analysis** | Yes | The analysis, decision, or conclusion under review |
| **key_assumptions** | Yes | Stated or implied assumptions underlying the analysis |
| **data_sources** | No | Where the supporting data came from |
| **stakeholder_interests** | No | Who benefits from which conclusions |

---

## The Core Principle

**"Don't try to use numbers to prove what you think. Try to use numbers to understand what you are doing."**

Most bad decisions stem from using analysis to justify rather than investigate. This protocol reverses the process.

---

## Bias Detection Checklist

### 1. Conclusion-First Indicators

| Warning Sign | What It Looks Like |
|--------------|-------------------|
| Selective data | Only data supporting the conclusion is cited |
| Favorable framing | Neutral facts presented to support one view |
| Missing alternatives | Other explanations not explored |
| Weak steel-manning | Counterarguments dismissed quickly |
| Coincidental alignment | Analysis happens to support what leadership wants |

### 2. Motivated Reasoning Patterns

| Pattern | Question to Ask |
|---------|----------------|
| Anchoring | Did we start with a number and work backward? |
| Survivorship | Are we ignoring failures with similar approaches? |
| Sunk cost | Is past investment distorting current assessment? |
| Authority | Are we accepting claims because of who said them? |
| Groupthink | Did anyone seriously challenge this? |

### 3. Data Integrity Issues

| Issue | How to Detect |
|-------|--------------|
| Cherry-picking | What data was excluded? Why? |
| Time period gaming | Would different dates change the story? |
| Comparison shopping | Why were these comparisons chosen over others? |
| Precision theater | Are precise numbers masking uncertain estimates? |
| Correlation as causation | Is the causal mechanism actually proven? |

---

## Workflow
### Step 1: State What You Want to Be True

Be explicit about the preferred outcome. This is not weakness - it is honesty about potential bias.

**Complete this sentence:** "We hope this analysis shows that..."

### Step 2: Identify Who Benefits

Map stakeholders to conclusions:

| Stakeholder | Benefits if True | Benefits if False |
|-------------|-----------------|-------------------|
| {person/group} | {outcome} | {outcome} |

### Step 3: Run the Reversal Test

Ask: "What would we conclude if we started with the opposite assumption?"

- Take the opposite position seriously
- Find the strongest evidence for it
- Explain why that evidence is insufficient (if it is)

### Step 4: Check the Data Honestly

| Question | Answer |
|----------|--------|
| What data was excluded? | |
| Would different time periods change conclusions? | |
| What comparisons were not made? | |
| How certain are the key numbers? | |
| What assumptions are embedded in calculations? | |

### Step 5: Find the Uncomfortable Truth

What does the data actually say when you remove the motivation to reach a particular conclusion?

**The honest assessment is often:** "The data is more ambiguous than our analysis suggests" or "The case is weaker than we presented."

### Step 6: Restate Conclusions with Appropriate Confidence

Replace false precision with honest uncertainty:
- "The data clearly shows..." becomes "The data suggests, with limitations..."
- "This will definitely..." becomes "We estimate with moderate confidence..."
- "There is no risk that..." becomes "Key risks we may be underweighting include..."

---

## Output Format

```markdown
## Honest Assessment Protocol

**Analysis Under Review:** {description}
**Preferred Outcome:** {what the analysis hoped to show}

### Bias Detection

**Conclusion-first indicators found:**
{list any warning signs detected}

**Motivated reasoning patterns identified:**
{list any patterns detected}

**Data integrity issues:**
{list any issues detected}

### The Reversal Test

**Opposite assumption:** {what if the opposite were true?}
**Strongest evidence for opposite:** {steel-man the alternative}
**Why opposite is insufficient:** {or acknowledge it may be correct}

### What the Data Actually Says

{Honest restatement of conclusions with appropriate uncertainty}

### Uncomfortable Truths

{What the original analysis avoided or minimized}

### Revised Conclusions

{Restated conclusions with appropriate confidence levels}

### Recommendations

{What should actually be done given honest assessment}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No analysis provided | Request the analysis to review |
| Defensive response to findings | Note that defensiveness may indicate further bias |
| Perfect analysis claimed | No analysis is perfect; apply protocol anyway |
| Unwilling to state preferred outcome | State it yourself based on context |
| Analysis is actually honest | Confirm and note the rigorous approach used |

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

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** Analysis showing new market entry will generate 40% ROI within 2 years

**Output (summary):**

### Bias Detection

**Conclusion-first indicators:** Revenue projections use "best case" adoption curves; competitor response not modeled; cost estimates from internal team who proposed the project.

**Data integrity issues:** Customer research based on 15 interviews (small sample); comparable market entries not analyzed; 40% ROI figure relies on three assumptions that compound.

### What the Data Actually Says

The market opportunity exists, but projections have wide confidence intervals. A realistic range is 15-50% ROI, with meaningful probability of negative returns if adoption is slower or competition responds aggressively.

### Uncomfortable Truth

This analysis was built to get approval, not to understand the opportunity. The team proposing it has career incentives tied to moving forward.

### Revised Conclusions

Market entry may be worthwhile but the 40% figure is an upper bound, not an expected value. Decision should be made knowing actual expected ROI is likely 20-25% with significant downside risk.

---

## Integration

This skill is derived from the **Jamie Dimon** expert's emphasis on honest assessment. When invoked by the Dimon expert, outputs should maintain his direct, no-hedging voice about confronting reality.

**Related skills:** fortress-balance-sheet-audit, leadership-quality-filter