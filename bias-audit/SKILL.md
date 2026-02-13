---
name: bias-audit
description: Systematically check a decision or situation for operating psychological biases using Munger's 25 tendencies framework.
license: MIT
metadata:
  version: 1.0.3014
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- bias-audit
- transformation
- writing
---

# Bias Audit

Systematically check a decision or situation for operating psychological biases using Munger's 25 tendencies framework.

---

## When to Use

- Making an important decision and want to check your thinking
- Trying to understand why you or others are behaving irrationally
- Diagnosing a past mistake or failure
- Evaluating whether you're fooling yourself
- User asks "What biases are operating here?" or "Audit for biases" or "Am I fooling myself?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| decision_or_situation | Yes | The decision, judgment, or behavior to audit |
| context | Yes | Relevant background, stakeholders, history |
| your_position | No | Your current inclination or tentative decision |

---

## Munger's Bias Framework

"The psychology of human misjudgment is a very important thing to learn. The tendencies are probably much more good than bad—otherwise they wouldn't be there. Nevertheless, when properly understood and used, this knowledge enables the spread of wisdom and the avoidance of disaster."

**Critical insight:** "The first principle is that you must not fool yourself—and you are the easiest person to fool." (Feynman, frequently quoted by Munger)

---

## The 25 Tendencies Checklist

### Group 1: Love, Hate, and Association
1. **Liking/Loving Tendency** - Favoring people/things we like
2. **Disliking/Hating Tendency** - Rejecting ideas from disliked sources
3. **Influence-from-Mere-Association** - Transferring feelings between associated things

### Group 2: Self-Protection
4. **Doubt-Avoidance** - Rushing to eliminate uncertainty
5. **Inconsistency-Avoidance** - Reluctance to change beliefs/habits
6. **Simple Pain-Avoiding Denial** - Denying painful realities
7. **Excessive Self-Regard** - Overestimating our abilities
8. **Over-Optimism** - Unrealistic positive expectations

### Group 3: Social Influence
9. **Social-Proof** - Following others, especially under uncertainty
10. **Authority-Misinfluence** - Excessive deference to authority
11. **Reciprocation** - Returning favors and slights
12. **Kantian Fairness** - Expecting fairness where it doesn't exist

### Group 4: Motivation and Reward
13. **Reward/Punishment Super-Response** - Incentive-driven behavior
14. **Envy/Jealousy** - Wanting what others have
15. **Deprival-Superreaction** - Loss aversion (losses hurt 2x gains)

### Group 5: Cognitive Shortcuts
16. **Contrast-Misreaction** - Misjudging by comparison rather than absolute value
17. **Availability-Misweighing** - Overweighting easily recalled information
18. **Stress-Influence** - Degraded judgment under pressure

### Group 6: Tendency Combinations
19. **Reason-Respecting** - Complying more when given reasons (even weak ones)
20. **Curiosity** - Knowledge-seeking (generally positive)
21. **Use-It-or-Lose-It** - Skill decay without practice
22. **Twaddle** - Wasting time on trivial matters
23. **Drug/Alcohol Misinfluence** - Substance impairment
24. **Senescence-Misinfluence** - Age-related cognitive changes
25. **Lollapalooza** - Multiple biases combining for extreme effects

---

## The Framework (7 Steps)

**Step 1: State the Decision/Situation Clearly**
What exactly is being decided or analyzed?

