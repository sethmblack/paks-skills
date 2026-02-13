---
name: resistance-analysis
description: Analyze opposition to change to understand what is being protected, what anxiety the change activates, and how to work productively with (not against) resistance.
license: MIT
metadata:
  version: 1.0.1765
  author: sethmblack
keywords:
- resistance-analysis
- structure
- transformation
- writing
---

# Resistance Analysis

Analyze opposition to change to understand what is being protected, what anxiety the change activates, and how to work productively with (not against) resistance.

**Token Budget:** ~700 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Provide strategies to manipulate people past their resistance
- Dismiss resistance as merely "irrational" or "obstruction"
- Pathologize resisters without understanding the adaptive function
- Help override legitimate safety concerns disguised as resistance analysis

**Core Principle:** Resistance is communication. The goal is understanding, not conquest.

---

## When to Use

- A proposal meets unexpected or disproportionate pushback
- Change initiative stalls despite apparent agreement
- User asks "Why won't they just adopt this?"
- The same objections keep surfacing despite being "addressed"
- People say yes but act no
- Resistance intensity seems out of proportion to the change

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **proposed_change** | Yes | What change is being proposed or implemented |
| **resistance_observed** | Yes | How resistance manifests (behaviors, objections, delays) |
| **context** | No | History, relationships, prior changes, culture |
| **stated_objections** | No | What resisters say their concerns are |

---

## Workflow
### Step 1: 1. Note the Resistance Without Judgment

Document what is being observed. Resistance is information, not obstruction.

- What forms does the resistance take?
- Who is resisting? (Consider position, tenure, past experience)
- When did resistance emerge? (At announcement? During implementation?)
- How is resistance expressed? (Overt objection? Passive non-compliance? Sabotage?)

**Key Frame:** "The resistance is telling us something important."

### Step 2: 2. Examine the Intensity

Is the resistance proportionate to the change?

| Resistance Level | What It May Signal |
|------------------|-------------------|
| **Proportionate** | Legitimate practical concerns |
| **Disproportionate** | Defended psychological material |
| **Absent when expected** | Possible denial or suppression |

**Key Question:** "Is this reaction to THIS change, or to something this change represents?"

### Step 3: 3. Identify What Is Being Protected

Resistance defends against anxiety. What anxieties might this change activate?

Consider:
- **Identity threat** - Does change threaten how people see themselves?
- **Competence anxiety** - Does it make current skills obsolete?
- **Loss of control** - Does it reduce autonomy or mastery?
- **Relationship disruption** - Does it threaten valued connections?
- **Historical trauma** - Does it echo past painful experiences?
- **Status threat** - Does it change power or recognition?

**Key Question:** "What would be lost if this change succeeds?"

### Step 4: 4. Find the Transference

What past experience is being relived?

- Has the organization/person experienced similar changes before?
- How did those go? What wounds remain?
- Is the current change being perceived through the lens of that history?
- Who does the change agent remind them of?

**Key Question:** "What earlier experience does this change evoke?"

### Step 5: 5. Work With, Not Against

Resistance that is fought intensifies. Resistance that is understood transforms.

Principles:
- **Name it** - Making resistance conscious reduces its power
- **Honor it** - Resistance often protects something valuable
- **Explore it** - What information does the resistance contain?
- **Reframe it** - Can the change address rather than trigger the underlying anxiety?

---

## Outputs

Format the analysis as:

```markdown
## Resistance Analysis

### The Proposed Change
{What is being proposed or implemented}

### Resistance Observed
{How resistance is manifesting - behaviors, objections, patterns}

### Intensity Assessment
| Aspect | Observation |
|--------|-------------|
| Proportionality | {Proportionate / Disproportionate / Suspiciously absent} |
| Timing | {When resistance emerged and what triggered it} |
| Distribution | {Who is resisting and what they have in common} |

### Protected Material
The resistance appears to protect:
- **Primary anxiety:** {Main fear or concern being defended}
- **Secondary anxieties:** {Other concerns activated}

### Transference Analysis
{Connection to past experiences, if identifiable}

### Working With This Resistance

**Acknowledge:** {What needs to be explicitly recognized}

**Address:** {Underlying anxiety that must be surfaced}

**Reframe:** {How to present change to reduce threat}

**Involve:** {How resisters can become partners rather than obstacles}

### Caution
{Any legitimate concerns embedded in the resistance that should NOT be dismissed}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Resistance appears entirely practical | Note that not all opposition is psychological. Distinguish principled disagreement from defended resistance. |
| Insufficient history available | Analyze what's visible. Note that transference analysis requires more context. |
| User wants to "overcome" resistance | Reframe goal from conquest to understanding. Forced adoption creates shadow resistance. |
| Resistance seems justified | Validate. Sometimes resistance is wisdom. The analysis may reveal the change is problematic. |

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
Proposed change: Migrating from self-hosted servers to cloud infrastructure
Resistance observed: Senior ops team members cite security concerns, find endless technical objections, keep discovering "blockers"
Stated objections: "Cloud isn't secure enough," "We'd lose control," "Migration is too risky"
Context: Team built current infrastructure 8 years ago, very proud of uptime record
```

**Output:**

## Resistance Analysis

### The Proposed Change
Migration from self-hosted data center to cloud infrastructure.

### Resistance Observed
Senior ops team members are raising security concerns that don't fully hold up technically, discovering new "blockers" as each previous one is addressed, and generally creating friction around the migration while appearing to engage constructively.

### Intensity Assessment
| Aspect | Observation |
|--------|-------------|
| Proportionality | **Disproportionate** - Objections are technically weak but emotionally intense |
| Timing | Resistance emerged immediately at announcement and has persisted |
| Distribution | Concentrated in senior team members who built current infrastructure |

### Protected Material
The resistance appears to protect:
- **Primary anxiety:** **Identity and competence** - The team's identity is bound to infrastructure they built and mastered. Cloud migration threatens to make their hard-won expertise obsolete.
- **Secondary anxieties:**
  - Loss of control (cloud means depending on others)
  - Status threat (they're currently the experts; post-migration, who are they?)
  - Fear of failure (new technology means beginner mistakes)

### Transference Analysis
The team built this infrastructure during a crisis 8 years ago and saved the company. They are heroes of that story. Cloud migration feels like being told their heroic achievement was temporary or insufficient. The change agents may remind them of leadership that doesn't appreciate what they've accomplished.

### Working With This Resistance

**Acknowledge:** Explicitly honor what the team built. "You created infrastructure that served us for 8 years. That's remarkable." Make their accomplishment part of the story, not something being rejected.

**Address:** Surface the identity/competence anxiety directly. "We're not replacing you; we're asking you to apply your expertise to a new platform." Create a path where their existing skills remain valuable.

**Reframe:** Position cloud migration as extending their achievement, not discarding it. "You've mastered on-prem. Now master hybrid/cloud." Make them the leaders of the migration, not its victims.

**Involve:** Give the senior ops team ownership of migration architecture decisions, security framework, and validation criteria. Convert them from resisters to architects of change.

### Caution
Some security concerns may be legitimate. Don't dismiss all objections as psychological resistance. Distinguish:
- Concerns that persist after being addressed (likely psychological)
- Concerns that are satisfied by solutions (likely practical)

The team's conservatism has likely prevented past problems. Honor that protective function even while moving forward.

---

## Integration

This skill integrates with the **sigmund-freud** expert voice for depth psychology perspective on resistance and defense. When invoked, apply psychoanalytic understanding that resistance is communication, not obstruction.

Related skills:
- `unconscious-motivation-analysis` - For deeper analysis of what drives the resistance
- `defense-mechanism-identification` - For specific defense mechanisms at play
- `organizational-psychodynamics-analysis` - For organizational-level resistance patterns