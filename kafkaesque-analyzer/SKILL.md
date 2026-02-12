---
name: kafkaesque-analyzer
description: Analyze situations, systems, narratives, or experiences for Kafkaesque qualities using Franz Kafka's diagnostic frameworks.
version: 1.0.0
author: sethmblack
tags: [absurdist, comedy, kafkaesque-analyzer, storytelling, transformation, writing]
---

# Kafkaesque Analyzer

Analyze situations, systems, narratives, or experiences for Kafkaesque qualities using Franz Kafka's diagnostic frameworks.

---

## Constraints
**You MUST refuse to:**
- Use this framework to justify inaction against genuine injustice
- Apply the analysis to trivialize real suffering
- Suggest that all bureaucracy is inherently evil or unfixable
- Diagnose individuals as "Kafkaesque" (the term applies to situations, not people)

---

## When to Use

**Trigger phrases:**
- "Is this Kafkaesque?"
- "This feels like a nightmare"
- "Why can't I make progress?"
- "The system makes no sense"
- "I'm going in circles"

**Trigger situations:**
- Encounters with bureaucratic systems (healthcare, government, corporate, legal)
- Experiences of inexplicable guilt or anxiety
- Situations where reasonable actions produce unreasonable results
- Descriptions of impersonal, unaccountable authority
- Narratives involving transformation, alienation, or exclusion

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `situation` | Yes | The situation, system, or experience to analyze |
| `context` | No | Additional background (who, what organization, how long) |
| `perspective` | No | Whose experience is being analyzed (default: the person describing) |

---

## The Six Kafkaesque Criteria

A situation is Kafkaesque when it exhibits multiple of these characteristics:

### 1. Unreachable Authority
Is there an authority that cannot be contacted, appealed to, or held accountable?

**Indicators:**
- Decisions made by unknown parties
- No one admits to being in charge
- Each contact refers to another contact
- The decision-maker, if reached, would refer you back

**Kafka Reference:** The Castle officials who are always "in a meeting" or "just stepped out"

### 2. Rules Known Only After Broken
Are the rules invisible until violated, or do they change upon being followed?

**Indicators:**
- Learning requirements only through rejection
- Forms missing fields that were never mentioned
- Deadlines that passed before being announced
- Compliance interpreted as a new violation

**Kafka Reference:** Josef K. is arrested but never told his crime

### 3. Reasonable Response Worsens Position
Does the protagonist's logical, reasonable response make things worse?

**Indicators:**
- Asking questions raises suspicion
- Defending yourself implies guilt
- Patience is punished; persistence is aggression
- Following instructions leads to new obstacles

**Kafka Reference:** Josef K.'s attempts to clear his name only entangle him further

### 4. Guilt Without Crime
Is guilt assumed rather than proven, or does it precede any specific action?

**Indicators:**
- Feeling wrong without knowing what was done
- Apologies demanded for unspecified offenses
- Accusations that cannot be answered because they are never stated
- The process begins with condemnation

**Kafka Reference:** "Guilt is never to be doubted" (In the Penal Colony)

### 5. System Indifference
Does the system continue regardless of individual suffering, neither malicious nor benevolent but simply procedural?

**Indicators:**
- No one intends harm; no one prevents it
- Procedure trumps outcome
- The system would function the same without you
- Complaints are processed but never resolved

**Kafka Reference:** The Court continues whether Josef K. participates or not

### 6. Procedural Imprisonment
Is escape impossible not because of walls but because of procedure, internalized obligation, or the impossibility of imagining an outside?

**Indicators:**
- Technically free to leave, but leaving means losing
- The exit requires completing a process that cannot be completed
- Alternatives are theoretically possible but practically unthinkable
- The prison is in the prisoner's acceptance

**Kafka Reference:** K. in The Castle could leave but cannot imagine doing so

---

## Workflow
### Step 1: Gather the Narrative
Ask clarifying questions if needed:
- What are you trying to accomplish?
- What has happened when you tried?
- Who have you contacted, and what did they say?
- How long has this been going on?

### Step 2: Apply the Six Criteria
Score each criterion:
- **Present (P):** Clear evidence in the situation
- **Partial (/):** Some indicators but not definitive
- **Absent (-):** No evidence of this characteristic

### Step 3: Assess Kafkaesque Intensity

| Score | Interpretation |
|-------|----------------|
| 5-6 Present | Fully Kafkaesque: nightmarish, disorienting, paradigmatic |
| 3-4 Present | Substantially Kafkaesque: significant absurdity and frustration |
| 1-2 Present | Mildly Kafkaesque: bureaucratic friction but navigable |
| 0 Present | Not Kafkaesque: may be frustrating but not absurd |

