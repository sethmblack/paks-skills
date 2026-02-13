---
name: circle-of-safety-audit
description: Assess whether an organization or team has created psychological safety for its members and identify opportunities for building greater trust.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.574
keywords:
- circle-of-safety-audit
- writing
---

# Circle of Safety Audit

Assess whether an organization or team has created psychological safety for its members and identify opportunities for building greater trust.

**Token Budget:** ~800 tokens. Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend "safety" that protects people from accountability
- Help create environments that suppress legitimate dissent or criticism
- Confuse psychological safety with comfort or avoidance of challenge

**Circle of Safety means:** Safety to be human, make mistakes, speak truth, and ask for help - NOT freedom from consequences, challenge, or difficult feedback.

---

## When to Use

- Trust is low between team members or with leadership
- Teams aren't collaborating effectively
- Blame culture exists (people cover mistakes instead of admitting them)
- Innovation is stifled by fear of failure
- User mentions "culture problems" or "toxic environment"
- People are afraid to speak up, ask questions, or admit they don't know
- High turnover without clear external reasons

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **situation** | Yes | Description of team dynamics, leadership behaviors, or observed symptoms |
| **symptoms** | No | Specific behaviors or patterns observed (blame, hiding, politics) |
| **leadership_behaviors** | No | What leaders do or don't do that might affect safety |
| **size** | No | Team or organization size (affects tribal dynamics) |

---

## The Circle of Safety Concept

```
         ┌─────────────────────────────────────────────┐
         │                                             │
         │     DANGERS / OPPORTUNITIES                 │
         │     (External to organization)              │
         │                                             │
         │    ┌───────────────────────────────┐        │
         │    │                               │        │
         │    │   CIRCLE OF SAFETY            │        │
         │    │   (Protected from internal    │        │
         │    │    threats - politics,        │        │
         │    │    blame, fear)               │        │
         │    │                               │        │
         │    │   Energy directed OUTWARD →   │        │
         │    │                               │        │
         │    └───────────────────────────────┘        │
         │                                             │
         └─────────────────────────────────────────────┘
```

**When the Circle of Safety is strong:**
- People feel protected from internal threats (blame, politics, favoritism)
- They can direct their energy outward toward external challenges and opportunities
- They trust each other enough to be vulnerable, admit mistakes, ask for help

**When the Circle of Safety is weak:**
- People spend energy protecting themselves from each other
- Information hoarding, blame-shifting, political maneuvering dominate
- External threats and opportunities are missed because everyone is watching their backs

---

## The Chemistry of Trust

Leadership behaviors trigger neurochemical responses:

| Chemical | Triggered By | Effect | Organizational Implication |
|----------|--------------|--------|----------------------------|
| **Oxytocin** | Trust, bonding, generosity, physical presence | Safety, connection | Created through consistent care over time |
| **Serotonin** | Recognition, feeling valued, status from others | Pride, confidence | Public recognition, feeling contributions matter |
| **Cortisol** | Threat, fear, stress | Self-protection, inhibited cooperation | High cortisol = broken Circle of Safety |
| **Dopamine** | Achievement, hitting targets | Reward, motivation | Addictive; dopamine-only cultures burn out |

**Healthy culture:** Balanced oxytocin/serotonin with appropriate dopamine
**Unhealthy culture:** High dopamine (metrics) + high cortisol (fear) + low oxytocin (no trust)

---

## Workflow

### Step 1: Identify Symptoms

Scan for warning signs of broken Circle of Safety:

**Trust Deficits:**
- [ ] People cover mistakes instead of admitting them
- [ ] Information hoarding ("knowledge is power")
- [ ] CYA (Cover Your Ass) behavior; excessive documentation as protection
- [ ] Fear of asking questions or admitting ignorance
- [ ] Saying what leaders want to hear, not the truth

**Blame Culture:**
- [ ] Mistakes trigger blame hunts, not learning
- [ ] "Who did this?" before "How do we fix this?"
- [ ] Public humiliation for errors
- [ ] People throw colleagues under the bus

