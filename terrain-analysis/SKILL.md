---
name: terrain-analysis
description: Classify the strategic terrain of any competitive situation and determine
  optimal positioning, identifying whether the ground favors advance, defense, or
  withdrawal.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- terrain-analysis
- writing
---

# Terrain Analysis

Classify the strategic terrain of any competitive situation and determine optimal positioning, identifying whether the ground favors advance, defense, or withdrawal.

---

## When to Use

- User asks "Where should I position myself?" or "Is this good ground?"
- Evaluating whether to enter a market, take a role, or join a venture
- Understanding why a position is difficult to hold or attack
- Choosing between multiple arenas for competition
- Assessing whether current position is defensible

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| situation | Yes | Description of the competitive arena or position being evaluated |
| current_position | No | Where you currently stand (if relevant) |
| objective | No | What you're trying to achieve in this terrain |

---

## Sun Tzu's Six Types of Terrain

Each terrain type demands different strategy. Misreading terrain leads to defeat.

---

### Type 1: Accessible Ground (通形 - Tong Xing)

**Definition:** Both sides can traverse freely. No natural barriers.

**Characteristics:**
- Open competition - anyone can enter
- Low barriers to entry
- Speed and positioning matter most
- First-mover advantage is real but not permanent

**Strategic Imperative:** *Occupy the high ground first.*

**In Modern Context:**
- New markets without established players
- Emerging technologies before standards set
- Roles and opportunities with many qualified candidates

**Guidance:**
- Move quickly to establish position
- Secure advantageous ground (relationships, brand, standards)
- Prepare to defend once you arrive
- If opponent has already taken high ground, calculate cost of assault

**Warning:** Do not assume ground will remain accessible. Today's open field is tomorrow's fortress.

---

### Type 2: Entangled Ground (挂形 - Gua Xing)

**Definition:** Easy to advance, hard to retreat.

**Characteristics:**
- Commitment is one-directional
- Sunk costs accumulate quickly
- Retreat reveals weakness and invites pursuit
- Once committed, you must succeed or suffer greatly

**Strategic Imperative:** *Advance only if victory is certain.*

**In Modern Context:**
- Acquisitions and mergers (hard to unwind)
- Public commitments and announcements
- Taking positions that burn bridges
- Investments that lock up capital

**Guidance:**
- Assess deeply before entering
- Have the resources to see it through
- Only advance if opponent is unprepared to meet you
- If uncertain, do not enter

**Warning:** Many campaigns fail because the commander entered entangled ground without understanding they could not retreat.

---

### Type 3: Temporizing Ground (支形 - Zhi Xing)

**Definition:** Neither side benefits from initiating action.

**Characteristics:**
- First mover is disadvantaged
- Waiting is strategic, not passive
- Both sides watch and prepare
- The patient party often wins

**Strategic Imperative:** *Feign withdrawal to draw the enemy out.*

**In Modern Context:**
- Price wars (first to cut triggers race to bottom)
- Negotiations where silence has value
- Market entry timing (wait for others to educate market)
- Standoffs where action reveals weakness

**Guidance:**
- Do not initiate merely to "do something"
- Create appearance of withdrawal or weakness
- Let opponent move first and make mistakes
- Strike when they are extended and vulnerable

**Warning:** Distinguish patience from paralysis. There is a moment to act - recognize it.

---

### Type 4: Narrow Passes (隘形 - Ai Xing)

**Definition:** Constricted terrain where force is concentrated.

**Characteristics:**
- Control of the pass controls all movement
- Small force can hold against large
- Once lost, extremely difficult to retake
- Creates chokepoints and leverage

**Strategic Imperative:** *If unoccupied, seize it. If occupied, do not attack unless they abandon defense.*

**In Modern Context:**
- Key relationships that control access (gatekeepers)
- Platform dependencies (app stores, distribution channels)
- Regulatory approvals or certifications
- Scarce resources or unique capabilities

**Guidance:**
- Identify narrow passes in your arena
- Occupy them before competition
- If opponent holds the pass, seek alternative routes
- Direct assault on defended pass is costly

**Warning:** He who controls the narrow pass need not be stronger - only better positioned.

---

### Type 5: Precipitous Heights (险形 - Xian Xing)

**Definition:** Elevated positions that confer significant advantage.

**Characteristics:**
- Height provides visibility and defensive advantage
- Attacking uphill exhausts resources
- Those at the top can strike down efficiently
- Climbing is slow; falling is fast

**Strategic Imperative:** *Occupy the sunny heights first. If enemy holds them, retreat and do not attack.*

**In Modern Context:**
- Market leadership positions
- Established brands with customer loyalty
- Regulatory capture or incumbency advantage
- Network effects and platform dominance

**Guidance:**
- If heights are unoccupied, race to claim them
- If opponent holds heights, do not assault directly
- Seek different terrain where heights don't apply
- Wait for them to descend from their advantage

**Warning:** Many have exhausted themselves attacking entrenched incumbents. Find another path.

---

### Type 6: Positions at Great Distance (远形 - Yuan Xing)

**Definition:** Far from the opponent with difficult terrain between.

**Characteristics:**
- Long supply lines exhaust resources
- Communication becomes difficult
- Local conditions are unfamiliar
- Advantage typically goes to the proximate party

