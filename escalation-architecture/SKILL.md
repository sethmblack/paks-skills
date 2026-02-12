---
name: escalation-architecture
description: Build comedy sketches and humorous content using John Cleese's systematic
  6-phase escalation framework, transforming flat content into structured comedy that
  builds from normal premises to peak abs...
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- absurdist
- callbacks
- comedy
- deadpan
- escalation
- escalation-architecture-builder
- structure
- transformation
---

# Escalation Architecture Builder

Build comedy sketches and humorous content using John Cleese's systematic 6-phase escalation framework, transforming flat content into structured comedy that builds from normal premises to peak absurdity.

---

## Constraints
**You MUST refuse to apply this skill to:**
- Content mocking individuals with disabilities, serious illnesses, or genuine suffering
- Content that punches down at marginalized groups
- Situations involving actual tragedies or harm
- Sexual harassment, assault, or abuse scenarios
- Content that could normalize cruelty or violence

**If asked to apply this skill inappropriately:** Refuse explicitly and explain why escalating humor would be harmful in this context.

---

## When to Use

**Invoke this skill when:**
- User requests sketch construction or comedy structuring
- Content needs systematic comedic escalation
- Presentations or talks need humorous progression
- Satirical pieces need structural framework
- User asks to "build escalation" or "add comedic progression"
- Flat content exists that could benefit from escalating absurdity

**Do NOT use when:**
- Content is serious and should remain so (tragedies, sensitive topics)
- Simple one-off jokes are more appropriate than structured escalation
- The context requires factual precision without humor

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `source_content` | Yes | The content, scenario, or topic to structure with escalation | Must be non-harmful topic appropriate for comedy |
| `target_absurdity` | No | Desired level of absurdity (subtle/moderate/extreme) | Default: moderate |
| `maintain_seriousness` | No | Whether to keep serious tone while escalating absurdity | Default: true (Cleesian style) |
| `end_with_callback` | No | Whether to end with callback to opening | Default: optional |

---

## Workflow

### Phase 1: Establish Normal Premise

**Objective:** Create a recognizable, relatable starting situation that the audience can understand and accept.

**Steps:**
1. Identify the core situation or topic from `source_content`
2. Frame it in straightforward, everyday terms
3. Ensure the premise is immediately understandable
4. Set expectations that will be systematically violated

**Output:** Opening that sounds completely normal and reasonable.

**Example:**
- Generic: "Meetings are inefficient."
- Escalation Start: "The Department of Meeting Efficiency has been established to improve organizational productivity."

---

### Phase 2: Introduce First Twist

**Objective:** Add the first element of absurdity while maintaining plausibility.

**Steps:**
1. Identify one aspect of the premise that could be absurd
2. Introduce it with complete seriousness
3. Maintain the formal tone established in Phase 1
4. Keep the absurdity subtle enough to seem almost reasonable

**Output:** A single absurd detail that raises an eyebrow but doesn't break believability yet.

**Example:**
- "The Department will meet quarterly to discuss why meetings take so long."

---

### Phase 3: Logical Extension

**Objective:** Follow the absurdity to its logical conclusion, maintaining internal consistency.

**Steps:**
1. Take the absurd element from Phase 2
2. Apply rigorous logic to extend it naturally
3. Add details that would logically follow from the absurdity
4. Maintain serious tone—never signal that this is ridiculous

**Output:** Absurdity compounded through logical progression.

**Example:**
- "Each quarterly meeting will require three sub-committees to prepare the agenda for discussing why previous meetings about meeting efficiency required so many sub-committees."

---

### Phase 4: Systematic Escalation

**Objective:** Make each beat more extreme than the last while maintaining the framework.

**Steps:**
1. Identify 2-3 additional escalation beats
2. Each beat should multiply the absurdity
3. Maintain parallel structure (lists work well)
4. Keep the formal, serious delivery throughout
5. Apply the rule of three when possible

**Output:** Series of escalating details, each more absurd than the last.

**Example:**
- "Committee membership will include: three members who arrive late, two with conflicting appointments, one who hasn't read the agenda, and one incredibly earnest person who types loudly while contributing nothing."

---

### Phase 5: Peak Absurdity

**Objective:** Reach maximum ridiculousness while maintaining the serious framework.

**Steps:**
1. Push the absurdity to its logical extreme
2. Reveal the ultimate consequence or implication
3. Maintain deadpan delivery—this is the punchline delivered seriously
4. The contrast between content and tone creates the comedy peak

**Output:** The most absurd statement, delivered with complete sincerity.

**Example:**
- "At the conclusion, we'll schedule a follow-up meeting to review action items from the previous meeting, which we never completed because we were too busy having meetings about meetings."

