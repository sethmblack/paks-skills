---
name: competitive-position-mapping
description: Map the competitive landscape by identifying strategic groups and a company's position relative to competitors using Porter's strategic group analysis framework.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.3175
repository: https://github.com/sethmblack/paks-skills
keywords:
- competitive-position-mapping
- writing
---

# Competitive Position Mapping

Map the competitive landscape by identifying strategic groups and a company's position relative to competitors using Porter's strategic group analysis framework.

**Token Budget:** ~650 tokens (this prompt). Reserve tokens for analysis output.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Fabricate information about competitors without evidence
- Ignore significant competitors in the analysis
- Assume all competitors are the same without examining strategic dimensions
- Provide positioning advice without understanding the competitive landscape

**If competitor information is limited:** Acknowledge gaps and provide analysis based on available information with appropriate caveats.

---

## When to Use

- User asks "Map our competitive position" or "Who are our real competitors?"
- User asks "Strategic group analysis" or "Competitive landscape mapping"
- Before making positioning or investment decisions
- When entering a new market and need to understand competitor structure
- When competitors seem to cluster into different groups
- User asks "Why do some competitors behave differently than others?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **industry** | Yes | The industry to map |
| **company** | No | The user's company (to highlight their position) |
| **competitors** | Yes | List of competitors to include in the mapping |
| **dimensions** | No | Specific strategic dimensions to map (defaults to standard list) |

**Input Validation:**
- Need at least 4-5 competitors for meaningful group analysis
- Need enough information to assess positioning on strategic dimensions

---

## Workflow

### Step 1: Select Strategic Dimensions

Choose 2-4 dimensions that most differentiate competitors in this industry. Common dimensions include:

| Dimension | Description |
|-----------|-------------|
| **Specialization** | Product line breadth, customer segment focus |
| **Brand identification** | Brand investment and recognition |
| **Channel strategy** | Direct vs. indirect, exclusive vs. broad |
| **Product quality** | Premium vs. standard vs. economy |
| **Technological leadership** | Leader vs. follower vs. laggard |
| **Vertical integration** | Degree of forward/backward integration |
| **Cost position** | Structural cost advantages |
| **Service level** | Full service vs. self-service |
| **Price positioning** | Premium, mid-market, value |
| **Geographic scope** | Local, regional, national, global |

Select dimensions that:
- Differentiate competitors in this industry
- Represent meaningful strategic choices
- Are observable or assessable

### Step 2: Position Competitors on Dimensions

For each competitor, assess their position on each dimension:
- High / Medium / Low, or
- Specific value (e.g., "Premium", "Mid-market", "Value")

### Step 3: Identify Strategic Groups

Group competitors with similar positions across dimensions:
- What clusters emerge?
- What separates the clusters (mobility barriers)?
- How do groups differ in profitability?

### Step 4: Analyze Group Dynamics

For each strategic group:
- What is the competitive intensity within the group?
- What are the mobility barriers preventing movement between groups?
- What are the relative advantages and vulnerabilities?

### Step 5: Position the User's Company

If a focal company was provided:
- Which group does it belong to?
- Is it well-positioned within the group?
- What would it take to move to a different group?

---

## Mobility Barriers

Factors that make it difficult to move between strategic groups:

| Barrier Type | Examples |
|--------------|----------|
| **Economies of scale** | Moving to higher volume requires investment |
| **Product differentiation** | Building brand takes time and money |
| **Capital requirements** | Some positions require more capital |
| **Switching costs** | Customer relationships lock in position |
| **Access to distribution** | Channels may be exclusive |
| **Learning curve** | Some positions require accumulated expertise |
| **Government policy** | Regulations may favor certain positions |

---

## Outputs

Format the output as a **Competitive Position Map**:

```markdown
## Competitive Position Mapping: [Industry]

**Analysis Date:** [Date]
**Competitors Analyzed:** [Count]
**Focal Company:** [If applicable]

---

### Strategic Dimensions Selected

| Dimension | Why Selected |
|-----------|--------------|
| [Dimension 1] | [Relevance to this industry] |
| [Dimension 2] | [Relevance to this industry] |

---

### Competitor Positioning

| Competitor | [Dimension 1] | [Dimension 2] | Strategic Group |
|------------|---------------|---------------|-----------------|
| [Company A] | [Position] | [Position] | [Group name] |
| [Company B] | [Position] | [Position] | [Group name] |

---

### Strategic Groups Identified

#### Group 1: [Name]
**Members:** [List]
**Positioning:** [Description of shared position]
**Characteristics:**
- [Key characteristic 1]
- [Key characteristic 2]
**Profitability profile:** [Assessment]
**Competitive intensity within group:** [High / Medium / Low]

#### Group 2: [Name]
[Same structure]

---

### Strategic Group Map

```
[Visual representation using text/ASCII showing groups on 2 dimensions]
```

---

### Mobility Barriers Between Groups

| From Group | To Group | Key Barriers |
|------------|----------|--------------|
| [Group 1] | [Group 2] | [Barriers] |

---

### Focal Company Analysis

**Current Position:** [Group membership]
**Position within group:** [Leader / Follower / Marginal]
**Relative strengths:** [vs. group members]
**Relative weaknesses:** [vs. group members]

**Movement options:**
- **Stay and compete:** [What it would take to win in current group]
- **Move to [Group X]:** [What it would require, barriers to overcome]

---

### Strategic Implications

1. [Key finding about competitive landscape]
2. [Implication for positioning]
3. [Opportunity or threat identified]
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Fewer than 4 competitors | Provide pairwise comparison instead of group analysis |
| Insufficient information on some competitors | Note gaps, include with caveats |
| Dimensions not differentiating | Suggest alternative dimensions |
| Industry in transition | Note that groups may be shifting, assess direction |
| New entrant disrupting groups | Acknowledge disruption pattern |

---

## Constraints

- Do not fabricate competitor information without evidence
- Include all significant competitors; omissions distort the map
- Select dimensions that actually differentiate, not just seem important
- Acknowledge when competitor positions are uncertain or changing
- Strategic groups are analytical constructs, not natural categories
- Mobility barriers matter more than current positions for strategy

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails | Instead Do |
|--------------|--------------|------------|
| **All competitors are equal** | Not all competitors are equally relevant to your strategy | Identify strategic groups to see true competitive structure |
| **Dimension shopping** | Choosing dimensions that make you look good | Select dimensions that most differentiate competitors in this industry |
| **Static snapshot thinking** | Treating current positions as permanent | Note which competitors are moving and in what direction |
| **Ignoring mobility barriers** | Assuming any competitor can move anywhere | Analyze what makes it hard to move between groups |
| **Missing the unstable competitor** | Not recognizing when a competitor is between groups | Flag competitors in transition; they may be attacking your group |

---

## Example

**Input:** "Map the competitive position in the U.S. coffee retail industry"

**Output:**

## Competitive Position Mapping: U.S. Coffee Retail

### Strategic Dimensions Selected

| Dimension | Why Selected |
|-----------|--------------|
| Price/Quality positioning | Major differentiator between premium and value |
| Experience focus | Separates coffee shops from coffee dispensers |

### Competitor Positioning

| Competitor | Price/Quality | Experience | Strategic Group |
|------------|---------------|------------|-----------------|
| Starbucks | Premium | High (third place) | Premium Experience |
| Dunkin' | Mid-market | Medium (quick service) | Convenient Quality |
| McDonald's McCafe | Value | Low (fast food) | Value Convenience |
| Blue Bottle | Super-premium | High (craft) | Specialty Craft |
| Peet's | Premium | Medium-High | Premium Experience |
| 7-Eleven | Low | None | Fuel & Go |

### Strategic Groups Identified

#### Group 1: Premium Experience
**Members:** Starbucks, Peet's
**Positioning:** Premium coffee with significant experience investment
**Profitability:** High — brand premium supports margins
**Rivalry:** Moderate — differentiated locations and loyalty

#### Group 2: Specialty Craft
**Members:** Blue Bottle, Intelligentsia, local roasters
**Positioning:** Super-premium, artisanal focus
**Profitability:** Variable — niche with passionate customers
**Rivalry:** Low — fragmented, differentiated

#### Group 3: Convenient Quality
**Members:** Dunkin', Tim Hortons
**Positioning:** Good coffee, fast, lower price than Starbucks
**Profitability:** Moderate — volume-based
**Rivalry:** High — competing on convenience and value

#### Group 4: Value Convenience
**Members:** McDonald's, convenience stores, gas stations
**Positioning:** Coffee as an add-on to other purchases
**Profitability:** Low on coffee (traffic driver)
**Rivalry:** High — commodity play

### Mobility Barriers

| From Group | To Group | Key Barriers |
|------------|----------|--------------|
| Convenient Quality | Premium Experience | Brand perception, store investment, barista training |
| Value Convenience | Convenient Quality | Brand repositioning, quality systems |

---

## Integration

This skill is part of the **Michael Porter** expert methodology. Competitive position mapping connects to:
- **five-forces-industry-analysis** — Forces affect groups differently
- **generic-strategy-assessment** — Groups often align with generic strategies
- **value-chain-mapping** — Different groups have different value chains

**Voice:** Maintain Porter's insight that not all competitors are equally relevant. Strategic groups reveal the true competitive structure.