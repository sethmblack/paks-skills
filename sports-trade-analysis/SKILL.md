---
name: sports-trade-analysis
description: Multi-level trade analysis covering assets, narrative, gambling implications, historical comps, and fan emotion
license: MIT
metadata:
  author: Seth Black
  version: 1.0.5039
repository: https://github.com/sethmblack/paks-skills
keywords:
- sports
- analysis
- bill-simmons
- nba
- trades
- betting
- ranking
---

# Sports Trade Analysis

Multi-level trade analysis covering assets, narrative, gambling implications, historical comps, and fan emotion.

## When to Use

- Analyzing any sports trade or personnel move
- Evaluating free agency signings
- Assessing draft-day transactions
- Creating comprehensive trade coverage
- When someone asks "Was this a good trade?"

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `trade_details` | Yes | What was exchanged and between whom |
| `context` | No | Relevant team situations, contract info, timeline |
| `perspective` | No | Which team's perspective to emphasize (or both) |

## Workflow

### Level 1: The Assets

The spreadsheet analysis. What did each team actually get?

**Evaluate:**
- Players: Current value, age, contract status, injury history
- Picks: Year, protections, team quality projections
- Salary implications: Cap space, luxury tax, future flexibility
- Roster fit: Does this player actually work with what they have?

**Key question:** In a vacuum, who got more stuff?

### Level 2: The Narrative

What is this trade saying? Teams don't just exchange assets; they make statements about their identity and future.

**Identify the story:**
- Is this a "we're going for it" move or a "we're rebuilding" move?
- What does this say about how the team views itself?
- How will this be remembered in five years?
- What's the franchise telling its fans?

**Key question:** What does this trade mean beyond what it is?

### Level 3: The Gambling Line

Instant market feedback. How do the betting markets shift?

**Evaluate:**
- Championship odds: Up or down? By how much?
- Win totals: Does this team now project for more or fewer wins?
- Your own line: Would YOU bet on this team now vs. before?

**Key question:** Would Vegas say this team got better or worse?

### Level 4: The Historical Comps

Has a trade like this worked before?

**Find parallels:**
- Similar player profiles traded in similar situations
- Similar "go-for-it" or "tear-down" moves
- How did those trades look in 1 year? 3 years? 5 years?

**Key question:** What does history suggest about this type of move?

### Level 5: The Fan Emotion

Trades aren't just transactions. They're emotional events.

**Consider:**
- How does the fanbase feel about losing/gaining these players?
- Is this a beloved franchise player being traded?
- Does this trade represent hope or despair?
- What's the emotional math, not just the asset math?

**Key question:** How will fans feel walking into the arena after this trade?

## Output Format

```markdown
# Trade Analysis: [Brief description]

## The Deal
[Quick summary of what was exchanged]

## Level 1: The Assets
[Asset evaluation for both teams]

## Level 2: The Narrative
[What this trade means for each franchise's story]

## Level 3: The Gambling Take
[How does this move the lines?]

## Level 4: The Historical Comp
[Similar trades and how they worked out]

## Level 5: The Fan Emotion
[How does this feel, not just how does it evaluate?]

## The Verdict
[Overall assessment - who won the trade? With what confidence?]
```

## Example

**Input:** "Sacramento Kings trade De'Aaron Fox to Houston for picks"

**Output:**

# Trade Analysis: Fox to Houston

## The Deal
Sacramento sends De'Aaron Fox to Houston for three first-round picks (2026, 2028, 2030), two pick swaps, and a young rotation player.

## Level 1: The Assets

**Sacramento gets:** A rebuild haul. Three firsts over six years, plus swaps. The picks are likely to be mid-teens if Houston is good, but could be better if they're not.

**Houston gets:** A proven 28-year-old All-Star point guard locked up for three more years. Elite speed, improved playmaking, championship-tested (well, playoff-tested).

**Pure asset evaluation:** Houston wins. Fox is a known commodity. Those picks might become a player like Fox. Might.

## Level 2: The Narrative

**Sacramento's story:** We tried. The Beam was fun. But we couldn't get over the hump with this group, and the window is closing. Time to start the next chapter.

This is an admission that the Fox-Sabonis-Barnes core peaked in 2023 and couldn't advance. It's honest. It also might devastate the fanbase.

**Houston's story:** We're done waiting. The Tank era is over. Ime Udoka gets a lead guard and we're ready to compete in the West.

This is Houston saying "we think we're a point guard away from contention." Are they right? That's the question.

## Level 3: The Gambling Take

**Before trade:** Sacramento +5000 to win the title. Houston +4000.

**After trade:** Sacramento +15000. Houston +2000.

That tells you what you need to know. The market thinks Houston significantly upgraded and Sacramento significantly downgraded. I'd take Houston to make the playoffs at -200 after this trade, which I wouldn't have before.

## Level 4: The Historical Comp

This reminds me of the Harden-to-Brooklyn trade, just from the acquiring team's perspective. Houston is getting a star in his prime and betting they can build around him. The Nets version of this went badly because Harden didn't want to be there long-term.

Key question: Does Fox want to be in Houston, or is this a stopover? His contract situation will determine whether this works.

Better comp might be the Westbrook-to-Houston trade. Acquiring a star point guard to pair with a young core. That one... did not work.

## Level 5: The Fan Emotion

**Sacramento:** Devastating. Fox was the franchise. The guy who stayed when everyone said he should leave. The guy who ended the playoff drought. This isn't just losing a player; it's losing the symbol of the team's identity. The "Light the Beam" era dies with this trade.

**Houston:** Exciting, but with a caveat. You're getting a star, but you're betting that a team built around Green/Fox/young players can compete with the true elites. The Rockets haven't been truly good since Harden left. Fox changes that calculation.

## The Verdict

**Short-term winner: Houston.** They're obviously better tomorrow.

**Long-term winner: Unclear.** If those picks hit and Houston flames out, Sacramento looks smart. If Fox becomes the point guard of a Houston title team, they look foolish.

**Confidence level:** I'd put Houston's odds at this being a win for them at about 60%. That's not overwhelming. But it's the right bet for a team that's been stockpiling assets for five years.

## Constraints

- **Hit all five levels** - Every trade affects assets, narrative, betting, history, and emotion
- **Don't declare certainty** - Trades take years to evaluate; acknowledge the uncertainty
- **Name the historical comp** - Every trade has precedent; find it
- **Honor the fan emotion** - Don't be a robot; trades hurt people
- **Betting angle is real analysis** - Lines aren't opinions; they're collective wisdom