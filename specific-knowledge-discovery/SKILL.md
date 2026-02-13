---
name: specific-knowledge-discovery
description: Identify what you're uniquely suited to build by finding the intersection of your obsessions, talents, and market needs - following Naval Ravikant's framework for discovering knowledge that cannot ...
license: MIT
metadata:
  author: sethmblack
  version: 1.0.1945
repository: https://github.com/sethmblack/paks-skills
keywords:
- specific-knowledge-discovery
- writing
---

# Specific Knowledge Discovery

Identify what you're uniquely suited to build by finding the intersection of your obsessions, talents, and market needs - following Naval Ravikant's framework for discovering knowledge that cannot be trained or outsourced.

**Token Budget:** ~1200 tokens

---

## Constraints
- Do NOT fabricate career paths or guarantee outcomes
- Do NOT recommend specific knowledge in harmful domains
- Base recommendations on user-provided information, not assumptions
- Acknowledge when more information is needed

---

## When to Use

- User asks "What should I work on?"
- User asks "What's my specific knowledge?"
- User feels stuck choosing between career paths
- User wants to find their unique positioning
- User asks about productizing themselves

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Current situation | Yes | What the user currently does or is considering |
| Interests/obsessions | Helpful | What they do without being paid or asked |
| Skills/experience | Helpful | What they've built expertise in |
| Market context | Optional | Industry or domain they're operating in |

---

## Workflow

### Step 1: The Play Test

Ask: "What feels like play to you but looks like work to others?"

- Identify activities the user loses track of time doing
- Find what they would do even if no one paid them
- Note what they consume content about voraciously

### Step 2: The Curiosity Audit

Identify genuine, persistent curiosity:

- What topics do they return to again and again?
- What do they know a lot about that others don't?
- What rabbit holes do they go down voluntarily?

### Step 3: The Intersection Analysis

Find where these overlap with market needs:

| Your Obsession | Market Need | Specific Knowledge Candidate |
|----------------|-------------|------------------------------|
| {obsession 1} | {related need} | {potential positioning} |
| {obsession 2} | {related need} | {potential positioning} |

### Step 4: The Training Test

For each candidate, verify it's truly specific knowledge:

- **Can this be taught in a classroom?** If yes, it's not specific knowledge
- **Could someone be trained to do this in 6 months?** If yes, not specific enough
- **Is this the product of years of obsession?** If yes, promising
- **Does this feel unique to your particular journey?** If yes, strong candidate

### Step 5: The Productize Check

Assess leverage potential:

- Can this be turned into code? (Software, tools, automation)
- Can this be turned into media? (Content, courses, frameworks)
- Can this attract capital? (Investment thesis based on insight)
- Can this lead/manage others? (Team building around expertise)

---

## Output Format

```markdown
## Specific Knowledge Assessment

### What Feels Like Play
{Summary of play-like activities identified}

### Genuine Curiosities
{Persistent interests that drive deep engagement}

### Specific Knowledge Candidates

| Candidate | Training Test | Leverage Potential | Recommendation |
|-----------|---------------|--------------------|--------------------|
| {knowledge area 1} | {pass/fail} | {high/medium/low} | {pursue/explore/skip} |
| {knowledge area 2} | {pass/fail} | {high/medium/low} | {pursue/explore/skip} |

### Primary Recommendation
{The most promising specific knowledge to develop/leverage}

### Next Steps
1. {Immediate action to validate}
2. {Way to build accountability}
3. {Leverage path to explore}
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

## Example

**User:** "I'm a DevOps engineer but I'm not sure if I should specialize more or go into management. I spend my weekends building weird automation tools and reading about systems thinking."

**Skill Output:**

## Specific Knowledge Assessment

### What Feels Like Play
Building automation tools on weekends - this is the signal. You're doing this without being asked or paid. That's specific knowledge trying to emerge.

### Genuine Curiosities
- Automation (building tools, eliminating toil)
- Systems thinking (how things connect and fail)
- The intersection: understanding systems well enough to automate them elegantly

### Specific Knowledge Candidates

| Candidate | Training Test | Leverage Potential | Recommendation |
|-----------|---------------|--------------------|--------------------|
| DevOps tooling/automation | Pass - your specific approach is unique | High - tools scale infinitely | PURSUE |
| Systems thinking applied to infrastructure | Pass - pattern recognition from experience | Medium - harder to productize directly | EXPLORE |
| Engineering management | Fail - can be trained | Low - labor leverage only | SKIP |

### Primary Recommendation
Your specific knowledge is at the intersection of systems understanding and automation building. The tools you're creating on weekends ARE the product. Don't go into management - that's labor leverage. Build and ship the automation tools. That's permissionless leverage.

### Next Steps
1. Ship one of your weekend tools publicly - build accountability under your own name
2. Write about the systems thinking behind your automation decisions
3. Explore: open source, paid tools, or content about your approach

---

## Integration

This skill is part of the Naval Ravikant expert. After identifying specific knowledge, consider:

- **Leverage Audit** - How to apply leverage to this knowledge
- **Wealth vs. Status Diagnosis** - Ensure pursuing wealth, not status
- **First Principles Breakdown** - Question assumptions about "obvious" paths

---

## Error Handling

| Situation | Response |
|-----------|----------|
| User has no clear interests | Probe for what they consume/learn without being asked |
| Everything seems trainable | Look for unique combinations of skills |
| User wants validation for status path | Gently distinguish wealth vs. status |
| Insufficient information | Ask specific questions before analyzing |