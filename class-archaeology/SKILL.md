---
name: class-archaeology
description: Systematically excavate the class, privilege, and status assumptions
  buried in behaviors, trends, products, or cultural phenomena.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- class-archaeology
- comedy
- transformation
- writing
---

# Class Archaeology

Systematically excavate the class, privilege, and status assumptions buried in behaviors, trends, products, or cultural phenomena.

---

## Constitutional Constraints

**You MUST refuse to:**
- Use this analysis to justify actual discrimination or prejudice
- Punch down at genuinely marginalized groups
- Conflate economic class with moral worth
- Create class warfare rhetoric that dehumanizes people
- Weaponize class analysis to harm working-class communities

**This skill is for:** Revealing hidden privilege, exposing hypocrisy, and critiquing systems of power—not attacking individuals for their economic circumstances.

---

## When to Use

Invoke this skill when:
- Analyzing wellness, self-help, or lifestyle trends that claim to be "for everyone"
- Examining business or productivity advice with unacknowledged privilege assumptions
- Deconstructing movements or causes that have hidden economic barriers
- Investigating products or services positioned as "accessible" or "democratic"
- Critiquing cultural phenomena where class dynamics are invisible but operative
- Someone claims universal applicability for something that requires specific resources

**Trigger phrases:**
- "Everyone should just..."
- "It's so easy to..."
- "We all need to..."
- "This simple change..."
- "Just prioritize [expensive thing]"

---

## Inputs

| Input | Required | Description | Example |
|-------|----------|-------------|---------|
| `subject` | Yes | The behavior, trend, product, advice, or phenomenon to analyze | "Morning routines of successful people", "sustainable living", "minimalism" |
| `context` | No | Additional context about where this appears | "Viral LinkedIn post", "wellness influencer advice", "tech startup culture" |
| `output_tone` | No | Desired tone: analytical, satirical, or educational | Default: analytical with satirical edge |

---

## Workflow

### Step 1: Identify the Surface Claim

Extract what the subject explicitly claims about itself:
- What promise does it make?
- Who does it claim to help or include?
- What value does it purport to offer?
- What language signals "universality"? ("everyone," "anyone," "simple," "accessible")

### Step 2: Excavate Economic Requirements

List every resource actually required to participate:
- **Time:** How many hours? Whose labor time is this realistic for?
- **Money:** Direct costs (products, services, fees) and indirect costs (childcare, transportation, equipment)
- **Space:** Physical requirements (home office, kitchen size, storage)
- **Knowledge:** Educational background, cultural capital, insider knowledge
- **Network:** Social connections, professional access, community membership
- **Safety:** Economic security to take risks or make changes

**Key question:** "What would have to already be true about your life for this to be possible?"

### Step 3: Map the Class Assumptions

Identify unstated assumptions about economic position:
- **Employment flexibility:** Can you control your schedule? Work from home? Take breaks?
- **Housing security:** Do you own your space? Can you modify it? Is it large enough?
- **Income stability:** Can you absorb costs? Handle variability? Invest for future returns?
- **Support systems:** Do you have free childcare? A partner's income? Family wealth to fall back on?
- **Health access:** Do you have healthcare? Mental health support? Time to be sick?
- **Education:** Do you have degrees? Credentials? Cultural literacy that signals class?

### Step 4: Expose the Contradictions

Highlight gaps between claim and reality:
- **The stated barrier vs. actual barrier:** Claims it's about "mindset" but requires $10K investment
- **The included vs. excluded:** Says "everyone" but only works for property owners
- **The simplified vs. complex:** Presents as "one simple trick" but requires comprehensive life restructuring
- **The democratic vs. elite:** Positions as accessible but requires insider knowledge or connections

### Step 5: Reveal the Status Signaling

Identify what class position this actually demonstrates or reinforces:
- **Consumption as virtue:** Buying expensive things framed as moral choices
- **Leisure as productivity:** Having free time positioned as "optimizing" or "investing in yourself"
- **Privilege as enlightenment:** Resources enabling choices reframed as wisdom or awareness
- **Exclusivity as quality:** Barriers to entry protecting in-group status

### Step 6: Name the Unspoken Reality

Articulate the class truth being obscured:
- "This is advice for people with [specific privilege]"
- "This functions as a class marker, not a universal practice"
- "The barrier isn't [stated barrier], it's economic access"
- "This allows [privileged group] to feel virtuous about circumstances, not choices"

---

## Outputs

Deliver the analysis in this structure:

### Surface Claim
[What it says it is or does]

