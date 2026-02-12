---
name: reverse-engineering-analysis
description: 'Understand complex systems by systematically dissecting them layer by
  layer. Apply Leonardo da Vinci''s anatomical methodology: sequential views, exploded
  diagrams, and progressive exposure of inter...'
license: MIT
metadata:
  version: 1.0.0
  author: sethmblack
keywords:
- callbacks
- reverse-engineering-analysis
- structure
- transformation
- writing
---

# Reverse Engineering Analysis

Understand complex systems by systematically dissecting them layer by layer. Apply Leonardo da Vinci's anatomical methodology: sequential views, exploded diagrams, and progressive exposure of internal structure.

---

## When to Use

- Approaching an unfamiliar system or codebase
- User asks "How does this actually work?"
- Analyzing legacy systems with limited documentation
- Understanding third-party integrations or black boxes
- Preparing to modify or extend an existing system
- Request for "dissection" or "reverse engineering" of a system

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| system | Yes | The system, component, or codebase to analyze |
| access_level | No | What you can do: read code, run queries, execute, modify |
| documentation | No | Available docs, their reliability, their age |
| purpose | No | Why you need to understand this (informs depth) |

---

## The Four-Step Framework

Leonardo dissected approximately 30 human corpses, approaching the body as an engineer approaches a machine. His anatomical drawings used techniques borrowed from engineering (exploded views) and architecture (elevation, plan, section). Apply the same method to technical systems.

### Step 1: Establish Outer View

Before dissection, understand the whole. What does this system appear to be from the outside?

**Document:**
- **Boundaries:** Where does this system start and end?
- **Interfaces:** What inputs does it accept? What outputs does it produce?
- **Dependencies:** What does it connect to? What connects to it?
- **Stated purpose:** What is it supposed to do (according to docs/stakeholders)?

**Techniques:**
- Read existing documentation (but verify later)
- Trace a single request/transaction through the system
- List all external touchpoints (APIs, databases, queues, files)
- Interview stakeholders about their understanding

**Leonardo's insight:** "The painter must first study the whole before studying the parts." Understand the system's place in the larger context before diving in.

### Step 2: Create Progressive Views

Like Leonardo's anatomical drawings showing the body at different layers of depth, create views at increasing levels of detail:

**Layer 1: Component Topology**
- What are the major components/services/modules?
- How do they connect?
- What is the flow of data/control?

**Layer 2: Component Internals**
For each major component:
- What does this component do?
- What are its internal parts?
- How does data transform as it passes through?

**Layer 3: Implementation Details**
For critical or confusing components:
- How is this actually implemented?
- What algorithms/patterns are used?
- Where does complexity concentrate?

**Leonardo's technique:** Sequential views, like cinema animation, showing the same subject from multiple perspectives and depths.

### Step 3: Identify Principles and Patterns

Leonardo didn't just draw what he saw; he sought to understand *why* it was constructed thus. For each discovery, ask:

**Pattern Questions:**
- Why was this designed this way? What problem does it solve?
- What constraints shaped this design? (Performance, history, team skills, time pressure)
- What patterns are being used? (Caching, queuing, eventual consistency, etc.)
- What patterns are being violated? (And possibly intentionally?)

**Anomaly Questions:**
- What is surprising or unexpected?
- What doesn't match the documentation?
- What seems unnecessarily complex? What seems suspiciously simple?
- Where does the "intended" design diverge from "actual" implementation?

**Leonardo's insight:** "Human subtlety will never devise an invention more beautiful, more simple, or more direct than does nature, because in her inventions nothing is lacking, and nothing is superfluous." If something seems superfluous, you may not yet understand its purpose.

### Step 4: Document and Validate

Create lasting documentation of your discoveries, and validate understanding:

**Documentation:**
- System diagrams at multiple layers
- Component interaction maps
- Data flow diagrams
- Key decision rationale (why it works this way)
- Gotchas and non-obvious behaviors

**Validation:**
- Make predictions about behavior you haven't yet observed
- Test predictions through observation or experiment
- Have others review your understanding
- Try to explain it simply; confusion reveals gaps

**Leonardo's insight:** "Those sciences are vain and full of error which are not born of experience." Validate your understanding through observation, not just reasoning.

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
## Reverse Engineering Analysis: [System Name]

### Analysis Scope
**System:** [What was analyzed]
**Access level:** [Read/Execute/Modify]
**Purpose:** [Why this analysis was needed]
**Documentation available:** [What existed, reliability assessment]

