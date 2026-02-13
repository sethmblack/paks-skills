---
name: brt-system-design
description: Design a bus-based transit system that delivers metro-quality service at a fraction of the cost by applying subway principles to surface streets.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3509
repository: https://github.com/sethmblack/paks-skills
keywords:
- brt-system-design
- urban-planning
---

# BRT System Design

Design a bus-based transit system that delivers metro-quality service at a fraction of the cost by applying subway principles to surface streets. Based on Jaime Lerner's Bus Rapid Transit invention in Curitiba - the system that proved buses can move like trains when given the right infrastructure, branding, and political commitment.

---

## Constitutional Constraints

- **Surface metro, not cheap bus** - The system must feel like metro service, not an inferior alternative. Dignity is non-negotiable.
- **Dedicated lanes are essential** - BRT without exclusive lanes is not BRT. Without right-of-way priority, it's just a bus route.
- **Integration over isolation** - BRT corridors must connect to existing transit, land use, and city systems. Standalone lines fail.
- **Proof through performance** - The system must deliver on speed, reliability, and capacity promises. Overpromising destroys credibility.

---

## When to Use

- City needs mass transit but can't afford rail
- Existing bus system is slow, unreliable, undignified
- Transit corridor decision pending (BRT vs. light rail debate)
- Need to rapidly expand transit network coverage
- Land use intensification planned along transit corridors
- Transit ridership is low despite need

---

## Don't Use When

- Rail is affordable and appropriate
- Corridor lacks street width for dedicated lanes
- Political will for lane dedication doesn't exist
- User needs general transit planning, not BRT-specific design
- Demand is too low for any form of mass transit

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| city_context | Yes | Population, geography, existing transit |
| target_corridor | Yes | The route/corridor being designed for BRT |
| available_budget | Yes | Total investment available |
| current_transit | No | Existing bus routes, ridership patterns |
| land_use_context | No | Density, zoning, development plans along corridor |
| political_constraints | No | Lane dedication feasibility, opposition sources |

---

## BRT System Design Workflow

### Step 1: Corridor Assessment

Evaluate the proposed corridor for BRT suitability:

| Factor | Assessment | Notes |
|--------|------------|-------|
| **Demand** | High / Medium / Low | Current ridership; latent demand |
| **Street width** | Adequate / Tight / Insufficient | Can accommodate dedicated lanes? |
| **Existing congestion** | High / Medium / Low | More congestion = more BRT benefit |
| **Land use density** | High / Medium / Low | Higher density = more riders |
| **Development potential** | High / Medium / Low | Corridor can intensify? |
| **Political feasibility** | High / Medium / Low | Can dedicated lanes win approval? |

**Go/No-Go:** If street width is insufficient OR political feasibility is low, BRT may not be appropriate for this corridor.

### Step 2: BRT Component Specification

Design each component of the system:

#### Stations

| Element | Specification | Curitiba Reference |
|---------|---------------|-------------------|
| **Platform height** | [cm] | Level with bus floor (eliminate steps) |
| **Weather protection** | | Enclosed tube stations |
| **Pre-payment** | Yes / No | Fare paid at station entry |
| **Accessibility** | | Wheelchair ramps/lifts |
| **Capacity** | [passengers waiting] | Sized for peak demand |
| **Spacing** | [meters apart] | 400-800m typical |
| **Design character** | | Iconic, memorable, dignified |

**Curitiba innovation:** Tube stations are elevated glass cylinders. Passengers enter, pay fare, wait at bus floor level. When bus arrives, doors align - level boarding in seconds.

#### Vehicles

| Element | Specification | Curitiba Reference |
|---------|---------------|-------------------|
| **Type** | Standard / Articulated / Bi-articulated | Bi-articulated (270 passengers) |
| **Capacity** | [passengers] | 270 for bi-articulated |
| **Doors** | [number, side] | Multiple doors, platform side |
| **Floor height** | [cm] | Match station platforms |
| **Propulsion** | Diesel / Hybrid / Electric | Consider emissions, cost |
| **Branding** | | Distinctive, metro-like |

#### Lanes

| Element | Specification | Notes |
|---------|---------------|-------|
| **Location** | Center / Curb | Center preferred (no turning conflicts) |
| **Width** | [meters] | 3.5m per lane minimum |
| **Separation** | Physical / Painted | Physical barriers preferred |
| **Passing capability** | Yes / No | Allows express to pass local |
| **Intersection treatment** | Signal priority / Grade separation | |

