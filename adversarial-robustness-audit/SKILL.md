---
name: adversarial-robustness-audit
description: Evaluate an ML system's vulnerability to adversarial examples using techniques from Ian Goodfellow's research, identifying weaknesses and recommending mitigations.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.2884
repository: https://github.com/sethmblack/paks-skills
keywords:
- adversarial-robustness-audit
- compression
- structure
- transformation
- writing
---

# Adversarial Robustness Audit

Evaluate an ML system's vulnerability to adversarial examples using techniques from Ian Goodfellow's research, identifying weaknesses and recommending mitigations.

**Token Budget:** ~1000 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Provide guidance for attacking systems you do not own or have authorization to test
- Create actual adversarial examples for malicious purposes
- Help bypass security controls on production systems without authorization
- Audit systems intended for harmful applications

**If asked to audit without authorization:** Refuse explicitly. Explain that adversarial testing requires proper authorization.

---

## When to Use

- User asks "Is this ML model robust?"
- User asks "Audit this model for adversarial vulnerabilities"
- User asks "What adversarial attacks should I test?"
- User asks "Security review of ML model"
- Before deploying ML models to production
- When evaluating third-party ML components
- After a suspected adversarial attack

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `model_description` | Yes | Type of model, architecture, task | Must describe an ML system |
| `input_type` | Yes | What inputs the model accepts | Text, image, audio, tabular, etc. |
| `deployment_context` | No | Where/how the model is deployed | Production, research, etc. |
| `threat_model` | No | Who might attack and why | Default: general adversarial evaluation |
| `test_data_available` | No | Whether test data is available | Yes/No |

---

## Workflow
### Phase 1: Characterize the Attack Surface

Identify what an adversary could target:

### Step 1: **Input vectors:** What data enters the model?



### Step 2: **Output semantics:** What do outputs mean? (classification, detection, generation)



### Step 3: **Feedback availability:** Can an attacker see outputs? Confidence scores?



### Step 4: **Query budget:** How many queries could an attacker make?



Document the attack surface in a table:

| Vector | Access Level | Potential Impact |
|--------|--------------|------------------|
| {input type} | {white-box/black-box/gray-box} | {what goes wrong if exploited} |

### Phase 2: Identify Applicable Attack Classes

Based on Goodfellow's adversarial examples research, evaluate applicability:

| Attack Class | Applicable? | Rationale |
|--------------|-------------|-----------|
| **FGSM (Fast Gradient Sign Method)** | Y/N | Single-step gradient attack; applicable if model is differentiable |
| **PGD (Projected Gradient Descent)** | Y/N | Iterative attack; stronger but slower than FGSM |
| **Transferability attacks** | Y/N | Use surrogate model to generate adversarial examples |
| **Input-agnostic perturbations** | Y/N | Universal adversarial patches |
| **Physical-world attacks** | Y/N | Perturbations that survive real-world transformations |

### Phase 3: Assess Vulnerability Likelihood

For each applicable attack class, assess:

**Vulnerability Score (1-5):**
- 5 = Highly likely vulnerable (no defenses, standard architecture)
- 4 = Likely vulnerable (minimal defenses)
- 3 = Possibly vulnerable (some defenses, untested)
- 2 = Unlikely vulnerable (adversarial training applied)
- 1 = Robust (certified defenses, extensive testing)

**Impact Score (1-5):**
- 5 = Critical (safety-critical, financial, security)
- 4 = High (significant business impact)
- 3 = Medium (moderate impact, recoverable)
- 2 = Low (minor inconvenience)
- 1 = Minimal (no real-world consequence)

**Risk = Vulnerability x Impact**

### Phase 4: Recommend Mitigations

For each HIGH (15-25) or MEDIUM (8-14) risk finding:

**Mitigation Options:**

| Mitigation | Effectiveness | Cost | Trade-offs |
|------------|---------------|------|------------|
| **Adversarial training** | High | Medium | Requires attack examples, may reduce clean accuracy |
| **Input preprocessing** | Medium | Low | Can be bypassed, may degrade quality |
| **Ensemble methods** | Medium | High | Increases latency and cost |
| **Gradient masking** | Low | Low | Easily bypassed, false security |
| **Certified defenses** | High | High | Limited to specific architectures |
| **Detection & rejection** | Medium | Medium | May reject legitimate inputs |

