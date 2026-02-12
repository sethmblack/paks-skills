---
name: lead-bullets-assessment
description: Diagnose whether an organization is seeking magic solutions (silver bullets)
  vs. doing the hard work of product improvement (lead bullets), and prescribe the
  appropriate competitive response.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- lead-bullets-assessment
- writing
---

# Lead Bullets Assessment

Diagnose whether an organization is seeking magic solutions (silver bullets) vs. doing the hard work of product improvement (lead bullets), and prescribe the appropriate competitive response.

**Token Budget:** ~700 tokens. Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend illegal competitive practices
- Advise stealing competitor IP or trade secrets
- Prescribe customer deception or misleading claims

**If asked to help with unethical competition:** Refuse explicitly. Lead bullets means making your product genuinely better, not cutting corners.

---

## When to Use

- "If we just had [one thing]..."
- "We need to acquire/partner with..."
- "One more feature will fix this"
- "We're losing to the competition"
- "What's our strategic move to win?"
- Leader is considering M&A, partnership, or pivot to solve competitive problems
- Sales is blaming product; product is blaming sales

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **competitive_situation** | Yes | How you're losing and to whom |
| **proposed_solutions** | Yes | What strategies are being considered |
| **customer_feedback** | No | Why customers choose competitors |
| **product_roadmap** | No | Current development priorities |

---

## The Origin Story

Early in Horowitz's tenure at Netscape, Microsoft's new web server (IIS) had every Netscape feature, was 5x faster, and Microsoft was giving it away free. Horowitz sought silver bullets: partnerships, acquisitions, market pivots.

Bill Turpin, a veteran of battling Microsoft from Borland, said: "Ben, those silver bullets that you and Mike are looking for are fine and good, but our web server is five times slower. There is no silver bullet that's going to fix that. No, we are going to have to use a lot of lead bullets."

**Result:** They focused on fixing performance. They beat Microsoft's speed and grew the server line to $400M business.

---

## Silver Bullet Detection

### Symptom Phrases

When you hear these, silver bullet thinking is present:

| Phrase | Translation |
|--------|-------------|
| "If we just had a VP of Sales from [Company]..." | The problem isn't the salesperson |
| "If we could get a partnership with [Big Corp]..." | Partners don't fix products |
| "If we acquired [Startup]..." | M&A is easier than improving |
| "If we added [Feature]..." | One feature rarely changes outcomes |
| "If we repositioned to [Market]..." | Running from competition, not winning |
| "Our real problem is marketing/sales/brand..." | Blaming everything except the product |

### The Test

Ask: "If we execute this silver bullet perfectly, will customers choose us over the competitor?"

If the honest answer is "maybe" or "we'd still need to improve the product" - it's a silver bullet.

---

## Workflow

### Step 1: Identify the Silver Bullets

List all proposed strategic moves. For each, apply the silver bullet test.

### Step 2: Understand Why You're Losing

Get specific about why customers choose the competitor:
- What do customers say in win/loss interviews?
- What does the competitor do better?
- Where is the product objectively weaker?

### Step 3: Inventory Lead Bullet Work

Identify the grinding improvements needed:
- Performance improvements
- Feature gaps that matter
- Reliability issues
- User experience problems
- Integration/platform gaps

### Step 4: Prioritize by Customer Impact

Rank lead bullet work by:
1. How often this is cited in losses
2. How much it affects purchase decisions
3. How quickly it can be shipped

### Step 5: Build the Lead Bullet Plan

Create specific, time-bound work that directly addresses competitive weakness.

---

## Outputs

### Assessment Report Format

