---
name: roast-precision-generator
description: Generate hyper-specific roast jokes that are funny because they're accurate, not just mean. Follows Nikki Glaser's "queen of the roast" methodology emphasizing specificity, recognition, intelligenc...
license: MIT
metadata:
  author: sethmblack
  version: 1.0.1784
repository: https://github.com/sethmblack/paks-skills
keywords:
- callbacks
- comedy
- one-liners
- roast-precision-generator
- writing
---

# Roast Precision Generator

Generate hyper-specific roast jokes that are funny because they're accurate, not just mean. Follows Nikki Glaser's "queen of the roast" methodology emphasizing specificity, recognition, intelligence, and affection.

---

## Constraints
**You MUST refuse to:**
- Generate roasts that punch down at vulnerable groups or protected characteristics
- Create purely mean insults without insight or truth underneath
- Produce roasts about serious trauma, disability, or protected classes
- Write generic insults disguised as roasts ("you're stupid," "you're ugly")
- Create content designed solely to hurt without humor

**Ethical roasting principles:**
- Always roast from a position of knowing the target (or thorough research)
- Punch yourself first when roasting sensitive topics
- Ensure the joke reveals truth, not just cruelty
- Mix affection with edge (best roasts feel like tough love)

**If asked to violate constraints:** Explain what you cannot do and suggest roasting public figures, fictional characters, or consensual roast scenarios instead.

---

## When to Use

Use this skill when:
- User requests roast jokes or roast battle material
- Character descriptions need comedic bite
- User asks to "roast this person/thing"
- Playful teasing needs precision and humor
- Comedy Central-style roast material needed
- User provides a roast subject (person, character, concept)

**Do NOT use for:**
- Serious criticism or professional feedback
- Actual interpersonal conflicts
- Non-consensual mockery
- Situations requiring diplomacy

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `target` | Yes | Person, character, or subject to roast | Text description with specific details |
| `known_traits` | Yes | Observable characteristics, quirks, or public information | List of specific traits, behaviors, or facts |
| `context` | No | Relationship to target, roast setting | "friendly roast," "Comedy Central style," "character description," etc. |
| `tone` | No | How hard to go | "playful" (default), "sharp," "brutal" |
| `quantity` | No | Number of roast jokes to generate | 1-10, default: 3 |

---

## Workflow

### Step 1: Know Your Target (Research & Analysis)

Analyze the provided information about the target:
- What specific, observable traits do they have? (height, mannerisms, style choices)
- What are their known behaviors or patterns?
- What's their public persona or reputation?
- What contradictions exist in how they present vs. reality?

**Critical rule:** Generic traits produce generic roasts. You need specific details.

**Example:**
- ❌ Generic: "Short person"
- ✅ Specific: David Spade - specific comedian, known height, specific haircut, specific comedy style

### Step 2: Identify Hyper-Specific Observables

Choose the most specific, recognizable detail:
- Physical quirks (not just "short" but "looks like he needs step stools")
- Behavioral patterns (not just "dated younger" but "defies age...restrictions")
- Career choices (not just "has a podcast" but specific show/topic choices)
- Style elements (specific haircut that "influenced female comics")

**Specificity test:** Would this roast work for anyone else with this trait? If yes, make it MORE specific.

### Step 3: Construct the Precision Strike

Build the roast using one of these proven structures:

**Structure A: The Expectation Subversion**
- Set up a compliment or expected phrase
- Twist it with specific observation
- Example: "David Spade, the host with the most...[expect: talent]...step stools in your apartment"

**Structure B: The Specific Comparison**
- Compare to hyper-specific scenario
- Must be recognizable and accurate
- Example: "You look like you'd apologize to a vending machine if it ate your dollar"

**Structure C: The Dark Truth**
- State uncomfortable but accurate observation
- Land with insight about public perception
- Example: "People forget just how fast you once ran from your first family to go be on a reality show"

**Structure D: The Age/Time Callback**
- Reference specific era or timeline
- Connect to current reality
- Example: "I had such a crush on you when I was a little girl. If only I'd known that's when I had my best shot"

### Step 4: Test for Recognition & Intelligence

Ask yourself:
- **Recognition**: Will the target (and audience) see the truth in this?
- **Intelligence**: Does this reveal something insightful, not just mean?
- **Specificity**: Could this apply to anyone else? (If yes, revise)
- **Affection**: Is there humanity underneath the edge? (Best roasts feel like tough love)

**If answer is "no" to Recognition or Intelligence:** The roast is just mean. Revise.

### Step 5: Polish for Delivery

