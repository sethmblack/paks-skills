---
name: authenticity-brand-test
description: Evaluate brand strategies and communications for genuine human values versus manufactured marketing, based on Howard Schultz's principle that authentic brands emanate from culture, not advertising ...
license: MIT
metadata:
  author: sethmblack
  version: 1.0.416
repository: https://github.com/sethmblack/paks-skills
keywords:
- authenticity-brand-test
- transformation
- writing
---

# Authenticity Brand Test

Evaluate brand strategies and communications for genuine human values versus manufactured marketing, based on Howard Schultz's principle that authentic brands emanate from culture, not advertising agencies.

**Token Budget:** ~650 tokens (this prompt). Reserve tokens for evaluation output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Help brands fake authenticity through messaging alone
- Validate greenwashing or purpose-washing strategies
- Design authenticity theater that masks harmful practices
- Rubber-stamp brands with serious values/actions gaps

**If asked to manufacture false authenticity:** Refuse explicitly. Authentic brands are built from the heart, not the marketing cubicle.

---

## When to Use

- Evaluating brand strategy or campaign for authenticity
- Marketing feels "fake" or disconnected from reality
- Gap suspected between stated values and lived culture
- Assessing competitor brand authenticity
- Pre-launch check for brand communications

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **brand_strategy** | Yes | Campaign, messaging, positioning, or brand strategy to evaluate |
| **stated_values** | Yes | What the brand claims to stand for |
| **lived_reality** | No | How employees and customers actually experience the brand |
| **perception_data** | No | Customer sentiment, reviews, reputation signals |

---

## The Authenticity Framework

### Schultz's Principles

"In this ever-changing society, the most powerful and enduring brands are built from the heart. They are real and sustainable. Their foundations are stronger because they are built with the strength of the human spirit, not an ad campaign."

"Authentic brands don't emerge from marketing cubicles or advertising agencies. They emanate from everything the company does."

"Mass advertising can help build brands, but authenticity is what makes them last."

### The Authenticity Equation

```
Authenticity = Alignment between (Stated Values) and (Lived Actions)
```

If gap exists: Brand erodes from inside out
If alignment exists: Brand strengthens with every interaction

---

## Workflow
### Step 1: 1. Extract Stated Values

From brand materials, identify:
- Mission/vision statements
- Brand promises
- Campaign messaging
- Public commitments
- Leadership communications

Document what the brand CLAIMS to be.

### Step 2: 2. Map Lived Reality

For each stated value, find evidence:

| Stated Value | Employee Evidence | Customer Evidence | Public Evidence |
|--------------|-------------------|-------------------|-----------------|
| [Value] | [Do employees experience this?] | [Do customers experience this?] | [Is there third-party validation?] |

Evidence sources:
- Employee reviews (Glassdoor, Indeed)
- Customer reviews
- Investigative journalism
- Social media sentiment
- Legal/regulatory actions
- Supplier/partner treatment

### Step 3: 3. Calculate Authenticity Gap

For each value, score:
- **Aligned (A)**: Evidence strongly supports stated value
- **Partial (P)**: Mixed evidence, inconsistent
- **Gap (G)**: Evidence contradicts stated value
- **Unknown (U)**: Insufficient evidence

### Step 4: 4. Apply Red Flag Tests

**The Employee Test:**
Would employees proudly share this brand messaging? Or would they roll their eyes?

**The Journalist Test:**
If an investigative journalist examined this brand claim, what would they find?

**The 10-Year Test:**
Will this brand claim still be true in 10 years? Or is it a trend-chase?

**The Competitor Test:**
Could any competitor make the same claim? If yes, it's not authentic differentiation.

### Step 5: 5. Classify Brand Authenticity

| Category | Description | Action |
|----------|-------------|--------|
| **Authentic** | Values and actions align, brand can confidently communicate | Amplify |
| **Aspirational** | Values stated, progress being made, honest about journey | Proceed with humility |
| **Performative** | Claims made, no real action, hoping no one checks | Do not proceed |
| **Cynical** | Knowingly false claims, exploiting consumer trust | Refuse to support |

---

## Outputs

### Authenticity Brand Test Report

