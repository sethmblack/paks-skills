---
name: sovereign-design
description: Design or evaluate governance structures by ensuring clear, undivided authority with defined enforcement mechanisms. Divided sovereignty is no sovereignty—this skill creates governance that can act...
license: MIT
metadata:
  author: sethmblack
  version: 1.0.5020
repository: https://github.com/sethmblack/paks-skills
keywords:
- escalation
- sovereign-design
- writing
---

# Sovereign Design

Design or evaluate governance structures by ensuring clear, undivided authority with defined enforcement mechanisms. Divided sovereignty is no sovereignty—this skill creates governance that can actually govern.

---

## When to Use

- User asks "How should this authority be structured?" for any organization
- Designing governance for a new venture, partnership, or institution
- Evaluating why an existing governance structure is failing
- Resolving disputes about decision-making authority
- Request to "design the governance" or "clarify who decides"
- Any situation where multiple parties claim authority over the same domain

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| domain | Yes | What decisions need to be governed |
| stakeholders | Yes | Who has claims to authority or input |
| constraints | No | Legal, cultural, or practical limitations |
| existing_structure | No | Current governance if any (for evaluation) |

---

## The Six-Step Framework

### Step 1: Define the Sovereign Domain

Clarify exactly what the sovereign will decide:
- What decisions fall within this authority?
- What decisions are explicitly excluded?
- Where does this domain border other authorities?
- What resources does the sovereign control?

**Hobbes's insight:** Ambiguous boundaries create future disputes. Define the kingdom before crowning the king.

### Step 2: Identify Candidate Sovereigns

List who could hold authority:
- Individual leader (CEO, President, Founder)
- Council or board (majority rule, consensus, or supermajority)
- External party (arbitrator, regulator, court)
- Algorithm or rule-based system

**For each, consider:**
- Do they have the information to decide well?
- Do they have the legitimacy to make decisions stick?
- Can they act quickly enough?
- Will their interests align with good decisions?

### Step 3: Apply the Hobbes Test

