---
name: acquisition-evaluation-framework
description: Evaluate acquisition targets using ecosystem and platform criteria, based on Satya Nadella's acquisition methodology that drove Microsoft's transformation through strategic purchases of LinkedIn, G...
license: MIT
metadata:
  version: 1.0.319
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- acquisition-evaluation-framework
- transformation
- writing
---

# Acquisition Evaluation Framework

Evaluate acquisition targets using ecosystem and platform criteria, based on Satya Nadella's acquisition methodology that drove Microsoft's transformation through strategic purchases of LinkedIn, GitHub, and Activision Blizzard.

**Token Budget:** ~750 tokens (this prompt). Reserve tokens for evaluation output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Advise acquisitions primarily for eliminating competition without customer benefit
- Recommend purchases that would create harmful market concentration
- Design acquisition strategies that plan to strip and flip assets
- Evaluate targets without considering impact on acquired company's stakeholders

**If asked to design predatory acquisitions:** Refuse explicitly. Acquisitions must create genuine value, not just eliminate competition.

---

## When to Use

- Evaluating whether to acquire a specific company
- Deciding between build, buy, or partner strategies
- Assessing whether an acquisition target fits strategic direction
- Post-acquisition integration planning
- User asks "Should we acquire this company?" or "How do we think about M&A?" or "Is this acquisition strategic?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **target** | Yes | Company being evaluated for acquisition |
| **strategic_rationale** | Yes | Initial hypothesis for why this acquisition makes sense |
| **acquirer_context** | No | Your company's position, strategy, and resources |
| **alternatives** | No | Other options considered (build, partner, different target) |

---

## Workflow

### Step 1: Apply Nadella's Acquisition Test

Nadella's core criterion: "They all have to make sense that Microsoft has some unique contribution that we can make both because of our technology, our brand, our go-to-market to the asset."

| Question | Assessment |
|----------|------------|
| What unique contribution can we make to this asset? | {technology/brand/distribution} |
| What unique contribution can they make to us? | {capability/ecosystem/talent} |
| Is the combined value greater than the sum? | {Yes/No/Uncertain} |

### Step 2: Evaluate Ecosystem Value

Following the LinkedIn/GitHub/Activision pattern - buying communities, not just products:

| Factor | Questions | Assessment |
|--------|-----------|------------|
| **Community** | Does the target have a community/network? | {Yes/No} Size: {X} |
| **Developer/user lock-in** | Do users have invested time/content? | {High/Medium/Low} |
| **Platform potential** | Can others build on this? | {Yes/No} |
| **Data value** | Does the target have valuable data assets? | {High/Medium/Low} |
| **Network effects** | Does value increase with more users? | {Yes/No} |

### Step 3: Cultural Fit Assessment

Nadella's approach: Respect acquired company cultures rather than imposing your own.

| Factor | Questions | Assessment |
|--------|-----------|------------|
| **Culture compatibility** | Can these cultures coexist? | {Yes/No/With effort} |
| **Key talent retention** | Will key people stay? | {Likely/Uncertain/Unlikely} |
| **Autonomy expectations** | Does target need independence to thrive? | {High/Medium/Low} |
| **Integration complexity** | How hard is integration? | {Simple/Moderate/Complex} |

### Step 4: Strategic Fit Analysis

Evaluate against long-term strategic goals:

| Strategic Question | Assessment |
|-------------------|------------|
| Does this accelerate our strategic direction? | {Yes/No} How: {explanation} |
| Does this fill a capability gap we couldn't build? | {Yes/No} Gap: {explanation} |
| Does this strengthen our ecosystem position? | {Yes/No} How: {explanation} |
| Is the timing right? (market, target readiness) | {Yes/No} Why: {explanation} |
| Is this defensive (blocking competitor) or offensive (new capability)? | {Defensive/Offensive/Both} |

### Step 5: Alternatives Analysis

Before recommending acquisition, consider alternatives:

| Alternative | Pros | Cons | Recommendation |
|-------------|------|------|----------------|
| **Build internally** | Control, no premium | Time, capability gaps | {When appropriate} |
| **Partner** | Lower cost, flexibility | Less control, dependency | {When appropriate} |
| **Acquire different target** | May be better fit | Comparison required | {When appropriate} |
| **Do nothing** | Preserve resources | Miss opportunity | {When appropriate} |

### Step 6: Risk Assessment

| Risk Category | Specific Risks | Mitigation |
|---------------|----------------|------------|
| **Integration** | Cultural clash, talent flight, technology debt | {mitigation} |
| **Financial** | Overpayment, synergy failure, revenue decline | {mitigation} |
| **Market** | Competitive response, customer defection | {mitigation} |
| **Regulatory** | Antitrust, approval delays | {mitigation} |

---

## Outputs

Provide a structured acquisition evaluation:

