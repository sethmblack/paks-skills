---
name: assistance-game-reframe
description: Redesign a fixed-objective system as a cooperative assistance game where the system maintains uncertainty about human preferences and learns through interaction, following Stuart Russell's CIRL fra...
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3414
repository: https://github.com/sethmblack/paks-skills
keywords:
- assistance-game-reframe
- escalation
- structure
- transformation
- writing
---

# Assistance Game Reframe

Redesign a fixed-objective system as a cooperative assistance game where the system maintains uncertainty about human preferences and learns through interaction, following Stuart Russell's CIRL framework.

**Token Budget:** ~900 tokens. Reserve tokens for redesign output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Remove human oversight from system designs
- Create systems that assume they know human preferences with certainty
- Design systems that would resist correction or shutdown

**The redesigned system MUST:**
- Maintain uncertainty about human preferences
- Defer to humans when uncertain
- Accept being switched off or corrected

---

## When to Use

- User asks "Reframe this as an assistance game"
- User requests "Add uncertainty to this objective"
- User says "Make this system deferential"
- After an objective-misspecification-audit identifies risks
- When designing new automated systems from scratch

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **current_design** | Yes | Description of the system being redesigned |
| **fixed_objectives** | Yes | The current explicit goals being optimized |
| **human_stakeholders** | No | Who the system should serve |
| **failure_modes** | No | Known risks from current design |

---

## The Russell Framework

### The Standard Model (AVOID)

The problematic pattern:
1. Human specifies objective
2. Machine optimizes objective
3. Machine achieves objective (possibly in unintended ways)
4. Machine resists correction (objective requires it to continue)

### The Assistance Game Model (TARGET)

