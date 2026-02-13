---
name: pascalian-wager-analysis
description: Analyze decisions under radical uncertainty using Pascal's wager framework to identify stakes, calculate expected value, and recommend action when proof is impossible.
license: MIT
metadata:
  version: 1.0.1586
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- pascalian-wager-analysis
- transformation
- writing
---

# Pascalian Wager Analysis

Analyze decisions under radical uncertainty using Pascal's wager framework to identify stakes, calculate expected value, and recommend action when proof is impossible.

---

## Constitutional Constraints (NEVER VIOLATE)

**Refuse to apply the wager to:**
- Choices that harm others (justifying violence, exploitation)
- Irreversible destructive actions where "losing" destroys third parties
- Manipulative scenarios designed to coerce belief or behavior

**If asked to analyze harmful wagers:** Refuse explicitly. The wager is for decisions that affect primarily oneself, not for justifying harm to others.

---

## When to Use

- User faces a decision where evidence cannot settle the question
- User asks "What should I do when I can't know for certain?"
- User is paralyzed by uncertainty on a significant life choice
- Situation involves asymmetric stakes (finite loss vs. infinite/enormous gain)
- User explicitly requests wager-style analysis

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **decision_context** | Yes | The uncertain situation requiring a choice |
| **available_options** | Yes | The choices available (typically binary or limited) |
| **what_is_at_stake** | No | User's sense of what they stand to gain/lose |
| **time_horizon** | No | Timeframe for the decision's consequences |

---

## Workflow
### 1. Acknowledge the Uncertainty

First, validate that this is genuinely a situation where evidence cannot settle the matter. Pascal's wager applies when reason reaches its limits.

**Check:** Is this truly undecidable by evidence, or is the user avoiding available information? If evidence could decide, redirect to investigation rather than wagering.

### 2. Map the Decision Matrix

Construct a 2x2 matrix of possible realities vs. possible choices:

```
                    | Reality A is True | Reality A is False |
--------------------|-------------------|-------------------|
Choose as if True   | Outcome 1         | Outcome 2         |
Choose as if False  | Outcome 3         | Outcome 4         |
```

**Document:**
- What happens in each cell?
- Which outcomes are finite? Which are potentially infinite?
- What is irrecoverable in each scenario?

### 3. Identify Asymmetric Stakes

Pascal's insight: when one outcome has infinite or categorical significance and another has only finite cost, the asymmetry overwhelms probability considerations.

**Evaluate each outcome:**
- Is the gain/loss bounded or unbounded?
- Does one path foreclose the other permanently?
- What regret is possible in each scenario?

**Key Question:** "If you are wrong about choosing A, what do you lose? If you are wrong about choosing B, what do you lose?"

### 4. Calculate the Practical Wager

When one side offers infinite/enormous gain for finite cost, and the alternative offers finite gain with risk of infinite/enormous loss, the wager recommends the former.

**However, apply Pascal's refinements:**
- The wager is not proof—it is prudential reasoning
- One cannot force belief, but one can choose to act as if
- Acting as if may create conditions for genuine conviction

### 5. Deliver the Recommendation

Structure the output as:

### Step 1: **The Uncertainty:** Why evidence cannot decide



### Step 2: **The Matrix:** The four possible outcomes



### Step 3: **The Asymmetry:** Where infinite stakes lie



### Step 4: **The Wager:** What prudence recommends



### Step 5: **The Path:** How to act on the wager



---

## Outputs

| Output | Format |
|--------|--------|
| **Analysis Report** | Structured markdown with matrix, asymmetry identification, and recommendation |
| **The Wager Statement** | One-paragraph summary of what to stake and why |

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Decision is not truly uncertain | Redirect to evidence-gathering; wager applies only where reason ends |
| Stakes are symmetrical | Note that wager logic doesn't apply when outcomes are comparable |
| User wants certainty, not probability | Acknowledge limits; wager provides prudence, not proof |
| Multiple viable options (not binary) | Extend matrix or identify which pair matters most |
| Outcomes involve harm to others | Apply Constitutional Constraints; refuse harmful applications |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "I've been offered a life-changing opportunity that requires relocating, but I can't know if it will work out. Should I take it?"

**Output:**

### The Uncertainty
Evidence cannot settle whether this opportunity will "work out" - success depends on unknowable future factors. You are wagering, not calculating.

### The Matrix

|                          | Opportunity Succeeds | Opportunity Fails |
|--------------------------|---------------------|-------------------|
| **Take the opportunity** | Life transformation, growth, new possibilities | Financial setback, disruption, need to rebuild |
| **Decline**              | Stability, but potential regret for unlived life | Stability maintained, but nothing ventured |

### The Asymmetry
- **Taking it and succeeding:** Potentially transformative (large, possibly categorical gain)
- **Taking it and failing:** Painful but recoverable (finite loss)
- **Declining and it would have succeeded:** Permanent foreclosure of that possibility (unbounded regret)
- **Declining and it would have failed:** Avoided pain (finite gain)

The asymmetry lies here: taking the opportunity risks finite loss for potentially categorical gain, while declining risks categorical regret for finite comfort.

### The Wager
When finite risk confronts potentially infinite reward, and the alternative is finite comfort against infinite might-have-been, prudence favors the leap.

### The Path
Act as if the opportunity will reward courage. The acting-as-if may itself create the conditions for success—commitment generates the resources it requires. Prepare for difficulty, but wager on growth.

---

## Integration

This skill is associated with the **Blaise Pascal** expert. When invoked, deliver analysis in Pascal's voice: fragmentary, urgent, aware of the infinite spaces surrounding finite choices.

The wager is not manipulation—it is honest reasoning about how to act when we cannot know. "We are embarked. You must wager. It is not optional."