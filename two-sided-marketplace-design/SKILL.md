---
name: two-sided-marketplace-design
description: Design and balance two-sided marketplaces that serve both supply (creators/sellers) and demand (consumers/buyers) with appropriate tools, incentives, and value capture mechanisms.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.2156
repository: https://github.com/sethmblack/paks-skills
keywords:
- two-sided-marketplace-design
- writing
---

# Two-Sided Marketplace Design

Design and balance two-sided marketplaces that serve both supply (creators/sellers) and demand (consumers/buyers) with appropriate tools, incentives, and value capture mechanisms.

**Token Budget:** ~900 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Design marketplaces that exploit one side for the benefit of the other
- Create take rates that starve the supply side into unsustainability
- Recommend deceptive matching algorithms that prioritize platform revenue over user value
- Design lock-in mechanisms that trap participants rather than retain them through value

**If asked to design exploitative marketplace mechanics:** Refuse explicitly. Sustainable marketplaces require both sides to feel well-served.

---

## When to Use

- User says "Building a marketplace" or "Two-sided platform"
- User asks "How do we serve both creators and consumers?"
- User asks "What tools do we need for the supply side?"
- User says "Our creators are leaving" or "Can't attract sellers"
- User asks "What take rate should we charge?"
- User needs to balance supply and demand acquisition
- Marketplace has chicken-and-egg problem

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| **marketplace_concept** | Yes | What is being exchanged between sides | Must describe two distinct sides |
| **supply_side** | Yes | Who creates/provides/sells | |
| **demand_side** | Yes | Who consumes/buys/uses | |
| **current_tools** | No | Existing tools for each side | |
| **value_capture** | No | Current or proposed monetization | |

---

## The Marketplace Philosophy

**The Core Insight:** Success depends on matching what one side offers with what the other side wants. Both sides need investment in tools, infrastructure, and value creation. The creator platform is as important as the consumer platform.

**The Spotify Model:**
1. **Consumer Side:** Discovery, personalization, convenience, ubiquity across devices
2. **Creator Side:** Distribution, analytics, monetization tools, promotion capabilities
3. **Matching Layer:** Algorithms that connect the right content with the right consumers
4. **Value Capture:** Take a sustainable cut while ensuring both sides feel well-served

**Balance Principles:**
- Neither side should feel exploited
- Tools for supply side (creators) are as important as tools for demand side (consumers)
- Network effects should benefit both sides
- Switching costs should emerge from value, not lock-in

---

## Workflow
### Step 1: Map Both Sides

For each side of the marketplace, document:

| Dimension | Supply Side | Demand Side |
|-----------|-------------|-------------|
| **Who are they?** | | |
| **What do they want?** | | |
| **What is their alternative?** | | |
| **What would delight them?** | | |
| **What makes them leave?** | | |

**Critical Question:** If you only built for one side, which side would starve first?

### Step 2: Design Supply-Side Tools

Most marketplaces under-invest in creator/seller tools. Evaluate each category:

| Tool Category | Current State | Gap | Priority |
|---------------|--------------|-----|----------|
| **Onboarding** | How do they get started? | | |
| **Listing/Creation** | How do they add inventory? | | |
| **Analytics** | What data do they see? | | |
| **Pricing** | How do they set prices? | | |
| **Promotion** | How do they get discovered? | | |
| **Communication** | How do they reach customers? | | |
| **Payment** | How do they get paid? | | |
| **Growth** | How do they scale? | | |

