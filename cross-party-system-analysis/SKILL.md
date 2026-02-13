---
name: cross-party-system-analysis
description: Analyze a political issue to reveal how ostensibly opposing parties serve the same underlying power structure, moving beyond partisan theater to systemic critique.
license: MIT
metadata:
  version: 1.0.701
  author: sethmblack
keywords:
- cross-party-system-analysis
- writing
---

# Cross-Party System Analysis

Analyze a political issue to reveal how ostensibly opposing parties serve the same underlying power structure, moving beyond partisan theater to systemic critique. This skill applies Mort Sahl's signature analytical method: observing that when opposing parties publicly disagree but privately align on outcomes, the disagreement is theater and the alignment reveals true interests. "Publicly, they're on opposite sides of this issue. Privately, they both make sure nothing changes. Now, why would that be?" The goal is not cynical nihilism but clear-eyed understanding—when you see the system clearly, you can engage it more effectively. This skill helps distinguish partisan rhetoric from bipartisan action, identify specific shared interests with evidence, and reveal structural mechanisms producing alignment while avoiding false equivalence.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Create "both sides are exactly the same" false equivalence that obscures real policy differences
- Generate cynical nihilism that discourages democratic participation
- Produce content designed to suppress voter turnout
- Create partisan propaganda disguised as non-partisan analysis
- Fabricate party positions or misrepresent actual policy stances

**Ethical Requirements:**
- Acknowledge real policy differences while identifying shared structural interests
- Distinguish between "same underlying interests" and "identical in all ways"
- Base party positions on documented statements and voting records
- Maintain citizen's perspective that voting and participation still matter
- Critique power structures without claiming resistance is futile

---

## When to Use

**Trigger conditions (use proactively when ANY apply):**
- Political debate frames issue as binary partisan choice
- Both major parties take similar action despite different rhetoric
- User asks "why do both parties support [X]?"
- Partisan talking points obscure deeper structural issue
- Issue has bipartisan support despite public opposition
- Request to understand "real" reason behind political consensus
- User frustrated with "both sides do the same thing"

**Do NOT use when:**
- Parties have genuinely opposing positions and actions
- User needs factual comparison of specific policy differences
- Issue is primarily about individual politician, not system
- Request is for partisan critique (supporting one party)
- Historical context matters more than structural analysis

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `issue` | Yes | The political issue or debate to analyze | Clear, specific topic (not vague like "corruption") |
| `party_positions` | No | Known stated positions from each party | Include sources if possible; will research if not provided |
| `recent_actions` | No | Recent votes, bills, or actions related to issue | Specific examples with dates |
| `audience_assumption` | No | What the audience likely believes about this issue | E.g., "audience thinks this is purely partisan fight" |

---

## Core Principle

When both parties publicly disagree but privately align on outcomes, the disagreement is theater and the alignment reveals true interests. Look at actions, not rhetoric. Bipartisan consensus—especially on issues with broad public opposition—often indicates shared interest in maintaining current power structures rather than genuine policy agreement.

---

## Methodology

### Step 1: Map the Partisan Theater
Identify how the issue is typically framed:
- What does each major party claim to support?
- What rhetoric does each side use?
- How is this presented as binary choice?
- What emotional appeals are employed?

### Step 2: Document Actual Actions
Look beyond rhetoric to behavior:
- How do parties actually vote when issue comes up?
- What bills pass with bipartisan support?
- When do actions contradict stated positions?
- What gets unanimous or near-unanimous approval?

### Step 3: Identify the Shared Interest
Ask the key questions:
- Who benefits from current system (regardless of which party is in power)?
- What constituency do both parties actually serve on this issue?
- What would genuinely threaten the shared interest?
- What alternatives are kept off the table by both sides?

### Step 4: Trace the System Structure
Reveal the underlying mechanism:
- What structural feature produces this alignment?
- How does system itself create incentives both parties respond to?
- What makes deviation from shared interest costly for either party?
- Why does partisan theater persist if interests align?

### Step 5: Build Sahl-Style Commentary
Present analysis in Mort Sahl voice:
- Start with surface-level partisan framing ("They say Republicans want X, Democrats want Y...")
- Introduce contradictory evidence ("But when you look at how they actually vote...")
- Express sophisticated naïveté ("Wait, let me get this straight...")
- Follow the logic to systemic conclusion
- Land on citizen's perspective

### Step 6: Preserve Nuance
Avoid false equivalence:
- Note where real policy differences DO exist
- Acknowledge this analysis addresses specific issue, not all issues
- Distinguish between "same on this" and "same on everything"
- Maintain that understanding system empowers citizens, doesn't negate participation

---

## Outputs

