---
name: third-place-design
description: Design physical and digital spaces that create emotional belonging between
  home and work contexts, based on Howard Schultz's methodology for transforming Starbucks
  into community anchors.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- third-place-design
- transformation
- writing
---

# Third Place Design

Design physical and digital spaces that create emotional belonging between home and work contexts, based on Howard Schultz's methodology for transforming Starbucks into community anchors.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for design output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Design spaces that exclude or discriminate against groups
- Create environments that manipulate or deceive users
- Recommend surveillance disguised as personalization
- Design addiction-inducing patterns that harm users

**If asked to design a harmful space:** Refuse explicitly. Third places are about genuine belonging, not manipulation.

---

## When to Use

- User asks to design a customer space or environment
- Request mentions "community," "belonging," or "third place"
- Evaluating retail, hospitality, or service environments
- Transforming transaction-focused spaces into experience-focused ones
- Digital community or platform experience design

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **space_description** | Yes | Current or planned space (physical or digital) |
| **target_audience** | Yes | Who should feel they belong here |
| **brand_values** | No | Core values the space should embody |
| **pain_points** | No | Current experience problems to solve |

---

## The Third Place Framework

### Origin

Sociologist Ray Oldenburg (1989) defined the "third place" as spaces beyond home (first place) and work (second place) where community happens. Howard Schultz transformed this into a design methodology.

### Schultz's Definition

"I've never thought of the third place just as a physical environment. For me, the third place has always been a feeling. An emotion. An aspiration that all people can come together and be uplifted as a result of a sense of belonging."

---

## Workflow
### Step 1: 1. Assess Current State

Evaluate the space against the seven third place elements:

| Element | Question | Physical Implementation | Digital Implementation |
|---------|----------|------------------------|----------------------|
| **Comfort Seating** | Does the space invite lingering? | Varied seating (couches, chairs, communal tables) | Comfortable UI, no time pressure |
| **Sensory Anchor** | Is there a signature sensory experience? | Aroma, temperature, texture | Sound design, visual warmth |
| **Curated Atmosphere** | Does the environment tell a story? | Music, art, lighting choices | Theme, voice, personality |
| **Warm Lighting** | Does lighting feel welcoming? | Natural light, warm tones | Color palette, contrast |
| **Personal Recognition** | Are people known and acknowledged? | Staff greet by name | Personalization, history |
| **Staying Infrastructure** | Can people stay comfortably? | Power outlets, WiFi, tables | Save state, notifications |
| **Ritual Creation** | Are there repeatable meaningful moments? | Order customization, loyalty program | Habits, rewards, traditions |

Score each element 1-5:
- **5**: Exceptional - creates delight and differentiation
- **4**: Strong - clearly intentional and effective
- **3**: Adequate - present but not memorable
- **2**: Weak - exists but feels like afterthought
- **1**: Missing - not present or actively negative

### Step 2: 2. Identify Belonging Barriers

