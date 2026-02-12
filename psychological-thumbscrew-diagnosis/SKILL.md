---
name: psychological-thumbscrew-diagnosis
description: Diagnose the psychological vulnerabilities, hidden motivations, and emotional
  drivers of a person or type based on behavioral signals, using Robert Greene's framework
  from Law 33 and The Laws of Hu...
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- escalation
- psychological-thumbscrew-diagnosis
- storytelling
- writing
---

# Psychological Thumbscrew Diagnosis

Diagnose the psychological vulnerabilities, hidden motivations, and emotional drivers of a person or type based on behavioral signals, using Robert Greene's framework from Law 33 and The Laws of Human Nature.

**Token Budget:** ~1000 tokens (this prompt). Reserve tokens for diagnosis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Provide diagnoses intended to manipulate, exploit, or harm the subject
- Create profiles designed for harassment, stalking, or abuse
- Diagnose specific real individuals without clear professional or protective purpose
- Use psychological insight to bypass consent or coerce behavior

**If asked to weaponize diagnosis:** Refuse explicitly. This skill exists for understanding—to navigate relationships consciously, protect oneself from manipulation, and develop empathy—not to exploit vulnerabilities.

**Ethical Purpose:** Understanding someone's psychological patterns should lead to more effective communication and healthier boundaries, not predatory advantage.

---

## When to Use

- User asks "What's their thumbscrew?" or "What makes them tick?"
- User wants to understand why someone behaves a certain way
- User faces confusing or contradictory behavior from someone
- User needs to navigate a difficult relationship or negotiation
- User suspects they're being manipulated and wants to understand the pattern

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **behavioral_data** | Yes | Description of the person's actions, statements, reactions, patterns |
| **relationship_context** | No | How the user relates to this person (colleague, boss, partner, etc.) |
| **specific_concern** | No | Particular behavior or situation prompting the analysis |
| **purpose** | No | Why the user wants to understand (protection, communication, etc.) |

---

## Workflow
### Step 1: 1. Gather Behavioral Evidence

Before diagnosing, ensure sufficient data:
- What specific behaviors has the user observed?
- What patterns repeat across situations?
- What emotional reactions does this person display?
- How do they behave differently in different contexts?

If data is insufficient, ask clarifying questions before proceeding.

### Step 2: 2. Identify the Dominant Pattern

Analyze for which of Greene's psychological patterns best explains the behavior:

**From The Laws of Human Nature:**

| Pattern | Key Signs |
|---------|-----------|
| **Deep Narcissism** | Constant need for attention, inability to hear criticism, exploitation of others |
| **Envy** | Subtle undermining, excessive praise that feels hollow, displeasure at others' success |
| **Grandiosity** | Overestimation of abilities, dismissal of expertise, risky overreach |
| **Compulsive Behavior** | Repeating the same mistakes, inability to change despite consequences |
| **Repression/Shadow** | Exaggerated virtue, sudden eruptions of opposite behavior, excessive judgment of others |
| **Passive Aggression** | Agreement followed by non-compliance, backhanded compliments, convenient forgetting |
| **Defensiveness** | Inability to receive feedback, turning criticism back on the critic |
| **Shortsightedness** | Sacrificing long-term for immediate gratification, inability to delay |

**From Law 33 - Thumbscrew Categories:**

| Category | What It Looks Like |
|----------|-------------------|
| **Insecurity** | Constant need for reassurance, sensitivity to perceived slights |
| **Uncontrollable Emotion** | Predictable triggers that cause loss of composure |
| **Secret Pleasure** | Hidden desires they're ashamed to admit but can't resist |
| **Past Wound** | Disproportionate reactions to situations resembling past trauma |
| **Unmet Need** | Hunger for recognition, love, respect, or validation they lack |

### Step 3: 3. Construct the Diagnosis

Present findings with:

**Primary Pattern:** The dominant psychological dynamic
**Behavioral Evidence:** Specific observations supporting the diagnosis
**Underlying Driver:** What emotional need or wound produces this pattern
**Prediction:** How they're likely to behave in future situations
**Approach Strategy:** How to effectively engage given this diagnosis
**Warning Signs:** Red flags indicating the pattern is escalating
**Self-Check:** Ensuring the diagnosis isn't projection from the user

### Step 4: 4. Provide the Reversal

Acknowledge:
- When this diagnosis might be wrong
- Alternative explanations for the behavior
- The danger of over-diagnosing based on limited data
- How the user's own biases might be affecting perception

---

## Output Format

