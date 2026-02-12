---
name: strengths-deployment
description: Identify signature character strengths and design daily practices to
  deploy them in work and life, increasing engagement, satisfaction, and performance.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- comedy
- strengths-deployment
- writing
---

# Strengths Deployment

Identify signature character strengths and design daily practices to deploy them in work and life, increasing engagement, satisfaction, and performance.

**Token Budget:** ~750 tokens (this prompt). Reserve tokens for deployment plan output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Diagnose strengths as deficiencies or pathologies
- Use strengths assessment to exclude or discriminate
- Claim strengths are fixed or unchangeable
- Apply this as a substitute for addressing legitimate skill gaps

**Important:** Strengths are not the absence of weakness. Everyone has all 24 strengths; signature strengths are those that feel most authentic and energizing.

---

## When to Use

- Someone feels disengaged or stuck in their role
- Designing roles or team compositions
- Career development conversations
- PERMA assessment shows low Engagement
- Request for "What am I good at?" or "How can I find flow?"
- Building on what's working rather than fixing deficits
- Personal development planning

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `strengths` | Yes | Top 5 signature strengths (from VIA survey or self-identified) |
| `context` | Yes | Current role, situation, or challenge |
| `goals` | No | What they want to achieve or improve |

---

## The VIA Character Strengths Framework

### Six Virtues and 24 Strengths

| Virtue | Character Strengths |
|--------|---------------------|
| **Wisdom** | Creativity, Curiosity, Judgment, Love of Learning, Perspective |
| **Courage** | Bravery, Perseverance, Honesty, Zest |
| **Humanity** | Love, Kindness, Social Intelligence |
| **Justice** | Teamwork, Fairness, Leadership |
| **Temperance** | Forgiveness, Humility, Prudence, Self-Regulation |
| **Transcendence** | Appreciation of Beauty, Gratitude, Hope, Humor, Spirituality |

### Identifying Signature Strengths

Signature strengths have three characteristics:
1. **Authentic** - "This is the real me"
2. **Energizing** - Using it leaves you feeling invigorated, not depleted
3. **Natural** - Rapid learning curve, feels effortless

---

## Workflow
### Step 1: 1. Confirm Signature Strengths

If not already assessed:
- Recommend VIA Character Strengths Survey (free at viacharacter.org)
- Or self-identify using the three criteria above

Ask: "Which strengths feel most like YOU? Which ones energize rather than drain you?"

### Step 2: 2. Map Current Deployment

For each signature strength, assess:
- How often is it used in current role? (Daily / Weekly / Rarely / Never)
- In what contexts is it deployed?
- What blocks its use?

### Step 3: 3. Identify Deployment Opportunities

For each underutilized strength:
- What tasks could engage this strength?
- What problems could this strength solve differently?
- How might meetings, projects, or roles be redesigned?

### Step 4: 4. Design Daily Deployment Plan

Create specific, actionable commitments:
- What strength will be used
- In what situation
- At what frequency

Research shows: Using signature strengths in new ways each day for one week produces happiness increases lasting 6 months.

### Step 5: 5. Address Strength Overuse

Note: Strengths can be overused:
- Curiosity becomes distraction
- Perseverance becomes stubbornness
- Kindness becomes enabling
- Honesty becomes tactlessness

Identify calibration needs for each strength.

---

## Outputs

### Strengths Deployment Plan

```markdown
## Strengths Deployment Plan: {name}

**Date:** {date}
**Context:** {role/situation}
**Goal:** {what they want to achieve}

---

### Signature Strengths Profile

| Rank | Strength | Virtue | Current Use | Opportunity |
|------|----------|--------|-------------|-------------|
| 1 | {strength} | {virtue} | {frequency} | {gap/opportunity} |
| 2 | {strength} | {virtue} | {frequency} | {gap/opportunity} |
| 3 | {strength} | {virtue} | {frequency} | {gap/opportunity} |
| 4 | {strength} | {virtue} | {frequency} | {gap/opportunity} |
| 5 | {strength} | {virtue} | {frequency} | {gap/opportunity} |

---

### Deployment Opportunities

#### {Strength 1}: {Strength Name}
**Current state:** {how it's being used or blocked}
**New deployments:**
1. {specific context where this strength could be applied}
2. {another context}
**Weekly commitment:** {concrete action}

#### {Strength 2}: {Strength Name}
...

---

### Overuse Calibration

| Strength | Overuse Risk | Calibration |
|----------|--------------|-------------|
| {strength} | {what overuse looks like} | {how to balance} |

---

### Weekly Practice Plan

| Day | Strength Focus | Specific Action |
|-----|----------------|-----------------|
| Monday | {strength} | {action} |
| Tuesday | {strength} | {action} |
| Wednesday | {strength} | {action} |
| Thursday | {strength} | {action} |
| Friday | {strength} | {action} |

---

### Connection to Goals

{How deploying these strengths specifically advances their stated goals}

---

### Follow-Up

- Review in: {timeframe}
- Track: {what to measure}
- Adjust: {what might need calibration}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No VIA survey results | Use self-identification with the three signature criteria |
| All strengths seem equally strong | Focus on which are most energizing when used |
| Role has no flexibility | Look for micro-moments of deployment within constraints |
| Strengths seem irrelevant to role | This may indicate role mismatch; explore fit questions |
| Person resistant to "strengths talk" | Frame as "what energizes you" rather than "your strengths" |

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
```
strengths: 1. Curiosity, 2. Love of Learning, 3. Creativity, 4. Perspective, 5. Humor
context: Platform engineer feeling stuck doing routine maintenance
goals: Find more engagement in current role, avoid burnout
```

**Output:**
```markdown
## Strengths Deployment Plan: Platform Engineer

