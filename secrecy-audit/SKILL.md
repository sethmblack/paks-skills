---
name: secrecy-audit
description: Evaluate whether information is legitimately classified or merely embarrassment-protected,
  assessing the true purpose behind secrecy.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- secrecy-audit
- writing
---

# Secrecy Audit

Evaluate whether information is legitimately classified or merely embarrassment-protected, assessing the true purpose behind secrecy.

---

## When to Use

- Questioning whether classification is legitimate
- User says "Is this classification justified?" or "Audit this secrecy claim"
- Evaluating whether to respect confidentiality designations
- Assessing institutional secrecy practices
- Determining if information is protected for security or for reputation

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| information | Yes | What is being kept secret |
| stated_justification | No | Official reason for secrecy |
| context | No | Institutional setting and background |
| public_interest | No | Why the public might need this information |

---

## The Ellsberg Framework

Ellsberg spent years with high-level security clearances and saw how classification actually works. His conclusion:

"The overwhelming majority of classified information is classified not to protect national security but to prevent embarrassment."

**The fundamental question:** Who is this secrecy protecting, and from what?

---

## Legitimate vs. Illegitimate Secrecy

### Legitimate Reasons for Secrecy

**National security (actual):**
- Active military operations
- Intelligence sources and methods
- Nuclear weapons specifications
- Diplomatic negotiations in progress

**Personal privacy:**
- Individual medical records
- Personnel files
- Sealed court proceedings protecting victims

**Necessary operational security:**
- Pending law enforcement operations
- Trade secrets (actual proprietary advantage)
- Attorney-client privileged communications

**Key characteristic:** Disclosure would cause specific, identifiable harm to identifiable parties or operations.

### Illegitimate Reasons for Secrecy

**Embarrassment protection:**
- Hiding mistakes or failures
- Concealing policy disagreements
- Preventing criticism of decisions

**Accountability avoidance:**
- Hiding evidence of wrongdoing
- Preventing oversight
- Avoiding responsibility for failures

**Political protection:**
- Information damaging to officials, not to security
- Evidence contradicting public statements
- Material that would change policy debates

**Competitive advantage for institutions (not true security):**
- Government agency protecting budget
- Corporation hiding regulatory violations
- Institution preventing reform pressure

**Key characteristic:** Disclosure would harm reputations, careers, or institutional interests—not actual security.

---

## The Classification Abuse Indicators

### Indicator 1: Over-Classification

Information classified at higher levels than warranted.

**Signs:**
- Routine documents marked Top Secret
- Information that's publicly available is still classified
- Historical documents that remain classified decades after relevance

**Ellsberg's observation:** "Almost everything is over-classified. Officials classify at higher levels because there's no penalty for over-classification but potential penalty for under-classification."

### Indicator 2: Selective Declassification

Information is released when it helps officials, hidden when it would hurt.

**Signs:**
- Leaks to favorable media that aren't prosecuted
- Declassification of "good news," continued classification of "bad news"
- Officials citing classified information to support their positions, but opponents can't see it

**The test:** Is the same classification standard applied regardless of whether the information helps or hurts the classifying authority?

### Indicator 3: Retroactive Classification

Information that was public becomes classified after it proves embarrassing.

**Signs:**
- Documents removed from public access
- Previously testified information now deemed classified
- Sudden claims of classification after freedom of information requests

### Indicator 4: Process Obstruction

Classification used to prevent oversight rather than protect secrets.

**Signs:**
- Lawmakers can't get briefings on programs they're supposed to oversee
- Classification prevents judicial review
- Internal watchdogs denied access

---

## The Audit Questions

### Question 1: What Specific Harm Would Disclosure Cause?

The justification should identify specific, concrete harm—not vague claims like "national security" or "operational concerns."

**Legitimate answer:** "Disclosure would reveal the identity of a covert source who would face imprisonment or death."
**Illegitimate answer:** "Disclosure would damage national security." (Too vague—how?)

### Question 2: Who Benefits from This Secrecy?

Follow the interest analysis:

- Does secrecy protect identifiable people from real harm?
- Or does it protect institutions from accountability?
- Or does it protect officials from embarrassment?

### Question 3: Is the Classification Consistent?

- Is similar information in similar contexts classified the same way?
- If similar information has been released elsewhere, why is this still classified?
- Would this information be classified if it reflected well on the classifying authority?

### Question 4: What Does the Public Need to Know to Self-Govern?

Democratic accountability requires informed citizens.

- Is this information necessary for the public to evaluate policies?
- Would knowing this change how people vote, organize, or advocate?
- Is the public being asked to support policies based on incomplete information?

### Question 5: Has Time Made Classification Moot?

Many classifications have expiration dates in theory but not in practice.

- Is this historical information that no longer affects current operations?
- Has the situation the classification protected already passed?
- Is this a Cold War secret about a country that no longer exists?

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
## Secrecy Audit: [Information Description]

### Information in Question
[What is being classified or kept secret]

### Stated Justification
[Official reason given for secrecy]

### Audit Questions

#### Q1: Specific Harm from Disclosure
- **Claimed harm:** [What they say would happen]
- **Analysis:** [Is the harm specific and identifiable?]
- **Verdict:** [Legitimate/Vague/Fabricated]

