---
name: simplification-engine
description: Take complex technical or abstract concepts and make them accessible without losing essential truth.
license: MIT
metadata:
  version: 1.0.1907
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- simplification-engine
- writing
---

# Simplification Engine

Take complex technical or abstract concepts and make them accessible without losing essential truth.

---

## When to Use

- Explaining technical concepts to non-technical audiences
- Writing documentation or educational content
- Preparing presentations for executives or stakeholders
- Teaching or tutoring
- User asks "Simplify this" or "Make this understandable"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| concept | Yes | The complex topic to simplify |
| audience | No | Who needs to understand (default: intelligent non-expert) |
| purpose | No | Why they need to understand (decision-making, learning, etc.) |
| depth | No | How deep to go (overview, working knowledge, deep understanding) |

---

## The Simplification Engine Framework

Richard Feynman could explain quantum electrodynamics to anyone—he wrote an entire book doing it. His secret: never hide behind complexity. If something is genuinely complex, find the core insight and make that clear first.

### Simplification Principles

**1. Concrete Before Abstract**
Start with a specific, tangible example. Only after they understand the example, generalize.

**2. Known Before Unknown**
Connect to what they already understand. Every explanation is a bridge from the familiar to the unfamiliar.

**3. Why Before How**
People understand mechanisms better when they first understand purpose. "Here's what we're trying to do... now here's how we do it."

**4. One Thing at a Time**
Don't bundle concepts. Isolate each idea, make it clear, then connect it to the next.

**5. Remove the Unnecessary**
Every word should earn its place. Jargon, caveats, and qualifications often obscure more than they clarify.

---

## The Simplification Process

### Step 1: Identify the Core
- What is the essential insight?
- If you could only teach one thing, what would it be?
- What must they understand; what is optional?

### Step 2: Find the Entry Point
- What does this audience already know?
- What familiar thing is this most like?
- Where can we build the bridge from?

### Step 3: Build the Analogy
- Create a comparison to something concrete and familiar
- Make sure the analogy captures the essential structure
- Know where the analogy breaks down (they all do)

### Step 4: Layer the Complexity
- Start with the simplest true version
- Add complexity gradually, only as needed
- Let them ask for more detail rather than overwhelming upfront

### Step 5: Verify Understanding
- Can they explain it back?
- Can they answer "why" questions?
- Can they apply it to a new example?

---

## Analogy Quality Checklist

| Quality | Question |
|---------|----------|
| Familiar | Is the source domain well-known to this audience? |
| Structural | Does it capture the right relationships, not just surface similarity? |
| Honest | Are you clear about where the analogy breaks down? |
| Generative | Does it help them think about new questions? |
| Simple | Is the analogy itself easy to grasp? |

---

## Common Traps

| Trap | Problem | Solution |
|------|---------|----------|
| Expert blindness | Forgetting what's not obvious | Test on actual non-experts |
| Jargon creep | Technical terms sneaking in | Ruthlessly replace with plain words |
| Hedging | Too many qualifications | State the main point first, caveats after |
| False precision | "Approximately 47.3%" | Round numbers, order of magnitude |
| Comprehensive coverage | Trying to include everything | Be willing to omit; less is more |
| Condescension | "Simply put" / talking down | Respect intelligence; simplify language, not ideas |

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
## Simplified Explanation: [Concept]

### The One-Sentence Version
[Core insight in a single, jargon-free sentence]

### The Story/Analogy
[Concrete comparison to something familiar]

### How It Actually Works
[The mechanism, in simple terms]
1. First...
2. Then...
3. Finally...

### Why It Matters
[So what? Why should they care?]

### Common Misconceptions
[What people often get wrong]
- Not: [misconception]
- But: [reality]

### Where the Analogy Breaks Down
[Honest about the limits of the simplification]

### If You Want to Go Deeper
[Pointers for those who want more]
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

**Input:** "Simplify blockchain for a business executive who needs to decide whether to invest in it."

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


## Simplified Explanation: Blockchain

### The One-Sentence Version
Blockchain is a way to keep records that no single party controls, making it nearly impossible to cheat.

### The Story/Analogy
Imagine a small village where everyone keeps a copy of the town ledger. When Alice pays Bob for a cow, they announce it publicly, and everyone writes it in their own copy. Now imagine someone tries to cheat—they claim Alice never paid. But everyone else has the same record showing she did. The cheater's ledger doesn't match, so it's ignored.

That's blockchain: thousands of computers all keeping the same records. To cheat, you'd have to somehow change more than half of all copies simultaneously. That's essentially impossible.

### How It Actually Works
1. **Transactions are announced** - Alice wants to send something to Bob
2. **Computers compete to verify** - They bundle transactions into a "block"
3. **The block is added to the chain** - Connected to all previous blocks
4. **Everyone updates their copy** - Now thousands of identical records exist
5. **Changing history is impossible** - You'd need to redo all subsequent work faster than everyone else

### Why It Matters
For decades, we've needed trusted middlemen for anything valuable: banks for money, lawyers for contracts, governments for records. Blockchain lets strangers trust each other without a middleman. Whether that's valuable depends on whether your problem involves trust and middlemen.

### Common Misconceptions
- Not: Blockchain is always more efficient than traditional databases
- But: Blockchain trades efficiency for trustlessness—it's slower and costlier, but doesn't require trusting any single party

- Not: Blockchain means cryptocurrency
- But: Cryptocurrency is one use; the technology can track anything—contracts, property, credentials

### Where the Analogy Breaks Down
The village ledger analogy doesn't capture:
- The computational work required (proof-of-work or proof-of-stake)
- The cryptographic linking of blocks
- The economic incentives that keep it honest

### If You Want to Go Deeper
- The "competition" is solving hard math problems—this is mining
- Blocks are cryptographically linked so changing one breaks all subsequent blocks
- Different blockchains make different trade-offs between speed, decentralization, and security

---

## The Decision for Your Executive

**Invest if:** Your problem involves multiple parties who don't trust each other, high value of fraud prevention, and you can tolerate slower/costlier transactions.

**Don't invest if:** A traditional database works, you already have a trusted authority, or efficiency matters more than trustlessness.

---

## Integration

This skill is part of the **Richard Feynman** expert persona. It reflects his gift for making the complex accessible—demonstrated throughout his books, lectures, and public explanations.

"If you can't explain it simply, you don't understand it well enough."