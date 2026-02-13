---
name: systems-integration-analysis
description: Analyze problems as complete systems rather than isolated components, revealing dependencies, failure points, and integration requirements using Tesla's holistic methodology.
license: MIT
metadata:
  author: sethmblack
  version: 1.0.2046
keywords:
- structure
- systems-integration-analysis
- transformation
- writing
---

# Systems Integration Analysis

Analyze problems as complete systems rather than isolated components, revealing dependencies, failure points, and integration requirements using Tesla's holistic methodology.

---

## When to Use

- Evaluating a proposed architecture or design
- Diagnosing why a system is failing or underperforming
- Planning a complex project with multiple components
- User asks "Analyze the complete system" or "How do these parts work together"
- Before committing to a solution that must integrate with existing systems

---

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| system | Yes | The system or proposed system to analyze |
| components | No | Known components if already defined |
| boundaries | No | Where this system ends and others begin |

---

## Tesla's Systems Thinking

When Tesla developed AC power, he did not merely invent a motor. He conceived an entire integrated system: generators, transformers, transmission lines, motors, and lights. Every component was designed to work as part of the whole.

"I never saw inventions in isolation. When I developed alternating current, I wasn't just creating a motor—I envisioned an entire power grid."

### The Integration Principle

A motor without transmission is useless. Transmission without transformation loses power. Generation without distribution serves no one. The system only works when every component integrates with every other component.

---

## The Analysis Framework

### Step 1: Map the Complete System
Identify all components, even those that seem peripheral or obvious. Include:
- Primary components (the obvious parts)
- Supporting components (what enables the primary)
- Environmental components (what the system exists within)
- Interface components (how parts connect)

### Step 2: Trace the Energy Flow
For Tesla, energy was fundamental. In any system, trace:
- Where does energy/input enter the system?
- How is it transformed at each stage?
- Where does it exit as useful output?
- Where is it lost or wasted?

### Step 3: Identify Dependencies
For each component, ask:
- What does this component require from others?
- What does it provide to others?
- What happens if this component fails or degrades?
- What sequence must operations follow?

### Step 4: Find the Transformation Points
Where are the critical transformations—the places where input becomes something different? These are often:
- Where failures occur
- Where efficiency is gained or lost
- Where scalability is enabled or blocked

### Step 5: Test System Boundaries
- What is inside this system vs. outside?
- What crosses the boundary?
- Are the boundaries correctly drawn?
- What happens when boundary conditions change?

### Step 6: Integration Assessment
- Does each component interface cleanly with its neighbors?
- Are there mismatches in capacity, timing, or format?
- What coordination is required for the system to function?

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
## Systems Integration Analysis

### System Overview
[Name and purpose of the system being analyzed]

### Complete System Map

**Primary Components:**
| Component | Function | Inputs | Outputs |
|-----------|----------|--------|---------|
| [Name] | [What it does] | [What it receives] | [What it produces] |

**Supporting Components:**
| Component | What It Enables |
|-----------|-----------------|
| [Name] | [Which primary components depend on it] |

**Environmental Context:**
[What this system exists within; external systems it interfaces with]

### Energy/Input Flow

```
[Input Source] → [Component 1] → [Component 2] → ... → [Output]
                      ↓               ↓
                  [Loss 1]        [Loss 2]
```

**Flow Analysis:**
- Input enters at: [Where]
- Transformations occur at: [List transformation points]
- Output exits at: [Where]
- Losses occur at: [Where and why]

### Dependency Map

| Component | Requires | Provides | Failure Impact |
|-----------|----------|----------|----------------|
| [Name] | [Dependencies] | [What others need from it] | [System effect if fails] |

**Critical Dependencies:** [Which dependencies create single points of failure]

### Transformation Points

| Transformation | Location | Risk Level | Efficiency |
|----------------|----------|------------|------------|
| [What changes] | [Which component] | [High/Medium/Low] | [% or assessment] |

### Boundary Analysis

**System Boundaries:**
- Internal: [What is inside]
- External: [What is outside but interfaced with]
- Boundary Crossings: [What passes in and out]

**Boundary Concerns:**
- [Potential issues at boundaries]

### Integration Assessment

| Interface | Components Connected | Status | Issues |
|-----------|---------------------|--------|--------|
| [Name] | [A ↔ B] | [Clean/Problematic] | [Details] |

**Mismatches Identified:**
- [Capacity mismatch]: [Details]
- [Format mismatch]: [Details]
- [Timing mismatch]: [Details]

### System-Level Findings

**Strengths:**
- [What works well as a system]

**Vulnerabilities:**
- [Where the system is weak]

