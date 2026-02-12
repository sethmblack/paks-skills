---
name: test-prompt
description: Validate prompts included in the book by running them against test cases
  and verifying they produce expected outputs.
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- test-prompt
- writing
---

# Test Prompt

Validate prompts included in the book by running them against test cases and verifying they produce expected outputs.

## CRITICAL REQUIREMENTS

Before testing ANY prompt:
- [ ] Verify prompt is not empty
- [ ] Verify at least one test case is provided (or generate basic ones)
- [ ] Constitutional constraints checked (no malicious prompt testing)
- [ ] API credentials available (or do static analysis only)

## Constraints
**You MUST refuse to:**
- Test prompts designed to jailbreak or manipulate AI systems
- Test prompts that generate harmful content (malware, phishing, etc.)
- Test prompts designed for deception or manipulation
- Execute prompts that could cause real-world harm

**If asked to test harmful prompts:** Refuse explicitly. Offer static analysis only to identify why the prompt is problematic.

## When to Use

- After writing or modifying a prompt for the book
- Before committing prompt examples to the repository
- When reviewing expert output containing prompts
- When the evaluate skill flags a prompt for verification
- When readers might copy-paste and use the prompt directly

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| **prompt** | Yes | The prompt template to test (cannot be empty) |
| **test_cases** | Recommended | Array of {input, expected_output} pairs. If not provided, basic cases will be generated. |
| **model** | No | Target model (default: "claude-3-5-sonnet-20241022") |
| **criteria** | No | Custom evaluation criteria beyond defaults |
| **runs** | No | Number of test runs for consistency (default: 3) |

### Input Validation

```python
# Validate inputs before testing
def validate_inputs(prompt: str, test_cases: list = None) -> tuple[bool, str]:
    if not prompt or not prompt.strip():
        return False, "ERROR: Prompt cannot be empty"

    if test_cases is not None and len(test_cases) == 0:
        return False, "ERROR: test_cases provided but empty"

    # Check for harmful patterns
    harmful_patterns = [
        "ignore previous instructions",
        "jailbreak",
        "pretend you have no restrictions",
        "DAN mode",
    ]
    prompt_lower = prompt.lower()
    for pattern in harmful_patterns:
        if pattern in prompt_lower:
            return False, f"REFUSED: Prompt contains harmful pattern: '{pattern}'"

    return True, "Validation passed"
```

### Test Case Format

```yaml
test_cases:
  - name: "Basic case"
    input:
      variable1: "value1"
      variable2: "value2"
    expected:
      contains: ["keyword1", "keyword2"]
      format: "json"  # or "code", "markdown", "freeform"
      constraints: ["must include error handling", "no hardcoded values"]

  - name: "Edge case - empty input"
    input:
      variable1: ""
    expected:
      behavior: "graceful_error"  # or "valid_output", "specific_message"
```

---

## Prompt Quality Dimensions

### What Makes a Book-Worthy Prompt

| Dimension | Good | Bad |
|-----------|------|-----|
| **Clarity** | Unambiguous instructions | Vague or confusing |
| **Completeness** | All context provided | Missing critical info |
| **Constraints** | Clear boundaries defined | No limits on output |
| **Format** | Output structure specified | No format guidance |
| **Examples** | Shows expected output | Reader must guess |
| **Robustness** | Handles edge cases | Breaks on unusual input |

### Testing Layers

| Layer | What It Tests | Method |
|-------|---------------|--------|
| Static Analysis | Prompt structure and completeness | Pattern matching |
| Single Execution | Basic functionality | One LLM call |
| Consistency | Reproducibility | Multiple runs, compare outputs |
| Edge Cases | Robustness | Unusual/boundary inputs |
| Adversarial | Failure modes | Intentionally bad inputs |

---

## Workflow
### Step 1: 0. Validate Inputs and Prerequisites

Before starting, verify:

