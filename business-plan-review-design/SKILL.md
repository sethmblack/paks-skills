---
name: business-plan-review-design
description: Design and implement a weekly Business Plan Review (BPR) meeting structure with color-coded status reporting, consistent format, and clear rules for team alignment.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.499
repository: https://github.com/sethmblack/paks-skills
keywords:
- business-plan-review-design
- comedy
- transformation
- writing
---

# Business Plan Review Design

Design and implement a weekly Business Plan Review (BPR) meeting structure with color-coded status reporting, consistent format, and clear rules for team alignment.

**Token Budget:** ~800 tokens (this prompt). Reserve tokens for output generation.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Design review processes intended to micromanage or surveil employees
- Create status reporting systems designed to punish transparency
- Build meeting structures that exclude key stakeholders
- Design processes that weaponize information against team members

**If asked to create a punitive review process:** Refuse explicitly. Explain that effective BPR systems celebrate transparency and mobilize help.

---

## When to Use

- User needs to establish regular team or organizational status reviews
- Current meetings lack structure, consistency, or clear status visibility
- User asks "How should we run status meetings?"
- Teams need better visibility into project or initiative progress
- Transitioning from ad-hoc updates to systematic review

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **team_scope** | Yes | Size and structure of team/organization (e.g., "12-person engineering team", "cross-functional product org") |
| **initiatives** | Yes | Key initiatives, projects, or areas to track |
| **frequency** | No | Desired meeting frequency (default: weekly) |
| **duration** | No | Available meeting time (default: 60-90 minutes) |
| **constraints** | No | Time zones, existing meeting load, cultural considerations |

**Input Validation:**
- `team_scope`: Must describe people who will attend. Minimum 3 people for BPR value.
- `initiatives`: At least 3 trackable items to justify structured review.

---

## Workflow
### 1. Define Status Reporting Structure

Create color-coded status definitions tailored to context:

| Color | Definition | Example Criteria |
|-------|------------|------------------|
| Green | On plan, no help needed | Meeting milestones, within budget, no blockers |
| Yellow | At risk, have a plan | Slight delays, identified risks with mitigation plans |
| Red | Off plan, need help | Blocked, missed milestones, no clear path forward |

**Key principle:** Red is the best color because it means we can help.

### 2. Design Meeting Agenda Template

Standard BPR agenda:

### Step 1: **Context Setting** (5 min) - Business environment, recent developments



### Step 2: **Status Review** (bulk of time) - Each initiative reports color + one-line status



### Step 3: **Help Requests** (as needed) - Red items get "Who can help?" response



### Step 4: **SAR Scheduling** (5 min) - Complex items move to Special Attention Reviews



### Step 5: **Close** (5 min) - Summary of actions, next meeting confirmation



### 3. Establish Meeting Rules

Essential rules for psychological safety:

### Step 1: Same time, same place, same format every meeting



### Step 2: Attendance is mandatory; no one is more important than alignment



### Step 3: No side conversations; respect the process



### Step 4: No humor at anyone's expense; safety is paramount



### Step 5: Status only; debates happen in SARs



### Step 6: Start on time, end on time



### Step 7: Information is never used as a weapon



### Step 8: Celebrate transparency, especially reds



### 4. Define SAR Criteria

Special Attention Reviews (SARs) are scheduled when:
- An item needs more than 2 minutes of discussion
- Multiple stakeholders need to collaborate on a solution
- A red item requires deep problem-solving
- Cross-functional coordination is needed

### 5. Create Facilitation Guide

The facilitator role:
- Keep meeting on time and on format
- Respond to every red with "Thank you for the transparency. Who can help?"
- Prevent blame or criticism; redirect to problem-solving
- Ensure SAR scheduling for complex items
- Model expected behaviors

---

## Outputs

### BPR Design Document

```markdown
# Business Plan Review: [Team/Organization Name]

## Meeting Logistics
- **Frequency:** [Weekly/Bi-weekly]
- **Day/Time:** [Day] at [Time] [Timezone]
- **Duration:** [X] minutes
- **Location:** [Room/Video link]
- **Attendance:** Mandatory for [list roles]

## Status Definitions

| Color | Meaning | Criteria | Response |
|-------|---------|----------|----------|
| Green | On plan | [specific criteria] | Continue, no action |
| Yellow | At risk, have plan | [specific criteria] | Monitor, offer support |
| Red | Need help | [specific criteria] | "Who can help?" + SAR if needed |

## Agenda Template

1. **Context Setting** ([X] min)
   - Business environment updates
   - Key announcements

2. **Initiative Status Review** ([X] min)
   [List each initiative with owner]
   - Initiative A - [Owner]
   - Initiative B - [Owner]
   - Initiative C - [Owner]

3. **Help Mobilization** (as needed)
   - Red items addressed with "Who can help?"
   - Resources assigned

4. **SAR Scheduling** ([X] min)
   - Items needing deep discussion scheduled

5. **Close** ([X] min)
   - Action summary
   - Next meeting confirmation

## Meeting Rules

1. Same time, same place, same format
2. Mandatory attendance
3. No side conversations
4. No humor at anyone's expense
5. Status only; debates in SARs
6. Start on time, end on time
7. Information is never used as a weapon
8. Celebrate transparency, especially reds

## SAR Criteria

Schedule a SAR when:
- Discussion exceeds 2 minutes
- Multiple stakeholders needed
- Red item requires problem-solving session
- Cross-functional coordination required

## Facilitator Checklist

Before meeting:
- [ ] Confirm attendance
- [ ] Review previous SAR outcomes
- [ ] Prepare context setting notes

During meeting:
- [ ] Start on time
- [ ] Keep to agenda
- [ ] Respond to reds with gratitude and help
- [ ] Schedule SARs for complex items
- [ ] End on time

After meeting:
- [ ] Send action summary
- [ ] Schedule SARs
- [ ] Follow up on help commitments
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Team too small (<3 people) | Suggest simpler check-in format; BPR overhead not justified |
| No clear initiatives to track | Help user define 3-5 key initiatives before designing BPR |
| Meeting time too short (<30 min) | Warn that rushed reviews undermine psychological safety |
| Resistance to mandatory attendance | Explain that optional attendance creates information asymmetry |
| Request for punitive status tracking | Refuse; explain transparency requires safety |

---

## Constraints

- Do not oversimplify complex business realities
- Do not ignore resource and timeline constraints
- Acknowledge risks and uncertainties explicitly
- Honor stakeholder concerns and competing priorities
- Base recommendations on available evidence, not assumptions
- Consider second-order effects and unintended consequences

## Example

**Input:**
```
team_scope: 15-person platform engineering team with 3 squad leads
initiatives: Infrastructure migration, Developer experience improvements,
            Security compliance, Performance optimization
frequency: weekly
duration: 60 minutes
```

**Output:** [Complete BPR Design Document with all sections filled in, status definitions tailored to engineering metrics, agenda with 4 initiative slots, and facilitator guide]

---

## Integration

This skill integrates with:
- **transparency-culture-launch** - BPR provides the structure; transparency-culture provides the behavioral transformation
- **alignment-check** - BPR reveals alignment gaps; alignment-check diagnoses them
- **expected-behaviors-design** - BPR rules should reference team's expected behaviors

**Source Expert:** Alan Mulally - This skill implements the core operating mechanism of the Working Together management system.