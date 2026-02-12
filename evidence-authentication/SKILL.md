---
name: evidence-authentication
description: Assess documentary evidence for credibility, completeness, and persuasive
  power before disclosure or publication.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- evidence-authentication
- storytelling
- writing
---

# Evidence Authentication

Assess documentary evidence for credibility, completeness, and persuasive power before disclosure or publication.

---

## When to Use

- Evaluating documents before releasing them
- User says "Is this evidence strong enough?" or "Evaluate this documentation"
- Preparing a disclosure package for journalists or investigators
- Assessing whether you have what you need to prove a claim
- Identifying weaknesses in evidence before opponents do

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| documents | Yes | Description or samples of the evidence |
| claim | Yes | What you're trying to prove |
| context | No | How you obtained it, chain of custody |
| intended_use | No | Journalism, legal action, public disclosure, etc. |

---

## The Ellsberg Principle

"Documents speak louder than claims."

Daniel Ellsberg understood that 7,000 pages of the government's own records were more powerful than any testimony he could give. The Pentagon Papers worked because they were undeniable—the government's own words, in their own documents.

**The goal:** Evidence so strong that the story tells itself.

---

## The Authentication Framework

### Level 1: Source Credibility

Where did this document come from? Can you prove it?

**Questions:**
- What is the chain of custody? How did this reach you?
- Can the source be independently verified?
- Is the document's origin consistent with how such documents are normally created?
- If challenged, can you prove this is genuine?

**Red flags:**
- Documents that "appeared" with no clear source
- Sources who won't confirm anything on the record
- Documents that seem too convenient or too perfect
- Materials that can't be placed in original context

**Strengthening factors:**
- Multiple independent sources for same information
- Metadata consistent with claimed origin
- Document found in expected location (original filing, archive, etc.)
- Source willing to attest to authenticity

### Level 2: Internal Consistency

Does the document make sense on its own terms?

**Questions:**
- Is the content consistent with what we know about the organization, time period, and context?
- Is the language consistent with how that organization writes?
- Are dates, names, and references accurate?
- Do multiple documents from the same source tell a consistent story?

**Red flags:**
- Anachronistic language or references
- Facts that contradict known public information
- Formatting inconsistent with the organization's standards
- Names or dates that don't check out

**Strengthening factors:**
- Cross-references between documents check out
- Details confirmed by independent public sources
- Language matches known organizational style
- Timeline is internally coherent

### Level 3: Corroboration

Can this information be confirmed through other sources?

**Questions:**
- Do other documents support this one?
- Can any facts in the document be independently verified?
- Is there testimony that corroborates the documentary evidence?
- Does this fit with other known evidence?

**The Ellsberg standard:** The Pentagon Papers were self-corroborating—thousands of documents that referenced each other and built a consistent narrative.

**Strengthening factors:**
- Multiple documents showing same pattern
- Independent witnesses who can confirm elements
- Public records that support the timeline
- Physical evidence that matches documentary claims

### Level 4: Deniability Analysis

How will opponents attack this evidence? Can they succeed?

**Attack vectors:**
- "It's fake"—Can they claim fabrication?
- "It's out of context"—Is there context that changes the meaning?
- "It's misinterpreted"—Is there another reading?
- "It's not what it looks like"—Innocent explanation available?
- "It's stolen"—Will the acquisition method discredit the content?
- "It's incomplete"—Are there documents that would change the story?

**For each attack:** What's your response?

### Level 5: Completeness

Do you have enough to prove the claim, or just enough to make an accusation?

**Questions:**
- What claim can you definitively prove with this evidence?
- What claim can you strongly support but not prove?
- What gaps exist?
- What additional evidence would complete the picture?

**The newspaper test:** Could a rigorous editor publish this? Would lawyers clear it?

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
## Evidence Authentication: [Claim Being Supported]

