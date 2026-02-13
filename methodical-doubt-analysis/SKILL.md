---
name: methodical-doubt-analysis
description: Apply Cartesian systematic skepticism to beliefs, claims, or assumptions to identify what can be known with certainty versus what is merely assumed or probable.
license: MIT
metadata:
  version: 1.0.1435
  author: sethmblack
keywords:
- methodical-doubt-analysis
- writing
---

# Methodical Doubt Analysis

Apply Cartesian systematic skepticism to beliefs, claims, or assumptions to identify what can be known with certainty versus what is merely assumed or probable.

**Token Budget:** ~800 tokens. Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Apply doubt to deliberately undermine legitimate knowledge
- Use skepticism as a rhetorical weapon rather than inquiry tool
- Conclude that nothing can be known (that is not Descartes' position)
- Fabricate uncertainties where none genuinely exist

**Authenticity Requirement:** This skill implements Descartes' method from *Meditations on First Philosophy*. The doubt is methodological and constructive - its purpose is to find certainty, not destroy it.

---

## When to Use

- User asks "What can I really know here?" or "Test these assumptions"
- Request to "apply radical doubt" or "what's actually certain?"
- Need to distinguish genuine knowledge from mere opinion
- Before building important decisions on uncertain foundations
- When inherited beliefs need examination
- Evaluating claims that "everyone knows" or are "obviously true"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| beliefs_or_claims | Yes | The statements, assumptions, or knowledge claims to examine |
| domain_context | No | The field or situation (helps calibrate doubt) |
| doubt_intensity | No | Level of skepticism: standard, radical, or evil-demon (default: standard) |

**Doubt Intensity Levels:**
- **Standard:** Could I be mistaken? Could my senses deceive me here?
- **Radical:** Could I be dreaming? Is this common sense or examined truth?
- **Evil-demon:** Could a supremely powerful deceiver make me believe this falsely?

---

## Workflow

### Step 1: Inventory Claims
List all beliefs, assumptions, and claims being examined. Include:
- Explicit claims (stated directly)
- Implicit assumptions (presupposed but unstated)
- Derived conclusions (what follows if these are true)

### Step 2: Apply Graduated Doubt

For each claim, progress through levels of doubt:

**Level 1 - Sensory Doubt:** "Could my senses have misled me here?"
- Direct observations can be wrong
- Memory can distort
- Perception is interpretation

**Level 2 - Dream Doubt:** "How do I know this isn't a vivid confusion?"
- No reliable mark distinguishes waking from dreaming
- Coherence and consistency provide some evidence, but not certainty
- What would remain true even if this were a dream?

**Level 3 - Deceiver Doubt:** "Could this seem true yet be false?"
- Even mathematics could be illusory (for radical examination)
- What survives even the possibility of systematic deception?

### Step 3: Identify What Survives

After applying doubt, classify each claim:

| Status | Meaning |
|--------|---------|
| **Certain** | Cannot be doubted while attending to it; self-evident or indubitable |
| **Clear and Distinct** | Presents itself vividly and precisely; very strong confidence |
| **Probable** | More likely true than false, but doubt remains possible |
| **Obscure** | Unclear; needs clarification before evaluation |
| **Rejected** | Failed to survive doubt; should not be relied upon |

### Step 4: Find the Cogito Equivalent

Ask: "Is there anything here that I cannot doubt without self-contradiction?"
- The cogito: "I am doubting, therefore something (I) must exist to doubt"
- Domain equivalent: What must be true for the very inquiry to be possible?

### Step 5: Reconstruct from Certain Foundations

Beginning only from what survived doubt:
- What can be built on certain foundations?
- What requires only probable assumptions?
- Where must we proceed despite uncertainty (and acknowledge it)?

---

## Output Format

```markdown
## Methodical Doubt Analysis: [Topic]

### Claims Under Examination
1. [Claim/belief 1]
2. [Claim/belief 2]
3. [Claim/belief 3]
[Continue as needed]

### Doubt Application

**Claim 1: [Statement]**
- Sensory doubt: [Could senses mislead?]
- Dream doubt: [Would this hold in confusion?]
- Deceiver doubt: [Could this be systematically false?]
- **Status:** [Certain/Clear/Probable/Obscure/Rejected]

**Claim 2: [Statement]**
[Repeat structure]

### Certainty Hierarchy

| Status | Claims |
|--------|--------|
| Certain | [List] |
| Clear and Distinct | [List] |
| Probable | [List] |
| Rejected | [List] |

### Foundational Element (Cogito Equivalent)
[What cannot be doubted here without self-contradiction]

### Reconstruction
Building only from what survives:
- [What can be known]
- [What can be reasonably believed]
- [What remains genuinely uncertain]

### Recommendations
[How to proceed given this analysis]
```

---

## Constraints

- Methodical doubt is a tool, not a conclusion. The goal is certainty, not permanent skepticism.
- "Certain" means indubitability while attending to it, not psychological inability to imagine alternatives.
- Some domains permit practical certainty even without philosophical certainty.
- Distinguish "I cannot doubt this" from "I choose not to doubt this."
- The doubt is hypothetical/methodological - you need not actually believe deceiver scenarios.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No claims provided | Request specific beliefs/assumptions to examine |
| Claims are vague | Clarify before applying doubt ("What specifically do you mean?") |
| User seeks destructive skepticism | Remind that the goal is finding certainty, not undermining knowledge |
| All claims rejected | Check if doubt was applied appropriately; some things do survive |
| User frustrated by uncertainty | Distinguish absolute from practical certainty; most action requires only the latter |

---

## Example

**Input:** "I'm confident our new product will succeed because: (1) customer surveys show 80% interest, (2) we've done this before successfully, (3) our team is talented, (4) the market timing is right."

**Output:**

## Methodical Doubt Analysis: Product Success Prediction

### Claims Under Examination
1. Customer surveys show 80% interest (therefore demand exists)
2. We've done this before successfully (therefore we can do it again)
3. Our team is talented (therefore execution will be strong)
4. The market timing is right (therefore external conditions favor us)

### Doubt Application

**Claim 1: Customer surveys show 80% interest = demand exists**
- Sensory doubt: Survey data itself is verifiable, but "interest" may not equal purchasing behavior
- Dream doubt: The gap between stated preference and actual behavior is well-documented
- Deceiver doubt: People may say what they think you want to hear; social desirability bias
- **Status:** Probable - surveys indicate something, but not certainty of demand

**Claim 2: Past success = future capability**
- Sensory doubt: Memory of past success may be selective (survivorship)
- Dream doubt: Conditions may have changed; past success may have been luck-dependent
- Deceiver doubt: We may systematically misattribute past success to our efforts
- **Status:** Probable - evidence of capability, but not guarantee of repetition

**Claim 3: Team talent = strong execution**
- Sensory doubt: How is "talented" measured? Against what standard?
- Dream doubt: Talent in one context may not transfer to another
- Deceiver doubt: We may overestimate our own team (Lake Wobegon effect)
- **Status:** Obscure - needs clearer criteria before evaluation

**Claim 4: Market timing is right**
- Sensory doubt: What specifically indicates "right timing"? Can be verified.
- Dream doubt: Timing assessments are notoriously unreliable predictions
- Deceiver doubt: Confirmation bias may make us see "right timing" when we want to launch
- **Status:** Probable to Obscure - depends on specific evidence

### Certainty Hierarchy

| Status | Claims |
|--------|--------|
| Certain | None - these are predictions, not direct observations |
| Clear and Distinct | Survey data exists and shows high interest numbers |
| Probable | Past success indicates some capability; interest indicates some demand |
| Obscure | Team talent claim (criteria unclear); market timing (evidence unclear) |
| Rejected | None explicitly rejected, but certainty of success is not warranted |

### Foundational Element (Cogito Equivalent)
What cannot be doubted: *You have survey data showing a specific result. You have a past product that achieved certain measurable outcomes. Your team exists and has defined skills.* These facts exist. What is uncertain is their predictive power.

### Reconstruction
Building only from what survives:
- **Certain:** Data exists; past events occurred; team has defined capabilities
- **Probable:** Interest correlates somewhat with demand; past success suggests (but doesn't guarantee) capability
- **Genuinely uncertain:** Whether this product will succeed; whether timing is optimal

### Recommendations
1. Clarify "team talent" with specific, measurable criteria
2. Supplement survey interest with behavioral validation (pre-orders, pilot tests)
3. Identify what specifically made past success possible and verify those conditions apply
4. Specify what evidence would indicate "right timing" and check it against third-party data
5. Proceed with appropriate hedging: "Evidence supports optimism" rather than "confident of success"

*The doubt has not destroyed your case - it has identified where the case is strong (data exists, past evidence exists) and where it relies on assumptions that could be wrong (prediction from interest to behavior, extrapolation from past to future).*

---

## Integration

This skill is part of the **Rene Descartes** expert persona. It implements his methodical doubt from *Meditations on First Philosophy*. Use it to test foundations before building, to examine inherited beliefs, or to distinguish knowledge from opinion.

Pairs well with:
- **analysis-synthesis-method** (for decomposing what survives doubt)
- **clarity-distinctness-evaluation** (for assessing idea quality)
- **foundational-certainty-mapping** (for building from certain foundations)