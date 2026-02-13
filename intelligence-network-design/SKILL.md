---
name: intelligence-network-design
description: Systematically gather intelligence before major decisions. Map what is known, unknown, and must be learned before action.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.4245
repository: https://github.com/sethmblack/paks-skills
keywords:
- intelligence-network-design
- writing
---

# Intelligence Network Design

Systematically gather intelligence before major decisions. Map what is known, unknown, and must be learned before action.

**Source Expert:** Genghis Khan
**Category:** Strategy / Decision Making

---

## When to Use

- Before entering a new market or competitive situation
- Before major acquisitions or partnerships
- When facing an unfamiliar competitor or environment
- Before high-stakes negotiations
- When existing information feels incomplete
- Before any decision where being wrong is costly

**Trigger Phrases:**
- "What do I need to know?"
- "How do I gather information?"
- "What am I missing?"
- "How do I research this market/competitor?"
- "I don't know enough to decide"
- "We're operating blind"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `decision/action` | Yes | What you're preparing to do |
| `target` | Yes | Market, competitor, partner, or situation |
| `current_knowledge` | Yes | What you already know |
| `constraints` | No | Time, budget, ethical boundaries |

---

## Workflow
### Step 1: The Mongol Intelligence Doctrine

> "Before we speak of action, tell me: what do you know for certain? What have you verified? What remains unknown?"

The Mongols operated history's most sophisticated pre-modern intelligence network. Before any campaign:
- Merchants were sent years ahead as scouts and spies
- Detailed information gathered on roads, water sources, defenses
- Political intelligence on internal divisions and potential allies
- Psychological profiles of enemy commanders
- Economic data on cities' wealth and trade connections

Only after this intelligence foundation was complete did armies move.

### Step 2: Framework

**1. Map the Known**
What do you actually know (not believe, not assume)? Separate verified facts from hearsay, opinion, and hope. Be ruthless about the distinction.

**2. Identify the Unknown**
What questions, if answered, would change your decision? What would make you go forward? What would make you retreat? These are your critical unknowns.

**3. Source Classification**
Identify potential sources by type:

| Source Type | Mongol Equivalent | Modern Equivalent |
|-------------|-------------------|-------------------|
| Merchants | Traders who visited enemy cities | Industry contacts, former employees, vendors |
| Scouts | Direct observation teams | On-site visits, product trials, demos |
| Defectors | Enemy subjects who switched sides | Ex-employees, disgruntled partners |
| Captured Documents | Seized records | Public filings, leaked information |
| Allies | Friendly neighboring rulers | Existing customers, partners, investors |

**4. Verify Through Multiple Sources**
One source is a rumor. Two independent sources are information. Three sources that agree are intelligence you can act on. Never rely on a single channel.

**5. Assess Source Reliability**
- What is the source's motive?
- What do they gain from telling you this?
- What are they not telling you?
- How would they know this information?

**6. Update Continuously**
Intelligence is perishable. Markets change. People change. What was true six months ago may not be true today. Build ongoing observation, not one-time research.

---