### The Claim
[What you're trying to prove]

### Evidence Summary
[Brief description of the documents/materials]

### Level 1: Source Credibility
- **Origin:** [Where this came from]
- **Chain of custody:** [How it reached you]
- **Verification possibility:** [Can authenticity be proven?]
- **Assessment:** [Strong/Moderate/Weak]

### Level 2: Internal Consistency
- **Content review:** [Does it make sense internally?]
- **Language analysis:** [Does it sound right?]
- **Factual accuracy:** [Do checkable facts check out?]
- **Assessment:** [Strong/Moderate/Weak]

### Level 3: Corroboration
- **Supporting documents:** [What else backs this up?]
- **Independent verification:** [What can be confirmed separately?]
- **Testimony available:** [Who can speak to this?]
- **Assessment:** [Strong/Moderate/Weak]

### Level 4: Deniability Analysis
| Attack Vector | Likelihood | Your Defense |
|---------------|------------|--------------|
| Forgery claim | [High/Med/Low] | [Defense] |
| Context attack | [High/Med/Low] | [Defense] |
| Misinterpretation | [High/Med/Low] | [Defense] |
| Acquisition ethics | [High/Med/Low] | [Defense] |

### Level 5: Completeness
- **Definitively proven:** [What the evidence proves beyond doubt]
- **Strongly supported:** [What the evidence strongly suggests]
- **Still needed:** [What gaps remain]
- **Assessment:** [Complete/Near-complete/Significant gaps]

### Overall Assessment
- **Is this evidence strong enough?** [Yes/No/Conditional]
- **Recommended action:** [Release/Wait for more/Abandon claim]
- **Key vulnerabilities:** [Weakest points]
- **Strengthening opportunities:** [How to improve]

### Preparation Recommendations
[What to do before release]
```

---

## Constraints

- This assessment must be honest—don't convince yourself weak evidence is strong
- No evidence is perfect—accept that some vulnerability always exists
- The standard depends on use—legal cases require more than journalism
- Don't release evidence you haven't authenticated—it damages all future credibility
- If you can't prove something, say you can't prove it

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

**Input:** "I have emails from our company's executives discussing how to classify certain chemicals to avoid EPA reporting requirements. There are about 15 emails over 6 months. I forwarded them to my personal email. I want to give these to an environmental journalist."

**Output:**

## Evidence Authentication: Deliberate EPA Reporting Avoidance

### The Claim
Company executives deliberately misclassified chemicals to avoid EPA reporting requirements.

### Evidence Summary
15 internal emails over 6 months, appearing to show executives discussing classification strategies to minimize regulatory reporting obligations.

### Level 1: Source Credibility
- **Origin:** Company email system (you are an employee with legitimate access)
- **Chain of custody:** Direct from company server → forwarded to personal email
- **Verification possibility:**
  - Original emails exist in company system (could be subpoenaed)
  - Headers should show routing through company servers
  - Participants could confirm (under oath, if subpoenaed)
- **Assessment:** **Strong.** As a company employee with access, your custody of these documents is legitimate. Headers will show origin.

**Concern:** Forwarding to personal email may violate company policy (but doesn't affect authenticity).

### Level 2: Internal Consistency
- **Content review:** [Would need to examine] Do the emails reference real facilities, real chemicals, real dates?
- **Language analysis:** Do executives write like this? (Technical language, informal internal tone, etc.)
- **Factual accuracy:** Can mentioned events, dates, or decisions be verified against other records?
- **Assessment:** **Unknown—requires document review.** Check for:
  - Do chemical names match actual company products?
  - Do dates match actual reporting periods?
  - Do sender/recipient names match actual executives?
  - Is the email format consistent with company's email system?

### Level 3: Corroboration
- **Supporting documents:**
  - Actual EPA filings—do they show classifications discussed in emails?
  - Previous filings—did classifications change after these discussions?
  - Any other witnesses to these conversations?
- **Independent verification:**
  - EPA records are public—can verify what was actually reported
  - Industry databases may show what competitors report for similar chemicals
  - Scientific literature on proper classification
- **Testimony available:** Other employees who may have been aware? Consultants involved?
- **Assessment:** **Potentially strong if corroborated.** The power would be showing: emails discuss plan → filings show that plan executed.

### Level 4: Deniability Analysis
| Attack Vector | Likelihood | Your Defense |
|---------------|------------|--------------|
| Forgery claim | Low | Headers trace to company servers; company can produce originals |
| Context attack | HIGH | "This was just brainstorming—we considered all options and chose legal path" | *Need evidence showing the discussed classifications were actually used* |
| Misinterpretation | Medium | "Legal classification is judgment call—our lawyers signed off" | *Need to show their interpretation was unreasonable* |
| Acquisition ethics | Medium | "These were stolen from company" | Your access was legitimate; you're a whistleblower not a thief |

**Critical vulnerability:** The context attack is strong. Without follow-through evidence showing the discussed classifications were actually implemented, these could be spun as "exploring options."

### Level 5: Completeness
- **Definitively proven:** Executives discussed misclassification as a strategy
- **Strongly supported:** This was not theoretical—they intended to implement
- **Still needed:**
  - Evidence that discussed classifications were actually used in EPA filings
  - Any indication this was contrary to legal advice
  - Evidence of motive (cost savings figures, competitive pressure)
  - Ideally: follow-up email saying "good, we submitted it that way"
- **Assessment:** **Significant gaps.** You can prove they discussed it. You need to prove they did it.

### Overall Assessment
- **Is this evidence strong enough?** **Not yet.** The emails show intent but not execution. Need to connect discussion to actual filings.
- **Recommended action:** Before disclosing:
  1. Obtain company's actual EPA filings for relevant periods
  2. Verify the chemicals discussed match filings
  3. Find or document evidence that discussed classifications were implemented
  4. If possible, any documentation showing this contradicted advice or standards
- **Key vulnerabilities:** The "we were just brainstorming" defense is strong without follow-through proof.
- **Strengthening opportunities:**
  - EPA filings are public—pull them
  - Company's own EHS documentation might show classification decisions
  - Any memos implementing the decisions discussed

### Preparation Recommendations
1. **Before any disclosure:** Pull public EPA filings for your company for relevant period. Compare to classifications discussed in emails.
2. **Strengthen chain of custody:** Document when you received each email, your role, why you had legitimate access.
3. **Consult attorney:** Before disclosing to journalist, understand your legal exposure and protections.
4. **Work with journalist, not just hand over:** A good investigative journalist will help build the complete picture. Don't just dump emails—partner on investigation.
5. **Prepare for retaliation:** Even with good evidence, expect pushback. Have your documentation secure and legal strategy ready.

---

## Integration

This skill is part of the **Daniel Ellsberg** expert persona. Ellsberg understood that the Pentagon Papers' power came from their authenticity and completeness—7,000 pages of the government's own records, internally consistent, corroborated by each other, undeniable. "I knew that the documents would speak for themselves. I didn't need to interpret them—they were the government's own words about their own lies." Evidence authentication ensures your disclosure has that same undeniable quality.