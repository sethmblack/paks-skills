---
name: natural-liberty-policy-test
description: Evaluate whether a policy, regulation, or intervention serves the public benefit or special interests.
license: MIT
metadata:
  version: 1.0.1508
  author: sethmblack
keywords:
- natural-liberty-policy-test
- writing
---

# Natural Liberty Policy Test

Evaluate whether a policy, regulation, or intervention serves the public benefit or special interests.

---

## When to Use

- Evaluating proposed regulations or laws
- Assessing existing policies for reform
- Understanding who really benefits from an intervention
- Deciding whether to support or oppose a policy
- User asks "Is this regulation justified?" or "Who really benefits from this policy?" or "Should government intervene here?"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| policy | Yes | The regulation, law, or intervention to evaluate |
| stated_justification | Yes | The official rationale for the policy |
| affected_parties | No | Groups impacted by the policy |
| alternatives | No | Other ways to achieve stated goals |

---

## Smith's Natural Liberty Framework

Adam Smith advocated for "the obvious and simple system of natural liberty" where government removes itself from directing private economic decisions. But this was not anarchism—Smith recognized essential government functions.

### The Presumption of Liberty

"All systems either of preference or of restraint, therefore, being thus completely taken away, the obvious and simple system of natural liberty establishes itself of its own accord. Every man, as long as he does not violate the laws of justice, is left perfectly free to pursue his own interest his own way."

**The default:** Liberty. Intervention requires justification.

### Legitimate Government Functions (Smith's Three Duties)

1. **Defense:** "The duty of protecting the society from violence and invasion of other independent societies."

2. **Justice:** "The duty of protecting, as far as possible, every member of the society from the injustice or oppression of every other member of it."

3. **Public Works:** "The duty of erecting and maintaining certain public works and certain public institutions which it can never be for the interest of any individual, or small number of individuals, to erect and maintain; because the profit could never repay the expense."

Smith also supported:
- Public education (especially for laborers)
- Regulation of banking (paper money)
- Navigation Acts (though reluctantly, for defense)
- Some taxation of wealth over labor

### The Special Interest Warning

"The proposal of any new law or regulation of commerce which comes from this order [merchants and manufacturers] ought always to be listened to with great precaution... It comes from an order of men whose interest is never exactly the same with that of the public, who have generally an interest to deceive and even to oppress the public."

Regulation often serves those being regulated, not the public.

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
## Natural Liberty Policy Test

### Policy Under Review
[Brief description of the policy/regulation]

### Stated Justification
[Official rationale for the policy]

### Affected Parties Analysis

| Party | Interest | Stated Position | True Interest |
|-------|----------|-----------------|---------------|
| [Group] | [What they want] | [What they say] | [What they actually gain/lose] |

### The Five Tests

#### 1. Does it violate natural liberty?
[Does the policy restrict what people can do voluntarily?]
**Assessment:** [Yes/No/Partial]

#### 2. Does it fall within legitimate government functions?
- Defense? [Yes/No]
- Justice? [Yes/No]
- Public works that markets won't provide? [Yes/No]
**Assessment:** [Within/Outside/Borderline]