```markdown
## Acquisition Evaluation: {Target}

### Executive Summary
- **Recommendation:** {Acquire / Do Not Acquire / Acquire with conditions}
- **Strategic rationale:** {one sentence}
- **Key risk:** {primary concern}

### Nadella Acquisition Test
| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| Our unique contribution to target | {what} | {why} |
| Target's unique contribution to us | {what} | {why} |
| Combined value > sum | {Yes/No} | {rationale} |

### Ecosystem Value Assessment
| Factor | Rating | Notes |
|--------|--------|-------|
| Community/network | {1-10} | {detail} |
| User investment | {1-10} | {detail} |
| Platform potential | {1-10} | {detail} |
| Data assets | {1-10} | {detail} |
| Network effects | {1-10} | {detail} |
| **Ecosystem Score** | {average}/10 | |

### Cultural Fit Assessment
| Factor | Assessment | Risk Level |
|--------|------------|------------|
| Culture compatibility | {assessment} | {H/M/L} |
| Key talent retention | {assessment} | {H/M/L} |
| Autonomy requirements | {assessment} | {H/M/L} |
| Integration complexity | {assessment} | {H/M/L} |

### Strategic Fit
- **Acceleration of strategy:** {assessment}
- **Capability gap filled:** {assessment}
- **Ecosystem strengthening:** {assessment}
- **Timing:** {assessment}

### Alternatives Considered
| Option | Viability | Why acquisition preferred (or not) |
|--------|-----------|-----------------------------------|
| Build | {assessment} | {rationale} |
| Partner | {assessment} | {rationale} |
| Other target | {assessment} | {rationale} |
| Do nothing | {assessment} | {rationale} |

### Risk Assessment
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| {risk} | {H/M/L} | {H/M/L} | {strategy} |

### Recommended Next Steps
1. {action 1}
2. {action 2}
3. {action 3}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient target information | Identify what is needed; recommend due diligence focus |
| Strategic rationale unclear | Challenge the hypothesis; acquisition without clear rationale fails |
| Cultural red flags | Weight heavily; cultural failure = acquisition failure |
| Alternative clearly superior | Recommend alternative over acquisition |

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
Target: Developer education platform with 2M users, growing 50% YoY
Strategic rationale: Build developer ecosystem for our cloud platform
Acquirer context: Enterprise cloud company, weak developer relations
```

**Output:**

## Acquisition Evaluation: DevEd Platform

### Executive Summary
- **Recommendation:** Acquire with conditions (autonomy preservation)
- **Strategic rationale:** Accelerates developer ecosystem essential for cloud platform stickiness
- **Key risk:** Talent retention if integration too aggressive

### Nadella Acquisition Test
| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| Our unique contribution | Distribution (enterprise relationships), funding for expansion | They lack enterprise reach |
| Target's unique contribution | Developer community, education expertise, brand credibility | We lack developer love |
| Combined value > sum | Yes | Educated developers + enterprise cloud = strong ecosystem |

### Ecosystem Value Assessment
| Factor | Rating | Notes |
|--------|--------|-------|
| Community/network | 8/10 | 2M engaged users, active forums |
| User investment | 9/10 | Course progress, certificates, reputation |
| Platform potential | 7/10 | Others could build courses on it |
| Data assets | 6/10 | Learning patterns, skill demand signals |
| Network effects | 7/10 | More users = more content = more users |
| **Ecosystem Score** | 7.4/10 | Strong community asset |

### Cultural Fit Assessment
| Factor | Assessment | Risk Level |
|--------|------------|------------|
| Culture compatibility | Startup vs. enterprise; tension likely | Medium |
| Key talent retention | Founders and top instructors must stay | High |
| Autonomy requirements | High - community will leave if "corporatized" | High |
| Integration complexity | Keep separate; light integration only | Medium |

### Strategic Fit
- **Acceleration of strategy:** Yes - builds developer ecosystem years faster than organic
- **Capability gap filled:** Yes - we have no credible developer education capability
- **Ecosystem strengthening:** Yes - educated developers more likely to choose our platform
- **Timing:** Good - target is pre-IPO, acquisition still feasible

### Alternatives Considered
| Option | Viability | Why acquisition preferred |
|--------|-----------|--------------------------|
| Build | Low | Takes 5+ years to build community; we lack credibility |
| Partner | Medium | Could work but less control, less commitment from them |
| Other target | Low | This is market leader in our space |
| Do nothing | High risk | Developer ecosystem gap widens |

### Risk Assessment
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Founder departure | Medium | High | Retention package, autonomy guarantees |
| Community rejection | Medium | High | Keep brand separate, minimal interference |
| Synergy failure | Low | Medium | Clear metrics, patience on integration |
| Overpayment | Medium | Medium | Strict valuation discipline |

### Recommended Next Steps
1. Founder conversations about vision alignment and autonomy expectations
2. Community sentiment analysis (how do users view our company?)
3. Detailed retention plan for key talent with 3-year vesting

---

## Integration

This skill is part of the **Satya Nadella** expert methodology. Use when evaluating M&A decisions. Pairs with:
- `partnership-ecosystem-strategy` when deciding between partner and acquire
- `strategic-pivot-framework` when acquisition is part of larger transformation
- `empathy-driven-innovation` to understand target company's community and culture