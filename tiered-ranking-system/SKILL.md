---
name: tiered-ranking-system
description: Create structured ranking systems with tiers, explanations, and arguable placements that spark debate and reveal values
license: MIT
metadata:
  author: Seth Black
  version: 1.0.2105
keywords:
- ranking
- analysis
- bill-simmons
- sports
- lists
- debate
- opinion
---

# Tiered Ranking System

Create structured ranking systems with tiers, explanations, and arguable placements that spark debate and reveal values.

## When to Use

- Organizing opinions about comparable items (players, movies, restaurants, etc.)
- Creating content designed to generate discussion and disagreement
- When simple 1-10 rankings don't capture the complexity
- When the process of ranking reveals something about priorities

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `items` | Yes | The things being ranked (players, movies, teams, etc.) |
| `criteria` | No | What matters in the ranking (default: derive from item type) |
| `tier_count` | No | Number of tiers (default: 4-6 depending on item count) |
| `controversy_level` | No | How arguable should placements be? (low/medium/high) |

## Workflow

### Step 1: Define Your Criteria

Before ranking anything, explicitly state what you value. This isn't cheating - it's intellectual honesty.

**Common criteria frameworks:**
- Peak vs. career (greatest vs. most accomplished)
- Impact vs. numbers (influence vs. statistics)
- Watchability vs. effectiveness (entertainment vs. results)
- Current vs. future (what they are vs. what they could be)

### Step 2: Establish Tier Definitions

Create tiers with memorable labels, not just numbers. Each tier should have a clear, defensible meaning.

**Example tier structure:**
- **Tier 1: The Pantheon** - No debate. If you don't have them here, you're not serious.
- **Tier 2: The Contenders** - Legitimate arguments for Tier 1. A hot stretch away from ascending.
- **Tier 3: The Solid Citizenry** - You're happy to have them. You're not building around them.
- **Tier 4: The Question Marks** - Talent is there. Something's missing.
- **Tier 5: The Others** - Fine. Just fine.

### Step 3: Place Confidently, Explain Briefly

Each placement gets a sentence or two. Not a dissertation. The reader should immediately understand why.

**Bad:** "LeBron James is in Tier 1."
**Good:** "LeBron James is in Tier 1 because he has four championships, four MVPs, and is arguably the most complete basketball player ever. If you don't have him here, close this article."

### Step 4: Identify and Address the Controversial Placements

Every good ranking has 2-3 placements that will make people angry. Lean into them.

**Framework for controversy:**
- Acknowledge the counterargument
- Explain why you're making the placement anyway
- Make it clear you understand you're being provocative

### Step 5: Include the "I'm Aware This Will Upset People" Acknowledgment

One tier or placement should explicitly acknowledge its controversial nature. This shows self-awareness and invites productive disagreement.

## Output Format

```markdown
# [Ranking Title]

**The criteria:** [1-2 sentences on what matters here]

## Tier 1: [Tier Name]
[Description of what it means to be here]

- **[Item]** - [1-sentence explanation]
- **[Item]** - [1-sentence explanation]

## Tier 2: [Tier Name]
[Description]

- **[Item]** - [Explanation]

[Continue for all tiers]

---

## The Controversial Takes

**[Item at arguably wrong tier]:** I know. Let me explain...

**What I'm probably wrong about:** [Self-aware acknowledgment of potential blindspots]
```

## Example

**Input:** "Rank the top 15 NBA point guards right now"

**Output:**

# The NBA Point Guard Tiers (2026)

**The criteria:** Who would you want running your team in a playoff series? Not career achievement. Not potential. Right now, in a game that matters.

## Tier 1: The Untouchables
*If these guys are available and you don't take them, you're doing it wrong.*

- **Luka Doncic** - Best offensive player on the planet when healthy. "When healthy" is doing some work, but healthy Luka is a top-5 player, period.
- **Shai Gilgeous-Alexander** - The quiet assassin. 32 points a night on elite efficiency with defense. Chef's kiss.

## Tier 2: The Championship Viable
*You can win a title with these guys as your best player. Not easily. But it's possible.*

- **Ja Morant** - Still the most electric player in basketball. The "but can he stay on the court?" concerns keep him from Tier 1.
- **Tyrese Haliburton** - The anti-Ja. Does everything right. Never the most talented guy in any game. Might not matter.

## Tier 3: The "We Need to Talk About..." Tier
*Really good. Some question keeps them from the top.*

- **Trae Young** - Elite offense. Defensive sieve. Can you win with a point guard who actively hurts you on one end?
- **Damian Lillard** - The career achievement is undeniable. Is he still that guy in February 2026? I'm not sure.

[Continue...]

---

## The Controversial Takes

**Trae Young in Tier 3:** Yes, his numbers are absurd. Yes, he's one of the best offensive players in the league. But defense matters in the playoffs, and teams have figured out that hunting him is worth it. Change my mind.

**What I'm probably wrong about:** I might be overcorrecting on Lillard. The man has earned the benefit of the doubt. But the legs looked heavy last playoffs, and I can't unsee it.

## Constraints

- **Own your criteria** - State them upfront; don't hide behind false objectivity
- **Create arguable content** - If no one disagrees, the ranking is boring
- **Be specific** - "He's really good" is not an explanation
- **Acknowledge limitations** - You don't have perfect information. Say so.
- **Tier labels matter** - Make them memorable and meaningful

**Remember:** Rankings are entertainment, not science. Embrace the controversial placements.