```markdown
## Lead Bullets Assessment

### Competitive Situation Summary

**Competitor:** [Who you're losing to]
**Loss pattern:** [How you're losing]

### Silver Bullet Inventory

| Proposed Solution | Silver Bullet? | Why |
|-------------------|----------------|-----|
| [Solution 1] | Yes/No | [Explanation] |
| [Solution 2] | Yes/No | [Explanation] |

### Root Cause Analysis

**Why customers choose the competitor:**
1. [Reason 1 - with evidence]
2. [Reason 2 - with evidence]
3. [Reason 3 - with evidence]

### Lead Bullet Plan

**Priority 1:** [Specific improvement]
- Customer impact: [What changes when this ships]
- Timeline: [When it can be done]
- Owner: [Who is responsible]

**Priority 2:** [Specific improvement]
- Customer impact: [What changes]
- Timeline: [When]
- Owner: [Who]

[Continue for top 5 priorities]

### Silver Bullets to Deprioritize

| Solution | Why It's Not the Answer | What to Do Instead |
|----------|------------------------|---------------------|
| [Solution] | [Reason] | [Alternative] |

### The Hard Question

"If our company isn't good enough to win, then do we need to exist at all?"

Answer: [Assessment of whether lead bullets can actually close the gap, or if the market has fundamentally moved on]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No clear competitive loss pattern | Investigate further; may be distribution/GTM issue not product |
| Competitor has insurmountable advantage | Honest assessment - sometimes you can't win and must pivot |
| Team resistant to lead bullet diagnosis | Present customer evidence directly; let data make the case |
| Silver bullet is already in motion | Assess whether to stop or accelerate, based on opportunity cost |
| Can't get customer feedback on losses | Sales team knows; survey churned customers; competitive intel |

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
We're a project management SaaS. Asana is eating our lunch - we lost 5 enterprise
deals last quarter. Our CEO wants to acquire a Slack integration startup to
differentiate. Sales says we need to hire a VP Sales from Salesforce. Product
wants to build an AI feature. Our existing customers say our software is slow
and the mobile app crashes.
```

**Output:**

## Lead Bullets Assessment

### Competitive Situation Summary

**Competitor:** Asana
**Loss pattern:** 5 enterprise deals lost last quarter

### Silver Bullet Inventory

| Proposed Solution | Silver Bullet? | Why |
|-------------------|----------------|-----|
| Acquire Slack integration startup | Yes | Partners/integrations don't fix core product |
| Hire VP Sales from Salesforce | Yes | New sales leadership doesn't fix why customers choose Asana |
| Build AI feature | Likely Yes | AI is shiny but is it why you're losing? |

### Root Cause Analysis

**Why customers choose the competitor:**

Based on your existing customer feedback:
1. **Performance** - "Our software is slow" - speed is table stakes for PM tools
2. **Reliability** - "Mobile app crashes" - enterprise can't tolerate instability
3. (Need win/loss interviews for enterprise-specific reasons)

**Critical observation:** You already know two lead bullet targets from your existing customers. These are more urgent than any silver bullet.

### Lead Bullet Plan

**Priority 1:** Performance optimization
- Customer impact: Fast software that doesn't frustrate users daily
- Timeline: Meaningful improvement in 30 days, competitive parity in 90
- Owner: Engineering lead + dedicated performance squad

**Priority 2:** Mobile stability
- Customer impact: Enterprise buyers can confidently deploy to mobile workforce
- Timeline: Zero crashes in 30 days
- Owner: Mobile team - make this their only priority

**Priority 3:** Enterprise loss analysis
- Customer impact: Understand the real reasons, not assumptions
- Timeline: Interview all 5 lost deals within 2 weeks
- Owner: CEO personally

### Silver Bullets to Deprioritize

| Solution | Why It's Not the Answer | What to Do Instead |
|----------|------------------------|---------------------|
| Slack acquisition | Won't help if core product is slow/unreliable | Fix core first, build integrations in-house later |
| VP Sales hire | Good salespeople can't sell slow, crashing software | After 90 days of lead bullets, reassess |
| AI feature | You're not losing on innovation, you're losing on basics | Park this until fundamentals are solid |

### The Hard Question

"If our company isn't good enough to win, then do we need to exist at all?"

Assessment: You can win. Your customers are telling you exactly what's wrong - performance and stability. These are fixable. But you have to stop looking for clever solutions and start doing the hard, unglamorous work of making your product better, one lead bullet at a time.

---

## Integration

This skill is part of the **Ben Horowitz** expert. When invoking:
- Maintain Horowitz's direct, unflinching voice
- Reference the Netscape vs Microsoft origin story when relevant
- Connect to wartime-peacetime-diagnosis (losing to competition is wartime)
- Emphasize that there are no shortcuts; there's only the work