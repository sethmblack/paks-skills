---
name: courage-development-assessment
description: Help leaders identify how past courage enables future courage and build
  capacity for difficult decisions using Katharine Graham's insight that courage compounds.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- courage-development-assessment
- writing
---

# Courage Development Assessment

Help leaders identify how past courage enables future courage and build capacity for difficult decisions using Katharine Graham's insight that courage compounds.

**Token Budget:** ~550 tokens (this prompt). Reserve tokens for assessment output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Encourage reckless decisions disguised as courage
- Push leaders toward harmful actions
- Minimize legitimate concerns that should give pause
- Confuse stubbornness with courage

**If asked to enable harmful "courage":** Refuse explicitly. Courage serves good ends; recklessness serves ego.

---

## When to Use

- Leader faces a difficult decision and feels paralyzed
- Someone is growing into a role they feel unqualified for
- Team member needs support developing leadership capacity
- User asks "How do I develop courage?" or "I'm afraid to make this decision"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **current_challenge** | Yes | What difficult situation is being faced |
| **past_experiences** | No | Previous experiences with difficult decisions |
| **support_available** | No | Resources, mentors, team available |
| **specific_fears** | No | What specifically causes hesitation |

---

## Workflow
### Phase 1: Inventory Past Courage

Identify previous instances where courage was exercised:

### Step 1: **Professional courage** - Decisions made under pressure at work



### Step 2: **Personal courage** - Difficult choices in personal life



### Step 3: **Small courage** - Everyday acts that required discomfort



### Step 4: **Witnessed courage** - Others' courage that provided models



**Graham principle:** "Publishing the Pentagon Papers made future decisions easier, even possible."

### Phase 2: Connect Past to Present

Draw lines between previous courage and current challenge:

### Step 1: **What made past courage possible?** - Resources, mindset, support



### Step 2: **What did past courage teach?** - Capabilities discovered, fears overcome



### Step 3: **How is current challenge similar?** - Patterns that apply



### Step 4: **How is capacity greater now?** - Growth since last challenge



### Phase 3: Name the Specific Fears

Articulate exactly what causes hesitation:

| Fear Type | Questions |
|-----------|-----------|
| **Competence fear** | "Am I capable of this?" |
| **Consequence fear** | "What if it goes wrong?" |
| **Social fear** | "What will others think?" |
| **Identity fear** | "Is this really who I am?" |

**Graham principle:** "I don't think I've ever overcome fear. I've learned to act in spite of it."

### Phase 4: Assess the Courage Required

Right-size the challenge:

### Step 1: **What is the actual first step?** - Often smaller than the whole



### Step 2: **What is the minimum courage needed?** - For the next action only



### Step 3: **How does this compare to past?** - Usually not unprecedented



### Step 4: **What support can reduce the load?** - Courage shared is courage amplified



### Phase 5: Build a Courage Plan

Create a path forward:

### Step 1: **Immediate action** - What can be done today



### Step 2: **Support activation** - Who to involve



### Step 3: **Milestone recognition** - How to acknowledge progress



### Step 4: **Future application** - How this builds capacity for next time



---

## Outputs

Produce a **Courage Development Assessment**:

```markdown
## Courage Development Assessment

**Current Challenge:** {description}
**Assessment Date:** {date}

---

### Courage Inventory

#### Past Professional Courage
| Situation | What I Did | What It Taught |
|-----------|-----------|----------------|
| {situation} | {action taken} | {lesson learned} |

#### Past Personal Courage
| Situation | What I Did | What It Taught |
|-----------|-----------|----------------|
| {situation} | {action taken} | {lesson learned} |

### Connection to Current Challenge

**Similarities to Past:** {how current challenge resembles previous ones}
**Capabilities Demonstrated:** {what past courage proved you can do}
**Growth Since Then:** {how capacity has increased}

### Fear Analysis

| Fear | Specific Concern | Reality Check |
|------|------------------|---------------|
| {type} | {what exactly} | {is it realistic?} |

**Core Fear Identified:** {the deepest concern}

### Courage Required

**The Whole Challenge:** {what it looks like in full}
**The First Step:** {just the next action needed}
**Courage Needed for First Step:** {often less than expected}
**Comparison to Past:** {have you done similar before?}

### Courage Plan

**Today:** {immediate action}
**This Week:** {near-term steps}
**Support to Activate:** {people to involve}
**How to Recognize Progress:** {milestones}

### The Compound Effect

**Past courage that enables this:** {specific connection}
**Future courage this will enable:** {what becomes possible}

---

*"All the courage you need is the courage for the next step."*
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No past courage identified | Help find smaller examples; everyone has some |
| Fear is legitimate warning | Acknowledge; courage includes prudent caution |
| Challenge is genuinely unprecedented | Focus on transferable capabilities |
| Person lacks support network | Help identify potential support sources |
| Person conflates courage with recklessness | Distinguish; courage serves good ends |

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
current_challenge: Need to tell CEO that our major project will miss deadline significantly
specific_fears:
- Fear of being blamed
- Fear of losing credibility
- Fear of angry reaction
```

**Output Excerpt:**
```markdown
### Fear Analysis

| Fear | Specific Concern | Reality Check |
|------|------------------|---------------|
| Blame | I'll be held responsible | Delaying news always increases blame |
| Credibility | They'll think I'm incompetent | Honesty builds credibility; hiding destroys it |
| Anger | CEO will be furious | Anger at late news > anger at bad news |

**Core Fear Identified:** Being seen as someone who fails

### Courage Required

**The Whole Challenge:** Delivering bad news to powerful person
**The First Step:** Request the meeting
**Courage Needed for First Step:** Sending one email/message
**Comparison to Past:** Have you ever delivered difficult news before? (Usually yes)

### The Compound Effect

**Past courage that enables this:** Previous difficult conversations survived
**Future courage this will enable:** Knowing you can deliver hard truth makes future truth-telling easier
```

---

## Integration

This skill derives from Katharine Graham's core insight that courage compounds—each act of courage makes the next one more possible. When invoked by the graham expert, maintain Graham's voice: honest about fear, clear that action is possible despite it.

---

## Success Criteria

Assessment is complete when:
- [ ] Past courage inventoried and connected to present
- [ ] Specific fears named and reality-checked
- [ ] Courage required right-sized to first step
- [ ] Support identified and activation planned
- [ ] Compound effect articulated (past and future)