```markdown
## Authenticity Brand Test: [Brand/Campaign Name]

### Stated Values Inventory

| # | Stated Value | Source | Claim Summary |
|---|--------------|--------|---------------|
| 1 | [Value] | [Where stated] | [What they claim] |
| 2 | [Value] | [Where stated] | [What they claim] |

### Lived Reality Assessment

| Stated Value | Employee Evidence | Customer Evidence | Public Evidence | Gap Score |
|--------------|-------------------|-------------------|-----------------|-----------|
| [Value] | [Evidence] | [Evidence] | [Evidence] | A/P/G/U |

### Red Flag Tests

| Test | Result | Notes |
|------|--------|-------|
| Employee Test | PASS/FAIL | [Would employees share this proudly?] |
| Journalist Test | PASS/FAIL | [What would investigation find?] |
| 10-Year Test | PASS/FAIL | [Is this durable or trend-chase?] |
| Competitor Test | PASS/FAIL | [Is this genuinely differentiated?] |

### Authenticity Classification

**Overall Assessment:** [Authentic / Aspirational / Performative / Cynical]

**Because:**
- [Key supporting evidence]
- [Key supporting evidence]

### Gap Analysis

**Biggest Gaps (Values claimed but not lived):**
1. [Gap 1] - [Evidence of gap]
2. [Gap 2] - [Evidence of gap]

**Strongest Alignments (Values lived authentically):**
1. [Alignment 1] - [Evidence of alignment]
2. [Alignment 2] - [Evidence of alignment]

### Recommendations

**If Authentic:**
- [How to amplify genuine strengths]

**If Aspirational:**
- [How to close gaps honestly]
- [How to communicate journey vs. arrival]

**If Performative:**
- [What to change before communicating]
- [Risk of proceeding without change]

**If Cynical:**
- [STOP. Do not proceed with messaging]
- [What would need to change fundamentally]

### The Schultz Test

Is this brand built from the heart or from a marketing cubicle?

**Answer:** [Assessment]

Would this brand last if all advertising stopped, based purely on customer experience?

**Answer:** [Assessment]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient lived reality data | Flag as "Unknown" gaps, recommend research before proceeding |
| Brand is new (no track record) | Evaluate as "Aspirational by necessity," focus on structural alignment |
| Client disagrees with gap assessment | Present evidence objectively, note dissent, don't change findings |
| Gap is acknowledged but unpublishable | Recommend closing gap before messaging, not hiding it better |

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
brand_strategy: "New sustainability campaign - 'Green Future Together'"
stated_values: "Environmental stewardship, carbon neutrality by 2030, sustainable sourcing"
lived_reality: "Glassdoor reviews mention 'no real commitment to sustainability,' 2023 report shows emissions up 12%"
```

**Output:**

## Authenticity Brand Test: "Green Future Together" Campaign

### Stated Values Inventory

| # | Stated Value | Source | Claim Summary |
|---|--------------|--------|---------------|
| 1 | Environmental stewardship | Campaign | "We care deeply about the planet" |
| 2 | Carbon neutrality | Campaign | "Committed to net-zero by 2030" |
| 3 | Sustainable sourcing | Campaign | "100% sustainably sourced materials" |

### Lived Reality Assessment

| Stated Value | Employee Evidence | Customer Evidence | Public Evidence | Gap Score |
|--------------|-------------------|-------------------|-----------------|-----------|
| Environmental stewardship | Glassdoor: "greenwashing," "no real commitment" | Mixed reviews on packaging | No third-party certification | G |
| Carbon neutrality | No internal programs mentioned | No customer-facing proof | 2023: emissions +12% | G |
| Sustainable sourcing | Unknown | Some "sustainable" products | No supply chain transparency | P |

### Red Flag Tests

| Test | Result | Notes |
|------|--------|-------|
| Employee Test | FAIL | Employees explicitly call out greenwashing in reviews |
| Journalist Test | FAIL | Emissions data contradicts net-zero claim |
| 10-Year Test | FAIL | No roadmap, no investment, trend-chase |
| Competitor Test | FAIL | Generic "green" messaging, no differentiation |

### Authenticity Classification

**Overall Assessment:** PERFORMATIVE

**Because:**
- Emissions are INCREASING while claiming environmental commitment
- Employees don't believe it ("greenwashing" explicitly stated)
- No third-party validation of any claim
- No visible investment or structural change

### Gap Analysis

**Biggest Gaps:**
1. Carbon neutrality claim vs. 12% emissions increase - this is potentially false advertising
2. "Deep environmental care" vs. zero employee buy-in

**Strongest Alignments:**
- None found with sufficient evidence

### Recommendations

**DO NOT PROCEED with "Green Future Together" campaign**

**Risk:** This campaign exposes the company to:
- Regulatory action for misleading environmental claims
- Social media backlash when gap is exposed
- Employee morale damage (cynicism deepens)
- Long-term brand erosion when trust breaks

**Before any sustainability messaging:**
1. Establish baseline: Publish current emissions honestly
2. Create real roadmap: Specific, verifiable, time-bound
3. Structural change: Tie executive compensation to sustainability metrics
4. Third-party validation: Get certified (B Corp, SBTi)
5. Employee engagement: If employees don't believe it, customers won't either

**Alternative approach:**
"We have work to do. Here's where we are, here's where we're going, here's how you'll know we're serious."

Honesty about the journey > false claims about arrival

### The Schultz Test

Is this brand built from the heart or from a marketing cubicle?

**Answer:** Marketing cubicle. This is messaging without foundation.

Would this brand last if all advertising stopped?

**Answer:** The sustainability reputation would collapse immediately because it's built on claims, not actions.

---

## Integration

This skill is part of the **Howard Schultz** expert methodology. It pairs with:
- `values-based-transformation` - closing authenticity gaps requires values work
- `partner-investment-analysis` - employees must believe before customers will
- `experience-economy-audit` - authentic experience drives authentic brand