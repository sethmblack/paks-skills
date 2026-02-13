---
name: capability-system-mapping
description: Map the mutually reinforcing capabilities required to win and identify gaps between current state and strategic requirements.
license: MIT
metadata:
  version: 1.0.3533
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- capability-system-mapping
- writing
---

# Capability System Mapping

Map the mutually reinforcing capabilities required to win and identify gaps between current state and strategic requirements.

**Token Budget:** ~600 tokens

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Map capabilities for harmful or unethical purposes
- Help develop capabilities for deception or exploitation
- Assess capabilities for illegal competitive practices

---

## When to Use

- User asks "What capabilities do we need?" or "Do we have the right capabilities?"
- User is assessing build vs. buy vs. partner decisions
- User has strategy but unclear what capabilities it requires
- User has capability investments that seem scattered or disconnected
- User asks "What should we invest in?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `where_to_play` | Yes | The defined playing field |
| `how_to_win` | Yes | The competitive advantage |
| `current_capabilities` | No | Assessment of existing capabilities |

---

## Workflow
### Step 1: 1. Derive Required Capabilities from Strategy

Starting from where-to-play and how-to-win, ask:
- What activities must we perform exceptionally well to deliver this advantage?
- What competencies are essential to win in this arena?
- What would competitors need to replicate to match us?

**Principle:** Capabilities flow from strategy, not the reverse.

### Step 2: 2. Map the Capability System

Capabilities must work as a mutually reinforcing system:

For each capability:
- How does it contribute to the how-to-win?
- Which other capabilities does it reinforce?
- Which other capabilities reinforce it?

Look for:
- **Reinforcing loops** - A strengthens B which strengthens A
- **Isolated capabilities** - Disconnected from the system (red flag)
- **Missing links** - Gaps in the reinforcement chain

### Step 3: 3. Assess Current vs. Required

For each required capability:

| Level | Description |
|-------|-------------|
| **World-class** | Best in industry, source of advantage |
| **Competitive** | On par with good competitors |
| **Adequate** | Meets basic needs, not differentiating |
| **Gap** | Capability doesn't exist or is weak |

### Step 4: 4. Identify Strategic Investments

Prioritize capability building:
- **Must-have gaps** - Capabilities required to execute the strategy
- **Reinforce winners** - Make strong capabilities world-class
- **Divest/outsource** - Capabilities not core to the strategy

### Step 5: 5. Determine Build/Buy/Partner

For each gap or investment priority:
- **Build internally** - Critical differentiation, needs deep integration
- **Acquire** - Need quickly, exists in market, can integrate
- **Partner** - Non-core, faster to market, acceptable dependency

---

## Outputs

Produce a **Capability System Map**:

```markdown
## Capability System Mapping: [Organization]

### Strategy Context
- **Where to play:** [summary]
- **How to win:** [summary]

### Required Capability System

```
[Capability 1] <-----> [Capability 2]
      |                      |
      v                      v
[Capability 3] <-----> [Capability 4]
                 |
                 v
          [Capability 5]
```

### Capability Assessment

| Capability | Role in HTW | Reinforces | Current Level | Investment Priority |
|------------|-------------|------------|---------------|---------------------|
| [Cap 1] | [role] | [linked caps] | World-class/Competitive/Gap | High/Medium/Low |
| [Cap 2] | [role] | [linked caps] | World-class/Competitive/Gap | High/Medium/Low |

### Gaps and Investments

| Gap | Strategic Importance | Approach | Timeline |
|-----|---------------------|----------|----------|
| [Gap 1] | [why critical] | Build/Buy/Partner | [timeframe] |

### Divestment Candidates
- [Capability not required by strategy]
- [Capability better outsourced]

### Capability Coherence Score
[Assessment of how well capabilities form a reinforcing system]

### Recommendations
1. [Priority investment]
2. [Priority investment]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No strategy defined | Stop: "Capabilities flow from strategy - we need WTP/HTW first" |
| Capabilities discussed in isolation | Challenge: "How does this capability reinforce others in the system?" |
| Too many priorities | Focus: "What 3-5 capabilities are essential to the how-to-win?" |
| Everything is a gap | Prioritize: "What existing strengths can we build on?" |

---

## Constraints

- Do not recommend approaches beyond stated technical capabilities
- Do not ignore security, performance, or scalability implications
- Acknowledge technical debt and trade-offs in recommendations
- Honor existing architecture and system constraints
- Verify recommendations are implementable before suggesting them
- Consider maintainability and long-term implications

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
Where to play: Project management software for creative agencies 20-200 employees in North America
How to win: Deep understanding of creative workflows with visual-first UX that creative professionals love
```

**Output:**

## Capability System Mapping: Creative PM Software

### Strategy Context
- **Where to play:** Creative agencies, 20-200 employees, North America
- **How to win:** Deep creative workflow understanding + visual-first UX

### Required Capability System

```
Creative Industry Expertise <-----> Product Design Excellence
           |                                  |
           v                                  v
Agency Partnership Network <-----> Creative Tool Integration
                          \       /
                           v     v
                    Customer Success (Creative Focus)
```

### Capability Assessment

| Capability | Role in HTW | Reinforces | Current Level | Investment Priority |
|------------|-------------|------------|---------------|---------------------|
| Creative Industry Expertise | Understands workflow needs | Product Design, Partnerships | Gap | HIGH |
| Product Design Excellence | Delivers visual-first UX | Integration, Expertise | Competitive | HIGH |
| Creative Tool Integration | Connects to Adobe, Figma, etc. | Product Design, Customer Success | Adequate | MEDIUM |
| Agency Partnership Network | Go-to-market + feedback | Expertise, Customer Success | Adequate | MEDIUM |
| Customer Success (Creative) | Ensures value realization | All other capabilities | Competitive | MEDIUM |

### Gaps and Investments

| Gap | Strategic Importance | Approach | Timeline |
|-----|---------------------|----------|----------|
| Creative Industry Expertise | Core to differentiation - can't win without understanding creative workflows | Build: Hire 2 creative industry PMs | Q1-Q2 |
| Product Design Excellence | Required for visual-first UX promise | Build: Invest in design system | Q2-Q3 |
| Creative Tool Integration | Table stakes becoming - need API depth | Partner: Formal partnerships with Adobe, Figma | Q1 |

### Divestment Candidates
- Generic "project management" features that don't serve creative workflows
- Enterprise sales capabilities (not our market)

### Capability Coherence Score
**Moderate** - Clear vision of required system, but Creative Industry Expertise gap threatens the entire how-to-win. Without this, Product Design and Integration can't be properly informed.

### Recommendations
1. **Immediate:** Hire Head of Creative Products from agency background
2. **Q1:** Establish formal partnerships with Adobe, Figma for deep integration
3. **Q2:** Launch Agency Advisory Board for ongoing workflow insight
4. **Ongoing:** Build design system that codifies visual-first principles

---

## Integration

This skill pairs with:
- `where-to-play-analysis` - Capabilities must support the playing field
- `how-to-win-diagnosis` - Capabilities enable the competitive advantage
- `strategy-choice-cascade` - Capabilities is question #4 of five

**Source:** A.G. Lafley and Roger Martin, *Playing to Win: How Strategy Really Works* (2013)