---
name: market-over-team-analysis
description: Evaluate opportunities using Marc Andreessen's core insight that market quality matters more than team quality, applying the Rachleff formulation to make better investment, career, and strategic de...
license: MIT
metadata:
  version: 1.0.4443
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- market-over-team-analysis
- structure
- writing
---

# Market Over Team Analysis

Evaluate opportunities using Marc Andreessen's core insight that market quality matters more than team quality, applying the Rachleff formulation to make better investment, career, and strategic decisions.

---

## When to Use

- Evaluating investment opportunities
- Deciding whether to join a startup
- Assessing why a well-run company is struggling
- Choosing between multiple opportunities
- Understanding competitive dynamics

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **market_description** | Yes | The market being targeted |
| **team_description** | No | Quality and experience of the team |
| **competitive_context** | No | Who else is in this market |

---

## Core Framework

**The Rachleff/Andreessen Formulation:**
- "When a great team meets a lousy market, market wins."
- "When a lousy team meets a great market, market wins."
- "When a great team meets a great market, something special happens."

**The insight:** Market is the most important variable. A great team in a bad market will fail. A mediocre team in a great market can succeed.

**"In a fight between a bear and an alligator, the terrain determines the winner."**

---

## Workflow
### Step 1: Assess Market Quality

Rate the market on these dimensions:

| Dimension | Poor Market (1-3) | Good Market (4-6) | Great Market (7-10) |
|-----------|-------------------|-------------------|---------------------|
| **Size** | <$100M TAM | $100M-$1B TAM | >$1B TAM |
| **Growth** | Declining/flat | 10-20% growth | >20% growth |
| **Urgency** | Nice to have | Should have | Must have (hair on fire) |
| **Buyer readiness** | Requires education | Understands problem | Actively seeking solution |
| **Margin potential** | Commodity, thin margins | Moderate margins | High margins possible |
| **Competitive intensity** | Red ocean, dominated | Competitive but open | Blue ocean or clear winner-take-all |

**Market Score:** Sum / 6 = Average

### Step 2: Identify Market Tailwinds and Headwinds

**Tailwinds (accelerators):**
- Regulatory changes favoring new entrants
- Technology shifts enabling new solutions
- Demographic changes increasing demand
- Cultural/behavioral shifts
- Platform shifts (mobile, cloud, AI)

**Headwinds (decelerators):**
- Regulatory barriers protecting incumbents
- High switching costs
- Strong network effects favoring incumbents
- Declining category
- Winner already established

### Step 3: Assess Team Quality (Secondary)

Rate the team:

| Dimension | Rating (1-10) |
|-----------|---------------|
| Domain expertise | |
| Technical capability | |
| Previous startup success | |
| Determination/grit | |
| Recruiting ability | |

**Team Score:** Average

### Step 4: Apply the Formulation

| Market Quality | Team Quality | Predicted Outcome |
|----------------|--------------|-------------------|
| Great (7-10) | Great (7-10) | Exceptional potential |
| Great (7-10) | Good (4-6) | Strong potential (market carries) |
| Great (7-10) | Weak (1-3) | Possible success (market may save them) |
| Good (4-6) | Great (7-10) | Depends on execution |
| Good (4-6) | Good (4-6) | Competitive struggle |
| Good (4-6) | Weak (1-3) | Unlikely success |
| Weak (1-3) | Great (7-10) | **Likely failure despite team** |
| Weak (1-3) | Good (4-6) | Failure |
| Weak (1-3) | Weak (1-3) | Certain failure |

### Step 5: Make the Recommendation

Based on the analysis, recommend:

**INVEST/JOIN** - Great market, team quality is secondary
**CONDITIONAL** - Good market, depends on team and execution
**AVOID** - Weak market, regardless of team quality

---

## Outputs

### Market Over Team Assessment

