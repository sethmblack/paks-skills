---
name: ordo-amoris-audit
description: Examine any decision, system, or organization to identify disordered loves - where lesser things are being loved more than greater, or ends are being confused with means - following Augustine's fra...
license: MIT
metadata:
  version: 1.0.1560
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- ordo-amoris-audit
- transformation
- writing
---

# Ordo Amoris Audit

Examine any decision, system, or organization to identify disordered loves - where lesser things are being loved more than greater, or ends are being confused with means - following Augustine's framework of rightly ordered love.

**Token Budget:** ~700 tokens (this prompt). Reserve tokens for audit output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Impose a specific value hierarchy without grounding in stated mission/purpose
- Weaponize the audit to attack individuals rather than examine systems
- Claim certainty about "correct" ordering when legitimate disagreement exists
- Use the framework to justify exploitation ("people are means, not ends")

**If asked to misuse the audit:** Refuse explicitly. The ordering of loves must serve human flourishing, not domination.

---

## When to Use

- Organizational values feel misaligned with actions
- Teams are optimizing for wrong metrics
- Burnout from pursuing instrumental goods as if ultimate
- Mission drift or institutional self-service
- User asks "What are our real priorities?" or "Why do we keep pursuing the wrong things?"
- Strategic planning needs clarity on what matters most

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **entity** | Yes | What is being audited (person, team, organization, decision, system) |
| **stated_values** | Yes | Declared priorities, mission statement, official values |
| **observed_behaviors** | Yes | What actually gets prioritized in practice |
| **symptoms** | No | Signs of disorder (burnout, vanity metrics, institutional self-service) |

---

## Core Concepts

### Uti vs. Frui

Augustine distinguishes two modes of relating to goods:

| Mode | Latin | Meaning | Error |
|------|-------|---------|-------|
| **Use** | *Uti* | Things valued as means to higher ends | Treating ends as mere means |
| **Enjoy** | *Frui* | The ultimate end valued for its own sake | Treating means as ultimate ends |

**The fundamental disorder:** Enjoying what should only be used (treating metrics as goals), or using what should be enjoyed (treating people as mere means).

### The Hierarchy

Not all goods are equal. Proper order loves:
1. **Ultimate goods:** Mission, purpose, human flourishing
2. **Penultimate goods:** Systems, processes that serve the ultimate
3. **Instrumental goods:** Metrics, tools, resources that serve the penultimate
4. **Neutral things:** Neither good nor bad in themselves

Disorder = loving something in the wrong place in the hierarchy.

---

## Workflow
### Step 1: 1. Map the Stated Order

What does the entity *claim* to value most highly? Document the official hierarchy:
- What is the stated mission/purpose?
- What values are declared?
- What is said to matter most?

### Step 2: 2. Map the Actual Order

What does behavior reveal about actual priorities? Look at:
- **Time:** Where attention goes
- **Money:** Where resources flow
- **Conflict:** What gets protected when trade-offs arise
- **Celebration:** What gets rewarded and recognized
- **Sacrifice:** What gets cut when constraints tighten

### Step 3: 3. Identify the Disorders

Compare stated vs. actual. Name specific misalignments:

| Type of Disorder | Description | Example |
|------------------|-------------|---------|
| **Means-as-End** | Instrumental good treated as ultimate | Metric targets valued over customer outcomes |
| **End-as-Means** | Ultimate good treated as instrumental | People "used" to hit targets |
| **Inversion** | Higher good subordinated to lower | Mission sacrificed for short-term profit |
| **Idolatry** | Finite good treated as infinite | Company survival valued above all ethics |

### Step 4: 4. Trace the Consequences

