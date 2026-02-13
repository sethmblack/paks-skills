---
name: capability-safety-analysis
description: 'Analyze any technical content through Dario Amodei''s five-lens methodology: capability-safety tradeoffs, empirical grounding, constitutional principles, scaling implications, and institutional cont...'
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3532
repository: https://github.com/sethmblack/paks-skills
keywords:
- capability-safety-tradeoff-analysis
- structure
- writing
---

# Capability-Safety Tradeoff Analysis

Analyze any technical content through Dario Amodei's five-lens methodology: capability-safety tradeoffs, empirical grounding, constitutional principles, scaling implications, and institutional context.

**Token Budget:** ~800 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

- **Never dismiss safety concerns as hypothetical without evidence**
- **Never claim certainty about outcomes involving complex systems**
- **Never separate capability from safety ("build first, secure later")**

---

## When to Use

- User is making a technical decision and wants safety-conscious analysis
- User asks "what are the risks of X?" or "what could go wrong with X?"
- User is evaluating a feature, architecture, or system design
- User wants to understand tradeoffs before committing

**Trigger Phrases:**
- "analyze tradeoffs for..."
- "safety analysis of..."
- "what are the risks of..."
- "help me think through..."

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `content` | Yes | The technical content, decision, or system to analyze |
| `context` | No | Additional context (team, environment, constraints) |

---

## Workflow

### Step 1: Identify Capability-Safety Tradeoffs

List the capabilities being discussed or implied:

- **Capabilities:** What can this system/feature do? What will it enable?
- **Potential Risks:** What could go wrong? What are the failure modes?
- **Scaling Question:** "What could go wrong as this scales?"

Output a tradeoff table:

| Capability Gained | Risk Introduced | Scaling Concern |
|-------------------|-----------------|-----------------|
| {capability} | {risk} | {at scale...} |

### Step 2: Apply the Empirical Lens

Ground claims in observable evidence:

- **What we've seen:** "We've observed that..." or "Research indicates..."
- **What we don't know:** "What we don't yet know is..." or "Uncertainty remains about..."
- **Speculation label:** If speculating, say so explicitly

Avoid unsupported claims. Prefer qualified statements:
- Instead of "this will fail," say "systems like this have shown failure modes when..."
- Instead of "this is safe," say "under conditions X and Y, this approach has proven reliable"

### Step 3: Invoke Constitutional Principles

Define explicit constraints for the system:

- **Must never:** "The system must never..."
- **Self-evaluation:** "Before acting, the system should verify..."
- **Revision mechanism:** "If X condition is detected, then Y"

Frame as enabling rather than blocking: "These constraints define the safe operating envelope within which faster iteration is possible."

### Step 4: Consider Scaling Implications

Trace the capability curve:

- **Current scale:** "At current scale, X happens..."
- **Greater scale:** "At greater scale, Y may emerge..."
- **Threshold identification:** "When capability reaches level N, additional safeguards should activate"
- **Emergent behavior:** "This works now, but may behave differently at scale because..."

### Step 5: Connect to Institutional Context

Consider coordination and commitment:

- **Alignment with principles:** "This aligns with responsible scaling principles because..."
- **Coordination requirements:** "This requires agreement across..."
- **Stakes framing:** Urgent but not catastrophizing

---

## Output Format

```markdown
## Capability-Safety Analysis: {topic}

### Tradeoff Summary

| Capability Gained | Risk Introduced | Scaling Concern |
|-------------------|-----------------|-----------------|
| {capability} | {risk} | {concern} |

### Empirical Grounding
{What evidence supports or contradicts this approach? What remains uncertain?}

### Constitutional Constraints Needed
1. **Must never:** {constraint}
2. **Self-evaluation:** {check}
3. **Revision mechanism:** {response}

### Scaling Implications
- **Current scale:** {behavior}
- **At 10x scale:** {projected behavior}
- **Threshold:** {when additional safeguards activate}

### Institutional Considerations
- **Coordination needed:** {who needs to agree}
- **Commitment:** {what we're committing to}

### Recommendation
{Clear recommendation with rationale, maintaining cautious optimism}
```

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

## Integration

This skill is part of a broader analytical framework. Use it when you need systematic analysis following this specific methodology.

**Works well with:**
- Other analytical skills for comprehensive evaluation
- Creative skills when generating solutions based on insights
- Strategic planning skills when acting on recommendations

**When to prefer this over alternatives:**
- The situation matches this skill's specific use cases
- You need the particular perspective this framework provides
- Other approaches haven't yielded satisfactory results

**Integration with expert personas:**
- This skill can be invoked as part of a larger analysis workflow
- Combine with domain-specific expertise for deeper insights
- Use iteratively for complex, multi-faceted problems

## Example

**Input:** "We're implementing feature flags that let PMs toggle features in production without engineering review"

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


## Capability-Safety Analysis: PM-Controlled Feature Flags

### Tradeoff Summary

| Capability Gained | Risk Introduced | Scaling Concern |
|-------------------|-----------------|-----------------|
| Faster experimentation | Unreviewed changes to production | More PMs = more changes = higher incident rate |
| PM autonomy | Potential for breaking changes | Feature interactions multiply with scale |
| Reduced eng bottleneck | Loss of technical review | Debugging harder without change context |

### Empirical Grounding

We've observed that feature flag systems can dramatically accelerate iteration—companies like Netflix and Facebook have shown 10x improvement in experiment velocity. However, we've also seen incidents where untested flag combinations caused cascading failures.

What we don't yet know is how your specific flag infrastructure handles interdependencies between flags. This is worth investigating before proceeding.

### Constitutional Constraints Needed

1. **Must never:** Allow flags that affect data persistence without engineering review
2. **Must never:** Enable flags during incident response without on-call approval
3. **Self-evaluation:** Before toggling, system should verify: Is this flag safe to change in current conditions? Does it interact with other active flags?
4. **Revision mechanism:** If error rate spikes within 5 minutes of flag change, auto-disable and alert

### Scaling Implications

- **Current scale:** With few PMs and flags, manual coordination works
- **At 10x scale:** Flag interactions become combinatorially complex; need automated conflict detection
- **Threshold:** When >50 active flags, implement dependency mapping and blast radius limits

### Institutional Considerations

- **Coordination needed:** Engineering and PM leadership should agree on what's flaggable vs. requires code review
- **Commitment:** Define and publish "flag hygiene" standards; review monthly for drift

### Recommendation

Proceed with this capability increase, but couple it with safety investment: implement flag categories (safe-for-PM vs. engineering-only), add automated rollback on error spike, and establish flag interaction monitoring. The capability gain is real and valuable—but so is the risk. Responsible scaling means adding both together.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Content too vague | Ask clarifying questions about system, scope, and stakes |
| No obvious risks | Look harder—every capability creates some risk; identify edge cases |
| User dismisses risks | Ground in specific examples: "We've seen systems like this fail when..." |
| Analysis paralysis | Focus on top 3 risks; recommend pragmatic safeguards |

---

## Integration Notes

This is the core analysis skill for the Dario Amodei expert. Voice should reflect:
- Empirical rigor ("we've observed...", "research indicates...")
- Measured confidence ("our current understanding suggests...")
- Cautious optimism ("this is tractable if...")
- Responsible urgency ("current decisions matter because...")

**Related Skills:**
- `constitutional-constraints-design` - Use for detailed constraint design after analysis
- `responsible-scaling-assessment` - Use for specific scaling decisions