#### Q2: Who Benefits from Secrecy
- **Beneficiaries identified:** [Who gains from this being secret]
- **Harm to them if disclosed:** [What they'd lose]
- **Verdict:** [Security protection/Accountability avoidance/Embarrassment protection]

#### Q3: Classification Consistency
- **Comparable cases:** [Similar information and how it's treated]
- **Selective application:** [Any evidence of inconsistency?]
- **Verdict:** [Consistent/Inconsistent/Suspicious]

#### Q4: Democratic Necessity
- **Public interest in knowing:** [Why citizens need this]
- **Policy implications:** [What decisions depend on this]
- **Verdict:** [Necessary for democracy/Useful but not essential/Legitimately private]

#### Q5: Temporal Relevance
- **Original classification date:** [When this was classified]
- **Current relevance:** [Does secrecy still serve its purpose?]
- **Verdict:** [Still relevant/Moot/Should have been declassified]

### Classification Abuse Indicators
- [ ] Over-classification
- [ ] Selective declassification
- [ ] Retroactive classification
- [ ] Process obstruction

### Overall Assessment
- **Is this secrecy legitimate?** [Yes/Partially/No]
- **Primary purpose of secrecy:** [Security/Accountability avoidance/Embarrassment/Other]
- **Recommendation:** [Respect/Challenge/Disclose]

### Considerations for Disclosure
[If recommending disclosure: risks, methods, protections]
```

---

## Constraints

- Some secrecy is legitimate—don't assume all classification is abuse
- You may not have full information—secrecy may be justified for reasons you can't know
- Legal consequences exist for unauthorized disclosure regardless of legitimacy
- The audit helps inform judgment—it doesn't authorize action
- Even illegitimate secrecy may serve some purpose worth considering

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

**Input:** "A government agency classified a report about their program's effectiveness. The report apparently showed the program wasn't working. The agency says it's classified for 'operational security.'"

**Output:**

## Secrecy Audit: Program Effectiveness Report

### Information in Question
Government agency report evaluating effectiveness of [program]. Report apparently concludes program is not achieving its stated objectives.

### Stated Justification
"Operational security"

### Audit Questions

#### Q1: Specific Harm from Disclosure
- **Claimed harm:** "Operational security" (no specific harm articulated)
- **Analysis:** "Operational security" is a category, not a specific harm. What operation would be compromised by knowing the program doesn't work? How would disclosure change adversary behavior?
- **Verdict:** **Vague.** No specific, identifiable harm articulated. A program's ineffectiveness is an outcome measure, not typically an operational detail.

#### Q2: Who Benefits from Secrecy
- **Beneficiaries identified:**
  - Agency leadership (avoids accountability for failed program)
  - Program staff (avoids cuts or reassignment)
  - Officials who championed the program (avoids political embarrassment)
  - Contractors involved (avoids contract review)
- **Harm to them if disclosed:** Career damage, budget cuts, political criticism, contract loss
- **Verdict:** **Accountability avoidance / Embarrassment protection.** The primary beneficiaries are institutional, not security-related.

#### Q3: Classification Consistency
- **Comparable cases:**
  - Program effectiveness reports are frequently published (GAO reports, IG reports)
  - Positive effectiveness reports from same agency—are those classified?
  - Congressional testimony about program—was effectiveness discussed there?
- **Selective application:** If positive results would have been disclosed, the classification is selective.
- **Verdict:** **Likely inconsistent / Suspicious.** Effectiveness data is routinely disclosed; classification of negative results suggests selective application.

#### Q4: Democratic Necessity
- **Public interest in knowing:**
  - Taxpayers fund the program
  - Voters elect officials who authorize and oversee it
  - Policy decisions about continuing, expanding, or cutting depend on effectiveness
- **Policy implications:** Congress is considering program renewal without knowing it doesn't work
- **Verdict:** **Necessary for democracy.** This information is directly relevant to democratic accountability over public expenditure.

#### Q5: Temporal Relevance
- **Original classification date:** Recent
- **Current relevance:** Program is ongoing and subject to authorization decisions
- **Verdict:** **Current situation—not moot.** However, this cuts both ways: information is current and relevant, but so are any operational concerns.

### Classification Abuse Indicators
- [x] Over-classification (effectiveness data rarely requires classification)
- [x] Selective declassification (positive results would likely be publicized)
- [ ] Retroactive classification (not applicable)
- [x] Process obstruction (Congress making decisions without this information)

### Overall Assessment
- **Is this secrecy legitimate?** **Likely No.**
- **Primary purpose of secrecy:** Accountability avoidance and embarrassment protection
- **Recommendation:** Challenge through legitimate channels

**Key analysis:** "Operational security" is the claimed justification, but no specific operation has been identified that would be compromised by knowing a program failed. The pattern—classifying negative evaluation, likely publicizing positive evaluation—indicates secrecy is protecting officials, not operations.

### Considerations for Disclosure

**If you have access to this report:**
1. **Do not disclose without legal counsel.** Classification, even illegitimate, carries legal consequences.
2. **Try legitimate channels first:**
   - Congressional oversight (members with clearance can view)
   - Inspector General (can investigate classification decisions)
   - Request declassification review
3. **If legitimate channels fail:**
   - Consult with whistleblower attorney about protections
   - Consider whether disclosure is worth personal risk
   - If disclosing, work with journalists who have experience with classified material

**The Ellsberg question:** The Pentagon Papers showed that official secrecy often protects reputation, not security. But Ellsberg also faced criminal charges. The question is whether this information is important enough to accept the consequences of disclosure.

---

## Integration

This skill is part of the **Daniel Ellsberg** expert persona. Ellsberg spent years with the highest security clearances and saw how classification actually operates: "The classification system works much less to protect secrecy from foreign adversaries than to keep information from the American public." The secrecy audit applies his framework: distinguish genuine security from institutional self-protection, and evaluate whether the public's right to know outweighs the claimed need for secrecy.