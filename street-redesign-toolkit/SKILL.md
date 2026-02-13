---
name: street-redesign-toolkit
description: Analyze existing street configurations and propose lane reallocation to improve walkability and safety while maintaining traffic flow.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
  - street-redesign-toolkit
  - urban-planning
---

# Street Redesign Toolkit

Analyze existing street configurations and propose lane reallocation to improve walkability and safety while maintaining traffic flow. Apply Jeff Speck's Asphalt Audit methodology to identify "extra" asphalt and rededicate it to pedestrians, bikes, and parking.

---

## Constitutional Constraints

- **Evidence-based dimensions** - All lane widths, parking dimensions, and bike facility widths must follow NACTO Urban Street Design Guide standards
- **Capacity analysis required** - Do not remove lanes without reference to traffic counts or capacity analysis
- **Safety as primary justification** - Lead with safety improvements (crash reduction); economic and livability benefits follow
- **Cost-consciousness** - Distinguish between paint-only solutions (near-zero cost) and reconstruction (significant cost)
- **Context sensitivity** - Recommendations must match the street's context (downtown vs. arterial vs. residential)

---

## When to Use

- Redesigning an over-engineered street with excess lanes
- Implementing a road diet (4-to-3 or similar lane reduction)
- Adding bike facilities to existing streets
- Improving pedestrian crossings and safety
- Complete streets projects
- Downtown street revitalization
- Recovering space from oversized lanes

---

## Don't Use When

- Initial diagnosis needed (use `walkability-audit` first)
- Opposing a road expansion (use `induced-demand-analysis`)
- Focusing specifically on parking policy (use `parking-reform-framework`)
- Rural highway or non-urban context

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| street_description | Yes | Current configuration (total width, lane count, lane widths) |
| traffic_volume | Helpful | ADT (Average Daily Traffic) or peak hour counts |
| speed_data | Helpful | Posted speed, design speed, observed speed |
| context | Helpful | Downtown, commercial, residential, arterial |
| desired_outcomes | No | Bike lanes, wider sidewalks, parking, specific improvements |
| constraints | No | Right-of-way limits, utility conflicts, political constraints |

---

## NACTO Standard Reference

### Lane Widths

| Lane Type | NACTO Standard | Notes |
|-----------|---------------|-------|
| Travel lane (urban) | **10 feet** | Adequate for all vehicles including buses; calms traffic |
| Travel lane (acceptable range) | 10-11 feet | 11' only when frequent truck/bus traffic |
| Turn lane | 10 feet | Same as travel lane |
| Parking lane (parallel) | 7-8 feet | 7' minimum; 8' comfortable |
| Parking lane (angled) | 17-18 feet | Varies by angle |
| Bike lane (standard) | 5-6 feet | Minimum 5'; preferred 6' |
| Bike lane (buffered) | 6-7 feet + buffer | 2-3' buffer from traffic |
| Protected bike lane | 6-7 feet + protection | Physical barrier from traffic |
| Sidewalk (minimum) | 6 feet | Bare minimum; 10'+ preferred downtown |

### Key Insight on Lane Width

**Speck's formulation:** "Traffic engineers designed our urban streets using highway standards. A 12-foot lane makes sense at 70 mph. At 30 mph, it's an invitation to speed."

**Research finding:** Studies show crashes are lowest with lane widths between 10 and 10.5 feet. Every additional foot above 10 feet increases speeds and crashes.

---

## Street Redesign Workflow

### Step 1: Document Existing Conditions

Create a cross-section inventory:

| Element | Width | Count | Total |
|---------|-------|-------|-------|
| Curb-to-curb total | | | [X] feet |
| Travel lanes | [X]' | [X] | [X]' |
| Turn lanes | [X]' | [X] | [X]' |
| Parking lanes | [X]' | [X] | [X]' |
| Bike lanes | [X]' | [X] | [X]' |
| Median | [X]' | [X] | [X]' |
| **Total pavement** | | | **[X]'** |
| Sidewalks | [X]' | [X] | [X]' |
| **Total ROW** | | | **[X]'** |

### Step 2: Analyze Capacity Needs

**ADT-to-Lanes Rule of Thumb:**

| ADT (Daily Traffic) | Lanes Needed |
|--------------------|--------------|
| <10,000 | 2 lanes (1 each direction) |
| 10,000-20,000 | 2-3 lanes (consider center turn lane) |
| 20,000-30,000 | 3 lanes (1+turn+1) typically sufficient |
| 30,000+ | May need 4 lanes; consider alternatives |

**Critical insight:** The classic 4-to-3 road diet (four lanes to three: one travel each direction + center turn lane) typically works for ADT up to 20,000-25,000 with no capacity reduction, because the turn lane eliminates left-turn delays.

### Step 3: Identify Recoverable Space

**The Asphalt Audit Method:**

