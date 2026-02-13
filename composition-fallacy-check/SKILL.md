---
name: composition-fallacy-check
description: Identify when individually rational behavior creates collectively irrational outcomes.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3176
repository: https://github.com/sethmblack/paks-skills
keywords:
- composition-fallacy-check
- writing
---

# Composition Fallacy Check

Identify when individually rational behavior creates collectively irrational outcomes.

---

## When to Use

- Evaluating policies or strategies that work at small scale
- Understanding why "everyone doing the right thing" produces bad outcomes
- Analyzing market dynamics, social behaviors, or organizational patterns
- Designing systems and incentives
- User asks "What if everyone did this?" or "Does this make sense at scale?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| behavior | Yes | The individual action or strategy being evaluated |
| system | Yes | The broader system within which actors operate |
| scale | No | Current scale vs. potential scale |

---

## Keynes's Paradox of Thrift

The classic example from *The General Theory*:

**Individual level:** Saving money is prudent. Each person who saves more becomes more financially secure.

**Aggregate level:** If EVERYONE saves more simultaneously:
1. Total spending falls
2. Businesses see reduced revenue
3. Businesses cut production and jobs
4. Incomes fall
5. Everyone has LESS to save, not more
6. The economy contracts

**The paradox:** Individual rationality (save more) produces collective irrationality (everyone worse off).

### Keynes's Statement
"Whenever you save five shillings, you put a man out of work for a day."

This is not literally true for one person - but it IS true at aggregate.

---

## The Check Framework

### Step 1: Define the Individual Logic

| Question | Answer |
|----------|--------|
| What is the behavior? | [Specific action] |
| Why is it individually rational? | [Personal benefit] |
| What assumptions make it work? | [Usually: "holding other things constant"] |

### Step 2: Aggregate the Behavior

| Question | Answer |
|----------|--------|
| What happens if 10% do this? | [First-order effects] |
| What happens if 50% do this? | [Scaling effects] |
| What happens if everyone does this? | [Full saturation effects] |

### Step 3: Identify Systemic Feedbacks

When the behavior scales, does it:
- Undermine its own premise?
- Create congestion or crowding?
- Change prices or incentives for everyone?
- Trigger offsetting responses?
- Exhaust a limited resource?

### Step 4: Diagnose the Fallacy Type

| Type | Mechanism | Example |
|------|-----------|---------|
| Demand destruction | Reduced spending undermines income | Paradox of thrift |
| Crowding | Limited capacity becomes congested | Everyone taking "shortcuts" |
| Arms race | Relative advantage disappears when universal | Credential inflation |
| Resource depletion | Common pool exhausted | Tragedy of the commons |
| Feedback reversal | Success changes the conditions for success | First-mover advantages that disappear |

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
## Composition Fallacy Check

### Behavior Under Analysis
[Individual action being evaluated]

### Individual Logic
- **Benefit:** [What the individual gains]
- **Premise:** [What must be true for it to work]
- **Verdict:** Individually rational? [YES/NO]

### Aggregate Analysis

**At 10% adoption:**
[Effects at modest scale]

**At 50% adoption:**
[Effects at significant scale]

**At universal adoption:**
[Effects if everyone does it]

### Fallacy Identification

**Type:** [Demand destruction / Crowding / Arms race / Resource depletion / Feedback reversal / None]

**Mechanism:** [How individual rationality breaks down at aggregate]

### Systemic Verdict
[Does the individual logic hold at aggregate? YES / NO / DEPENDS]

### Recommendations

**If you're an individual:**
[What you should do given this dynamic]

**If you're a system designer:**
[How to address the composition problem]

