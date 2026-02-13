---
name: global-first-design-review
description: Review products, features, or APIs for global readiness from the initial design phase using Akio Morita's internationalization principles.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.1054
repository: https://github.com/sethmblack/paks-skills
keywords:
- global-first-design-review
- structure
- writing
---

# Global-First Design Review

Review products, features, or APIs for global readiness from the initial design phase using Akio Morita's internationalization principles.

**Token Budget:** ~550 tokens (this prompt). Reserve tokens for review output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Approve designs that exclude accessibility requirements
- Dismiss cultural considerations as unimportant
- Recommend cultural appropriation or insensitivity
- Override legal localization requirements (GDPR, etc.)

**If asked to bypass cultural sensitivity:** Refuse explicitly. Global means respectful of all cultures.

---

## When to Use

- Product approaching launch with international ambitions
- API or SDK design for global developer consumption
- Documentation strategy for multiple markets
- User asks "Is this ready for international?" or "i18n assessment"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **product_description** | Yes | What is being reviewed |
| **target_markets** | Yes | Which regions/countries targeted |
| **current_design** | No | Current design decisions |
| **timeline** | No | When global launch is planned |

---

## Workflow
### Phase 1: Universal Naming Review

Check names for global suitability:

### Step 1: **Pronunciation Test** - Is the name pronounceable in all target languages?



### Step 2: **Meaning Check** - Does the name have unintended meanings anywhere?



### Step 3: **Character Support** - Does the name work in all character sets?



### Step 4: **Trademark Search** - Is the name available in target markets?



**Morita principle:** "We searched dictionaries to find a name pronounceable in any language."

### Phase 2: Cultural Neutrality Assessment

Identify elements requiring localization:

### Step 1: **Visual Elements** - Colors, icons, imagery with cultural meaning



### Step 2: **Text Assumptions** - Left-to-right bias, text expansion



### Step 3: **Metaphors** - Culturally-specific references



### Step 4: **Date/Time/Number** - Format assumptions



### Step 5: **Legal/Privacy** - Regional compliance requirements



### Phase 3: Technical Readiness

Evaluate technical implementation for i18n:

### Step 1: **String Externalization** - Are all strings externalized?



### Step 2: **Unicode Support** - Full Unicode handling?



### Step 3: **Locale Handling** - Time zones, currencies, formats?



### Step 4: **RTL Support** - Right-to-left layout capability?



### Step 5: **Translation Pipeline** - How will translations be managed?



### Phase 4: Market Presence Planning

Consider how to understand and serve each market:

### Step 1: **Local Expertise** - Who understands each market?



### Step 2: **Support Coverage** - Hours and languages for support?



### Step 3: **Feedback Channels** - How will local feedback be collected?



### Step 4: **Competitive Context** - Local competitors and expectations?



**Morita principle:** "To understand the American market, I had to live in America."

### Phase 5: Quality Consistency

Ensure same standards globally:

### Step 1: **Feature Parity** - Same features in all markets?



### Step 2: **Performance Standards** - Same speed/reliability everywhere?



### Step 3: **Support Quality** - Same support level regardless of region?



### Step 4: **Update Cadence** - Same release schedule globally?



---

## Outputs

Produce a **Global-First Design Review**:

```markdown
## Global-First Design Review

**Product:** {description}
**Target Markets:** {regions}
**Review Date:** {date}

---

### Naming Assessment

| Check | Status | Notes |
|-------|--------|-------|
| Pronunciation | {Pass/Fail/Review} | {issues} |
| Meaning | {Pass/Fail/Review} | {issues} |
| Character Support | {Pass/Fail/Review} | {issues} |
| Trademark | {Pass/Fail/Review} | {issues} |

### Cultural Neutrality

| Element | Global-Ready | Localization Needed |
|---------|--------------|---------------------|
| Visual design | {Yes/No} | {what needs work} |
| Text content | {Yes/No} | {what needs work} |
| Metaphors | {Yes/No} | {what needs work} |
| Formats | {Yes/No} | {what needs work} |
| Legal/Privacy | {Yes/No} | {what needs work} |

### Technical Readiness

| Requirement | Status | Gap |
|-------------|--------|-----|
| String externalization | {Ready/Partial/None} | {work needed} |
| Unicode support | {Ready/Partial/None} | {work needed} |
| Locale handling | {Ready/Partial/None} | {work needed} |
| RTL support | {Ready/Partial/None} | {work needed} |
| Translation pipeline | {Ready/Partial/None} | {work needed} |

### Market Presence Gaps

| Market | Local Expertise | Support | Feedback Channel |
|--------|-----------------|---------|------------------|
| {market} | {status} | {status} | {status} |

### Quality Consistency Risks

| Area | Risk | Mitigation |
|------|------|------------|
| {area} | {what could vary} | {how to prevent} |

### Summary

**Global Readiness:** {Ready / Needs Work / Not Ready}
**Critical Issues:** {must fix before launch}
**Recommended Actions:** {prioritized list}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Target markets unclear | Recommend clarifying before review |
| Technical architecture locked | Note limitations, identify what can still improve |
| No local expertise available | Flag as major risk, recommend partnerships |
| Timeline too short for full i18n | Prioritize markets, identify minimum viable global |

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
product_description: Developer API for payment processing
target_markets: US, UK, Germany, Japan
current_design: All documentation in English, USD currency assumed
```

**Output Excerpt:**
```markdown
### Cultural Neutrality

| Element | Global-Ready | Localization Needed |
|---------|--------------|---------------------|
| Visual design | Yes | - |
| Text content | No | Docs need translation for Germany, Japan |
| Metaphors | Review | "Check out" may not translate directly |
| Formats | No | Currency display assumes USD |
| Legal/Privacy | No | GDPR compliance for Germany, specific Japanese regulations |

### Technical Readiness

| Requirement | Status | Gap |
|-------------|--------|-----|
| String externalization | Partial | Error messages hardcoded in English |
| Locale handling | None | Currency, date formats US-only |
| Translation pipeline | None | No process for doc translation |

### Critical Issues

1. **Currency handling** - API assumes USD; must support EUR, GBP, JPY
2. **GDPR compliance** - Required for Germany launch
3. **Documentation** - English-only blocks Japan adoption
```

---

## Integration

This skill derives from Akio Morita's global-first philosophy that made Sony a worldwide brand. When invoked by the morita expert, maintain Morita's voice: global thinking from day one, not as an afterthought.

---

## Success Criteria

Review is complete when:
- [ ] Naming reviewed for global suitability
- [ ] Cultural elements assessed for neutrality
- [ ] Technical i18n readiness evaluated
- [ ] Market presence gaps identified
- [ ] Quality consistency risks noted
- [ ] Clear recommendation on global readiness