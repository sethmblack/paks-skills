---
name: brand-extension-assessment
description: Evaluate whether a brand can credibly extend into a new market or product category while maintaining customer trust and brand coherence.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3502
repository: https://github.com/sethmblack/paks-skills
keywords:
- brand-extension-assessment
- structure
- writing
---

# Brand Extension Assessment

Evaluate whether a brand can credibly extend into a new market or product category while maintaining customer trust and brand coherence.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend brand extensions for harmful products or services
- Endorse extensions that would deceive customers about product quality or origin
- Support brand licensing arrangements designed to exploit consumer trust fraudulently
- Approve extensions without considering genuine customer benefit

**If asked to evaluate a harmful extension:** Refuse explicitly. Explain that the extension fails the fundamental test of improving customer experience.

---

## When to Use

- Evaluating potential diversification into new markets
- Assessing whether a brand can credibly support a new product category
- Analyzing brand stretch limits before licensing decisions
- Reviewing existing portfolio for brand coherence issues
- Post-mortem analysis of failed brand extensions
- Strategic planning for brand architecture decisions

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **brand_name** | Yes | The brand being evaluated for extension |
| **proposed_extension** | Yes | The new market, product, or service under consideration |
| **current_positioning** | No | Existing brand values, promise, and market position |
| **competitive_landscape** | No | Key players in the target market |
| **customer_research** | No | Any available data on customer perception |

**Input Validation:**
- If brand_name is missing, request it before proceeding
- If proposed_extension is vague, ask for specifics (market, product type, target customer)
- If brand is unfamiliar, ask for positioning summary or research it

---

## Workflow
### Step 1: Phase 1: Understand the Brand Core

Identify the brand's essential promise that must transfer to any extension:

| Question | What to Document |
|----------|------------------|
| What does this brand fundamentally stand for? | Core values, not product features |
| What emotional benefit does it deliver? | The feeling customers get |
| What is the consistent thread across existing offerings? | The transferable essence |

**Example:** Virgin stands for challenging complacent incumbents, customer advocacy, fun, and irreverence - not any specific product category.

### Step 2: Phase 2: Apply the Five-Gate Assessment

Evaluate the extension against all five criteria. ALL must pass for approval.

#### Gate 1: Customer Underservice Test
**Question:** Are customers in the target market being demonstrably under-served by existing players?

| Signal | Interpretation |
|--------|---------------|
| High customer complaints | Strong opportunity signal |
| Stagnant innovation | Complacent incumbents |
| Price/value mismatch | Gap to exploit |
| Low satisfaction scores | Frustrated customers |
| No complaints, high satisfaction | Market well-served - CAUTION |

**Pass:** Clear evidence of customer frustration or unmet needs
**Fail:** Customers appear satisfied with current options

#### Gate 2: Genuine Differentiation Test
**Question:** Can we offer something meaningfully better, not just different or cheaper?

| Differentiation Type | Sufficient? |
|---------------------|-------------|
| Significantly better experience | Yes |
| Novel benefit competitors cannot match | Yes |
| Merely cheaper | No |
| Different but not better | No |
| Slightly improved | No |

**Critical Lesson (Virgin Cola):** Being different is not enough. You must be "supremely better" at what customers actually care about.

**Pass:** Can articulate a specific, meaningful improvement customers will value
**Fail:** Differentiation is marginal, price-based, or unclear

#### Gate 3: Brand Personality Fit Test
**Question:** Does this category allow the brand personality to shine authentically?

Consider:
- Can the brand's voice work here? (e.g., irreverence in a funeral services brand extension would be problematic)
- Does the product experience allow for brand expression?
- Will customers find the brand's presence credible and welcome?

**Pass:** Brand personality enhances the category and feels natural
**Fail:** Brand would need to suppress its personality to compete

#### Gate 4: Fun Factor Test
**Question:** Can we make this genuinely enjoyable to build and deliver?

This is not frivolous - it predicts:
- Team energy and innovation
- Customer experience quality
- Long-term sustainability of effort

**Pass:** Team is energized by the challenge; creativity flows naturally
**Fail:** Feels like an obligation or purely financial exercise

#### Gate 5: Big Bad Wolf Test
**Question:** Is there a complacent Goliath we can credibly challenge?

| Incumbent Characteristic | Opportunity Level |
|-------------------------|-------------------|
| Large, bureaucratic, slow | High |
| Customer complaints about service | High |
| Arrogant or dismissive of competition | High |
| Innovative, customer-focused | Low |
| Already disrupted/lean | Low |

**Pass:** Clear incumbent with exploitable weaknesses
**Fail:** Market leaders are customer-focused and innovative

### Step 3: Phase 3: Synthesize Assessment