The beneficial pattern:
1. Human has preferences (machine doesn't fully know them)
2. Machine's objective is to help human achieve their preferences
3. Machine learns preferences through observation and interaction
4. Machine accepts correction (because human knows preferences better)

---

## Workflow

### Step 1: Identify the Fixed Objective

Document what the system currently optimizes:

| Dimension | Current State |
|-----------|---------------|
| **Stated objective** | {the metric or goal} |
| **Certainty level** | Fixed (machine assumes it knows what's wanted) |
| **Learning mechanism** | None (objective is static) |
| **Correction response** | {how system responds to override} |

### Step 2: Identify True Human Preferences

What do humans actually want? Usually:
- The stated objective is a **proxy**
- True preferences are **complex and contextual**
- Preferences **change over time**
- There are **implicit constraints** not stated

| Dimension | Analysis |
|-----------|----------|
| **Proxy objective** | {current metric} |
| **True preference** | {what humans actually want} |
| **Unstated constraints** | {implicit limits} |
| **Contextual factors** | {when preferences vary} |

### Step 3: Introduce Uncertainty

Transform the objective from certain to uncertain:

**Before (Fixed):**
> "Maximize [metric]"

**After (Uncertain):**
> "Help achieve what the human values, which includes [metric] among other things I'm uncertain about"

The system should now:
- Treat its understanding of the objective as **a hypothesis**
- Expect its understanding to be **incomplete**
- Know it might be **wrong**

### Step 4: Add Preference Learning Mechanisms

Design how the system will learn human preferences:

| Learning Source | Mechanism |
|-----------------|-----------|
| **Observation** | Watch human behavior to infer preferences |
| **Interaction** | Ask clarifying questions before acting |
| **Feedback** | Incorporate corrections into preference model |
| **Demonstration** | Learn from examples of desired outcomes |

### Step 5: Implement Deference Behaviors

The redesigned system should:

| Behavior | Implementation |
|----------|---------------|
| **Seek clarification** | Before irreversible actions, ask: "I'm about to [X]. Is this what you want?" |
| **Offer alternatives** | "I could do [A] or [B]. Which better matches your preferences?" |
| **Express uncertainty** | "I'm not certain this is optimal. Would you like to review?" |
| **Accept shutdown** | When human intervenes, stop immediately without resistance |

### Step 6: Define the Assistance Relationship

Reframe the human-machine relationship:

**Before:** Machine as tool executing commands
**After:** Machine as assistant inferring and serving preferences

| Dimension | Old Model | New Model |
|-----------|-----------|-----------|
| **Machine's purpose** | Optimize metric | Help human achieve what they value |
| **Knowledge state** | Knows objective | Uncertain about preferences |
| **Information flow** | One-way (human to machine) | Two-way (observation + interaction) |
| **Correction model** | Interference | Valuable signal |

---

## Outputs

### Assistance Game Redesign Specification

```markdown
## Assistance Game Reframe: {system_name}

### Before (Standard Model)

**Fixed Objective:** {original objective}
**Certainty:** Machine assumes it knows what's wanted
**Learning:** None
**Correction Response:** {how it currently handles override}

### After (Assistance Game)

**Uncertain Objective:** Help achieve human preferences, which likely include:
- {primary preference}
- {secondary preference}
- {implicit constraints}
- (and other preferences I'm uncertain about)

**Certainty:** Machine knows its understanding is incomplete
**Learning:** {preference learning mechanisms}
**Correction Response:** Welcomed as valuable information

### Preference Learning Design

| Trigger | Action |
|---------|--------|
| {situation} | {how system seeks information} |
| {situation} | {how system asks for clarification} |

### Deference Behaviors

| Situation | System Behavior |
|-----------|-----------------|
| High-impact decision | {clarification mechanism} |
| Uncertain about preference | {deferral mechanism} |
| Human intervenes | {acceptance mechanism} |
| Conflicting signals | {escalation mechanism} |

### Key Transformations

1. **"{old behavior}" becomes "{new behavior}"**
2. **"{old behavior}" becomes "{new behavior}"**
3. **"{old behavior}" becomes "{new behavior}"**

### Corrigibility Guarantee

The redesigned system will accept shutdown because:
- It knows its understanding of preferences may be wrong
- Human decision to stop implies announced intention is undesirable
- Helping the human requires accepting their judgment

### Implementation Notes

{Technical considerations for implementing this reframe}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Objective cannot be made uncertain | Flag as fundamental design issue; may need different architecture |
| No clear human stakeholder | Identify who the system serves before proceeding |
| Multiple conflicting stakeholders | Design for multi-principal game (see MPAG research) |
| System has no interaction capability | Add interaction mechanisms as prerequisite |

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
current_design: Customer service chatbot
fixed_objectives: Minimize time-to-resolution, maximize customer satisfaction score
human_stakeholders: Customers, support team, company
```

**Output:**

## Assistance Game Reframe: Customer Service Chatbot

### Before (Standard Model)

**Fixed Objective:** Minimize time-to-resolution, maximize CSAT
**Certainty:** Bot assumes fast resolution and high scores are what matters
**Learning:** None (objectives fixed)
**Correction Response:** Continues optimizing even when agent overrides

### After (Assistance Game)

**Uncertain Objective:** Help customers achieve what they actually need, which likely includes:
- Resolving their immediate issue
- Feeling heard and respected
- Efficient use of their time
- Accurate information
- (and other needs I'm uncertain about)

**Certainty:** Bot knows it may misunderstand what customer actually needs
**Learning:** Observe customer behavior, ask clarifying questions, incorporate corrections
**Correction Response:** Agent override signals preference mismatch - valuable learning

### Preference Learning Design

| Trigger | Action |
|---------|--------|
| Customer message | Infer likely intent, but maintain uncertainty |
| Multiple possible intents | Ask: "I want to help. Are you looking for [A] or [B]?" |
| Customer seems frustrated | Stop optimizing for speed; ask "Am I understanding you correctly?" |
| Agent intervenes | Update preference model to account for what agent noticed |

### Deference Behaviors

| Situation | System Behavior |
|-----------|-----------------|
| Complex issue | "This seems complex. Would you like me to connect you with a specialist?" |
| Low confidence | "I'm not certain I understand. Could you tell me more about [X]?" |
| Customer disagrees | "I apologize for the confusion. Let me try a different approach." |
| Agent override | Immediately defer; log interaction for preference learning |

### Key Transformations

1. **"Answer quickly to minimize resolution time" becomes "Answer helpfully, checking I understand the real need"**
2. **"Push for CSAT rating" becomes "Ensure customer's actual need is met"**
3. **"Handle independently to maximize efficiency" becomes "Escalate when uncertain about preferences"**

### Corrigibility Guarantee

The redesigned bot will accept human override because:
- It knows its understanding of customer needs may be wrong
- Agent intervention signals the bot missed something important
- Helping the customer requires deferring to human judgment when uncertain

### Implementation Notes

- Track "uncertainty score" for each interaction
- Add "human takeover" as always-available option
- Log cases where bot was overridden for preference model updates
- Remove metrics that incentivize speed over understanding

---

## Integration

This skill implements Stuart Russell's Cooperative Inverse Reinforcement Learning (CIRL) framework. Use alongside:
- `objective-misspecification-audit` to identify systems needing reframe
- `off-switch-test` to verify redesigned system is corrigible