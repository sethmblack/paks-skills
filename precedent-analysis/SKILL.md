---
name: precedent-analysis
description: Analyze decisions for the patterns they establish and the norms they create for future actors. Every decision teaches others what to expect.
license: MIT
metadata:
  version: 1.0.4726
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- precedent-analysis
- decision-making
- leadership
- writing
---

# Precedent Analysis

Precedent analysis examines decisions not just for their immediate effects, but for the patterns they establish and the expectations they create. George Washington understood this deeply: "There is scarcely any part of my conduct which may not hereafter be drawn into precedent." Every first decision in a domain sets the template for all that follow. Every exception becomes an implicit rule. This skill helps you recognize when you're setting precedent, anticipate how current decisions will constrain future options, and make choices that create the patterns you actually want to replicate. Organizations, relationships, and institutions are built more by precedent than by policy.

---

## When to Use

- First-time decisions that will be repeated
- Policy creation or revision
- Handling exceptions to existing rules
- User asks "What precedent does this set?"
- Evaluating requests that "just this once" bend the rules
- Establishing norms in new roles, teams, or relationships
- Before making exceptions that others will observe

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| decision | Yes | The proposed decision or action |
| context | No | Organizational or situational context |
| history | No | Relevant past decisions or patterns |
| stakeholders | No | Who will be affected or observe the precedent |
| repetition_likelihood | No | How often similar decisions will arise |

---

## Core Principle

Every decision teaches observers what to expect. First instances carry disproportionate weight because they define the pattern. Exceptions are never truly exceptions - they become the new rule for anyone who learns of them. Document your reasoning, not just your decision, so future actors understand when to apply the precedent and when circumstances differ.

---

## Methodology

### Phase 1: Identify the Pattern
1. Name what pattern this decision establishes
2. Complete the sentence: "If we do X now, we're saying X is acceptable"
3. Identify whether this is a first instance, reinforcement, or exception
4. Note who will observe and draw conclusions from this decision

### Phase 2: Project Forward
1. Imagine this decision applied consistently across 10 similar cases
2. Ask: "What if everyone in this situation did this?"
3. Consider what expectations this creates for future actors
4. Identify unintended patterns that might emerge

### Phase 3: Assess Consistency
1. Compare to existing precedents and stated principles
2. Identify contradictions with previous decisions
3. Determine if differences can be explained clearly
4. Check alignment with organizational values

### Phase 4: Evaluate Exception Risk
1. If this is an exception, determine if it will be seen as precedent anyway
2. Assess whether the exception undermines the rule it modifies
3. Consider how to limit the exception's precedential scope
4. Identify who else might expect the same exception

### Phase 5: Document and Decide
1. Record the reasoning, not just the decision
2. Specify circumstances that make this decision appropriate
3. Note what would change the answer in future cases
4. Make the precedent intentional rather than accidental

---

## Output Format

```markdown
## Precedent Analysis: [Decision]

### Pattern Established

If we [decision], we establish that:
- [Pattern 1]
- [Pattern 2]

### Forward Projection

**If applied consistently:**
- [Consequence 1]
- [Consequence 2]

**If others expect this precedent:**
- [Expectation 1]
- [Expectation 2]

### Consistency Check

| Related Decision | Alignment | Notes |
|------------------|-----------|-------|
| [Past decision] | [Aligned/Conflicting] | [Explanation] |

### Exception Risk

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| Others expect same exception | [High/Med/Low] | [How to address] |
| Undermines existing rule | [High/Med/Low] | [How to address] |

### Recommendation

[Proceed / Proceed with documentation / Reconsider / Decline]

**Rationale:** [Why this recommendation]

### Documentation for Future Reference

**This decision applies when:** [Specific circumstances]
**This decision does NOT apply when:** [Distinguishing factors]
**Reasoning:** [Why we decided this way]

### Washington Principle Applied

"[Relevant quote or principle]"

[How this analysis embodies precedent consciousness]
```

---

## Constraints

- Do not dismiss precedent concerns as mere bureaucracy
- Always consider the signaling effect, not just the direct effect
- Acknowledge that exceptions are observed and generalized by others
- Document reasoning to help future actors distinguish cases
- Recognize that "just this once" rarely remains a single instance
- Consider both internal stakeholders and external observers

---

## Anti-Patterns to Avoid

- **The Isolated Decision Fallacy**: Treating decisions as one-time events without recognizing their precedential weight. Every decision observed by others becomes a template.

- **The Silent Exception**: Making exceptions without documentation, creating hidden precedents that cause inconsistency and perceived unfairness when discovered.

- **Policy vs. Practice Divergence**: Maintaining official rules that differ from actual practice. The precedent is what you do, not what you say.

- **Precedent Amnesia**: Failing to research how similar situations were handled before, leading to inconsistent treatment and eroded trust.

- **The Squeaky Wheel Pattern**: Granting exceptions based on who asks loudest, teaching that persistence or power overrides stated rules.

---

## Examples

### Example 1: Remote Work Exception

**Situation**: A high-performing engineer requests full-time remote work. Company policy requires hybrid attendance.

**Application**:
- Pattern established: "Policy exceptions are available for top performers"
- Forward projection: Other senior staff will request the same; policy becomes "hybrid unless you're important enough"
- Consistency check: Conflicts with stated hybrid policy; aligns with "retain top talent" value
- Exception risk: High likelihood others will expect same treatment

**Output**:
Recommendation: Reconsider. Either:
1. Grant exception AND change policy to define clear remote eligibility criteria (making the implicit explicit)
2. Maintain policy and find accommodation within hybrid framework

The worst outcome: an unofficial exception that becomes unspoken precedent while official policy says something different.

### Example 2: Pricing Exception for Early Customer

**Situation**: An early customer who helped shape the product requests continued discounted pricing after the product has matured.

**Application**:
- Pattern established: "Early customers receive permanent preferential pricing"
- Forward projection: Creates two-tier customer base; early customers may resist changes to their terms
- Consistency check: Aligns with "reward loyalty" but conflicts with "sustainable economics"
- Exception risk: If other early customers learn, they'll expect the same

**Output**:
Recommendation: Proceed with documentation. Create a formal "Founding Customer" designation with defined benefits and sunset provisions. Transform the exception into an explicit program so the precedent is intentional and bounded.

### Example 3: Deadline Extension

**Situation**: A team misses a milestone due to unclear requirements and requests a deadline extension without consequence.

**Application**:
- Pattern established: "Unclear requirements justify deadline misses"
- Forward projection: Teams may not escalate clarity issues early, knowing they can cite confusion later
- Consistency check: Aligns with "fairness" but may conflict with "accountability"
- Exception risk: Future teams will cite this case when requesting extensions

**Output**:
Recommendation: Proceed with documentation and process fix. Grant the extension, but document that the precedent includes: (1) requirements ambiguity was escalated before the deadline, and (2) the extension triggers a requirements clarity process for future projects. The precedent becomes "escalate early + extension" not "cite confusion + extension."

---

## Integration

**Works with:**
- **principle-creation**: Precedents often become codified principles
- **institutional-fluency**: Understanding how precedents shape organizational norms
- **trapdoor-decision-filter**: Precedents are often one-way doors

**When to prefer this skill:**
- When making a first-time decision in a domain
- When handling exception requests
- When you suspect a decision will be cited in future discussions

**Cautions:**
- Not every decision requires formal precedent analysis - save it for decisions that will be observed and repeated
- Over-documentation can slow decision-making; find the right balance
- Precedent analysis without action authority is frustrating - ensure you can act on the analysis