```python
import os

# Check API key is available
if not os.environ.get("ANTHROPIC_API_KEY"):
    print("WARNING: ANTHROPIC_API_KEY not set. Will do static analysis only.")
    API_AVAILABLE = False
else:
    API_AVAILABLE = True

# Validate prompt and test cases
valid, message = validate_inputs(prompt, test_cases)
if not valid:
    print(message)
    exit(1)

# If no test cases, generate basic ones
if not test_cases:
    test_cases = generate_basic_test_cases(prompt)

def generate_basic_test_cases(prompt: str) -> list:
    """Generate basic test cases from prompt structure."""
    import re

    # Extract template variables
    variables = re.findall(r'\{\{(\w+)\}\}', prompt)

    if not variables:
        # No variables, create a simple execution test
        return [{
            "name": "Basic execution",
            "input": {},
            "expected": {"behavior": "valid_output"}
        }]

    # Create basic case with sample values
    basic_input = {var: f"sample_{var}_value" for var in variables}

    # Create empty input case for robustness
    empty_input = {var: "" for var in variables}

    return [
        {
            "name": "Basic case with sample values",
            "input": basic_input,
            "expected": {"behavior": "valid_output"}
        },
        {
            "name": "Edge case - empty inputs",
            "input": empty_input,
            "expected": {"behavior": "graceful_error"}
        }
    ]
```

### Step 2: 1. Parse the Prompt

Identify prompt components:

```markdown
## Prompt Analysis

**Template Variables:** {list variables like {{user_input}}}
**Has System Context:** {yes/no}
**Has Output Format:** {yes/no}
**Has Examples:** {yes/no}
**Has Constraints:** {yes/no}
**Estimated Token Count:** {approximate}
```

### 2. Static Quality Check

Before execution, check for common issues:

```markdown
## Static Analysis Checklist

### Structure
- [ ] Clear role/identity statement (if needed)
- [ ] Context provided for the task
- [ ] Explicit instructions on what to do
- [ ] Output format specified
- [ ] Constraints or boundaries defined

### Variables
- [ ] All template variables are used
- [ ] Variable names are descriptive
- [ ] Default handling for optional variables

### Common Anti-Patterns
- [ ] No "be creative" without constraints
- [ ] No "do your best" vagueness
- [ ] No undefined acronyms or jargon
- [ ] No implicit assumptions about input format
- [ ] No missing error handling instructions
```

### 3. Prepare Test Cases

For each test case, fill in the template:

```python
def fill_template(prompt_template: str, variables: dict) -> str:
    """Fill prompt template with test case variables."""
    result = prompt_template
    for key, value in variables.items():
        result = result.replace(f"{{{{{key}}}}}", str(value))
    return result

# Example
prompt = "Analyze this error log and identify the root cause:\n\n{{error_log}}\n\nProvide your analysis in JSON format."
filled = fill_template(prompt, {"error_log": "ConnectionTimeout: Failed to connect to database"})
```

### 4. Execute Test Cases

Run each test case against the LLM (skip if API unavailable):

```python
import anthropic
from anthropic import APIError, RateLimitError

client = anthropic.Anthropic()

def run_test_case(prompt: str, test_case: dict, model: str = "claude-3-5-sonnet-20241022") -> dict:
    """Execute a single test case with error handling."""
    filled_prompt = fill_template(prompt, test_case["input"])

    # Estimate tokens (rough: ~4 chars per token)
    estimated_input_tokens = len(filled_prompt) // 4

    try:
        response = client.messages.create(
            model=model,
            max_tokens=1024,
            messages=[{"role": "user", "content": filled_prompt}]
        )

        return {
            "name": test_case["name"],
            "input": test_case["input"],
            "output": response.content[0].text,
            "expected": test_case["expected"],
            "tokens_used": {
                "input": response.usage.input_tokens,
                "output": response.usage.output_tokens
            },
            "error": None
        }
    except RateLimitError:
        return {"name": test_case["name"], "error": "Rate limited. Retry later."}
    except APIError as e:
        return {"name": test_case["name"], "error": f"API error: {e}"}
```

### 5. Evaluate Results

For each test result, check against expected criteria:

```python
def evaluate_result(result: dict) -> dict:
    """Evaluate test result against expected criteria."""
    # Handle API errors
    if result.get("error"):
        return {"passed": False, "failures": [result["error"]], "needs_review": False}

    expected = result["expected"]
    output = result["output"]
    passed = True
    failures = []

    # Check "behavior" criteria
    if "behavior" in expected:
        if expected["behavior"] == "valid_output":
            # Just check that we got a non-empty response
            if not output or not output.strip():
                passed = False
                failures.append("Expected valid output but got empty response")
        elif expected["behavior"] == "graceful_error":
            # Check output acknowledges the issue
            error_indicators = ["cannot", "invalid", "missing", "error", "need more"]
            if not any(ind in output.lower() for ind in error_indicators):
                failures.append("Manual check: Verify graceful error handling")
        elif expected["behavior"] == "requests_more_info":
            question_indicators = ["?", "please provide", "can you", "what is"]
            if not any(ind in output.lower() for ind in question_indicators):
                failures.append("Expected prompt to request more information")

    # Check "contains" criteria
    if "contains" in expected:
        for keyword in expected["contains"]:
            if keyword.lower() not in output.lower():
                passed = False
                failures.append(f"Missing expected content: '{keyword}'")

    # Check "format" criteria
    if "format" in expected:
        if expected["format"] == "json":
            try:
                import json
                json.loads(output)
            except json.JSONDecodeError:
                passed = False
                failures.append("Output is not valid JSON")
        elif expected["format"] == "code":
            # Check for code block markers
            if "```" not in output:
                passed = False
                failures.append("Output missing code block formatting")

    # Check "constraints" criteria
    if "constraints" in expected:
        for constraint in expected["constraints"]:
            # Manual evaluation needed - flag for review
            failures.append(f"Manual check needed: {constraint}")

    # Check "not_contains" criteria (things that should NOT appear)
    if "not_contains" in expected:
        for forbidden in expected["not_contains"]:
            if forbidden.lower() in output.lower():
                passed = False
                failures.append(f"Contains forbidden content: '{forbidden}'")

    return {
        "passed": passed and len([f for f in failures if "Manual check" not in f]) == 0,
        "failures": failures,
        "needs_review": any("Manual check" in f for f in failures)
    }
```

### 6. Consistency Testing (if runs > 1)

Run multiple times and compare:

```python
def test_consistency(prompt: str, test_case: dict, runs: int = 3) -> dict:
    """Test prompt consistency across multiple runs."""
    outputs = []

    for i in range(runs):
        result = run_test_case(prompt, test_case)
        outputs.append(result["output"])

    # Calculate similarity (simple approach)
    # For structured output, check key presence
    # For freeform, check semantic similarity

    consistent_elements = []
    inconsistent_elements = []

    # Check if all outputs have same structure
    if test_case["expected"].get("format") == "json":
        import json
        keys_sets = []
        for output in outputs:
            try:
                parsed = json.loads(output)
                keys_sets.append(set(parsed.keys()) if isinstance(parsed, dict) else set())
            except:
                keys_sets.append(set())

        common_keys = set.intersection(*keys_sets) if keys_sets else set()
        all_keys = set.union(*keys_sets) if keys_sets else set()
        consistency_score = len(common_keys) / len(all_keys) if all_keys else 1.0
    else:
        # For text, check if key expected elements appear in all outputs
        if "contains" in test_case["expected"]:
            for keyword in test_case["expected"]["contains"]:
                found_in = sum(1 for o in outputs if keyword.lower() in o.lower())
                if found_in == len(outputs):
                    consistent_elements.append(keyword)
                else:
                    inconsistent_elements.append(f"{keyword} ({found_in}/{len(outputs)})")

        consistency_score = len(consistent_elements) / (len(consistent_elements) + len(inconsistent_elements)) if (consistent_elements or inconsistent_elements) else 1.0

    return {
        "runs": runs,
        "consistency_score": consistency_score,
        "consistent_elements": consistent_elements,
        "inconsistent_elements": inconsistent_elements,
        "outputs": outputs  # For manual review
    }
```

### 7. Generate Test Report

Use this template, replacing placeholders with actual results:

```markdown
## Prompt Test Report: [prompt name or identifier]

