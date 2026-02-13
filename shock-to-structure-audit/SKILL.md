---
name: shock-to-structure-audit
description: Evaluate whether dark or controversial content is shock-for-shock's-sake or properly structured with misdirection and craft.
license: MIT
metadata:
  version: 1.0.4969
  author: sethmblack
repository: https://github.com/sethmblack/paks-skills
keywords:
- comedy
- shock-to-structure-audit
- structure
- transformation
- writing
---

# Shock-to-Structure Audit

Evaluate whether dark or controversial content is shock-for-shock's-sake or properly structured with misdirection and craft.

---

## Constraints
**Audit all submitted comedy objectively**, including highly controversial material. The goal is to distinguish between structured dark comedy and lazy shock tactics.

**REFUSE to audit:**
- Content that's clearly sincere hate speech or genuine calls for violence (not comedy)

---

## When to Use

Use this skill when:
- User asks "is this dark comedy or just offensive?"
- User provides controversial content and wants evaluation
- User requests "audit this for structure"
- User asks whether shock elements serve the comedy
- User wants to know if material crosses from comedy to mean-spiritedness

---

## Inputs

| Input | Required | Description | Validation |
|-------|----------|-------------|------------|
| `material` | Yes | Dark or controversial comedic content to audit | At least one complete joke or statement |
| `context` | No | Performance context (audience type, setting, etc.) | Optional background information |

---

## Workflow

### Step 1: Identify All Shock Elements

List every element in the material that could be considered shocking, offensive, or controversial.

**Shock elements include:**
- Dark topics (death, tragedy, violence, illness)
- Controversial subjects (race, religion, politics, sex)
- Taboo admissions (immoral thoughts, selfish motives)
- Offensive language or imagery

**Create a shock inventory:**
```
Shock Element 1: [description]
Shock Element 2: [description]
...
```

### Step 2: Evaluate Each Shock Element Against Structure Criteria

For each shock element, assess whether it meets the 4 criteria for structured dark comedy:

#### Criterion 1: Does the Shock Serve Joke Architecture?

**Question:** Is this shock element essential to the setup → reversal structure, or could you remove it without affecting the joke?

**Evaluation:**
- **PASS:** Shock is integral to the misdirection or punchline
- **FAIL:** Shock is decorative or gratuitous, doesn't serve the structure

**Example PASS:** "I'm afraid of flying. [pause] Not the crash—I'm afraid I'll survive and have to make small talk with other survivors."
- Shock element (dark thought about surviving crash) serves the reversal

**Example FAIL:** "I hate flying on those f***ing planes with all the f***ing idiots."
- Shock elements (profanity, insults) don't serve any joke structure—just ranting

#### Criterion 2: Is There Proper Misdirection?

**Question:** Does the material set up an expectation and then violate it, or is it just stating shocking things directly?

**Evaluation:**
- **PASS:** Clear setup → false direction → reversal architecture present
- **FAIL:** Direct shock statements without misdirection (just being offensive)

**Example PASS:** "I donate to charity every year. Feels good to help people. [pause] Plus the tax deduction is incredible."
- Sets up altruism expectation, reverses to selfishness

**Example FAIL:** "Poor people are lazy and deserve to suffer."
- Direct offensive statement, no setup or reversal

#### Criterion 3: Is the Language Economical?

**Question:** Is the shock delivered with precision, or is it padded with unnecessary details that telegraph the offensive direction?

**Evaluation:**
- **PASS:** Tight language, shock arrives unexpectedly
- **FAIL:** Bloated setup that clearly signals "offensive joke incoming"

**Example PASS:** "My girlfriend's getting too old for me. [pause] She's turning 30 next week."
- Economic setup, quick reversal

**Example FAIL:** "So I'm dating this girl and let me tell you, she's not getting any younger, if you know what I mean. I like them young, really young, you know? The younger the better, that's what I say. Anyway..."
- Bloated, telegraphs the offensive direction, no surprise

#### Criterion 4: Is There Confidence in Delivery?

**Question:** Does the material commit to the dark stance, or does it hedge with disclaimers and apologies?

**Evaluation:**
- **PASS:** Commits fully to the dark position without qualification
- **FAIL:** Softens with "I know this is wrong but..." or "Just kidding!" or "I'm a terrible person for saying this..."

**Example PASS:** "I've spent the past two years looking for my ex-girlfriend's killer. [pause] But no one will do it."
- Commits to the dark admission without apology

**Example FAIL:** "I know this is terrible and I shouldn't say it, but sometimes I think about... no, I can't say it. Okay, you want me to say it? I think about [shock element]. But I don't really mean it!"
- Hedges, apologizes, breaks character

### Step 3: Score Each Shock Element

For each shock element, assign a score:

```
Shock Element: [description]
├─ Serves Joke Architecture: PASS / FAIL
├─ Proper Misdirection: PASS / FAIL
├─ Economical Language: PASS / FAIL
└─ Confident Delivery: PASS / FAIL

Overall: [X/4 criteria passed]
```

### Step 4: Calculate Overall Material Score

**Scoring:**
- **4/4 PASS:** Structured dark comedy (shock serves craft)
- **3/4 PASS:** Mostly structured, minor issues
- **2/4 PASS:** Problematic, shock is doing too much work without structure
- **1/4 or 0/4 PASS:** Shock-for-shock's-sake, not comedy

### Step 5: Provide Verdict and Specific Fixes

**Verdict format:**

**PASS (Structured Dark Comedy):** This material uses shock elements in service of joke architecture. The darkness serves the comedy.

