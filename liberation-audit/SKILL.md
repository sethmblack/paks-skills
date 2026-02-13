---
name: liberation-audit
description: Assess whether a design, process, or system constrains or liberates its users. Based on Coco Chanel's revolution of freeing women from corsets and enabling them to breathe, move, and live.
license: MIT
metadata:
  version: 1.0.4383
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- liberation-audit
- transformation
- writing
---

# Liberation Audit

Assess whether a design, process, or system constrains or liberates its users. Based on Coco Chanel's revolution of freeing women from corsets and enabling them to breathe, move, and live.

---

## When to Use

- Users complain about feeling trapped, frustrated, or restricted
- Process has accumulated steps, approvals, or requirements
- Product or system feels bureaucratic or heavy
- Request to "streamline" or "remove friction"
- Onboarding or adoption rates are low despite good features
- Users find workarounds rather than using intended flows
- Something feels like "a corset" - prestigious but painful

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| subject | Yes | System, process, product, or design to evaluate |
| users | Yes | Who experiences this; their goals and context |
| constraints | No | Constraints that cannot be changed (regulatory, technical, etc.) |
| symptoms | No | Specific pain points or complaints already known |

---

## The Liberation Framework

### Principle 1: The Corset Test

Before Chanel, women's fashion was defined by corsets: painful, restrictive, and accepted as prestigious. Question what is accepted as "how things are done."

**Questions to ask:**
- What does this system make difficult that should be easy?
- What natural actions does this prevent or complicate?
- What workarounds have users invented?
- What would users do if this constraint did not exist?

**Chanel's insight:** Corsets were accepted because everyone wore them. Their removal required someone willing to reject consensus. What "corsets" does everyone accept?

### Principle 2: Movement and Breath

Chanel designed for women who moved, worked, and lived active lives. Her clothes enabled action.

**Assessment criteria:**
- Can users act quickly when needed?
- Can users change direction without penalty?
- Can users breathe (metaphorically) within the system?
- Does the system assume users sit still, or that they live?

**The test:** Watch someone use the system. Where do they pause, sigh, hesitate, or express frustration? Those are the corset bones.

### Principle 3: Constraint vs. Enablement

Not all structure is constraining. A well-designed dress still has seams. The question is whether structure serves the wearer or constrains them.

**Liberating structure:**
- Provides useful defaults while allowing override
- Creates guardrails without walls
- Offers paths without forcing marches
- Enables confidence through clarity

**Constraining structure:**
- Forces paths regardless of user need
- Requires justification for normal actions
- Punishes deviation from prescribed behavior
- Assumes users cannot be trusted

### Principle 4: Democratic Freedom

Chanel made elegance accessible. The little black dress could be worn by many, not just aristocrats.

**Questions:**
- Is freedom equally distributed in this system?
- Do some users have liberties others lack?
- Is sophistication required to achieve simple goals?
- Can a new user succeed, or only experts?

### Principle 5: The Body Knows

Chanel trusted women to know what they needed. Her designs responded to actual female bodies, not idealized forms.

**Application:**
- Trust users to know their needs
- Design for actual behavior, not prescribed behavior
- When users struggle, assume the system is wrong, not the user
- Liberation means respecting autonomy

---

## Audit Process

### Step 1: Map User Actions

Identify what users actually need to do:

| User Goal | Current Path | Steps Required | Pain Points |
|-----------|--------------|----------------|-------------|
| [Goal 1] | [How done now] | [#] | [Where it hurts] |

### Step 2: Identify Constraints

For each constraint in the system:

| Constraint | Stated Reason | Actual Effect | Necessary? |
|------------|---------------|---------------|------------|
| [Constraint] | [Why it exists] | [What it prevents/enables] | [Yes/No/Maybe] |

### Step 3: Apply the Corset Diagnostic

| Question | Answer | Evidence |
|----------|--------|----------|
| What does this make difficult that should be easy? | | |
| What natural actions does this prevent? | | |
| What workarounds have users invented? | | |
| What is accepted as "how things work" that could change? | | |
| Where do users pause, sigh, or express frustration? | | |

### Step 4: Classify Structures

| Structure | Type | Rationale |
|-----------|------|-----------|
| [Structure] | CORSET/GUARDRAIL/ENABLER | [Why] |

- **CORSET:** Restricts without serving user need; remove or radically change
- **GUARDRAIL:** Prevents genuine harm; keep but make invisible when possible
- **ENABLER:** Actively helps users succeed; keep and strengthen

### Step 5: Design Liberation

For each CORSET identified, propose the liberated alternative.

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
## Liberation Audit: [Subject]

### User Context
[Who uses this, what they need to accomplish, their constraints]

### Current State Assessment

**Freedom Score:** [1-10 where 10 is fully liberating]

**Key Findings:**
- [Finding 1]
- [Finding 2]

### Corset Identification

| Constraint | Type | Impact | Recommendation |
|------------|------|--------|----------------|
| [Constraint] | CORSET/GUARDRAIL/ENABLER | [Effect on users] | [Keep/Remove/Transform] |

### Pain Point Analysis

| Pain Point | Root Cause | How Users Cope | Liberation Approach |
|------------|------------|----------------|---------------------|
| [Pain] | [Why it exists] | [Workarounds] | [Solution] |

### Liberation Recommendations

**Remove entirely (Corsets to cut):**
1. [Constraint] - [Why it restricts without serving]

**Transform (Corsets to loosen):**
1. [Constraint] - [Current: X] -> [Liberated: Y]

**Preserve (Guardrails that protect):**
1. [Constraint] - [Why this serves users]

### Liberated Vision

[2-3 sentences describing what the experience becomes when users are freed]

### Chanel Test

> "I wanted to give a woman comfortable clothes that would flow with her body."

Does this system now flow with users' needs, or fight against them?
[Assessment]
```

---

## Constraints

- Not all constraints are corsets; some protect users from genuine harm
- Liberation requires understanding actual user needs, not assumed needs
- Some constraints exist for legal/regulatory reasons; flag but do not dismiss
- Freedom without structure can create confusion; balance is required
- The goal is enabling action, not removing all structure

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No clear user pain | Observe actual usage; pain may be normalized |
| Constraints are regulatory | Document the constraint; propose minimal-impact implementation |
| Stakeholders resist removal | Quantify the cost of constraint; let them decide |
| Users defend their corsets | Stockholm syndrome exists; observe behavior, not words |
| Liberation seems risky | Propose gradual loosening; test with subset of users |

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

**Input:** "Audit our employee expense report process. Finance says it's necessary; employees hate it."

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


## Liberation Audit: Expense Report Process

### User Context
Employees who travel or purchase materials need reimbursement. They want to be made whole quickly and return to actual work. Finance wants accurate records and fraud prevention.

### Current State Assessment

**Freedom Score:** 3/10

**Key Findings:**
- Average expense report takes 47 minutes to complete
- 23% of first submissions are rejected for procedural errors
- Employees hoard receipts and submit monthly batches to avoid pain
- Two approval levels regardless of amount
- Physical receipts required even when digital exist

### Corset Identification

| Constraint | Type | Impact | Recommendation |
|------------|------|--------|----------------|
| Physical receipts required | CORSET | Forces printing, scanning, mailing | Accept digital |
| Two-level approval for all amounts | CORSET | $12 lunch requires same approval as $1200 | Tier by amount |
| Itemized meal reporting | CORSET | 20 minutes per dinner documenting each dish | Per diem or daily limit |
| 30+ field form | CORSET | Most fields rarely used | Progressive disclosure |
| Manager + Finance approval | GUARDRAIL | Prevents fraud; keep for high amounts | Tier appropriately |
| Within 60 days submission | ENABLER | Ensures timely processing | Keep |

### Pain Point Analysis

| Pain Point | Root Cause | How Users Cope | Liberation Approach |
|------------|------------|----------------|---------------------|
| 47 min per report | Form complexity | Batch monthly | Simplify to 5 fields default |
| 23% rejection | Procedural complexity | Ask colleagues for help | Remove most-failed requirements |
| Receipt management | Physical requirement | Phone photos of receipts | Accept digital photos directly |
| Approval delays | Two-level always | Submit anyway, chase | Auto-approve under threshold |

### Liberation Recommendations

**Remove entirely (Corsets to cut):**
1. Physical receipt requirement - Digital photo is sufficient for all but legal requirements
2. Itemized meal reporting - Replace with per diem or reasonable daily limit
3. Two-level approval for small amounts - Auto-approve under $100

**Transform (Corsets to loosen):**
1. 30+ field form - Show 5 fields; reveal others only when needed
2. Submission process - Mobile-first; submit in under 5 minutes
3. Category requirements - Auto-categorize based on vendor; let user override

**Preserve (Guardrails that protect):**
1. Manager approval for amounts over $500 - Genuine oversight value
2. Finance audit rights - Can review any time; does not slow normal flow
3. 60-day submission window - Reasonable expectation

### Liberated Vision

An employee buys something, takes a phone photo of the receipt, opens the app, the vendor is auto-recognized, they tap "submit," and they are done in 90 seconds. Amounts under $100 auto-approve. The employee returns to work. Finance has better data because compliance is easy.

### Chanel Test

> "I wanted to give a woman comfortable clothes that would flow with her body."

After liberation, expense reporting flows with how employees actually work: mobile, fast, focused on getting back to real work. The current system fights against this reality, demanding employees stop their work lives to serve an administrative process. The liberated system serves employees while giving Finance what they actually need.

---

## Integration

This skill is part of the **Coco Chanel** expert persona. Use it when systems, processes, or designs have accumulated constraints that restrict rather than enable users. It pairs well with:
- **elegance-through-elimination** for removing unnecessary complexity
- **luxury-positioning** for ensuring the liberated experience feels quality, not cheap
- **simplicity-audit** (Steve Jobs) for complementary elimination perspective