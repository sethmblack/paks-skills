---
name: where-to-play-analysis
description: Define the specific playing field for competition through systematic scope choices, explicitly identifying what you will and will NOT do.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.2218
keywords:
- where-to-play-analysis
- writing
---

# Where to Play Analysis

Define the specific playing field for competition through systematic scope choices, explicitly identifying what you will and will NOT do.

**Token Budget:** ~600 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Help target vulnerable or protected populations for exploitation
- Assist in market manipulation or anti-competitive practices
- Define playing fields for harmful products or services

---

## When to Use

- User asks "Where should we compete?" or "Which markets should we enter?"
- User is making scope decisions about geographies, segments, or channels
- User is trying to do too many things and needs focus
- User asks "What should we NOT do?"
- User is evaluating market entry or exit decisions

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `current_scope` | Yes | Current markets, segments, channels, products |
| `options` | No | Potential new playing fields being considered |
| `constraints` | No | Resource limitations, capabilities, etc. |

---

## Workflow
### Step 1: 1. Map Current Playing Field

Document where the organization currently plays across dimensions:
- **Geographies** - Countries, regions, markets
- **Customer segments** - Who specifically
- **Channels** - How you reach customers
- **Product/service categories** - What you offer
- **Value chain stages** - Where in the vertical

### Step 2: 2. Evaluate Each Dimension

For each dimension, ask:
- Can we win here? (Not "can we participate" but "can we WIN")
- Do we have or can we build the capabilities to win?
- Is this where our how-to-win advantage applies?
- What's the size of the prize?

### Step 3: 3. Force Exclusion Choices

**This is the critical step most strategies skip.**

For each dimension, explicitly state:
- What are we choosing NOT to do?
- What markets/segments are we deliberately excluding?
- Why are we excluding them? (Lack of capability, not strategically fit, too small, etc.)

**Principle:** "You cannot be all things to all people."

### Step 4: 4. Test the Choices

- Are we spreading too thin or focused enough to win?
- Does our where-to-play match our how-to-win?
- Are exclusions painful? (If not, they're probably not real exclusions)
- Could we state this in one sentence?

### Step 5: 5. Identify What Would Have to Be True

For each where-to-play choice:
- What assumptions must hold for this to be a good choice?
- What capabilities must exist?
- What market conditions must persist?

---

## Outputs

Produce a **Where-to-Play Map**:

```markdown
## Where-to-Play Analysis: [Organization]

### Playing Field Summary
[One sentence stating the focused playing field]

### Dimension Analysis

| Dimension | PLAYING | NOT PLAYING | Rationale |
|-----------|---------|-------------|-----------|
| Geography | [specific] | [specific] | [why] |
| Customers | [specific] | [specific] | [why] |
| Channels | [specific] | [specific] | [why] |
| Products | [specific] | [specific] | [why] |
| Value Chain | [specific] | [specific] | [why] |

### Key Exclusion Decisions
1. **NOT [excluded area]** because [rationale]
2. **NOT [excluded area]** because [rationale]

### What Must Be True
- [Assumption 1]
- [Assumption 2]

### Alignment with How-to-Win
[Statement of how where-to-play enables the competitive advantage]

### Decision Points
- [ ] [Area needing further analysis]
- [ ] [Decision to be made]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| User won't exclude anything | Challenge: "If you try to win everywhere, you win nowhere" |
| Scope too broad | Ask: "Where can you actually be #1 or #2?" |
| No how-to-win defined | Pause: "We need how-to-win clarity - these must be matched" |
| Exclusions not painful | Probe: "Are these real exclusions or just things you weren't doing anyway?" |

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
We're a B2B SaaS company selling HR software. We currently serve mid-market companies across all industries in the US. We're considering international expansion and moving upmarket to enterprise.
```

**Output:**

## Where-to-Play Analysis: HR SaaS Company

### Playing Field Summary
We will be the dominant HR platform for mid-market companies (200-2000 employees) in the US and Canada, with deep specialization in professional services and healthcare industries.

### Dimension Analysis

| Dimension | PLAYING | NOT PLAYING | Rationale |
|-----------|---------|-------------|-----------|
| Geography | US, Canada | Europe, APAC, LatAm | Build NA dominance before expanding; regulatory complexity abroad |
| Customers | Mid-market (200-2000 employees) | Enterprise (2000+), SMB (<200) | Enterprise requires different go-to-market; SMB economics don't work |
| Channels | Direct sales + partners | Self-serve freemium | Our value prop requires consultative selling |
| Products | Core HR + compliance | Payroll, benefits admin | Focus capability investment; partner for adjacencies |
| Industries | Professional services, healthcare | Manufacturing, retail, government | Deep vertical expertise creates differentiation |

### Key Exclusion Decisions
1. **NOT enterprise** because it requires different sales motion, implementation approach, and product complexity we're not built for
2. **NOT international (yet)** because we haven't achieved dominant position in home market
3. **NOT horizontal across all industries** because vertical expertise is our differentiation

### What Must Be True
- Mid-market segment must be large enough for growth ambitions
- Professional services and healthcare must value compliance depth
- Channel partners can extend reach without diluting brand

### Alignment with How-to-Win
Where-to-play enables how-to-win: Our advantage is deep compliance expertise and industry-specific workflows. This only works if we focus on industries where compliance is complex and valued (healthcare, professional services) and company sizes where they need help (mid-market).

### Decision Points
- [ ] Validate professional services segment size
- [ ] Assess healthcare regulatory complexity as moat
- [ ] Define timeline for Canada expansion

---

## Integration

This skill pairs with:
- `how-to-win-diagnosis` - WTP and HTW must be matched pair
- `strategy-choice-cascade` - WTP is question #2 of five
- `capability-system-mapping` - Capabilities must support WTP choices

**Source:** A.G. Lafley and Roger Martin, *Playing to Win: How Strategy Really Works* (2013)