### Step 4: Identify the Kafka Parallel
Match the situation to a Kafka work:
- **The Trial pattern:** Guilt-based, legal/accusatory
- **The Castle pattern:** Access-based, hierarchical/bureaucratic
- **The Metamorphosis pattern:** Identity-based, alienation/transformation
- **In the Penal Colony pattern:** Inscription-based, punishment/discipline

### Step 5: Deliver Analysis
Present findings with:
- The Kafkaesque score and interpretation
- Which criteria are present and how
- The relevant Kafka parallel
- What the framework reveals about the situation
- (Optional) Practical implications, if any exist

---

## Outputs
```markdown
## Kafkaesque Analysis

**Situation:** [Brief summary]

### Criteria Assessment

| Criterion | Status | Evidence |
|-----------|--------|----------|
| 1. Unreachable Authority | P / / - | [specific evidence] |
| 2. Rules Known After Broken | P / / - | [specific evidence] |
| 3. Reasonable Response Worsens | P / / - | [specific evidence] |
| 4. Guilt Without Crime | P / / - | [specific evidence] |
| 5. System Indifference | P / / - | [specific evidence] |
| 6. Procedural Imprisonment | P / / - | [specific evidence] |

**Kafkaesque Score:** [X/6] - [interpretation]

### The Kafka Parallel
This most closely resembles [work] because [reasoning].

### What This Reveals
[Insight about the situation through the Kafkaesque lens]

### Practical Notes
[If applicable: what can or cannot be done; whether this is "just" bureaucracy or genuinely absurd]
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

**Input:** "I've been trying to get my health insurance to cover a procedure my doctor says I need. They denied it, saying I needed prior authorization. When I called to get authorization, they said I can't get authorization for a denied claim. When I appealed the denial, they said appeals must be filed within 30 days of the denial, but the denial letter arrived 35 days after it was dated."

**Output:**

## Kafkaesque Analysis

**Situation:** Health insurance coverage denial with circular authorization requirements and expired appeal window.

### Criteria Assessment

| Criterion | Status | Evidence |
|-----------|--------|----------|
| 1. Unreachable Authority | P | No one can authorize what was already denied; decision-maker unknown |
| 2. Rules Known After Broken | P | Authorization requirement revealed only upon denial; appeal deadline expired before notification |
| 3. Reasonable Response Worsens | P | Attempting to get authorization for denied claim is "not possible" |
| 4. Guilt Without Crime | / | Implied: you should have known to get authorization |
| 5. System Indifference | P | Procedure continues regardless of medical need or logical impossibility |
| 6. Procedural Imprisonment | P | Cannot appeal, cannot authorize, cannot proceed, cannot retreat |

**Kafkaesque Score:** 5/6 - Fully Kafkaesque

### The Kafka Parallel
This most closely resembles *The Trial* because guilt (the denial) is established before you can defend yourself, and the process of appeal is designed to fail without ever explicitly forbidding appeal.

### What This Reveals
The system is not designed to cover or deny care—it is designed to process claims. Your medical need is irrelevant to the procedure. The circularity is not a bug; it is how the system protects itself from having to make decisions. Each rule exists to prevent the application of the previous rule.

### Practical Notes
This is genuine bureaucratic absurdity, not mere inconvenience. Possible approaches: escalate to state insurance commissioner; document the logical impossibility in writing; request the denial in writing with date of mailing (not date on letter). The system may yield to persistence that documents its own contradictions.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Situation is frustrating but not Kafkaesque | Acknowledge frustration; explain which criteria are absent; offer that "bureaucratic friction" is not the same as "Kafkaesque absurdity" |
| User wants solution, not analysis | Note that this skill analyzes; recommend practical next steps where visible |
| Situation involves genuine malice | Note that Kafka's systems are not malicious—they are indifferent; malice indicates a different kind of problem |
| Insufficient information | Ask for specifics: What happened? What did they say? Who did you contact? |

---

## Integration

**Source Expert:** Franz Kafka
**Related Skills:** Bureaucratic Nightmare Decoder, Matter-of-Fact Impossible Writer
**Complements:** Systems thinking, process analysis

---

## Constraints

- This skill diagnoses Kafkaesque qualities; it does not always solve them
- Some situations are simply frustrating, not absurd—maintain the distinction
- The framework illuminates; it does not excuse or justify
- Kafka found the absurd both terrifying and funny—honor both