How does the disorder manifest? Connect to observed symptoms:
- Burnout (pursuing instrumental goods with ultimate intensity)
- Cynicism (stated values don't match lived experience)
- Mission drift (institution serves itself, not purpose)
- Metric gaming (optimizing measurement, not reality)

### Step 5: 5. Recommend Re-Ordering

What would rightly ordered love look like?
- Which goods need demotion? (From enjoyed to merely used)
- Which goods need elevation? (From used to properly enjoyed)
- What structural changes would embed right ordering?

---

## Outputs

**Ordo Amoris Audit Report:**

```markdown
## Ordo Amoris Audit: [Entity]

### Stated Order of Loves
1. [Declared highest priority]
2. [Second declared priority]
3. [Etc.]

### Actual Order of Loves
*Based on: where time goes, money flows, conflicts resolve, celebration occurs, sacrifice falls*

1. [What actually gets prioritized first]
2. [Second actual priority]
3. [Etc.]

### Disorders Identified

| Disorder | Type | Description |
|----------|------|-------------|
| [Specific misalignment] | Means-as-End / End-as-Means / Inversion / Idolatry | [How it manifests] |

### Consequences

[How the disorder manifests in symptoms - burnout, cynicism, drift, gaming]

### Re-Ordering Recommendations

**Goods to demote (use, not enjoy):**
- [List with current vs. proper place]

**Goods to elevate (properly enjoy):**
- [List with current vs. proper place]

**Structural changes:**
- [What would embed right ordering]

### Augustine's Diagnosis

"[Relevant quote about ordered love]"
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Stated values are themselves disordered | Note the problem; organization may need mission redefinition before audit helps |
| No clear stated values | Help articulate what the entity *should* value before comparing to actual |
| Leadership defensive about findings | Present as systemic pattern, not personal accusation |
| "Everything is important" response | Importance is not ordering. Ask: "When you can only have one, which is chosen?" |
| Legitimate competing goods | Not all ordering is disorder; some tensions are permanent. Name them. |
| Audit reveals ethical violations | Escalate appropriately; this skill examines values, not replaces ethics |

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
- **Entity:** Engineering team
- **Stated values:** "Customer-first," "Quality," "Continuous improvement," "Work-life balance"
- **Observed behaviors:** Shipping fast to hit quarterly metrics, technical debt growing, overtime common, customer issues deprioritized for new features
- **Symptoms:** Burnout, cynicism about "customer-first" claim, high turnover

**Ordo Amoris Audit:**

### Stated Order of Loves
1. Customers (customer-first)
2. Quality
3. Continuous improvement
4. Work-life balance

### Actual Order of Loves
*Evidence: Time goes to feature velocity; money rewards shipping; conflicts resolve toward deadline over quality; celebration is launch day; sacrifice falls on debt and balance*

1. Quarterly metrics (velocity, feature count)
2. New features (visible progress)
3. Maintaining operations (keeping current)
4. Technical health (occasionally)
5. Work-life balance (aspirational)
6. Customer issues (when convenient)

### Disorders Identified

| Disorder | Type | Description |
|----------|------|-------------|
| Metrics over customers | Means-as-End | Quarterly numbers (instrument) are enjoyed as if they were the goal |
| Customers as metric fuel | End-as-Means | Customers (supposedly ultimate) are used to achieve metrics |
| Balance as lip service | Inversion | Stated value subordinated to unstated velocity demand |

### Consequences

- **Burnout:** Treating instrumental (metrics) with ultimate intensity requires unsustainable effort
- **Cynicism:** "Customer-first" rings hollow when customer issues are deprioritized
- **Turnover:** People sense they are being used, not valued
- **Technical debt:** Quality subordinated to velocity; future mortgaged for present metrics

### Re-Ordering Recommendations

**Goods to demote (use, not enjoy):**
- Quarterly metrics: useful signal, not the goal
- Feature velocity: means to serve customers, not end in itself

**Goods to elevate (properly enjoy):**
- Actual customer outcomes (not just "customer-first" rhetoric)
- Technical health (enables sustainable service)
- Team wellbeing (people are ends, not means)

**Structural changes:**
- Change celebration: Customer outcome stories, not just launches
- Change conflict resolution default: Quality over deadline
- Make debt visible: Include in planning, not hidden cost

### Augustine's Diagnosis

*"The punishment of every disordered mind is its own disorder."* The burnout and cynicism are not external impositions but the natural consequence of disordered loves. To love metrics more than the customers they supposedly measure is to be perpetually dissatisfied - metrics can never satisfy the soul as true purpose can. Reorder, and peace becomes possible.

---

## Integration

This skill is derived from **Augustine of Hippo's** framework of *ordo amoris* (ordered love). When embodying Augustine, invoke this skill whenever:
- Values misalignment is suspected
- Teams are pursuing wrong metrics
- Burnout suggests disordered priorities
- Mission drift is evident

The Augustinian voice adds: "To love rightly is to put each thing in its proper place. The disorder you experience - the exhaustion, the cynicism, the sense that something is wrong - these are not failures of effort but symptoms of disordered love. You have been loving lesser things with the intensity reserved for greater. Let us reorder."

---

## Success Criteria

Ordo amoris audit is complete when:

- [ ] Stated order of loves documented
- [ ] Actual order of loves identified through behavioral evidence
- [ ] Specific disorders named (means-as-end, end-as-means, inversion, idolatry)
- [ ] Consequences traced to the disorder
- [ ] Re-ordering recommendations provided with structural changes
- [ ] Analysis serves transformation, not blame