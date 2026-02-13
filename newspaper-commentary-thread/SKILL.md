---
name: newspaper-commentary-thread
description: Transform a collection of current news items into an improvisational political commentary thread that reveals underlying patterns, using Mort Sahl's jazz-inspired connection-making approach.
license: MIT
metadata:
  version: 1.0.1521
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- newspaper-commentary-thread
- transformation
- writing
---

# Newspaper Commentary Thread

Transform a collection of current news items into an improvisational political commentary thread that reveals underlying patterns, using Mort Sahl's jazz-inspired connection-making approach.

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Create partisan propaganda that serves one political party over truth
- Fabricate news events or quotes that didn't happen
- Generate content intended to mislead voters or suppress participation
- Create deepfake-style misrepresentations of political figures
- Bypass fact-checking or verification systems

**Ethical Requirements:**
- Base commentary on verifiable, recent news events
- Maintain non-partisan stance (critique power regardless of party)
- Distinguish between documented facts and commentary/interpretation
- Preserve nuance—avoid absolutist "all politicians are..." generalizations
- Respect democratic discourse even while critiquing specific actions

---

## When to Use

**Trigger conditions (use proactively when ANY apply):**
- User provides 2+ current news items/headlines
- User asks for political commentary on recent events
- User requests "Mort Sahl-style analysis"
- User wants to connect disparate political stories
- Multiple recent political events seem disconnected but may share underlying pattern
- Request to "find the pattern" in current events
- Need to move from headline-level to systemic-level understanding

**Do NOT use when:**
- News items are outdated (>6 months old) - Sahl's method requires currency
- User wants purely partisan critique (this skill is non-partisan)
- Topic is non-political (personal, cultural, linguistic)
- User wants dry analysis without commentary voice

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `news_items` | Yes | 2-5 current news stories, headlines, or political events | Must be recent (within 6 months), verifiable, include source if possible |
| `focus_area` | No | Specific angle or theme to explore (e.g., "presidential power", "congressional dysfunction") | Free text, 1-3 words |
| `audience_context` | No | What the audience already knows or cares about | Free text, 1-2 sentences |
| `length` | No | Desired length: "brief" (1-2 paragraphs), "moderate" (3-4 paragraphs), "extended" (5+ paragraphs) | Default: moderate |

**Input Validation:**
```bash
# Check news_items count
if [ ${#news_items[@]} -lt 2 ]; then
    echo "ERROR: Provide at least 2 news items for pattern analysis"
    exit 1
fi

# Check recency (warn if items appear old)
if [[ "$news_items" =~ (2023|2024) ]]; then
    echo "WARNING: Some news items may be outdated. Sahl's method works best with current events."
fi
```

---

## Workflow
### Step 1: Verify News Items
- Confirm each news item is real and accurately represented
- Note the source and date
- If quotes are involved, verify they're actual quotes
- **If fabricated:** Stop and request verified sources

### Step 2: Identify the Contradiction
For each news item, identify:
- What official statement or position is being taken
- What observable reality contradicts or complicates it
- What's being obscured by the framing

### Step 3: Find the Connection Thread
Look for patterns across items:
- Do they reveal the same power dynamic from different angles?
- Do they show contradictory policies from the same entity?
- Do they illustrate system-level issue manifesting in multiple places?
- What's the "according to whom?" question that unites them?

### Step 4: Build the Improvisational Thread
Using Mort Sahl's voice:
- Start with one news item using "I read that..." or "According to..."
- Express sophisticated naïveté about the contradiction
- Connect to second item through association or contrast
- Follow the thought wherever it leads (jazz improvisation)
- Circle back with variations
- Build intellectual momentum without predetermined conclusion

### Step 5: Land on the System
Conclude with:
- Systemic insight, not partisan point-scoring
- "This is how [system] actually works" revelation
- Non-partisan observation about power structures
- Citizen's perspective, not insider cynicism

### Step 6: Apply Sentence-Level Craft
Polish for Sahl's distinctive voice:
- Conversational rhythms with intellectual vocabulary
- Embedded skepticism ("according to...", "they say...")
- Mid-thought corrections showing thinking process
- Trust audience to make connections

---

## Outputs

| Output | Format | Description |
|--------|--------|-------------|
| `commentary` | Markdown text | The improvisational political commentary thread |
| `pattern_identified` | 1-2 sentences | The underlying pattern revealed by connecting the items |
| `sources_used` | List | News items cited with sources |

---



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


## Error Handling

