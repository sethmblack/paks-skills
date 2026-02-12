---
name: creator-tools-audit
description: Audit the tools and infrastructure provided to the supply side of a marketplace and identify gaps that weaken creator retention and marketplace health.
version: 1.0.0
author: sethmblack
tags: [creator-tools-audit, writing]
---

# Creator Tools Audit

Audit the tools and infrastructure provided to the supply side of a marketplace and identify gaps that weaken creator retention and marketplace health.

**Token Budget:** ~600 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend tools designed to exploit or deceive creators
- Suggest take rates or policies that make creator businesses unsustainable
- Design opaque systems that hide important information from creators
- Create lock-in through data hostage rather than value delivery

**If asked to design creator-exploitative systems:** Refuse explicitly. Marketplaces die when they starve their supply side.

---

## When to Use

- User says "Are we serving creators well?"
- User says "Creator retention problem" or "Creators are leaving"
- User asks "What tools do we need for the supply side?"
- User says "We focus mostly on consumers"
- User is building a marketplace and only has consumer-facing features
- Supply side of marketplace is weaker than demand side

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| **marketplace_description** | Yes | What the marketplace does | Must have identifiable supply side |
| **current_creator_tools** | Yes | What tools creators have today | |
| **creator_feedback** | No | Known complaints or requests | |
| **competitor_tools** | No | What competitors offer creators | |

---

## The Philosophy

**The Core Insight:** The creator platform is as important as the consumer platform. Most marketplaces under-invest in the supply side, then wonder why creators leave or underperform.

