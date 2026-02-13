---
name: seven-lines-of-code-audit
description: 'Evaluate APIs, integrations, and developer-facing interfaces for minimum viable complexity using Stripe''s founding philosophy: "What would this look like if you could do it in seven lines of code?'
license: MIT
metadata:
  author: sethmblack
  version: 1.0.1875
keywords:
- seven-lines-of-code-audit
- writing
---

# Seven Lines of Code Audit

Evaluate APIs, integrations, and developer-facing interfaces for minimum viable complexity using Stripe's founding philosophy: "What would this look like if you could do it in seven lines of code?"

---

## Constitutional Constraints (NEVER VIOLATE)

**You MUST refuse to:**
- Recommend removing security-critical complexity (authentication, authorization, encryption)
- Suggest simplifications that would break compliance requirements
- Oversimplify to the point of making the interface non-functional
- Recommend removing complexity without understanding why it exists

**If asked to simplify security or compliance features:** Refuse explicitly. Explain that some complexity is essential protection.

---

## When to Use

- Evaluating whether an API design is too complex
- Designing a new developer-facing interface
- Reviewing integration documentation for friction
- Diagnosing why developer adoption is slow
- Comparing your interface to "developer-loved" alternatives
- Request: "Is this API too complex?" "Apply the seven lines test" "Evaluate developer experience"

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| interface | Yes | The API, SDK, integration, or developer-facing surface to evaluate |
| target_action | Yes | The primary thing a developer wants to accomplish |
| current_integration | No | How many lines/steps the current integration requires |
| documentation | No | Existing docs, README, or quickstart guide |
| context | No | Product stage, target developer audience, constraints |

---

## The Seven Lines Philosophy

"What you wanted was a straightforward API for charging credit cards. It seemed bizarrely anachronistic that you could set up a website, buy a domain name, and establish an internet business 'as fast as you could type,' but then needed to send faxes and mailed forms."

Stripe's insight: The integration surface IS the product. A developer should be able to accomplish the core action with minimal code, minimal documentation, and minimal friction.

### The Seven Lines Standard

The number "seven" is a proxy for:
- **Minimal cognitive load** - A developer can understand the entire integration at a glance
- **Copy-paste ready** - Can be added to a project in minutes, not hours
- **No hidden prerequisites** - Works immediately, doesn't require separate setup
- **Durability** - Once integrated, shouldn't need to be touched for years

### The Four Questions

1. **What is the absolute minimum integration surface?**
2. **What would this look like starting from scratch with no legacy?**
3. **Can the developer achieve their goal without reading documentation?**
4. **Is complexity hidden, not removed?**

---

## Workflow

### Step 1: Identify the Core Action

What is the ONE thing a developer most wants to do?

| Question | Answer |
|----------|--------|
| Primary action | [What the developer wants to accomplish] |
| Current line count | [How many lines it takes now] |
| Current time to first success | [Minutes/hours to working integration] |
| Documentation required | [How much reading before first success] |

### Step 2: Count the Friction Points

Map every step between "developer decides to integrate" and "first successful action":

| Step | Type | Essential? | Lines/Time |
|------|------|------------|------------|
| [Step 1] | Setup / Config / Code / Auth | Yes/No | [Cost] |
| [Step 2] | ... | ... | ... |

**Friction Types:**
- **Setup friction** - Installing, configuring, getting credentials
- **Cognitive friction** - Understanding concepts before writing code
- **Code friction** - Lines of code required
- **Auth friction** - Authentication and authorization complexity
- **Error friction** - Unclear error messages, hard to debug

### Step 3: Apply the Seven Lines Test

Can the core action be accomplished in approximately seven lines of clear, readable code?

**If NO:** What is preventing it?

| Blocker | Why It Exists | Could It Be Hidden? |
|---------|---------------|---------------------|
| [Blocker 1] | [Reason] | [Yes/No - How] |
| [Blocker 2] | [Reason] | [Yes/No - How] |

**Key Insight:** The goal is not to eliminate complexity but to hide it. Stripe's seven lines hide enormous complexity in payments, compliance, fraud detection. The developer doesn't see it.

### Step 4: Benchmark Against Excellence

| Metric | Current | Seven Lines Standard | Gap |
|--------|---------|---------------------|-----|
| Lines of code | [N] | ~7 for core action | [+/-] |
| Time to first success | [X min/hrs] | <5 minutes | [+/-] |
| Docs required before start | [Pages] | 0 (can start immediately) | [+/-] |
| Concepts to understand first | [N] | 1-2 max | [+/-] |
| Error message clarity | [Rating] | Self-explanatory | [+/-] |

### Step 5: Generate Recommendations

For each gap, provide specific recommendations.

---

## Output Format

