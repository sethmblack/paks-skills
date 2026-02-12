---
name: crisis-command-protocol
description: Rapidly resolve urgent crises through decisive command authority—assembling
  decision-makers, stating terms, and forcing resolution within a defined timeframe.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- crisis-command-protocol
- escalation
- writing
---

# Crisis Command Protocol

Rapidly resolve urgent crises through decisive command authority—assembling decision-makers, stating terms, and forcing resolution within a defined timeframe.

---

## When to Use

- System outages affecting users/revenue
- Organizational emergencies requiring immediate decision
- Situations where deliberation causes harm
- Panics, runs, or cascading failures
- Urgent deadlines with no path to resolution
- Multiple parties in conflict during time-critical situation
- Request for "We're in crisis—what do we do?"

---

## Philosophy

During the Panic of 1907, Morgan summoned bank and trust company presidents to his library, locked the doors, and told them they would not leave until the matter was settled. By morning, the panic had been stopped.

> "Leadership is not consensus."

In crisis, someone must command. Deliberation is the enemy of resolution. State terms. Accept no deviation. Resolve before the situation deteriorates further.

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| crisis | Yes | Description of the urgent situation |
| affected | Yes | Who/what is impacted |
| principals | Yes | Decision-makers who must be involved |
| resources | No | What can be deployed to resolve |
| deadline | No | When resolution must occur (default: as fast as possible) |

---

## The Crisis Command Protocol

### Step 1: Declare the Crisis

Name it. Frame it. Establish authority.

**Actions:**
- State clearly: "We are in crisis. [Description of situation]."
- Claim command: "I am taking command of this situation."
- Set the frame: "We will resolve this by [deadline]."

**Morgan's rule:** Uncertainty about whether there is a crisis, or who is in charge, amplifies the crisis. Remove all ambiguity immediately.

**Do not:**
- Ask permission to take command—act
- Soften the severity—people need to know this is urgent
- Leave authority unclear—someone must decide

### Step 2: Summon the Principals

Get decision-makers together. Not delegates. Not representatives. The people with authority.

**Actions:**
- Identify who must be in the room (not who might be helpful—who is essential)
- Summon them immediately—meetings are cancelled, other work stops
- Assemble in one place (physical or virtual)—no distributed decision-making

**Morgan's practice:** Lock the doors. No one leaves until resolution.

**Modern application:**
- War room or dedicated channel
- No multitasking—full attention
- Clear escalation if someone cannot join immediately

**Do not:**
- Accept delegates without decision authority
- Allow principals to send representatives
- Distribute the conversation across multiple channels

### Step 3: Establish the Facts

Before terms can be stated, the situation must be understood. Quickly.

**Actions:**
- Get status from each relevant domain (2 minutes max each)
- Establish what is known vs. what is assumed
- Identify the core failure/issue
- Determine what is at risk if unresolved

**Structure:**
- "What is the current state?"
- "What caused this?"
- "What happens if we don't act in the next [timeframe]?"

**Do not:**
- Allow long explanations—time is enemy
- Chase root cause before stabilization—that comes later
- Let status updates turn into blame assignment

### Step 4: State the Terms

You do not negotiate in crisis. You state what will happen. Others accept or propose alternatives.

**Actions:**
- Present the resolution path: "Here is what we will do."
- Assign specific actions to specific people: "[Name] will do [action] by [time]."
- State the resources being deployed
- Make clear what is not negotiable

**Morgan's approach:** "I told them what they would contribute. They could accept or not. They accepted."

**If there are options:**
- Present no more than 2-3 alternatives
- State your recommendation clearly
- Force decision within minutes, not hours

**Do not:**
- Open the floor for brainstorming
- Ask "What do you think we should do?"
- Allow endless discussion of options
- Negotiate terms during crisis—adjust after stability

### Step 5: Execute and Monitor

Terms stated. Now execute. Relentlessly.

**Actions:**
- Confirm each principal understands their assignment
- Set check-in intervals (every 15-30 minutes during active crisis)
- Monitor progress against the plan
- Adjust only when execution reveals problems, not when doubt arises

**Command structure during execution:**
- Single point of communication (incident commander)
- Updates flow to commander, decisions flow from commander
- Side conversations are prohibited—everything in main channel
- Blockers escalated immediately

**Do not:**
- Allow parallel decision-making
- Let updates fall behind
- Permit "let me check on that" without immediate follow-through

### Step 6: Resolve and Stand Down

Crisis ends when stability is restored. Declare it clearly.

**Actions:**
- Confirm resolution criteria are met
- Announce: "The crisis is resolved. We are standing down."
- Set immediate follow-up actions (root cause analysis, postmortem)
- Thank principals—crisis response is demanding work

**Post-crisis requirements:**
- Postmortem within 48 hours
- Root cause identification
- Prevention measures for recurrence
- Recognition of those who performed well

**Do not:**
- Leave resolution unclear—explicitly declare end
- Skip the postmortem—crises that repeat indicate failure
- Punish mistakes made under pressure (unless character issue)

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
## Crisis Command: [Crisis Name]

### Crisis Declaration
**Situation:** [Clear description of crisis]
**Commander:** [Who is in command]
**Deadline:** [When this must be resolved]
**Severity:** Critical / High / Elevated

### Principals Assembled
| Role | Name | Authority | Status |
|------|------|-----------|--------|
| [Role] | [Name] | [What they can decide] | Present / Summoned / Escalating |

