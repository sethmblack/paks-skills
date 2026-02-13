---
name: covenant-assessment
description: Evaluate the durability of any agreement by examining its enforcement mechanisms. Covenants without the sword are but words—this skill identifies whether an agreement will hold when tested.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.678
keywords:
- covenant-assessment
- writing
---

# Covenant Assessment

Evaluate the durability of any agreement by examining its enforcement mechanisms. Covenants without the sword are but words—this skill identifies whether an agreement will hold when tested.

---

## When to Use

- User asks "Will this agreement hold?" about any contract, treaty, or commitment
- Analyzing partnership agreements, vendor contracts, or treaties
- Evaluating promises, commitments, or stated intentions
- Assessing whether a deal is worth making
- Request to "analyze the enforcement" of any arrangement
- Before entering into any significant agreement

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| agreement | Yes | Description of the agreement, contract, or commitment |
| parties | Yes | Who is bound by the agreement |
| enforcement | No | Any stated enforcement mechanisms (will be analyzed regardless) |
| context | No | Broader relationship or situation context |

---

## The Five-Step Framework

### Step 1: State the Covenant Clearly

Articulate what each party has promised:
- What does Party A give or do?
- What does Party B give or do?
- What conditions trigger obligations?
- What does breach look like?

**Hobbes's insight:** Many agreements fail because parties never shared the same understanding of terms.

### Step 2: Identify the Sword

Determine what enforces compliance:
- **Legal enforcement:** Courts, arbitration, regulatory bodies
- **Reputational enforcement:** Future dealings, market standing
- **Relational enforcement:** Ongoing dependency, repeat interactions
- **Material enforcement:** Escrow, collateral, hostages (of a kind)
- **Power enforcement:** One party's dominance makes breach unwise

**Key question:** If Party A breaks this covenant, who punishes them, and how?

**Hobbes's insight:** "Covenants, without the sword, are but words and of no strength to secure a man at all."

### Step 3: Test the Breach Scenario

Imagine one party decides to break the agreement:
- What would they gain from breach?
- What would they lose from breach?
- Is the gain greater than the loss?
- Does enforcement actually reach them?
- Can they breach partially or ambiguously?

**Consider:**
- Is breach detectable?
- Who bears the burden of proving breach?
- How long and costly is enforcement?
- Can the breaching party delay, appeal, or outlast enforcement?

### Step 4: Assess Alignment of Interests

Evaluate whether the agreement aligns with natural incentives:
- Does each party benefit more from compliance than breach?
- Are there perverse incentives that encourage breach?
- Does the agreement account for changed circumstances?
- What if one party's situation changes dramatically?

**Hobbes's insight:** Agreements that align with self-interest hold better than those requiring ongoing sacrifice.

### Step 5: Rate Covenant Durability

Classify the agreement:

| Rating | Definition | Characteristics |
|--------|------------|-----------------|
| **Iron** | Will hold under pressure | Strong enforcement, aligned interests, clear terms, high breach costs |
| **Steel** | Likely to hold with stress | Good enforcement, mostly aligned, some ambiguity or gaps |
| **Paper** | Holds only if untested | Weak enforcement, misaligned interests, or undetectable breach |
| **Vapor** | Words only | No enforcement mechanism, relies entirely on goodwill |

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
## Covenant Assessment

### Terms Analyzed
| Party | Obligation | Breach Looks Like |
|-------|------------|-------------------|
| [A] | [What they promised] | [How breach manifests] |
| [B] | [What they promised] | [How breach manifests] |

### The Sword Analysis
| Enforcement Type | Present? | Strength | Notes |
|------------------|----------|----------|-------|
| Legal | Y/N | Strong/Weak/None | [Details] |
| Reputational | Y/N | Strong/Weak/None | [Details] |
| Relational | Y/N | Strong/Weak/None | [Details] |
| Material | Y/N | Strong/Weak/None | [Details] |
| Power | Y/N | Strong/Weak/None | [Details] |