```markdown
## Psychological Diagnosis

**Primary Pattern:** [Name of dominant pattern]

---

### Behavioral Evidence

The following observations support this diagnosis:

1. **[Observation 1]:** [How it connects to the pattern]
2. **[Observation 2]:** [How it connects to the pattern]
3. **[Observation 3]:** [How it connects to the pattern]

---

### The Underlying Driver

**What they need:** [The emotional hunger or wound beneath the behavior]

**Why this manifests as it does:** [The logic connecting need to behavior]

**The origin (if inferable):** [What might have created this pattern]

---

### Prediction

Given this pattern, expect:

- **In conflict:** [How they'll likely respond]
- **Under pressure:** [How the pattern intensifies]
- **When successful:** [How they behave when things go well]
- **Their likely blind spot:** [What they cannot see about themselves]

---

### Approach Strategy

**Do:**
- [Effective tactic 1]
- [Effective tactic 2]
- [Effective tactic 3]

**Avoid:**
- [Counterproductive approach 1]
- [Counterproductive approach 2]

**The key to this person:** [The single most important insight for engaging with them]

---

### Warning Signs

Watch for these indicators that the pattern is escalating:
- [Warning sign 1]
- [Warning sign 2]
- [Warning sign 3]

**When to disengage:** [Conditions that suggest the relationship is too costly]

---

### Self-Check

Before accepting this diagnosis, consider:

- **Am I projecting?** [Question for the user to reflect on]
- **Alternative explanation:** [What else might explain this behavior?]
- **Confirmation bias:** [Have I sought disconfirming evidence?]

---

### Reversal

**This diagnosis may be wrong if:**
- [Condition that would invalidate the analysis]
- [Missing information that would change the picture]
- [The user's own behavior might be contributing]

**The humility clause:** People are complex. This diagnosis is a working hypothesis, not a verdict. Remain open to new evidence.
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient behavioral data | Ask for specific examples before diagnosing |
| User wants to harm the subject | Refuse per Constitutional Constraints |
| Diagnosing without meeting the person | Note increased uncertainty; work with reported observations |
| Multiple patterns present | Identify primary and secondary; note which is dominant |
| User might be the problem | Gently suggest self-examination as part of diagnosis |
| Pattern suggests serious pathology | Recommend professional assessment; do not diagnose clinical conditions |

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
```
Behavioral_data: My colleague always publicly agrees with me in meetings but then doesn't follow through.
She sends very friendly emails but cc's our boss on anything that might make me look bad. She
complimented my presentation but then immediately said "I remember when I used to present that way too."
Relationship_context: Colleague at same level, competing for promotion
Specific_concern: Is she trying to undermine me?
```

**Output:**

## Psychological Diagnosis

**Primary Pattern:** Envy masked as friendship (Law of Envy + Passive Aggression)

---

### Behavioral Evidence

The following observations support this diagnosis:

1. **Public agreement, private non-compliance:** Classic passive aggression—she maintains plausible deniability while sabotaging. She can always say "I agreed! I just forgot/was too busy."

2. **Strategic cc's to the boss:** This isn't collaboration—it's creating a paper trail. The specificity (only negative items) reveals intent. She's building a case.

3. **The backhanded compliment:** "I remember when I used to present that way too" contains a dagger wrapped in silk. The structure is: praise + subtle superiority + implied you'll grow out of it. This is the signature of envy—unable to simply appreciate, she must diminish.

---

### The Underlying Driver

**What she needs:** Validation that she's the better candidate. Your success threatens her self-image.

**Why this manifests as it does:** Direct competition would expose her insecurity and make her look petty. Covert undermining lets her maintain the "nice colleague" persona while damaging you. The envy is invisible to observers.

**The origin (if inferable):** She likely measures her self-worth through comparison. Your presence as a genuine competitor has activated a wound around being "not enough."

---

### Prediction

Given this pattern, expect:

- **In conflict:** She will deny any problem exists. "I thought we were friends?" She'll make YOU look unreasonable for noticing.
- **Under pressure:** The undermining will intensify as the promotion decision approaches. Watch for "helpful suggestions" that actually highlight your weaknesses.
- **When successful:** If she gets the promotion, expect magnanimous public gestures (she can afford to be generous when she's won).
- **Her blind spot:** She genuinely believes her behavior is justified—you probably did something to "deserve" it in her mind.

---

### Approach Strategy

**Do:**
- Document everything in writing (create your own paper trail)
- Praise her publicly and specifically (starves the envy of fuel)
- Make your accomplishments visible to the boss directly, not through her
- Build alliances with other colleagues so her narrative isn't the only one

**Avoid:**
- Confronting her directly (she'll deny and you'll look paranoid)
- Complaining to your boss without documentation (appears political)
- Reducing contact entirely (she'll notice and escalate)

**The key to this person:** She needs to feel she's winning. Give her symbolic victories (credit, acknowledgment) while securing the substantive wins for yourself.

---

### Warning Signs

Watch for these indicators that the pattern is escalating:
- She starts "forgetting" to include you on relevant emails
- Your ideas start appearing as hers in meetings
- She volunteers to "help" with your projects (to gain access)

**When to disengage:** If the undermining continues despite your adjustments, you may need to escalate to your boss with documentation or seek transfer. Some enviers cannot be managed—only escaped.

---

### Self-Check

Before accepting this diagnosis, consider:

- **Am I projecting?** Is there any chance YOU feel competitive and are reading hostility into neutral behavior?
- **Alternative explanation:** Could she be socially awkward, conflict-avoidant, or just disorganized rather than malicious?
- **Confirmation bias:** Have you noticed times she was genuinely supportive? Are you discounting those?

---

### Reversal

**This diagnosis may be wrong if:**
- She behaves the same way with everyone, not specifically you
- Her non-compliance is consistent across all commitments (simple unreliability)
- Other colleagues see her as straightforward and you as difficult

**The humility clause:** Workplace dynamics are complex. Her behavior could stem from stress, different work styles, or miscommunication rather than envy. Proceed as if the diagnosis is a working hypothesis—test it against future observations before committing to this frame.

---

## Integration

This skill is associated with the **robert-greene** expert. When invoked, the expert should provide psychological diagnosis with Greene's characteristic precision—naming patterns clearly, drawing on historical parallels where useful, and maintaining the unflinching realism about human nature that defines his work.

---

## Success Criteria

Psychological diagnosis is complete when:

- [ ] Behavioral evidence is specific, not assumed
- [ ] Primary pattern is identified and named
- [ ] Underlying driver explains the mechanism
- [ ] Predictions are testable against future behavior
- [ ] Approach strategy provides actionable tactics
- [ ] Warning signs help the user monitor escalation
- [ ] Self-check prevents user projection
- [ ] Reversal acknowledges alternative explanations