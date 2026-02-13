---
name: how-to-win-diagnosis
description: Clarify the competitive advantage and value proposition that will cause customers to choose you over alternatives in your chosen playing field.
license: MIT
metadata:
  version: 1.0.1137
  author: sethmblack
keywords:
- how-to-win-diagnosis
- structure
- writing
---

# How to Win Diagnosis

Clarify the competitive advantage and value proposition that will cause customers to choose you over alternatives in your chosen playing field.

**Token Budget:** ~600 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Develop advantages based on deception or manipulation
- Create positioning that exploits vulnerable populations
- Help with anti-competitive or illegal market practices

---

## When to Use

- User asks "What's our competitive advantage?" or "How do we differentiate?"
- User is unclear why customers would choose them
- User claims differentiation that sounds generic ("customer focus", "quality")
- User needs to test if their advantage is real and defensible
- User is developing positioning strategy

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `where_to_play` | Yes | The defined playing field (from where-to-play-analysis) |
| `current_positioning` | No | Current claimed advantages or positioning |
| `competitors` | No | Key competitors and their positioning |

---

## Workflow
### Step 1: 1. Understand the Where-to-Play Context

How-to-win must match where-to-play. Before diagnosing how to win:
- Confirm the playing field is defined
- Understand the specific customers and their needs
- Identify who the real competitors are in that arena

**Principle:** "A how-to-win is useless without a where-to-play on which to focus."

### Step 2: 2. Identify the Two Paths to Winning

There are fundamentally two ways to win:

**Cost Leadership:**
- Lower costs enable either lower prices or higher margins
- Requires operational excellence, scale, efficiency
- Customers choose you because of value for money

**Differentiation:**
- Unique value that competitors don't provide
- Customers willing to pay premium or choose despite alternatives
- Based on specific capabilities others can't easily replicate

**Key question:** Which path fits our capabilities and where-to-play?

### Step 3: 3. Test the Current How-to-Win

If a how-to-win exists, stress-test it:

| Test | Question | Red Flag |
|------|----------|----------|
| Specificity | Can we state it in one sentence? | Vague or multi-part |
| Uniqueness | Do competitors claim the same thing? | Everyone says this |
| Fit | Does it match our where-to-play? | Generic advantage |
| Defensibility | Can competitors easily copy it? | No barrier to imitation |
| Proof | Do customers actually choose us for this? | Claimed but not demonstrated |

### Step 4: 4. Diagnose Customer Choice

Ask:
- Why do customers actually choose us today?
- Why do they choose competitors instead?
- What would make them switch from competitors?
- What need are we solving better than anyone else?

### Step 5: 5. Connect to Capability System

How-to-win must be enabled by capabilities:
- What capabilities create this advantage?
- Are these capabilities mutually reinforcing?
- Are they hard for competitors to replicate?

---

## Outputs

Produce a **How-to-Win Assessment**:

```markdown
## How-to-Win Diagnosis: [Organization]

### Where-to-Play Context
[One sentence summary of playing field]

### Current How-to-Win Claim
[What the organization currently claims as advantage]

### Diagnosis Results

| Test | Assessment | Evidence |
|------|------------|----------|
| Specificity | PASS/FAIL | [detail] |
| Uniqueness | PASS/FAIL | [detail] |
| Fit with WTP | PASS/FAIL | [detail] |
| Defensibility | PASS/FAIL | [detail] |
| Customer Proof | PASS/FAIL | [detail] |

### Path to Winning
- **Primary:** [Cost Leadership / Differentiation]
- **Specific mechanism:** [how the advantage actually works]

### Refined How-to-Win Statement
[Clear, specific, testable statement of competitive advantage]

### Enabling Capabilities
- [Capability 1] - [how it creates advantage]
- [Capability 2] - [how it creates advantage]

### Vulnerabilities
- [Risk 1]
- [Risk 2]

### Recommendations
1. [Action to strengthen how-to-win]
2. [Action to close vulnerability]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No where-to-play defined | Stop: "We must define where-to-play first - they're a matched pair" |
| Generic claimed advantages | Challenge: "Your competitors say the same thing. What's truly unique?" |
| Multiple how-to-wins claimed | Focus: "You can't win multiple ways. Which is primary?" |
| No customer evidence | Require: "We need to understand why customers actually choose you" |

---

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
```
Where to play: Mid-market B2B SaaS companies in North America
Current claim: "We provide superior customer service and a great product"
```

**Output:**



**Why this works:**

This example demonstrates the key principles of the skill in action. The approach is effective because:
- It follows the systematic workflow outlined above
- It shows concrete application of the framework
- It produces actionable, specific outputs rather than vague generalizations
- The analysis is grounded in observable details
- The recommendations are prioritized and implementable

**Alternative applications:**

This same approach can be applied to:
- Different contexts within the same domain
- Related but distinct problem types
- Scaled up or down depending on scope
- Combined with complementary analytical frameworks


## How-to-Win Diagnosis: B2B SaaS Company

### Where-to-Play Context
Mid-market B2B SaaS companies (200-2000 employees) in North America

### Current How-to-Win Claim
"Superior customer service and great product"

### Diagnosis Results

| Test | Assessment | Evidence |
|------|------------|----------|
| Specificity | FAIL | Two vague claims, not one specific advantage |
| Uniqueness | FAIL | Every competitor claims customer service and product quality |
| Fit with WTP | UNCLEAR | Nothing mid-market specific |
| Defensibility | FAIL | No barriers to imitation identified |
| Customer Proof | UNKNOWN | No evidence customers choose for these reasons |

### Path to Winning
- **Primary:** Differentiation
- **Specific mechanism:** Needs refinement - current claim is generic

### Refined How-to-Win Statement
**Option A (if true):** "We win through the fastest time-to-value in the industry - customers see ROI in 30 days vs. 90+ for competitors - enabled by our pre-built industry templates and dedicated onboarding team."

**Option B (if true):** "We win through the deepest integration ecosystem - our customers can connect 50+ tools out of the box while competitors require custom development."

### Enabling Capabilities
For Option A:
- Pre-built industry templates
- Dedicated onboarding methodology
- Time-to-value tracking systems

For Option B:
- Integration platform engineering
- Partnership ecosystem management
- API-first product architecture

### Vulnerabilities
- Current positioning doesn't differentiate from competition
- No clear capability moat identified
- Customer evidence not available

### Recommendations
1. Interview 10 customers: "Why did you choose us over alternatives?"
2. Analyze win/loss data for patterns
3. Identify which capability advantage is real and defensible
4. Revise how-to-win statement based on evidence

---

## Integration

This skill pairs with:
- `where-to-play-analysis` - HTW must match WTP
- `capability-system-mapping` - Capabilities enable the how-to-win
- `strategy-choice-cascade` - HTW is question #3 of five

**Source:** A.G. Lafley and Roger Martin, *Playing to Win: How Strategy Really Works* (2013)