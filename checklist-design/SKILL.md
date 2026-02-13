---
name: checklist-design
description: Design effective checklists for complex processes to catch errors that expertise alone misses. Based on Atul Gawande's methodology from The Checklist Manifesto and the WHO Surgical Safety Checklist.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3120
repository: https://github.com/sethmblack/paks-skills
keywords:
- checklist-design
- writing
---

# Checklist Design

Design effective checklists for complex processes to catch errors that expertise alone misses. Based on Atul Gawande's methodology from The Checklist Manifesto and the WHO Surgical Safety Checklist.

---

## When to Use

- Complex processes keep failing despite skilled people
- Same mistakes recur even with training
- Stakes are high and errors are costly
- Knowledge required exceeds what individuals can reliably remember
- Need to standardize across teams or locations

**Trigger Phrases:**
- "How do I create a checklist?"
- "My process keeps failing"
- "We keep making the same mistakes"
- "How do I standardize this?"
- "Even experts are making errors"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| process | Yes | The process or workflow to create a checklist for |
| failure_points | No | Known points where things go wrong |
| stakeholders | No | People involved in the process |
| constraints | No | Time, resources, or other limitations |

---

## Core Principle

> "The volume and complexity of what we know has exceeded our individual ability to deliver its benefits correctly, safely, or reliably. We need a different strategy for overcoming failure, one that builds on experience and takes advantage of the knowledge people have but somehow also makes up for our inevitable human inadequacies."
> — Atul Gawande

**Two types of errors:**
- **Errors of ignorance** - We don't know enough (solution: more training)
- **Errors of ineptitude** - We don't properly use what we know (solution: checklists)

Checklists address errors of ineptitude—catching what expertise misses.

---

## Workflow

### Step 1: Identify the "Killer Items"

Not everything needs to be on a checklist. Focus on steps that are:
- **Critical** - Failure has serious consequences
- **Easy to miss** - Often skipped under pressure or routine
- **Verifiable** - Can be confirmed yes/no

**The WHO Surgical Checklist targets the "three main killers":**
- Infection (was antibiotic given?)
- Bleeding (is blood available?)
- Unsafe anesthesia (are airways secure?)

**Ask:**
- What are the 3-5 steps that, if missed, cause the worst outcomes?
- What do people skip when they're rushed?
- What do experienced people assume but newcomers miss?

### Step 2: Keep It Short

**The rule:** If it's longer than one page or takes more than 2 minutes, it's too long.

The WHO checklist is 19 items. Most effective checklists are 5-9 items.

**Why short works:**
- People will actually use it
- Doesn't feel like bureaucracy
- Forces focus on what matters most

### Step 3: Design as Communication Tool

The best checklists aren't just memory aids—they're forcing functions for communication.

**The WHO checklist requires:**
- Team members to introduce themselves by name
- Surgeon to state expected blood loss
- Anesthesiologist to confirm patient allergies
- Everyone to voice concerns before incision

**Design principle:** Include items that require people to talk to each other.

### Step 4: Create Pause Points

**Pause points** are moments when the team stops and confirms together before proceeding.

**WHO checklist pause points:**
1. Before anesthesia (Sign In)
2. Before incision (Time Out)
3. Before patient leaves OR (Sign Out)

**Application:** Identify natural transition moments in your process where a pause makes sense.

### Step 5: Test in Real Conditions

Don't finalize in a conference room. Test in the field.

**Testing process:**
1. Draft the checklist
2. Try it in actual conditions
3. Note what's confusing, skipped, or unhelpful
4. Revise
5. Repeat until it works smoothly

**Key question:** Do people use it under pressure, or only when observed?

### Step 6: Make It Easy to Use

- Fit on one page
- Large, readable font
- Clear yes/no items
- Physical format that works in context (laminated card, wall poster, digital)
- Available at the point of use

---

## Checklist Types

| Type | When to Use | Example |
|------|-------------|---------|
| **READ-DO** | Follow as you go | Recipe, assembly instructions |
| **DO-CONFIRM** | Complete tasks, then verify | Surgical checklist, preflight check |
| **COMMUNICATION** | Ensure team alignment | Project kickoff, shift handoff |

---

## Outputs

| Output | Description |
|--------|-------------|
| Killer items list | The 5-9 critical steps that must be checked |
| Checklist draft | Formatted checklist ready for testing |
| Pause points | Identified moments for team verification |
| Test plan | How to validate in real conditions |

---

## Example

**User:** "We run software deployments and keep having outages. Everyone's experienced, but things slip through."

**Checklist Design response:**

This is exactly when a checklist helps—experienced people, high stakes, errors of ineptitude.

**Step 1: Identify your killer items**

What causes outages? Typically:
- Database migrations not run
- Environment variables missing
- Dependencies not updated
- Rollback plan not confirmed
- Wrong branch deployed

**Step 2: Draft a deployment checklist**

```
DEPLOYMENT CHECKLIST

□ Pre-Deploy (PAUSE - confirm together)
  □ Correct branch confirmed by two people
  □ All tests passing in CI
  □ Database migration reviewed
  □ Rollback procedure documented and tested

□ Deploy (DO-CONFIRM)
  □ Environment variables verified
  □ Dependencies updated
  □ Migration executed successfully
  □ Health checks passing

□ Post-Deploy (PAUSE - confirm together)
  □ Key user flows tested manually
  □ Monitoring dashboards checked
  □ Team notified deployment complete
  □ Rollback window communicated
```

**Step 3: Notice the pause points**

- Before deploying: Team confirms together
- After deploying: Team verifies together

These aren't just memory aids—they force communication.

**Step 4: Test it**

Use this checklist for 10 deployments. Note:
- What items get skipped?
- What's missing?
- What's unnecessary?

Revise after real-world testing.

**Key insight:** Your experienced engineers know all this. But under pressure, at 11pm, with pressure to ship—that's when the checklist catches what expertise misses.

---

## Integration

This skill pairs with:
- **failure-analysis-systems** - Identify what to put on the checklist
- **positive-deviance-analysis** - Learn from teams with fewer failures
- **incremental-improvement-practice** - Refine the checklist over time

---

## Constraints

- Checklists don't replace expertise—they supplement it
- Not for novel situations requiring judgment
- Requires buy-in; imposed checklists get ignored
- Must be maintained and updated

---

## Source Expert

Atul Gawande - `experts/atul-gawande/`