**The Creator Platform Evolution (Spotify's Path):**
1. **Distribution** - Get creator content to consumers
2. **Discovery** - Help consumers find creator content
3. **Creator Tools** - Help creators manage their business
4. **Monetization Tools** - Enable direct creator-consumer economics
5. **Multi-Format** - Let creators offer different types of content

**The Principle:** "We want you to win democratically - because your [offering] is the best."

---

## Workflow
### Step 1: Map Creator Journey

Document what creators do on your platform:

| Stage | What Creator Does | Current Tool Support | Gap |
|-------|-------------------|---------------------|-----|
| **Onboard** | Join the platform | | |
| **Create** | Add content/inventory | | |
| **Optimize** | Improve performance | | |
| **Grow** | Reach more consumers | | |
| **Monetize** | Earn money | | |
| **Analyze** | Understand performance | | |
| **Manage** | Handle operations | | |

### Step 2: Audit Tool Categories

Score each category (1-5):

| Tool Category | Current State | Score | Gap |
|---------------|--------------|-------|-----|
| **Onboarding** | How do creators get started? | /5 | |
| **Listing/Creation** | How do they add content? | /5 | |
| **Analytics** | What data can they see? | /5 | |
| **Pricing** | How do they set/adjust prices? | /5 | |
| **Promotion** | How do they get discovered? | /5 | |
| **Communication** | How do they reach consumers? | /5 | |
| **Payment** | How do they get paid? | /5 | |
| **Growth** | How do they scale their business? | /5 | |
| **Support** | How do they get help? | /5 | |
| **Export/Portability** | Can they take their data if they leave? | /5 | |

**Total: /50**

**Scoring Guide:**
- 5: Best-in-class, creators cite this as reason to stay
- 4: Good, meets needs, no major complaints
- 3: Adequate, gets the job done, some friction
- 2: Weak, frequent complaints, workarounds required
- 1: Missing or non-functional

### Step 3: Identify Critical Gaps

For each category scoring 2 or below:

| Gap | Impact on Creators | Impact on Marketplace | Fix Complexity |
|-----|-------------------|----------------------|----------------|
| [Gap] | [How it hurts them] | [How it hurts you] | High/Med/Low |

**Priority Framework:**
- High Impact + Low Complexity = Do immediately
- High Impact + High Complexity = Plan carefully
- Low Impact + Low Complexity = Quick wins
- Low Impact + High Complexity = Deprioritize

### Step 4: Benchmark Against Evolution Model

Where is your platform in the evolution?

| Stage | Status | Notes |
|-------|--------|-------|
| 1. Distribution | Complete/Partial/Missing | |
| 2. Discovery | Complete/Partial/Missing | |
| 3. Creator Tools | Complete/Partial/Missing | |
| 4. Monetization Tools | Complete/Partial/Missing | |
| 5. Multi-Format | Complete/Partial/Missing | |

**Most Marketplaces:** Strong on 1-2, weak on 3-5. This is the opportunity.

### Step 5: Define Creator Value Proposition

Can you answer this clearly?

**"Creators should use our platform because we give them _____ that they cannot get elsewhere."**

If you cannot answer this, your creator tools are not differentiated.

---

## Outputs

Return a structured Creator Tools Audit:

```markdown
## Creator Tools Audit: [Marketplace Name]

### Creator Journey Map

| Stage | Current Tools | Quality | Gap |
|-------|--------------|---------|-----|
| Onboard | [Tools] | [Score] | [Gap] |
| Create | [Tools] | [Score] | [Gap] |
| Optimize | [Tools] | [Score] | [Gap] |
| Grow | [Tools] | [Score] | [Gap] |
| Monetize | [Tools] | [Score] | [Gap] |
| Analyze | [Tools] | [Score] | [Gap] |
| Manage | [Tools] | [Score] | [Gap] |

### Tool Category Audit

| Category | Score | Notes |
|----------|-------|-------|
| Onboarding | /5 | |
| Listing/Creation | /5 | |
| Analytics | /5 | |
| Pricing | /5 | |
| Promotion | /5 | |
| Communication | /5 | |
| Payment | /5 | |
| Growth | /5 | |
| Support | /5 | |
| Export/Portability | /5 | |
| **Total** | /50 | |

### Critical Gaps (Score 2 or below)

| Gap | Creator Impact | Marketplace Impact | Priority |
|-----|---------------|-------------------|----------|
| [Gap] | [Impact] | [Impact] | High/Med/Low |

### Evolution Stage Assessment

| Stage | Status |
|-------|--------|
| 1. Distribution | |
| 2. Discovery | |
| 3. Creator Tools | |
| 4. Monetization Tools | |
| 5. Multi-Format | |

**Current Stage:** [1-5]

### Creator Value Proposition

**Current:** "[What you offer now]"

**Target:** "[What you should offer]"

### Priority Recommendations

1. **[Immediate - high impact, low complexity]**
   - What: [Specific tool or improvement]
   - Why: [Impact on creator and marketplace]

2. **[Next - high impact, high complexity]**
   - What: [Specific tool or improvement]
   - Why: [Impact on creator and marketplace]

3. **[Quick Win - low impact, low complexity]**
   - What: [Specific tool or improvement]
   - Why: [Why it's worth doing]

### Summary

**Overall Creator Tool Score:** [X]/50

**Verdict:** [Strong/Adequate/Weak/Critical]

**Key Message:** [One sentence summary of the biggest opportunity]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No creator feedback available | Recommend urgent creator research; audit without feedback is guessing |
| All categories score high | Validate against actual creator behavior; high scores + creator churn = something is wrong |
| Too many critical gaps | Prioritize ruthlessly; recommend addressing 2-3 gaps before expanding |
| Creator tools exist but unused | Distinguish tool quality from tool awareness; may be discovery problem |
| Platform has no supply side | This audit doesn't apply; redirect to product strategy |

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
marketplace_description: "Connects local tutors with students for in-person lessons"
current_creator_tools: "Profile page, basic calendar, chat with students"
creator_feedback: "Hard to set availability, no idea how I rank in search, payments are late"
```

**Output Summary:**

> **Overall Creator Tool Score: 18/50** - Weak. You are strong on distribution (tutors can list), partial on discovery (students find tutors), and weak on everything else.
>
> **Critical Gaps:**
> - Analytics: 1/5 - Tutors have no idea how they appear in search, what their conversion rate is, or how they compare to others
> - Payment: 2/5 - Late payments damage trust; tutors may leave for platforms with faster/reliable payment
> - Pricing: 2/5 - No guidance on market rates, no dynamic pricing tools
>
> **Evolution Stage: 2** (Distribution + partial Discovery). You have not yet entered Stage 3 (Creator Tools).
>
> **Creator Value Proposition:** Currently unclear. Tutors use you because students are there, not because you make them successful.
>
> **Priority Recommendations:**
> 1. **Immediate:** Analytics dashboard showing views, inquiries, bookings, and comparison to market
> 2. **Next:** Payment acceleration (same-week payment minimum)
> 3. **Quick Win:** Pricing recommendations based on subject, location, experience

---

## Integration

This skill originates from the **Daniel Ek** expert methodology. When used:
- Apply Ek's principle: "The creator platform is as important as the consumer platform"
- Follow the evolution model: Distribution → Discovery → Creator Tools → Monetization → Multi-Format
- Remember: "We want you to win democratically - because your [offering] is the best"

---

## Success Criteria

Creator Tools Audit is complete when:
- [ ] Creator journey mapped (all stages)
- [ ] All 10 tool categories scored
- [ ] Critical gaps (score 2 or below) identified with impact
- [ ] Evolution stage assessed
- [ ] Creator value proposition evaluated
- [ ] Priority recommendations delivered (immediate, next, quick win)
- [ ] Overall score and verdict provided