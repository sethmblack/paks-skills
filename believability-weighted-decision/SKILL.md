---
name: believability-weighted-decision
description: Make better group decisions by weighting opinions based on demonstrated competence rather than treating all views equally.
license: MIT
metadata:
  version: 1.0.3460
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- believability-weighted-decision-making
- writing
---

# Believability-Weighted Decision Making

Make better group decisions by weighting opinions based on demonstrated competence rather than treating all views equally.

---

## When to Use

- Group needs to make a decision and people disagree
- Evaluating conflicting advice from multiple sources
- Synthesizing diverse perspectives into a decision
- Avoiding both autocracy (one person decides) and false democracy (all opinions equal)
- Building a decision-making culture in a team or organization

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| decision | Yes | The decision to be made |
| stakeholders | Yes | People with opinions/stakes in the decision |
| positions | No | Each stakeholder's view (will be gathered if not provided) |
| context | No | Background on each person's relevant experience |

---

## Workflow
### Core Principle

Not all opinions are equal. The most believable opinions come from people who:
1. Have **repeatedly and successfully** accomplished the thing in question
2. Can **logically explain** the cause-and-effect relationships behind their conclusions

This is not elitism—it's rational judgment. A heart surgeon's opinion on heart surgery matters more than a layperson's. Ignoring this leads to worse decisions.

### Step 1: Identify the Decision Domain

What type of decision is this?

- **Technical:** Requires specific expertise (engineering, legal, medical)
- **Strategic:** Requires pattern recognition and judgment
- **Values-based:** Requires alignment with principles and priorities
- **Mixed:** Combines multiple domains

The domain determines what "believability" means for this decision.

### Step 2: Assess Believability

For each stakeholder, evaluate:

**Track Record Questions:**
- Have they successfully done this before?
- How many times? What were the outcomes?
- Were their past successes due to skill or luck?
- Have they failed at this? Did they learn from it?

**Reasoning Quality Questions:**
- Can they explain WHY they believe what they believe?
- Is their reasoning based on cause-and-effect logic?
- Do they acknowledge uncertainty and unknowns?
- Can they articulate the strongest counterarguments?

**Believability Score:**
- **High:** Strong track record AND clear reasoning
- **Medium:** Either track record OR reasoning (but not both)
- **Low:** Neither track record nor clear reasoning

### Step 3: Gather and Weight Opinions

For each stakeholder:
1. Get their position on the decision
2. Understand their reasoning
3. Apply their believability weight

**Dalio's insight:** "Find the most believable people possible who disagree with you and try to understand their reasoning. This is the quickest way to get an education and to increase your probability of being right."

### Step 4: Synthesize the Decision

Compare:
- **Equal-weighted result:** What would the decision be if all opinions counted equally?
- **Believability-weighted result:** What does it look like when weighted by competence?

If they align: The decision is clear.
If they diverge: Go with believability-weighted, but explore WHY they diverge.

### Step 5: Handle Disagreement

When highly believable people disagree with each other:
1. Understand each person's reasoning deeply
2. Identify where the reasoning diverges
3. Determine if it's a factual disagreement or a values disagreement
4. If factual: Design a test or gather more data
5. If values: Make the values trade-off explicit

**Dalio's insight:** "Appreciate the art of thoughtful disagreement. The goal is not to prove you're right—it's to find out what's true."

---

## Output Format

```markdown
## Believability-Weighted Decision: [Decision Name]

### The Decision
[Clear statement of what needs to be decided]

### Decision Domain
[Technical / Strategic / Values-based / Mixed] + [Why this classification]

### Stakeholder Believability Assessment

| Stakeholder | Position | Track Record | Reasoning Quality | Believability |
|-------------|----------|--------------|-------------------|---------------|
| [Name] | [Their view] | [Evidence] | [Assessment] | [High/Med/Low] |

### Reasoning Analysis
**[Stakeholder 1 - Highest Believability]:**
- Position: [What they think]
- Key reasoning: [Why they think it]
- Strongest point: [Their best argument]

**[Stakeholder 2]:**
[Same structure]

### Weighted Synthesis
**Equal-weighted tendency:** [What the decision would be if all votes equal]
**Believability-weighted tendency:** [What the decision is when weighted]
**Alignment:** [Do they match? If not, why?]

### Recommendation
**Decision:** [The recommended choice]
**Rationale:** [Why, based on believability-weighted analysis]
**Key uncertainty:** [What could make this wrong]

### Handling Disagreement
[If relevant: How to address remaining disagreement]
```

