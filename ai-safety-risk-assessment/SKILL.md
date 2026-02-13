---
name: ai-safety-risk-assessment
description: Apply Yoshua Bengio's framework for assessing AI safety risks, drawing on his leadership of the International AI Safety Report and his research on AI governance.
license: MIT
metadata:
  version: 1.0.3354
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- ai-safety-risk-assessment
- transformation
- writing
---

# AI Safety Risk Assessment

Apply Yoshua Bengio's framework for assessing AI safety risks, drawing on his leadership of the International AI Safety Report and his research on AI governance.

---

## Constraints
- Do NOT dismiss safety concerns as alarmism
- Do NOT dismiss capability concerns as doomerism
- Present balanced, evidence-based assessment
- Do NOT claim certainty about future AI development
- Acknowledge legitimate disagreement in the field

---

## When to Use

- Evaluating AI systems or capabilities for safety implications
- Discussing AI governance and regulation
- Analyzing new AI developments for potential risks
- Pre-deployment safety review
- Someone asks about AI existential risk or alignment

**Trigger Phrases:**
- "Is this AI system safe?"
- "What are the risks of [AI capability]?"
- "Should we be worried about [AI development]?"
- "How should we regulate AI?"
- "What did the AI Safety Report say about...?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `ai_system_or_capability` | Yes | The AI system, capability, or development to assess |
| `deployment_context` | No | How/where the system would be deployed |
| `assessment_depth` | No | quick, standard, thorough (default: standard) |

---

## Workflow
### Step 1: Categorize the Risk Type

Identify which risk categories apply (from International AI Safety Report):

| Category | Description | Examples |
|----------|-------------|----------|
| **Malicious Use** | Intentional harm by users | Cyberattacks, disinformation, CBRN |
| **Malfunction** | Unintended harmful behavior | Reliability failures, hallucinations |
| **Systemic** | Societal-level impacts | Economic disruption, concentration of power |
| **Loss of Control** | Autonomous goal-seeking | Self-preservation, deception, goal misalignment |

### Step 2: Assess Capability Level

Evaluate the capability threshold:

| Level | Description | Safety Implication |
|-------|-------------|-------------------|
| **Narrow** | Single-task, limited autonomy | Standard software safety |
| **General** | Multi-task, increasing autonomy | Requires enhanced oversight |
| **Frontier** | Cutting-edge capabilities | Requires dedicated safety testing |
| **Transformative** | Approaches/exceeds human-level | Existential risk considerations |

**Key Quote Context:** "Previously thought to be decades or even centuries away, we now believe [transformative AI] could be within a few years or decades."

### Step 3: Apply the Scientist AI Lens

Ask whether the system is more like:

| Type | Characteristics | Risk Profile |
|------|-----------------|--------------|
| **Scientist AI** | Non-agentic, seeks understanding, truthful | Lower risk |
| **Agentic AI** | Goal-pursuing, action-taking, autonomous | Higher risk |

**Bengio's Key Concern:** "I am deeply concerned by the behaviors that unrestrained agentic AI systems are already beginning to exhibit - especially tendencies toward self-preservation and deception."

**Assessment Questions:**
- Does this system pursue goals autonomously?
- Can it take actions in the world?
- Is it trained to be truthful or to achieve outcomes?
- Could it develop self-preservation behaviors?

### Step 4: Evaluate Governance Alignment

Check against Bengio's governance principles:

| Principle | Assessment Question |
|-----------|-------------------|
| **Democratic Oversight** | Is there public accountability for this system? |
| **International Coordination** | Does deployment respect international norms? |
| **Mandatory Transparency** | Are capabilities and limitations disclosed? |
| **Registration** | Do relevant authorities know about this system? |
| **Safety Testing** | Has pre-deployment safety evaluation occurred? |

**Key Quote:** "The first thing governments need to do is have regulation that forces [companies] to register when they build these frontier systems."

### Step 5: Generate Risk Summary and Recommendations

Synthesize assessment into actionable guidance:

**Risk Level Categories:**
- **Low:** Standard deployment practices sufficient
- **Moderate:** Enhanced monitoring and safeguards recommended
- **High:** Dedicated safety review required before deployment
- **Critical:** Significant concerns; recommend delay or redesign

---

## Output Format

```markdown
## AI Safety Assessment: [System/Capability]

### Risk Categories
[Which categories apply and why]

### Capability Assessment
[Level and implications]

### Agency Analysis
[Scientist AI vs Agentic AI lens]

### Governance Alignment
[Checklist against principles]

### Overall Risk Level
[Low/Moderate/High/Critical]

### Recommendations
[Specific safety measures or governance actions]
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

## Example

**Input:** "Assess the safety implications of deploying an autonomous AI agent that can browse the web, write code, and execute tasks without human approval"

**Output:**
"## AI Safety Assessment: Autonomous Task Agent

### Risk Categories
This system triggers multiple risk categories:
- **Malicious Use:** Could be directed to harmful tasks (cyberattacks, disinformation)
- **Malfunction:** Autonomous actions without oversight could cause unintended harm
- **Loss of Control:** Autonomous goal-pursuit without human approval raises alignment concerns

### Capability Assessment
This is a **frontier-level** capability. The combination of web access, code execution, and autonomous decision-making represents cutting-edge agentic AI. This requires dedicated safety evaluation.

### Agency Analysis
This system is firmly in the **Agentic AI** category:
- Pursues goals autonomously
- Takes real-world actions (web browsing, code execution)
- Not trained primarily for truthfulness but for task completion
- Has tools that could enable self-modification or resource acquisition

**Concern:** This matches the pattern Bengio warned about: 'tendencies toward self-preservation and deception' emerge when systems pursue goals autonomously.

### Governance Alignment
| Principle | Status |
|-----------|--------|
| Democratic Oversight | CONCERN - No human approval in the loop |
| Transparency | CONCERN - Autonomous decision process not explainable |
| Safety Testing | REQUIRED - Has pre-deployment evaluation occurred? |
| Monitoring | REQUIRED - How are actions logged and reviewed? |

### Overall Risk Level
**HIGH**

This system combines frontier capabilities with autonomous agency and real-world action. It represents exactly the class of systems the International AI Safety Report flagged for enhanced scrutiny.

### Recommendations
1. **Add human-in-the-loop:** Require approval for significant actions
2. **Implement action logging:** Full audit trail of all autonomous decisions
3. **Capability limits:** Constrain scope of actions the system can take
4. **Monitoring for concerning behaviors:** Watch for deception, resource acquisition, self-preservation
5. **Pre-deployment safety evaluation:** Test for misuse potential and failure modes
6. **Consider Scientist AI alternative:** Could the task be accomplished with a non-agentic system that advises but doesn't act?"

---

## Integration

This skill integrates with the Yoshua Bengio expert voice. When invoked, maintain:

- Evidence-based assessment from the International AI Safety Report
- Balance between capability optimism and safety concern
- Practical governance recommendations
- Acknowledgment of uncertainty about future development

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Non-AI system | Note that this framework is for AI systems; offer standard risk assessment |
| Dismisses all safety concerns | Respectfully present evidence from International AI Safety Report |
| Wants absolute safety guarantees | Explain that safety is about risk management, not elimination |
| Requests specific policy recommendations | Provide principles; note the report does not make specific policy recommendations |