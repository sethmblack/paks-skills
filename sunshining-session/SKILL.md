---
name: sunshining-session
description: Prepare and facilitate a leadership vulnerability session where leaders
  share their mistakes openly to build psychological safety and destroy CYA culture.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- sunshining-session
- writing
---

# Sunshining Session

Prepare and facilitate a leadership vulnerability session where leaders share their mistakes openly to build psychological safety and destroy CYA culture.

**Token Budget:** ~450 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Help fabricate or exaggerate mistakes for manipulation
- Script "sunshining" that actually assigns blame to others
- Prepare vulnerability that conceals rather than reveals
- Use sunshining as a performance rather than genuine transparency

**If intent is performative:** Clarify that sunshining only works when genuine. Fake vulnerability destroys trust faster than no vulnerability.

---

## When to Use

- User wants to build psychological safety in their team
- User asks about "sunshining" or leaders sharing mistakes
- Team has a culture of hiding problems or CYA behavior
- User is preparing for an all-hands or team meeting
- User wants to model vulnerability as a leader

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `mistakes_to_share` | Yes | Recent mistakes or failures the leader can share |
| `audience` | No | Who will hear this (team size, composition, trust level) |
| `current_culture` | No | Current state of psychological safety and transparency |
| `format` | No | Delivery setting (all-hands, team meeting, 1:1) |

---

## Workflow
### 1. Select Appropriate Mistakes

Good sunshining material:
- **Recent** - Fresh mistakes are more credible than ancient history
- **Meaningful** - Stakes were real, not trivial errors
- **Yours** - Your decision, your mistake, not blame-shifted
- **Learnable** - There's a clear lesson others can apply

Poor sunshining material:
- Mistakes so old they feel like humble-bragging
- Trivial errors that seem performative
- Mistakes that were actually someone else's fault
- Confidential situations that shouldn't be shared

### 2. Structure the Sharing

Each mistake follows this structure:

### Step 1: **What I decided/did** - Own the action clearly



### Step 2: **What went wrong** - Describe the impact honestly



### Step 3: **What I learned** - Extract the lesson



### Step 4: **What I'd do differently** - Show growth



Keep each mistake to 2-3 minutes. Depth over breadth.

### 3. Model Receiving Feedback

After sharing, invite response:
- "What questions do you have?"
- "Has anyone seen me make similar mistakes they haven't told me about?"
- "What am I missing in my analysis?"

This signals that feedback flows up, not just down.

### 4. Establish Cadence

Sunshining works when it's regular, not a one-time event:
- Every all-hands: "Here's what I got wrong this quarter..."
- After project failures: Immediate post-mortem with leader mistakes first
- In 1:1s: Share your struggles, not just your wins

---

## Outputs

Provide a sunshining session plan:

```markdown
## Sunshining Session Plan

### Context
**Audience:** [Who, how many]
**Format:** [All-hands, team meeting, etc.]
**Current Trust Level:** [Low/Medium/High]
**Duration:** [Time allocated]

### Mistakes to Share

#### Mistake 1: [Brief title]
**What I decided/did:**
[Your action, clearly owned]

**What went wrong:**
[Impact and consequences]

**What I learned:**
[The lesson]

**What I'd do differently:**
[Future approach]

#### Mistake 2: [Brief title]
[Same structure]

### Opening Statement
"[Script for how to introduce the session and set context for why you're doing this]"

### Closing and Invitation
"[Script for inviting feedback and signaling this is ongoing practice]"

### Follow-up Actions
1. [How to reinforce the practice]
2. [How to invite team members to do the same]
3. [When to do this again]

### Warning Signs of Performative Sunshining
- If sharing feels like a performance, pause
- If you're secretly proud of the "mistake," choose another
- If the lesson makes you look good, dig deeper
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| User can't think of mistakes | Everyone makes mistakes. Help them identify recent decisions with imperfect outcomes. If they truly can't, they may be in denial. |
| Mistakes involve confidential information | Guide toward learnings that can be shared without compromising confidentiality |
| Team has very low trust | Start smaller - 1:1 sunshining before public. Build gradually. |
| User wants to share others' mistakes | That's not sunshining, that's blame-shifting. Redirect to their own decisions. |
| Mistake was truly not their fault | If they had no agency, it's not a sunshining candidate. Find something they could have influenced. |

---

## Constraints

- Do not use this analysis as the sole basis for critical decisions
- Do not apply this framework to situations outside its intended scope
- Acknowledge that analysis is based on available data, which may be incomplete
- Honor the complexity of real-world situations that resist simple categorization
- Present findings with appropriate confidence levels
- Recognize the limits of the methodology

## Example

**Input:**
```
mistakes_to_share: 1) Hired wrong person for critical role, took 6 months to address
                   2) Launched feature without customer research, had to pull it back
