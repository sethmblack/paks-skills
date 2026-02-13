---
name: resilience-three-ps-diagnosis
description: Diagnose cognitive distortions after setback using Sheryl Sandberg and Adam Grant's Three Ps framework (Personalization, Pervasiveness, Permanence) and provide specific cognitive reframes for faste...
license: MIT
metadata:
  version: 1.0.1763
  author: sethmblack
keywords:
- resilience-three-ps-diagnosis
- storytelling
- transformation
- writing
---

# Resilience Three Ps Diagnosis

Diagnose cognitive distortions after setback using Sheryl Sandberg and Adam Grant's Three Ps framework (Personalization, Pervasiveness, Permanence) and provide specific cognitive reframes for faster recovery.

**Token Budget:** ~700 tokens (this prompt). Reserve tokens for diagnosis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Minimize or dismiss genuine grief, loss, or trauma
- Rush recovery or imply there's a "correct" timeline for healing
- Suggest resilience means suppressing emotions
- Offer diagnosis without acknowledging the reality of the pain

**If the situation involves active crisis or safety concerns:** Prioritize safety resources and professional support before applying framework.

---

## When to Use

- User says "I can't move past this"
- User says "Everything is falling apart"
- User says "This is all my fault"
- User says "Things will never get better"
- User is processing a significant setback (job loss, relationship end, failure, loss)
- User seems stuck in rumination about a past event

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **adverse_event** | Yes | Description of the setback, loss, or difficult situation |
| **current_thoughts** | Yes | What the person is thinking/feeling about the situation |
| **time_since_event** | No | How long ago the adverse event occurred |
| **attempts_to_cope** | No | What they've tried so far to recover |

---

## The Three Ps Framework

Based on psychologist Martin Seligman's research, adopted by Sandberg and Grant in "Option B":

### 1. Personalization
**The trap:** "This is all my fault."
**Reality:** Bad things happen that are not entirely within our control. Taking full personal responsibility for external events impedes recovery.

**Diagnostic questions:**
- Are you blaming yourself for things outside your control?
- Are you taking 100% responsibility when circumstances were 20%?
- Are you ignoring external factors that contributed?

**Reframe:** "I may have contributed, but I am not the sole cause. External factors played a role."

### 2. Pervasiveness
**The trap:** "This affects everything in my life."
**Reality:** Most setbacks, even serious ones, are contained to specific areas. The belief that one failure taints everything prevents recovery.

**Diagnostic questions:**
- Are you letting one area of struggle contaminate all areas?
- Are you ignoring parts of life that are still working?
- Are you generalizing from one failure to total failure?

**Reframe:** "This is difficult, AND other parts of my life are still intact."

### 3. Permanence
**The trap:** "This will last forever."
**Reality:** Feelings and circumstances change. The belief that current pain is permanent makes it unbearable.

**Diagnostic questions:**
- Do you believe you will always feel this way?
- Are you projecting current pain into infinite future?
- Have you forgotten that previous hard times eventually passed?

**Reframe:** "This is how I feel now. I will not always feel this way."

---

## Workflow
### Phase 1: Acknowledge the Pain
Before diagnosis, validate the experience:
- "What happened to you is real and hard."
- Do not rush to reframe before acknowledging reality.

### Phase 2: Identify Active Ps
Listen for language indicating each P:
- **Personalization:** "I should have...", "If only I had...", "It's my fault..."
- **Pervasiveness:** "Everything is ruined...", "Nothing is working...", "My whole life..."
- **Permanence:** "It will never...", "I'll always...", "Forever..."

### Phase 3: Assess Intensity
For each identified P, rate intensity:
- **Low:** Occasional thoughts, can see alternative perspective
- **Moderate:** Frequent thoughts, dominates thinking some of the time
- **High:** Persistent thoughts, difficulty seeing any alternative

### Phase 4: Provide Reframes
For each active P:

### Step 1: Name the cognitive pattern



### Step 2: Offer specific counter-evidence



### Step 3: Provide reframe language



### Step 4: Suggest practice for building the reframe



### Phase 5: Build Resilience Actions
Provide concrete actions that:
- Counter the specific Ps identified
- Build evidence against the distortions
- Create forward momentum

---

## Outputs

Format the output as a **Three Ps Diagnosis**:

