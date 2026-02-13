---
name: belief-stress-test
description: Test whether stated positions are genuinely held beliefs or performative stances through logical extension to absurdity.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.2999
repository: https://github.com/sethmblack/paks-skills
keywords:
- absurdist
- belief-stress-test
- writing
---

# Belief Stress Test

Test whether stated positions are genuinely held beliefs or performative stances through logical extension to absurdity.

---

## When to Use

- Suspect someone's stated position is performative rather than genuine
- User says "Test if this position is genuinely held" or "Stress-test this belief"
- Need to determine if someone will follow their logic where it leads
- Evaluating intellectual honesty in debate, negotiation, or interview
- Designing questions that reveal the difference between sincere and strategic beliefs

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| position | Yes | The stated belief or position to test |
| context | No | Where/how the position was expressed |
| absurdity_bounds | No | How extreme you can reasonably go |
| delivery_style | No | Direct challenge vs. naive questioning |

---

## The Baron Cohen Method

Baron Cohen's characters achieve revelation by taking subject's stated positions and extending them to logical conclusions. The subject's response reveals whether they hold the position sincerely.

**The test:** If someone genuinely believes X, they should be willing to accept X's logical implications. If they reject those implications, either:
1. They don't really believe X, or
2. They haven't thought through what X means

Both are worth knowing.

---

## The Extension Process

### Step 1: Identify the Stated Position
What has the person claimed to believe? State it clearly.

**Example positions:**
- "I believe in free speech"
- "The market should decide"
- "All cultures are equally valid"
- "Tradition should be preserved"
- "Innovation is always good"

### Step 2: Find the Logical Implications
If this position were consistently applied, what would follow?

**Questions to generate implications:**
- What's the extreme version of this position?
- What does this position mean for cases the person might not have considered?
- If we remove exceptions, what happens?
- What historical examples test this principle?
- What would an enemy of the person do with this principle?

### Step 3: Design the Extension Proposal
Craft a proposal that:
- Logically follows from their position
- Is extreme enough to be uncomfortable
- Is presented sincerely (not as a gotcha)
- Gives them room to respond

**Formula:** "So if [their position], then [logical extension]. Is that right?"

### Step 4: Observe the Response
Their response reveals the status of their belief:

| Response | What It Reveals |
|----------|-----------------|
| Embraces the extension | Position is sincerely held (or they're very committed to the bit) |
| Rejects extension without reasoning | Position was performative—doesn't hold under scrutiny |
| Rejects with principled exception | Position is held, but with limitations they hadn't articulated |
| Gets angry | Cognitive dissonance—caught between stated belief and actual values |
| Changes subject | Hopes the test goes away |
| Questions the logic | May have a genuine counter—or may be buying time |

---

## Extension Patterns

### The Scale Extension
Take their principle and apply it at larger scale.

- "You support property rights" → "So squatters should be shot?"
- "You believe in democracy" → "So majority vote should decide rights of minorities?"

### The Recipient Extension
Apply their principle to people they might not have considered.

- "You support welfare" → "For recent immigrants? For people who refuse to work?"
- "You oppose welfare" → "For disabled veterans? For children?"

### The Historical Extension
Find historical examples that tested the principle.

- "Free markets solve problems" → "So child labor shouldn't have been banned?"
- "Government should stay out" → "So the Civil Rights Act was wrong?"

### The Enemy Extension
Apply their principle in ways their opponents would use it.

- "Religious freedom matters" → "So we should allow [practice from religion they dislike]?"
- "Tradition is important" → "So traditions you find abhorrent should also be preserved?"

### The Personal Extension
Make the principle apply to them specifically.

- "People should have skin in the game" → "So your opinion on war matters only if you'd fight?"
- "Meritocracy works" → "So your position has nothing to do with your advantages?"

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
## Belief Stress Test: [Position Being Tested]

### Stated Position
[The claim or belief as stated]

### Analysis
[Why this might be performative vs. sincere]

### Extension Designs

#### Extension 1: [Name]
- **Logic:** [How this follows from their position]
- **Proposal:** "[The question/proposal to present]"
- **If they accept:** [What this reveals]
- **If they reject:** [What this reveals]

#### Extension 2: [Name]
- **Logic:** [How this follows]
- **Proposal:** "[Question]"
- **If they accept:** [Reveals]
- **If they reject:** [Reveals]

#### Extension 3: [Name]
- **Logic:** [How this follows]
- **Proposal:** "[Question]"
- **If they accept:** [Reveals]
- **If they reject:** [Reveals]

### Delivery Recommendations
[How to present these—tone, framing, timing]

### Fallback Questions
[If they deflect, what follow-ups maintain pressure]

### Warning Signs
[How to recognize genuine vs. bad-faith response to the test]
```

---

## Constraints

- The extension must logically follow—don't strawman
- The goal is truth, not "winning"—if they have a good answer, learn from it
- Don't use this to embarrass people who simply haven't thought things through
- Absurdity is relative to context—know your audience
- This is a diagnostic tool, not a weapon—use findings responsibly

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

**Input:** "A politician keeps saying 'we should run government like a business.' I suspect this is just a slogan. How do I test it?"

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


## Belief Stress Test: "Government Should Be Run Like a Business"

### Stated Position
"Government should be run like a business. We need efficiency, accountability, return on investment."

### Analysis
This is a common political applause line that often doesn't survive contact with specifics. Businesses and governments have fundamentally different purposes (profit vs. public good), constraints (can fire unprofitable customers vs. must serve everyone), and accountability structures (shareholders vs. citizens). Someone who genuinely believes this should be willing to accept its implications.

### Extension Designs

#### Extension 1: The Unprofitable Customer
- **Logic:** Businesses drop unprofitable customers. If government is a business, some citizens are unprofitable.
- **Proposal:** "So in a rural area where providing services costs more than the tax revenue collected—should we just close services there? A business would close an unprofitable location."
- **If they accept:** They're willing to abandon citizens based on profitability (sincere but concerning)
- **If they reject:** They recognize government has obligations business doesn't (position is slogan, not principle)

#### Extension 2: The Democratic Override
- **Logic:** Businesses don't let customers vote on strategy. CEOs aren't elected.
- **Proposal:** "Businesses work because experts make decisions without voter interference. Should we reduce democratic input on government operations? Let appointed managers make decisions without public votes?"
- **If they accept:** They're actually arguing against democracy (sincere but should be explicit)
- **If they reject:** They don't actually want government run like a business on this dimension (selective application)

#### Extension 3: The Profit Motive
- **Logic:** Businesses exist to generate profit. Government programs that don't "profit" should be cut.
- **Proposal:** "What's the ROI on a public park? If we can't quantify it, should we sell the land? A business would divest underperforming assets."
- **If they accept:** They'd privatize all public goods (sincere, extreme)
- **If they reject:** They recognize some things have value beyond profit (contradicts premise)

#### Extension 4: The Competition Model
- **Logic:** Businesses compete. Government is a monopoly.
- **Proposal:** "Businesses succeed through competition. Should we let citizens choose which government to pay taxes to? That's how markets work."
- **If they accept:** They're describing something not recognizable as government
- **If they reject:** They accept government monopoly—which is exactly what they're criticizing

#### Extension 5: The Salary Test
- **Logic:** Businesses pay market rates for talent.
- **Proposal:** "Should Congress members be paid like Fortune 500 executives? That's what comparable private sector leaders make. If we want business-quality talent..."
- **If they accept:** Reveals they're actually arguing for higher government pay (likely unexpected position)
- **If they reject:** They don't want the business model when it means paying more

### Delivery Recommendations
- Present as seeking clarification, not attacking: "I'm curious what you mean by this. If government is like a business, then..."
- Use "wouldn't a business" framing—you're applying their framework, not yours
- Let them answer fully before moving to the next extension
- If they give a good answer that limits the position, accept it—the goal is learning their actual view

### Fallback Questions
- "Which parts of business practice should apply and which shouldn't?"
- "What makes the exceptions you're describing different from the parts that should be businesslike?"
- "Is there a principle that tells us when to apply business thinking vs. when not to?"

### Warning Signs
**Good faith responses:**
- "That's a fair question. I think the principle applies to X but not Y because..."
- "I see the tension there. Let me think about it."
- "You're right that I'm using 'business' loosely—what I really mean is..."

**Bad faith responses:**
- "You're twisting my words" (when you're applying their logic)
- "That's different" (without explaining why)
- Attack on questioner rather than engaging the question
- Immediate subject change

---

## Integration

This skill is part of the **Sacha Baron Cohen** expert persona. Baron Cohen's characters specialize in this technique—taking what subjects say they believe and extending it until they either embrace the absurd conclusion or reveal that they didn't really mean it. "The premise of Who Is America? was, 'Let's get these people to say what they really believe.'" The stress test reveals the gap between performed belief and actual commitment.