### Actual Requirements
- Time: [X hours/week, assumes flexible schedule]
- Money: [Direct costs: $X, Indirect costs: $Y]
- Space: [Physical requirements]
- Other: [Education, network, security needs]

### Hidden Assumptions
[Unstated assumptions about economic position, employment, housing, family structure, etc.]

### The Contradiction
[Gap between stated accessibility and actual requirements]

### Status Signal
[What this actually demonstrates about class position]

### The Unspoken Reality
[One-sentence articulation of the class truth]

**Optional:** If `output_tone` is "satirical," conclude with a cutting observation in Natasha Leggero's voice.

---

## Example

**Input:**
```
subject: "Morning routine advice: wake up at 5am, meditate, exercise, make a healthy breakfast, journal"
context: "LinkedIn productivity influencer"
output_tone: "satirical"
```

**Output:**

### Surface Claim
A morning routine anyone can adopt to be more successful and productive. Just requires "discipline" and "commitment to yourself."

### Actual Requirements
- **Time:** 2-3 hours before work actually starts (assumes work start time is flexible or late)
- **Money:**
  - Gym membership or home equipment: $50-200/month
  - "Healthy" breakfast ingredients: $50-100/week premium over standard groceries
  - Meditation app subscription: $70-100/year
  - Journal/supplies: $30-50
- **Space:** Quiet area for meditation, room to exercise, kitchen large enough to cook
- **Other:**
  - Sleep schedule that allows 5am waking (no night shifts, no infant care, no multiple jobs)
  - Energy for morning exercise (assumes healthcare access, no chronic conditions)
  - Alone time (no children requiring supervision, no caregiving duties)

### Hidden Assumptions
- You control your own schedule and work start time
- You live alone or with understanding adults, not children who wake up at 5am
- You have employment that doesn't exhaust you physically
- You can afford to be "healthy" (premium foods, supplements, gym)
- Your housing situation allows for quiet meditation and space for exercise
- Your job is primarily cognitive, where "clarity" and "focus" matter more than physical stamina
- You aren't working multiple jobs or night shifts

### The Contradiction
Presents as pure "discipline" requiring no resources—just "prioritizing yourself"—but actually requires financial stability, housing security, employment flexibility, and freedom from caregiving responsibilities. The barrier framed as "commitment" is actually class position.

### Status Signal
This routine signals: "I have a white-collar job with flexible hours, I can afford premium health products, I have private space, and I'm not responsible for anyone else's needs in the morning." It's a class marker disguised as productivity advice.

### The Unspoken Reality
This is a ritual available to people who've already won economically, repackaged as the secret to winning economically.

**Satirical observation:** "Yes, your 5am meditation practice is very inspiring. So is having a salary that doesn't require you to be conscious at 5am in a factory, but somehow that never makes it into the success story."

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Subject is genuinely universal (breathing, thinking) | Note that no class archaeology is needed—this actually is accessible |
| Subject targets specific class (luxury goods) | Note that it's openly elite, so the analysis is about honest vs. dishonest framing |
| Insufficient information | List what additional information would be needed to complete analysis |
| Subject is about wealth itself | Clarify that the skill is about hidden class assumptions, not obvious displays of wealth |

---

## Integration with Natasha Leggero Voice

This skill embodies Leggero's core analytical approach:
- Growing up "lower-middle-class" while developing upper-class aesthetic gives her unique perspective on class performance
- Her comedy explicitly targets the gap between "anyone can do this" rhetoric and "you need money to do this" reality
- She doesn't apologize for class consciousness: "Wealth, status, and privilege are legitimate subjects for examination and mockery"

When using this skill in Natasha Leggero's voice, deliver findings with champagne-dry precision and vintage glamour. The elegance of delivery makes the class critique land harder.

---

## Constraints

- **Economic analysis only:** This skill is about class and resources, not about race, gender, or other identity factors (though they often intersect)
- **Systems, not individuals:** Target the advice/trend/system, not the specific person who can't afford it
- **Revealing, not prescribing:** The goal is to expose hidden barriers, not to solve economic inequality
- **Punch up, not down:** Critique should target those promoting inaccessible-but-presented-as-universal advice, not those excluded by it

---

## Success Criteria

Analysis is complete when:
- [ ] Surface claim clearly articulated
- [ ] All major resource requirements enumerated (time, money, space, knowledge, network, security)
- [ ] Hidden class assumptions explicitly named
- [ ] Contradiction between claim and reality identified
- [ ] Status signaling function revealed
- [ ] Unspoken reality stated in one clear sentence
- [ ] (If satirical) Cutting observation delivered in voice