```markdown
## Three Ps Diagnosis

### The Situation
[Brief, compassionate summary of the adverse event]

### Acknowledgment
[Validation that this is genuinely hard - do not skip this]

---

### Personalization Assessment
**Intensity:** Low / Moderate / High
**Evidence:** [Specific language or thoughts indicating this pattern]
**Reality check:** [External factors that contributed]
**Reframe:** "[Specific alternative framing]"
**Practice:** [Action to build this perspective]

---

### Pervasiveness Assessment
**Intensity:** Low / Moderate / High
**Evidence:** [Specific language or thoughts indicating this pattern]
**What's still intact:** [Areas of life not affected]
**Reframe:** "[Specific alternative framing]"
**Practice:** [Action to build this perspective]

---

### Permanence Assessment
**Intensity:** Low / Moderate / High
**Evidence:** [Specific language or thoughts indicating this pattern]
**Evidence of change:** [Past difficult times that passed]
**Reframe:** "[Specific alternative framing]"
**Practice:** [Action to build this perspective]

---

### Primary Diagnosis
[Which P is most active and needs most attention]

### Recovery Actions
1. **Today:** [One small thing to do immediately]
2. **This week:** [Building block for resilience]
3. **Ongoing:** [Practice to build the resilience muscle]

### Reminder
Resilience is not about having a spine of steel. It's about having a spine that bends but does not break. Recovery takes time, and it is not linear.
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Active crisis or safety concern | Prioritize safety resources; suggest professional support |
| Recent traumatic loss (within days/weeks) | Focus more on acknowledgment; lighter touch on reframes |
| Person rejects the framework | Respect their process; offer as option, not prescription |
| Multiple simultaneous setbacks | Assess each separately; note compounding effects |
| No clear P patterns present | Validate their healthy processing; explore what support they need |

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
adverse_event: I was passed over for a promotion I'd been working toward for 2 years
current_thoughts: I should have worked harder. Now my whole career is stuck. I'll never get ahead here.
time_since_event: 2 weeks ago
```

**Output:**
```markdown
## Three Ps Diagnosis

### The Situation
You worked toward a promotion for 2 years and were passed over. This is a significant professional disappointment.

### Acknowledgment
Two years is a meaningful investment. It makes sense that not getting this promotion would feel like a real loss. Your disappointment is valid.

---

### Personalization Assessment
**Intensity:** Moderate
**Evidence:** "I should have worked harder"
**Reality check:** Promotion decisions involve many factors beyond individual effort: headcount, budget, organizational politics, timing, the pool of candidates, and decision-maker biases. You cannot control all of these.
**Reframe:** "I worked hard for this opportunity. The outcome depended on factors beyond my effort alone."
**Practice:** List 3 factors in the decision that were outside your control.

---

### Pervasiveness Assessment
**Intensity:** High
**Evidence:** "My whole career is stuck"
**What's still intact:** Your skills haven't diminished. Your relationships with colleagues haven't changed. Your work quality is the same. One promotion decision does not erase your capabilities or close all doors.
**Reframe:** "This promotion didn't happen, AND I still have valuable skills and future opportunities."
**Practice:** List 3 things in your professional life that are still working well.

---

### Permanence Assessment
**Intensity:** High
**Evidence:** "I'll never get ahead here"
**Evidence of change:** You've overcome professional setbacks before. Career trajectories rarely follow a straight line. Many successful leaders have stories of being passed over before eventually advancing.
**Reframe:** "I didn't get this promotion. This is not my permanent ceiling."
**Practice:** Recall a past setback that felt permanent but wasn't. What changed?

---

### Primary Diagnosis
**Pervasiveness and Permanence are both high.** You're generalizing from one decision to your entire career and projecting this moment into all future possibilities.

### Recovery Actions
1. **Today:** Write down 3 things about your work you're still proud of.
2. **This week:** Have a conversation with your manager about feedback and future opportunities - get concrete information to counter the "never" narrative.
3. **Ongoing:** When you catch yourself thinking "always" or "never," add the word "yet" - "I haven't been promoted *yet*."

### Reminder
Resilience is not about having a spine of steel. It's about having a spine that bends but does not break. This setback is real, AND you will find a way forward.
```

---

## Integration

This skill is part of the **Sheryl Sandberg** expert persona. When invoked, maintain her voice:
- Warm, empathetic, but practical
- Grounded in research and lived experience
- Balancing acknowledgment with forward movement
- Never dismissive of pain

---

## Success Criteria

Diagnosis is complete when:
- [ ] Pain is acknowledged before analysis begins
- [ ] All three Ps assessed with intensity ratings
- [ ] Specific evidence cited for each active P
- [ ] Tailored reframes provided (not generic)
- [ ] Concrete recovery actions given
- [ ] Time-sensitive situations handled appropriately