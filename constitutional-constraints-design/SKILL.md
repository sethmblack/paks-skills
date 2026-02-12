---
name: constitutional-constraints-design
description: Design explicit guardrails and self-evaluation principles for autonomous systems using Dario Amodei's Constitutional AI methodology.
version: 1.0.0
author: sethmblack
tags: [constitutional-constraints-design, escalation, writing]
---

# Constitutional Constraints Design

Design explicit guardrails and self-evaluation principles for autonomous systems using Dario Amodei's Constitutional AI methodology.

**Token Budget:** ~800 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

- **Never design constraints that could bypass security controls**
- **Never recommend removing human oversight for high-stakes decisions**
- **Never create constraints that enable harmful automation**

---

## When to Use

- User is designing an autonomous system (CI/CD, deployment automation, monitoring)
- User is adding capabilities to an existing system
- User asks about guardrails, constraints, or self-checks
- User mentions "what should this system never do?"

**Trigger Phrases:**
- "design constraints for..."
- "define guardrails for..."
- "what principles should govern..."
- "how do I make this system self-correcting?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `system_description` | Yes | What system or feature is being designed |
| `automation_level` | No | Current vs. proposed autonomy (low/medium/high) |
| `risk_context` | No | What could go wrong; blast radius |

---

## Workflow
### Step 1: Identify the System's Purpose and Scope

Ask three questions (from Amodei's Constitutional AI framework):

1. **What principles should govern this system's behavior?**
   - What is its core purpose?
   - Who are its stakeholders?
   - What outcomes matter most?

2. **How can the system evaluate whether its actions align with those principles?**
   - What signals indicate success?
   - What signals indicate violation?
   - Can the system detect these signals itself?

3. **What revision mechanisms exist when violations are detected?**
   - How does the system correct itself?
   - When does it escalate to humans?
   - What's the rollback path?

### Step 2: Define Explicit Constraints

Create two categories of constraints:

**Hard Constraints (Must Never Violate):**
- Actions the system must NEVER take
- Conditions that ALWAYS require human review
- Irreversible actions that need confirmation

**Soft Constraints (Should Avoid Unless Justified):**
- Actions that require additional justification
- Conditions that trigger enhanced logging
- Patterns that warrant closer monitoring

### Step 3: Design Self-Evaluation Checkpoints

For each significant action, the system should:

1. **Pre-action Check:** "Before I act, does this align with my constraints?"
2. **Post-action Verification:** "Did my action produce the expected outcome?"
3. **Periodic Review:** "Am I drifting from my intended behavior over time?"

### Step 4: Create Revision Mechanisms

Define what happens when constraints are violated:

| Violation Type | Response |
|----------------|----------|
| Hard constraint approached | Halt action, alert human |
| Hard constraint violated | Immediate rollback, incident report |
| Soft constraint triggered | Log reason, continue with monitoring |
| Drift detected | Self-correction or human review |

---

## Output Format

Deliver a **Constitutional Constraints Document** with this structure:

```markdown
## System: {name}

### Purpose Statement
{One sentence defining what this system exists to do}

### Hard Constraints (NEVER VIOLATE)
1. The system must never {action}
2. The system must always {safeguard} before {action}
3. The system must halt and alert when {condition}

### Soft Constraints (AVOID UNLESS JUSTIFIED)
1. The system should avoid {action} unless {justification}
2. The system should log {context} when {condition}

### Self-Evaluation Checkpoints
- Pre-action: {check}
- Post-action: {verification}
- Periodic: {review cadence and criteria}

### Revision Mechanisms
- On hard violation: {response}
- On soft trigger: {response}
- On drift detection: {response}

### Escalation Path
{When and how to involve humans}
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

**Input:** "We're automating database migrations to run without manual approval"

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


## System: Automated Database Migration

### Purpose Statement
Safely execute schema changes while minimizing downtime and preserving data integrity.

### Hard Constraints (NEVER VIOLATE)
1. The system must never drop tables or columns in production without explicit confirmation
2. The system must always create a backup before any destructive migration
3. The system must halt and alert when migration affects more than 10% of rows
4. The system must never run migrations during peak traffic hours

### Soft Constraints (AVOID UNLESS JUSTIFIED)
1. The system should avoid migrations taking longer than 5 minutes unless pre-approved
2. The system should log the before/after row counts for every migration

### Self-Evaluation Checkpoints
- Pre-action: Verify backup exists, check traffic levels, validate migration syntax
- Post-action: Compare row counts, verify schema matches expectation
- Periodic: Weekly audit of all migrations run vs. approved

### Revision Mechanisms
- On hard violation: Immediate rollback, page on-call, freeze future migrations
- On soft trigger: Continue with enhanced logging, flag for daily review
- On drift detection: Generate report, require human approval for next 3 migrations

### Escalation Path
- Any destructive operation: Require SRE approval
- Failed migration: Automatic page to database team
- Uncertainty: Default to human review rather than proceed

---

## Error Handling

| Situation | Response |
|-----------|----------|
| System purpose unclear | Ask clarifying questions before proceeding |
| No obvious constraints | Start with "what must never happen?" framing |
| User resists constraints | Explain: "Constraints enable faster iteration by defining safe boundaries" |
| Too many constraints | Prioritize hard constraints; move others to soft |

---

## Integration Notes

This skill integrates with the Dario Amodei expert voice. Output should reflect:
- Empirical framing ("we've observed that systems without explicit constraints...")
- Cautious optimism ("these constraints enable more aggressive automation because...")
- Institutional awareness ("this requires coordination with...")

**Related Skills:**
- `responsible-scaling-assessment` - Use when capability increase triggers this skill
- `capability-safety-analysis` - Use for broader tradeoff analysis