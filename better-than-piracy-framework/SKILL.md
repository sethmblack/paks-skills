---
name: better-than-piracy-framework
description: Analyze entrenched competitors (including free, illegal, or informal alternatives) and design strategies to out-compete through superior experience rather than enforcement or legislation.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.451
keywords:
- better-than-piracy-framework
- writing
---

# Better Than Piracy Framework

Analyze entrenched competitors (including free, illegal, or informal alternatives) and design strategies to out-compete through superior experience rather than enforcement or legislation.

**Token Budget:** ~700 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Design strategies that rely on legal threats against users
- Recommend DRM or restrictions that punish paying customers
- Create artificial scarcity to force payment when value isn't delivered
- Suggest surveillance or punishment-based approaches to prevent workarounds

**If asked to design enforcement-based competition:** Refuse explicitly. You cannot legislate away piracy. The only solution is to build something better.

---

## When to Use

- User says "How do we compete with free?"
- User says "Users are using workarounds/piracy/shadow IT"
- User says "Open source is eating our market"
- User says "They're giving it away for free"
- User says "Can't beat the incumbent" (when incumbent is free/cheap)
- User faces competition from illegal alternatives
- User's product competes with manual processes or informal solutions

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| **product_or_service** | Yes | What you are offering | Must describe specific offering |
| **entrenched_alternative** | Yes | The free/cheap/informal competitor | |
| **why_users_choose_alternative** | Yes | Honest assessment of why users tolerate inferior solution | |
| **current_approach** | No | How you are currently competing | |

---

## The Philosophy

**The Core Insight:** You cannot legislate away piracy. Laws can help, but they do not solve the problem. The only solution is to create a service that is better than piracy and at the same time compensates the industry.

**Why People "Pirate":**
- They do not want to be pirates
- They just want a great experience
- The legal option is worse (slower, harder, more expensive, less convenient)
- Piracy was "kind of hard: it took a few minutes... cumbersome... viruses"

**The Spotify Proof:**
- Target: 200 milliseconds from pressing play to hearing music
- That is better than having the song on your hard drive
- Speed, convenience, and instant access beat free-but-cumbersome every time

---

## Workflow
### Step 1: Honest Alternative Analysis

Do not demonize the alternative. Understand why users choose it:

| Question | Honest Answer |
|----------|---------------|
| What is the alternative? | |
| Why do users choose it despite downsides? | |
| What downsides do they accept? | |
| What would they pay to avoid those downsides? | |
| How much effort does the alternative require? | |

**Examples of "Piracy" in Different Markets:**
- Software: Cracked versions, open source alternatives, manual processes
- Content: Illegal streaming, torrents, password sharing
- Enterprise: Shadow IT, spreadsheets, personal tools
- Services: DIY, informal providers, word-of-mouth networks

### Step 2: Identify the Experience Gap

Map where your paid offering can be genuinely superior:

| Dimension | Alternative | Your Offering | Gap Size |
|-----------|-------------|---------------|----------|
| **Speed** | How fast? | How fast? | |
| **Convenience** | How easy? | How easy? | |
| **Reliability** | How consistent? | How consistent? | |
| **Safety** | What risks? | What risks? | |
| **Completeness** | What's missing? | What's included? | |
| **Legality/Peace of mind** | What concerns? | What certainty? | |

**The 200ms Principle:** Find your equivalent of "200 milliseconds." What is the single metric that, if you nail it, makes your offering undeniably better than free?

### Step 3: Design for Superior Experience

For each gap identified, specify how you will win:

| Gap | Specific Solution | Measurable Target |
|-----|------------------|-------------------|
| Speed | | |
| Convenience | | |
| Reliability | | |
| [etc.] | | |

**Design Principles:**
- Solve problems users accept but would prefer not to have
- Make the paid path easier than the free path
- Never punish paying customers with restrictions pirates don't face
- Instant gratification beats eventual access

### Step 4: Validate "Better Than Free"

Test your design against reality:

| Test | Pass/Fail | Evidence |
|------|-----------|----------|
| Is your solution faster than the free alternative? | | |
| Is your solution more convenient? | | |
| Would a rational user prefer your solution even if free existed? | | |
| Does your solution avoid the downsides users hate? | | |
| Are you competing on experience, not just legitimacy? | | |