```markdown
## Seven Lines of Code Audit: [Interface Name]

### The Core Action
**What developers want:** [One sentence]
**Current integration:** [Lines/steps required]
**Seven Lines Target:** [What it should look like]

### Friction Map

| Step | Type | Essential? | Friction Cost | Recommendation |
|------|------|------------|---------------|----------------|
| [Step] | [Type] | [Y/N] | [High/Med/Low] | [Action] |

### The Seven Lines Gap

**Current state:** [Lines of code / steps]
**Target state:** ~7 lines for core action
**Gap analysis:** [Why the gap exists]

### Complexity Audit

| Complexity | Currently Visible? | Should Be Hidden? | How to Hide |
|------------|-------------------|-------------------|-------------|
| [Complex thing] | Yes/No | Yes/No | [Approach] |

### Recommendations

#### Immediate (< 1 week)
1. [Specific, actionable recommendation]
2. [Specific, actionable recommendation]

#### Short-term (< 1 month)
1. [Specific, actionable recommendation]
2. [Specific, actionable recommendation]

#### Strategic (< 1 quarter)
1. [Specific, actionable recommendation]

### The Seven Lines Version

```[language]
// What it SHOULD look like
[Ideal ~7 line integration]
```

### Collison Test

Would Patrick Collison look at this and say "developers will love this"?
- [ ] Can be integrated without reading docs
- [ ] Core action in ~7 lines
- [ ] Errors are self-explanatory
- [ ] Works immediately after copy-paste
- [ ] Won't need to be touched for years

**Verdict:** PASSES / NEEDS WORK / FAILS
```

---

## Constraints

- Do not recommend removing essential security (auth, encryption, validation)
- Do not sacrifice correctness for brevity
- Do not ignore platform/language constraints
- Some complexity cannot be hidden and must be accepted
- Enterprise/compliance features may legitimately require more steps

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Interface is already minimal | Celebrate it. Note what makes it excellent. |
| Complexity is genuinely essential | Acknowledge it. Focus on hiding, not removing. |
| No clear "core action" | Help identify what developers most commonly need. |
| Multiple core actions | Audit each separately. |
| Legacy constraints | Note them but still define the ideal state. |

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

**Input:** "Evaluate our webhook integration. Developers complain it's too hard to set up."

**Output:**



**Why this works:**

This example demonstrates the key principles of the skill in action. The approach is effective because:
- It follows the systematic workflow outlined above
- It shows concrete application of the framework
- It produces actionable, specific outputs rather than vague generalizations
- The analysis is grounded in observable details
- The recommendations are prioritized and implementable

**Alternative applications:**

This same approach can be applied to:
- Different contexts within the same domain
- Related but distinct problem types
- Scaled up or down depending on scope
- Combined with complementary analytical frameworks


## Seven Lines of Code Audit: Webhook Integration

### The Core Action
**What developers want:** Receive events when something happens in your system
**Current integration:** 47 lines + separate dashboard configuration + HMAC verification setup
**Seven Lines Target:** Subscribe to events with a URL and start receiving them

### Friction Map

| Step | Type | Essential? | Friction Cost | Recommendation |
|------|------|------------|---------------|----------------|
| Create dashboard account | Setup | No | High | Allow API-only setup |
| Navigate to webhook settings | Setup | No | Medium | CLI or API creation |
| Configure endpoint URL | Config | Yes | Low | Keep, simplify |
| Select event types | Config | Yes (but...) | Medium | Default to all, filter later |
| Copy signing secret | Auth | Yes | Medium | Auto-inject via SDK |
| Implement HMAC verification | Code | Yes | High | SDK handles automatically |
| Parse event payload | Code | Yes | Medium | Typed event objects |
| Acknowledge receipt | Code | Yes | Low | Keep |

### The Seven Lines Gap

**Current state:** 47 lines of code + dashboard setup + understanding HMAC
**Target state:** ~7 lines for receiving and handling an event
**Gap analysis:** Authentication complexity is visible to developers. Event type selection happens upfront instead of in code. No SDK abstraction for common patterns.

### Complexity Audit

| Complexity | Currently Visible? | Should Be Hidden? | How to Hide |
|------------|-------------------|-------------------|-------------|
| HMAC verification | Yes (developer implements) | Yes | SDK middleware |
| Event parsing | Partially | Yes | Typed event classes |
| Retry logic | Yes (docs) | Yes | Handled by SDK |
| Dashboard configuration | Yes | Partially | API/CLI alternatives |

### Recommendations

#### Immediate (< 1 week)
1. Add SDK method: `stripe.webhooks.constructEvent(payload, signature)` that handles all verification
2. Create single-command CLI: `stripe webhooks create --url=https://...`

#### Short-term (< 1 month)
1. Default to all event types, let developers filter in code
2. Add typed event objects so IDEs provide autocomplete
3. Create "webhook-in-60-seconds" quickstart that actually takes 60 seconds

#### Strategic (< 1 quarter)
1. Consider webhook-as-a-service layer that handles parsing/verification entirely
2. Add local testing mode that tunnels webhooks to localhost

### The Seven Lines Version

```python
import stripe

@app.route('/webhook', methods=['POST'])
def webhook():
    event = stripe.Webhook.construct(request)  # Verification handled

    if event.type == 'payment.completed':
        handle_payment(event.data)

    return '', 200
```

### Collison Test

Would Patrick Collison look at this and say "developers will love this"?
- [ ] Can be integrated without reading docs - NO (HMAC requires docs)
- [ ] Core action in ~7 lines - NO (47 lines currently)
- [ ] Errors are self-explanatory - PARTIAL
- [ ] Works immediately after copy-paste - NO (requires dashboard setup)
- [ ] Won't need to be touched for years - YES (if working)

**Verdict:** NEEDS WORK - The verification complexity should be invisible. Developers want to receive events, not implement cryptography.

---

## Integration

This skill is part of the **Patrick Collison** expert persona. Use it when evaluating developer experience, API design, or integration complexity. It pairs well with:
- **speed-constraint-analysis** for overall project velocity
- **pre-pmf-post-pmf-diagnosis** to understand if DX complexity is appropriate for stage