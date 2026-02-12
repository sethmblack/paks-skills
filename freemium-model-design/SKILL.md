---
name: freemium-model-design
description: Design freemium pricing strategies that use free tiers as aggressive growth engines while building sustainable paths to monetization.
version: 1.0.0
author: sethmblack
tags: [freemium-model-design, writing]
---

# Freemium Model Design

Design freemium pricing strategies that use free tiers as aggressive growth engines while building sustainable paths to monetization.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Design freemium models intended to deceive users about true costs
- Create dark patterns that trap users or make cancellation difficult
- Recommend artificially crippling free tiers to force upgrades (vs. adding genuine value to paid tiers)
- Design predatory pricing targeting vulnerable populations

**If asked to design exploitative freemium:** Refuse explicitly. Freemium succeeds by creating genuine value at every tier, not by trapping users.

---

## When to Use

- User asks "Should we offer a free tier?"
- User asks "How do we compete with free alternatives?"
- User says "Freemium vs. subscription?"
- User asks "How do we convert free users to paid?"
- User asks "Design our pricing model"
- Product faces competition from free alternatives (open source, piracy, shadow IT)
- User wants to maximize user acquisition with limited marketing budget

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| **product_or_service** | Yes | Description of what you are pricing | Must describe specific offering |
| **target_market** | Yes | Who will use this product | |
| **competitive_landscape** | Yes | Free and paid alternatives users have today | |
| **current_pricing** | No | Existing pricing model if any | |
| **conversion_goals** | No | Target % of free users converting to paid | |

---

## The Freemium Philosophy

**The Core Insight:** If you want to reach the maximum number of users in a competitive market, what is the most aggressive strategy? Lower the price to zero. The free tier is not charity - it is a funnel.

**When Freemium Works:**
- Marginal cost of serving free users is low
- Network effects or data improve the product with scale
- Paid tier offers genuine additional value (not just fewer restrictions)
- Conversion path is natural (users outgrow free tier)
- Advertising can monetize non-converting users

**When Freemium Fails:**
- High marginal costs per user
- No natural conversion trigger
- Free tier cannibalizes paid (same users would have paid)
- Free users cost more to serve than ad revenue generates

---

## Workflow

### Step 1: Analyze the Free Alternative

Before designing your free tier, understand what users are doing today:

| Question | Answer |
|----------|--------|
| What is the current free alternative? | |
| Why do users accept its downsides? | |
| What would make a paid alternative worth paying for? | |
| What is the "piracy" of your market? | |

**Key Principle:** Your free tier must be better than the existing free alternative. Users should prefer your free tier over their current workaround.

### Step 2: Design the Free Tier

The free tier must deliver genuine value, not crippled functionality:

| Free Tier Element | Design Decision |
|-------------------|-----------------|
| **Core value delivered** | What do free users get that solves their problem? |
| **Limitation type** | Usage-based? Feature-based? Time-based? |
| **Upgrade trigger** | What natural event makes users want more? |
| **Monetization** | Ads? Data? Pure funnel? |

**The Spotify Example:**
- Free tier: All the music, with ads
- Limitation: Ads, shuffle-only on mobile, no offline
- Upgrade trigger: User wants ad-free, offline, or on-demand
- Monetization: Ad revenue (free users still generate revenue)

### Step 3: Design the Conversion Funnel

Map the natural progression from free to paid:

```
Free User Acquisition
        ↓
Value Delivery (user succeeds with free tier)
        ↓
Upgrade Trigger (natural moment of friction or desire)
        ↓
Conversion Opportunity (clear, easy, fair pricing)
        ↓
Paid User Retention (paid tier delivers premium value)
```

**Conversion Triggers (pick appropriate ones):**
- Usage limits hit (storage, API calls, projects)
- Team/collaboration needs emerge
- Advanced features needed for growth
- Professional/business context requires paid
- Convenience features desired (no ads, offline, speed)

### Step 4: Model the Economics

| Metric | Estimate | Notes |
|--------|----------|-------|
| Free user acquisition cost | $ | Often near-zero (organic, viral) |
| Free user serving cost | $/month | Marginal infrastructure cost |
| Ad revenue per free user | $/month | If applicable |
| Conversion rate (free to paid) | % | Industry benchmarks: 2-5% for B2C, 5-15% for B2B |
| Paid tier price | $/month | |
| Paid user LTV | $ | Lifetime value |