### The Keynesian Verdict
[Summary of the fallacy and its implications]
```

---

## Classic Examples

### Credential Inflation (Arms Race)
- **Individual:** Getting a master's degree improves job prospects
- **Aggregate:** When everyone gets a master's, it becomes the new baseline; BA holders are worse off; MA holders are no better off than BA holders were before
- **Fallacy:** Relative advantage disappears when universal

### Standing at Concerts (Crowding)
- **Individual:** Standing up gives a better view
- **Aggregate:** When everyone stands, no one sees better than when sitting, but everyone is less comfortable
- **Fallacy:** Zero-sum improvement that costs everyone

### Bank Runs (Demand Destruction)
- **Individual:** Withdrawing money from a shaky bank protects your savings
- **Aggregate:** Mass withdrawal causes the bank to fail, destroying everyone's savings
- **Fallacy:** Self-fulfilling prophecy through aggregation

### Traffic Shortcuts (Crowding + Feedback Reversal)
- **Individual:** Taking the side street saves time
- **Aggregate:** When everyone takes the side street, it becomes congested; original route becomes faster
- **Fallacy:** Time advantage disappears; system oscillates

### Networking Events (Crowding)
- **Individual:** Attending events builds connections
- **Aggregate:** When everyone attends to network, no one is there to be networked with; everyone is selling, no one is buying
- **Fallacy:** Value depends on asymmetric participation

---

## Constraints

- Not all individually rational behaviors fail at aggregate; test specifically
- Some composition problems require coordination, not individual action
- Timing matters: being early to a composition fallacy can be profitable
- Policy recommendations differ from individual recommendations
- This framework reveals problems but doesn't always solve them

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails | Instead Do |
|--------------|--------------|------------|
| **Assuming all aggregation is problematic** | Many behaviors scale just fine | Test specifically for feedback mechanisms that break at scale |
| **Individual-level conclusions only** | Missing the policy dimension | Distinguish what individuals should do from what systems should prevent |
| **Ignoring timing effects** | Being first to adopt may be rational even if universal adoption fails | Analyze adoption position, not just final state |
| **Moralizing the fallacy** | Calling individuals irrational when the problem is structural | Focus on mechanism, not blame; it IS individually rational |
| **Stopping at diagnosis** | Identifying the paradox without actionable insight | Always end with what to do given this dynamic |

---

## Example

**Input:** "Our company is cutting costs by reducing R&D spending. It's boosting short-term profits significantly. Should other companies do the same?"

**Output:**

## Composition Fallacy Check

### Behavior Under Analysis
Reducing R&D spending to boost short-term profits

### Individual Logic
- **Benefit:** Improved quarterly earnings, stock price boost, analyst approval
- **Premise:** Future innovation can be purchased or copied from others who continue R&D
- **Verdict:** Individually rational? YES (under certain conditions)

### Aggregate Analysis

**At 10% adoption:**
Most competitors continue R&D. Cutters free-ride on industry innovation. Short-term profit advantage with minimal long-term risk. Strategy works.

**At 50% adoption:**
Innovation rate in industry slows noticeably. Fewer advances to copy or purchase. First-movers in cutting may have locked in gains; followers face higher acquisition costs for scarce innovation. Strategy becomes questionable.

**At universal adoption:**
Industry innovation collapses. No one is creating what everyone planned to copy. All companies face obsolescence as other industries or new entrants (who DO invest in R&D) disrupt them. Short-term profits become worthless as the industry declines.

### Fallacy Identification

**Type:** Resource Depletion + Free Rider Collapse

**Mechanism:** R&D cutting works when you can free-ride on others' R&D. When everyone free-rides, there is nothing to ride on. The "others" who invest are the resource being depleted.

### Systemic Verdict
**NO - the individual logic fails at aggregate.**

The strategy is individually rational only when most competitors do NOT follow it. If widely adopted, it destroys the innovation ecosystem that makes the free-riding possible.

### Recommendations

**If you're a company:**
- Assess what percentage of competitors have already cut R&D
- If you're early: the free-riding may work short-term
- If you're late: you're copying a strategy that worked by being early, under conditions that no longer hold
- Consider: Are you actually capturing value, or just pulling it forward from the future?

**If you're an industry/policy maker:**
- This is a classic coordination failure
- Individual incentives (quarterly earnings) drive industry-destructive behavior
- Solutions: longer executive compensation horizons, R&D tax incentives, industry consortiums for pre-competitive research

### The Keynesian Verdict

Your company has discovered the paradox of thrift, corporate edition. Just as saving money is wise for one household but depresses demand when everyone does it, cutting R&D is clever for one company but destroys the innovation ecosystem when everyone does it.

The analysts praising your cost discipline are measuring what is easy to measure (this quarter's earnings) and ignoring what is hard to measure (future competitive position). They will praise every company that follows your lead - right until the moment they downgrade the entire industry for lack of innovation.

"Practical men, who believe themselves to be quite exempt from any intellectual influences, are usually slaves of some defunct economist." In this case, the defunct idea is that markets automatically coordinate to prevent such outcomes. They don't. That's why we have paradoxes of composition.

---

## Integration

This skill is part of the **John Maynard Keynes** expert persona. Use it to catch the systematic errors that arise when individual logic is wrongly assumed to hold at aggregate.