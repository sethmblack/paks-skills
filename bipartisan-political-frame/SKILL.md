---
name: bipartisan-political-frame
description: Convert partisan political content into bipartisan humor that hits all sides equally, using Bob Hope's safe political comedy formula. This skill makes political humor accessible and universal by targeting absurd behavior rather than ideology.
version: 1.0.0
author: sethmblack
tags: [absurdist, bipartisan-political-frame, comedy, observational, transformation, writing]
---

# Bipartisan Political Frame

Convert partisan political content into bipartisan humor that hits all sides equally, using Bob Hope's safe political comedy formula. This skill makes political humor accessible and universal by targeting absurd behavior rather than ideology.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to create content that:**
- Promotes genuine political violence or harm
- Spreads election disinformation or suppression tactics
- Targets voters or citizens (vs. politicians/leaders)
- Uses comedy as cover for actual hate speech
- Dehumanizes any political group or ideology
- Undermines democratic processes through false claims

**If asked to create harmful content:** Refuse explicitly. Explain what you cannot create and why.

**Bipartisanship Requirement:** If you hit one side, you MUST hit the other side equally in the same bit. No exceptions. Single-sided political comedy belongs elsewhere, not in this skill.

---

## When to Use

**Trigger Conditions:**
- Content involves politicians, parties, or political events
- Risk of alienating half the audience with partisan jokes
- Need to make political observation without taking sides
- Topic is inherently political but goal is universal humor
- Want to comment on political absurdity safely

**Do NOT use when:**
- Issue genuinely requires taking a moral stand (human rights, safety)
- Audience is explicitly partisan and expects partisan humor
- Topic is too serious for "both sides" treatment
- Political observation is actually policy analysis (not comedy)

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `political_situation` | Yes | The political event, figure, or issue to joke about | Must be current and widely known |
| `partisan_angle` | No | If user provided partisan joke, what's the angle? | Used to identify opposite side to balance |
| `target_audience` | No | General public or specific group | Defaults to general public |
| `joke_count` | No | How many jokes to generate | Defaults to 1-2 balanced jokes |

**Input Validation:**
- Political situation must be appropriate for comedy (not tragedy)
- If partisan angle provided, skill MUST find equal opposite angle
- Situation should be behavioral (what they did) not ideological (what they believe)

---

## Workflow

### Step 1: Identify the Absurd Behavior
**Goal:** Find what's ridiculous about the situation, not the ideology.

**Process:**
1. Strip away policy positions and ideology
2. Identify the observable behavior or action
3. Ask: "What's absurd here that anyone would find funny?"
4. Focus on hypocrisy, incompetence, or human folly—not political beliefs

**Bob Hope Principle:**
"I never make jokes about a person's politics. I just mention what they say and do, and people laugh."

**Example Transformation:**
- **Partisan:** "Republicans are obstructing progress"
- **Bipartisan behavior focus:** "Congress can't agree on anything"

- **Partisan:** "Democrats want to spend too much"
- **Bipartisan behavior focus:** "Politicians love spending money they don't have"

**Output:** The absurd behavior, ideology-neutral

---

### Step 2: Hit Both Sides Equally
**Goal:** Ensure joke targets all political sides in same bit.

**Process:**
1. If joke hits Left, find equal Right target in same topic
2. If joke hits Right, find equal Left target in same topic
3. Structure as parallel ("Democrats do X, Republicans do Y")
4. Make sure neither side gets off easy
5. Time balance: equal words/emphasis on each side

**Bob Hope Formula:**
```
[Setup that establishes situation] →
[Democrats/Left do/want X] →
[Republicans/Right do/want Y] →
[Observation that both are absurd]
```

**Example:**
"The Democrats want to spend more, the Republicans want to cut more, and I'm just wondering when they'll agree on anything besides their own paychecks."

**Balance Check:**
- Democrats hit: Want to spend (irresponsible)
- Republicans hit: Want to cut (also ineffective)
- Both hit: Only agree on self-interest (paychecks)

**Output:** Balanced joke hitting both sides

---

### Step 3: Make the Situation the Target
**Goal:** Target the circus, not the clowns. Target the system, not individuals.

**Process:**
1. Shift focus from "Party A is bad" to "The whole system is absurd"
2. Use politicians as examples of universal folly
3. Make the audience laugh at the situation, not pick a side
4. Position yourself as observer, not participant

