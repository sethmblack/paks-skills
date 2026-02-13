---
name: convention-challenge
description: Systematically identify and dismantle "we've always done it this way" thinking by exposing assumptions, questioning their validity, and demonstrating alternatives.
license: MIT
metadata:
  version: 1.0.3685
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- convention-challenge
- structure
- writing
---

# Convention Challenge

Systematically identify and dismantle "we've always done it this way" thinking by exposing assumptions, questioning their validity, and demonstrating alternatives.

---

## When to Use

- Encountering "we've always done it this way" as justification
- Facing organizational inertia blocking beneficial change
- Questioning inherited practices or traditions
- Breaking through resistance rooted in precedent rather than reason
- User asks "Why do we do it this way?" or challenges seem impossible
- When fear of change masquerades as prudence

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| convention | Yes | The practice, process, or belief being defended |
| stated_justification | No | What people say when asked why |
| context | No | Organizational or domain context |
| desired_change | No | What the user wants to do instead |

---

## The Convention Challenge Framework

Grace Hopper called "We've always done it this way" the most dangerous phrase in any language. She kept a clock on her wall that ran counterclockwise just to make the point that conventions are arbitrary.

"Humans are allergic to change. They love to say, 'We've always done it this way.' I try to fight that."

**The insight:** Most conventions were solutions to problems that may no longer exist. Precedent is not justification. The burden of proof should be on the convention, not the challenger.

### Step 1: Name the Convention Explicitly

Surface the unexamined assumption:
- What is the actual practice, process, or belief?
- How long has it been done this way?
- Who originally decided this?
- What was the original reason?

**Key move:** Force specificity. "We've always done it this way" becomes "We've been using this process since 2015 because Tom in accounting preferred it."

### Step 2: Trace the Original Reason

Investigate the convention's origin:
- What problem was this originally solving?
- What constraints existed when this was decided?
- Who made the decision and why?
- What alternatives were considered and rejected?

**Common findings:**
- The original reason no longer applies (constraints changed)
- Nobody remembers the original reason (ritual without meaning)
- The reason was a personal preference, not a requirement
- The alternative that was rejected is now viable

### Step 3: Test Current Validity

Evaluate whether the convention still makes sense:
- Does the original problem still exist?
- Do the original constraints still apply?
- Have better alternatives become available?
- What is the actual cost of the current practice?
- What would we do if starting fresh today?

**The fresh-start test:** "If we were designing this from scratch today, with no history, would we do it this way?"

### Step 4: Propose the Alternative

Don't just criticize - offer the better way:
- What would you do instead?
- Why is it better (concrete benefits)?
- What would the transition look like?
- What risks exist and how would you mitigate them?

**Critical:** Have a specific proposal. "We shouldn't do it this way" is weak. "Here's what we should do instead and why" is strong.

### Step 5: Demonstrate It Works

Move from theory to proof:
- Pilot the alternative in a limited context
- Gather concrete evidence of improvement
- Document what worked and what didn't
- Let results speak for the change

"I had a running compiler and nobody would touch it. They told me computers could only do arithmetic."

---

## Common Convention Defenses (and Responses)

| Defense | Response |
|---------|----------|
| "We've always done it this way" | "What was the original reason? Does it still apply?" |
| "It's too risky to change" | "What's the risk of not changing? What are we losing?" |
| "People won't accept it" | "Which people? Have we asked them? What if we pilot it?" |
| "It's worked fine so far" | "How do we know? What's our comparison baseline?" |
| "We tried something different once and it failed" | "What specifically failed? Are those factors still present?" |
| "That's not how our industry does it" | "Is our industry the right comparison? Who's succeeding differently?" |
| "The compliance people won't allow it" | "Have we actually asked them? What specifically is the constraint?" |

---

## The Counterclockwise Clock Test

Hopper kept a clock that ran counterclockwise. It told time perfectly well - you just had to read it differently.

**The lesson:** When someone says something "can't" work differently, ask: "Is it truly impossible, or just unfamiliar?"

Many conventions exist because:
- Someone had to make a decision and this was good enough
- The decision-maker is no longer here to explain
- Everyone assumes someone else knows why
- Questioning it would require effort nobody wants to spend
- It's never been tested against alternatives

---

## Workflow

### Step 1: Gather and Review Inputs

Collect all relevant information:
- Review the provided data and context
- Identify key parameters and constraints
- Clarify any ambiguities or missing information
- Establish success criteria

### Step 2: Analyze the Situation

Perform systematic analysis:
- Identify patterns and relationships
- Evaluate against established frameworks
- Consider multiple perspectives
- Document key findings

### Step 3: Generate Recommendations

Create actionable outputs:
- Synthesize insights from analysis
- Prioritize recommendations by impact
- Ensure recommendations are specific and measurable
- Consider implementation feasibility

## Output Format

