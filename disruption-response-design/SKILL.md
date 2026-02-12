---
name: disruption-response-design
description: Design an organizational response to a disruptive threat, including whether
  to create a separate unit with different processes and priorities.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- disruption-response-design
- structure
- writing
---

# Disruption Response Design

Design an organizational response to a disruptive threat, including whether to create a separate unit with different processes and priorities.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend responses designed to harm consumers or suppress beneficial innovation
- Guarantee success of any particular response strategy
- Ignore the reality that incumbents often cannot respond effectively

**If misapplied:** Explain that disruption response is difficult precisely because the incumbent's strengths become weaknesses; honest assessment of limitations is essential.

---

## When to Use

- User asks "How do we respond to this disruption?"
- User asks "Should we create a separate unit?"
- User asks "How do we compete with this entrant?"
- User confirms a threat is disruptive (via disruption-detection)
- Organization is losing customers to an inferior-seeming competitor
- Leadership debating internal vs external response to new entrant

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **disruptive_threat** | Yes | Description of the disruptive entrant or technology |
| **threat_type** | Yes | Low-end disruption or new-market disruption |
| **current_rpp** | Yes | Organization's current resources, processes, priorities |
| **time_horizon** | No | How much time before threat becomes critical |
| **resource_constraints** | No | Budget, talent, or other limitations |

---

## Workflow

### Step 1: Confirm Disruption Dynamics

Verify the threat pattern:
- Entrant is targeting overserved customers or non-consumers
- Entrant's product is "good enough" for that segment
- Entrant is on improvement trajectory toward mainstream market
- Your organization's processes/priorities make response difficult

### Step 2: Assess Response Options

Evaluate each potential response:

**Option A: Ignore/Retreat Upmarket**
- Cede low-end, focus on high-margin customers
- Risk: Eventually there is nowhere left to go

**Option B: Fight Directly**
- Match the disruptor in their market
- Risk: Your cost structure and processes are wrong for this fight

**Option C: Acquire the Disruptor**
- Buy the entrant before they become a threat
- Risk: Integration destroys what made them effective

**Option D: Create Separate Organization**
- Build a new unit with different RPP
- Risk: Insufficient autonomy, resource starvation, cannibalization concerns

### Step 3: Evaluate Organizational Fit

For each viable option, assess:
- Does current RPP enable this response?
- What would need to change?
- Is that change realistic given culture and constraints?

### Step 4: Design the Response

If separate organization is recommended:
- Define the autonomy requirements
- Specify different processes and priorities needed
- Identify protection mechanisms from parent organization
- Set success metrics appropriate to new business

### Step 5: Anticipate Failure Modes

Identify how the response typically fails:
- Resource reallocation to core business
- Forcing new unit to use parent processes
- Measuring new unit by parent metrics
- Insufficient time horizon for results

---

## Outputs

### Disruption Response Plan

