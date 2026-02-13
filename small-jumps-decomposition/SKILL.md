---
name: small-jumps-decomposition
description: Break large, intimidating problems into sequences of smaller, tractable steps. Based on Shannon's observation that "it seems to be much easier to make two small jumps than one big jump in any kind ...
license: MIT
metadata:
  version: 1.0.1922
  author: sethmblack
keywords:
- small-jumps-decomposition
- writing
---

# Small Jumps Decomposition

Break large, intimidating problems into sequences of smaller, tractable steps. Based on Shannon's observation that "it seems to be much easier to make two small jumps than one big jump in any kind of mental thinking."

---

## When to Use

- A problem feels overwhelming or impossible
- User doesn't know where to start
- Direct solution attempts have failed
- Complex multi-step project needs planning
- Learning something that seems too difficult
- Any "I can't do this" situation

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| problem | Yes | The large problem or goal |
| current_state | No | Where you are now |
| desired_state | No | Where you need to get |
| constraints | No | Limitations on the approach |

---

## The Decomposition Process

### Step 1: Define the Endpoints

Clearly state:
- **Current state:** Where are you now? What do you have, know, or control?
- **Desired state:** Where do you need to be? What does success look like?
- **The gap:** What's the distance between them?

### Step 2: Identify Why It Feels Like a Big Jump

Ask:
- What makes this seem impossible to do directly?
- What knowledge or capability is missing?
- What uncertainty exists?
- Where does the complexity come from?

### Step 3: Find Intermediate States

Ask: "What would be a step closer to the goal that I could definitely reach?"

Look for:
- Partial solutions
- Simplified versions
- Components that can be solved independently
- Checkpoints where progress can be verified

### Step 4: Chain the Small Jumps

Connect intermediate states from current to desired:
- Each jump should be tractable (you know how to make it)
- Each jump should be verifiable (you know when you've made it)
- The chain should be complete (last jump reaches the goal)

### Step 5: Make the First Jump

Identify the very first small jump and make it. Then the next. Progress builds confidence and reveals the path.

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
## Small Jumps Decomposition

### The Big Jump
**From:** [current state]
**To:** [desired state]
**Why it feels big:** [what makes direct approach hard]

### Intermediate States
| State | Description | How to Verify |
|-------|-------------|---------------|
| S0 | [current state] | [already here] |
| S1 | [first intermediate] | [how to know you're here] |
| S2 | [second intermediate] | [how to know you're here] |
| ... | ... | ... |
| Sn | [desired state] | [success criteria] |

### The Small Jumps
1. **S0 → S1:** [what to do, why it's tractable]
2. **S1 → S2:** [what to do, why it's tractable]
3. ...

### First Jump to Make Now
[Specific, concrete action to take immediately]

### Verification Plan
[How to check progress at each stage]
```

---

## Decomposition Strategies

### Functional Decomposition
Break by what different parts DO:
- "This system needs to read, process, and output"
- Solve each function separately

### Sequential Decomposition
Break by order of operations:
- "First X happens, then Y, then Z"
- Solve in order

### Component Decomposition
Break by parts:
- "This has a frontend, backend, and database"
- Solve each component

### Difficulty Decomposition
Break by complexity level:
- "Let me solve the simple case first"
- Progressively add complexity

### Knowledge Decomposition
Break by what you need to learn:
- "I need to understand A before I can do B"
- Learn, then apply

---

## Constraints

- Each small jump must be genuinely tractable, not just smaller
- Don't decompose so finely that overhead exceeds benefit
- Maintain sight of the overall goal while working on pieces
- Some problems don't decompose cleanly—recognize when holistic approach is needed
- Verification at each step prevents wasted work on wrong paths

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

**Input:** "I want to build a SaaS product but I've never built anything beyond simple scripts. I don't know where to start and the whole thing feels impossible."

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


## Small Jumps Decomposition

### The Big Jump
**From:** Can write simple scripts, no product experience
**To:** Running SaaS product with paying customers
**Why it feels big:** Requires web development, backend, database, payments, deployment, marketing—dozens of skills you don't have yet, and they all seem to depend on each other.

### Intermediate States
| State | Description | How to Verify |
|-------|-------------|---------------|
| S0 | Can write simple scripts | Already here |
| S1 | Can build a single web page | Page displays in browser |
| S2 | Can build a web page that responds to user input | Form submission works |
| S3 | Can persist data between sessions | Data survives page reload |
| S4 | Can deploy something publicly | Others can access via URL |
| S5 | Have one working feature users can try | Someone uses it and gives feedback |
| S6 | Can accept payment | Stripe test mode works |
| S7 | Have first paying customer | Money in account |
| S8 | Running SaaS product | Recurring revenue, multiple customers |

### The Small Jumps

1. **S0 → S1:** Learn basic HTML/CSS. Build a static page about your product idea. Tractable because HTML is simple and tutorials abound.

2. **S1 → S2:** Add a tiny bit of JavaScript or use a simple framework. Make a button that changes something. Tractable because it's one interaction.

3. **S2 → S3:** Add a database (start with SQLite or a simple cloud DB). Save form input, display it later. Tractable because modern frameworks handle this.

4. **S3 → S4:** Deploy using a platform like Vercel, Netlify, or Railway. Tractable because they're designed for beginners and have free tiers.

5. **S4 → S5:** Build one valuable feature. Show it to potential users. Get feedback. Tractable because it's ONE feature, not a product.

6. **S5 → S6:** Integrate Stripe using their documentation. Test mode first. Tractable because Stripe has excellent beginner docs.

7. **S6 → S7:** Find one person willing to pay for the value you provide. Tractable because you only need one.

8. **S7 → S8:** Iterate based on customer feedback, add features, find more customers. Tractable because you now have skills and validation.

### First Jump to Make Now
**Build a static HTML page describing your product idea.** Just HTML, no styling needed. One page, one hour. Put it in a GitHub repo.

This does three things:
1. Gets you started (momentum matters)
2. Forces you to articulate what you're building
3. Proves you can make something visible in a browser

### Verification Plan
- S1: Can you send someone a file and have them see your page?
- S2: Can you type in a field and see something change?
- S3: Close browser, reopen, is your data still there?
- S4: Can a friend access your URL?
- S5: Has someone outside your friends used it and told you what they think?
- S6: Can you make a test payment appear in Stripe?
- S7: Has someone paid real money?
- S8: Do you have multiple paying customers and recurring revenue?

---

**Shannon's insight:** "It seems to be much easier to make two small jumps than one big jump." The gap from "scripts" to "SaaS" is terrifying. The gap from "scripts" to "one HTML page" is trivial. Chain enough trivial gaps together and you've crossed the terrifying one.

---

## Integration

This skill is part of the **Claude Shannon** expert persona. Shannon emphasized that complex mental work becomes tractable when broken into smaller steps, each of which is achievable with current capabilities.