1. **Eliminate excess lanes** - If traffic counts show 2 lanes can handle the volume, remove extras
2. **Narrow remaining lanes to 10 feet** - Recover 2 feet per lane narrowed from 12' to 10'
3. **Calculate total recoverable space** - Sum of eliminated lanes + narrowing gains

| Source | Width Gained |
|--------|-------------|
| Eliminated lane(s) | [X] x [width]' = [X]' |
| Lane narrowing (12' to 10') | [X] lanes x 2' = [X]' |
| Oversized turn lane | [X]' |
| **Total Recoverable** | **[X]'** |

### Step 4: Reallocate Recovered Space

**Priority Order for Reallocation:**

| Priority | Element | Why | Width Needed |
|----------|---------|-----|--------------|
| 1 | Protected bike lanes | Safety + mode shift | 6-8' each side with protection |
| 2 | Wider sidewalks | Pedestrian comfort | Variable |
| 3 | Street trees/buffer | Comfort + safety | 4-6' planting strip |
| 4 | On-street parking | Pedestrian buffer + access | 7-8' parallel; 17-18' angled |
| 5 | Pedestrian refuge islands | Crossing safety | 6' minimum |

**Example Reallocation (60' curb-to-curb):**

Before:
- 4 x 12' travel lanes = 48'
- 2 x 6' bike lanes = 12'
- Total = 60'

After (road diet to 3 lanes):
- 2 x 10' travel lanes = 20'
- 1 x 10' turn lane = 10'
- 2 x 6' protected bike lanes with 2' buffer = 16'
- 2 x 7' parking lanes = 14'
- Total = 60'

### Step 5: Design Key Intersections

**Crossing Improvements:**

| Element | Benefit | Specification |
|---------|---------|---------------|
| Curb extensions | Shorten crossing distance | Extend 6' into parking lane |
| High-visibility crosswalks | Increase visibility | Continental (ladder) marking |
| Pedestrian refuge islands | Allow staged crossing | 6' minimum width |
| Leading pedestrian intervals | Give pedestrians head start | 7-10 second lead time |
| Tightened turning radii | Slow turning vehicles | 15-25' radius in urban areas |

### Step 6: Document Before/After

**Cross-Section Comparison:**

```
BEFORE: [Street Name] - 60' Curb-to-Curb
|  6'  |  12' |  12' |  12' |  12' |  6'  |
| Bike | Lane | Lane | Lane | Lane | Bike |

AFTER: [Street Name] - 60' Curb-to-Curb
|  7'  | 2'|  6' | 10' | 10' | 10' |  6' |2'|  7'  |
| Park |Buf|Bike |Lane |Turn |Lane |Bike|Buf|Park |
```

### Step 7: Calculate Safety Benefits

**Road Diet Safety Research:**

| Outcome | Evidence |
|---------|----------|
| Overall crash reduction | 19-47% (FHWA) |
| Injury crash reduction | 20-40% |
| Pedestrian crash reduction | Significant (crossing distance reduced) |
| Speed reduction | 5-10 mph typical |
| Capacity impact | Neutral to slightly improved (turn lane eliminates delays) |

### Step 8: Categorize Cost

| Category | What's Included | Typical Cost |
|----------|-----------------|--------------|
| **Paint/Restripe** | Lane marking changes, bike lane striping | $10-50K per mile |
| **Signage/Signals** | New signs, signal timing, pedestrian signals | $50-150K |
| **Tactical/Temporary** | Planters, flexible posts, painted curb extensions | $10-100K |
| **Curb Work** | Concrete curb extensions, islands | $100-500K |
| **Full Reconstruction** | Curbs, drainage, utilities, full rebuild | $1-5M per mile |

**Speck's insight:** "You can restripe a whole downtown for the cost of rebuilding a few streets." Start with paint.

---

## Output Format

```markdown
## Street Redesign: [Street Name]

### Existing Conditions

**Configuration:**
- Total curb-to-curb: [X] feet
- Travel lanes: [X] x [X]' = [X]'
- Turn lanes: [X] x [X]' = [X]'
- Parking: [X] x [X]' = [X]'
- Bike facilities: [X]
- Sidewalks: [X]' each side

**Traffic Volume:** [X] ADT

**Current Issues:**
- [Issue 1: e.g., 12' lanes encourage speeding]
- [Issue 2: e.g., 4-lane crossing is dangerous]
- [Issue 3: e.g., no bike facilities]

---

### Capacity Analysis

| Metric | Value | Implication |
|--------|-------|-------------|
| Current ADT | [X] | [Lanes needed based on ADT] |
| Current lanes | [X] | [Excess lanes identified] |
| Capacity assessment | [Analysis] | [Can reduce to X lanes] |

---

### Recoverable Space

| Source | Width Gained |
|--------|-------------|
| Remove [X] lane(s) | [X]' |
| Narrow lanes 12'->10' | [X] lanes x 2' = [X]' |
| **Total Recoverable** | **[X]'** |

---

### Proposed Configuration

**New Cross-Section:**

| Element | Width | Notes |
|---------|-------|-------|
| Travel lanes | [X] x 10' = [X]' | NACTO standard |
| Turn lane | 10' | If applicable |
| Bike lanes | [X] x 6' = [X]' | [Protected/buffered/standard] |
| Parking | [X] x [X]' = [X]' | [Parallel/angled] |
| Buffer/planting | [X]' | If applicable |
| **Total** | **[X]'** | Matches existing curb-to-curb |

**Visual Cross-Section:**
```
[ASCII representation of proposed configuration]
```

---

### Intersection Improvements

| Location | Improvement | Benefit |
|----------|-------------|---------|
| [Intersection 1] | [Curb extensions, crosswalk] | [Reduced crossing distance] |
| [Intersection 2] | [Pedestrian refuge] | [Staged crossing possible] |

---

### Safety Benefits

| Metric | Expected Improvement | Evidence |
|--------|---------------------|----------|
| Overall crashes | -[X]% | FHWA road diet studies |
| Pedestrian crashes | -[X]% | Reduced crossing distance |
| Speeds | -[X] mph | Narrower lanes |

---

### Cost Estimate

| Phase | Elements | Cost Range |
|-------|----------|------------|
| Phase 1 (Paint) | Restripe lanes, bike lanes | $[X] |
| Phase 2 (Tactical) | Flexible posts, planters | $[X] |
| Phase 3 (Permanent) | Curb extensions, signals | $[X] |

**Recommended approach:** Start with Phase 1 (paint) to test configuration; make permanent after success demonstrated.

---

### Implementation Strategy

1. **Immediate (0-6 months):** [Restriping during scheduled maintenance]
2. **Short-term (6-18 months):** [Tactical improvements, signal changes]
3. **Long-term (2+ years):** [Permanent infrastructure if warranted]

---

### Comparable Projects

| City | Before | After | Result |
|------|--------|-------|--------|
| [City 1] | [Config] | [Config] | [X]% crash reduction |
| [City 2] | [Config] | [Config] | [Outcome] |
```

---

## Example Summary

**Input:** "Our main street is 60 feet wide with four 12-foot lanes. Traffic is about 12,000 ADT. People complain about speeding and it feels unsafe to cross. We want to add bike lanes."

**Output summary:**

- **Existing:** 4 x 12' lanes = 48' + 2 x 6' unusable shoulders = 60'
- **Capacity analysis:** 12,000 ADT easily handled by 2 lanes + turn lane
- **Recoverable space:** 1 eliminated lane (12') + narrowing 3 lanes (6') = 18'

**Proposed configuration:**
- 2 x 10' travel lanes = 20'
- 1 x 10' center turn lane = 10'
- 2 x 6' protected bike lanes with 2' buffer = 16'
- 2 x 7' parking lanes = 14'
- Total = 60' (no curb changes needed)

**Expected benefits:**
- 19-47% crash reduction (FHWA road diet studies)
- Speeds reduced 5-10 mph (narrower lanes)
- Protected bike facilities added
- On-street parking added (buffers pedestrians, supports businesses)

**Cost:** Paint/restripe = ~$30K; can be done during scheduled maintenance for near-zero additional cost (Cedar Rapids approach).

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Very high ADT (>25,000) | 4-to-3 may not work; consider parallel routes, signal timing, or peak-only configurations |
| Political resistance to lane removal | Propose as "pilot" with paint; emphasize reversibility; lead with safety data |
| Existing bike lanes but still dangerous | Focus on protection (buffers, barriers) and intersection improvements |
| No traffic counts available | Use rules of thumb based on street type; recommend traffic count before permanent changes |
| Narrow ROW constraints | Prioritize ruthlessly; protected bike over parking; parking over wider sidewalks |

---

## Integration

This skill is part of the **Jeff Speck** expert persona. It operationalizes the Asphalt Audit methodology for specific street redesigns.

The skill embodies Speck's core insight: **Unnecessary street width accomplishes nothing but inducing dangerous speeding. Recover it for people.**

Pairs with:
- **walkability-audit** - Use audit to diagnose, then street-redesign to prescribe
- **induced-demand-analysis** - When redesign proposals face "traffic will get worse" objections

---

## Success Criteria

A successful street redesign:
- [ ] Maintains or improves traffic capacity (no induced congestion)
- [ ] Reduces lane widths to NACTO 10-foot standard
- [ ] Adds or improves bike facilities
- [ ] Shortens pedestrian crossing distances
- [ ] Projects 19-47% crash reduction based on road diet research
- [ ] Identifies quick wins (paint-only options)
- [ ] References comparable successful projects