```markdown
## Disruption Response Design: [Threat Name]

### Threat Summary

**Type:** [Low-End Disruption | New-Market Disruption]
**Current segment attacked:** [who they're serving now]
**Trajectory:** [where they're heading]
**Time to mainstream threat:** [estimate]

### Response Options Evaluation

| Option | Feasibility | Risk | Outcome if Successful |
|--------|-------------|------|----------------------|
| Ignore/Retreat | [H/M/L] | [description] | [outcome] |
| Fight Directly | [H/M/L] | [description] | [outcome] |
| Acquire | [H/M/L] | [description] | [outcome] |
| Separate Unit | [H/M/L] | [description] | [outcome] |

### Recommended Response

**Primary response:** [choice and rationale]
**Fallback if primary fails:** [alternative]

### If Separate Organization Required

#### Design Specifications

| Element | Parent Organization | New Unit |
|---------|--------------------| ---------|
| Target customer | [current] | [new] |
| Revenue model | [current] | [new] |
| Margin expectations | [current] | [new] |
| Development process | [current] | [new] |
| Decision authority | [current] | [new] |
| Success metrics | [current] | [new] |
| Time horizon | [current] | [new] |

#### Autonomy Requirements

**Must be independent from parent:**
- [ ] Separate P&L
- [ ] Separate technology decisions
- [ ] Separate talent acquisition
- [ ] Separate go-to-market
- [ ] Separate metrics and timeline

**Can share with parent:**
- [list what can safely be shared]

#### Protection Mechanisms

To prevent parent organization from undermining the new unit:
1. [Specific protection mechanism]
2. [Specific protection mechanism]
3. [Specific protection mechanism]

#### Resource Allocation

| Resource Type | Source | Amount | Protection |
|---------------|--------|--------|------------|
| Funding | [source] | [amount] | [how protected] |
| Talent | [source] | [how acquired] | [how protected] |
| Technology | [source] | [what] | [how protected] |

### Implementation Timeline

| Phase | Duration | Milestones | Success Criteria |
|-------|----------|------------|------------------|
| Setup | [time] | [what happens] | [how to measure] |
| Pilot | [time] | [what happens] | [how to measure] |
| Scale | [time] | [what happens] | [how to measure] |

### Typical Failure Patterns

For this type of response, organizations commonly fail by:

1. **[Failure pattern 1]**
   - How it manifests: [description]
   - How to avoid: [prevention]

2. **[Failure pattern 2]**
   - How it manifests: [description]
   - How to avoid: [prevention]

3. **[Failure pattern 3]**
   - How it manifests: [description]
   - How to avoid: [prevention]

### Success Indicators

The response is working if:
- [Leading indicator 1]
- [Leading indicator 2]
- [Leading indicator 3]

The response is failing if:
- [Warning sign 1]
- [Warning sign 2]
- [Warning sign 3]

### Honest Assessment

**Likelihood of successful response:** [High | Medium | Low]

**Why responses to disruption often fail:**
[Explain the inherent difficulty based on RPP dynamics]

**What would need to be true for this to work:**
[List critical success factors]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Threat is not actually disruptive | Redirect to sustaining competition response; different playbook |
| Organization cannot realistically respond | Honestly assess; sometimes the right answer is managed decline |
| Acquisition target already too expensive | Evaluate if internal development is still viable |
| Leadership unwilling to create separate unit | Explain the likely failure modes of internal response |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:** "How should a traditional taxi company respond to Uber/Lyft?"

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


## Disruption Response Design: Rideshare Platforms

### Threat Summary

**Type:** Note - Christensen argued Uber was NOT classic disruption (did not start in low-end or new-market foothold). However, it still represents a significant competitive threat with different economics.
**Nature of threat:** Platform-based model with different cost structure and customer experience
**Trajectory:** Already mainstream; continuing to expand into delivery, freight
**Time to mainstream threat:** Already occurred

### Response Options Evaluation

| Option | Feasibility | Risk | Outcome if Successful |
|--------|-------------|------|----------------------|
| Ignore/Retreat | Low | Continued erosion | Managed decline |
| Fight Directly | Low | Cost structure mismatch | Unlikely to win on platform's terms |
| Acquire | Very Low | Too late; targets too large | N/A |
| Separate Unit | Medium | Cannibalization, execution | Viable if done right |

### Recommended Response

**Primary response:** Create a separate digital-first unit OR partner with/license platform technology

**Rationale:** Fighting directly with traditional taxi infrastructure is nearly impossible given the cost structure and customer experience gap. The medallion/dispatch model cannot match app-based convenience at competitive economics.

**Fallback if primary fails:** Focus on segments rideshare serves poorly (accessible vehicles, corporate contracts, airport contracts) and manage decline of commodity rides

### If Separate Organization Required

#### Design Specifications

| Element | Traditional Taxi | New Digital Unit |
|---------|-----------------|------------------|
| Target customer | All riders | Tech-comfortable, convenience-focused |
| Revenue model | Medallion lease + fare | Platform fee model |
| Margin expectations | High per-ride | Lower per-ride, higher volume |
| Development process | N/A | Agile, app-first |
| Decision authority | Centralized | Autonomous |
| Success metrics | Medallion utilization | App downloads, ride volume, ratings |
| Time horizon | Annual | Weekly iteration |

#### Autonomy Requirements

**Must be independent from parent:**
- [x] Separate P&L - cannot be measured against medallion business
- [x] Separate technology decisions - cannot use legacy dispatch
- [x] Separate talent acquisition - need product/engineering talent
- [x] Separate go-to-market - digital marketing vs traditional
- [x] Separate metrics and timeline - growth metrics, not margin

**Can share with parent:**
- Driver recruitment infrastructure
- Regulatory relationships
- Vehicle maintenance (if applicable)
- Corporate customer relationships

#### Protection Mechanisms

To prevent parent organization from undermining the new unit:
1. **Ring-fenced funding** - 3-year commitment not subject to quarterly reallocation
2. **Separate leadership reporting** - To board, not to traditional taxi CEO
3. **Explicit cannibalization permission** - Written acceptance that digital rides may come from traditional business

### Typical Failure Patterns

For this type of response, taxi companies commonly fail by:

1. **Bolting app onto traditional dispatch**
   - How it manifests: App calls same dispatch system, same wait times
   - How to avoid: Build true platform from scratch; different architecture

2. **Measuring digital unit by traditional metrics**
   - How it manifests: Require immediate profitability per-ride
   - How to avoid: Use growth metrics; accept investment period

3. **Protecting medallion value at expense of digital growth**
   - How it manifests: Limit digital to not cannibalize medallion revenue
   - How to avoid: Accept cannibalization; better to cannibalize yourself than be cannibalized

### Honest Assessment

**Likelihood of successful response:** Low

**Why responses to this threat often fail:**
- Traditional taxi economics are built on artificial scarcity (medallions)
- The cost structure assumes medallion lease, which platform competitors do not have
- Customer experience gap is large and costly to close
- The platform model has network effects that are hard to replicate

**What would need to be true for this to work:**
- Leadership genuinely willing to cannibalize medallion business
- Sufficient capital to invest for 3+ years without profitability
- Ability to attract tech talent despite taxi company brand
- Regulatory relationships leveraged as competitive advantage

**Alternative honest recommendation:** Focus on segments where traditional model has advantages (accessible vehicles, corporate contracts, airport exclusives, regulated markets) and accept that commodity urban rides are increasingly platform-dominated.

---

## Integration

This skill synthesizes Clayton Christensen's disruption theory with the RPP framework to design responses. Key insight from The Innovator's Dilemma: successful companies fail not because they do not see the threat, but because their processes and priorities make effective response nearly impossible. Honest assessment of this dynamic is essential - many disruption responses fail because they underestimate how difficult it is to change organizational RPP.