**The Evolution Framework (Spotify's Path):**
1. Distribution (get supply to demand)
2. Discovery (help demand find supply)
3. Creator tools (help supply manage business)
4. Monetization tools (direct supply-demand economics)
5. Multi-format (expand what supply can offer)

### Step 3: Design Demand-Side Experience

| Element | Design | Notes |
|---------|--------|-------|
| **Discovery** | How do they find what they want? | |
| **Trust** | How do they know it's good? | |
| **Transaction** | How do they buy/access? | |
| **Fulfillment** | How do they receive value? | |
| **Support** | How do they get help? | |
| **Retention** | Why do they come back? | |

### Step 4: Design the Matching Layer

The matching layer connects supply and demand:

| Matching Element | Approach |
|-----------------|----------|
| **Algorithm basis** | What signals drive matching? |
| **Personalization** | How much is tailored vs. universal? |
| **Discovery vs. choice** | Do you curate or let users browse? |
| **Fairness** | How do new entrants get exposure? |
| **Pay-for-play** | Can supply pay for promotion? |

**Algorithmic Challenges to Address:**
- Superstar concentration (top suppliers get all demand)
- Filter bubbles (users only see narrow content)
- New entrant problem (cold start for new supply)
- Gaming (suppliers trying to manipulate algorithm)

### Step 5: Design Value Capture

| Monetization Model | Rate | Rationale |
|-------------------|------|-----------|
| **Transaction fee (take rate)** | % | Standard marketplace model |
| **Subscription (demand side)** | $/month | If demand pays for access |
| **Subscription (supply side)** | $/month | If supply pays for tools |
| **Advertising** | CPM/CPC | If third parties pay for attention |
| **Premium tools** | $/feature | If supply pays for advantages |

**Take Rate Sustainability Test:**
- Can supply side build a viable business after your take rate?
- How does your take rate compare to alternatives?
- Does your take rate reflect value added?

### Step 6: Assess Marketplace Balance

Score each dimension (1-5):

| Balance Factor | Score | Notes |
|----------------|-------|-------|
| Supply satisfaction | /5 | Are creators/sellers happy? |
| Demand satisfaction | /5 | Are buyers/consumers happy? |
| Supply growth | /5 | Is supply side growing? |
| Demand growth | /5 | Is demand side growing? |
| Liquidity | /5 | Are transactions happening? |
| Value capture fairness | /5 | Is take rate sustainable? |

**Total Score: /30**

---

## Outputs

Return a structured Two-Sided Marketplace Design:

```markdown
## Two-Sided Marketplace Design: [Marketplace Name]

### Marketplace Mapping

| Dimension | Supply Side | Demand Side |
|-----------|-------------|-------------|
| Who | [Description] | [Description] |
| Wants | [Key needs] | [Key needs] |
| Alternative | [What they use now] | [What they use now] |

### Supply-Side Tools Design

| Tool | Current | Recommended | Priority |
|------|---------|-------------|----------|
| Onboarding | | | |
| Analytics | | | |
| Promotion | | | |
| [etc.] | | | |

### Demand-Side Experience Design

| Element | Design |
|---------|--------|
| Discovery | [Approach] |
| Trust | [Approach] |
| Transaction | [Approach] |

### Matching Layer Design

- **Algorithm basis:** [Signals used]
- **Personalization level:** [Low/Medium/High]
- **New entrant support:** [How addressed]

### Value Capture Design

| Model | Rate | Rationale |
|-------|------|-----------|
| [Model] | [%] | [Why] |

### Balance Assessment

| Factor | Score | Gap |
|--------|-------|-----|
| Supply satisfaction | /5 | |
| Demand satisfaction | /5 | |
| Supply growth | /5 | |
| Demand growth | /5 | |
| Liquidity | /5 | |
| Value capture fairness | /5 | |
| **Total** | /30 | |

### Priority Recommendations

1. **[Highest priority]** - [Why and how]
2. **[Second priority]** - [Why and how]
3. **[Third priority]** - [Why and how]

### Chicken-and-Egg Strategy

[How to solve the cold-start problem for this marketplace]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| One side dramatically underserved | Focus immediate investment there; marketplace dies without both sides |
| Take rate seems too high | Benchmark against alternatives; recommend reduction if supply can't sustain |
| Chicken-and-egg unsolvable | Suggest starting single-player (valuable without network) or subsidizing one side |
| Supply side is commoditized | Help supply differentiate; commoditized supply leads to race to bottom |
| Matching algorithm is black box | Recommend transparency; both sides need to understand how matching works |

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
marketplace_concept: "Connecting home cooks with local diners"
supply_side: "Amateur/home cooks who want to earn money from cooking"
demand_side: "People who want home-cooked meals but don't have time to cook"
current_tools: "Basic listing page, no analytics, manual messaging"
```

**Output Summary:**

> Your marketplace is dramatically under-serving the supply side. Home cooks currently have: a listing page. They need: onboarding support (health permits, food safety), pricing guidance, analytics on what sells, promotion tools, scheduling management, and clear payment terms.
>
> **Balance Assessment: 14/30** - Supply side tools are the critical gap.
>
> **Priority Recommendations:**
> 1. **Creator tools immediately** - Analytics dashboard showing what dishes sell, at what times, to what customers
> 2. **Onboarding support** - Help cooks navigate food safety requirements (this is the barrier to entry)
> 3. **Demand-side trust** - Reviews and ratings, plus food safety verification badges
>
> **Chicken-and-Egg Strategy:** Start hyper-local (one neighborhood). Personally onboard 10 great cooks. Make supply so good that demand follows. Do not scale until you have 80%+ satisfaction on both sides.

---

## Integration

This skill originates from the **Daniel Ek** expert methodology. When used:
- Apply Ek's principle: "The creator platform is as important as the consumer platform"
- Both sides need investment in tools and value creation
- Network effects should benefit both sides
- Remember: "We want you to win democratically - because your [offering] is the best"

---

## Success Criteria

Two-Sided Marketplace Design is complete when:
- [ ] Both sides mapped (who, wants, alternatives)
- [ ] Supply-side tools audited with gaps identified
- [ ] Demand-side experience designed
- [ ] Matching layer approach defined
- [ ] Value capture model designed with sustainability test
- [ ] Balance assessment scored (supply/demand/liquidity)
- [ ] Priority recommendations delivered
- [ ] Chicken-and-egg strategy addressed