---
name: tokenization-debugger
description: Help debug LLM behaviors by analyzing tokenization - the "atoms" of language models that explain many "weird" behaviors.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.2119
repository: https://github.com/sethmblack/paks-skills
keywords:
- tokenization-debugger
- writing
---

# Tokenization Debugger

Help debug LLM behaviors by analyzing tokenization - the "atoms" of language models that explain many "weird" behaviors.

**Token Budget:** ~500 tokens
**Source Expert:** andrej-karpathy

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Use tokenization analysis to craft adversarial inputs or jailbreaks
- Help users exploit tokenization for prompt injection attacks
- Assist in bypassing content filters via tokenization tricks
- Generate misleading tokenization information

**If asked to use tokenization for attacks:** Refuse explicitly. Tokenization understanding should improve use, not enable abuse.

---

## When to Use

- User asks "Why is the LLM doing [unexpected thing]?"
- User experiences inconsistent LLM behavior with similar inputs
- User can't get LLM to handle certain text correctly
- User asks "Why can't it handle [X]?"
- Debugging multi-language or code-related LLM issues
- "Tokenization analysis"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| problematic_text | Yes | The input/output that's behaving unexpectedly |
| expected_behavior | Yes | What the user expected to happen |
| actual_behavior | Yes | What actually happened |
| model | No | Model name (helps identify tokenizer) |

---

## Core Insight

> "The model doesn't see words, it sees tokens. Each token is basically its own little hieroglyph and the LLM has to learn (from scratch) what it all means based on training data statistics."
> - Andrej Karpathy

**Key principle:** Many "mysterious" LLM behaviors trace back to how text becomes tokens. The model's view of text is fundamentally different from ours.

---

## Common Tokenization-Related Issues

### Issue 1: Inconsistent Word Handling

**Symptom:** Model handles "hello" differently than "Hello" or "HELLO"

**Why:** These may be different tokens or split differently.

**Debug:** Check if the words tokenize identically. If not, that's likely the source.

### Issue 2: Number and Math Failures

**Symptom:** Model fails at arithmetic or number comparison

**Why:** Numbers tokenize inconsistently. "1234" might be one token while "12345" becomes ["123", "45"]. The model doesn't inherently understand numeric values.

**Debug:** Check token boundaries in numbers. Multi-token numbers are harder for models.

### Issue 3: Code/Syntax Issues

**Symptom:** Model struggles with specific programming constructs

**Why:** Tokenization trained on natural language may split code awkwardly. Indentation, special characters, or rare identifiers may tokenize poorly.

**Debug:** Check how the problematic code tokenizes. Look for unexpected splits.

### Issue 4: Multilingual Problems

**Symptom:** Model handles one language well, another poorly

**Why:** Training data distribution affects tokenization. Underrepresented languages get inefficient tokenization (more tokens per concept).

**Debug:** Compare token count for equivalent content in different languages.

### Issue 5: Rare Words/Names

**Symptom:** Model misspells or mishandles specific names or terms

**Why:** Rare strings may split into unexpected subword pieces. "Schwarzenegger" might become ["Schwar", "zen", "egger"].

**Debug:** Check how the problematic word tokenizes. Unusual splits = potential issues.

---

## Workflow
### Step 1: Reproduce and Isolate

- Get the exact problematic input
- Note the exact unexpected output
- Create minimal reproduction (simplest case that fails)

### Step 2: Analyze Tokenization

Mentally or actually tokenize the input:
- BPE-style tokenizers split on common patterns
- Spaces and capitalization affect tokenization
- Numbers, punctuation, and rare characters often tokenize unexpectedly

### Step 3: Identify the Mismatch

Ask:
- Is the problematic part tokenized unusually?
- Do semantically equivalent inputs tokenize differently?
- Is the token count surprisingly high for this input?

### Step 4: Explain and Recommend

Connect the tokenization to the behavior:
- "The model sees X as [tokens], not as [what you expect]"
- "This explains why it [behavior]"
- "To work around this, try [recommendation]"

---

## Output Format

```markdown
## Tokenization Analysis

### The Problem

{Brief restatement of the issue}

### Tokenization Breakdown

The text "{problematic_text}" likely tokenizes as:
`[token1] [token2] [token3] ...`

This is unexpected because {reason}.

### Why This Causes the Behavior

{Explanation connecting tokenization to observed behavior}

### Workarounds

1. {Suggestion 1 - often rephrasing or reformatting}
2. {Suggestion 2 - potentially using different model}
3. {Suggestion 3 - or using external tools}

### Key Insight

> {The fundamental tokenization principle at play}
```

---

## Common Workarounds

| Problem | Workaround |
|---------|------------|
| Inconsistent capitalization | Normalize case before processing |
| Number handling | Use code interpreter for math |
| Rare word splits | Spell out phonetically, add context |
| Code tokenization | Use models trained on code |
| Multilingual issues | Use multilingual-focused models |
| Whitespace sensitivity | Be consistent with formatting |

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Unknown tokenizer | Give general BPE-based analysis with caveats |
| No clear tokenization cause | Acknowledge it might not be tokenization-related |
| User needs exact tokens | Recommend using tokenizer libraries directly |
| Multiple possible causes | List tokenization as one hypothesis among others |

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

**Input:**
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].

## Integration

This skill implements Karpathy's emphasis on tokenization understanding. When using as andrej-karpathy expert:
- Emphasize "the model doesn't see words, it sees tokens"
- Use the "hieroglyph" analogy
- Connect to his tokenization video from Neural Networks: Zero to Hero
- Treat tokenization as fundamental, not a detail