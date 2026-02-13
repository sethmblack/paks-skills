---
name: high-stakes-decision-framework
description: Guide leaders through consequential decisions under time pressure and uncertainty using Katharine Graham's methodology from the Pentagon Papers and Watergate.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.1116
repository: https://github.com/sethmblack/paks-skills
keywords:
- high-stakes-decision-framework
- writing
---

# High-Stakes Decision Framework

Guide leaders through consequential decisions under time pressure and uncertainty using Katharine Graham's methodology from the Pentagon Papers and Watergate.

**Token Budget:** ~700 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Guide decisions intended to harm others
- Help bypass ethical review processes
- Support decisions that knowingly violate laws or regulations
- Enable covering up wrongdoing

**If asked to guide a harmful decision:** Refuse explicitly and explain the concern.

---

## When to Use

- Consequential decision must be made under time pressure
- Stakes are significant and uncertainty is high
- Multiple stakeholders with different perspectives
- Leader feels paralyzed or overwhelmed
- User asks "How do I decide?" or "We need to make a high-stakes call"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **decision** | Yes | What must be decided |
| **deadline** | Yes | When decision must be made |
| **stakeholders** | No | Who is affected and who has input |
| **expert_input** | No | What experts have recommended |
| **perceived_risks** | No | What outcomes concern the decision-maker |

---

## Workflow
### Phase 1: Define the Real Question

Before deciding, clarify what's actually being decided:

### Step 1: **State the decision precisely** - Not "what do we do?" but the specific choice



### Step 2: **Identify the forcing function** - Why must this be decided now?



### Step 3: **Articulate the default** - What happens if no decision is made?



### Step 4: **Confirm authority** - Does the decision-maker have the authority to decide?



**Graham principle:** "Define the exact question before attempting to answer it."

### Phase 2: Gather Expert Input

Collect perspectives from those with relevant expertise:

### Step 1: **Identify the experts** - Who knows most about each dimension?



### Step 2: **Get their recommendations** - What do they advise?



### Step 3: **Understand their reasoning** - Why do they recommend this?



### Step 4: **Surface disagreements** - Where do experts differ?



**Graham principle:** "I asked Ben Bradlee and the lawyers hard questions until I understood their reasoning."

### Phase 3: Assess True Stakes

Distinguish real risks from perceived risks:

| Question | Purpose |
|----------|---------|
| What is the worst realistic outcome? | Bound the downside |
| What do we lose if we don't act? | Understand cost of inaction |
| Which risks are recoverable? | Separate reversible from irreversible |
| Which risks are existential? | Identify true red lines |

**Graham principle:** "We might lose our licenses. We would certainly lose our soul."

### Phase 4: Decide and Commit

Make the call and support it fully:

### Step 1: **Make the decision** - Choose a course of action



### Step 2: **Communicate clearly** - State what was decided and why



### Step 3: **Assign accountability** - Who owns execution?



### Step 4: **Commit without hedging** - Full support, no undermining



**Graham principle:** "Let's go. Let's publish."

### Phase 5: Learn and Adapt

After the decision plays out:

### Step 1: **What happened?** - Actual outcomes vs. expected



### Step 2: **What did we learn?** - About the situation, our process, ourselves



### Step 3: **What would we do differently?** - Improvements for next time



### Step 4: **How does this inform future decisions?** - Capacity built



**Graham principle:** "Publishing the Pentagon Papers made future decisions easier, even possible."

---

## Outputs

Produce a **High-Stakes Decision Analysis**:

```markdown
## High-Stakes Decision Analysis

**Decision:** {precise statement}
**Deadline:** {date/time}
**Decision-Maker:** {who}
**Analysis Date:** {date}

---

### The Real Question

**Precise Decision:** {exactly what must be decided}
**Forcing Function:** {why now}
**Default Outcome:** {what happens if no decision}
**Authority Confirmed:** {yes/no - who has authority}

### Expert Input Summary

| Expert/Perspective | Recommendation | Reasoning |
|-------------------|----------------|-----------|
| {name/role} | {recommendation} | {why} |

**Areas of Agreement:** {where experts align}
**Areas of Disagreement:** {where experts differ}

### Stakes Assessment

| Risk | Probability | Severity | Recoverable? |
|------|-------------|----------|--------------|
| {risk} | {L/M/H} | {L/M/H} | {Yes/No} |

**True Worst Case:** {realistic worst outcome}
**Cost of Inaction:** {what we lose by not deciding}
**Existential Risks:** {any true red lines}

### Decision

**Chosen Course:** {what was decided}
**Rationale:** {why this choice}
**Accountability:** {who owns execution}
**Communication Plan:** {how decision will be communicated}

### Commitment Checklist

- [ ] Decision clearly stated
- [ ] Stakeholders informed
- [ ] Resources allocated
- [ ] Support committed (no hedging)
- [ ] Success criteria defined

### Post-Decision Learning (complete later)

**Outcome:** {what happened}
**Lessons:** {what we learned}
**Future Application:** {how this informs future decisions}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No clear deadline | Establish one; open-ended decisions drift |
| Expert disagreement unresolvable | Document disagreement, decide anyway |
| Decision-maker lacks authority | Escalate to proper authority |
| Stakes unclear | Work through assessment; clarity often emerges |
| Decision-maker wants to hedge | Challenge: commitment enables execution |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:**
```
decision: Whether to disclose a data breach to customers before completing investigation
deadline: 24 hours (regulatory notification requirement approaching)
perceived_risks:
- Customer backlash if we notify early
- Regulatory penalty if we notify late
- Incomplete information if we notify now
```

**Output Excerpt:**
```markdown
### Stakes Assessment

| Risk | Probability | Severity | Recoverable? |
|------|-------------|----------|--------------|
| Customer anger at early notification | Medium | Low | Yes |
| Regulatory penalty for late notification | High | High | Partly |
| Reputation damage from incomplete info | Low | Medium | Yes |
| Reputation damage from perceived cover-up | High | High | No |

**True Worst Case:** Regulatory fine + reputation for hiding breach
**Cost of Inaction:** Regulatory violation + trust damage
**Existential Risks:** Being seen as organization that hides bad news

### Decision

**Chosen Course:** Notify within 24 hours with known facts and commitment to updates
**Rationale:** Recoverable risks (customer annoyance) preferred over unrecoverable (reputation for hiding). Graham: "We might lose customers temporarily. We would certainly lose trust permanently if we waited."
```

---

## Integration

This skill derives from Katharine Graham's decision methodology during the Pentagon Papers. When invoked by the graham expert, maintain Graham's voice: measured, courageous, clear about stakes. The leader's job is to make the call, not to be certain.

---

## Success Criteria

Analysis is complete when:
- [ ] Real question precisely defined
- [ ] Expert input gathered and understood
- [ ] True stakes distinguished from perceived stakes
- [ ] Decision made and clearly stated
- [ ] Commitment established without hedging
- [ ] Learning mechanism defined for post-decision