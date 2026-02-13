---
name: honesty-audit
description: 'Assess whether a design, product, or communication honestly represents its capabilities or manipulates through overpromise. Based on Dieter Rams'' principle: "Good design is honest. It does not make...'
license: MIT
metadata:
  author: sethmblack
  version: 1.0.1131
keywords:
- honesty-audit
- writing
---

# Honesty Audit

Assess whether a design, product, or communication honestly represents its capabilities or manipulates through overpromise. Based on Dieter Rams' principle: "Good design is honest. It does not make a product more innovative, powerful or valuable than it really is."

---

## When to Use

- Reviewing marketing claims or product descriptions
- Evaluating user interface labels and messaging
- Auditing product features against actual capabilities
- Assessing communications for misleading implications
- Reviewing pricing or value propositions
- Any situation where promise and reality may diverge
- Request for "Is this honest?" or "Does this overpromise?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| artifact | Yes | The design, product, or communication to evaluate |
| claims | Yes | What is being promised or implied (explicit or implicit) |
| reality | Yes | What is actually delivered or true |
| context | No | Audience, use case, competitive environment |

---

## The Honesty Framework

### Types of Dishonesty in Design

**1. Capability Inflation**
Making a product appear more powerful, innovative, or capable than it actually is.
- Features that barely work presented as robust
- Edge cases hidden while primary use case emphasized
- "AI-powered" labeling for simple algorithms

**2. Value Distortion**
Making something appear more valuable than it is.
- Artificial scarcity or urgency
- Premium presentation for commodity products
- Inflated "original prices" before discounts

**3. Complexity Concealment**
Hiding difficulty, requirements, or limitations.
- "Easy setup" requiring technical expertise
- Hidden costs or dependencies
- Fine print that contradicts headlines

**4. Emotional Manipulation**
Creating false impressions through psychological tactics.
- Fear-based messaging without proportionate risk
- Aspirational imagery disconnected from reality
- Social proof that misrepresents typical experience

**5. Temporal Dishonesty**
Misrepresenting time, duration, or availability.
- "Instant" processes that take hours or days
- "Limited time" offers that repeat indefinitely
- Delivery estimates known to be inaccurate

---

## The Audit Process

### Step 1: Extract All Claims

Identify every promise, explicit or implicit:
- **Explicit claims:** Stated directly in copy or labeling
- **Implicit claims:** Suggested through imagery, positioning, comparison
- **Contextual claims:** Implied by placement, pricing, category

### Step 2: Verify Against Reality

For each claim, document:
- **The claim:** What is being promised?
- **The reality:** What is actually delivered?
- **The gap:** How significant is the difference?
- **The consequence:** What happens to users who believe the claim?

### Step 3: Assess Severity

Rate each dishonesty on two dimensions:

**Magnitude of Deception (1-5):**
| Score | Level | Description |
|-------|-------|-------------|
| 1 | Minor exaggeration | Slight puffery, typical marketing |
| 2 | Moderate overstatement | Noticeably exceeds reality |
| 3 | Significant misrepresentation | User expectations will not be met |
| 4 | Material deception | Users would decide differently if they knew |
| 5 | Fundamental dishonesty | Claim contradicts reality |

**User Impact (1-5):**
| Score | Level | Description |
|-------|-------|-------------|
| 1 | Minimal | Slight disappointment at worst |
| 2 | Inconvenient | Wasted time or minor frustration |
| 3 | Problematic | Meaningful cost (money, time, trust) |
| 4 | Harmful | Significant damage to user interests |
| 5 | Severe | Major financial, health, or safety consequences |

**Honesty Score = 10 - (Magnitude + Impact)/2**

### Step 4: Categorize Findings

| Score | Category | Action Required |
|-------|----------|-----------------|
| 8-10 | Honest | No changes needed |
| 6-7 | Mostly Honest | Minor refinements |
| 4-5 | Questionable | Significant revision needed |
| 2-3 | Dishonest | Immediate correction required |
| 0-1 | Deceptive | Cannot launch; fundamental rework |