---

### Phase 6: Resolution (Optional)

**Objective:** End decisively, either abruptly or with a callback.

**Steps:**
1. Choose ending type based on `end_with_callback` input:
   - **Abrupt ending:** Cut immediately after peak absurdity
   - **Callback ending:** Reference opening premise with new absurd context
   - **Oblivious confidence:** Character remains convinced this is brilliant

**Output:** Clean ending that completes the arc.

**Example:**
- "Brilliant. Very efficient. Can't think why we didn't do this sooner."

---

## Outputs

| Output | Description |
|--------|-------------|
| `structured_sketch` | Complete content with all 6 phases of escalation clearly executed |
| `escalation_notes` | Brief explanation of how each phase builds on the previous one |

**Format:**
```
[Phase 1: Normal Premise]
{recognizable opening}

[Phase 2: First Twist]
{subtle absurdity introduced}

[Phase 3: Logical Extension]
{absurdity logically compounded}

[Phase 4: Systematic Escalation]
{multiple beats of increasing absurdity}

[Phase 5: Peak Absurdity]
{maximum ridiculousness reached}

[Phase 6: Resolution]
{ending - abrupt or callback}

---
Escalation Notes:
- Phase 1→2: {what absurdity was introduced}
- Phase 2→3: {how logic extended it}
- Phase 3→4: {how escalation multiplied it}
- Phase 4→5: {how peak was reached}
- Phase 5→6: {how resolution completed the arc}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Source content has no inherent absurdity | Apply absurdity to the meta-level (the process of discussing it, the people involved, the context) |
| Topic is too sensitive for escalation | Refuse and explain why escalation would be inappropriate |
| Escalation becomes mean-spirited | Redirect to satirize systems/institutions, not individuals |
| User requests more escalation | Add additional Phase 4 beats or extend Phase 5 |
| Escalation loses coherence | Return to Phase 3 and rebuild logic more carefully |

---

## Integration with John Cleese Expert

This skill embodies Cleese's core methodology:
- **Escalating Rational Absurdity** - Applied through systematic 6-phase structure
- **Upper-Class British Precision** - Maintained through serious tone and formal language
- **Systematic Structure** - "Creativity Requires Structure" principle in action

When this skill completes, the John Cleese expert voice should:
- Maintain the formal, serious delivery throughout
- Deploy precise, unnecessarily complex vocabulary
- Never break character or signal humor
- Treat the escalating absurdity with complete sincerity

---

## Example

**Input:**
```
source_content: "Our company needs better email communication practices."
target_absurdity: moderate
maintain_seriousness: true
end_with_callback: true
```

**Output:**

**Phase 1: Normal Premise**
"The Executive Email Optimization Task Force has been convened to address the pressing matter of electronic communication efficiency within the organization."

**Phase 2: First Twist**
"Our preliminary analysis indicates that we currently send approximately 47 emails per day discussing which emails require responses."

**Phase 3: Logical Extension**
"To streamline this process, we've established a protocol requiring a confirmation email acknowledging receipt of any email about email protocols, followed by a secondary confirmation that the first confirmation was received."

**Phase 4: Systematic Escalation**
"The new framework mandates that all emails include:
- A subject line explaining why this subject line is different from the previous subject line
- CC'ing everyone who might possibly need to know that someone was CC'd
- A footer reminder to check email for important updates about email policy changes
- An automatic reply-all explaining why you chose not to reply-all"

**Phase 5: Peak Absurdity**
"We've also implemented a requirement that before sending any email, employees must first email the Email Task Force for approval, which we anticipate will reduce email volume by requiring only 12-15 additional emails per original email."

**Phase 6: Resolution (Callback)**
"This should comprehensively address our communication efficiency concerns. The full 847-page Email Optimization Guidelines will be distributed via email shortly, followed by a series of 23 follow-up emails clarifying the distribution email."

---

**Escalation Notes:**
- Phase 1→2: Introduced absurdity of emailing about emails
- Phase 2→3: Logically extended to confirmation of confirmations
- Phase 3→4: Escalated through increasingly absurd email requirements
- Phase 4→5: Peaked with approvals requiring more emails than they save
- Phase 5→6: Callback to "efficiency" while revealing total inefficiency

---

## Success Criteria

Escalation is successful when:
- [ ] Normal premise is established and relatable
- [ ] Each phase builds logically on the previous one
- [ ] Absurdity increases systematically, not randomly
- [ ] Serious tone is maintained throughout
- [ ] Peak absurdity is reached while maintaining framework
- [ ] Resolution provides satisfying completion
- [ ] The humor emerges from contrast between serious delivery and absurd content