For any proposed structure, ask:
- **Who decides if the sovereign exceeds its authority?** (If another body, that body is the true sovereign)
- **Can the sovereign be removed?** (If yes, by whom? That's where true power lies)
- **Can two authorities both claim the same decision?** (If yes, you have no sovereign—only competitors)
- **What happens in a tie or deadlock?** (No answer = no governance)

**Hobbes's insight:** "If there be no power erected, or not great enough for our security, every man will and may lawfully rely on his own strength and art for caution against all other men."

### Step 4: Design the Enforcement Mechanism

Ensure the sovereign's decisions can be enforced:
- How are decisions communicated and made binding?
- What happens if someone ignores a sovereign decision?
- Who executes the enforcement?
- What resources back the enforcement?

**Key principle:** The sovereign must have the sword—the ability to compel compliance—or sovereignty is merely advisory.

### Step 5: Address Succession and Limits

Plan for sovereign failure or transition:
- How is a new sovereign selected if needed?
- What triggers removal or replacement?
- Are there any absolute limits (constitutional constraints)?
- Who enforces limits on the sovereign?

**Warning:** Every limit creates a question of enforcement. Don't create checks without answering who checks the checkers.

### Step 6: Document the Design

Produce a clear governance specification that answers:
- Who decides what?
- How are decisions made?
- How are decisions enforced?
- How does authority change hands?

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
## Sovereign Design

### Domain Specification
**Governed decisions:** [List of what the sovereign controls]
**Excluded decisions:** [What is outside sovereign authority]
**Boundaries with other authorities:** [Where this domain ends and others begin]

### Sovereign Selection Analysis
| Candidate | Information Access | Legitimacy | Speed | Interest Alignment |
|-----------|-------------------|------------|-------|-------------------|
| [Option A] | [Assessment] | [Assessment] | [Assessment] | [Assessment] |
| [Option B] | [Assessment] | [Assessment] | [Assessment] | [Assessment] |

### Recommended Sovereign
**Who:** [Recommended holder of authority]
**Rationale:** [Why this choice serves the domain best]

### Hobbes Test Results
| Question | Answer |
|----------|--------|
| Who judges if sovereign exceeds authority? | [Answer] |
| How can sovereign be removed? | [Answer] |
| Are there competing claims? | [Answer] |
| What breaks deadlocks? | [Answer] |

### Enforcement Design
**Decision communication:** [How decisions are made known]
**Non-compliance response:** [What happens if decisions are ignored]
**Enforcement resources:** [What backs the sovereign's authority]

### Succession Protocol
**Trigger for change:** [What causes sovereign transition]
**Selection mechanism:** [How new sovereign is chosen]
**Transition process:** [How authority transfers]

### Governance Summary
[Clear statement of who decides what and how]
```

---

## Constraints

- Do not create divided sovereignty and call it "checks and balances"
- Do not propose limits without specifying who enforces them
- Do not assume consensus will emerge—design for disagreement
- Do not confuse input (consultation) with authority (decision)
- Be specific about deadlock resolution—"discuss further" is not a solution

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

**Input:** "We're starting a 3-person partnership. How should we structure decision-making?"

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


## Sovereign Design

### Domain Specification
**Governed decisions:**
- Strategic direction and pivots
- Major expenditures (>$5,000)
- Hiring and firing
- Equity allocation and dilution
- External agreements and partnerships
- Dissolution or sale

**Excluded decisions:**
- Day-to-day operations within each partner's domain
- Expenses within approved budgets
- Technical decisions within technical domain
- Sales decisions within sales domain

**Boundaries with other authorities:**
- Each partner has sovereign authority within their operational domain
- Partnership-level decisions require the governance structure below

### Sovereign Selection Analysis
| Candidate | Information Access | Legitimacy | Speed | Interest Alignment |
|-----------|-------------------|------------|-------|-------------------|
| Unanimous consent | Full (all partners) | High | Low (deadlock risk) | High (everyone agrees) |
| Majority (2 of 3) | Good | Moderate (1 overruled) | Good | Moderate (2 benefit) |
| Single managing partner | Depends | Low (others feel excluded) | High | Risk of self-dealing |
| Rotating chair | Good | High | Moderate | Varies by issue |
| External board/advisor | Limited | Moderate | Moderate | Less biased but less informed |

### Recommended Sovereign

**Structure:** Tiered sovereignty with defined escalation

**Tier 1 - Operational:** Each partner is sovereign in their domain (no partnership vote needed)

**Tier 2 - Normal business:** Majority rule (2 of 3) for routine partnership decisions

**Tier 3 - Existential:** Unanimous consent for:
- Equity changes
- New partners
- Major debt
- Sale or dissolution
- Domain boundary changes

**Deadlock mechanism:** If Tier 2 deadlocks repeatedly (same issue, 3 consecutive meetings), any partner can invoke arbitration by a pre-selected advisor/board member.

### Hobbes Test Results
| Question | Answer |
|----------|--------|
| Who judges if sovereign exceeds authority? | The tier definitions are clear; exceeded authority can be challenged by any partner and resolved at Tier 3 |
| How can sovereign be removed? | Tier 3 unanimous decision can restructure governance; partner removal requires buyout at predetermined formula |
| Are there competing claims? | No—clear domains with explicit escalation path |
| What breaks deadlocks? | Tier 3 requires unanimity (no deadlock possible—either agree or don't act); Tier 2 has arbitration backstop |

### Enforcement Design
**Decision communication:** Meeting minutes signed by all present; major decisions in writing to all partners within 48 hours
**Non-compliance response:** Written notice of breach; 30-day cure period; if uncured, arbitration with authority to enforce or dissolve
**Enforcement resources:** Operating agreement with arbitration clause; partnership assets as security

### Succession Protocol
**Trigger for change:** Partner departure (voluntary or involuntary), death, or incapacity
**Selection mechanism:** Remaining partners decide (2-person majority) whether to admit new partner or continue as 2-person partnership
**Transition process:** Buyout at formula price over 24 months; non-compete for 2 years; defined IP assignment

### Governance Summary

This partnership has three tiers of sovereignty:
1. **Individual domains:** Each partner is king of their own domain
2. **Normal business:** Two of three partners decide routine matters
3. **Existential matters:** All three must agree, or the matter doesn't proceed

Deadlocks at Tier 2 escalate to arbitration after three attempts. Tier 3 has no deadlock mechanism because unanimity is required—if you can't all agree on something existential, it shouldn't happen.

This design accepts slower decisions on big matters in exchange for clear authority and no partner feeling overruled on issues that could destroy the partnership.

---

## Integration

This skill is part of the **Thomas Hobbes** expert persona. Use it when you need to design governance that will actually work—because divided sovereignty is no sovereignty at all.