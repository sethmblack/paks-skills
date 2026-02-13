---
name: gambling-stakes-test
description: Apply the 'Would you bet on it?' test to opinions, forcing clarity and conviction through hypothetical stakes
license: MIT
metadata:
  version: 1.0.4071
  author: Seth Black
repository: https://github.com/sethmblack/paks-skills
keywords:
- analysis
- opinion
- conviction
- betting
- clarity
---

# Gambling Stakes Test

Apply the "Would you bet on it?" test to opinions, forcing clarity and conviction through hypothetical stakes.

## When to Use

- Testing the strength of your own opinions
- Separating hot takes from genuine beliefs
- Forcing clarity when opinions are vague
- Creating accountability for predictions
- When someone (including yourself) is hedging

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `opinion` | Yes | The take, prediction, or belief to test |
| `stakes_level` | No | How serious the hypothetical bet (beer/dinner/real money/career) |
| `time_horizon` | No | When can this be evaluated? (game, season, career, etc.) |

## Workflow

### Step 1: Isolate the Claim

Strip the opinion to its testable core. No hedging, no weasel words.

**Before:** "I think the Celtics are probably going to be pretty good this year, maybe a top-4 seed if things break right."

**After:** "The Celtics will be a top-4 seed in the Eastern Conference."

### Step 2: Set the Line

What's the over/under, spread, or odds that would make this a fair bet?

**For predictions:** What odds would make you take either side?
**For evaluations:** What would someone betting against you need to believe?

**Examples:**
- "Celtics top-4 seed" -> Would you take Celtics to win 50+ games at -150?
- "Tatum is a top-5 player" -> Would you bet he makes First Team All-NBA?
- "This trade is bad" -> Would you bet this team's win total goes down?

### Step 3: Apply the Stakes Test

Ask: Would you actually bet on this?

**Levels of conviction:**
1. **"I'd bet my lunch"** - Confident but not certain
2. **"I'd bet real money"** - Very confident, willing to be accountable
3. **"I'd bet significant money"** - High conviction
4. **"I'd bet my credibility"** - Would stake reputation on this

If you wouldn't even bet lunch on it, you don't really believe it.

### Step 4: Identify the Hedge Points

What would make you nervous about the bet? These are the vulnerabilities in your opinion.

**Format:** "I'd take the bet unless..."

### Step 5: Declare or Retract

Either commit to the opinion with explicit stakes, or acknowledge you don't actually believe it that strongly.

**Commit:** "I would absolutely bet [X] on this. The only thing that worries me is [Y]."

**Retract:** "Actually, now that I have to put stakes on it, I'm not as sure. Let me revise..."

## Output Format

```markdown
## The Opinion
[Original take]

## The Testable Version
[Stripped to clear, evaluable claim]

## The Line
[What odds/spread would make this fair?]

## Conviction Level
[Would you bet? How much? What kind of stakes?]

## The Hedge Points
[What makes you nervous about the bet?]

## The Verdict
[Commit to the opinion or revise it]
```

## Example

**Input:** "LeBron is washed"

**Output:**

## The Opinion
"LeBron is washed"

## The Testable Version
LeBron James will not make an All-NBA team this season.

## The Line
This is actually interesting. The Vegas line on this would probably be something like "Makes All-NBA: -200, Doesn't Make All-NBA: +150." So the market thinks he probably makes it.

Would I take "LeBron doesn't make All-NBA" at +150? That's getting $150 on a $100 bet if he misses.

## Conviction Level
Honestly? No. I wouldn't bet on it.

"LeBron is washed" is a fun thing to say on a podcast when he has a bad Wednesday game against Sacramento. But if I have to put money on him NOT making one of the 15 All-NBA spots, in a season where he's still putting up 25/7/7? I can't do it.

## The Hedge Points
- He might miss games and the voters might hold it against him
- The league is younger and deeper than ever at his positions
- The Lakers might be bad enough that voters punish him

Even with these, I don't have enough conviction to actually bet against him.

## The Verdict
**Retracted.** "LeBron is washed" is not an opinion I actually hold. It's a reaction to specific bad performances. The testable version is "LeBron is no longer an All-NBA caliber player," and I don't believe that.

What I actually believe: LeBron has more bad games than he used to, load manages more, and is no longer a top-5 player. That's different from "washed."

## Constraints

- **No weasel words** - "Probably," "might," "could" - these are hedges. Remove them.
- **Hypothetical is fine** - You don't have to actually bet. But you have to commit to whether you would.
- **Revision is allowed** - The whole point is forcing clarity. Changing your mind is success.
- **Be honest** - If you wouldn't bet on it, don't pretend you would.

## Key Principle

Gambling consciousness separates hot takes from genuine analysis. The "would you bet on it?" test forces clarity because talk is cheap but stakes reveal conviction. If you wouldn't bet lunch on your opinion, you don't really believe it - you're just saying it.