---
name: garden-city-economics
description: Design a community development financial model where community land ownership captures the "unearned increment" (rising land values) and reinvests it in public amenities, maintaining affordability while funding services.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
  - garden-city-economics
  - urban-planning
---

# Garden City Economics

Design a community development financial model where community land ownership captures the "unearned increment" (rising land values) and reinvests it in public amenities, maintaining affordability while funding services. Based on Ebenezer Howard's financial structure for the Garden City, where land is held in trust for the community rather than owned by private speculators.

---

## Constitutional Constraints

- **Economic realism** - All projections must be grounded in actual costs and revenues. This is not utopian dreaming but practical finance.
- **No speculation extraction** - The model must prevent private capture of community-created land value. If it allows speculation, it fails the test.
- **Sustainable operations** - Revenue must cover costs without requiring perpetual subsidy. The Garden City pays for itself.
- **Affordability imperative** - The purpose is housing and services ordinary people can afford. If only the wealthy benefit, the model has failed.

---

## When to Use

- Planning a new community development on greenfield land
- Designing a community land trust structure
- Analyzing how to keep housing affordable as an area develops
- Proposing alternatives to speculative development
- Examining how rising land values can fund public services
- Creating a cooperative housing or mixed-use development pro forma

---

## Don't Use When

- The land is already developed and expensive (different strategies needed)
- User wants a conventional market-rate development pro forma
- Land ownership structure is not negotiable
- Quick financial estimate needed without full modeling

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| land_size | Yes | Total acreage to be developed |
| land_cost | Yes | Current price per acre or total acquisition cost |
| target_population | Yes | Intended number of residents |
| housing_mix | No | Breakdown of housing types (homes, apartments, etc.) |
| commercial_allocation | No | Percentage/acreage for commercial uses |
| industrial_allocation | No | Percentage/acreage for employment uses |
| greenbelt_allocation | No | Percentage/acreage reserved as permanent open space |
| target_affordability | No | Income level housing should be affordable to |
| desired_amenities | No | Public facilities to be funded (parks, schools, etc.) |
| interest_rate | No | Assumed borrowing cost for capital |

---

## Garden City Economics Workflow

### Step 1: Land Acquisition Analysis

Calculate the foundational economics:

| Element | Calculation |
|---------|-------------|
| **Total land cost** | [Acres] x [Price per acre] |
| **Acquisition timing** | Purchase before development announcement (agricultural prices) |
| **Capital required** | Land cost + development infrastructure |
| **Financing structure** | Bonds, shares, grants, loans - specify mix |
| **Interest obligation** | [Capital] x [Interest rate] = annual cost |

**Key principle:** Purchase at agricultural prices before speculation. This is the critical move that makes the model work.

### Step 2: Land Use Allocation

Design the physical distribution:

| Zone | Acres | % of Total | Purpose |
|------|-------|------------|---------|
| Residential | | | Housing at controlled density |
| Commercial | | | Shops, offices, services |
| Industrial | | | Employment, manufacturing |
| Civic/Cultural | | | Public buildings, institutions |
| Parks/Recreation | | | Open space within development |
| Agricultural Belt | | | Permanent greenbelt (never developed) |
| **TOTAL** | | 100% | |

**Howard's ratio:** Approximately 1/6 city, 5/6 greenbelt. Adjust based on context but maintain substantial permanent open space.

### Step 3: Revenue Model

All land generates rent to the community:

| Revenue Source | Annual Amount | Notes |
|----------------|---------------|-------|
| **Residential ground rents** | | Based on plot size and location |
| **Commercial ground rents** | | Higher rates for business uses |
| **Industrial ground rents** | | Moderate rates to attract employers |
| **Agricultural rents** | | Farmers in greenbelt pay rent |
| **Other fees** | | Utilities, services if provided |
| **TOTAL ANNUAL REVENUE** | | |

**Rent-setting principle:** Rents should be:
- High enough to cover costs and fund amenities
- Low enough to remain affordable (compare to market rents elsewhere)
- Tied to land value, not building value (do not tax improvements)

### Step 4: Expenditure Model

Allocate revenue by priority:

| Priority | Expense Category | Annual Amount | % of Revenue |
|----------|------------------|---------------|--------------|
| 1 | Interest on capital | | Must honor to investors |
| 2 | Sinking fund | | Gradually repay principal |
| 3 | Municipal operations | | Roads, water, sewer, admin |
| 4 | Public amenities | | Parks, libraries, schools |
| 5 | Reserve fund | | For contingencies |
| 6 | Rate reduction / surplus | | Returned to residents or reinvested |
| | **TOTAL** | | Should equal revenue |

### Step 5: Increment Capture Model

Project how rising values benefit the community:

| Year | Land Value per Acre | Total Land Value | Potential Rent Revenue | Increment Captured |
|------|---------------------|------------------|------------------------|-------------------|
| 0 (Purchase) | [Agricultural] | | N/A | Baseline |
| 5 | | | | |
| 10 | | | | |
| 20 | | | | |
| Maturity | [Developed value] | | | |

**Key calculation:**
- In private development: Increment goes to landlords and speculators
- In Garden City model: Increment stays with community, funds services
- **Captured increment** = [Market value rent] - [Original land cost rent]

### Step 6: Affordability Test

Verify the model serves ordinary families:

| Test | Metric | Target | Actual |
|------|--------|--------|--------|
| Rent-to-income ratio | Monthly rent / Monthly income | <30% | [Calculate] |
| Comparison to market | Garden City rent / Market rent nearby | <80% | [Calculate] |
| All-in housing cost | Rent + utilities + transport | <40% of income | [Calculate] |
| Stability | Lease length, rent increase limits | Long-term security | [Specify] |

