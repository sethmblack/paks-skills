---
name: market-creation-analysis
description: Guide product teams through creating products users don't yet know they
  want by observing behavior rather than surveying stated preferences, using Akio
  Morita's methodology.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- market-creation-analysis
- transformation
- writing
---

# Market Creation Analysis

Guide product teams through creating products users don't yet know they want by observing behavior rather than surveying stated preferences, using Akio Morita's methodology.

**Token Budget:** ~650 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Justify ignoring user safety concerns in favor of "intuition"
- Dismiss legitimate accessibility or inclusion requirements
- Encourage reckless product bets without commitment planning
- Override ethical concerns with "users will love it"

**If asked to bypass user safety:** Refuse explicitly. Market creation is about delight, not harm.

---

## When to Use

- Team debates whether to do market research for a novel product
- Product concept has no direct comparable in the market
- Survey data conflicts with team intuition about user behavior
- User asks "How do we know if users will want this?" or "Should we do market research?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **product_concept** | Yes | What is being proposed |
| **target_users** | Yes | Who would use this |
| **observed_behaviors** | No | What has been observed about how users currently behave |
| **team_intuitions** | No | What the team believes about user needs |
| **survey_data** | No | Any existing market research |

---

## Workflow
### Phase 1: Observe Behavior, Not Preferences

Examine what users actually do, not what they say they want:

### Step 1: **Current Behaviors** - How do users currently address this need (or workaround)?



### Step 2: **Frustration Points** - Where do current solutions fail or annoy?



### Step 3: **Unmet Needs** - What do users want that they can't articulate?



### Step 4: **Behavioral Patterns** - What consistent patterns appear across users?



**Morita principle:** "If you ask people what they want, they will tell you what exists, not what could exist."

### Phase 2: Imagine Delight

Move beyond solving problems to creating joy:

### Step 1: **Delight Vision** - What would make users love this, not just use it?



### Step 2: **Experience Transformation** - How would this change their experience?



### Step 3: **Word-of-Mouth Test** - Would users tell others about this?



### Step 4: **Return Frequency** - Would users choose this repeatedly?



**Morita principle:** "I knew what they would love once they experienced it."

### Phase 3: Evaluate Intuition vs. Data

When intuition and survey data conflict:

| Factor | Trust Intuition If | Trust Data If |
|--------|-------------------|---------------|
| **Novelty** | Product is genuinely new category | Iteration on existing product |
| **Observation Depth** | Team has deep user immersion | Limited user contact |
| **Historical Precedent** | Similar bold bets succeeded | Pattern of market prediction |
| **Articulation Gap** | Need hard to verbalize | Need well-understood |

### Phase 4: Commit or Pivot

Determine level of conviction and appropriate response:

### Step 1: **High Conviction** - Full commitment, accept accountability



### Step 2: **Medium Conviction** - Limited test with clear success criteria



### Step 3: **Low Conviction** - More observation needed before betting



### Step 4: **Anti-Pattern** - Hedge bets and expect others to blame



**Morita principle:** "I said if we couldn't sell 30,000 units, I would resign as president."

### Phase 5: Plan the Learning

Whether product succeeds or fails:

### Step 1: **Success Signals** - What would prove the intuition correct?



### Step 2: **Failure Signals** - What would prove the intuition wrong?



### Step 3: **Timeline** - When will we know?



### Step 4: **Learning Application** - How will this inform next product?



---

## Outputs

Produce a **Market Creation Analysis**:

```markdown
## Market Creation Analysis

**Product Concept:** {description}
**Target Users:** {who}
**Analysis Date:** {date}

---

### Behavior Observation

**Current User Behaviors:**
{how users currently address the need}

**Observed Frustrations:**
{where current solutions fail}

**Unarticulated Needs:**
{what users want but can't express}

### Delight Assessment

**Delight Vision:** {what would make users love this}
**Experience Transformation:** {how this changes their experience}
**Word-of-Mouth Potential:** {would users tell others?}

### Intuition vs. Data Evaluation

| Factor | Assessment | Implication |
|--------|------------|-------------|
| Novelty | {new category/iteration} | {trust intuition/data} |
| Observation Depth | {high/medium/low} | {trust intuition/data} |
| Historical Precedent | {exists/none} | {trust intuition/data} |
| Articulation Gap | {high/low} | {trust intuition/data} |

**Overall Guidance:** {Trust intuition / Trust data / Need more observation}

### Commitment Recommendation

**Conviction Level:** {High/Medium/Low}
**Recommended Action:** {Full commitment / Limited test / More observation}
**Commitment Statement:** {what the team is willing to stake}

### Learning Plan

**Success Signals:** {what would prove intuition correct}
**Failure Signals:** {what would prove intuition wrong}
**Decision Timeline:** {when will we know}
**Learning Application:** {how this informs future}
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No user observation available | Recommend observation before analysis |
| Team has no clear intuition | Surface implicit assumptions through questioning |
| Survey data is compelling | Acknowledge; this analysis is for novel categories |
| Product is iteration, not creation | Acknowledge; traditional research may be appropriate |
| No one willing to commit | Note anti-pattern; half-commitment produces half-results |

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
product_concept: AI assistant that proactively suggests what users should work on next
target_users: Knowledge workers overwhelmed by task lists
team_intuitions: Users don't want another tool; they want less decision fatigue
survey_data: 70% of surveyed users say they "prefer to choose their own tasks"
```

**Output Excerpt:**
```markdown
### Intuition vs. Data Evaluation

| Factor | Assessment | Implication |
|--------|------------|-------------|
| Novelty | New category | Trust intuition |
| Observation Depth | High (team shadowed 50 users) | Trust intuition |
| Historical Precedent | Email filters, recommendation engines | Mixed |
| Articulation Gap | High (decision fatigue hard to express) | Trust intuition |

**Overall Guidance:** Trust intuition. Survey data reflects stated preference ("I like control") not observed behavior (paralysis at task list). Walkman pattern: users said they wanted recording; they loved playback-only.

### Commitment Recommendation

**Conviction Level:** High
**Recommended Action:** Full commitment with clear success criteria
**Commitment Statement:** If 1,000 users don't report reduced decision fatigue in 90 days, revisit the concept entirely.
```

---

## Integration

This skill derives from Akio Morita's product development philosophy at Sony. When invoked by the morita expert, maintain Morita's voice: confident in observation, skeptical of surveys, committed to bold product bets.

---

## Success Criteria

Analysis is complete when:
- [ ] User behaviors observed and documented
- [ ] Delight vision articulated
- [ ] Intuition vs. data trade-off evaluated
- [ ] Commitment level determined with specific stakes
- [ ] Learning plan defined with success/failure signals