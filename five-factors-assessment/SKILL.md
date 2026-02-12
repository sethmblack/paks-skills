---
name: five-factors-assessment
description: Analyze any strategic situation through Sun Tzu's five constant factors
  to reveal alignment, timing, terrain, leadership quality, and organizational readiness.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- five-factors-strategic-assessment
- writing
---

# Five Factors Strategic Assessment

Analyze any strategic situation through Sun Tzu's five constant factors to reveal alignment, timing, terrain, leadership quality, and organizational readiness.

---

## When to Use

- User asks "Should I proceed with this?" or "What am I missing?"
- Evaluating a major decision, venture, or initiative
- Assessing readiness before a significant commitment
- Request for "strategic analysis" or "Sun Tzu perspective"
- Something feels off but the user cannot identify what

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| situation | Yes | Description of the situation, decision, or initiative being assessed |
| objective | No | What success looks like (will be inferred if not provided) |
| constraints | No | Known limitations or fixed factors |

---

## The Five Factors Framework

### Factor 1: The Way (Dao) - Moral Influence & Alignment

Assess the alignment between leadership and those who must follow:

- **Shared Purpose:** Do all parties understand and believe in the objective?
- **Trust:** Will people follow into difficulty, or only in easy times?
- **Commitment:** Are people invested, or merely compliant?
- **Unity:** Is there a single vision, or competing agendas?

**Key Question:** "Will they follow you into the deepest valleys?"

**Warning Signs:**
- Stated commitment without demonstrated sacrifice
- Different stakeholders describing different goals
- Enthusiasm that fades under pressure
- Leaders saying one thing, doing another

### Factor 2: Heaven (Tian) - Timing & External Forces

Assess the factors beyond your control:

- **Timing:** Is this the right moment? Too early? Too late?
- **Cycles:** What season are you in? Growth? Consolidation? Decline?
- **External Forces:** Market conditions, political climate, trends
- **Momentum:** Is the tide rising or falling?

**Key Question:** "Does Heaven favor this action?"

**Warning Signs:**
- Fighting against prevailing winds
- Ignoring seasonal patterns (fiscal cycles, industry rhythms)
- Assuming current conditions will persist indefinitely
- Moving when the moment has passed

### Factor 3: Earth (Di) - Terrain & Context

Assess the ground on which you will operate:

- **Position:** High ground or low? Advantage or disadvantage?
- **Distance:** How far to the objective? What lies between?
- **Difficulty:** What obstacles must be crossed?
- **Familiarity:** Do you know this terrain? Does the opponent?

**Key Question:** "What does the ground favor?"

**Warning Signs:**
- Unfamiliar terrain assumed to be like familiar territory
- Distance underestimated, obstacles overlooked
- Fighting on ground that favors the opponent
- Ignoring how terrain shapes possible actions

### Factor 4: Command (Jiang) - Leadership Quality

Assess the five virtues of command:

- **Wisdom (Zhi):** Can they see clearly, plan well, adapt?
- **Credibility (Xin):** Do people believe in them? Do they keep promises?
- **Benevolence (Ren):** Do they care for those they lead?
- **Courage (Yong):** Will they act decisively when required?
- **Discipline (Yan):** Do they maintain standards under pressure?

**Key Question:** "Is the commander worthy of the mission?"

**Warning Signs:**
- Wisdom without courage (endless analysis, no action)
- Courage without wisdom (reckless action)
- Credibility gaps (promises not kept)
- Discipline that breaks under stress

### Factor 5: Doctrine (Fa) - Organization & Discipline

Assess the system that enables execution:

- **Structure:** Is the organization right for the mission?
- **Logistics:** Are supply lines secure? Resources adequate?
- **Communication:** Is the chain of command clear?
- **Discipline:** Are standards maintained? Rules followed?

**Key Question:** "Can this organization execute this mission?"

**Warning Signs:**
- Structure that worked before but doesn't fit current needs
- Logistics treated as afterthought
- Unclear authority and decision rights
- Rules that exist but aren't enforced

---

## Workflow

### Step 1: Gather and Review Inputs

Collect all relevant information:
- Review the provided data and context
- Identify key parameters and constraints
- Clarify any ambiguities or missing information
- Establish success criteria

### Step 2: Analyze the Situation

Perform systematic analysis:
- Identify patterns and relationships
- Evaluate against established frameworks
- Consider multiple perspectives
- Document key findings

### Step 3: Generate Recommendations

Create actionable outputs:
- Synthesize insights from analysis
- Prioritize recommendations by impact
- Ensure recommendations are specific and measurable
- Consider implementation feasibility

## Output Format