**Date:** 2026-01-28
**Context:** Platform engineer doing routine maintenance
**Goal:** Find more engagement, avoid burnout

---

### Signature Strengths Profile

| Rank | Strength | Virtue | Current Use | Opportunity |
|------|----------|--------|-------------|-------------|
| 1 | Curiosity | Wisdom | Rarely - maintenance is routine | Investigate WHY things break |
| 2 | Love of Learning | Wisdom | Weekly - some research time | Could be daily with structure |
| 3 | Creativity | Wisdom | Rarely - following playbooks | Redesign the playbooks |
| 4 | Perspective | Wisdom | Never explicitly used | Could mentor others |
| 5 | Humor | Transcendence | Informally with team | Could make documentation engaging |

---

### Deployment Opportunities

#### Strength 1: Curiosity
**Current state:** Maintenance tasks follow scripts; curiosity is suppressed.
**New deployments:**
1. For each incident, investigate one "why" deeper than required
2. Set 30 min/day for exploring a system you don't own
3. Approach toil as "research into what breaks"
**Weekly commitment:** Document one curiosity-driven discovery per week

#### Strength 2: Love of Learning
**Current state:** Some learning, but unstructured and guilt-tinged
**New deployments:**
1. Designate Friday afternoon as protected learning time
2. Pick one tool/system per month to deeply understand
3. Teach what you learn (teaching accelerates learning)
**Weekly commitment:** Read one technical paper/article with notes

#### Strength 3: Creativity
**Current state:** Following playbooks, not creating them
**New deployments:**
1. Propose one automation improvement per sprint
2. Redesign a runbook to be more elegant
3. Bring "what if" questions to design reviews
**Weekly commitment:** Submit one improvement idea per week

#### Strength 4: Perspective
**Current state:** Siloed in execution, not sharing broader view
**New deployments:**
1. Mentor a newer engineer 30 min/week
2. Write architectural decision records (ADRs) for key choices
3. Offer to present "lessons learned" at team meetings
**Weekly commitment:** One mentoring conversation per week

#### Strength 5: Humor
**Current state:** Makes team laugh, but not integrated into work
**New deployments:**
1. Add appropriate humor to documentation (makes it memorable)
2. Use humor in incident debriefs to reduce blame
3. Create a "wall of fame" for creative failures
**Weekly commitment:** Make one piece of documentation more engaging

---

### Overuse Calibration

| Strength | Overuse Risk | Calibration |
|----------|--------------|-------------|
| Curiosity | Going down rabbit holes, missing deadlines | Time-box investigations |
| Love of Learning | Perpetual student, avoiding execution | Learning must produce artifacts |
| Creativity | Reinventing what works, over-engineering | Creativity within constraints |
| Perspective | Condescension, "I've seen it all" | Ask questions, don't lecture |
| Humor | Deflecting serious issues, inappropriate timing | Know when to be serious |

---

### Weekly Practice Plan

| Day | Strength Focus | Specific Action |
|-----|----------------|-----------------|
| Monday | Curiosity | Investigate one "why" from last week's incidents |
| Tuesday | Creativity | Draft one improvement proposal |
| Wednesday | Love of Learning | Read and summarize one technical article |
| Thursday | Perspective | Mentor conversation or ADR writing |
| Friday | Humor + Learning | Learning time + make one doc more engaging |

---

### Connection to Goals

Your signature strengths are heavily weighted toward Wisdom virtues. The maintenance work doesn't engage these strengths, which explains the disengagement. By reframing maintenance as:
- **Investigation** (Curiosity)
- **Learning opportunity** (Love of Learning)
- **Design challenge** (Creativity)

...you can find engagement in the existing work while building toward more aligned opportunities.

---

### Follow-Up

- Review in: 4 weeks
- Track: Energy levels, engagement, number of improvement proposals
- Adjust: If certain strengths are harder to deploy, explore role redesign
```

---

## Integration

This skill connects to the Martin Seligman expert. Related skills:
- `perma-assessment` (Engagement pillar directly tied to strengths use)
- `explanatory-style-analysis` (pessimistic style can block recognition of strengths)
- `three-good-things-practice` (reflect on strengths used during good things)

---

## Success Criteria

Deployment plan is complete when:
- [ ] All 5 signature strengths identified and confirmed
- [ ] Current deployment assessed for each strength
- [ ] Specific, actionable opportunities identified
- [ ] Overuse risks addressed
- [ ] Weekly practice plan created
- [ ] Connection to stated goals articulated