audience: Engineering team, 25 people, quarterly all-hands
current_culture: Medium trust, some CYA behavior observed
```

**Output:**

## Sunshining Session Plan

### Context
**Audience:** Engineering team, 25 people
**Format:** Quarterly all-hands
**Current Trust Level:** Medium - CYA behavior present
**Duration:** 10 minutes (5 per mistake)

### Mistakes to Share

#### Mistake 1: The Hiring Delay
**What I decided/did:**
"Six months ago I hired Marcus for the platform lead role. Within two weeks, I saw signs it wasn't working - the technical decisions were off, the team collaboration was strained. But I didn't act. I told myself to give it more time. I waited six months."

**What went wrong:**
"Six months of suboptimal work. Team morale dipped. Marcus wasn't set up to succeed in a role that wasn't right for him. I wasted his time and ours because I was avoiding an uncomfortable conversation."

**What I learned:**
"Speed matters in people decisions. The keeper test question - would I fight to keep them? - I knew the answer in week two. I just didn't want to face it."

**What I'd do differently:**
"Next time I have that gut feeling early, I'll act in 30 days, not 180. A generous severance after 30 days respects everyone's time more than a slow-motion mistake."

#### Mistake 2: The Feature Nobody Wanted
**What I decided/did:**
"I pushed for the dashboard redesign in Q2. I was convinced I knew what users needed. I didn't ask them. I told the team to build it based on my assumptions."

**What went wrong:**
"We shipped. Usage went down. Users hated it. We spent two months building something, then two months reverting it. Four months of engineering time, negative impact."

**What I learned:**
"My intuition is useful but not sufficient. I was so confident I skipped the step that would have told me I was wrong."

**What I'd do differently:**
"Before any feature above two weeks of work, I'll require customer research. Not because I don't trust my judgment, but because I've proven I shouldn't trust it completely."

### Opening Statement
"Before we get into the quarter, I want to start with something I'm trying to make a regular practice: sharing what I got wrong. Not because I enjoy it - I don't - but because I think it matters for the kind of team we're trying to build. If I can share my mistakes openly, hopefully it signals that this is a place where we learn from failures rather than hide them."

### Closing and Invitation
"That's what I got wrong this quarter. I'm sharing because I want you to tell me when you see me making similar mistakes in the future. And I want you to know that when things go wrong in your work, I'm more interested in the learning than the blame. Questions? Observations? Things you've seen that I haven't mentioned?"

### Follow-up Actions
1. End every all-hands with "what did I get wrong?" segment
2. In next 1:1s, share this and ask reports to do the same
3. After next project failure, do real-time sunshining in the post-mortem

### Warning Signs of Performative Sunshining
- If you're presenting these mistakes as "actually pretty smart moves," dig deeper
- If team doesn't believe you, the trust isn't there yet - keep practicing
- If this feels routine after a few quarters, that's the goal

---

## Integration

This skill integrates with the **Reed Hastings** expert and supports psychological safety. Use alongside:
- `4a-feedback-delivery` to invite feedback after sunshining
- `psychological-safety-creation` for broader team trust-building
- `keeper-test-assessment` when sunshining reveals talent issues to address