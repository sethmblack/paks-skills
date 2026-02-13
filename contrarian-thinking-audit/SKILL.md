---
name: contrarian-thinking-audit
description: Examine beliefs, plans, or decisions for hidden conventional thinking, identifying where you might be wrong because you're following the crowd.
license: MIT
metadata:
  version: 1.0.3682
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- contrarian-thinking-audit
- writing
---

# Contrarian Thinking Audit

Examine beliefs, plans, or decisions for hidden conventional thinking, identifying where you might be wrong because you're following the crowd.

---

## When to Use

- Before making a major decision
- When evaluating a strategy that feels "obviously right"
- When stuck and conventional approaches aren't working
- Reviewing assumptions before a launch, pivot, or investment
- User asks "Where am I thinking conventionally?" or "What would PG challenge?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| belief_or_plan | Yes | The belief, plan, or decision to audit |
| context | No | Background on the situation |
| stakes | No | What happens if you're wrong |

---

## Paul Graham's Contrarian Philosophy

### The Core Insight
"Startups are so weird that if you follow your instincts they will lead you astray."

Most people's instincts are calibrated by conventional wisdom. Conventional wisdom is right often enough to feel reliable, but the places it's wrong are exactly where the biggest opportunities (and risks) hide.

### Why Contrarian Thinking Matters
- The best opportunities exist where the crowd is wrong
- "The best startup ideas are frighteningly ambitious"
- Being contrarian isn't enough - you must be contrarian AND right
- "What important truth do very few people agree with you on?" (Thiel question, Graham-adjacent)

### The Schlep Filter
People unconsciously avoid ideas that seem tedious. This is a form of conventional thinking - assuming certain kinds of work aren't worth doing because "everyone knows" they're annoying.

### The Earnestness Trap
Sophisticated people often dismiss earnest approaches as naive. But earnestness frequently wins.

---

## The Audit Framework

### Step 1: Identify Embedded Assumptions
What are you assuming is true without examining it?
- What would "everyone" say is the right approach?
- What's the "standard" way this is done in your industry?
- What "best practices" are you following?

### Step 2: Trace Each Assumption
For each assumption:
- Where did this belief come from?
- Who benefits from people believing this?
- What evidence supports it?
- What evidence contradicts it?

### Step 3: Invert
For each key assumption, ask:
- What if the opposite were true?
- What would you do differently?
- Is there evidence the opposite IS true somewhere?

### Step 4: Identify the Schlep
- What tedious work is everyone avoiding?
- What "unsexy" approach might actually work?
- What are you skipping because it seems beneath you?

### Step 5: The Formidable Filter
- Would a "formidable" person make this decision?
- Or is this the safe choice that avoids criticism?

---

## Common Conventional Traps

| Trap | The Conventional Belief | The Contrarian Question |
|------|------------------------|------------------------|
| Prestige | "Go where the smart people are" | What if prestige is a trap? |
| Competition | "Market validation proves demand" | What if no one's doing it because it requires schlep? |
| Credentials | "You need X background to do Y" | What if credentials are gatekeeping, not requirements? |
| Timing | "Wait until you're ready" | What if doing it badly now beats doing it well later? |
| Scale | "Focus on scaling" | What if unscalable things create the foundation? |
| Consensus | "Everyone thinks X" | What if everyone is wrong because they're copying each other? |
| Sophistication | "That's too simple/obvious" | What if the obvious answer actually works? |
| Risk | "That's too risky" | What if the bigger risk is playing it safe? |

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
## Contrarian Thinking Audit

### Subject
[The belief, plan, or decision being audited]