| Situation | Response |
|-----------|----------|
| News items can't be verified | Request verifiable sources; refuse to proceed with unverified claims |
| Only 1 news item provided | Request at least one more for pattern analysis, or suggest this needs different skill |
| Items are too old (>1 year) | Warn that Sahl's method requires currency; suggest historical analysis instead |
| User wants partisan conclusion | Redirect to non-partisan systemic analysis; explain Sahl targeted all parties |
| Items have no connectable pattern | Note this honestly; not all items reveal patterns—that's okay |
| Requested length is "extended" but only 2 items | Warn that extended analysis needs 3+ items for sufficient material |

---

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

## Integration

This skill is part of a broader analytical framework. Use it when you need systematic analysis following this specific methodology.

**Works well with:**
- Other analytical skills for comprehensive evaluation
- Creative skills when generating solutions based on insights
- Strategic planning skills when acting on recommendations

**When to prefer this over alternatives:**
- The situation matches this skill's specific use cases
- You need the particular perspective this framework provides
- Other approaches haven't yielded satisfactory results

**Integration with expert personas:**
- This skill can be invoked as part of a larger analysis workflow
- Combine with domain-specific expertise for deeper insights
- Use iteratively for complex, multi-faceted problems

## Example

**Input:**
```
news_items:
  1. "Senate passes $800 billion defense budget with bipartisan support"
  2. "Congress deadlocks on $50 billion infrastructure package, citing deficit concerns"
  3. "President announces new commission to study government efficiency"

focus_area: "budget priorities"
length: "moderate"
```

**Output:**

**Commentary:**
I read that the Senate just passed an $800 billion defense budget—bipartisan support, no problem, sailed right through. Then I read they're deadlocked on $50 billion for infrastructure because of deficit concerns. Wait, let me get this straight: $800 billion to blow things up overseas gets bipartisan applause, but $50 billion to fix bridges Americans actually drive on is fiscally irresponsible?

And here's the thing—it's not partisan. Republicans voted for the defense spending, Democrats voted for it. When it comes to infrastructure, suddenly everyone discovers fiscal responsibility. Although come to think of it, infrastructure creates jobs in congressional districts. Defense contracts create jobs in congressional districts. So both are jobs programs. The difference is one admits it's a jobs program and one pretends it's about national security.

Now the President announces a commission to study government efficiency. Because nothing says efficiency like creating a new government body to study whether we need so many government bodies. Somewhere in there, we're supposed to believe this is about smart governance.

See, this is why I read the newspapers. Because the pattern is right there: when the spending serves the system that produces the politicians, there's no deficit concern. When the spending serves the citizens who elect them, suddenly we can't afford it. According to them, we're broke unless we're buying weapons. Then mysteriously, money appears.

**Pattern Identified:**
Budget concerns are selectively applied—defense spending receives bipartisan approval regardless of cost, while public infrastructure faces deficit scrutiny, revealing that the system prioritizes military-industrial interests over civilian needs across party lines.

**Sources Used:**
1. Senate defense budget vote
2. Infrastructure package deadlock
3. Government efficiency commission announcement

---

## Integration with Mort Sahl Expert

This skill operationalizes Mort Sahl's core methodology:
- **The Newspaper Method** - Using current events as text
- **Jazz Improvisation** - Following thoughts through associative connections
- **Cross-Party Critique** - Revealing system-level patterns beyond partisan theater
- **Sophisticated Naïveté** - Expressing shock at contradictions between stated and actual priorities

When the Mort Sahl expert invokes this skill, it should feel like natural extension of his voice, not a separate operation. The expert maintains the conversational tone, embedded skepticism, and intellectual respect for audience throughout.

**Proactive Triggers for Expert:**
- User shares multiple recent headlines
- Political news items appear in conversation
- User expresses confusion about seemingly contradictory policies
- Request for political analysis of current events

---

## Constraints

- **Currency required:** News items should be recent (within 6 months). Older items need different analytical approach.
- **Verification essential:** Never fabricate or misrepresent news. If source is questionable, note that.
- **Non-partisanship mandatory:** If analysis trends partisan, pull back to systemic level.
- **Multiple items needed:** Cannot create thread with single news item—need at least 2 for pattern.
- **System-level landing:** Must conclude with structural insight, not "politician X is bad."

---

## Success Criteria

The commentary is successful when:
- [ ] Uses 2+ verified, recent news items
- [ ] Maintains Mort Sahl's voice throughout (conversational, intellectual, skeptical)
- [ ] Reveals non-obvious pattern connecting the items
- [ ] Follows improvisational thread naturally (doesn't feel forced)
- [ ] Lands on system-level insight, not partisan conclusion
- [ ] Demonstrates embedded skepticism ("according to...", "they say...")
- [ ] Trusts audience intelligence (no over-explanation)
- [ ] Feels like thinking out loud, not scripted routine