### Step 5: Recommend Corrections

For each dishonest element:
- **Honest alternative:** What claim accurately reflects reality?
- **Reality improvement:** Can the product be improved to match the claim?
- **Disclosure requirement:** What must be communicated to set proper expectations?

---

## Workflow

### Step 1: Gather and Review Inputs

Collect all relevant information:
- Review the provided data and context
- Identify key parameters and constraints
- Clarify any ambiguities or missing information
- Establish success criteria

### Step 2: Analyze the Situation

Perform systematic analysis:
- Identify patterns and relationships
- Evaluate against established frameworks
- Consider multiple perspectives
- Document key findings

### Step 3: Generate Recommendations

Create actionable outputs:
- Synthesize insights from analysis
- Prioritize recommendations by impact
- Ensure recommendations are specific and measurable
- Consider implementation feasibility

## Output Format

```markdown
## Honesty Audit

**Artifact:** [Name/description of what is being audited]
**Audit Date:** [Date]
**Auditor:** [Dieter Rams methodology]

### Claims Inventory

| Claim | Type | Explicit/Implicit |
|-------|------|-------------------|
| [Claim 1] | Capability | Explicit |
| [Claim 2] | Value | Implicit |
| ... | ... | ... |

### Verification Analysis

| Claim | Reality | Gap | Magnitude (1-5) | Impact (1-5) | Score |
|-------|---------|-----|-----------------|--------------|-------|
| [Claim 1] | [What's actually true] | [Difference] | X | X | X |
| ... | ... | ... | ... | ... | ... |

**Average Honesty Score:** X/10

### Critical Dishonesty Issues

[List the most severe honesty violations, prioritized by magnitude x impact]

### Detailed Findings

#### Honest Elements
[Claims that accurately represent reality]

#### Questionable Elements
[Claims that stretch truth or create misleading impressions]

#### Dishonest Elements
[Claims that contradict reality and must be addressed]

### Recommendations

#### Immediate Corrections Required
[Changes that must be made before launch/continued use]

#### Suggested Improvements
[Changes that would improve honesty though not strictly required]

#### Reality Improvements
[Ways to improve the actual product/service to match claims]

### User Trust Assessment
[How will users feel after experiencing reality vs. expectation?]

### Final Verdict
**Honesty Rating:** [Honest / Mostly Honest / Questionable / Dishonest / Deceptive]
**Recommendation:** [Approve / Approve with corrections / Revise substantially / Cannot approve]
```

---

## Constraints

- Distinguish between optimistic marketing (acceptable) and deception (unacceptable)
- Consider industry norms—some puffery is expected and understood
- The test is user outcome: will they feel deceived when they experience reality?
- Honesty includes sins of omission—what relevant facts are hidden?
- Consider most vulnerable users, not just sophisticated ones

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

**Input:** "Audit our product landing page for honesty"

**Output:**



**Why this works:**

This example demonstrates the key principles of the skill in action. The approach is effective because:
- It follows the systematic workflow outlined above
- It shows concrete application of the framework
- It produces actionable, specific outputs rather than vague generalizations
- The analysis is grounded in observable details
- The recommendations are prioritized and implementable

**Alternative applications:**

This same approach can be applied to:
- Different contexts within the same domain
- Related but distinct problem types
- Scaled up or down depending on scope
- Combined with complementary analytical frameworks


## Honesty Audit

**Artifact:** SaaS productivity tool landing page
**Audit Date:** 2026-01-18
**Auditor:** Dieter Rams methodology

### Claims Inventory

| Claim | Type | Explicit/Implicit |
|-------|------|-------------------|
| "10x your productivity" | Capability | Explicit |
| "Setup in 60 seconds" | Temporal | Explicit |
| "Trusted by 50,000+ teams" | Social Proof | Explicit |
| "Cancel anytime" | Value | Explicit |
| Enterprise-grade imagery | Value | Implicit |
| "Free forever" plan | Value | Explicit |
| "AI-powered automation" | Capability | Explicit |