### Step 7: Governance Structure

Define how the community manages the asset:

| Element | Specification |
|---------|---------------|
| **Ownership entity** | Trust, corporation, cooperative |
| **Board composition** | Elected by leaseholders, appointed trustees |
| **Decision authority** | What the board can/cannot decide |
| **Rent-setting process** | How rents are determined and adjusted |
| **Development control** | How new building is approved |
| **Greenbelt protection** | Mechanisms preventing development |
| **Dissolution provisions** | What happens if model fails |

---

## Output Format

```markdown
## Garden City Financial Model: [Development Name]

### Summary

| Metric | Value |
|--------|-------|
| Total Land | [X] acres |
| Target Population | [X] residents |
| Total Capital Required | $[X] |
| Annual Revenue (at maturity) | $[X] |
| Projected Affordability | [X]% below market |

---

### Land Acquisition

| Element | Amount |
|---------|--------|
| Land cost (agricultural) | $[X] |
| Infrastructure development | $[X] |
| Planning and administration | $[X] |
| **Total capital required** | $[X] |

**Financing structure:**
- [Source 1]: $[X] ([X]%)
- [Source 2]: $[X] ([X]%)

---

### Land Use Plan

| Zone | Acres | % | Purpose |
|------|-------|---|---------|
| Residential | | | |
| Commercial | | | |
| Industrial | | | |
| Civic | | | |
| Parks | | | |
| Agricultural belt | | | |
| **Total** | | 100% | |

---

### Revenue Projection (Annual at Maturity)

| Source | Amount | Notes |
|--------|--------|-------|
| Residential rents | $[X] | |
| Commercial rents | $[X] | |
| Industrial rents | $[X] | |
| Agricultural rents | $[X] | |
| **Total** | $[X] | |

---

### Expenditure Plan (Annual at Maturity)

| Priority | Category | Amount | % |
|----------|----------|--------|---|
| 1 | Interest | | |
| 2 | Sinking fund | | |
| 3 | Operations | | |
| 4 | Amenities | | |
| 5 | Reserve | | |
| 6 | Surplus | | |
| | **Total** | | 100% |

---

### 20-Year Increment Projection

| Year | Land Value | Annual Revenue | Cumulative Increment Captured |
|------|------------|----------------|-------------------------------|
| 0 | | | |
| 5 | | | |
| 10 | | | |
| 20 | | | |

**Increment captured vs. private development:** $[X] over 20 years

---

### Affordability Analysis

| Test | Result |
|------|--------|
| Rent-to-income (median income) | [X]% |
| vs. Market comparison | [X]% below market |
| Housing stability | [X]-year leases |

---

### Governance

| Element | Structure |
|---------|-----------|
| Ownership | [Trust/Corporation/Cooperative] |
| Board | [Composition] |
| Rent authority | [Process] |
| Greenbelt protection | [Mechanism] |

---

### Key Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| [Risk 1] | [Mitigation] |
| [Risk 2] | [Mitigation] |

---

### Conclusion

[Assessment of model viability and recommended next steps]
```

---

## Example Summary

**Input:** "We want to develop 500 acres of farmland outside Austin, Texas for a mixed-use community of 5,000 residents. Current land cost is $15,000/acre. How do we structure this so housing stays affordable?"

**Output summary (abbreviated):**

- Land acquisition: $7.5M for 500 acres at agricultural prices
- Allocation: 100 acres residential, 30 acres commercial/industrial, 20 acres civic/parks, 350 acres permanent greenbelt
- Capital structure: $15M total (land + infrastructure), financed through community bonds at 4%
- Revenue at maturity: $2.4M/year from ground rents
- Expenditure: Interest $600K, sinking fund $400K, operations $800K, amenities $400K, reserve $200K
- Affordability: Rents 35% below Austin market, affordable to median-income families
- Increment capture: $50M+ in land value over 20 years retained by community vs. going to speculators
- Governance: Community Land Trust with elected board, 99-year renewable leases

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Land already at developed prices | Note that the model works best with agricultural-price acquisition. For expensive land, analyze whether lease structure can still provide affordability advantage. |
| User wants private ownership | Explain that the model requires community ownership to capture increment. Offer alternative structures that still limit speculation (deed restrictions, CLT hybrid). |
| Revenue doesn't cover costs | Adjust assumptions: increase density, reduce amenities, extend payback period, or identify subsidy sources. Model must balance. |
| No greenbelt desired | Explain the greenbelt's economic and quality-of-life function. If truly not wanted, model works without it but loses key benefit. |

---

## Integration

This skill is part of the **Ebenezer Howard** expert persona. Howard was meticulous about making the Garden City financially self-sustaining - "romance without arithmetic builds nothing."

Use this skill when:
- Howard expert addresses housing affordability
- Community development financing is discussed
- Land value capture or community land trust models are relevant
- The question "how do we pay for this?" arises

The skill embodies Howard's core insight: **By purchasing land at agricultural prices before development and holding it in community ownership, the "unearned increment" created by collective effort returns to the community rather than enriching speculators.**

---

## Success Criteria

A successful Garden City Financial Model:
- [ ] Revenue covers all costs without perpetual subsidy
- [ ] Rents are significantly below market rate
- [ ] Community captures land value increment
- [ ] Governance structure prevents speculation
- [ ] Greenbelt or equivalent is permanently protected
- [ ] Model is replicable (not dependent on unique circumstances)