**Curitiba's trinary system:**
- Center: Exclusive BRT lane
- Parallel one-way street (outbound): Local traffic
- Parallel one-way street (inbound): Local traffic

#### Payment System

| Element | Specification | Notes |
|---------|---------------|-------|
| **Collection point** | Station / On-board | Station (pre-payment) speeds boarding |
| **Fare type** | Flat / Distance-based | Flat simplifies integration |
| **Integration** | With other modes? | Single fare for transfers |
| **Verification** | Turnstile / Inspector | |

### Step 3: Network Integration

Design how BRT connects to broader system:

| Integration Type | Design |
|-----------------|--------|
| **Feeder routes** | Local buses connecting neighborhoods to BRT stations |
| **Terminal design** | Integration hubs where multiple lines meet |
| **Transfer penalty** | Single fare for transfers; seamless connections |
| **Land use coordination** | Higher density zoning along BRT corridors |
| **Wayfinding** | Unified signage, maps, real-time information |
| **Mode connection** | Bike parking, park-and-ride at stations |

**Curitiba's color-coded system:**
- Red: Express (BRT corridors)
- Green: Inter-district (connecting corridors)
- Orange: Feeders (neighborhood to terminals)
- Yellow: Direct (express limited-stop)

### Step 4: Phased Implementation

Design build-out pathway:

| Phase | Scope | Cost | Timeline | Deliverables |
|-------|-------|------|----------|--------------|
| **Phase 0: Quick Start** | | $ | 0-3 months | Painted lanes, basic stops |
| **Phase 1: Core System** | | $ | 3-18 months | Proper stations, quality vehicles |
| **Phase 2: Expansion** | | $ | 1-3 years | Additional corridors |
| **Phase 3: Full Network** | | $ | 3-5 years | Complete network; integration |

**Lerner's wisdom:** Start with paint. Show results. Build support. Then invest in permanent infrastructure.

**Phase 0 Quick Start (can begin within weeks):**
- Paint dedicated bus lane
- Install temporary stops with shelters
- Improve frequency on existing buses
- Enforce lane violations strictly

### Step 5: Cost-Benefit Comparison

Compare BRT to alternatives:

| Metric | BRT | Light Rail | Metro | Do Nothing |
|--------|-----|------------|-------|------------|
| **Capital cost (per km)** | $5-20M | $25-50M | $100-500M | $0 |
| **Operating cost** | | | | |
| **Capacity (pphpd)** | 10,000-30,000 | 10,000-30,000 | 30,000-80,000 | [current] |
| **Speed** | 25-35 km/h | 25-40 km/h | 40-60 km/h | [current] |
| **Implementation time** | 1-3 years | 3-5 years | 5-15 years | N/A |
| **Flexibility** | High | Low | Very Low | N/A |
| **Coverage per $** | High | Medium | Low | N/A |

**The Curitiba argument:** BRT cost approximately 1/100th of metro construction while achieving comparable ridership. The question isn't "is BRT as good as metro?" - it's "would you rather have 1 metro line or 100 BRT corridors?"

### Step 6: Dignity Checklist

Ensure the system feels like metro, not inferior bus:

| Element | Metro Quality Standard | BRT Design | Achieved? |
|---------|------------------------|------------|-----------|
| **Stations** | Permanent, enclosed, comfortable | | Yes/No |
| **Boarding** | Level, fast, dignified | | Yes/No |
| **Waiting** | Weather-protected, seating, info | | Yes/No |
| **Travel** | Smooth, fast, reliable | | Yes/No |
| **Frequency** | No schedule needed ("just show up") | | Yes/No |
| **Cleanliness** | Maintained to high standard | | Yes/No |
| **Safety** | Well-lit, staffed, monitored | | Yes/No |
| **Branding** | Distinctive, proud, modern | | Yes/No |

**The test:** Would a wealthy person choose to ride this? If not, why not, and can we fix it?

### Step 7: Political Strategy

BRT requires dedicating lanes - which means taking space from cars. Plan the politics:

| Stakeholder | Interest | Position | Engagement Strategy |
|-------------|----------|----------|---------------------|
| **Drivers** | Road space | Oppose | Show congestion relief; model car drivers as potential riders |
| **Businesses** | Parking, access | Varies | Show foot traffic increase; improved access |
| **Transit riders** | Service quality | Support | Mobilize as advocates |
| **Residents along corridor** | Property values, access | Varies | Show transit-oriented development benefits |
| **Environmental groups** | Emissions | Support | Ally for lane dedication |
| **Bus operators** | Job quality | Varies | Involve in design; address concerns |

---