**Critical Question:** If the alternative were suddenly legal and free forever, would users still prefer your product? If no, you are not better - you are just legal.

---

## Outputs

Return a structured Better-Than-Piracy Strategy:

```markdown
## Better-Than-Piracy Strategy: [Product Name]

### Alternative Analysis

**The "piracy" in this market:** [What users do instead]

**Why users choose it:**
- [Reason 1]
- [Reason 2]
- [Reason 3]

**Downsides they tolerate:**
- [Downside 1]
- [Downside 2]
- [Downside 3]

### Experience Gap Analysis

| Dimension | Alternative | Your Offering | Gap |
|-----------|-------------|---------------|-----|
| Speed | [X] | [Y] | [+/-] |
| Convenience | [X] | [Y] | [+/-] |
| Reliability | [X] | [Y] | [+/-] |
| Safety | [X] | [Y] | [+/-] |
| Completeness | [X] | [Y] | [+/-] |

### Your "200 Milliseconds"

**The single metric that proves you're better:** [What and why]

**Target:** [Specific measurable goal]

### Strategy Design

**How you will be faster:**
[Specific approach]

**How you will be more convenient:**
[Specific approach]

**How you will be more reliable:**
[Specific approach]

### Validation Assessment

| Test | Status | Notes |
|------|--------|-------|
| Faster than free? | Pass/Fail | |
| More convenient than free? | Pass/Fail | |
| Would users prefer even if free existed? | Pass/Fail | |

### Recommendations

**Do this:**
- [Action 1]
- [Action 2]

**Stop doing this:**
- [Anti-pattern 1]
- [Anti-pattern 2]

### Verdict

[Summary: Can you beat "piracy" on experience? What must change?]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Alternative is actually better | Acknowledge honestly; recommend specific investments to close gap |
| Only advantage is legality | Warn this is not sustainable; users eventually choose convenience |
| Users are not price-sensitive | Consider whether this is a piracy problem or a discovery problem |
| Alternative has no downsides | Question whether you should be in this market |
| User wants to use legal threats | Redirect to experience competition; legal threats alienate potential customers |

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
product_or_service: "Enterprise learning management system (LMS)"
entrenched_alternative: "Teams use shared Google Docs, YouTube playlists, and informal Slack threads"
why_users_choose_alternative: "Free, already have accounts, no procurement, works good enough"
current_approach: "Emphasizing compliance features and formal certifications"
```

**Output Summary:**

> Your competition is not other LMS vendors. It is Google Docs and Slack. Users are "pirating" enterprise learning by stitching together free tools because your formal system is slower and harder than their informal workarounds.
>
> **Why they choose the alternative:**
> - Zero procurement friction (already have Google accounts)
> - Instant sharing (paste a link vs. LMS upload workflow)
> - Good enough for most training needs
>
> **Your "200 milliseconds":** Time from "I want to share this training" to "my team can access it." If your LMS takes 30 minutes of admin work vs. their 30-second Google Doc link, you lose.
>
> **Strategy:** Stop selling compliance. Sell speed. Make creating and sharing a course faster than creating a Google Doc. Add compliance as a bonus, not the value proposition.
>
> **Verdict:** You can beat the shadow IT alternative, but only if you compete on convenience. Your current approach (emphasizing compliance) is the equivalent of music labels emphasizing that piracy is illegal. Users know. They do not care. Be better.

---

## Integration

This skill originates from the **Daniel Ek** expert methodology. When used:
- Apply Ek's principle: "You cannot legislate away piracy"
- Remember the 200ms standard - find your equivalent metric
- People do not want to pirate; they want a great experience
- Never punish paying customers with restrictions pirates avoid

---

## Success Criteria

Better-Than-Piracy Strategy is complete when:
- [ ] Alternative honestly analyzed (no demonization)
- [ ] User motivations understood (why they tolerate downsides)
- [ ] Experience gaps identified (speed, convenience, reliability)
- [ ] "200 milliseconds" equivalent defined (your proof point)
- [ ] Strategy focuses on experience, not enforcement
- [ ] Validation tests applied (would users still prefer you if free existed?)
- [ ] Clear recommendations delivered