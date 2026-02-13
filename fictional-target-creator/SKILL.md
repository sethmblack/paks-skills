---
name: fictional-target-creator
description: Create fictional characters (like Phyllis Diller's "Fang") to critique institutions, relationships, or roles safely without attacking real people.
license: MIT
metadata:
  version: 1.0.964
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- absurdist
- callbacks
- comedy
- fictional-target-creator
- one-liners
- writing
---

# Fictional Target Creator

Create fictional characters (like Phyllis Diller's "Fang") to critique institutions, relationships, or roles safely without attacking real people.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Create fictional characters as thin disguises for specific real people (that's still attacking individuals)
- Build characters based on harmful stereotypes about groups
- Use "fictional" as excuse to say things that would be unethical about real people
- Create characters that mock people with disabilities, marginalized identities, or vulnerable populations
- Generate targets for punching down

**This skill is for:**
- Critiquing INSTITUTIONS (marriage, work, family structures)
- Exploring UNIVERSAL DYNAMICS in relationships
- Creating PERMISSION STRUCTURE for taboo topics
- Targeting ROLES and SYSTEMS, not individuals

**Ethical distinction:** "Fang" allowed Phyllis to roast marriage without insulting her actual husband. The character represents the INSTITUTION, not an individual.

---

## When to Use

**Trigger Conditions (use automatically when detected):**
- Need to critique institution (marriage, parenthood, workplace dynamics) but direct criticism would offend
- Want to roast relationship dynamics without attacking specific people
- Topic is taboo or sensitive, needs safe framework
- Real-world examples would be too personal or hurtful
- Need recurring character for ongoing comedy about a role/institution
- Want to explore "what everyone thinks but won't say" about a relationship type

**Examples of valid triggers:**
- Discussing marriage frustrations without insulting one's spouse
- Talking about difficult parents/in-laws without targeting actual relatives
- Exploring workplace dynamics without HR violations
- Addressing universal relationship tensions (romance, friendship, family)
- Creating comedy about "types" everyone recognizes

**Not valid for:**
- Thinly veiled attacks on specific people you're mad at
- Creating stereotyped characters to mock groups
- Bypassing ethics by claiming "it's fictional"

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `institution_or_role` | Yes | What are you critiquing (marriage, boss, parent, etc.) | Must be institution/role, not individual |
| `universal_tensions` | Yes | What do most people experience with this role | Must be widely relatable |
| `character_name` | No | Name for fictional character (defaults to generated) | Should be memorable, slightly absurd |
| `recurring_use` | No | Will this character appear repeatedly? (defaults to true) | Affects level of detail |
| `tone` | No | "affectionate roast" or "satirical critique" (defaults to "affectionate roast") | Balance of warmth vs. critique |

---

## Workflow

### Step 1: Identify the Institution/Role Being Critiqued

Define what you're actually criticizing (not WHO):

**Valid targets:**
- **Marriage** - The institution, expectations, daily dynamics
- **Parenthood** - The role, society's expectations, impossible standards
- **In-laws** - The relationship dynamic, boundary issues, cultural expectations
- **Bosses** - Workplace hierarchies, power dynamics, corporate culture
- **Neighbors** - Social obligations, boundary violations, community expectations
- **Aging parents** - Role reversal, care dynamics, generational differences

**Invalid targets:**
- "My husband John who never listens" → This is attacking John, not marriage
- "Asian mothers-in-law" → This is stereotyping a group
- "Karen from accounting" → This is targeting an individual

**Example:**
- Good: "The institution of marriage and its unrealistic expectations"
- Bad: "My specific spouse and their annoying habits"

### Step 2: Extract Universal Tensions

Identify what EVERYONE experiences with this institution/role (not just your personal grievance):

**Universal Tension Questions:**
- What does society say this role should be?
- What is it actually like?
- What does everyone think but not say?
- What's the gap between the myth and reality?
- What would people secretly admit about this if given permission?

**Example (Marriage):**
- Society myth: "Marriage is constant romance and companionship"
- Reality: "Marriage is negotiating who takes out the trash and pretending to listen to the same story for the 47th time"
- What everyone thinks: "Sometimes my spouse annoys me, and I feel guilty for feeling that way"
- The tension: Gap between "happily ever after" and "pass the remote"

### Step 3: Create Fictional Character That Embodies the Institution

Build a character that represents the ROLE, not a real person:

**Character Elements:**

**A. Name (memorable and slightly absurd)**
- Should signal "this is fictional"
- Hint at the role or characteristic
- Examples: "Fang" (spouse), "Moby Dick" (mother-in-law), "Mrs. Clean" (neighbor)

**B. Defining traits (universal, not personal)**
- Focus on traits EVERYONE would recognize in the role
- Make them slightly exaggerated but relatable
- Avoid traits that would only describe one specific person

**C. Consistent characteristics**
- 3-5 recurring traits/behaviors that audience can count on
- These become shorthand: just saying the name invokes the pattern

**D. Affection underneath (optional but recommended)**
- Even while roasting, signal this is affectionate
- "I keep him around for sentimental value"
- Separates institutional critique from genuine contempt

**Example: "Fang" (Phyllis Diller's husband character)**
- Name: "Fang" (signals bite, but also absurd/cartoonish)
- Traits: Lazy, clueless, always hungry, oblivious to household chaos
- Consistency: Always makes same mistakes, reliable target
- Affection: "I keep him around like the broken stove—sentimental value"

### Step 4: Build the Permission Structure

Establish rules for how the character can be used:

**Permission Signals:**
- **Introduce as fictional**: Make clear this isn't a real person
- **Exaggerate obviously**: Push traits beyond realism so audience knows it's performance
- **Apply universally**: Show this represents the ROLE, not one person
- **Balance with self-deprecation**: Roast yourself too

**Introduction Formula:**
```
"Let me tell you about [CHARACTER NAME], my [ROLE].
[CHARACTER NAME] [CHARACTERISTIC 1 - exaggerated].
[CHARACTER NAME] [CHARACTERISTIC 2 - more extreme].
Of course, [CHARACTER NAME] isn't real / is a composite / represents every [ROLE] everywhere."
```

**Example:**
"Let me tell you about Fang, my husband. Fang drops his pants to his ankles before going to the bathroom—doesn't realize he's supposed to take them off first. Fang thinks 'helping with housework' means watching me do it. Of course, Fang's been the same for forty years—which tells you everything about marriage, doesn't it?"

### Step 5: Create Recurring Material

Develop 5-10 jokes/scenarios about the character that reveal institutional tensions:

**Material Categories:**

**A. Defining moment** - Introduction that establishes character
"The first time I met Fang's mother, she brought a measuring tape. She was measuring me for a coffin—said she wanted to be prepared."

**B. Recurring behaviors** - Predictable patterns that become callbacks
"Every time I ask Fang to do something, he says 'I was just about to do that.' He's been 'just about to' fix the garage door for three years."

**C. Relationship dynamics** - How you interact
"Fang and I have been married forty years. That's a twenty-five-year sentence with fifteen off for good behavior."

**D. Universal truths revealed** - What the character exposes about the institution
"Living with Fang taught me that marriage is really about learning to ignore things. Big things. Like, does he actually breathe that loud, or did I just never notice?"

**E. Affectionate moments** - Signals this is roasting, not genuine contempt
"I give Fang a hard time, but he's been here forty years. That takes commitment. Or extremely poor planning on his part."

---

## Outputs

| Output | Format | Description |
|--------|--------|-------------|
| `character_profile` | Text | Name, role, defining traits |
| `introduction_script` | Text | How to introduce character first time |
| `sample_material` | List (5-10 jokes) | Jokes/scenarios about character |
| `usage_guidelines` | Text | When/how to invoke character |
| `institutional_critique` | Text | What this character reveals about the role/institution |

---

## Example

**Input:**
```
institution_or_role: "The modern workplace and 'that one coworker'"
universal_tensions: "Someone who creates extra work, takes credit, avoids responsibility, but is somehow never fired"
character_name: [generate]
recurring_use: true
tone: "satirical critique"
```

**Output:**

**Character Profile:**
- **Name**: "Chad from Synergy"
- **Role**: The coworker who embodies everything wrong with corporate culture
- **Defining Traits**:
  1. Uses business jargon to say nothing ("circle back", "move the needle", "synergy")
  2. Takes credit for others' work in meetings
  3. Never available when actual work needs doing
  4. Somehow always gets promoted
  5. Master of "strategic visibility" (looking busy without working)

**Introduction Script:**
"Let me tell you about Chad from Synergy. That's not his department—that's just how he refers to himself. 'Chad from Synergy.' Chad's never done actual work. He 'facilitates conversations.' He 'creates alignment.' Last week Chad sent a meeting invite titled 'Pre-Meeting for the Pre-Planning Meeting.' Three hours. No agenda. Just 'synergy.'

Chad takes credit for work like some people take breath mints—automatically and without thinking. You finish a project, Chad mentions it in one meeting, suddenly it's 'Chad's initiative.' Chad's office is positioned so he can see everyone working. That way he knows exactly what to take credit for.

And here's the thing—Chad keeps getting promoted. Because management thinks visibility equals productivity. Chad doesn't move the needle. Chad doesn't even know where the needle is. But Chad sure knows how to schedule a meeting about finding the needle."

**Sample Material:**
1. "Chad from Synergy sent an email: 'Let's take this offline for a deep dive and circle back with stakeholder alignment.' It was about whose turn to order coffee."

2. "Chad's resume says 'Dynamic Go-Getter.' What that means is he goes and gets other people to do his work."

3. "Last week Chad scheduled a meeting to discuss meeting culture. I suggested we cancel it. Chad said, 'Let's table that for the next meeting.'"

4. "Chad's favorite phrase is 'I'm slammed.' He is. With his own calendar invites."

5. "Chad from Synergy asked me to 'reach out and touch base about interfacing on deliverables.' I told him to send an email. He scheduled a meeting."

6. "Every company has a Chad from Synergy. If you don't know who yours is, it might be you."

7. "Chad works from home on Fridays. He also works from home on Thursdays. And Wednesdays. His definition of 'hybrid schedule' is 'mostly absent.'"

8. "I asked Chad for help on a project. He said, 'Let me connect you with the right resources.' The right resource was me. I'd connected myself."

9. "Chad's biggest accomplishment this year was 'optimizing workflow efficiency.' He automated his out-of-office message."

10. "I respect Chad's dedication. He's been not-working here for seven years."

**Usage Guidelines:**
- Invoke "Chad from Synergy" when discussing workplace dysfunction
- Use him to critique corporate jargon, credit-theft, performative busyness
- Character works for any industry ("Chad from Engineering", "Chad from Marketing")
- Balance criticism with absurdity—he's satirical, not a real person
- Can be modified to "Karen from Compliance" or other names for different institutional roles

**Institutional Critique:**
"Chad from Synergy" reveals how modern workplace culture values visibility over productivity, jargon over clarity, and meeting attendance over actual work. He embodies the dysfunction of systems that reward performance of work rather than work itself. By making Chad a character, you can critique these institutional problems without attacking specific coworkers or getting fired.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Character is thinly veiled attack on specific person | Reject. Redirect to identifying ROLE traits, not personal grievances |
| Character based on harmful stereotype | Reject. Must be based on universal institutional dynamics, not group characteristics |
| User wants to "get back at" someone through "fiction" | Reject. This skill is for institutional critique, not personal vengeance |
| Character traits are too specific/personal | Generalize. Multiple people should recognize this dynamic |
| No affection/humor, just contempt | Add balance. Show complexity or affection, or soften tone |

---

## Integration with Phyllis Diller Voice

**Phyllis's Fictional Characters:**
- **Fang** - Husband (marriage institution)
- **Mrs. Clean** - Neighbor (social expectations)
- **Moby Dick** - Mother-in-law (family dynamics)

**Phyllis-Specific Techniques:**
- Names are absurd/cartoonish (signals fiction)
- Traits are exaggerated to ridiculous degree
- Always callback to same characteristics for consistency
- Balance roasting with "I keep him around for sentimental value"
- Use in rapid-fire one-liner sequences

**Example in Phyllis voice:**
"Fang drops his pants to his ankles before he goes to the bathroom. He doesn't realize he's supposed to take them off first! *CACKLE!* The other night Fang said, 'What's for dinner?' I said, 'Reservations.' He said, 'I had that yesterday!' *CACKLE!* But I keep Fang around. He came with the house, kind of like the broken stove. Sentimental value!"

---

## Constraints

- **Must represent INSTITUTION/ROLE, not individual person**
- **Traits must be UNIVERSALLY RECOGNIZABLE, not personal grievances**
- **Exaggeration must be OBVIOUS (signals this is fiction/satire)**
- **Balance roasting with affection or humor** (not pure contempt)
- **Cannot be based on stereotypes of protected groups**
- **Must be reusable** (not one-off joke)

---

## Success Criteria

Fictional character is successful when:

- [ ] Name is memorable and signals "this is fiction"
- [ ] 3-5 defining traits that are universally recognizable in the role
- [ ] Traits are exaggerated enough to signal satire/performance
- [ ] Introduction script establishes character clearly
- [ ] 5-10 pieces of sample material demonstrate how to use character
- [ ] Character critiques institution/role, not specific individual
- [ ] Balance exists between roasting and affection/humor
- [ ] Multiple people could use this character in their own context
- [ ] Character becomes shorthand for institutional tensions

---

## Notes

**Why This Works:**

Creating fictional characters allows you to explore taboo topics and relationship tensions that would be too personal or hurtful if directed at real people. The key is making the character OBVIOUSLY FICTIONAL through:
1. Absurd names
2. Exaggerated traits
3. Universal rather than personal characteristics
4. Consistent patterns that become callbacks

**Phyllis Diller's Innovation:**

"Fang" allowed Phyllis to:
- Roast marriage without insulting her actual husband (divorced 1965, but character continued)
- Explore what "everyone thinks but won't say" about spousal dynamics
- Create recurring character audience looked forward to
- Critique the institution of marriage from the inside

The fictional target gave her permission to say things that would have been too personal/mean if directed at a real person.

**Modern Applications:**

- **Work**: "Chad from Synergy" or similar for workplace dysfunction
- **Parenting**: "SuperMom" for impossible parenting standards
- **Social media**: "The Influencer" for performance culture
- **Dating**: "Mr. Perfect" or "Red Flag Rita" for dating app culture
- **Family**: "Uncle Politics" for difficult family gatherings

The technique remains the same: create a character that embodies institutional problems, make them absurd enough to signal satire, and use them to give voice to universal frustrations.

**Comparison to Related Techniques:**

- **Archetypes** (Jung): Fictional targets are simplified archetypes for comedy
- **Strawman** (Logic): Different—strawman misrepresents arguments; fictional target represents real institutional dynamics accurately but through absurd character
- **Satire** (Literature): This IS satire, using character as vehicle
- **Roasting** (Comedy): Related, but fictional target protects real people from roast

**Legal/Ethical Note:**

If your "fictional" character is clearly recognizable as a specific person, you've failed. The character must represent the ROLE with traits many people in that role share, not one individual's unique characteristics. When done right, everyone thinks "Oh, I know someone like that" (not "Oh, that's obviously Bob").