# Carrier Swarm Inference Architecture

A lightweight protocol for coordinating central carrier models and specialized wing models to reduce unnecessary large-model activation through traceable inference relay.

## Status

**Current version:** `v0.5.0-candidate`
**Current focus:** Compute and Royalty Integration
**Validation status:** GitHub Actions passed

This repository has reached its fifth functional validation point.

The repository now includes:

* `Carrier Swarm Mission`
* `Wing Role Registry`
* `Activation Policy`
* `Trace Receipt Integration`
* `Compute and Royalty Integration`
* JSON Schemas
* YAML examples
* validation script
* GitHub Actions workflow

All v0.1, v0.2, v0.3, v0.4, and v0.5 examples validate successfully against their schemas.

## Overview

**Carrier Swarm Inference Architecture** defines a modular AI inference structure in which a central carrier model coordinates multiple lightweight wing models.

The carrier model is not treated as an always-on monolithic intelligence.
Instead, it serves as a coordination, integration, memory, escalation, trace consolidation, and final reasoning node that is activated only when needed.

Smaller wing models handle local detection, classification, routing, compression, verification, safety checking, memory lookup, and trace logging before escalation to the carrier.

The core principle is:

> Do not invoke the largest model by default.
> Let smaller models scout, filter, compress, verify, route, and record first.

## Why This Matters

Modern AI systems often rely on large centralized models for every task, even when the input is simple, repetitive, local, or low-risk.

This causes unnecessary:

* compute usage
* energy consumption
* latency
* bandwidth usage
* cost
* central dependency
* opaque multi-agent behavior
* unclear contribution tracking

Carrier Swarm Inference Architecture reduces this waste by introducing an inference relay structure.

Instead of sending every input directly to a large model, the system first delegates the task to lightweight specialized models. Only uncertain, complex, high-risk, or high-value cases are escalated to the carrier model.

With v0.5, the system can also record compute usage, optional energy cost, contribution weight, reward eligibility, royalty hooks, and allocation boundaries.

## Conceptual Model

```text
Input
  ↓
Wing Model: Scout / Classifier / Router
  ↓
Local Inference
  ↓
Compression / Verification / Safety Check
  ↓
Activation Policy
  ↓
Early Exit / Continue with Wings / Activate Carrier / Human Review / Halt
  ↓
Trace Receipt Integration
  ↓
Compute and Royalty Integration
  ↓
Carrier Model: Integration / Final Reasoning
  ↓
Human Review / Trace Record / Contribution Record / Allocation Boundary
```

## Core Components

### Carrier Model

The carrier model is the central coordination node.

Its responsibilities include:

* global context integration
* memory coordination
* complex reasoning
* final synthesis
* mission reassignment
* escalation handling
* trace consolidation
* human review support

The carrier model should not be activated for every task by default.

### Wing Models

Wing models are lightweight specialized models or agents.

Typical roles include:

* scout
* router
* classifier
* compressor
* verifier
* summarizer
* safety guard
* sensor agent
* memory agent
* trace agent

Wing models are not merely reduced versions of a large model.
They are role-specific inference units designed to reduce unnecessary central activation.

### Inference Relay

An inference relay is the structured flow of a task across wing models and the carrier model.

A minimal relay cycle consists of:

1. dispatch
2. local inference
3. event filtering
4. return report
5. activation decision
6. carrier integration
7. human review
8. trace record

### Wing Role Registry

The **Wing Role Registry** defines standardized wing model roles.

Each role may define:

* role identifier
* display name
* category
* responsibility
* typical inputs
* typical outputs
* activation mode
* escalation permission
* activation conditions
* trace requirements
* human governance note

The purpose of the registry is to prevent wing models from becoming vague or redundant.

Each wing should know:

* what it does;
* when it activates;
* whether it can request carrier activation;
* whether it can recommend early exit;
* whether it can request human review;
* what it must record.

### Activation Policy