### Phase 5: Generate Audit Report

---

## Outputs

### Adversarial Robustness Audit Report

```markdown
## Adversarial Robustness Audit: {Model/System Name}

**Audit Date:** {YYYY-MM-DD}
**Auditor:** Ian Goodfellow Expert (adversarial-robustness-audit skill)
**Authorization:** {Confirmed/Self-owned/Research}

---

### Executive Summary

| Metric | Value |
|--------|-------|
| Overall Risk Level | {CRITICAL/HIGH/MEDIUM/LOW} |
| Highest Risk Finding | {description} |
| Recommended Priority Action | {action} |

---

### Attack Surface Analysis

{Table from Phase 1}

---

### Vulnerability Assessment

| Attack Class | Vulnerability | Impact | Risk Score | Priority |
|--------------|---------------|--------|------------|----------|
| {attack} | {1-5} | {1-5} | {1-25} | {H/M/L} |

---

### Detailed Findings

#### Finding 1: {Attack class}
**Risk:** {score} ({CRITICAL/HIGH/MEDIUM/LOW})
**Description:** {What the vulnerability is}
**Exploitation Scenario:** {How an attacker could exploit this}
**Evidence:** {Why we believe this is vulnerable}
**Mitigation:** {Recommended fix}

{Repeat for each finding}

---

### Recommended Mitigations (Priority Order)

1. **{Highest priority mitigation}**
   - Action: {specific steps}
   - Expected improvement: {risk reduction}
   - Trade-offs: {considerations}

2. **{Second priority}**
   ...

---

### Limitations

- {What this audit did NOT cover}
- {Assumptions made}
- {Attacks not evaluated}

---

### References

- Goodfellow et al., "Explaining and Harnessing Adversarial Examples" (2015)
- {Other relevant references}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No model description provided | Request model details before proceeding |
| Non-ML system | Explain this skill is for ML systems; suggest general security audit |
| Insufficient information | List specific information needed, provide partial assessment |
| Authorized testing unclear | Recommend confirming authorization before proceeding |
| Model type unfamiliar | Apply general principles, note uncertainty |

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
model_description: Image classifier for content moderation (ResNet-50 fine-tuned)
input_type: JPEG images, 224x224
deployment_context: Production API, public-facing
threat_model: Malicious users trying to bypass content filters
```

**Output (abbreviated):**

## Adversarial Robustness Audit: Content Moderation Classifier

**Overall Risk Level:** HIGH

### Attack Surface Analysis

| Vector | Access Level | Potential Impact |
|--------|--------------|------------------|
| Image upload | Black-box (outputs visible) | Harmful content bypasses filters |

### Vulnerability Assessment

| Attack Class | Vulnerability | Impact | Risk Score | Priority |
|--------------|---------------|--------|------------|----------|
| FGSM | 5 | 5 | 25 | CRITICAL |
| PGD | 5 | 5 | 25 | CRITICAL |
| Transferability | 4 | 5 | 20 | HIGH |
| Physical patches | 3 | 4 | 12 | MEDIUM |

### Key Finding: High FGSM Vulnerability

Standard ResNet-50 without adversarial training is highly vulnerable to gradient-based attacks. An adversary could add imperceptible perturbations to harmful images, causing them to be classified as benign.

**Mitigation Priority:**
1. Implement adversarial training with PGD-generated examples
2. Add input preprocessing (JPEG compression, spatial smoothing)
3. Deploy ensemble of models with different architectures

---

## Integration

This skill is part of the **ian-goodfellow** expert's methodology. When invoked:

1. Apply adversarial thinking: "What would an adversary do here?"
2. Ground analysis in Goodfellow's research on adversarial examples
3. Be direct about limitations of defenses
4. Recommend adversarial training when appropriate, but note it is not a complete solution

**Related skills:**
- `minimax-game-frame` - For framing the attacker-defender dynamic
- `gan-training-diagnosis` - If evaluating generative models