**FAIL (Shock-for-Shock's-Sake):** This material uses shock without proper structure. It's offensive without being funny because [specific reason].

**For FAIL verdicts, provide specific fixes:**

```
Issue: [criterion failed]
Fix: [specific structural change]
Rationale: [how this transforms shock into structured comedy]
```

---

## Outputs

| Output | Description |
|--------|-------------|
| Shock inventory | List of all shocking elements in the material |
| Criterion evaluation | PASS/FAIL for each of 4 criteria, per shock element |
| Overall score | X/4 criteria passed |
| Verdict | PASS (structured dark comedy) or FAIL (shock-for-shock's-sake) |
| Specific fixes (if FAIL) | Actionable improvements to add structure |

---

## Example Audit 1 (PASS)

**Input Material:**
"I love my grandmother. She's 93 years old, still sharp as a tack. She tells me stories about the Depression, about the war. She's seen so much. [pause] I'm gonna be so rich when she dies."

**Output:**

**Shock Inventory:**
- Shock Element 1: Thinking about grandmother's death
- Shock Element 2: Mercenary motive (inheritance)

**Criterion Evaluation:**

**Shock Element 1 & 2 (combined in same reversal):**
- Serves Joke Architecture: **PASS** - The inheritance motive is the punchline, essential to the reversal
- Proper Misdirection: **PASS** - Sets up loving, respectful grandson, reverses to mercenary motive
- Economical Language: **PASS** - Tight setup, no wasted words
- Confident Delivery: **PASS** - States the dark thought directly, no apology

Overall: **4/4 criteria passed**

**Overall Material Score: 4/4**

**Verdict: PASS (Structured Dark Comedy)**

This material uses shock elements (grandmother's death, inheritance greed) in service of misdirection architecture. The setup builds sympathy (loving grandson), the reversal reveals selfishness (waiting for inheritance). The darkness serves the comedy.

---

## Example Audit 2 (FAIL)

**Input Material:**
"You know what really grinds my gears? Fat people. They're just so fat and gross and lazy. I can't stand fat people. They should just stop eating so much. It's disgusting. Don't you think fat people are disgusting? I'm just being honest here."

**Output:**

**Shock Inventory:**
- Shock Element 1: Attacking fat people
- Shock Element 2: Calling people "disgusting"
- Shock Element 3: Claiming honesty as defense

**Criterion Evaluation:**

**Shock Element 1, 2, 3 (no structure to separate):**
- Serves Joke Architecture: **FAIL** - No joke structure present, just direct insults
- Proper Misdirection: **FAIL** - No setup or reversal, states offensive position directly
- Economical Language: **FAIL** - Repetitive, bloated, keeps restating the same insult
- Confident Delivery: **FAIL** - Asks for validation ("Don't you think...?"), uses "just being honest" as shield

Overall: **0/4 criteria passed**

**Overall Material Score: 0/4**

**Verdict: FAIL (Shock-for-Shock's-Sake)**

This material uses shock without structure. It's offensive without being funny because there's no misdirection, no reversal, no joke architecture—just direct insults masked as honesty.

**Specific Fixes:**

**Issue:** No misdirection - Direct attack instead of setup → reversal
**Fix:** Create a setup that seems sympathetic, then reverse it. Example: "I joined a gym recently. Everyone's so supportive, encouraging each other. It's really inspiring. [pause] I go there to feel better about myself by comparison."
**Rationale:** This creates misdirection (joining gym sounds positive) and reveals selfishness (using others to feel superior) without direct insults.

**Issue:** No joke architecture - Just complaint
**Fix:** Requires complete restructure with setup, planted expectation, and reversal. Current material has no salvageable joke structure.
**Rationale:** Shock only works in comedy when it serves a joke. Build the joke first, then add darkness.

**Issue:** Asks for validation - Breaks confidence
**Fix:** Remove "Don't you think...?" and "I'm just being honest." Commit to the position without asking permission.
**Rationale:** Dark comedy requires confidence. Asking for agreement undermines the delivery.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Material has no shock elements | Note: "This material contains no controversial or shocking elements. Nothing to audit for shock-vs-structure." |
| Material is sincere, not comedy | Clarify: "This doesn't appear to be comedy. The audit evaluates comedic structure, not sincere positions." |
| Material violates constitutional constraints | Refuse: "This appears to be genuine hate speech rather than dark comedy attempting joke structure." |
| Multiple bits to audit | Request focus: "This contains multiple distinct pieces. Should I audit them separately or evaluate the set as a whole?" |

---

## Integration with Anthony Jeselnik Expert

This skill enforces Jeselnik's core philosophy:

"It's not just about being offensive—you really have to be smart and clever within a joke."

The audit separates offensive-but-smart (structured dark comedy) from offensive-without-smart (shock-for-shock's-sake).

Jeselnik's principle: "The joke is king. You're not trying to make a social point or be shocking for shock's sake. Every dark element serves the joke structure. If it's not funny, it's not worth saying."

The 4 criteria directly map to Jeselnik's standards:
1. Serves joke architecture = "The joke is king"
2. Proper misdirection = "You really have to be smart and clever"
3. Economical language = Economy of language principle
4. Confident delivery = "Confidence is non-negotiable"

---

## Notes

- This audit is structural, not moral—it evaluates whether shock serves comedy, not whether topics are appropriate
- A joke can PASS the audit and still be too offensive for certain audiences (that's a context decision)
- A joke can FAIL the audit but still get laughs (from shock value alone, not structure)
- The goal is to identify whether the comedian is using craft or just being mean
- Material can partially pass (2-3 criteria)—provide specific fixes for the failed criteria

## Example

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].