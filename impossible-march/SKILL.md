---
name: impossible-march
description: When competitors or obstacles guard all conventional paths, find the route they consider impossible—the one that is harder but undefended.
license: MIT
metadata:
  version: 1.0.4215
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- the-impossible-march
- writing
---

# The Impossible March

When competitors or obstacles guard all conventional paths, find the route they consider impossible—the one that is harder but undefended.

**Source Expert:** Simon Bolivar
**Category:** Strategy / Competitive Positioning

---

## When to Use

- Every obvious market approach is dominated by stronger players
- Conventional wisdom says your goal is impossible
- Competitors have all the easy paths locked up
- You need an asymmetric advantage against a stronger opponent
- The "reasonable" timeline would result in failure

**Trigger Phrases:**
- "All the obvious paths are blocked"
- "We can't compete on their terms"
- "Every approach has been tried"
- "The market is locked up"
- "How do we get around them?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `objective` | Yes | What you're trying to achieve |
| `blocked_paths` | Yes | The conventional approaches that don't work |
| `adversary` | Yes | Who/what is blocking you |
| `resources` | No | What you have available |
| `constraints` | No | Limits on what you can do |

---

## Workflow
### Step 1: The Crossing of the Andes (1819)

Bolivar needed to reach Bogota. The Spanish guarded the frontier heavily—on all the routes they expected him to use. But they considered the Andes impassable during winter.

Bolivar's choice:
- Cross the flooded plains (36 days, waist-deep in water)
- Then the Pisba Pass (13,000 feet, icy winds, unclothed troops)
- Lose one-third of his army to cold, starvation, altitude sickness
- Lose all horses to hypothermia

The result: He arrived where there was no defense. Three months later, Colombia was free.

### Step 2: Framework

**1. Map the Blocked Paths**

What routes have you tried or considered?

| Path | Who Blocks It | Their Advantage |
|------|---------------|-----------------|
| [approach] | [competitor/obstacle] | [why they win here] |

**2. Find the "Impossible" Routes**

What approaches does conventional wisdom dismiss?
- "That would take too long"
- "That's too expensive"
- "No one has ever done that"
- "That technology doesn't exist"
- "The conditions are too harsh"

List every dismissed path. These are candidates.

**3. Assess True vs. Assumed Impossibility**

For each "impossible" route:
- Is it physically impossible or just very hard?
- Is it economically impossible or just expensive?
- Has it been tried and failed, or just assumed to fail?
- What would it actually require?
- Why do competitors not take this path?

**4. Calculate the Real Cost**

If you take the impossible path:
- What will you lose? (Bolivar lost one-third of his army)
- What will you preserve that the conventional path would destroy?
- What will you gain that the conventional path cannot provide?
- Is the cost survivable?

**5. Prepare for the March**

The impossible path requires preparation others don't need:
- What capabilities must you build?
- What hardships must your team endure?
- What supplies must you stockpile?
- What commitments must people make?
- How do you prevent desertion when the march gets hard?

**6. Execute with Speed**

Once committed, move fast:
- The impossible path's advantage is surprise
- Hesitation allows competitors to respond
- Suffering is finite if you move quickly
- Arrive before they believe you can

---

## Output Format

```markdown
## Blocked Path Analysis

| Conventional Path | Who Blocks It | Why We Lose |
|-------------------|---------------|-------------|
| [path] | [adversary] | [their advantage] |

## Impossible Path Candidates

| Dismissed Approach | Why Dismissed | True Difficulty |
|--------------------|---------------|-----------------|
| [approach] | [conventional reason] | [actual assessment] |

## Selected Path: [Name]

**Why This Path:**
- [Reason it's undefended]
- [Reason it's actually possible]
- [What we gain by taking it]

## Cost Analysis

| Loss | Survivable? | Worth It? |
|------|-------------|-----------|
| [what you'll lose] | [Yes/No] | [assessment] |

**Total Cost:** [Summary]
**Alternative Cost:** [What conventional path would cost]

## March Preparation

**Capabilities to Build:**
1. [capability]
2. [capability]

**Hardships to Prepare For:**
1. [hardship]
2. [hardship]

**Team Commitments Required:**
- [what people must agree to]

**Desertion Prevention:**
- [how you keep people committed when it gets hard]

## Execution Timeline

| Phase | Action | Duration | Key Risk |
|-------|--------|----------|----------|
| [phase] | [action] | [time] | [risk] |

## Arrival State

**Where We End Up:** [Position after the march]
**Enemy State:** [Their position/awareness]
**Next Move:** [What becomes possible]
```

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
- Objective: Launch AI-powered legal document review competing with Thomson Reuters and LexisNexis
- Blocked paths: Enterprise sales (they have relationships), brand recognition (they have decades), feature completeness (they have everything)
- Adversary: Established legal tech giants