| Output | Format | Description |
|--------|--------|-------------|
| `analysis` | Markdown text | The cross-party system analysis in Sahl voice |
| `shared_interest` | 1 sentence | The underlying interest both parties serve |
| `partisan_theater` | 1 sentence | What the debate claims to be about |
| `evidence` | List | Specific votes, actions, or statements supporting analysis |

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Parties genuinely oppose each other on issue | Note this honestly; not every issue reveals shared interest |
| Insufficient evidence for shared interest claim | Acknowledge speculation vs. documented fact; present as hypothesis |
| Analysis becomes partisan (favoring one party) | Pull back; re-center on system structure both parties navigate |
| User wants cynical "nothing matters" conclusion | Redirect to "understanding system enables change" framing |
| Historical complexity exceeds current scope | Focus on recent actions; acknowledge historical factors but stay grounded in present |
| Issue has regional rather than partisan split | Note that geography or constituency matters more than party label here |

---

## Example

**Input:**
```
issue: "Congressional stock trading"
party_positions:
  - Republicans: "Free market principles"
  - Democrats: "Conflict of interest concerns"
recent_actions:
  - 2022: Stock trading ban bill introduced, died in committee
  - Bipartisan opposition prevented floor vote
```

**Output:**

**Analysis:**
I read that there's a big debate about Congressional stock trading. Republicans say it's about free market principles—members of Congress have a right to invest like anyone else. Democrats say it's a conflict of interest—how can you regulate industries you're personally invested in? Sounds like a classic partisan divide, right?

Except when you look at what actually happens, both parties killed the bill that would have banned it. It died in committee. Bipartisan opposition—that means they agreed on something. Which is interesting, because they claim to disagree.

So let me get this straight: publicly, they're on opposite sides of this issue. Privately, they both make sure nothing changes. Now, why would that be? Well, according to the reports, members of both parties have stock portfolios. Some of them beat the market consistently, which is remarkable given that they have access to... wait, what do they have access to? Information about upcoming legislation? Regulatory changes? Government contracts?

See, this is one of those rare moments where the system reveals itself. The partisan debate is about principles—free market versus conflict of interest. The bipartisan action is about self-interest—keeping the ability to trade on information we don't have. The theater is for us. The alignment is for them.

**Shared Interest:**
Maintaining Congressional access to stock trading with inside information that produces market-beating returns.

**Partisan Theater:**
Free market principles (Republicans) versus conflict of interest concerns (Democrats).

**Evidence:**
- 2022 stock trading ban bill died in committee with bipartisan opposition
- Multiple members of both parties consistently outperform market averages
- Public rhetoric opposes private action—both parties blocked reform

---

## Integration with Mort Sahl Expert

This skill operationalizes Mort Sahl's signature non-partisan critique:
- **Cross-Party Observation** - Revealing when "opponents" serve same interest
- **System Over Personality** - Moving from individual politicians to structural analysis
- **Sophisticated Naïveté** - Expressing shock at gap between rhetoric and action
- **The Newspaper Method** - Using documented facts (votes, bills) as evidence

When the Mort Sahl expert invokes this skill, it should feel like his core methodology in action. The expert's voice carries through the analysis, maintaining conversational tone and embedded skepticism.

**Proactive Triggers for Expert:**
- User frustrated with partisan gridlock
- Bipartisan consensus emerges on controversial issue
- Rhetoric and action clearly diverge
- User asks "why do both parties agree on this?"
- Political debate feels performative rather than substantive

---

## Constraints

- Evidence-based: Must document actual party actions, not just rhetoric
- Nuance preservation: Avoid "both parties are identical" false equivalence
- System focus: Must identify structural mechanism, not just "politicians are corrupt"
- Specific issue scope: Analysis applies to specific issue provided, not all politics generally
- Citizen perspective: End with empowerment, not nihilism

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails | Better Approach |
|--------------|--------------|-----------------|
| **"Both Sides Are Exactly the Same"** | False equivalence obscures real policy differences that matter. | Identify where parties genuinely differ. This analysis applies to specific issues, not all issues. |
| **Cynical Nihilism** | "Nothing matters, don't bother voting" discourages democratic participation. | Understanding system enables more effective action, not less. |
| **Conspiracy Framing** | "Secret cabals control everything" replaces analysis with paranoia. | Focus on documented actions, votes, and structural incentives—not speculation about hidden coordination. |
| **Missing Evidence** | "Everyone knows they're the same" without specific votes, bills, or documented actions. | Base party positions on documented statements and voting records. |
| **Partisan Disguise** | Using "non-partisan analysis" to attack one party while defending the other. | Genuine system analysis criticizes both parties' role in maintaining problematic structures. |

---

## Success Criteria

The analysis is successful when:
- [ ] Clearly distinguishes partisan rhetoric from bipartisan action
- [ ] Identifies specific shared interest with evidence
- [ ] Reveals structural mechanism producing alignment
- [ ] Maintains Mort Sahl voice (conversational, intellectual, skeptical)
- [ ] Avoids false equivalence—acknowledges nuance
- [ ] Empowers rather than depresses (understanding system ≠ futility)
- [ ] Based on verifiable actions (votes, bills, documented statements)
- [ ] Exposes partisan theater without claiming all issues are theater