The **Activation Policy** defines when the carrier model should be activated, when early exit is allowed, and how escalation decisions must be justified.

It enables the system to choose among:

* early exit
* continue with wings
* activate carrier
* request human review
* halt mission

The Activation Policy is the energy-aware decision layer of the carrier-swarm architecture.

It prevents the carrier model from becoming an always-on monolith again.

### Trace Receipt Integration

The **Trace Receipt Integration** defines how mission activity is connected to trace receipts, contribution records, activation records, early exit records, filtered event records, and audit boundaries.

It records:

* which mission was referenced;
* which trace receipts were generated;
* which wing, carrier, trace, or human actor contributed;
* why the carrier was activated;
* why early exit was allowed or rejected;
* what events were filtered before escalation;
* whether the record is ready for audit;
* whether future royalty or compute allocation integration is possible.

The purpose is to prevent carrier-swarm inference from becoming a black-box multi-agent process.

### Compute and Royalty Integration

The **Compute and Royalty Integration** defines how carrier-swarm trace records connect to compute cost, optional energy cost, contribution weights, reward eligibility, royalty hooks, and allocation boundaries.

It records:

* mission reference
* trace reference
* compute usage
* optional energy cost
* optional monetary cost estimate
* contribution allocation
* reward eligibility
* royalty hooks
* compute access hooks
* origin attribution hooks
* audit export hooks
* allocation boundaries

The purpose is to connect inference relay with resource accounting and future value distribution.

This turns carrier-swarm inference into a compute-aware and contribution-aware architecture.

## v0.1 Scope — Carrier Swarm Mission

The first version defines a minimal record format for a **Carrier Swarm Mission**.

A Carrier Swarm Mission records:

* mission identity
* carrier node
* wing nodes
* relay cycle
* activation policy
* escalation reason
* trace requirements
* human review boundary

## v0.2 Scope — Wing Role Registry

The second version defines a standard registry for wing model roles.

The initial registry includes:

* Scout Wing
* Router Wing
* Compression Wing
* Verification Wing
* Safety Guard Wing
* Memory Wing
* Trace Wing

This turns the carrier-swarm model from a general relay concept into a structured role-based architecture.

## v0.3 Scope — Activation Policy

The third version defines the decision policy for carrier activation and early exit.

The Activation Policy records:

* default carrier activation mode
* early exit conditions
* carrier activation triggers
* numeric thresholds
* escalation decisions
* trace requirements
* human governance boundaries

This turns carrier-swarm inference into a controlled decision system rather than a loose multi-agent pipeline.

## v0.4 Scope — Trace Receipt Integration

The fourth version defines the trace integration layer for carrier-swarm missions.

Trace Receipt Integration records:

* mission references
* trace receipts
* contribution records
* carrier activation records
* early exit records
* filtered event records
* audit boundaries
* future royalty or compute allocation readiness

This turns carrier-swarm inference into a traceable, auditable, contribution-aware relay system.

## v0.5 Scope — Compute and Royalty Integration

The fifth version defines the compute and value-allocation integration layer.

Compute and Royalty Integration records:

* compute cost records
* optional energy cost records
* optional monetary cost estimates
* contribution allocation records
* reward eligibility
* royalty hooks
* compute access allocation hooks
* origin attribution hooks
* audit export hooks
* allocation boundaries

This turns carrier-swarm inference into a compute-aware, energy-aware, contribution-aware, and royalty-ready relay system.

## Design Principles

### 1. Carrier Is Not a Monolith

The carrier is not an always-on god model.

It is a coordination and integration node.

The system should avoid routing every input directly to the carrier.

### 2. Wings Act First

Wing models perform lightweight local inference before escalation.

They reduce unnecessary large-model activation by handling:

* simple cases
* repetitive cases
* low-risk cases
* local detection
* initial filtering
* compression
* verification
* safety checks
* memory lookup
* trace logging

### 3. Roles Must Be Explicit

Wing models should not be vague helper agents.

Each wing role should define:

* responsibility
* activation mode
* escalation permission
* trace requirements
* human governance boundary

### 4. Activation Must Be Policy-Driven

Carrier activation should not happen automatically.

The system should record why it chose to:

* exit early;
* continue with wing models;
* activate the carrier;
* request human review;
* halt the mission.

### 5. Escalation Must Be Explicit

Carrier activation should happen only when clearly justified.

Typical escalation reasons include:

* low confidence
* high ambiguity
* safety concern
* conflicting wing reports
* high-value decision
* human review requirement

### 6. Trace Everything

Every mission should produce a traceable record.

The system should be able to explain:

* which wing models participated
* what each wing model inferred
* what was filtered
* what was escalated
* why the carrier was activated
* why early exit was allowed or rejected
* whether human review occurred
* what contribution each participant made

### 7. Contribution Should Be Recoverable

Carrier-swarm inference should preserve enough information for future contribution analysis.

The trace layer should make it possible to identify:

* scouting contributions
* routing contributions
* compression contributions
* verification contributions
* safety assessment contributions
* memory lookup contributions
* carrier integration contributions
* human review contributions

This enables future integration with compute allocation, royalty allocation, or origin attribution systems.

### 8. Compute Cost Should Be Visible

Carrier-swarm inference should record how much compute was used where possible.

Compute records may include:

* token usage
* inference calls
* model steps
* CPU milliseconds
* GPU milliseconds
* NPU milliseconds
* edge events
* manual review units

Optional fields may include:

* energy cost in millijoules
* monetary cost estimate
* cost estimation method

### 9. Reward Allocation Must Respect Governance

Reward or royalty allocation should not happen blindly.

Allocation boundaries should define:

* whether allocation is ready;
* whether human review is required;
* whether automatic distribution is allowed;
* whether audit is required.

### 10. Human Governance Remains Central

The carrier model is not the final authority in high-impact contexts.

Human review should remain available, especially when:

* decisions affect people
* outputs are uncertain
* safety risks exist
* attribution or reward allocation is involved
* automatic distribution is requested

## Validation

Install dependencies:

```bash
pip install jsonschema pyyaml
```

Run validation:

```bash
python scripts/validate_examples.py
```

Expected output:

```text
[validate] Carrier Swarm Mission
  schema : schemas/carrier-swarm-mission.schema.json
  example: examples/carrier-swarm-mission.example.yaml
[ok] carrier-swarm-mission.example.yaml is valid
[validate] Wing Role Registry
  schema : schemas/wing-role-registry.schema.json
  example: examples/wing-role-registry.example.yaml
[ok] wing-role-registry.example.yaml is valid
[validate] Activation Policy
  schema : schemas/activation-policy.schema.json
  example: examples/activation-policy.example.yaml
[ok] activation-policy.example.yaml is valid
[validate] Trace Receipt Integration
  schema : schemas/trace-receipt-integration.schema.json
  example: examples/trace-receipt-integration.example.yaml
[ok] trace-receipt-integration.example.yaml is valid
[validate] Compute and Royalty Integration
  schema : schemas/compute-royalty-integration.schema.json
  example: examples/compute-royalty-integration.example.yaml
[ok] compute-royalty-integration.example.yaml is valid
[ok] all examples are valid
```

The repository also includes a GitHub Actions workflow:

```text
.github/workflows/validate.yml
```

This workflow validates the example files automatically on push, pull request, or manual dispatch.

## Repository Structure

```text
.
├── README.md
├── CHANGELOG.md
├── schemas/
│   ├── carrier-swarm-mission.schema.json
│   ├── wing-role-registry.schema.json
│   ├── activation-policy.schema.json
│   ├── trace-receipt-integration.schema.json
│   └── compute-royalty-integration.schema.json
├── examples/
│   ├── carrier-swarm-mission.example.yaml
│   ├── wing-role-registry.example.yaml
│   ├── activation-policy.example.yaml
│   ├── trace-receipt-integration.example.yaml
│   └── compute-royalty-integration.example.yaml
├── scripts/
│   └── validate_examples.py
└── .github/
    └── workflows/
        └── validate.yml
```