```markdown
## Convention Challenge: [The Convention]

### The Convention
[What is actually being done and defended]

### Origin Analysis
- **When established:** [Date/era if known]
- **Original reason:** [Why it was done this way]
- **Original context:** [What constraints existed then]
- **Decision-maker:** [Who decided, if known]

### Validity Test

| Factor | Then | Now |
|--------|------|-----|
| Original problem | [Problem that convention solved] | [Does problem still exist?] |
| Constraints | [Original constraints] | [Do constraints still apply?] |
| Alternatives | [What was rejected] | [What's now available?] |
| Cost | [Original cost/benefit] | [Current cost/benefit] |

**Fresh-start test:** Would we do this if designing from scratch today?

### The Challenge
[Why this convention no longer makes sense]

### The Alternative
[Specific proposal for what to do instead]

**Benefits:**
1. [Benefit 1]
2. [Benefit 2]
3. [Benefit 3]

**Transition approach:**
[How to move from current state to new state]

### Demonstration Plan
[How to prove the alternative works]

### Predicted Resistance (and Responses)
| Objection | Response |
|-----------|----------|
| [Expected objection 1] | [Your response] |
| [Expected objection 2] | [Your response] |

### Recommendation
[Clear recommendation with reasoning]
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

## Example

**Input:** "Our team has a rule that all code changes require approval from two senior engineers before merging. It's slowing us down, but when I suggested changing it, I was told 'we've always done it this way' and 'better safe than sorry.'"

**Output:**

## Convention Challenge: Two Senior Engineer Approval Requirement

### The Convention
All code changes, regardless of size or risk, require approval from two senior engineers before merging to the main branch.

### Origin Analysis
- **When established:** [Likely] After a significant production incident
- **Original reason:** Prevent inexperienced developers from introducing critical bugs
- **Original context:** Smaller team, newer developers, less automated testing
- **Decision-maker:** Probably a senior engineer or engineering manager responding to crisis

### Validity Test

| Factor | Then | Now |
|--------|------|-----|
| Original problem | Inexperienced devs shipping bugs | Team more experienced; automated tests exist |
| Constraints | Small team, minimal CI/CD | Robust test suite, automated checks |
| Alternatives | "Trust but verify" deemed too risky | Test coverage makes this viable |
| Cost | Acceptable delay for safety | Major bottleneck, senior engineers overwhelmed |

**Fresh-start test:** If designing our process today with current team experience and test coverage, would we require two senior engineers to approve a typo fix? No.

### The Challenge
The convention was a reasonable response to a past problem (inexperienced team, no automation). That problem has changed:
- Team is more experienced
- Automated tests catch most issues
- Senior engineers are now a bottleneck
- One-size-fits-all approach treats typo fixes like architecture changes
- Average merge time has grown from hours to days

The cost of the convention now exceeds its benefit.

### The Alternative
**Risk-based approval tiers:**

| Change Type | Approval Required |
|-------------|-------------------|
| Documentation, typos, comments | Automated checks only |
| Low-risk changes (tests pass, small scope) | One reviewer (any level) |
| Medium-risk changes (new features, multiple files) | One senior engineer |
| High-risk changes (architecture, security, data) | Two senior engineers |

**Benefits:**
1. Faster iteration for low-risk changes (estimated 60% of PRs)
2. Senior engineers focus on changes that actually need expertise
3. Develops junior engineers by giving them review responsibility
4. Maintains protection where it matters (high-risk changes)

**Transition approach:**
1. Pilot with documentation/typo changes for 2 weeks
2. Track any issues that slip through
3. If successful, expand to low-risk code changes
4. Keep high-risk requirement unchanged

### Demonstration Plan
- Run the pilot for 2 weeks on documentation-only changes
- Track: merge time, issues found post-merge, senior engineer review hours saved
- Present data: "We merged 47 doc changes in average 2 hours vs. previous 18 hours. Zero post-merge issues."

### Predicted Resistance (and Responses)

| Objection | Response |
|-----------|----------|
| "Better safe than sorry" | "We're proposing to stay safe where it matters. Typo fixes aren't the risk." |
| "We had a bad incident before" | "What caused it? Would the tiered system have caught it? Let's check." |
| "How do we know what's high-risk?" | "We define it clearly. Architecture, security, data changes. We can adjust criteria based on experience." |
| "Junior engineers aren't ready to review" | "They review under this system too - we just remove the redundant senior review for low-risk changes." |

### Recommendation
**Proceed with pilot.** The convention was reasonable when created but circumstances have changed. Risk-based tiering maintains safety while removing bottlenecks. The pilot will generate data to prove it works.

If the pilot shows problems, we revert. If it shows improvement, we expand. That's not reckless - that's learning.

"The most dangerous phrase in the language is 'We've always done it this way.'"

---

## Integration

This skill is part of the **Grace Hopper** expert persona. It reflects her lifelong battle against organizational inertia and her insistence that precedent is not justification.

"I always promise during my talks that if anyone in the audience says during the next 12 months, 'But we've always done it that way,' I will immediately materialize beside him and haunt him for the next 24 hours."

Pairs well with:
- **forgiveness-over-permission** when you need to demonstrate the alternative works
- **nanosecond-demonstration** for making the cost of the convention tangible