### Outer View
**Boundaries:** [Where system starts/ends]
**Stated purpose:** [What it's supposed to do]

**External Interfaces:**
| Interface | Type | Direction | Connects To |
|-----------|------|-----------|-------------|
| [Name] | API/Queue/DB/etc | In/Out/Both | [External system] |

### Component Topology (Layer 1)
```
[ASCII diagram or description of major components and connections]
```

**Component Summary:**
| Component | Role | Key Dependencies |
|-----------|------|------------------|
| [Name] | [Purpose] | [What it needs] |

### Component Details (Layer 2)

#### [Component Name]
**Purpose:** [What it does]
**Inputs:** [What it receives]
**Outputs:** [What it produces]
**Key internals:** [Important sub-components]
**Data transformation:** [How data changes]

### Critical Implementation Details (Layer 3)
[For complex/critical components only]

#### [Component/Algorithm Name]
**Implementation:** [How it actually works]
**Why this way:** [Design rationale if known]
**Gotchas:** [Non-obvious behaviors]

### Patterns Identified
| Pattern | Where Used | Purpose |
|---------|------------|---------|
| [Pattern] | [Components] | [Why] |

### Anomalies and Surprises
1. **[Anomaly]:** [What was unexpected] - [Possible explanation]

### Validation
| Prediction | Tested | Result |
|------------|--------|--------|
| [Expected behavior] | Yes/No | [Confirmed/Refuted/Partial] |

### Open Questions
- [What remains unclear]
- [What would require deeper investigation]
```

---

## Constraints

- Do not confuse documentation with reality; verify through observation
- Do not assume complexity is unnecessary; understand before criticizing
- Do not stop at the first layer; depth reveals important patterns
- Acknowledge access limitations; some systems cannot be fully dissected
- Recognize when reverse engineering would take longer than rewriting

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

**Input:**
```
system: Legacy order processing service (order-svc)
access_level: Read code, read-only database access, can observe logs
documentation: README from 2019, incomplete API docs
purpose: Need to add new payment provider integration
```

**Output:**

## Reverse Engineering Analysis: order-svc

### Analysis Scope
**System:** Order processing service (order-svc)
**Access level:** Read code, read-only DB, observe logs
**Purpose:** Add new payment provider integration
**Documentation available:** README (2019, partially outdated), incomplete API docs (missing recent endpoints)

### Outer View
**Boundaries:** Accepts orders from checkout-svc, processes payments via payment-svc, writes to orders DB, publishes to fulfillment queue
**Stated purpose:** Process customer orders from cart through payment completion

**External Interfaces:**
| Interface | Type | Direction | Connects To |
|-----------|------|-----------|-------------|
| /api/orders | REST API | In | checkout-svc |
| /api/orders/{id} | REST API | In | admin-dashboard |
| payment-svc | gRPC | Out | Payment processing |
| orders-db | PostgreSQL | Out | Persistence |
| fulfillment-queue | RabbitMQ | Out | fulfillment-svc |
| events-topic | Kafka | Out | Analytics, notifications |

### Component Topology (Layer 1)
```
                    checkout-svc
                         |
                         v
                 ┌───────────────┐
                 │   API Layer   │
                 │  (Express.js) │
                 └───────┬───────┘
                         │
           ┌─────────────┼─────────────┐
           v             v             v
    ┌──────────┐  ┌──────────┐  ┌──────────┐
    │ Order    │  │ Payment  │  │ Event    │
    │ Manager  │  │ Handler  │  │ Publisher│
    └────┬─────┘  └────┬─────┘  └────┬─────┘
         │             │              │
         v             v              v
    orders-db    payment-svc    Kafka/RabbitMQ
```

**Component Summary:**
| Component | Role | Key Dependencies |
|-----------|------|------------------|
| API Layer | HTTP routing, validation | Express.js, Joi |
| Order Manager | Order lifecycle, state machine | orders-db |
| Payment Handler | Payment provider abstraction | payment-svc |
| Event Publisher | Async event emission | Kafka, RabbitMQ |

### Component Details (Layer 2)

#### Payment Handler
**Purpose:** Abstract payment providers behind unified interface
**Inputs:** Order ID, payment method, amount
**Outputs:** Payment result (success/failure/pending)
**Key internals:**
- `PaymentProviderFactory` - selects provider based on payment method
- `StripeProvider`, `PayPalProvider` - concrete implementations
- `PaymentRetryPolicy` - handles transient failures

**Data transformation:**
```
Order → PaymentRequest → ProviderSpecificRequest → ProviderResponse → PaymentResult
```

### Critical Implementation Details (Layer 3)

#### PaymentProviderFactory
**Implementation:** Switch statement on `payment_method` field, returns provider instance
**Why this way:** Predates dependency injection adoption (2018 code)
**Gotchas:**
- Provider instances are created per-request (no pooling)
- Adding new provider requires code change (no config-based discovery)
- Provider selection happens BEFORE validation, so invalid payment methods fail late

**Location:** `src/services/payment/PaymentProviderFactory.js:23-45`

### Patterns Identified
| Pattern | Where Used | Purpose |
|---------|------------|---------|
| State Machine | Order Manager | Order lifecycle (pending→paid→fulfilled) |
| Factory | Payment Handler | Provider selection |
| Outbox | Event Publisher | Reliable event delivery (events table → Kafka) |
| Retry with backoff | Payment Handler | Transient failure handling |

### Anomalies and Surprises
1. **Duplicate payment protection is order-level, not idempotency-key**: System checks if order already paid, but doesn't use idempotency keys. Risk of duplicate charges on network retry.
2. **Event publisher writes to both Kafka AND RabbitMQ**: Expected one or the other. Investigation shows Kafka for analytics, RabbitMQ for fulfillment (legacy split).
3. **PaymentRetryPolicy has hardcoded 3 retries**: Not configurable, may need adjustment for new provider with different failure characteristics.

### Validation
| Prediction | Tested | Result |
|------------|--------|--------|
| Adding provider requires Factory code change | Yes (read code) | Confirmed |
| Order state transitions are enforced | Yes (traced logs) | Confirmed |
| Failed payments leave order in pending state | Yes (DB query) | Confirmed (with 24h timeout) |

### Open Questions
- How are webhook callbacks handled for async payment providers? (Not visible in this service; may be in payment-svc)
- What happens to orders stuck in pending >24h? (Saw timeout in code, unclear on notification)
- Is there a way to configure retry policy per provider? (Not currently, may need to add)

---

## Integration

This skill is part of the **Leonardo da Vinci** expert persona. Use it when understanding complex systems requires systematic dissection rather than documentation trust.

Leonardo's anatomical studies used techniques revolutionary for his time: exploded views, multiple angles, layer-by-layer exposure. His drawings were unequaled in accuracy until the photographic techniques of the 19th century. Apply that same systematic rigor to understanding technical systems.