### Prompt Under Test
\`\`\`
[the prompt template]
\`\`\`

### Static Analysis
| Check | Status |
|-------|--------|
| Has clear instructions | ✓/✗ |
| Output format specified | ✓/✗ |
| Variables documented | ✓/✗ |
| Constraints defined | ✓/✗ |
| No anti-patterns | ✓/✗ |

### Test Case Results

| Test Case | Result | Details |
|-----------|--------|---------|
| [name] | PASS/FAIL | [failures or "All checks passed"] |

### Consistency (if tested with runs > 1)
- **Score:** [0-100]%
- **Consistent elements:** [list]
- **Inconsistent elements:** [list]

### Token Usage
| Metric | Value |
|--------|-------|
| Total input tokens | [sum] |
| Total output tokens | [sum] |
| Estimated cost | $[calculated based on model pricing] |

### Sample Outputs

**Test Case: [name]**
Input:
\`\`\`
[input variables]
\`\`\`

Output:
\`\`\`
[actual LLM output]
\`\`\`

Expected:
\`\`\`
[expected criteria]
\`\`\`

### Overall: [PASS / FAIL / NEEDS REVIEW]

### Issues Found
| Issue | Severity | Suggestion |
|-------|----------|------------|
| [issue] | High/Medium/Low | [fix] |

### Recommendations
1. [recommendation]
```

---

## Common Prompt Issues and Fixes

| Issue | Example | Fix |
|-------|---------|-----|
| No output format | "Analyze this error" | Add "Respond in JSON with keys: cause, severity, fix" |
| Vague instruction | "Help with this code" | Specify: "Review for bugs", "Optimize for performance", etc. |
| Missing context | "Fix the bug" | Include: language, framework, what the code should do |
| No constraints | "Write a script" | Add: length limits, required features, forbidden approaches |
| Ambiguous variables | `{{data}}` | Use descriptive: `{{error_log_text}}`, `{{user_csv_data}}` |
| No error handling | Assumes valid input | Add: "If the input is invalid, respond with..." |
| Too open-ended | "Be creative" | Define boundaries: "Choose from: A, B, or C approach" |

---

## Test Case Templates

### For Code Generation Prompts

```yaml
test_cases:
  - name: "Basic functionality"
    input:
      task: "Read CSV file"
      language: "python"
    expected:
      contains: ["import", "csv", "open("]
      format: "code"
      not_contains: ["# TODO", "..."]

  - name: "Error handling"
    input:
      task: "Read CSV file with error handling"
      language: "python"
    expected:
      contains: ["try", "except", "FileNotFoundError"]
      format: "code"
```

### For Data Extraction Prompts

```yaml
test_cases:
  - name: "Structured extraction"
    input:
      text: "John Smith, age 32, works at Acme Corp as Senior Engineer since 2019"
    expected:
      format: "json"
      contains: ["name", "age", "company", "title"]

  - name: "Missing data handling"
    input:
      text: "Jane Doe works somewhere"
    expected:
      format: "json"
      contains: ["name"]
      # Should handle missing fields gracefully
```

### For Analysis Prompts

```yaml
test_cases:
  - name: "Error log analysis"
    input:
      log: "ERROR 2024-01-15 Connection refused: localhost:5432"
    expected:
      contains: ["database", "connection", "port 5432"]
      constraints: ["identifies root cause", "suggests fix"]

  - name: "Ambiguous error"
    input:
      log: "Error occurred"
    expected:
      behavior: "requests_more_info"  # Should ask for more context
```

---

## Outputs

| Output | Format | Destination |
|--------|--------|-------------|
| Test report | Markdown | User message |
| Pass/Fail verdict | Boolean | For evaluate skill |
| Issue list | Structured | For improve skill if FAIL |
| Sample outputs | Text | For documentation/examples |



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


## Constraints

- **Real LLM calls.** Don't simulate—actually run the prompt.
- **Document costs.** Note approximate token usage for test suite.
- **Preserve original prompt.** Testing doesn't modify; fixes go through improve skill.
- **Reproducibility matters.** Use temperature=0 when consistency is critical.
- **Test what readers will use.** If the book shows a prompt, test exactly that prompt.

### Temperature Guidance

```python
# For consistency testing (runs > 1), use temperature=0
response = client.messages.create(
    model=model,
    max_tokens=1024,
    temperature=0,  # Deterministic for testing
    messages=[{"role": "user", "content": filled_prompt}]
)

# For single-run creative prompts, default temperature is fine
# Only add temperature=0 when you need reproducible results
```