## Relationship to Other Protocols

Carrier Swarm Inference Architecture can connect with:

* AI Search Trace Receipt Standard
* Trace Receipt Protocol
* Structural Rumination Layer
* Memory Breathing Protocol
* Compute Access Royalty OS
* Origin Structure Market

This repository focuses on the inference relay layer:

> How should inference be distributed, routed, escalated, role-assigned, policy-controlled, traced, audited, costed, and connected to reward allocation?

## Intended Use Cases

* local AI systems
* edge AI networks
* multi-agent inference
* small model orchestration
* energy-aware AI
* human-in-the-loop AI
* traceable reasoning pipelines
* distributed sensor intelligence
* lightweight model swarms
* compute-aware AI governance
* role-based AI agent coordination
* activation-controlled AI inference
* auditable inference relay
* contribution-aware AI workflows
* royalty-ready inference systems
* compute allocation records
* origin attribution workflows

## Roadmap

### v0.1 — Carrier Swarm Mission

Define the minimal mission record for carrier-swarm inference relay.

Status:

* README created
* JSON Schema created
* YAML example created
* validation script created
* GitHub Actions workflow created
* validation passed

### v0.2 — Wing Role Registry

Define standard roles for wing models.

Status:

* Wing Role Registry schema created
* Wing Role Registry example created
* validation script updated
* GitHub Actions validation passed

Initial roles:

* scout
* router
* compressor
* verifier
* safety guard
* memory agent
* trace agent

### v0.3 — Activation Policy

Define when the carrier model should be activated and when early exit is allowed.

Status:

* Activation Policy schema created
* Activation Policy example created
* validation script updated
* GitHub Actions validation passed

Initial decisions:

* early exit
* continue with wings
* activate carrier
* request human review
* halt mission

### v0.4 — Trace Receipt Integration

Connect carrier-swarm missions with trace receipts and contribution records.

Status:

* Trace Receipt Integration schema created
* Trace Receipt Integration example created
* validation script updated
* GitHub Actions validation passed

Initial records:

* mission reference
* trace receipt
* contribution record
* carrier activation record
* early exit record
* filtered event record
* audit boundary

### v0.5 — Compute and Royalty Integration

Connect carrier-swarm traces with compute cost, optional energy cost, contribution weight, reward allocation readiness, and royalty hooks.

Status:

* Compute and Royalty Integration schema created
* Compute and Royalty Integration example created
* validation script updated
* GitHub Actions validation passed

Initial records:

* mission reference
* trace reference
* compute record
* optional energy cost
* optional monetary cost estimate
* contribution allocation
* royalty hook
* allocation boundary

## Conceptual Position

Carrier Swarm Inference Architecture does not reject large models.

It repositions them.

A large model should not be invoked as the default path for every input.
It should function as a carrier: a coordination, integration, memory, escalation, trace consolidation, and final reasoning node.

Wing models perform the first movement.

The Activation Policy decides whether the mission can end early, continue with wings, activate the carrier, request human review, or halt.

The Trace Receipt Integration records who participated, what was filtered, why escalation happened, and whether the mission is ready for audit or future contribution allocation.

The Compute and Royalty Integration records compute usage, optional energy cost, contribution weights, reward eligibility, and downstream allocation hooks.

The carrier integrates only when needed.

The Wing Role Registry ensures that the swarm does not become chaotic.
The Activation Policy ensures that the carrier does not become monolithic again.
The Trace Receipt Integration ensures that the relay does not become opaque.
The Compute and Royalty Integration ensures that contribution and resource usage can be accounted for.

This turns AI inference from a monolithic pipeline into a traceable, role-based, policy-controlled, contribution-aware, and royalty-ready relay system.

In short:

> Monolith AGI is replaced by Carrier-Swarm AI.

## License

TBD.