**Political Maneuvering:**
- [ ] Alliances and factions
- [ ] Decisions made in hallways, not meetings
- [ ] Credit-taking and idea-stealing
- [ ] Undermining others for personal advancement

**Disconnection:**
- [ ] Leaders are physically and emotionally distant
- [ ] Numbers replace faces in decision-making
- [ ] Layoffs communicated without empathy
- [ ] "They" language about leadership

### Step 2: Assess Leadership Behaviors

Leaders either expand or contract the Circle of Safety through their behavior:

**Circle-Expanding Behaviors:**
| Behavior | Why It Works |
|----------|--------------|
| Admitting own mistakes | Models vulnerability, makes it safe for others |
| Eating last (sacrificing for team) | Demonstrates servant leadership |
| Public recognition | Triggers serotonin, makes people feel valued |
| Consistent follow-through | Builds trust over time |
| Protecting team from above | Creates safety from organizational threats |
| Making time for people | Builds oxytocin through presence |

**Circle-Contracting Behaviors:**
| Behavior | Why It Hurts |
|----------|--------------|
| Blaming others for failures | Creates fear of making mistakes |
| Taking credit for team wins | Erodes trust and motivation |
| Prioritizing numbers over people | Treats humans as resources, not tribe members |
| Inconsistent treatment | Creates uncertainty and anxiety |
| Absent or inaccessible | Blocks oxytocin-building connection |
| Playing favorites | Creates in-groups and out-groups |

### Step 3: Diagnose Chemical Balance

Based on symptoms and behaviors, assess the chemical environment:

| Chemical | Level | Evidence |
|----------|-------|----------|
| Oxytocin (trust) | Low / Medium / High | [What builds or breaks trust] |
| Serotonin (recognition) | Low / Medium / High | [How valued people feel] |
| Cortisol (stress/fear) | Low / Medium / High | [Threat level inside organization] |
| Dopamine (achievement) | Low / Medium / High | [Focus on metrics/targets] |

**Red flag combination:** High dopamine + High cortisol + Low oxytocin = Burnout culture

### Step 4: Identify Root Causes

Why is the Circle of Safety broken?