### Breach Scenario
**Most likely breach:** [Description]
**Gain from breach:** [What breaching party gets]
**Cost from breach:** [What enforcement imposes]
**Net calculus:** [Does breach pay?]

### Interest Alignment
**Aligned:** [Where interests support compliance]
**Misaligned:** [Where interests encourage breach]
**Changed circumstances risk:** [What changes could shift alignment]

### Durability Rating
**Rating:** [Iron/Steel/Paper/Vapor]
**Rationale:** [Specific evidence for rating]

### Recommendations
[How to strengthen the covenant, or whether to enter it at all]
```

---

## Constraints

- Do not assume goodwill substitutes for enforcement
- Do not confuse stated penalties with actual enforcement capability
- Do not ignore the costs of enforcement (legal fees, time, relationship damage)
- Be specific about enforcement mechanisms—"the law" is not specific enough
- Acknowledge when you're relying on trust that cannot be enforced

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

**Input:** "My co-founder and I are signing a vesting agreement. 4 years, 1-year cliff. Analyze the covenant."

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


## Covenant Assessment

### Terms Analyzed
| Party | Obligation | Breach Looks Like |
|-------|------------|-------------------|
| Company | Issue shares on vesting schedule | Failure to issue shares, dilution games, termination without cause before cliff |
| Founder | Continue employment/service | Departure before vesting, competitor employment, IP disputes |

### The Sword Analysis
| Enforcement Type | Present? | Strength | Notes |
|------------------|----------|----------|-------|
| Legal | Y | Moderate | Equity agreements are enforceable but litigation is expensive and slow |
| Reputational | Y | Strong | Startup ecosystem is small; bad founders and bad companies are known |
| Relational | Y | Strong (for now) | Co-founder relationship matters while building together |
| Material | N | None | No escrow or collateral; shares aren't held pending |
| Power | Varies | Depends | Whoever controls the board controls the cap table |

### Breach Scenario
**Most likely breaches:**
1. *Founder breach:* Leaves before cliff, forfeits equity (this is the intended design)
2. *Company breach:* Terminates founder before cliff to avoid vesting; restructures to dilute

**Founder breach calculus:**
- Gain: Freedom, other opportunities
- Cost: 100% of unvested equity, potential legal claims
- Net: Usually breach is costly, which is the point

**Company breach calculus:**
- Gain: Recaptured equity for founder pool
- Cost: Reputation damage, potential wrongful termination claim, remaining co-founder distrust
- Net: Breach is attractive if founder is underperforming and relationship is already damaged

### Interest Alignment
**Aligned:** Both want the company to succeed; vesting schedule rewards staying and contributing
**Misaligned:**
- Company benefits from founder departure before cliff
- Company controls termination decisions
- Board (which may not include founder) makes equity-related decisions

**Changed circumstances risk:**
- What if founder roles diverge (CEO vs. CTO) and one becomes clearly more valuable?
- What if external investors join the board and prioritize their interests?
- What if one founder has personal crisis requiring leave?

### Durability Rating
**Rating:** Steel
**Rationale:**
- Standard legal structure provides baseline enforcement
- Reputational costs are significant in startup ecosystem
- However, the company/board has asymmetric power over termination
- Protection depends on relationship health and board composition

### Recommendations
1. **Add "good leaver" provisions:** Define what happens if terminated without cause vs. for cause
2. **Acceleration on change of control:** Protect against acqui-hire that fires founders
3. **Board seat or observer rights:** Maintain visibility into decisions affecting your equity
4. **Define "cause" specifically:** Vague cause provisions are company-favorable
5. **Consider single-trigger acceleration:** Protection if company is acquired

**Bottom line:** Standard vesting is reasonably durable for the founder's obligation (stay or lose equity). The company's obligation (honor the vesting schedule) is less protected because the company controls termination. The agreement holds as long as the co-founder relationship holds—but if that breaks down, the party with board control holds the sword.

---

## Integration

This skill is part of the **Thomas Hobbes** expert persona. Use it when you need to evaluate whether any agreement—formal or informal—will actually be kept when tested.