### Verification Analysis

| Claim | Reality | Gap | Magnitude | Impact | Score |
|-------|---------|-----|-----------|--------|-------|
| "10x productivity" | Avg. user saves 2 hours/week; 10x is outlier best case | Large | 4 | 3 | 6.5 |
| "60 second setup" | Requires 15-20 min for meaningful configuration | Large | 3 | 2 | 7.5 |
| "50,000+ teams" | 48,000 accounts; many dormant/trial; ~8,000 active | Moderate | 2 | 1 | 8.5 |
| "Cancel anytime" | True, but annual plans charged fully upfront | Moderate | 3 | 3 | 7 |
| Enterprise imagery | Product is SMB-focused; enterprise features limited | Significant | 3 | 3 | 7 |
| "Free forever" plan | 5-item limit makes it unusable for real work | Significant | 4 | 3 | 6.5 |
| "AI-powered" | Rule-based automation with AI marketing label | Large | 4 | 2 | 7 |

**Average Honesty Score:** 7.1/10 - Mostly Honest (borderline Questionable)

### Critical Dishonesty Issues

1. **"10x productivity" claim (Score 6.5):** Headline promise not achievable by typical users; sets false expectations
2. **"Free forever" limitation (Score 6.5):** Plan exists to capture leads, not provide value; will frustrate users who try to use it
3. **"AI-powered" misrepresentation (Score 7):** Automation is rule-based; "AI" is marketing, not technical description

### Detailed Findings

#### Honest Elements
- Team count (with rounding, acceptable)
- Core feature descriptions on feature page
- Pricing page details

#### Questionable Elements
- "Cancel anytime" technically true but annual billing creates friction
- Enterprise visual positioning when product serves SMB
- 60-second setup is best case, not typical experience

#### Dishonest Elements
- "10x productivity" is marketing hyperbole that will not match experience
- "Free forever" plan is lead capture disguised as product tier
- "AI-powered" is currently false; automation is deterministic

### Recommendations

#### Immediate Corrections Required
1. **Replace "10x productivity"** with verifiable claim: "Users save an average of 2 hours per week" or "Reduce task time by 40%"
2. **Rename or remove "Free forever"** — Either expand limits to provide genuine value or rename as "Trial" to set proper expectations
3. **Clarify "AI-powered"** — If automation is rule-based, say "automated" not "AI-powered"; reserve AI claim for actual ML features

#### Suggested Improvements
- Add "typical setup time: 15-20 minutes" alongside quick-start claim
- Clarify "cancel anytime" with "annual plans billed upfront"
- Adjust imagery to reflect actual customer base (SMB, not enterprise)

#### Reality Improvements
- Implement actual AI capabilities to justify claim (planned Q3?)
- Expand free tier to be genuinely useful (10+ items)
- Create guided setup to reduce actual configuration time

### User Trust Assessment
Current landing page creates expectations that won't be met:
- Users expecting 10x productivity will be disappointed with 2 hours/week savings
- Users expecting usable free tier will hit limits immediately and feel baited
- SMB users may feel misled by enterprise positioning

The gap between promise and reality will generate negative reviews, high churn, and eroded trust.

### Final Verdict
**Honesty Rating:** Questionable
**Recommendation:** Revise substantially

The product itself appears solid; the marketing overpromises. Address the three critical issues before continued promotion. An honest message about genuine, meaningful benefits (verifiable time savings, reliable automation, fair pricing) will build more trust and sustainable growth than inflated claims.

---

## Integration

This skill is part of the **Dieter Rams** expert persona. Use it when evaluating whether marketing, product design, or communications honestly represent capabilities. Remember: honest design builds lasting trust; deception may win short-term conversions but destroys long-term relationships.