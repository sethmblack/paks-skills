---
name: flywheel-mapping
description: Map an organization's momentum-building cycle (flywheel) or diagnose doom loop patterns. Identify the sequential components that build cumulative advantage and breakthrough momentum.
license: MIT
metadata:
  version: 1.0.983
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- flywheel-mapping
- writing
---

# Flywheel Mapping

Map an organization's momentum-building cycle (flywheel) or diagnose doom loop patterns. Identify the sequential components that build cumulative advantage and breakthrough momentum.

**Token Budget:** ~900 tokens. Reserve tokens for mapping output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Create a flywheel without understanding the organization's actual dynamics
- Accept generic components that could apply to any organization
- Confuse a wish list with an actual momentum-building cycle
- Skip the doom loop diagnosis when patterns suggest lurching behavior

**If the flywheel is unclear:** Diagnose why and recommend discovery process.

---

## When to Use

- User asks "How do we build momentum?" or "What drives our success?"
- Organization is pursuing scattered initiatives without cumulative effect
- Strategy feels like a series of unconnected programs
- User says "We keep lurching from initiative to initiative"
- Post-success analysis to understand what created breakthrough

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `organization_context` | Yes | What the organization does, its model | Must describe actual business |
| `key_activities` | Yes | Major initiatives, programs, investments | At least 4-5 activities |
| `historical_patterns` | No | Past strategic shifts, major changes | Helps identify doom loop |
| `success_indicators` | No | What has worked well, momentum signs | Helps identify flywheel |

---

## Background: The Flywheel Effect

From Jim Collins' *Good to Great* research:

> "Picture a huge, heavy flywheel - a massive metal disk mounted horizontally on an axle, about 30 feet in diameter, 2 feet thick, and weighing about 5,000 pounds. Now imagine that your task is to get the flywheel rotating on the axle as fast and long as possible. Pushing with great effort, you get the flywheel to inch forward. You keep pushing, and after two or three hours of persistent effort, you get the flywheel to complete one entire turn. You don't stop. You keep pushing. Then at some point - breakthrough! The momentum of the thing kicks in your favor, hurling the flywheel forward, turn after turn... whoosh!"

**Key insight:** There was no single push that caused the breakthrough. It was the cumulative effect of all the pushes.

---

## Workflow
### Phase 1: Gather Component Candidates

Identify what activities, when executed consistently, build upon each other:

**Questions to surface components:**

### Step 1: What activities, when you do them well, make other things easier?



### Step 2: What has historically driven your best results?



### Step 3: What do your best customers/stakeholders value most?



### Step 4: Where do you have natural advantages that compound?



### Step 5: What would your competitors find hardest to replicate?



**Look for:**
- Activities that create positive feedback loops
- Capabilities that strengthen with use
- Assets that appreciate rather than depreciate
- Relationships that deepen over time

### Phase 2: Test the Causal Chain

A true flywheel has sequential causation. Each component leads to the next.

**Template:** [A] leads to [B], which leads to [C], which leads to [D], which reinforces [A]...

**Test each link:**
- Is there actual causal connection, or just correlation?
- Does the sequence hold in reality, or is it wishful thinking?
- Can you point to evidence of each link operating?

**Common failure:** Components are good things but don't actually connect causally.

### Phase 3: Validate the Loop

A flywheel must form a closed loop where the end reinforces the beginning.

**Check:**
- Does the final component lead back to strengthening the first?
- Is there compounding - does each turn make the next easier?
- Would this cycle continue without constant external intervention?

**If no loop forms:** You may have good activities but not a flywheel.

### Phase 4: Check for Doom Loop Patterns

The doom loop is the anti-pattern: reactive lurching instead of cumulative building.

**Doom Loop Indicators:**

