---
name: merit-assessment
description: Evaluate people based on demonstrated results and proven ability rather than credentials, titles, or background.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.1431
keywords:
- merit-assessment
- writing
---

# Merit Assessment

Evaluate people based on demonstrated results and proven ability rather than credentials, titles, or background.

**Source Expert:** Genghis Khan
**Category:** Leadership / Evaluation

---

## When to Use

- Hiring decisions where credentials don't tell the whole story
- Promotion decisions within an organization
- Evaluating potential partners or co-founders
- Assessing team members for critical assignments
- Deciding whether to trust someone who switched from a competitor

**Trigger Phrases:**
- "Who should I promote?"
- "Evaluate this person/team"
- "Should I hire them?"
- "How do I assess real capability?"
- "They have great credentials but..."
- "They came from a competitor"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `person/team` | Yes | Who you are evaluating |
| `role/purpose` | Yes | What you need them to do |
| `available_evidence` | Yes | What you know about their history |
| `context` | No | Relevant organizational/competitive context |

---

## Workflow
### Step 1: The Jebe Principle

> "A man who shows skill and courage against you will show the same in your service. A man who betrays his master to help you will betray you for another."

When an arrow struck Genghis Khan's horse (likely wounding the Khan himself), he demanded to know who had fired it. The archer Jirqo'adai stepped forward, confessed, and offered his life or his service. Genghis made him a general and renamed him Jebe ("arrow"). Jebe became one of the greatest Mongol commanders.

The lesson: Judge by demonstrated deeds, not by words or position. The enemy who fought well against you is more valuable than the ally who betrayed someone else to join you.

### Step 2: Framework

**1. Strip Away the Credentials**
Ignore titles, degrees, company names, and LinkedIn endorsements. These are words, not deeds. Ask only: What has this person actually built? What problems have they actually solved? What results can be verified?

**2. Examine Behavior Under Pressure**
How did they act when things went wrong? Did they abandon their position, or hold it? Did they blame others, or take responsibility? Courage and loyalty reveal themselves in difficulty, not in success.

**3. Apply the Loyalty Test**
If they left a previous employer or partner:
- Did they leave honorably, or by betrayal?
- Did they badmouth their previous master?
- Did they bring secrets or proprietary information as their "value"?
- Would you want them to leave YOU the way they left their last position?

**4. Verify Through Action**
Past deeds indicate future performance, but only if verified. Talk to people who worked with them. Look at what they built. Examine the trail they left. Claims are words; evidence is deeds.

**5. Test with Small Stakes**
Before major responsibility, give them a smaller challenge. Watch how they handle it. Do they execute or excuse? Do they own the outcome or explain it away?

---

## Output Format

```markdown
## Merit Assessment: [Person/Team Name]

### Demonstrated Deeds
- [Verified accomplishment 1]
- [Verified accomplishment 2]
- [What they actually built/achieved/solved]

### Credentials to Ignore
- [Title/degree/affiliation that doesn't prove capability]

### Loyalty Indicators
- **How they left previous positions:** [Honorable/Concerning]
- **How they speak of former employers:** [Respectful/Disparaging]
- **What they're offering:** [Skills/Secrets]

### Pressure Behavior
- [Evidence of how they acted under difficulty]

### Assessment
**Verdict:** [Worthy of command / Needs verification / Untrustworthy]
**Reasoning:** [2-3 sentences explaining the judgment]

### Recommended Action
[Specific next step: promote, hire, test further, decline]
```

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
- Person: Senior engineer from major competitor, impressive resume
- Role: Technical lead for critical project
- Evidence: Led team that built competitor's core product; left after disagreement with leadership; reached out to us; offering "insights" into competitor's roadmap

**Output:**

## Merit Assessment: [Candidate Name]

### Demonstrated Deeds
- Led 12-person team that shipped competitor's core product (verified)
- Product achieved market fit and scaled to 100K users (verifiable)
- Team members speak highly of technical leadership (reference checks)

### Credentials to Ignore
- Stanford CS degree (words, not deeds)
- "Senior Staff" title (company-specific, means different things)
- Impressive LinkedIn recommendations (easily manufactured)

### Loyalty Indicators
- **How they left previous positions:** Concerning. Left after disagreement, but the timing suggests frustration rather than principle.
- **How they speak of former employers:** Disparaging. Used phrases like "they never listened" and "leadership was clueless."
- **What they're offering:** MAJOR RED FLAG. Offering competitor roadmap information as part of their value proposition.

### Pressure Behavior
- Reference indicates they held their ground during a critical launch crisis
- However, also blamed product team for problems that were partly engineering decisions

### Assessment
**Verdict:** Skills worthy; loyalty concerning

The technical ability is real and verified. However, offering competitor secrets as value is the behavior of someone who would do the same to you. A man who betrays his master for you will betray you for another.

### Recommended Action
Decline for leadership role. If technical skills are truly needed, consider individual contributor role with limited access to strategic information. Do not place in position where loyalty matters more than skill.

---

## Anti-Patterns

**DON'T:**
- Be dazzled by prestigious credentials
- Trust claims without verification
- Value those who bring secrets from competitors
- Ignore how someone left their previous position
- Skip reference checks with actual colleagues (not provided references)
- Mistake interview performance for actual capability

**WARNING SIGNS:**
- Speaks disparagingly of previous employers
- Offers insider information as part of their pitch
- Cannot point to specific, verifiable accomplishments
- Claims credit for team achievements without acknowledging others
- Changed jobs frequently without clear progression or reason

---

## Integration

This skill pairs with:
- **Talent Absorption:** After assessing merit, how to integrate valuable people
- **Decimal Organization:** Where to place people based on assessed capability
- **Intelligence Network Design:** Verifying claims about accomplishment