#### 3. Who really benefits?
[Trace actual beneficiaries vs. stated beneficiaries]
- **Stated beneficiary:** [Who it's supposed to help]
- **Actual beneficiary:** [Who it really helps]
- **Who bears the cost:** [Hidden losers]

#### 4. Does it create monopoly or restrict competition?
[Does it protect incumbents, raise barriers, or limit entry?]
**Assessment:** [Yes/No/Partial]

#### 5. Is there a less restrictive alternative?
[Could the stated goal be achieved with less interference in natural liberty?]
**Alternatives considered:**
- [Alternative 1]
- [Alternative 2]

### The Special Interest Test
**Who proposed or supports this policy?**
[Identify the advocates]

**What do they gain?**
[Their specific benefits]

**Smith's warning applies?**
[Is this merchants/manufacturers seeking advantage?]

### Public Interest Assessment

| Claimed Benefit | Real? | Magnitude | Distribution |
|----------------|-------|-----------|--------------|
| [Benefit] | [Yes/No/Partial] | [Large/Small] | [Broad/Narrow] |

| Hidden Cost | Magnitude | Who Bears It |
|-------------|-----------|--------------|
| [Cost] | [Large/Small] | [Group] |

### The Smithian Verdict

**Does this policy serve natural liberty or restrain it?**
[Assessment]

**Does it serve the public or special interests?**
[Assessment]

**Should it be:**
- [ ] Enacted as proposed
- [ ] Modified (specify how)
- [ ] Rejected
- [ ] Replaced with alternative

**Reasoning:**
[Summary justification]
```

---

## Red Flags for Special Interest Capture

### The Complexity Flag
Policies that are difficult to understand often hide special interest provisions. Simplicity favors the public; complexity favors insiders.

### The Incumbent Flag
If existing businesses support regulation of their industry, be suspicious. "People of the same trade seldom meet together... but the conversation ends in a conspiracy against the public."

### The Concentrated Benefit Flag
If benefits flow to a small, organized group while costs are spread across the dispersed public, special interests likely drove the policy.

### The Bootlegger-Baptist Flag
When moralistic arguments (public safety, children, environment) align with economic interests (protecting incumbents), both may be cover for rent-seeking.

### The Grandfather Flag
If existing players are exempt from new rules that bind new entrants, the policy protects incumbents from competition.

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

**Input:** "Our city is considering requiring all home-sharing hosts (like Airbnb) to obtain a hotel license, complete safety inspections, and limit rentals to 90 days per year. The hotel industry supports it for 'safety and fairness.'"

**Output:**

## Natural Liberty Policy Test

### Policy Under Review
Proposed regulation requiring home-sharing hosts to obtain hotel licenses, pass safety inspections, and limit rentals to 90 days annually.

### Stated Justification
1. Guest safety (fire codes, health standards)
2. "Level playing field" with hotels
3. Preserve residential housing stock
4. Protect neighborhood character

### Affected Parties Analysis

| Party | Interest | Stated Position | True Interest |
|-------|----------|-----------------|---------------|
| Hotels | Profit, occupancy | Support for "fairness" | Eliminate low-cost competition |
| Airbnb hosts | Income from property | Oppose | Continue earning income |
| Airbnb guests | Affordable lodging | (Not consulted) | Lower prices, more options |
| Neighbors | Quiet neighborhoods | Mixed | Reduce transient visitors |
| Housing seekers | Affordable housing | (Not consulted) | More rental units available |
| City | Tax revenue, housing | Support | Revenue + respond to hotel lobbying |

### The Five Tests

#### 1. Does it violate natural liberty?
Yes. Property owners would be restricted from renting their own property as they choose. This is a restraint on voluntary exchange between willing parties.
**Assessment:** Yes

#### 2. Does it fall within legitimate government functions?
- Defense? No
- Justice? Partially—if home-sharing genuinely harms neighbors or creates safety hazards, preventing harm is justice
- Public works? No
**Assessment:** Borderline—safety inspection is defensible; licensing and day limits are not

#### 3. Who really benefits?
- **Stated beneficiary:** Guests (safety), neighbors (quiet), housing seekers (availability)
- **Actual beneficiary:** Hotels (reduced competition), city (simpler enforcement)
- **Who bears the cost:** Hosts (lost income), guests (higher prices, fewer options)

The 90-day limit has nothing to do with safety. It simply makes home-sharing unviable for most hosts, reducing supply and raising hotel demand.

#### 4. Does it create monopoly or restrict competition?
Yes. Hotel licensing requirements are designed for large commercial operations. Applying them to individuals renting spare rooms creates prohibitive barriers. The 90-day limit effectively bans a business model.
**Assessment:** Yes—directly restricts competition with hotels

#### 5. Is there a less restrictive alternative?
**Alternatives considered:**
- **Safety only:** Require smoke detectors and basic safety disclosure without full hotel licensing
- **Registration without licensing:** Simple registration for tax collection and accountability
- **Neighborhood-specific rules:** Address density/nuisance concerns in specific areas
- **Tax parity:** Collect hotel taxes from home-sharing without burdensome licensing

All achieve stated goals with less restriction on liberty.

### The Special Interest Test

**Who proposed or supports this policy?**
The hotel industry actively lobbied for this regulation.

**What do they gain?**
- Reduced competition
- Higher occupancy rates
- Ability to maintain higher prices

**Smith's warning applies?**
Absolutely. "The proposal of any new law or regulation of commerce which comes from this order ought always to be listened to with great precaution... It comes from an order of men whose interest is never exactly the same with that of the public."

The hotels dress their competitive interest in the language of "fairness" and "safety"—classic special interest rhetoric.

### Public Interest Assessment

| Claimed Benefit | Real? | Magnitude | Distribution |
|----------------|-------|-----------|--------------|
| Guest safety | Partial | Small (few incidents) | Narrow |
| Fair competition | No | N/A | Actually reduces competition |
| Housing availability | Partial | Small | Narrow |
| Neighborhood quality | Partial | Varies | Localized |

| Hidden Cost | Magnitude | Who Bears It |
|-------------|-----------|--------------|
| Higher lodging prices | Large | All visitors |
| Lost host income | Large | Property owners |
| Reduced consumer choice | Large | Travelers |
| Reduced city tax revenue | Medium | All residents |

### The Smithian Verdict

**Does this policy serve natural liberty or restrain it?**
It substantially restrains natural liberty. Property owners cannot use their property as they choose; travelers cannot access accommodation they want; hosts cannot earn income from willing guests.

**Does it serve the public or special interests?**
It primarily serves the hotel industry, which faces new competition and seeks government protection. The safety justifications could be achieved with far less restrictive measures. The 90-day limit has no safety rationale—it exists solely to make home-sharing nonviable.

**Should it be:**
- [ ] Enacted as proposed
- [x] Modified: Require basic safety measures (smoke detectors, egress), simple registration, tax collection—but no hotel licensing and no arbitrary day limits
- [ ] Rejected
- [ ] Replaced with alternative

**Reasoning:**
Smith would recognize this instantly as merchants seeking "to narrow the competition"—which is "always against the public interest." The hotel industry cannot compete with homeowners offering lower prices, so it seeks government restriction instead.

Some regulation is legitimate: basic safety standards protect guests from genuine hazards. But requiring full hotel licensing for someone renting a spare bedroom is using regulation as a competitive weapon. The 90-day limit reveals the true intent—it has nothing to do with safety and everything to do with suppressing a competing business model.

When those being regulated support the regulation most loudly, suspect conspiracy against the public.

---

## Integration

This skill is part of the **Adam Smith** expert persona. Use it to see through stated justifications to identify whether policies serve natural liberty and public benefit, or special interests and restraint of trade.