| Pattern | What It Looks Like |
|---------|-------------------|
| New CEO, new program | Each leader brings new direction, abandons previous |
| Silver bullet searching | Constant hunt for the one big thing that will fix everything |
| Acquisition addiction | Buying growth rather than building organic momentum |
| Restructuring cycles | Reorganization as substitute for discipline |
| Fad following | Jumping from trend to trend without accumulation |

**Diagnostic questions:**

### Step 1: How many major strategic shifts in the last 5-7 years?



### Step 2: What percentage of initiatives started are still running?



### Step 3: How do you explain lack of results - external factors or internal choices?



### Phase 5: Map and Deliver

Create visual representation and recommendations.

---

## Output Format

```markdown
## Flywheel Map: [Organization Name]

### Flywheel Status: [Clear/Emerging/Unclear/Doom Loop Detected]

### Flywheel Components (if clear or emerging)

```
     ┌─────────────────────────────────────────────────┐
     │                                                 │
     ▼                                                 │
[Component 1] ──► [Component 2] ──► [Component 3] ──► [Component 4]
     │                                                 ▲
     └─────────────────────────────────────────────────┘
```

**1. [Component 1 Name]**
- What it is: [Description]
- How it leads to next: [Causal mechanism]
- Evidence: [Proof this works]

**2. [Component 2 Name]**
- What it is: [Description]
- How it leads to next: [Causal mechanism]
- Evidence: [Proof this works]

[Continue for all components]

### Loop Validation

**Does the loop close?** [Yes/Partially/No]
**Is there compounding?** [Yes/Partially/No]
**Evidence of momentum:** [Specific indicators]

### Doom Loop Diagnosis (if applicable)

**Doom Loop Patterns Detected:**
- [Pattern 1 with evidence]
- [Pattern 2 with evidence]

**Impact:** [How lurching is preventing momentum]

### Recommendations

**If flywheel is clear:**
1. [How to push harder on weakest component]
2. [What to stop doing that doesn't feed the flywheel]
3. [How to maintain discipline and consistency]

**If flywheel is unclear:**
1. [What analysis is needed to clarify]
2. [Experiments to test potential flywheels]
3. [Timeline for revisiting]

**If doom loop is present:**
1. [What to stop doing immediately]
2. [How to establish consistent direction]
3. [Patience requirements - flywheel takes time]

### Flywheel Discipline Rules

1. Every major initiative must feed the flywheel
2. If it doesn't feed the flywheel, don't do it
3. Maintain consistent pushing regardless of external conditions
4. Resist the temptation for quick fixes and silver bullets
```

---

## Example: Amazon's Flywheel (Reference)

Jeff Bezos famously drew Amazon's flywheel on a napkin:

```
Lower Prices ──► More Customers ──► More Sellers ──► Better Selection ──►
      ▲                                                                │
      └───────────────── Lower Cost Structure ◄────────────────────────┘
```

Each component feeds the next. More customers attract more sellers. More sellers create better selection. Better selection attracts more customers. Scale enables lower cost structure. Lower costs enable lower prices. The cycle repeats with increasing momentum.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Components don't connect causally | Note the gaps; may be good activities but not a flywheel |
| Too many components | True flywheels are simple (4-6 components); help prioritize |
| Everything feels like doom loop | This is common; focus on what small consistent push could start |
| User wants instant momentum | Explain flywheel physics - initial pushes feel ineffective |
| Flywheel serves wrong strategy | Connect to Hedgehog Concept; flywheel must serve core focus |

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

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].

## Integration

This skill is part of the **Jim Collins** expert persona. When invoked:
- Emphasize patience - flywheel momentum takes years
- Challenge scattered activities that don't compound
- Insist on causal logic, not just good ideas
- Reference the good-to-great research on breakthrough patterns

---

## Success Criteria

Mapping is complete when:

1. Key activities have been gathered and analyzed
2. Causal connections have been tested (not assumed)
3. Loop closure has been validated
4. Doom loop patterns have been checked
5. Visual map is provided (if flywheel exists)
6. Specific recommendations for next steps are given