## Outputs
```markdown
## Intelligence Assessment: [Target/Situation]

### Decision Under Consideration
[What action you're preparing for]

### Known (Verified Facts)
| Fact | Source | Confidence | Last Verified |
|------|--------|------------|---------------|
| [Fact 1] | [Source] | High/Medium/Low | [Date] |

### Unknown (Critical Gaps)
| Question | Why It Matters | Impact If Wrong |
|----------|----------------|-----------------|
| [Question 1] | [Stakes] | [Consequence] |

### Intelligence Collection Plan

| Gap | Source Strategy | Timeline | Owner |
|-----|-----------------|----------|-------|
| [Gap 1] | [How to find out] | [When] | [Who] |

### Source Assessment
| Source | Access | Reliability | Motive |
|--------|--------|-------------|--------|
| [Source 1] | [What they can see] | [Trustworthy?] | [Why telling us?] |

### Decision Readiness
- **Ready to act:** [Yes/No]
- **Critical blockers:** [What must be learned first]
- **Acceptable risk:** [What unknowns we can tolerate]
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
- Decision: Acquire a competitor
- Target: Mid-size SaaS company, 50 employees, $8M ARR
- Current knowledge: Public metrics, press releases, one conversation with CEO
- Constraints: 60-day timeline, cannot contact their customers directly (yet)

**Output:**

## Intelligence Assessment: [Target Company] Acquisition

### Decision Under Consideration
Acquire competitor for $30-40M to consolidate market position and absorb their customer base

### Known (Verified Facts)
| Fact | Source | Confidence | Last Verified |
|------|--------|------------|---------------|
| $8M ARR | CEO direct statement | Medium (unverified) | 30 days ago |
| 50 employees | LinkedIn scrape | Medium | Current |
| Series A funded ($12M) | Crunchbase | High | 2 years ago |
| Key product features | Product trial | High | Current |
| 3 enterprise customers named | Case studies | High | Current |

### Unknown (Critical Gaps)
| Question | Why It Matters | Impact If Wrong |
|----------|----------------|-----------------|
| Actual churn rate | Could indicate product-market fit issues | Overpay by 50%+ if churn is 10%+ |
| Net revenue retention | Expansion vs. contraction | Business model viability |
| Cap table / investor preferences | Deal structure requirements | Deal could fail |
| Key employee retention risk | Value walks out the door | Destroy acquisition value |
| Technical debt level | Integration cost and timeline | Hidden $2-5M cost |
| Customer satisfaction reality | Churn risk post-acquisition | Lose the asset we're buying |

### Intelligence Collection Plan

| Gap | Source Strategy | Timeline | Owner |
|-----|-----------------|----------|-------|
| Churn/NRR | Request financials under NDA; verify with board member contact | Week 1-2 | CFO |
| Cap table | Standard DD process; backdoor check with Series A investor (we know them) | Week 1 | Corp Dev |
| Key employee risk | Interview top 5 people; check LinkedIn activity for job seeking signals | Week 2-3 | VP Eng + HR |
| Technical debt | Code review during DD; talk to their former engineers (2 on LinkedIn) | Week 3-4 | CTO |
| Customer satisfaction | G2 reviews; backdoor industry contacts; Gartner inquiry | Week 1-2 | VP Sales |
| Culture fit | Extended time with leadership; office visit; team lunches | Week 2-4 | CEO |

### Source Assessment
| Source | Access | Reliability | Motive |
|--------|--------|-------------|--------|
| Target CEO | Full (wants deal) | Medium (motivated to sell) | Exit, personal upside |
| Former engineer #1 | Left 6mo ago | Medium-High | Possibly disgruntled, but specific knowledge |
| Series A investor | Good (warm intro) | High | Has info; wants liquidity |
| G2 reviews | Public | Medium | Self-selected reviewers |

### Decision Readiness
- **Ready to act:** No
- **Critical blockers:** Actual financials (churn, NRR), technical debt assessment, key person retention
- **Acceptable risk:** Culture fit ambiguity (can work through), exact cap table details (negotiate later)

---

## Anti-Patterns

**DON'T:**
- Act on single-source information
- Confuse belief with knowledge
- Trust sources without understanding their motives
- Assume the intelligence you have is current
- Let urgency override due diligence
- Ignore information that contradicts your preferred outcome

**INFORMATION FAILURE MODES:**
- "Everyone knows..." - Shared assumptions, not verified facts
- "They told us..." - Single source, possibly motivated
- "It's obvious that..." - Skipping verification
- "We don't have time to check..." - Urgency bias
- "That doesn't fit our thesis..." - Confirmation bias

---

## The Information Sufficiency Test

Before action, answer these three questions:
1. If a hostile critic examined my information, what would they attack?
2. What would I need to see to abandon this course of action?
3. What is my enemy counting on me not knowing?

If you cannot answer these questions, you are not ready to act.

---

## Integration

This skill pairs with:
- **Know Your Enemy (Sun Tzu):** Analysis of gathered intelligence
- **Five Factors Assessment (Sun Tzu):** Strategic framework for what to gather
- **Merit Assessment:** Evaluating human sources and targets