Look for elements that prevent belonging:
- Transactional pressure (speed over connection)
- Exclusionary design (who doesn't feel welcome?)
- Sterile or generic environments
- Missing personal recognition
- No staying infrastructure
- Forced efficiency over comfort

### Step 3: 3. Design for Belonging

For each weak element, create specific improvements:

**Comfort:** What invites people to stay?
**Recognition:** How are people acknowledged as individuals?
**Ritual:** What repeatable moments create meaning?
**Community:** How do strangers connect?
**Sensory:** What makes this place feel like THIS place?

### Step 4: 4. Test the Third Place Promise

Apply Schultz's test: "At home, you're part of a family. At work you're part of a company. And somewhere in between there's a place where you can sit back and be yourself."

Ask: Can people BE THEMSELVES here? What prevents it?

---

## Outputs

### Third Place Design Report

```markdown
## Third Place Assessment: [Space Name]

### Current State Scores

| Element | Score | Notes |
|---------|-------|-------|
| Comfort Seating | X/5 | [observation] |
| Sensory Anchor | X/5 | [observation] |
| Curated Atmosphere | X/5 | [observation] |
| Warm Lighting | X/5 | [observation] |
| Personal Recognition | X/5 | [observation] |
| Staying Infrastructure | X/5 | [observation] |
| Ritual Creation | X/5 | [observation] |

**Overall Third Place Score: XX/35**

### Belonging Barriers Identified

1. [Barrier] - [How it prevents belonging]
2. [Barrier] - [How it prevents belonging]

### Design Recommendations

#### Priority 1: [Most impactful change]
- Current state: [what exists now]
- Recommendation: [specific change]
- Expected impact: [how this creates belonging]

#### Priority 2: [Second priority]
...

### The Third Place Promise Test

Can people be themselves here?
- YES because: [supporting elements]
- NOT YET because: [remaining barriers]

### Implementation Sequence

1. [Quick win - immediate impact]
2. [Foundation - enables other changes]
3. [Differentiation - creates unique belonging]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Space is purely transactional by design | Acknowledge limitation, suggest hybrid zones |
| Digital-only space | Apply framework with digital equivalents |
| Budget constraints | Prioritize high-impact, low-cost elements first |
| Brand conflicts with belonging | Flag tension, suggest brand evolution |

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
```
space_description: "Fast-casual restaurant with counter ordering, basic seating, focus on lunch rush"
target_audience: "Urban professionals seeking quick, quality lunch"
pain_points: "Customers eat quickly and leave, no repeat recognition, feels generic"
```

**Output:**

## Third Place Assessment: Fast-Casual Restaurant

### Current State Scores

| Element | Score | Notes |
|---------|-------|-------|
| Comfort Seating | 2/5 | Basic functional chairs, no variety |
| Sensory Anchor | 3/5 | Good food aroma, generic background music |
| Curated Atmosphere | 2/5 | Standard restaurant lighting and decor |
| Warm Lighting | 2/5 | Bright overhead, no warmth zones |
| Personal Recognition | 1/5 | No names, no history, each visit starts fresh |
| Staying Infrastructure | 1/5 | No outlets, no WiFi, tables small |
| Ritual Creation | 2/5 | Ordering is efficient but not memorable |

**Overall Third Place Score: 13/35** (Transaction-focused, not experience-focused)

### Belonging Barriers Identified

1. **Speed-first design** - Everything signals "eat and leave"
2. **Anonymity** - Regulars treated same as first-timers
3. **No staying zones** - Physical setup discourages lingering

### Design Recommendations

#### Priority 1: Recognition System
- Current: Each customer is anonymous
- Recommendation: Loyalty program that stores name, favorites, visit history. Train staff to greet regulars by name.
- Expected impact: Transforms from "restaurant" to "my place"

#### Priority 2: Zoned Seating
- Current: Uniform fast-turnover seating
- Recommendation: Create 3 zones - quick counter seating (grab-and-go), standard tables (lunch meetings), comfortable corner (work and linger)
- Expected impact: Serves both efficiency seekers AND belonging seekers

#### Priority 3: Signature Sensory
- Current: Generic background
- Recommendation: Distinctive playlist that becomes "the sound of this place," visible food prep adds theater
- Expected impact: Memorable sensory identity

### The Third Place Promise Test

Can people be themselves here?
- NOT YET because: Current design treats all visits as transactions
- COULD BE because: Food quality foundation exists, needs experience layer

### Implementation Sequence

1. Staff recognition training (free, immediate)
2. Loyalty app with personalization (weeks)
3. Seating zone redesign (months)

---

## Integration

This skill is part of the **Howard Schultz** expert methodology. It pairs with:
- `experience-economy-audit` - to understand where experience adds value
- `partner-investment-analysis` - staff enabling recognition and connection
- `authenticity-brand-test` - ensuring third place design matches brand truth