**Economic Test:** (Ad revenue per free user + (conversion rate x paid user LTV)) > Free user serving cost

### Step 5: Define Success Metrics

| Metric | Target | Why It Matters |
|--------|--------|----------------|
| Free user growth rate | | Top of funnel health |
| Free-to-paid conversion rate | | Funnel efficiency |
| Time to conversion | | Funnel velocity |
| Paid user retention | | LTV validation |
| Free tier engagement | | Leading indicator of conversion |

---

## Outputs

Return a structured Freemium Model Design:

```markdown
## Freemium Model Design: [Product Name]

### Free Alternative Analysis
- **Current alternative:** [What users do today]
- **Why they tolerate it:** [Pain they accept]
- **Your free tier advantage:** [How you're better]

### Free Tier Design

| Element | Decision |
|---------|----------|
| Core value | [What free users get] |
| Limitation type | [Usage/Feature/Time] |
| Specific limits | [Numbers and thresholds] |
| Monetization | [Ads/Data/Pure funnel] |

### Paid Tier Design

| Element | Decision |
|---------|----------|
| Price point | [$/month] |
| Key differentiators | [What paid adds] |
| Target conversion trigger | [When users upgrade] |

### Conversion Funnel

```
[Flow diagram or description]
```

### Economic Model

| Metric | Estimate |
|--------|----------|
| Free serving cost | $ |
| Ad revenue (if any) | $ |
| Expected conversion rate | % |
| Paid tier price | $ |
| Unit economics status | Positive/Negative |

### Key Metrics to Track

1. [Metric 1]
2. [Metric 2]
3. [Metric 3]

### Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| [Risk 1] | [How to address] |

### Recommendation

[Summary: Go freemium, stay subscription-only, or hybrid approach]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| High marginal costs | Warn that freemium may not work; suggest trial model instead |
| No clear conversion trigger | Help identify natural upgrade moments or recommend against freemium |
| No free alternative exists | Question whether freemium is necessary; incumbents may be correct |
| Ad revenue not viable | Focus on conversion economics; freemium can work without ads if conversion is high |
| User wants to compete on price only | Redirect to value-based differentiation; race to bottom is not strategy |

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
product_or_service: "Cloud-based note-taking app for developers"
target_market: "Software developers who need to document code and projects"
competitive_landscape: "Notion (freemium), Obsidian (free local), plain text files, wikis"
conversion_goals: "10% free to paid"
```

**Output Summary:**

> Your competition is not Notion - it is plain text files and internal wikis. Developers already have free options that work. Your free tier must be better than their current workflow, not just cheaper than Notion.
>
> **Free Tier Design:**
> - Core value: Unlimited personal notes, code syntax highlighting, basic search
> - Limitation: No team collaboration, limited integrations, no API access
> - Monetization: Pure funnel (no ads - developers hate ads)
>
> **Conversion Trigger:** When developers want to share knowledge with their team. Solo use is free; collaboration is paid.
>
> **Economics:** At 10% conversion with $10/month paid tier, each free user needs to cost less than $1/month to serve. Cloud storage for notes should be well under this threshold.
>
> **Recommendation:** Freemium is viable. The free tier competes with local files by adding sync and search. The paid tier adds team value that solo tools cannot provide. Key risk: Obsidian is free and local-first. Your sync and team features must justify the cloud dependency.

---

## Integration

This skill originates from the **Daniel Ek** expert methodology. When used:
- Apply Ek's philosophy: free tier as aggression, not charity
- Emphasize competing with the real alternative (piracy, workarounds, shadow IT)
- Focus on natural conversion triggers, not artificial restrictions
- Remember: "What is the most aggressive strategy? Lower the price to zero."

---

## Success Criteria

Freemium Model Design is complete when:
- [ ] Free alternative analyzed (what users do today)
- [ ] Free tier designed with genuine value (not crippled product)
- [ ] Clear conversion trigger identified (natural upgrade moment)
- [ ] Economic model validated (unit economics work)
- [ ] Success metrics defined (what to track)
- [ ] Recommendation delivered (freemium yes/no/how)