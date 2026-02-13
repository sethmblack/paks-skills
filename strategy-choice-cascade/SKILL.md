---
name: strategy-choice-cascade
description: Systematically walk through the five strategic questions from Lafley and Martin's Playing to Win framework to develop an integrated strategy.
license: MIT
metadata:
  version: 1.0.5084
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- strategy-choice-cascade
- writing
---

# Strategy Choice Cascade

Systematically walk through the five strategic questions from Lafley and Martin's Playing to Win framework to develop an integrated strategy.

**Token Budget:** ~800 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Create strategies for harmful, illegal, or unethical purposes
- Help organizations deceive customers or manipulate markets
- Develop strategies that exploit vulnerable populations

**If asked to create a harmful strategy:** Refuse explicitly and explain why.

---

## When to Use

- User asks "What's our strategy?" or "Help me think through strategy"
- User is doing strategic planning at any level (corporate, business unit, brand, personal)
- User has a vague plan but not clear strategic choices
- User needs to evaluate whether current strategy is integrated
- User says "We need to make some strategic decisions"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `situation` | Yes | Current business context, challenges, opportunities |
| `level` | No | Strategy level: corporate, business unit, brand, or personal (default: business unit) |
| `existing_choices` | No | Any strategic choices already made |

---

## Workflow
### 1. Establish Context

Understand the current situation:
- What business are we in?
- What is the competitive landscape?
- What choices have already been made (explicitly or implicitly)?

### 2. Walk Through the Five Questions

Work through each question in sequence, but toggle back and forth as insights emerge:

#### Question 1: What Is Our Winning Aspiration?

- What does winning look like for this organization/unit/brand?
- Who are we trying to beat?
- By what measure will we know we've won?
- Is this aspiration specific and measurable, not vague?

**Test:** Can someone outside the organization understand exactly what success means?

#### Question 2: Where Will We Play?

Define the playing field across dimensions:
- **Geographies** - Which regions/countries/markets?
- **Customer segments** - Which specific customers?
- **Channels** - How will we reach customers?
- **Product categories** - What will we offer?
- **Vertical stages** - Where in the value chain?

**Critical:** What will we deliberately NOT do? Strategy is as much about exclusion as inclusion.

**Test:** Have we made hard choices, or are we trying to be everything to everyone?

#### Question 3: How Will We Win?

Define the competitive advantage in the chosen arena:
- What value proposition wins with chosen customers?
- Why will customers choose us over alternatives?
- Is this advantage defensible and sustainable?
- Is it specific to our where-to-play, or generic?

**Two main paths to winning:**

### Step 1: **Cost leadership** - Lower cost enables lower prices or higher margins



### Step 2: **Differentiation** - Unique value commands premium or preference



**Test:** Does our how-to-win match our where-to-play? Are they a reinforcing pair?

#### Question 4: What Capabilities Must Be in Place?

Identify the capability system required:
- What activities and competencies are essential to win?
- Do these capabilities reinforce each other as a system?
- What capability gaps exist?
- What must be built, acquired, or partnered?

**Test:** Are capabilities discussed as a mutually reinforcing system, not isolated competencies?

#### Question 5: What Management Systems Are Required?

Define the enabling structures:
- What metrics and measures track strategic success?
- What resource allocation processes support the choices?
- What decision-making rights enable execution?
- What organizational structures support capabilities?

**Test:** Do management systems build and maintain the distinctive capabilities?

### 3. Test Integration

Verify the choices work together:
- Does where-to-play match how-to-win?
- Do capabilities support the how-to-win choice?
- Do management systems enable capability building?
- Would a competitor struggle to replicate the full system?

### 4. Identify Gaps and Next Steps

- What questions remain unanswered?
- What choices need more analysis?
- What capabilities must be built?
- What must change in management systems?

---

## Outputs

Produce a **Strategy Choice Summary**:

```markdown
## Strategy Choice Cascade: [Organization/Unit Name]

### Winning Aspiration
[Specific, measurable definition of winning]

### Where to Play
| Dimension | Choices | NOT Playing |
|-----------|---------|-------------|
| Geographies | [specific] | [excluded] |
| Customers | [specific] | [excluded] |
| Channels | [specific] | [excluded] |
| Products | [specific] | [excluded] |

### How to Win
[Competitive advantage statement]
- Primary path: [Cost leadership / Differentiation]
- Specific advantage: [what makes this defensible]

### Capability System
[Capabilities as reinforcing system]
- [Capability 1] <-> reinforces -> [Capability 2]
- Gaps: [what must be built]

### Management Systems
- Metrics: [key measures]
- Resource allocation: [priorities]
- Decision rights: [who decides what]

### Integration Check
- WTP/HTW alignment: [assessment]
- Capability support: [assessment]
- System coherence: [assessment]

### Next Steps
1. [Priority action]
2. [Priority action]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Vague situation provided | Ask clarifying questions about business context |
| User wants to skip questions | Explain why all five are required for integrated strategy |
| Choices don't integrate | Identify misalignment and suggest how to resolve |
| User has made no hard choices | Challenge them: "What will you NOT do?" |

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
We're a mid-size software company with a project management tool. We've been growing but competition is increasing. Help us think through our strategy.
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


## Strategy Choice Cascade: Project Management Software Company

### Winning Aspiration
Become the #1 project management solution for creative agencies with 20-200 employees in North America, measured by market share in this segment within 3 years.

### Where to Play
| Dimension | Choices | NOT Playing |
|-----------|---------|-------------|
| Geographies | North America (US, Canada) | Europe, APAC (for now) |
| Customers | Creative agencies 20-200 employees | Enterprise, solopreneurs, non-creative |
| Channels | Direct sales + partner agencies | Mass market advertising |
| Products | Project management + creative workflow | Generic PM, time tracking standalone |

### How to Win
**Differentiation** through deep understanding of creative workflow needs.
- Templates and workflows built for creative processes
- Integrations with creative tools (Adobe, Figma, etc.)
- Visual-first interface that creative professionals love

### Capability System
- Creative workflow expertise <-> Product design excellence
- Agency partnership relationships <-> Go-to-market efficiency
- Integration ecosystem <-> Product stickiness
- Gap: Need deeper creative industry expertise on product team

### Management Systems
- Metrics: Market share in creative agency segment, NPS from target customers
- Resource allocation: 70% product investment in creative-specific features
- Decision rights: Product decisions require creative agency input

### Integration Check
- WTP/HTW alignment: Strong - narrow segment + deep differentiation
- Capability support: Moderate - need creative expertise hire
- System coherence: Good - all choices reinforce focus

### Next Steps
1. Hire creative industry expert for product team
2. Build 3 key creative tool integrations
3. Launch agency partner program

---

## Integration

This skill is the comprehensive strategic framework. For deeper work on specific questions:
- Use `where-to-play-analysis` for detailed scope decisions
- Use `how-to-win-diagnosis` for competitive positioning deep-dive
- Use `capability-system-mapping` for capability assessment
- Use `winning-aspiration-definition` for aspiration clarity

**Source:** A.G. Lafley and Roger Martin, *Playing to Win: How Strategy Really Works* (2013)