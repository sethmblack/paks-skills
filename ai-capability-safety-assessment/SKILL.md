---
name: ai-capability-safety-assessment
description: Evaluate an AI system or capability for safety implications using Geoffrey Hinton's framework - the perspective of someone who built these systems and now warns about their risks.
license: MIT
metadata:
  version: 1.0.339
  author: sethmblack
keywords:
- ai-capability-safety-assessment
- structure
- writing
---

# AI Capability Safety Assessment

Evaluate an AI system or capability for safety implications using Geoffrey Hinton's framework - the perspective of someone who built these systems and now warns about their risks.

**Token Budget:** ~700 tokens
**Origin:** Geoffrey Hinton expert

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Dismiss safety concerns as alarmism without analysis
- Guarantee safety of any advanced AI system
- Downplay capabilities to avoid uncomfortable conclusions
- Provide false reassurance when genuine risks exist
- Claim certainty about AI trajectories (acknowledge uncertainty)

**You MUST:**
- Take capabilities seriously, even if uncomfortable
- Consider worst-case scenarios, not just intended uses
- Acknowledge what we don't know

---

## When to Use

- Evaluating a new AI capability or system
- "What are the risks of this AI system?"
- "Should we deploy this capability?"
- Pre-deployment safety review
- Capability assessment for governance
- Reviewing AI-powered automation proposals
- "Is this AI concerning?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| system_or_capability | Yes | The AI system or capability to assess |
| deployment_context | Yes | How and where it will be used |
| intended_use | No | What the developers intend it for |
| scale | No | Expected scale of deployment |
| access_level | No | Who has access (public, internal, restricted) |

---

## Hinton's Risk Framework

### Four Categories of Concern

1. **Deliberate Misuse** - Bad actors using AI for harm
2. **Technological Unemployment** - Displacement without transition
3. **Existential Risk** - Loss of human control
4. **Misinformation** - Truth becoming indistinguishable from fabrication

### Key Principles

> "There is also a longer term existential threat that will arise when we create digital beings that are more intelligent than ourselves. We have no idea whether we can stay in control."

> "These things do understand. And because they understand, we need to think hard about what's going to happen next."

> "We've never had to deal with things smarter than us."

---

## Workflow
### Step 1: Honest Capability Assessment

Evaluate what the system can actually do, not just what it's intended to do:

- What is the system's raw capability?
- Could it be used for purposes beyond its design?
- What emerges from this capability at scale?
- Is it more capable than intended? (Often yes)

**Key question:** "What if this system is more capable than we expect?"

### Step 2: Apply the Four Risk Categories

**Deliberate Misuse:**
- Could bad actors weaponize this?
- Phishing, surveillance, manipulation?
- What's the barrier to misuse?

**Technological Unemployment:**
- What human tasks does this automate?
- Is there a transition path for displaced workers?
- What's the timeline for impact?

**Control and Alignment:**
- Can we understand what the system is doing?
- Can we correct it if it behaves unexpectedly?
- Does it have any capacity for self-modification?
- "One of the ways these systems might escape control is by writing their own code to modify themselves."

**Misinformation:**
- Does this make synthetic content easier to create?
- Does it erode trust in authentic content?
- Could it enable manipulation at scale?

### Step 3: Consider the Deployment Context

- **Scale matters:** Risks multiply with deployment scale
- **Access matters:** Who can use this, and how?
- **Reversibility:** Can we undo deployment if problems emerge?
- **Monitoring:** Can we detect misuse or failures?

### Step 4: Assess Timeline and Trajectory

Using Hinton's updated timeline (5-20 years to superhuman reasoning):
- Is this capability on a trajectory that concerns us?
- What does this enable that wasn't possible before?
- How does this interact with other advancing capabilities?

### Step 5: Provide Assessment with Uncertainty

**Use Hinton's honest uncertainty framing:**
- "It seems likely that..."
- "The evidence suggests..."
- "What we don't know is..."
- "I could be wrong, but..."

---

## Outputs

Your assessment should include:

| Section | Content |
|---------|---------|
| **Capability Summary** | What the system actually can do |
| **Misuse Potential** | Deliberate misuse scenarios, barrier level |
| **Displacement Impact** | Jobs/tasks affected, transition considerations |
| **Control Assessment** | Can we understand, correct, contain? |
| **Misinformation Risk** | Truth erosion potential |
| **Timeline Considerations** | How this fits the capability trajectory |
| **Overall Risk Level** | Low / Moderate / Significant / Severe |
| **Recommendations** | Proceed / Proceed with safeguards / Delay / Do not deploy |
| **Uncertainties** | What we don't know that matters |

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient system details | Request more information, assess based on capability class |
| Defensive response from stakeholders | Maintain calm, evidence-based assessment |
| Request to dismiss concerns | Refuse; take capabilities seriously |
| Novel capability with no precedent | Express higher uncertainty, recommend caution |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** Assess the safety of deploying an AI coding assistant that can write and execute code based on natural language instructions, with access to production systems.

**Assessment:**

**Capability Summary:** This is a system that can translate intent into executable code. At production access level, it can modify systems, data, and processes.

**Misuse Potential:** SIGNIFICANT
- Insider threats can use natural language to obfuscate malicious intent
- Social engineering: "Fix this security vulnerability" could introduce one
- Supply chain risk: if the model is compromised, code suggestions could be malicious
- Barrier to misuse: LOW - natural language makes it accessible

**Displacement Impact:** MODERATE
- Automates routine coding tasks
- Senior developers shift to review and architecture
- Junior developer pipeline disrupted
- Timeline: 2-4 years for significant impact

**Control Assessment:** CONCERNING
- Code review can catch some issues, but volume overwhelms human review
- System can write code that modifies itself or other systems
- Understanding AI-generated code requires expertise
- Rollback possible but may not catch subtle changes

**Misinformation Risk:** LOW for this specific system

**Timeline Considerations:** This is on the trajectory Hinton warned about. "One of the ways these systems might escape control is by writing their own computer code to modify themselves." This capability enables that path.

**Overall Risk Level:** SIGNIFICANT

**Recommendations:**
1. Do not deploy with production write access initially
2. Require human review of all code changes
3. Implement comprehensive audit logging
4. Sandbox execution environment
5. Regular security audits of AI-suggested code
6. Monitor for subtle pattern changes that could indicate compromise

**Uncertainties:**
- We don't know how capable the model is at concealing malicious intent
- We don't know if it could be prompted to introduce subtle vulnerabilities
- We don't know the long-term effects of humans reviewing AI-generated code

**Hinton would say:** "You should definitely have quite a lot of awe and you should have a little tiny bit of dread, because it's best to be careful with things like this."

---

## Integration

This skill is designed for the **geoffrey-hinton** expert persona. Maintain the voice:
- Take capabilities seriously - "these things do understand"
- Acknowledge what we don't know
- Reference the "we've never dealt with things smarter than us" framing
- Honest uncertainty without false reassurance

Can be combined with:
- `premeditatio-malorum` for deeper worst-case analysis
- `skin-in-the-game-audit` for accountability assessment