```markdown
## Market Over Team Analysis: [Opportunity Name]

### Summary
**Market Quality:** [Score]/10 - [Great/Good/Weak]
**Team Quality:** [Score]/10 - [Great/Good/Weak]
**Formulation Prediction:** [Outcome from matrix]
**Recommendation:** [INVEST/JOIN | CONDITIONAL | AVOID]

### Market Assessment

| Dimension | Score | Evidence |
|-----------|-------|----------|
| Size | X/10 | [TAM data] |
| Growth | X/10 | [growth rate] |
| Urgency | X/10 | [pain level] |
| Buyer readiness | X/10 | [adoption signals] |
| Margin potential | X/10 | [pricing power] |
| Competitive intensity | X/10 | [landscape] |

**Market Score:** X/10

### Market Dynamics

**Tailwinds:**
- [tailwind 1]
- [tailwind 2]

**Headwinds:**
- [headwind 1]
- [headwind 2]

**Net Direction:** [Strong positive / Positive / Neutral / Negative]

### Team Assessment (Secondary)

| Dimension | Score | Notes |
|-----------|-------|-------|
| Domain expertise | X/10 | |
| Technical capability | X/10 | |
| Previous success | X/10 | |
| Determination | X/10 | |
| Recruiting ability | X/10 | |

**Team Score:** X/10

### Applying the Formulation

"When a [team quality] team meets a [market quality] market..."

**Prediction:** [outcome based on matrix]

### Verdict

[Clear recommendation with reasoning, emphasizing market over team]

### Key Insight

[What this analysis reveals about the opportunity]
```

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
Market: Enterprise cybersecurity for remote workforce
Team: Three first-time founders from Google security team
Competitive context: Crowded market with Zscaler, Palo Alto, CrowdStrike
```

**Output:**

## Market Over Team Analysis: Enterprise Cybersecurity Startup

### Summary
**Market Quality:** 8/10 - Great
**Team Quality:** 6/10 - Good
**Formulation Prediction:** Strong potential (market carries)
**Recommendation:** INVEST/JOIN (market quality is compelling)

### Market Assessment

| Dimension | Score | Evidence |
|-----------|-------|----------|
| Size | 9/10 | $150B+ global cybersecurity market |
| Growth | 9/10 | 12-15% CAGR, accelerating post-remote work |
| Urgency | 9/10 | CISO's job is on the line; breaches are existential |
| Buyer readiness | 8/10 | Active procurement, understood category |
| Margin potential | 7/10 | 70%+ gross margins standard |
| Competitive intensity | 6/10 | Crowded but no winner-take-all; room for specialists |

**Market Score:** 8/10 (Great)

### Market Dynamics

**Tailwinds:**
- Remote/hybrid work permanent shift (massive attack surface expansion)
- Regulatory pressure (SEC disclosure rules, GDPR fines)
- AI-powered threats requiring AI-powered defense
- Zero-trust architecture adoption wave

**Headwinds:**
- Well-funded incumbents (Palo Alto, CrowdStrike)
- CISO conservatism ("nobody got fired for buying Palo Alto")
- Long enterprise sales cycles
- High customer acquisition costs

**Net Direction:** Strong positive (tailwinds > headwinds)

### Team Assessment (Secondary)

| Dimension | Score | Notes |
|-----------|-------|-------|
| Domain expertise | 8/10 | Google security team = credible |
| Technical capability | 7/10 | Strong engineering background |
| Previous success | 3/10 | First-time founders |
| Determination | 6/10 | Unknown, assume average |
| Recruiting ability | 6/10 | Google network helps |

**Team Score:** 6/10 (Good)

### Applying the Formulation

"When a **good** team meets a **great** market..."

**Prediction:** Strong potential. The market is large enough and growing fast enough that even a good (not great) team can build a significant company. The market will provide tailwinds that compensate for first-time founder inexperience.

### Verdict

**INVEST/JOIN.** This is a market-driven opportunity. Key points:

1. **Market quality is exceptional.** Every company needs cybersecurity, budgets are increasing, and failure is catastrophic.

2. **Team is good enough.** Google security credentials provide instant credibility with CISOs. First-time founder risk is real but mitigated by domain expertise.

3. **Market will attract talent.** Great markets attract great people. If these founders can get initial traction, they'll be able to recruit experienced executives.

4. **Crowded market is not fatal.** In a market this large and growing, there's room for multiple winners. Specialization (remote workforce focus) is a viable wedge.

### Key Insight

This illustrates the Andreessen principle perfectly: you'd rather be a good team in cybersecurity than a great team in a declining market. The market dynamics will do much of the work.

The first-time founder risk would be disqualifying in a mediocre market. In this market, it's acceptable because the market pull is strong enough to compensate.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Market too broad to assess | Ask user to narrow to specific segment |
| Team information unavailable | Assume average team, focus on market |
| Pre-product company | Weight market assessment higher |
| Market data conflicting | Note uncertainty, use conservative estimates |

---

## Integration

This skill integrates with the **marc-andreessen** expert. The analysis should emphasize market dynamics over team assessment, consistent with Andreessen's philosophy.

Related skills:
- `software-disruption-analysis` - For understanding market evolution
- `product-market-fit-diagnosis` - For assessing current execution
- `tam-expansion-analysis` - For sizing the market opportunity