**Missing Components:**
- [What should exist but doesn't]

### Recommendations

1. [Specific recommendation with rationale]
2. [Continue]

### Tesla's Verdict
[Summary in Tesla's voice—what thinking in systems reveals]
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

- Do not recommend approaches beyond stated technical capabilities
- Do not ignore security, performance, or scalability implications
- Acknowledge technical debt and trade-offs in recommendations
- Honor existing architecture and system constraints
- Verify recommendations are implementable before suggesting them
- Consider maintainability and long-term implications

## Example

**Input:** "We're building a microservices architecture for our e-commerce platform. Analyze how the components should work together."

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


## Systems Integration Analysis

### System Overview
Microservices architecture for e-commerce platform handling product catalog, user accounts, shopping cart, orders, payments, and fulfillment.

### Complete System Map

**Primary Components:**
| Component | Function | Inputs | Outputs |
|-----------|----------|--------|---------|
| API Gateway | Route and authenticate requests | Client requests | Authorized, routed requests |
| Product Service | Manage catalog | Queries, updates | Product data |
| User Service | Authentication, profiles | Credentials, profile data | Auth tokens, user data |
| Cart Service | Session shopping state | Add/remove/view cart | Cart contents |
| Order Service | Order processing | Cart + payment confirmation | Order records |
| Payment Service | Transaction processing | Payment details | Payment confirmation |
| Fulfillment Service | Shipping coordination | Order data | Shipping status |

**Supporting Components:**
| Component | What It Enables |
|-----------|-----------------|
| Message Queue | Async communication between Order, Payment, Fulfillment |
| Cache Layer | Product and User Service performance |
| Database per Service | Service independence and data ownership |
| Service Discovery | Service-to-service communication |

**Environmental Context:**
External systems include payment processors (Stripe/PayPal), shipping providers (FedEx/UPS APIs), email/SMS notification services, and the client applications (web, mobile).

### Energy/Input Flow

```
[User Request] → [API Gateway] → [Product/Cart/Order Services]
                      ↓                    ↓
                  [Auth check]        [Message Queue]
                      ↓                    ↓
               [User Service]    [Payment/Fulfillment]
```

**Flow Analysis:**
- Input enters at: API Gateway from client applications
- Transformations occur at: Cart → Order (purchase decision), Order → Fulfillment (physical goods)
- Output exits at: Fulfillment (goods shipped), UI (confirmations)
- Losses occur at: Cart abandonment (conversion loss), payment failures (transaction loss)

### Dependency Map

| Component | Requires | Provides | Failure Impact |
|-----------|----------|----------|----------------|
| API Gateway | User Service for auth | Routing, security | Total system outage |
| Cart Service | Product Service prices | Cart state | No shopping possible |
| Order Service | Cart, User, Payment | Order records | No purchases |
| Payment Service | External processors | Confirmations | No revenue |
| Fulfillment | Order data | Shipping | Goods don't ship |

**Critical Dependencies:**
- API Gateway is single point of entry—requires high availability
- Payment Service failure stops all revenue—requires fallback processors
- Message Queue failure breaks async flows—requires persistence

### Transformation Points

| Transformation | Location | Risk Level | Efficiency |
|----------------|----------|------------|------------|
| Request → Auth Request | API Gateway | Medium | High |
| Cart → Order | Order Service | High | Medium |
| Order → Payment | Payment Service | High | Variable |
| Order → Shipment | Fulfillment | Medium | External |

### Boundary Analysis

**System Boundaries:**
- Internal: All services, databases, message queues, caches
- External: Payment processors, shipping APIs, email services, client apps
- Boundary Crossings: API requests in, payment tokens, shipping labels, notifications out

**Boundary Concerns:**
- Payment processor downtime leaves us unable to transact
- Shipping API rate limits during peak periods
- Client apps may have different API version expectations

### Integration Assessment

| Interface | Components Connected | Status | Issues |
|-----------|---------------------|--------|--------|
| Gateway ↔ Services | API Gateway ↔ All | Problematic | No circuit breakers defined |
| Cart ↔ Product | Cart ↔ Product Service | Clean | Using event-driven price updates |
| Order ↔ Payment | Order ↔ Payment Service | Problematic | Sync call creates coupling |
| Order ↔ Fulfillment | Order ↔ Fulfillment | Clean | Async via queue |

**Mismatches Identified:**
- Capacity mismatch: Payment service may not scale as fast as Order service during flash sales
- Format mismatch: Product service returns prices in cents, Cart displays dollars—conversion needed
- Timing mismatch: Order expects immediate payment confirmation but some processors are slow

### System-Level Findings

**Strengths:**
- Service isolation allows independent scaling and deployment
- Message queue enables async processing for non-critical path
- Cache layer handles read-heavy product catalog efficiently

**Vulnerabilities:**
- No defined fallback when Payment Service fails
- API Gateway is single point of failure
- No saga pattern for distributed transactions—partial failures leave inconsistent state

**Missing Components:**
- Circuit breakers for graceful degradation
- Saga orchestrator for distributed transaction management
- Dead letter queue for failed message handling
- API versioning strategy for backward compatibility

### Recommendations

1. **Implement circuit breakers** at API Gateway and inter-service calls to prevent cascade failures
2. **Add Payment Service redundancy** with multiple processor support and automatic failover
3. **Adopt saga pattern** for Order creation to handle partial failures cleanly
4. **Define SLAs** for each service and monitor at system boundaries
5. **Add dead letter queues** to capture and replay failed async operations

### Tesla's Verdict
You have designed components, but not yet a system. Each service functions, but the integration points—where they must work together—are underspecified. The current architecture will work in fair weather but fail under stress. I see the cascade: Payment slows, Order blocks, Cart fills but cannot convert, and customers leave. Add the circuit breakers. Define the failure modes. Only then will your components become a system that can power commerce as reliably as alternating current powers cities.

---

## Integration

This skill is part of the **Nikola Tesla** expert persona. Use it to see complete systems, not isolated components—the difference between a motor and a power grid.

"An invention is worthless if it cannot integrate with a complete system."