## Error Handling

| Situation | Response |
|-----------|----------|
| API unavailable | Note limitation, do static analysis only |
| Rate limited | Wait and retry, or reduce test cases |
| Prompt too long | Note token count, suggest shortening |
| No test cases provided | Create basic test cases from prompt context |
| Output unparseable | Mark as FAIL, include raw output for review |

## Success Criteria

Testing is complete when:

1. Static analysis has been performed
2. All test cases have been executed
3. Results are evaluated against expected criteria
4. Consistency has been assessed (if multiple runs)
5. Clear pass/fail verdict with evidence
6. Actionable recommendations if issues found

### Verdict Definitions

| Verdict | Criteria |
|---------|----------|
| **PASS** | All test cases pass. Static analysis clean. Consistency ≥80%. |
| **NEEDS REVIEW** | Some test cases pass but constraints need manual verification. |
| **FAIL** | Any test case fails format/contains checks OR static analysis finds anti-patterns. |

---

## Example Test Session

**Prompt Under Test:**

```
You are an IT automation assistant. Analyze the following error log and provide:
1. The root cause of the error
2. Severity level (critical, high, medium, low)
3. Recommended fix

Error log:
{{error_log}}

Respond in JSON format with keys: root_cause, severity, recommended_fix
```

**Test Cases:**

```yaml
test_cases:
  - name: "Database connection error"
    input:
      error_log: "2024-01-15 10:23:45 ERROR ConnectionRefused: Unable to connect to PostgreSQL at localhost:5432 - Connection refused"
    expected:
      format: "json"
      contains: ["root_cause", "severity", "recommended_fix"]
      constraints: ["mentions database/PostgreSQL", "suggests checking if DB is running"]

  - name: "Permission denied error"
    input:
      error_log: "PermissionError: [Errno 13] Permission denied: '/etc/passwd'"
    expected:
      format: "json"
      contains: ["root_cause", "severity", "recommended_fix"]
      constraints: ["mentions permissions", "suggests chmod or running as different user"]

  - name: "Vague error"
    input:
      error_log: "Error: Something went wrong"
    expected:
      format: "json"
      constraints: ["acknowledges limited information", "asks for more context or suggests logging"]
```

**Test Report:**

```markdown
## Prompt Test Report: Error Log Analyzer

### Prompt Under Test
(See above)

### Static Analysis
| Check | Status |
|-------|--------|
| Has clear instructions | ✓ |
| Output format specified | ✓ |
| Variables documented | ✓ |
| Constraints defined | ✓ |
| No anti-patterns | ✓ |

### Test Case Results

| Test Case | Result | Details |
|-----------|--------|---------|
| Database connection error | PASS | All checks passed |
| Permission denied error | PASS | All checks passed |
| Vague error | NEEDS REVIEW | Manual check: acknowledges limited information |

### Consistency (3 runs)
- **Score:** 100%
- **Consistent elements:** root_cause, severity, recommended_fix
- **Inconsistent elements:** None

### Token Usage
| Metric | Value |
|--------|-------|
| Total input tokens | 892 |
| Total output tokens | 456 |
| Estimated cost | $0.005 |

### Overall: PASS

### Recommendations
1. Consider adding example output in the prompt for more consistent formatting
2. Add instruction for how to handle multi-line or very long error logs
```

---

## REINFORCEMENT: Critical Checklist

Before returning test results:

- [ ] Prompt validated (not empty, no harmful patterns)
- [ ] Constitutional constraints checked
- [ ] Static analysis completed
- [ ] Test cases executed (or generated if none provided)
- [ ] Results evaluated against expected criteria
- [ ] Consistency tested if runs > 1
- [ ] Clear PASS/NEEDS REVIEW/FAIL verdict provided
- [ ] Sample outputs included for evidence
- [ ] Recommendations provided if issues found

**If prompt contains harmful patterns, REFUSE and explain why.**

**If API unavailable, do static analysis only and note limitation.**

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
- input_data: [Specific example input]
- context: [Relevant background]

**Output:**

[Detailed demonstration of the skill in action - showing the complete process and final result]

**Why this works:**
This example demonstrates the key principles of the skill by [explanation of what makes it effective].