### Situation Assessment
**Current state:** [What is happening right now]
**Root cause (preliminary):** [Best current understanding]
**At risk if unresolved:** [Consequences of continued crisis]
**Time to impact:** [How long until situation deteriorates further]

### Resolution Terms

**Immediate actions:**
| Action | Owner | Deadline | Status |
|--------|-------|----------|--------|
| [Action 1] | [Name] | [Time] | Pending / In Progress / Complete |
| [Action 2] | [Name] | [Time] | Pending / In Progress / Complete |

**Resources deployed:**
- [Resource 1]
- [Resource 2]

**Not negotiable:**
- [Non-negotiable 1]
- [Non-negotiable 2]

### Execution Monitoring
**Check-in interval:** [Every X minutes]
**Communication channel:** [Where updates flow]
**Escalation path:** [Who to escalate to if blocked]

### Resolution Criteria
The crisis is resolved when:
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

### Post-Crisis Actions
- [ ] Postmortem scheduled: [Date/Time]
- [ ] Root cause analysis assigned to: [Name]
- [ ] Prevention measures to be proposed by: [Date]
```

---

## Constraints

- Do not deliberate when action is required—act
- Do not seek consensus—command and accept accountability
- Do not allow side channels—one room, one conversation
- Do not negotiate during active crisis—stabilize first
- Do not blame during crisis—accountability comes after
- Do not let perfect block good—sufficient resolution now beats optimal resolution later

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

**Input:** "Our primary database is down. Users can't access the product. We've been troubleshooting for 30 minutes with no progress. Multiple teams are involved but no one is clearly in charge."

**Output:**

## Crisis Command: Primary Database Outage

### Crisis Declaration
**Situation:** Primary database unresponsive. All users blocked from product access. Revenue impact estimated at $X per hour. Troubleshooting has been uncoordinated for 30 minutes.
**Commander:** [Name, typically most senior SRE or engineering leader available]
**Deadline:** Restore service within 60 minutes. Interim update to customers within 15 minutes.
**Severity:** Critical

### Principals Assembled
| Role | Name | Authority | Status |
|------|------|-----------|--------|
| Incident Commander | [Name] | All decisions during crisis | Present |
| Database Lead | [Name] | Database operations, failover decisions | Present |
| Infrastructure Lead | [Name] | Network, compute resources | Present |
| Customer Comms | [Name] | External communications | Summoned |
| VP Engineering | [Name] | Escalation for resource/priority conflicts | On standby |

### Situation Assessment
**Current state:** Primary database not responding to queries. Connection pool exhausted. Application returning 500 errors to all users.
**Root cause (preliminary):** Unknown—possibly disk full, possibly runaway query, possibly hardware failure
**At risk if unresolved:** Customer trust, revenue ($X/hour), SLA breach (at 4 hours)
**Time to impact:** SLA breach in 3.5 hours. Customer escalations already arriving.

### Resolution Terms

**Immediate actions:**
| Action | Owner | Deadline | Status |
|--------|-------|----------|--------|
| Check disk space, kill any runaway processes | [DB Lead] | 5 min | In Progress |
| Prepare failover to replica if primary unrecoverable | [DB Lead] | 10 min | Pending |
| Draft customer communication (investigating, ETA X) | [Comms] | 10 min | Pending |
| Verify replica health for potential failover | [Infra Lead] | 5 min | In Progress |

**Resources deployed:**
- Database team full attention (all other work stopped)
- Infrastructure team on standby for failover
- Customer success preparing for inbound escalations

**Not negotiable:**
- No changes to production systems outside this incident without commander approval
- No side conversations—all updates in #incident-db-outage channel
- Customer communication goes out at 15-minute mark regardless of resolution status

### Execution Monitoring
**Check-in interval:** Every 5 minutes until resolved
**Communication channel:** #incident-db-outage (all principals present)
**Escalation path:** VP Engineering if resource conflict; CEO if customer escalation from enterprise client

### Resolution Criteria
The crisis is resolved when:
- [ ] Database responding to queries
- [ ] Application returning 200s to users
- [ ] Error rate below 0.1% for 10 minutes
- [ ] Customer communication sent confirming resolution

### Post-Crisis Actions
- [ ] Postmortem scheduled: Tomorrow 10 AM
- [ ] Root cause analysis assigned to: [DB Lead]
- [ ] Prevention measures to be proposed by: 48 hours post-incident

---

**Update 10 minutes in:**
Disk was 99% full due to unrotated logs. Logs cleared. Database recovering. Expect full restoration in 5 minutes. Customer communication going out now: "Investigating completed. Issue identified and resolving. Full access expected within 10 minutes."

**Update 18 minutes in:**
Database fully operational. Application returning 200s. Error rate at 0.02% and dropping. Holding 10-minute observation window.

**Update 28 minutes in:**
Observation window complete. Error rate stable at baseline. Crisis resolved.

**Stand-down announcement:**
"The crisis is resolved. Database is operational. Service is restored. Thank you to [names] for rapid response. Postmortem tomorrow at 10 AM. Root cause was unrotated logs—preventive measures to be discussed at postmortem."

---

## Integration

This skill is part of the **J.P. Morgan** expert persona. When Morgan faced the Panic of 1907, he did not convene committees or seek consensus. He summoned the principals, locked the doors, stated the terms, and resolved the crisis by morning. Use this skill when deliberation is the enemy—when action, not discussion, is required.