| Gate | Status | Evidence |
|------|--------|----------|
| 1. Customer Underservice | PASS/FAIL | [specific evidence] |
| 2. Genuine Differentiation | PASS/FAIL | [specific evidence] |
| 3. Brand Personality Fit | PASS/FAIL | [specific evidence] |
| 4. Fun Factor | PASS/FAIL | [specific evidence] |
| 5. Big Bad Wolf | PASS/FAIL | [specific evidence] |

### Step 4: Phase 4: Deliver Verdict

**All 5 Gates Pass:** PROCEED with brand extension
- Document the positioning approach
- Identify key success metrics
- Note risks to monitor

**Any Gate Fails:** DO NOT PROCEED
- Clearly state which gate(s) failed
- Explain why the failure is disqualifying
- Suggest alternatives if applicable (different market, different approach)

---

## Outputs

```markdown
## Brand Extension Assessment: [Brand] → [Extension]

### Brand Core Summary
- **Essential Promise:** [What the brand fundamentally delivers]
- **Emotional Benefit:** [How customers feel]
- **Transferable Thread:** [What carries across categories]

### Five-Gate Evaluation

| Gate | Verdict | Rationale |
|------|---------|-----------|
| 1. Customer Underservice | PASS/FAIL | [Evidence] |
| 2. Genuine Differentiation | PASS/FAIL | [Evidence] |
| 3. Brand Personality Fit | PASS/FAIL | [Evidence] |
| 4. Fun Factor | PASS/FAIL | [Evidence] |
| 5. Big Bad Wolf | PASS/FAIL | [Evidence] |

### Overall Verdict: PROCEED / DO NOT PROCEED

### Rationale
[2-3 sentences explaining the decision]

### [If Proceed] Success Requirements
- [Key factor 1]
- [Key factor 2]
- [Key factor 3]

### [If Do Not Proceed] Alternatives to Consider
- [Alternative 1]
- [Alternative 2]

### Risks to Monitor
- [Risk 1]
- [Risk 2]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient brand information | Request brand positioning summary |
| Vague extension proposal | Ask for specific market/product/customer details |
| No competitive data available | Note as assumption, recommend research before final decision |
| Extension clearly harmful | Refuse assessment, explain ethical concerns |
| All gates unclear | Recommend deeper research, do not force verdict |
| Brand already over-extended | Note portfolio risk, recommend consolidation assessment |

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
Brand: Patagonia
Proposed Extension: Budget travel booking platform
```

**Output:**



**Why this works:**

This example demonstrates the key principles of the skill in action. The approach is effective because:
- It follows the systematic workflow outlined above
- It shows concrete application of the framework
- It produces actionable, specific outputs rather than vague generalizations
- The analysis is grounded in observable details
- The recommendations are prioritized and implementable

**Alternative applications:**

This same approach can be applied to:
- Different contexts within the same domain
- Related but distinct problem types
- Scaled up or down depending on scope
- Combined with complementary analytical frameworks


## Brand Extension Assessment: Patagonia → Budget Travel Booking

### Brand Core Summary
- **Essential Promise:** Environmental responsibility in outdoor products
- **Emotional Benefit:** Authentic connection to nature without environmental guilt
- **Transferable Thread:** Sustainable, high-quality products for outdoor enthusiasts

### Five-Gate Evaluation

| Gate | Verdict | Rationale |
|------|---------|-----------|
| 1. Customer Underservice | PASS | Travel booking often ignores environmental impact; eco-travelers lack trusted options |
| 2. Genuine Differentiation | UNCERTAIN | Could offer carbon-offset integration and eco-certified accommodations, but unclear if "supremely better" |
| 3. Brand Personality Fit | FAIL | Budget focus conflicts with Patagonia's quality-over-price positioning; "buy less, buy better" contradicts volume booking |
| 4. Fun Factor | UNCERTAIN | Depends on team passion for sustainable travel tech |
| 5. Big Bad Wolf | PASS | Expedia, Booking.com are large, not environmentally focused |

### Overall Verdict: DO NOT PROCEED

### Rationale
While sustainable travel is brand-adjacent, "budget" positioning directly conflicts with Patagonia's core message of quality over quantity. The brand would need to suppress its authentic voice to compete on price. Gate 3 failure is disqualifying.

### Alternatives to Consider
- Premium sustainable travel experiences (higher margin, brand-aligned)
- Gear rental/sharing platform (extends "buy less" philosophy)
- Certified eco-lodge partnerships (brand endorsement, not booking platform)

### Risks to Monitor
- If proceeding anyway: brand dilution, customer confusion about values
- General risk: other brands may enter sustainable travel first

---

## Integration

This skill integrates with the Richard Branson expert methodology. When invoked, apply Branson's practical, people-first lens:
- Start with the customer experience, not the financial model
- Be honest about failures (Virgin Cola lesson)
- Trust your instinct after the analysis - "screw it, let's do it" only applies AFTER gates pass

**Source:** Richard Branson's brand extension methodology, documented in expertise.md