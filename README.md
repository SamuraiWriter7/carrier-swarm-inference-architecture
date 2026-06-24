# Carrier Swarm Inference Architecture

A lightweight protocol for coordinating central carrier models and specialized wing models to reduce unnecessary large-model activation through traceable inference relay.

## Overview

**Carrier Swarm Inference Architecture** defines a modular AI inference structure in which a central carrier model coordinates multiple lightweight wing models.

The carrier model is not treated as an always-on monolithic intelligence.
Instead, it serves as a coordination, integration, memory, and final reasoning node that is activated only when needed.

Smaller wing models handle local detection, classification, routing, compression, verification, and preliminary judgment before escalation to the carrier.

The core principle is:

> Do not invoke the largest model by default.
> Let smaller models scout, filter, compress, and route first.

## Why This Matters

Modern AI systems often rely on large centralized models for every task, even when the input is simple, repetitive, local, or low-risk.

This causes unnecessary:

* compute usage
* energy consumption
* latency
* bandwidth usage
* cost
* central dependency

Carrier Swarm Inference Architecture reduces this waste by introducing an inference relay structure.

Instead of sending every input directly to a large model, the system first delegates the task to lightweight specialized models. Only uncertain, complex, high-risk, or high-value cases are escalated to the carrier model.

## Conceptual Model

```text
Input
  ↓
Wing Model: Scout / Classifier / Router
  ↓
Local Inference
  ↓
Event Filtering
  ↓
Return Report
  ↓
Carrier Model: Integration / Final Reasoning
  ↓
Human Review / Trace Record
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
5. carrier integration
6. human review
7. trace record

## v0.1 Scope

The first version of this repository defines a minimal record format for a **Carrier Swarm Mission**.

A Carrier Swarm Mission records:

* mission identity
* carrier node
* wing nodes
* relay cycle
* activation policy
* escalation reason
* trace requirements
* human review boundary

## Example

```yaml
mission_id: mission-2026-001
mission_type: inference_relay

carrier_node:
  id: local-carrier-model-01
  role: integration_and_final_reasoning
  activation_mode: on_demand

wing_nodes:
  - id: scout-model-01
    role: initial_classification
    model_class: lightweight_model

  - id: router-model-01
    role: routing_decision
    model_class: lightweight_model

  - id: compression-model-01
    role: summary_and_feature_compression
    model_class: lightweight_model

relay_cycle:
  - dispatch
  - local_inference
  - event_filtering
  - return_report
  - carrier_integration
  - human_review
  - trace_record

activation_policy:
  central_activation: on_demand
  early_exit_enabled: true
  escalation_required_when:
    - low_confidence
    - high_risk
    - high_ambiguity
    - human_review_required

trace:
  receipt_required: true
  contribution_logging: true
  energy_logging: optional
  human_review_required: true
```

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

### 3. Escalation Must Be Explicit

Carrier activation should happen only when clearly justified.

Typical escalation reasons include:

* low confidence
* high ambiguity
* safety concern
* conflicting wing reports
* high-value decision
* human review requirement

### 4. Trace Everything

Every mission should produce a traceable record.

The system should be able to explain:

* which wing models participated
* what each wing model inferred
* what was filtered
* what was escalated
* why the carrier was activated
* whether human review occurred

### 5. Human Governance Remains Central

The carrier model is not the final authority in high-impact contexts.

Human review should remain available, especially when:

* decisions affect people
* outputs are uncertain
* safety risks exist
* attribution or reward allocation is involved

## Relationship to Other Protocols

Carrier Swarm Inference Architecture can connect with:

* AI Search Trace Receipt Standard
* Trace Receipt Protocol
* Structural Rumination Layer
* Memory Breathing Protocol
* Compute Access Royalty OS
* Origin Structure Market

This repository focuses on the inference relay layer:

> How should inference be distributed, routed, escalated, and recorded?

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

## Repository Structure

```text
.
├── README.md
├── CHANGELOG.md
├── schemas/
│   └── carrier-swarm-mission.schema.json
├── examples/
│   └── carrier-swarm-mission.example.yaml
└── scripts/
    └── validate_examples.py
```

## Roadmap

### v0.1 — Carrier Swarm Mission

Define the minimal mission record for carrier-swarm inference relay.

### v0.2 — Wing Role Registry

Define standard roles for wing models, including scout, router, compressor, verifier, guard, and memory agent.

### v0.3 — Activation Policy

Define when the carrier model should be activated and when early exit is allowed.

### v0.4 — Trace Receipt Integration

Connect carrier-swarm missions with trace receipts and contribution records.

### v0.5 — Compute and Royalty Integration

Add compute cost, energy cost, contribution weight, and reward allocation fields.

## Status

This repository is currently in early specification development.

Initial focus:

* define the carrier-swarm mission schema
* provide a valid example
* validate examples with a simple script
* prepare for `v0.1.0-candidate`

## License

TBD.