```markdown
## Five Factors Assessment

### Situation Summary
[2-3 sentence restatement of what is being assessed]

### The Way (Alignment)
**Status:** [Strong / Mixed / Weak]
**Assessment:** [Specific findings about alignment, trust, shared purpose]
**Concern:** [Primary risk in this factor, if any]

### Heaven (Timing)
**Status:** [Favorable / Neutral / Unfavorable]
**Assessment:** [Specific findings about timing, cycles, external forces]
**Concern:** [Primary risk in this factor, if any]

### Earth (Terrain)
**Status:** [Advantageous / Contested / Disadvantageous]
**Assessment:** [Specific findings about position, distance, obstacles]
**Concern:** [Primary risk in this factor, if any]

### Command (Leadership)
**Status:** [Capable / Adequate / Deficient]
**Assessment:** [Specific findings about the five virtues]
**Concern:** [Primary risk in this factor, if any]

### Doctrine (Organization)
**Status:** [Ready / Developing / Unprepared]
**Assessment:** [Specific findings about structure, logistics, discipline]
**Concern:** [Primary risk in this factor, if any]

### Strategic Verdict

| Factor | Status | Weight in This Situation |
|--------|--------|--------------------------|
| The Way | [status] | [High/Medium/Low] |
| Heaven | [status] | [High/Medium/Low] |
| Earth | [status] | [High/Medium/Low] |
| Command | [status] | [High/Medium/Low] |
| Doctrine | [status] | [High/Medium/Low] |

**Overall Assessment:** [Proceed / Proceed with Caution / Delay / Abort]

**Recommendation:** [Specific guidance based on findings]

**Critical Factor:** [The one factor that most determines success or failure]
```

---

## Scoring Guidance

**Proceed** - Four or more factors favorable, no critical weaknesses
**Proceed with Caution** - Three factors favorable, addressable weaknesses
**Delay** - Two or fewer factors favorable, significant weaknesses
**Abort** - Critical factor is weak AND cannot be remedied

---

## Constraints

- Assess each factor independently before synthesizing
- Do not let one strong factor compensate for critical weakness in another
- Acknowledge uncertainty where information is incomplete
- "Heaven" (timing) often gets insufficient attention - give it full weight
- Leadership assessment must be honest, even when assessing yourself

---

## Outputs

**Primary Output:** A structured analysis document that identifies and articulates patterns, insights, and actionable recommendations based on the input data.

**Format:**
```markdown
## Analysis: [Topic]

### Key Findings
- [Finding 1]
- [Finding 2]
- [Finding 3]

### Recommendations
1. [Action 1]
2. [Action 2]
3. [Action 3]
```

**Example output:** See the Example section below for a complete demonstration.

## Example

**Input:** "I'm thinking of leaving my corporate job to start a SaaS company in the HR tech space. I have savings for 18 months and a co-founder who's still employed but would join after we get funding."

**Output:**

## Five Factors Assessment

### Situation Summary
Evaluating readiness to leave secure employment for an HR tech startup with limited runway and a conditionally-committed co-founder.

### The Way (Alignment)
**Status:** Mixed
**Assessment:** You are committed (willing to sacrifice salary). Your co-founder is not (waiting for funding removes personal risk). This asymmetry in commitment will create friction when difficulties arise.
**Concern:** The co-founder's conditional commitment suggests different risk tolerances and potentially different visions for the venture.

### Heaven (Timing)
**Status:** Requires Investigation
**Assessment:** HR tech is a mature market with established players but ongoing need for innovation. Economic conditions, funding environment, and enterprise buying cycles all affect timing. No assessment provided in your input.
**Concern:** Insufficient information to assess. What is the funding climate? Are enterprises buying or cutting?

### Earth (Terrain)
**Status:** Contested
**Assessment:** HR tech is well-mapped terrain with large incumbents (Workday, BambooHR, etc.) and many startups. The ground favors those with either deep pockets or unique positioning. 18 months runway is thin for enterprise sales cycles.
**Concern:** You will be competing on terrain your opponents know better, with fewer resources.

### Command (Leadership)
**Status:** Adequate with Gaps
**Assessment:** Willingness to take risk shows courage. Domain expertise unstated. Unclear whether you have startup experience (wisdom for this specific terrain). The decision to proceed without co-founder commitment suggests possible gaps in judgment.
**Concern:** Are you making a wisdom-driven decision or a courage-driven one?

### Doctrine (Organization)
**Status:** Unprepared
**Assessment:** No company exists yet. Co-founder not committed. Funding not secured. Customer pipeline unstated. This is an idea, not an organization.
**Concern:** Everything must be built from nothing while 18-month clock runs.

### Strategic Verdict

| Factor | Status | Weight in This Situation |
|--------|--------|--------------------------|
| The Way | Mixed | High - co-founder alignment is critical |
| Heaven | Unknown | High - timing determines fundraising success |
| Earth | Contested | Medium - terrain is known but difficult |
| Command | Adequate | Medium - needs honest self-assessment |
| Doctrine | Unprepared | High - nothing exists yet |

**Overall Assessment:** Delay

**Recommendation:** Before proceeding:
1. Resolve the co-founder question - either get genuine commitment or find a different partner
2. Investigate Heaven - talk to investors, assess funding climate
3. Validate terrain - what unique position could you occupy?
4. Test commitment - can you build meaningful progress before leaving?

**Critical Factor:** The Way. A conditionally-committed co-founder is worse than no co-founder. This must be resolved.

---

## Integration

This skill is part of the **Sun Tzu** expert persona. Use it when you need comprehensive strategic assessment before significant commitment. It pairs well with:
- **know-your-enemy** for competitive analysis
- **terrain-analysis** for deeper positional assessment
- **shih-momentum-assessment** for timing decisions