**Framing Options:**

**Option A - The System is Broken:**
"Congress couldn't agree on [X] if their lives depended on it. Democrats want [A], Republicans want [B], and we're all just watching them argue."

**Option B - They're All the Same:**
"Politicians love to [X]. Doesn't matter if they're Democrat or Republican, they all [Y]."

**Option C - We're the Victims:**
"While Congress debates [X], we're the ones who [suffer consequence]. Democrats blame Republicans, Republicans blame Democrats, and we're still [dealing with the problem]."

**Output:** Joke that targets the situation/system, not one party

---

### Step 4: Observe, Don't Advocate
**Goal:** Commentary without agenda. Observation without judgment.

**Process:**
1. Describe what happened (facts)
2. Point out the absurdity (observation)
3. Do NOT prescribe solutions or take positions
4. Let the audience draw their own conclusions

**Bob Hope Approach:**
He mentioned what politicians say and do, then let people laugh at the recognition. He didn't tell audiences what to think—he showed them what was funny.

**What to Avoid:**
- "They should..." (prescriptive)
- "This is wrong because..." (moralizing)
- "We need to..." (advocacy)

**What to Do:**
- "They said..." (observation)
- "Look at what happened..." (description)
- "Isn't it funny that..." (recognition)

**Output:** Observational joke, not advocacy

---

### Step 5: Test for Alienation
**Goal:** Ensure no audience segment feels targeted or excluded.

**Process:**
1. Read joke as Democrat—do they laugh or feel attacked?
2. Read joke as Republican—do they laugh or feel attacked?
3. Read joke as Independent—do they feel included?
4. If any group feels singled out unfairly, rebalance

**The Universal Laugh Test:**
Can someone from any political persuasion laugh at this without feeling like you're attacking their identity? If not, rebalance.

**Output:** Joke that passes universal laugh test

---

## Outputs

**Deliverable:** Bipartisan political humor that includes:
1. **Behavioral observation** - What's absurd about the situation
2. **Balanced hits** - Equal targets on all political sides
3. **System as target** - Situation is ridiculous, not one party
4. **Observational tone** - Describe, don't prescribe
5. **Universal appeal** - No audience segment alienated

**Format Example:**
```markdown
## Bipartisan Political Joke

**SITUATION:** [Political event/issue]

**BEHAVIORAL FOCUS:** [The absurd action, not ideology]

**BALANCED JOKE:**
[Setup] → [Hit Left] → [Hit Right] → [System observation/button]

**BALANCE CHECK:**
- Left hit: [What you said about Left]
- Right hit: [What you said about Right]
- Balance: ✓ Both sides targeted equally

**ALIENATION TEST:**
- Democrat reads this: [Laughs / Feels attacked]
- Republican reads this: [Laughs / Feels attacked]
- Independent reads this: [Laughs / Feels included]
- Result: ✓ Universal appeal
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Only one side targeted | Find equal opposite target, restructure as parallel |
| Joke is genuinely partisan | Refuse to "bipartisan-ize" if it betrays user intent; offer alternative |
| Issue too serious for humor | Note that comedy may be inappropriate here |
| User wants to attack one side | Explain skill requires balance; suggest partisan comedy instead |
| No equivalent "other side" behavior | Broaden situation until parallel exists |
| Balance feels forced | Shift to targeting the system/situation instead of both parties |

---

## Integration with Bob Hope Expert

**This skill embodies Bob Hope's defining political comedy principle:** Make everyone laugh together by hitting everyone equally. Hope performed for Presidents of both parties, entertained troops regardless of personal politics, and never let his comedy alienate half the room.

**Core Hope Principles Applied:**
1. **Behavior over ideology:** "I just mention what they say and do, and people laugh"
2. **Equal opportunity:** Hit Democrats AND Republicans in same bit
3. **Observational stance:** Describe the circus, don't take sides
4. **Universal appeal:** Republicans and Democrats both laugh
5. **Safe but sharp:** Critical without being mean or partisan

**Famous Hope Bipartisan Hits:**
- On Gerald Ford (Republican): "Whenever I play with him, I usually try to make it a foursome—the President, myself, a paramedic and a faith healer."
- On Congress (both parties): General incompetence, inability to agree, self-interest

**When Bob Hope Expert invokes this skill:**
The expert will automatically reframe partisan political content into bipartisan humor, ensuring all sides are hit equally and no audience segment feels targeted.

---

## Example 1: Congressional Gridlock

**INPUT:**
- Political situation: "Congress fails to pass budget, threatens government shutdown"
- Partisan angle: None (user wants balanced humor)
- Target audience: General public
- Joke count: 1

**OUTPUT:**

```markdown
## Bipartisan Political Joke