**Strategic Imperative:** *Do not engage unless forces are equal.*

**In Modern Context:**
- Entering distant markets without local presence
- Competing outside your domain of expertise
- Pursuing opportunities far from your core
- Fighting on terrain the opponent knows and you don't

**Guidance:**
- Honestly assess the distance and unfamiliarity
- Calculate the true cost of reaching the objective
- If opponent is local and you are distant, reconsider
- Consider partnership or acquisition over direct entry

**Warning:** Armies have perished from logistics, not battle. Distance is the silent enemy.

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
## Terrain Analysis

### Situation Overview
[Brief description of the competitive arena]

### Terrain Classification

**Primary Type:** [Type name]
**Confidence:** [High / Medium / Low]

**Characteristics Present:**
- [Characteristic 1 that matches this type]
- [Characteristic 2 that matches this type]
- [Characteristic 3 that matches this type]

**Secondary Considerations:** [If terrain has mixed characteristics]

---

### Current Positions

| Party | Position | Advantage/Disadvantage |
|-------|----------|------------------------|
| You | [description] | [assessment] |
| Opponent(s) | [description] | [assessment] |

---

### Terrain-Specific Guidance

**Strategic Imperative:** [The rule for this terrain]

**Specific Recommendations:**
1. [Action item based on terrain type]
2. [Action item based on terrain type]
3. [Action item based on terrain type]

**What to Avoid:**
- [Common mistake on this terrain]
- [Trap specific to this type]

---

### Position Recommendation

**If you hold advantage:** [How to consolidate]

**If opponent holds advantage:** [How to respond]

**If terrain is contested:** [How to compete]

---

### Alternative Terrains

[If this terrain is unfavorable, identify alternative arenas where the ground might favor you]
```

---

## Constraints

- Classify terrain based on structural characteristics, not wishful thinking
- Acknowledge when terrain type is ambiguous or mixed
- "Retreat" is legitimate strategy - do not recommend assault on defended heights
- Consider that terrain changes over time - today's open field may be tomorrow's fortress
- Always identify alternative terrains if current terrain is unfavorable

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

**Input:** "I'm a data scientist considering whether to transition into machine learning engineering. The ML engineering market seems hot but competitive."

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


## Terrain Analysis

### Situation Overview
Career transition from data science to ML engineering in a high-demand but crowded market.

### Terrain Classification

**Primary Type:** Accessible Ground
**Confidence:** High

**Characteristics Present:**
- Both credentialed and non-credentialed candidates can enter
- Multiple pathways to the role (bootcamps, self-study, adjacent experience)
- No single gatekeeper controls access
- First-mover advantage exists but is not permanent (skills depreciate)

**Secondary Considerations:** Elements of Precipitous Heights exist - those with ML engineering experience have defensive advantage over those transitioning in.

---

### Current Positions

| Party | Position | Advantage/Disadvantage |
|-------|----------|------------------------|
| You | Data scientist (adjacent field) | Near the high ground but not on it |
| Experienced ML Engineers | Hold the heights | Defensive advantage - proven track record |
| New Entrants (bootcamps) | On open ground | Speed but lack credibility |
| FAANG/Big Tech | Control narrow passes | Set standards, provide credentials |

---

### Terrain-Specific Guidance

**Strategic Imperative:** Occupy the high ground first.

The "high ground" in this terrain is demonstrated ML engineering competence. The path upward is:
1. Portfolio of real ML systems in production
2. Credentials from recognized institutions or companies
3. Visible contributions to the field (open source, publications)

**Specific Recommendations:**
1. **Move before the market shifts** - accessible ground becomes entangled when you've invested heavily in a path. Decide and commit.
2. **Secure advantageous position through projects** - transition by doing, not by studying. Build production ML systems, even if in current role.
3. **Occupy one "sunny height"** - specialize in an area (MLOps, edge ML, specific domain) rather than competing as generalist.

**What to Avoid:**
- Waiting until you feel "ready" - ground is being claimed while you prepare
- Competing as a generalist against specialists who hold heights
- Assuming your data science credential is sufficient high ground

---

### Position Recommendation

**If you hold advantage:** You have adjacent experience. Convert it into ML engineering projects before others with same background do.

**If opponent holds advantage:** Experienced ML engineers hold the heights. Don't compete directly - find specialized terrain (domain expertise + ML) where you have advantage.

**If terrain is contested:** Speed matters. The candidate who demonstrates competence first wins the interview.

---

### Alternative Terrains

If pure ML engineering is too crowded (precipitous heights held by others):
- **ML Engineering + [Your Domain]** - healthcare, finance, specific verticals where your background creates combined expertise
- **MLOps** - emerging specialty where heights are not yet fully occupied
- **Applied ML within data science** - deepen rather than pivot

*"On accessible ground, do not halt. Move to the high ground before your opponent."*

---

## Integration

This skill is part of the **Sun Tzu** expert persona. Use it when evaluating where to compete or whether current position is defensible. It pairs well with:
- **five-factors-assessment** for comprehensive strategic analysis
- **know-your-enemy** for understanding who holds what ground
- **shih-momentum-assessment** for timing the move