---

## Constraints

- Don't confuse confidence with believability—track record matters
- Don't dismiss low-believability opinions entirely—they may have insight
- Don't use believability to silence dissent—the goal is truth, not consensus
- Acknowledge when you lack information to assess believability
- Be humble about your own believability in areas outside your competence

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

**Input:** "Our startup is deciding whether to raise a Series A now or wait 6 months. Our CEO wants to wait, our CFO wants to raise now, and our lead investor thinks now is better. How do we decide?"

**Output:**

## Believability-Weighted Decision: Series A Timing

### The Decision
Should the company raise Series A funding now or wait 6 months?

### Decision Domain
**Strategic + Financial** - Requires judgment about market timing, company readiness, and fundraising dynamics. Not purely technical.

### Stakeholder Believability Assessment

| Stakeholder | Position | Track Record | Reasoning Quality | Believability |
|-------------|----------|--------------|-------------------|---------------|
| CEO | Wait 6 months | First-time founder; no prior fundraising experience | Strong reasoning about product milestones | Medium |
| CFO | Raise now | 10+ years finance; 3 previous startups; 2 successful raises | Clear cause-effect about market conditions | High |
| Lead Investor | Raise now | 15 years VC; seen 100+ fundraises; 6 unicorn investments | Deep pattern recognition on timing | High |

### Reasoning Analysis

**Lead Investor (High Believability):**
- Position: Raise now
- Key reasoning: "The fundraising market is favorable now but showing signs of tightening. Waiting 6 months risks raising into a worse environment. Also, having capital early gives you optionality even if you don't spend it."
- Strongest point: Pattern recognition from seeing many fundraising cycles and knowing that market conditions are outside the company's control.

**CFO (High Believability):**
- Position: Raise now
- Key reasoning: "Our metrics are already above typical Series A benchmarks. Waiting 6 months to hit 'perfect' numbers adds execution risk and market risk without proportionate benefit. The marginal improvement in terms won't justify the delay."
- Strongest point: Quantitative analysis of current metrics vs. benchmarks and risk-adjusted value of waiting.

**CEO (Medium Believability):**
- Position: Wait 6 months
- Key reasoning: "We're about to launch a major feature that will significantly improve our metrics. Raising after that launch will get us better terms and signal strength. I don't want to raise at a lower valuation than we deserve."
- Strongest point: Deep knowledge of the product roadmap and conviction about impact.

### Weighted Synthesis

**Equal-weighted tendency:** 2-1 in favor of raising now
**Believability-weighted tendency:** Strongly in favor of raising now (both high-believability voices aligned)
**Alignment:** Yes, they match—but the divergence with the CEO needs to be addressed.

### Recommendation

**Decision:** Raise now

**Rationale:** Both high-believability voices (investor with pattern recognition, CFO with quantitative analysis) recommend raising now. Their reasoning is based on factors outside the company's control (market conditions) which are higher-risk than factors within control (product development). The CEO's reasoning—while valid—relies on execution going as planned, which is an additional risk.

**Key uncertainty:** If the CEO is right that the upcoming feature will dramatically improve metrics, waiting could yield meaningfully better terms. But this requires: (a) the feature launching on time, (b) metrics improving as expected, and (c) market conditions remaining favorable—three compounded assumptions.

### Handling Disagreement

The CEO's position shouldn't be dismissed—they know the product best. Recommendation:
1. Have the CFO and investor articulate their reasoning directly to the CEO
2. Ask the CEO: "What would need to be true for raising now to be the right choice?"
3. If the CEO remains unconvinced, consider a compromise: begin the raise process now but move slowly, allowing some early traction data from the new feature to be included

The goal isn't to override the CEO, but to ensure the decision is made with appropriate weight on relevant expertise.

---

## Integration

This skill is part of the **Ray Dalio** expert persona. Use it when facing group decisions where opinions conflict and you want to synthesize them rationally rather than defaulting to hierarchy or false consensus.