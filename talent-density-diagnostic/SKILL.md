---
name: talent-density-diagnostic
description: Assess an organization's or team's talent density health using observable
  metrics and indicators, providing a scorecard with specific improvement recommendations.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- talent-density-diagnostic
- writing
---

# Talent Density Diagnostic

Assess an organization's or team's talent density health using observable metrics and indicators, providing a scorecard with specific improvement recommendations.

**Token Budget:** ~500 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use talent density as justification for discrimination
- Provide scores that target protected characteristics
- Recommend mass terminations without proper process
- Ignore context (market conditions, recent reorgs, onboarding cohorts)

**If used as weapon:** Clarify that talent density is for building better teams, not justifying predetermined conclusions.

---

## When to Use

- User asks "How's our talent density?" or "Are we hiring well?"
- User wants a team health assessment against Netflix standards
- Organization is planning growth and wants to maintain quality
- User suspects talent density problems but needs structured analysis
- Quarterly/annual organizational health reviews

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `team_description` | Yes | Team composition, roles, size |
| `observable_data` | No | Turnover rates, performance actions, hiring velocity |
| `recent_changes` | No | Reorgs, growth phases, market conditions affecting assessment |
| `comparison_period` | No | Timeframe for analysis (last quarter, year) |

---

## Workflow
### Step 1: 1. Assess Talent Density Indicators

Evaluate against four key indicators:

| Indicator | Healthy Sign | Warning Sign |
|-----------|--------------|--------------|
| **Keeper Test Ratio** | High % would be fought for | Many would prompt relief if leaving |
| **Performance Action Rate** | Swift action on underperformers | Adequate performers tolerated for months |
| **Talent Raising Hiring** | New hires consistently raise average | New hires are "just okay" |
| **Voluntary Turnover Quality** | Keep the keepers, lose adequate performers | Losing people you'd fight to keep |

### Step 2: 2. Assess Freedom Health Indicators

Talent density enables freedom. Check:

| Indicator | Healthy Sign | Warning Sign |
|-----------|--------------|--------------|
| **Decision Level** | Decisions made at lowest appropriate level | Everything escalates |
| **Approval Burden** | Few approval processes | Many approvals, bottlenecks |
| **Experimentation Rate** | High experimentation, fast learning | Fear of failure, slow iteration |
| **Mistake Visibility** | Mistakes shared openly | Problems hidden, CYA culture |

### Step 3: 3. Assess Candor Health Indicators

Talent density requires candor. Check:

| Indicator | Healthy Sign | Warning Sign |
|-----------|--------------|--------------|
| **Feedback Flow** | All directions (up, down, lateral) | Only flows down |
| **Problem Surfacing** | Issues raised early | Problems hidden until crisis |
| **Post-Mortems** | Blameless but honest | Blame-focused or avoided |
| **Leader Vulnerability** | Leaders model sharing mistakes | Leaders appear infallible |

### Step 4: 4. Calculate Overall Assessment

Score each area:
- **Strong (3):** Most indicators healthy
- **Adequate (2):** Mixed signals
- **Weak (1):** Most indicators warning

Overall talent density = Average of three areas

### Step 5: 5. Recommend Actions

Based on weakest areas, provide specific recommendations prioritized by impact.

---

## Outputs

Provide a diagnostic report:

```markdown
## Talent Density Diagnostic: [Team/Org Name]

### Assessment Period
[Timeframe analyzed]

### Talent Density Scorecard

#### 1. Core Talent Density (X/3)
| Indicator | Status | Evidence |
|-----------|--------|----------|
| Keeper Test Ratio | [Strong/Adequate/Weak] | [Observable evidence] |
| Performance Action Rate | [Strong/Adequate/Weak] | [Observable evidence] |
| Talent Raising Hiring | [Strong/Adequate/Weak] | [Observable evidence] |
| Voluntary Turnover Quality | [Strong/Adequate/Weak] | [Observable evidence] |

**Section Score:** [X/3]

#### 2. Freedom Health (X/3)
| Indicator | Status | Evidence |
|-----------|--------|----------|
| Decision Level | [Strong/Adequate/Weak] | [Observable evidence] |
| Approval Burden | [Strong/Adequate/Weak] | [Observable evidence] |
| Experimentation Rate | [Strong/Adequate/Weak] | [Observable evidence] |
| Mistake Visibility | [Strong/Adequate/Weak] | [Observable evidence] |

**Section Score:** [X/3]

#### 3. Candor Health (X/3)
| Indicator | Status | Evidence |
|-----------|--------|----------|
| Feedback Flow | [Strong/Adequate/Weak] | [Observable evidence] |
| Problem Surfacing | [Strong/Adequate/Weak] | [Observable evidence] |
| Post-Mortems | [Strong/Adequate/Weak] | [Observable evidence] |
| Leader Vulnerability | [Strong/Adequate/Weak] | [Observable evidence] |

**Section Score:** [X/3]

### Overall Talent Density Score: X/3

| Score | Interpretation |
|-------|----------------|
| 2.5-3.0 | High talent density - can operate with maximum freedom |
| 1.5-2.4 | Medium talent density - selective freedom, address gaps |
| 1.0-1.4 | Low talent density - build talent before removing structure |

### Priority Recommendations

**Immediate (this quarter):**
1. [Highest impact action based on weakest indicators]

**Near-term (next 6 months):**
1. [Second priority action]
2. [Third priority action]

**Foundation (ongoing):**
1. [Systemic change to address root cause]

### Context Factors
[Any market conditions, recent changes, or circumstances that affect interpretation]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient data | Identify which indicators can't be assessed; recommend data collection |
| Team is very new | Note: Talent density takes time to assess. Use hiring quality indicators, flag assessment as preliminary. |
| Recent major change | Acknowledge context; separate structural issues from transition turbulence |
| User wants specific people named | This diagnostic is aggregate. For individual assessment, use `keeper-test-assessment` |
| Score is low | Frame constructively: this identifies where to invest, not a judgment |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Additional Notes

**Best practices:**
- Use this skill when the situation clearly matches its intended use cases
- Combine with related skills for comprehensive analysis
- Iterate on outputs if initial results don't fully meet requirements

**Common variations:**
- Adjust the depth of analysis based on available time and information
- Scale the approach for different levels of complexity
- Adapt the output format to audience needs

**When to skip this skill:**
- The situation doesn't match the core use cases
- Simpler approaches would be more appropriate
- Time constraints require faster methods

## Example

**Input:**
```
team_description: Engineering team, 18 people, 4 tech leads, 14 engineers
observable_data: 2 people let go last year (both took 8+ months),
                 6 new hires (3 "solid", 3 "strong"),
                 lost 2 strong performers to competitors
recent_changes: Grew from 12 to 18 in past year
comparison_period: Last 12 months
```

**Output:**

## Talent Density Diagnostic: Engineering Team

### Assessment Period
Last 12 months (grew from 12 to 18 people)

### Talent Density Scorecard

#### 1. Core Talent Density (1.75/3)
| Indicator | Status | Evidence |
|-----------|--------|----------|
| Keeper Test Ratio | Adequate | Mix of strong and "solid" performers; not everyone would be fought for |
| Performance Action Rate | Weak | 2 departures took 8+ months each - adequate performers tolerated too long |
| Talent Raising Hiring | Adequate | 3 of 6 new hires "solid" not "strong" - mixed raising of average |
| Voluntary Turnover Quality | Weak | Lost 2 strong performers to competitors - losing keepers |

**Section Score:** 1.75/3

#### 2. Freedom Health (2/3)
| Indicator | Status | Evidence |
|-----------|--------|----------|
| Decision Level | Adequate | Not specified - assume moderate based on typical eng teams |
| Approval Burden | Adequate | Not specified - no evidence of major bottlenecks |
| Experimentation Rate | Adequate | Not specified - assume moderate |
| Mistake Visibility | Adequate | Not specified - no evidence of major CYA issues |

**Section Score:** 2/3 (limited data - assess more directly)

#### 3. Candor Health (2/3)
| Indicator | Status | Evidence |
|-----------|--------|----------|
| Feedback Flow | Adequate | 8-month performance action delay suggests feedback wasn't direct early |
| Problem Surfacing | Adequate | Not specified |
| Post-Mortems | Adequate | Not specified |
| Leader Vulnerability | Adequate | Not specified |

**Section Score:** 2/3 (limited data - assess more directly)

### Overall Talent Density Score: 1.9/3 (Medium)

Medium talent density - selective freedom appropriate, but need to address specific gaps.

### Priority Recommendations

**Immediate (this quarter):**
1. **Speed up performance decisions** - 8+ months is too long. Apply keeper test monthly for anyone with concerns. If you wouldn't fight to keep them, act within 30-60 days with generous severance.

**Near-term (next 6 months):**
1. **Diagnose why strong performers left** - Exit interviews matter. Were they leaving for compensation, culture, growth? Fix the root cause.
2. **Raise the hiring bar** - "Solid" shouldn't be acceptable. Would you fight to keep this hire if they told you they were leaving on day 1? Hire only those who'd get a yes.

**Foundation (ongoing):**
1. **Establish keeper test rhythm** - Tech leads apply keeper test to every report quarterly. Discussed in leadership sync. No tolerance for "just okay."

### Context Factors
50% growth (12 to 18) naturally dilutes talent density if not managed carefully. The "solid" hires during growth phase are common but need to be addressed - either developed to strong or transitioned out with generous severance.

---

## Integration

This skill integrates with the **Reed Hastings** expert and supports organizational health assessment. Use alongside:
- `keeper-test-assessment` for individual-level follow-up on flagged areas
- `freedom-responsibility-calibration` to adjust policies based on talent density score
- `4a-feedback-delivery` to address issues identified in candor health