**Output:**

## Blocked Path Analysis

| Conventional Path | Who Blocks It | Why We Lose |
|-------------------|---------------|-------------|
| Enterprise sales to AmLaw 100 | Thomson Reuters, LexisNexis | 20-year relationships, bundled contracts, switching costs |
| Feature completeness | Incumbents | They have 30 years of features; we have months |
| Brand awareness | Established players | No general counsel will risk career on unknown vendor |

## Impossible Path Candidates

| Dismissed Approach | Why Dismissed | True Difficulty |
|--------------------|---------------|-----------------|
| Solo practitioners | "No money, too fragmented" | Actually: huge market, zero incumbent focus, modern expectations |
| Legal aid / pro bono | "Can't monetize non-profits" | Actually: grants available, social mission creates loyalty, law school partnerships |
| International emerging markets | "Different legal systems, too hard" | Actually: less incumbent entrenchment, mobile-first opportunity |
| Vertical specialization (immigration only) | "Too narrow to build a business" | Actually: massive volume, underserved, emotional stakes drive adoption |

## Selected Path: Immigration Law Vertical

**Why This Path:**
- Giants consider it low-margin, ignore it
- Massive volume: millions of cases, highly repetitive documents
- Underserved: solo practitioners and small firms, tech-disadvantaged
- Emotional stakes: clients will push lawyers to use better tools
- Community: tight-knit bar association, word spreads fast

## Cost Analysis

| Loss | Survivable? | Worth It? |
|------|-------------|-----------|
| Credibility with BigLaw initially | Yes | Build it later with immigration success |
| "AI for all law" positioning | Yes | Can expand after beachhead |
| Revenue ceiling initially | Yes | Immigration is bigger than it looks |
| 6 months building domain expertise | Yes | Creates moat competitors can't quickly cross |

**Total Cost:** 12-18 months focused on "small" market; forego enterprise credibility initially
**Alternative Cost:** 3 years and $20M trying to compete with Thomson Reuters; probable failure

## March Preparation

**Capabilities to Build:**
1. Immigration law domain expertise (hire 2 immigration attorneys)
2. Integration with immigration-specific case management (CLIO, Docketwise)
3. Spanish/multilingual support (client-facing materials)

**Hardships to Prepare For:**
1. Team frustration ("why aren't we going after the big market?")
2. Investor skepticism ("immigration is too small")
3. Slower initial revenue than enterprise deals would provide

**Team Commitments Required:**
- 18-month focus on immigration vertical—no distractions
- Willingness to travel to immigration law conferences (often in less glamorous locations)
- Learning immigration law deeply, not just applying generic AI

**Desertion Prevention:**
- Make the mission explicit: "We're helping people stay with their families"
- Celebrate immigration wins visibly
- Show the expansion roadmap once beachhead is established

## Execution Timeline

| Phase | Action | Duration | Key Risk |
|-------|--------|----------|----------|
| Domain immersion | Hire attorneys, attend conferences, learn the practice | Months 1-3 | Underestimating complexity |
| MVP for immigration | Build immigration-specific document review | Months 4-8 | Feature creep toward generic |
| Beachhead sales | 50 immigration firms using product | Months 9-14 | Pricing too high for solo practitioners |
| Expansion preparation | Document playbook, prepare for adjacent verticals | Months 15-18 | Premature expansion |

## Arrival State

**Where We End Up:** Dominant AI tool for immigration law document review, 200+ firms, strong word-of-mouth, case studies, revenue
**Enemy State:** Unaware or dismissive ("they're just doing immigration")
**Next Move:** Expand to adjacent verticals (family law, personal injury) using same playbook; approach enterprise from position of proven success rather than pitch deck

---

## Anti-Patterns

**DON'T:**
- Choose the impossible path because it's dramatic (only choose it if conventional paths truly don't work)
- Underestimate the cost (Bolivar lost a third of his army—know what you'll lose)
- Tell the army the full plan before they're committed (they may desert if they know how hard it will be)
- Hesitate once you start (speed is part of the advantage)
- Confuse "hard" with "impossible" in either direction

**The Test:** Are you choosing this path because it's actually better, or because you're romanticizing difficulty?

---

## Integration

This skill pairs with:
- **Speed and Audacity:** Execute the march with urgency
- **Lead from the Front:** The impossible march requires visible leadership commitment
- **Resilience Through Defeat:** If the march fails, extract the lessons
- **Revolutionary Rhetoric:** Inspiring the team to attempt what seems impossible