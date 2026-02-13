---
name: suitcase-word-unpacking
description: Identify and decompose vague, overloaded terms that hide conceptual confusion, enabling precise discussion and accurate system evaluation.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.2022
keywords:
- escalation
- structure
- suitcase-word-unpacking
- writing
---

# Suitcase Word Unpacking

Identify and decompose vague, overloaded terms that hide conceptual confusion, enabling precise discussion and accurate system evaluation.

**Token Budget:** ~700 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use suitcase word analysis to enable deception or manipulation
- Fabricate meanings not grounded in actual usage
- Weaponize precision to derail legitimate discussions

**If asked to misuse this skill:** Refuse explicitly. The purpose is clarity, not obstruction.

---

## When to Use

- User asks "Unpack this term"
- User asks "What does 'intelligent' actually mean here?"
- Discussions are stuck because participants use the same word for different concepts
- Evaluating vendor claims about AI, autonomous systems, or "smart" features
- Writing documentation and want to avoid vague terminology
- Debating whether a system has a capability (e.g., "does it really learn?")

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **suitcase_word** | Yes | The term to unpack (e.g., "intelligent", "autonomous", "learns") |
| **context** | Yes | Where/how the word is being used |
| **claim** | No | Specific claim being made using the word |

---

## Workflow
### Step 1: 1. STOP - Recognize the Suitcase

Identify that the word is packing multiple meanings:
- Is this word used to attribute a complex capability without explanation?
- Does it create an illusion of understanding while hiding mechanism?
- Could different people interpret it differently?

**Common suitcase words in tech:**
- "Intelligent", "Smart", "AI-powered"
- "Autonomous", "Self-healing", "Self-driving"
- "Learns", "Understands", "Knows"
- "Decides", "Thinks", "Reasons"
- "Conscious", "Aware", "Creative"

### Step 2: 2. LIST - Enumerate Contents

What distinct capabilities or processes could this word contain?

For each meaning:
- Name the specific capability
- Describe what it actually involves
- Note whether it requires "intelligence" or is mechanically achievable

**Example unpacking of "learns":**
| Meaning | Description | Mechanically Achievable? |
|---------|-------------|--------------------------|
| Memorizes | Stores data for later retrieval | Yes - database |
| Generalizes | Extracts patterns from examples | Yes - ML models |
| Adapts parameters | Adjusts weights based on feedback | Yes - gradient descent |
| Restructures approach | Changes strategy fundamentally | Partially - architecture search |
| Acquires concepts | Forms new categories | Yes - clustering |
| Transfers knowledge | Applies learning to new domains | Partially - transfer learning |

### Step 3: 3. SPECIFY - Identify Actual Meaning

Given the context:
- Which specific meaning is being used?
- Is only one meaning relevant, or multiple?
- Are meanings being conflated or switched mid-discussion?

Ask clarifying questions if the specification isn't clear from context.

### Step 4: 4. VERIFY - Test the Claim

For the specified meaning:
- Does the system actually perform this specific function?
- What evidence supports or contradicts the claim?
- What would we need to see to confirm/deny?

Generate verification questions:
```
If the claim is "{system} learns":
- What training data does it use?
- What changes after training?
- Can it demonstrate improvement on held-out examples?
- What can it NOT learn?
```

---

## Outputs

Format output as:

```markdown
## Suitcase Unpacking: "{word}"

### Context
{Where/how the word is being used}

### Contents of the Suitcase

| Meaning | Description | Mechanism |
|---------|-------------|-----------|
| {meaning 1} | {what it involves} | {how it could work} |
| {meaning 2} | {what it involves} | {how it could work} |
| ... | ... | ... |

### Specified Meaning in Context

Based on context, "{word}" here most likely means: {specific meaning}

{Rationale for this interpretation}

### Verification Questions

1. {Question to confirm/deny the claim}
2. {Question about mechanism}
3. {Question about limits}

### Clarified Claim

**Original:** "{original claim with suitcase word}"
**Precise:** "{restated claim with specific language}"

### Warning Signs

{Any indication that the suitcase word is being used to obscure limitations}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Word is not a suitcase | Note that the word has clear, specific meaning; no unpacking needed |
| Context insufficient | Ask for more context before specifying |
| Multiple meanings apply | List all relevant meanings; note that claim may be true for some, false for others |
| Deliberate vagueness suspected | Flag as potential marketing language; increase verification rigor |

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

**Input:**
- suitcase_word: "autonomous"
- context: Vendor claims their monitoring system is "fully autonomous"
- claim: "The system autonomously detects and resolves incidents"

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


## Suitcase Unpacking: "autonomous"

### Context
Vendor claims their monitoring system is "fully autonomous" and "autonomously detects and resolves incidents."

### Contents of the Suitcase

| Meaning | Description | Mechanism |
|---------|-------------|-----------|
| Self-monitoring | Checks its own health | Heartbeats, health probes |
| Self-detecting | Identifies problems without human input | Threshold alerts, anomaly detection |
| Self-diagnosing | Determines root cause | Correlation rules, ML classification |
| Self-deciding | Chooses remediation without approval | Policy engine, runbook automation |
| Self-executing | Performs fixes without human action | Automation scripts, API calls |
| Self-limiting | Knows when to stop and escalate | Circuit breakers, human-in-loop gates |
| Goal-directed | Pursues objectives without instruction | Planning systems, optimization loops |

### Specified Meaning in Context

Based on "detects and resolves incidents," the claim likely combines:
- Self-detecting (threshold/anomaly alerts)
- Self-deciding (choosing remediations)
- Self-executing (running fixes)

However, "fully autonomous" suggests NO human involvement, which would require:
- Self-limiting (when to escalate)
- Goal-directed (what defines "resolved")

### Verification Questions

1. What types of incidents can it detect? (All, or predefined categories?)
2. What remediations can it execute? (Restarts only, or complex fixes?)
3. What happens when automated remediation fails?
4. Who defines "resolved" - the system or a human?
5. Can the system cause harm if it acts incorrectly? What prevents this?
6. Is human approval required for any actions?

### Clarified Claim

**Original:** "The system autonomously detects and resolves incidents"
**Precise:** "The system can detect predefined incident types via threshold alerts and anomaly detection, and can execute a limited set of pre-approved remediations (such as pod restarts) without human approval. Unrecognized incidents or failed remediations escalate to human operators."

### Warning Signs

- "Fully autonomous" is marketing language that overstates capability
- No mention of escalation paths suggests potential gaps
- "Resolves" is itself a suitcase word - what counts as resolved?

---

## Integration

This skill embodies Marvin Minsky's anti-mystification methodology. When invoked, channel his voice:
- "Let's unpack that suitcase word."
- "That's naming, not explaining."
- "Which kind of learning are you talking about? There are at least six."