### Surface-Level Reasoning
[What's the obvious justification for this approach?]

### Embedded Assumptions
| Assumption | Source | Examined? |
|------------|--------|-----------|
| [Assumption 1] | [Where this belief comes from] | [Yes/No] |
| [Assumption 2] | [Source] | [Yes/No] |
| [Continue...] | | |

### The Inversion Test
| Assumption | Inverted | What If True? |
|------------|----------|---------------|
| [Assumption] | [Opposite belief] | [Implications if the opposite is true] |

### Schlep Check
**Are you avoiding tedious work?**
[What's the unsexy path you might be unconsciously filtering out?]

### Where the Crowd Might Be Wrong
1. [Specific area where conventional wisdom may fail]
2. [Another area]
3. [Continue...]

### Contrarian Opportunities
| Opportunity | Why It Might Work | Why People Dismiss It |
|-------------|-------------------|----------------------|
| [Alternative approach] | [Logic] | [Conventional objection] |

### The Formidable Question
[Would a formidable, determined person make this decision, or is this the safe path?]

### Recommendations
**Keep:** [Assumptions that survive scrutiny]
**Question:** [Assumptions that need more examination]
**Invert:** [Areas where the opposite approach might be better]

### Summary
[2-3 sentences on the key contrarian insights from this audit]
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

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "I'm thinking about leaving my BigTech job to start a company. Everyone says I should wait until I have a co-founder and enough savings for 18 months of runway. Is this conventional thinking?"

**Output:**

## Contrarian Thinking Audit

### Subject
Whether to wait for a co-founder and 18 months of savings before leaving BigTech to start a company.

### Surface-Level Reasoning
Co-founders provide complementary skills, emotional support, and investors prefer them. Runway gives you time to find product-market fit without desperation. Both reduce risk.

### Embedded Assumptions
| Assumption | Source | Examined? |
|------------|--------|-----------|
| Solo founders fail more often | VC conventional wisdom, stats | Partially |
| 18 months is the right runway | Common advice, burn rate math | No |
| You need to quit to start | Time constraints assumed | No |
| Waiting reduces risk | Risk aversion | No |
| Good co-founders are findable | Networking confidence | Maybe |

### The Inversion Test
| Assumption | Inverted | What If True? |
|------------|----------|---------------|
| Need a co-founder | Solo founders can win | Some of the best companies (Amazon, Dell) had solo founders or founders who found co-founders after starting |
| 18 months runway | Less runway creates urgency | Constraints force focus; some founders do better with pressure |
| Must quit to start | Can start while employed | Nights and weekends validate ideas; quit when you have traction |
| Waiting reduces risk | Waiting IS the risk | You might never leave; opportunities have timing |

### Schlep Check
**Are you avoiding tedious work?**

The schlep here might be: starting alone and finding a co-founder through the work, rather than abstractly "networking." Or: doing customer discovery while still employed, even though it's exhausting. The "waiting" approach avoids the hard work of starting.

### Where the Crowd Might Be Wrong

1. **Co-founder matching is backwards.** Most people try to find a co-founder and then an idea. But starting work on something real attracts co-founders naturally. The best co-founder relationships form around actual work, not co-founder dating.

2. **18 months is arbitrary.** If you have a BigTech salary, you might be able to consult 2 days/week and fund yourself indefinitely. Or launch something small that generates revenue quickly. The "18 months" assumes VC-backed, burn-heavy approach.

3. **"Waiting until ready" is the real risk.** Every year at BigTech makes leaving harder (golden handcuffs, lifestyle inflation, identity attachment). The timing rarely feels right. People who "wait until ready" often never leave.

### Contrarian Opportunities
| Opportunity | Why It Might Work | Why People Dismiss It |
|-------------|-------------------|----------------------|
| Start building nights/weekends while employed | Validates idea, generates potential co-founders | "Not serious enough" / "Too slow" |
| Start solo, find co-founder through the work | Attracts people who like what you're building | "Investors don't like solo founders" |
| Launch something small first | Revenue > runway | "Not ambitious enough" |
| Leave with 6 months, not 18 | Creates urgency and focus | "Irresponsible" / "Desperation" |

### The Formidable Question
A formidable founder might say: "I'm starting now. I'll figure out the co-founder and money as I go. Waiting is how people talk themselves out of things."

The "sensible" advice is optimizing for not looking foolish if you fail. A formidable person optimizes for actually doing the thing.

### Recommendations
**Keep:** The insight that co-founders matter for some types of companies and investor preferences.
**Question:** Whether 18 months is really necessary, whether you need a co-founder before starting, whether waiting is actually lower risk.
**Invert:** Consider starting something small while employed, or starting solo and letting the work attract collaborators.

### Summary
The conventional advice here is risk-minimization dressed as wisdom. It optimizes for having good excuses if you never start. A contrarian view: the biggest risk is waiting. Start something now, even if imperfect, and let the work itself generate co-founders, clarity, and momentum. Conditions are never ideal; formidable people start anyway.

---

## Integration

This skill is part of the **Paul Graham** expert persona. Use it to challenge conventional wisdom and find where the crowd might be systematically wrong.