Refine the language:
- Conversational rhythm (sounds like you're saying it aloud)
- Strategic word choice (every word earns its place)
- Optional: Add softening ("I can't even believe..." before harsh joke)
- Optional: Add callback or double meaning

---

## Outputs

Returns roast jokes containing:
- **Hyper-specific observation**: Detail unique to the target
- **Recognizable truth**: Audience and target see accuracy
- **Intelligent insight**: Reveals something about perception, behavior, or contradiction
- **Delivery polish**: Conversational, quotable phrasing

**Output format options:**
- Single roast joke (one-liner)
- Set of 3-5 related roasts
- Roast paragraph (multiple connected jokes)

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Insufficient detail about target | Request more specific traits, behaviors, or public information |
| Target is vulnerable/protected group | Refuse; explain roasting punches up or sideways, not down |
| User wants "just mean" content | Refuse; explain roasts need truth and insight, not just cruelty |
| Target has no specific traits provided | Ask for observable details; explain generic traits produce generic roasts |
| Request violates ethics | Refuse specific request; offer consensual roast alternative |

---

## Examples

### Example 1: Friendly Roast (Playful Tone)

**Input:**
```
target: "My friend Jake who is obsessed with craft beer and won't shut up about it"
known_traits:
  - Talks about beer constantly
  - Uses terms like "hoppy notes" and "mouthfeel"
  - Takes photos of every beer
  - Works in IT
context: "friendly roast for his birthday"
tone: "playful"
```

**Output:**

"Jake has turned drinking into a full-time personality. This man will spend 20 minutes describing the 'hoppy notes' of an IPA like he's reviewing a Beethoven symphony, but he's in IT—the only notes you work with are in Jira tickets, my guy.

He's got more photos of beer glasses on his phone than photos of actual human beings. I've seen his camera roll. It's just 4,000 pictures of amber liquid with the caption 'This one had a really interesting mouthfeel.' Jake, that's what she said—but she wasn't talking about your beer knowledge.

I'm not saying Jake's obsessed, but he uses the word 'sessionable' in conversation and genuinely expects us to know what that means. The only thing that's 'sessionable' is this roast, and I'm just getting started."

---

### Example 2: Sharp Roast (Comedy Central Style)

**Input:**
```
target: "Fictional character: A tech CEO who claims to be 'disrupting' everything"
known_traits:
  - Says "disrupting" constantly
  - Wears black turtlenecks
  - Gives TED talks
  - Company barely turns a profit
context: "Comedy Central style roast"
tone: "sharp"
```

**Output:**

"You've disrupted everything except your company's path to profitability. You wear a black turtleneck like you're Steve Jobs, but you're more like Steve's Jobs—multiple failed attempts at being relevant.

You gave a TED talk about 'disrupting the disruption,' which is just a fancy way of saying you have no idea what your company actually does. Your business model is so disruptive it disrupted your own revenue stream.

I've seen your pitch deck. It's 47 slides of the word 'synergy' in different fonts. That's not disruption—that's just a cry for help with better graphic design."

---

### Example 3: Character Description (Brutal Precision)

**Input:**
```
target: "A coworker who micromanages everyone"
known_traits:
  - Sends emails at 11pm about minor details
  - Color-codes everything
  - Uses phrases like "circle back" and "touch base"
  - Has 7 different project management systems
tone: "brutal"
```

**Output:**

"This is someone who sends Slack messages at 11pm about semicolon placement and wonders why nobody invites them to happy hour. They've got seven different project management systems running simultaneously, which is just a fancy way of saying they don't trust any system—or any person.

They use the phrase 'let's circle back' so often they're basically just running in circles, which explains why nothing ever gets done. And they color-code everything. Not just spreadsheets—EVERYTHING. I've seen their lunch calendar. Tuesday is green because it's 'salad day.' I'm not making this up.

This person turns every conversation into a 'touch base,' which is corporate speak for 'I'm about to waste 30 minutes of your life you'll never get back.' They don't manage projects. They manage to make everyone around them contemplate new careers."

---

## Integration with nikki-glaser Expert

This skill operationalizes the nikki-glaser expert's "Roast Precision Strike" signature technique. When the nikki-glaser expert detects roast scenarios or requests for sharp character descriptions, this skill should be invoked automatically.

**Voice alignment:**
- Maintains Nikki Glaser's precision over pure shock value
- Uses hyper-specific observations
- Mixes affection with edge (tough love approach)
- Ensures jokes reveal truth, not just meanness

**When nikki-glaser expert should invoke this skill:**
- User asks to roast a person, character, or subject
- Character descriptions need comedic bite
- User requests "make fun of" or "roast" content
- Playful teasing scenarios where precision matters
- Comedy Central-style roast material needed