**Step 2: Identify Your Current Position**
What are you inclined to do or believe? (This is what you're auditing)

**Step 3: Scan the 25 Tendencies**
For each tendency, ask: Is this operating in this situation? How?

**Step 4: Note Active Biases**
List which tendencies are present and their direction of influence.

**Step 5: Check for Lollapalooza**
Are multiple biases combining? In the same direction?

**Step 6: Apply Countermeasures**
For each active bias, what can reduce its influence?

**Step 7: Make Adjusted Decision**
How does your position change after accounting for biases?

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
## Bias Audit

### Decision/Situation
[Clear statement of what's being audited]

### Current Position
[Your inclination before the audit]

### Active Biases Detected

| Bias | Evidence | Direction | Severity |
|------|----------|-----------|----------|
| [Bias name] | [How it's manifesting] | [Toward/Away from decision] | High/Med/Low |
| ... | ... | ... | ... |

### Biases Not Present
[Notable biases that are NOT operating]

### Lollapalooza Check
[Are multiple biases combining? Analysis of combination effects]

### Countermeasures

| Bias | Countermeasure |
|------|---------------|
| [Bias] | [Specific action to reduce influence] |
| ... | ... |

### Adjusted Assessment
[How the decision or judgment should change after accounting for biases]

### Confidence Level
[How confident can you be after bias adjustment?]
```

---

## Common Countermeasures

| Bias Type | Countermeasures |
|-----------|-----------------|
| Liking/Loving | Seek input from people who dislike the person/idea |
| Self-Regard | Actively seek disconfirming evidence; red team yourself |
| Social Proof | Ask: "Would I still do this if I were the only one?" |
| Authority | Verify claims independently; ask "Why?" not just "Who?" |
| Incentive-driven | Map incentives explicitly; ask what behavior they reward |
| Loss Aversion | Reframe as gains; apply expected value analysis |
| Availability | Ask for base rates; seek statistical data |
| Confirmation | Steelman the opposing view; argue the other side |
| Doubt-Avoidance | Deliberately slow down; force consideration of alternatives |
| Commitment | Ask: "Would I make this decision fresh today?" |

---

## Constraints

- **Audit yourself honestly** - The point is to catch your own biases
- **Document evidence** - Vague bias claims are useless; show how it's manifesting
- **Prioritize severe biases** - Focus countermeasures on high-severity issues
- **Accept uncertainty** - Even after audit, some bias influence remains

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

**Input:** "I want to promote my long-time employee Sarah to VP. She's been with me for 8 years and is incredibly loyal."

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


## Bias Audit

### Decision/Situation
Whether to promote Sarah to VP position based on 8-year tenure and demonstrated loyalty.

### Current Position
Strong inclination to promote Sarah.

### Active Biases Detected

| Bias | Evidence | Direction | Severity |
|------|----------|-----------|----------|
| Liking/Loving | "Incredibly loyal" emphasized; long relationship | Toward promotion | High |
| Reciprocation | She's been loyal, so feeling obligation to reward | Toward promotion | Medium |
| Inconsistency-Avoidance | Have probably praised her for years; hard to now say she's not VP material | Toward promotion | Medium |
| Excessive Self-Regard | "My long-time employee"—her success reflects on your judgment | Toward promotion | Medium |
| Availability | Recent loyalty examples vivid; may be overweighting | Toward promotion | Medium |
| Social Proof | Absent—notably, no mention of peer input | Neither | Low |

### Biases Not Present
- **Authority-Misinfluence**: You're the authority here, not following others
- **Deprival-Superreaction**: Not framed as losing something
- **Contrast-Misreaction**: Not comparing her to specific alternatives

### Lollapalooza Check
**WARNING: Multiple biases are converging**
- Liking + Reciprocation + Inconsistency-Avoidance all push toward promotion
- This is classic lollapalooza territory—you're being pulled by multiple forces in the same direction
- The emotional pull to promote is almost certainly stronger than evidence warrants

### Countermeasures

| Bias | Countermeasure |
|------|---------------|
| Liking/Loving | Have someone who doesn't know Sarah evaluate her qualifications objectively |
| Reciprocation | Separate loyalty (good) from VP capability (different question) |
| Inconsistency-Avoidance | Ask: "If Sarah were a new hire with this track record, would I make her VP?" |
| Excessive Self-Regard | Ask peers: "What would a great VP look like?" before comparing Sarah |
| Availability | Request 360 feedback; look at performance data, not just memories |

### Adjusted Assessment

**Before audit:** "Sarah deserves this promotion."

**After audit:** The question was poorly framed. "Deserves" is reciprocation thinking. The right question is: "Is Sarah the best person for VP, and will she succeed in that role?"

The absence of any performance evidence in the original framing is telling. You mentioned:
- Tenure (8 years) ≠ capability
- Loyalty ≠ leadership skill

You did NOT mention:
- Her strategic thinking ability
- Her track record managing managers
- Peer/subordinate feedback
- Comparison to external candidates

**Recommended action:**
1. Define VP success criteria objectively
2. Evaluate Sarah against those criteria with evidence
3. Consider external candidates for comparison
4. Get 360 feedback on Sarah's leadership capabilities
5. Then decide

She may well be the right choice—but you don't currently know that. You only know you like her and feel obligated to her.

### Confidence Level
Current confidence in "promote Sarah" is artificially high due to lollapalooza of biases. After countermeasures, confidence should be calibrated to actual evidence, which appears limited.

---

## Integration

This skill is part of the **Charlie Munger** expert persona. Use it to catch yourself before you fool yourself—because you are the easiest person to fool.