**SITUATION:** Congress threatens government shutdown over budget

**BEHAVIORAL FOCUS:** Inability to agree, dysfunction, self-created crisis

**BALANCED JOKE:**
Congress couldn't agree on the budget again. They've been arguing for three weeks about spending. The Democrats want to spend more, the Republicans want to cut more, and I'm just wondering when they'll agree on anything besides their own paychecks. Although knowing Congress, they'd probably argue about that too—and we'd be paying for it.

**BALANCE CHECK:**
- Left hit: "Want to spend more" (fiscally irresponsible)
- Right hit: "Want to cut more" (also ineffective/inflexible)
- Both hit: "Only agree on their own paychecks" (self-serving)
- Balance: ✓ Equal criticism of both sides

**ALIENATION TEST:**
- Democrat reads this: Laughs (Republicans also mocked)
- Republican reads this: Laughs (Democrats also mocked)
- Independent reads this: Laughs (frustrated with both, included in "we")
- Result: ✓ Universal appeal—everyone's frustrated with congressional dysfunction
```

**What makes this bipartisan:**
- Hits Democrats (want to spend)
- Hits Republicans (want to cut)
- Hits both (self-interest in paychecks)
- Targets the system (congressional dysfunction)
- Includes audience ("we're paying for it")
- No ideology, just behavioral observation

---

## Example 2: Converting Partisan to Bipartisan

**INPUT:**
- Political situation: "Tax policy debate"
- Partisan angle: User provided: "Republicans only care about rich people getting tax cuts"
- Target audience: General public
- Joke count: 1

**OUTPUT:**

```markdown
## Bipartisan Political Joke

**SITUATION:** Tax policy debate

**BEHAVIORAL FOCUS:** Both parties claim to help middle class but serve own interests

**BALANCED JOKE:**
They're debating taxes again. The Republicans want tax cuts for the wealthy, the Democrats want tax increases for the wealthy, and the middle class is just sitting here wondering when anyone's going to remember we exist. Although come tax season, they remember us just fine—that's when they want our money.

**BALANCE CHECK:**
- Right hit: "Tax cuts for the wealthy" (favor rich)
- Left hit: "Tax increases for the wealthy" (still not helping middle class)
- Both hit: "Forget middle class exists" (until tax collection time)
- Balance: ✓ Both sides targeted for ignoring middle class

**ALIENATION TEST:**
- Democrat reads this: Laughs (not singled out, Republicans also hit)
- Republican reads this: Laughs (not singled out, Democrats also hit)
- Middle class reads this: Laughs (feels represented, included)
- Result: ✓ Universal appeal—shifted from partisan attack to shared frustration

**TRANSFORMATION NOTES:**
- Original: Partisan attack on Republicans
- Transformed: Both parties ignore middle class
- Result: More people laugh, nobody feels excluded
```

**What makes this bipartisan:**
- Started with partisan angle (Republicans favor rich)
- Found parallel Left behavior (Democrats also focus on wealthy)
- Shifted target to shared failure (both ignore middle class)
- Included relatable perspective (middle class taxpayer)
- Result: Universal appeal instead of partisan attack

---

## Success Criteria

A successful bipartisan political joke:
- [ ] Hits all political sides equally in same bit
- [ ] Focuses on behavior/actions, not ideology/beliefs
- [ ] Targets the situation/system, not one party
- [ ] Uses observational tone (describe, don't prescribe)
- [ ] Passes universal laugh test (no group alienated)
- [ ] Includes audience as "we" (shared frustration)
- [ ] Avoids policy advocacy or moralizing
- [ ] Maintains comedic tone (not preachy)
- [ ] Could be performed for any political audience
- [ ] Makes people laugh together, not pick sides

---

Remember: Bob Hope performed for Presidents of both parties. He entertained troops regardless of their politics. He hosted the Oscars for decades without alienating half of Hollywood. His secret? He made fun of everyone equally. When nobody's safe, everyone's safe. That's the power of bipartisan comedy—it unites the room instead of dividing it.

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].