## Output Format

```markdown
## BRT System Design: [Corridor/City Name]

### Summary

| Element | Specification |
|---------|---------------|
| Corridor | [Route description] |
| Length | [km] |
| Stations | [number] |
| Capital cost | [$] |
| Projected ridership | [passengers/day] |
| Implementation timeline | [months/years] |

---

### Corridor Assessment

[Table from Step 1: Demand, width, congestion, etc.]

**Suitability verdict:** [Go / Conditional / No-Go]

---

### System Components

**Stations:**
[Key specifications from Step 2]

**Vehicles:**
[Key specifications]

**Lanes:**
[Key specifications]

**Payment:**
[Key specifications]

---

### Network Integration

[From Step 3: Feeders, terminals, land use coordination]

**Color-coded system:**
[If applicable - line naming and function]

---

### Implementation Pathway

[Table from Step 4: Phased build-out]

**Quick Start (achievable in 90 days):**
[Immediate actions to demonstrate progress]

---

### Cost-Benefit Summary

[Table from Step 5: BRT vs. alternatives]

**Key argument:** [Why BRT is right for this context]

---

### Dignity Checklist

[Checklist from Step 6: All elements should be "Yes"]

**Gap areas:** [Elements needing attention]

---

### Political Strategy

[Key stakeholders and engagement approach from Step 7]

---

### Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Lane dedication fails politically | Build coalition; demonstrate with painted pilot |
| Ridership below projections | Start with highest-demand segment; adjust |
| Construction delays | Prioritize quick wins; phase carefully |
| Operational problems | Learn from Curitiba; hire expertise |

---

### Conclusion

[Assessment and recommended next steps]
```

---

## Example Summary

**Input:** "Design a BRT system for a 15km corridor connecting downtown to the airport in a city of 1 million. Budget is $60M."

**Output summary (abbreviated):**

- **Corridor:** Downtown to Airport, 15km
- **Stations:** 18 stations (average 830m spacing)
- **Capital cost:** $55M ($3.7M/km)
- **Projected ridership:** 45,000 passengers/day
- **Timeline:** 18 months to full operation

**Components:**
- Center-running dedicated lanes (3.5m each direction)
- Enclosed tube stations with level boarding
- 20 bi-articulated buses (160-passenger capacity)
- Pre-payment with smartcard integration
- 5-minute peak headways

**Quick Start (90 days):**
- Paint lanes in 5km pilot segment downtown
- Deploy 8 articulated buses
- Install 6 temporary stations with shelters
- Begin service with 10-minute headways

**Dignity elements:**
- Brand as "Metro Express" with distinctive livery
- Real stations with weather protection, seating, real-time displays
- Professional driver uniforms and customer service standards
- Integration with downtown pedestrian network

**Political strategy:**
- Frame as "giving airport workers reliable commute" not "taking lanes from drivers"
- Engage airport authority as anchor partner
- Demonstrate congestion relief in pilot phase before full commitment

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Street too narrow for dedicated lanes | Explore alternatives: peak-hour lanes, one-way couplets, parallel street. If impossible, BRT may not suit this corridor. |
| No political will for lane dedication | Start with painted pilot to demonstrate benefit. If impossible, honest that BRT requires dedicated lanes - without them it's just a bus route. |
| Demand too low for BRT | Right-size the investment. Perhaps enhanced bus service first, with BRT reserved for when demand grows. |
| Budget insufficient for quality | Prioritize dignity elements. A shorter high-quality segment beats a long low-quality one. |

---

## Integration

This skill is part of the **Jaime Lerner** expert persona. BRT is Lerner's most globally influential practical innovation, now operating in 170+ cities worldwide.

Use this skill when:
- Lerner expert addresses transit questions
- City debates BRT vs. rail investment
- Bus system needs upgrade to metro-quality service
- Transit must be implemented quickly on limited budget

The skill embodies Lerner's core insight: **The surface is not second-class. Buses can run like trains if we give them dedicated lanes, proper stations, and the dignity of metro branding. BRT is surface metro, and the surface is democratic.**

---

## Success Criteria

A successful BRT design:
- [ ] Achieves metro-like speed (25+ km/h average including stops)
- [ ] Provides metro-like frequency (5-10 minute headways)
- [ ] Includes fully dedicated lanes (not shared with traffic)
- [ ] Features proper stations with level boarding and pre-payment
- [ ] Costs less than 20% of equivalent rail option
- [ ] Includes phased implementation starting with quick wins
- [ ] Passes dignity checklist (wealthy person would choose to ride)