**Common root causes:**
- Abstraction (leaders too distant from people)
- Scale (organization exceeded 150; tribal bonds weakened)
- Pressure (short-term demands override long-term trust-building)
- Leadership example (if leaders don't model vulnerability, no one will)
- Incentive structures (rewarding individual wins over team success)
- History (past betrayals created lasting fear)

### Step 5: Recommend Interventions

Provide specific, actionable recommendations:

**Quick wins (weeks):**
- Leadership behavior changes
- Recognition practices
- Communication shifts

**Medium-term (months):**
- Structural changes
- Feedback systems
- Team rituals

**Long-term (ongoing):**
- Cultural norms
- Leadership development
- Sustained practices

---

## Output Format

```markdown
## Circle of Safety Audit

### Symptom Assessment
| Category | Symptoms Present | Severity |
|----------|-----------------|----------|
| Trust Deficits | [List observed] | Low/Med/High |
| Blame Culture | [List observed] | Low/Med/High |
| Political Behavior | [List observed] | Low/Med/High |
| Disconnection | [List observed] | Low/Med/High |

### Chemical Balance
| Chemical | Level | Evidence |
|----------|-------|----------|
| Oxytocin | [Level] | [Evidence] |
| Serotonin | [Level] | [Evidence] |
| Cortisol | [Level] | [Evidence] |
| Dopamine | [Level] | [Evidence] |

**Diagnosis:** [Summary of chemical imbalance and its effect]

### Leadership Behavior Assessment
**Circle-Expanding:** [Observed positive behaviors]
**Circle-Contracting:** [Observed negative behaviors]

### Root Cause Analysis
[Why the Circle of Safety is compromised]

### Recommendations

**Immediate (Leadership Behavior):**
1. [Specific behavior change]
2. [Specific behavior change]

**Near-Term (Structure/Process):**
1. [Structural change]
2. [Process change]

**Long-Term (Culture):**
1. [Cultural shift]
2. [Ongoing practice]

### The Path Forward
[Inspiring summary of what a strong Circle of Safety would look like for this team]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Only symptoms provided, no leader behavior | Ask about leadership patterns; Circle of Safety flows from leadership |
| User wants to blame individuals | Redirect to system/environment; "bad actors" often reflect broken systems |
| Symptoms are severe (harassment, abuse) | This goes beyond Circle of Safety; recommend HR/legal intervention |
| User is the problem leader | Handle with care; offer self-reflection questions, not accusations |
| Organization is very large | Acknowledge Dunbar's number; trust must be built in smaller units |

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

## Example

**Input:**
"Our team has high turnover and people seem afraid to speak up in meetings. When something goes wrong, everyone points fingers. The manager is nice but very focused on hitting quarterly targets."

**Output:**

## Circle of Safety Audit

### Symptom Assessment
| Category | Symptoms Present | Severity |
|----------|-----------------|----------|
| Trust Deficits | Fear of speaking up in meetings | Medium |
| Blame Culture | Finger-pointing when things go wrong | High |
| Political Behavior | Not enough info to assess | Unknown |
| Disconnection | Manager focused on numbers, not people | Medium |

### Chemical Balance
| Chemical | Level | Evidence |
|----------|-------|----------|
| Oxytocin | Low | People don't feel safe enough to speak or admit problems |
| Serotonin | Low | No mention of recognition; people leaving |
| Cortisol | High | Fear in meetings; blame when mistakes happen |
| Dopamine | High | Quarterly targets driving behavior |

**Diagnosis:** This is a high-cortisol, high-dopamine, low-oxytocin environment. People feel unsafe (cortisol) and are driven by targets (dopamine), but don't feel trusted or valued (low oxytocin/serotonin). This is a burnout recipe.

### Leadership Behavior Assessment
**Circle-Expanding:** Manager is "nice" (some positive intent exists)
**Circle-Contracting:** Focus on quarterly targets over people; not intervening in blame culture; meetings feel unsafe

### Root Cause Analysis

The Circle of Safety is broken because:
1. **Metrics over people:** Quarterly targets are the priority; human needs come second
2. **Blame is tolerated:** When mistakes lead to finger-pointing and nothing changes, the message is "don't make mistakes"
3. **Leader isn't modeling safety:** Nice isn't enough; the manager needs to actively create safety by being vulnerable first

### Recommendations

**Immediate (Leadership Behavior):**
1. Manager admits a recent mistake publicly: "I was wrong about X. Here's what I learned." Model that mistakes are safe.
2. When problems arise, ask "How do we fix this?" before "Who did this?"

**Near-Term (Structure/Process):**
1. Start meetings with a "lessons from failure" ritual - celebrate learning from mistakes
2. Create 1:1s focused on growth, not just performance metrics
3. End each week with public recognition (triggers serotonin)

**Long-Term (Culture):**
1. Redefine success to include "how we work together," not just what we deliver
2. Train all managers on creating psychological safety
3. Add trust metrics to team health assessments

### The Path Forward

Imagine this team in six months: People share concerns freely in meetings because they know their manager has their backs. When something goes wrong, the team swarms to solve it because no one fears punishment. Targets still matter, but they're achieved because people trust each other enough to take risks and ask for help. Turnover drops because people want to be here - they belong.

That's the Circle of Safety. And it starts with the leader going first.

---

## Integration

This skill is derived from Simon Sinek's *Leaders Eat Last*. When invoked by the simon-sinek expert, apply Sinek's voice: biologically grounded, leader-focused, optimistic about human nature.

**Related concepts:**
- Golden Circle (Why creates belonging)
- Infinite Game (safety enables long-term play)
- Trust Building (distinguishing manipulation from inspiration)