# Carrier Swarm Inference Architecture

A lightweight protocol for coordinating central carrier models and specialized wing models to reduce unnecessary large-model activation through traceable inference relay.

## Status

**Current version:** `v0.3.0-candidate`
**Current focus:** Activation Policy
**Validation status:** GitHub Actions passed

This repository has reached its third functional validation point.

The repository now includes:

* `Carrier Swarm Mission`
* `Wing Role Registry`
* `Activation Policy`
* JSON Schemas
* YAML examples
* validation script
* GitHub Actions workflow

All v0.1, v0.2, and v0.3 examples validate successfully against their schemas.

## Overview

**Carrier Swarm Inference Architecture** defines a modular AI inference structure in which a central carrier model coordinates multiple lightweight wing models.

The carrier model is not treated as an always-on monolithic intelligence.
Instead, it serves as a coordination, integration, memory, escalation, and final reasoning node that is activated only when needed.

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
Compression / Verification / Safety Check
  ↓
Activation Policy
  ↓
Early Exit / Continue with Wings / Activate Carrier / Human Review / Halt
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

## Example: Carrier Swarm Mission

```yaml
mission_id: mission-2026-001
mission_type: inference_relay
description: >
  A minimal carrier-swarm inference relay mission where lightweight wing models
  perform initial classification, routing, and compression before escalating
  only necessary information to the carrier model.

carrier_node:
  id: local-carrier-model-01
  role: integration_and_final_reasoning
  model_class: local_carrier
  activation_mode: on_demand

wing_nodes:
  - id: scout-model-01
    role: scout
    model_class: lightweight_model
    local_inference:
      result: "Input appears to be a low-risk local event."
      confidence: 0.82
      early_exit_recommended: false
      escalation_recommended: true

  - id: router-model-01
    role: router
    model_class: specialized_agent
    local_inference:
      result: "Route to compression model before carrier integration."
      confidence: 0.88
      early_exit_recommended: false
      escalation_recommended: true

  - id: compression-model-01
    role: compressor
    model_class: small_model
    local_inference:
      result: "Compressed event report generated for carrier review."
      confidence: 0.91
      early_exit_recommended: false
      escalation_recommended: true

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
    - high_ambiguity
    - human_review_required
  confidence_threshold: 0.85
  risk_threshold: medium

escalation:
  carrier_activated: true
  reason: >
    Carrier activation was required because the scout confidence was below
    the mission threshold and human review was required.
  triggered_by:
    - scout-model-01
    - low_confidence
    - human_review_required

trace:
  receipt_required: true
  contribution_logging: true
  energy_logging: optional
  human_review_required: true
  trace_record_id: trace-carrier-swarm-2026-001

human_review:
  required: true
  status: pending
  reviewer_role: human_operator
```

## Example: Wing Role Registry

```yaml
registry_id: wing-role-registry-v0.2
version: v0.2.0-candidate
description: >
  A standard registry of wing model roles for Carrier Swarm Inference Architecture.
  Wing roles define how lightweight models scout, route, compress, verify, guard,
  remember, and trace inference missions before carrier activation.

roles:
  - role_id: scout
    display_name: Scout Wing
    category: scouting
    responsibility: >
      Performs initial observation and determines whether an input appears simple,
      repetitive, uncertain, risky, or worth escalating.
    typical_inputs:
      - raw_input
      - local_event
      - sensor_event
    typical_outputs:
      - initial_observation
      - confidence_score
      - early_exit_recommendation
      - escalation_recommendation
    activation_mode: always_first
    escalation_permission:
      can_request_carrier_activation: true
      can_end_mission_early: true
      can_request_human_review: false
    activation_conditions:
      - new_input_received
      - sensor_event_detected
    trace_requirements:
      log_input_summary: true
      log_output_summary: true
      log_confidence: true
      log_escalation_reason: true
    human_governance_note: >
      Scout wings may recommend escalation or early exit, but should not make
      final high-impact decisions.
```

## Example: Activation Policy

```yaml
policy_id: activation-policy-v0.3
version: v0.3.0-candidate
description: >
  A carrier activation policy for Carrier Swarm Inference Architecture.
  This policy defines when lightweight wing models may complete a mission locally,
  when the carrier model must be activated, and when human review is required.

default_carrier_activation: on_demand

early_exit:
  enabled: true
  allowed_when:
    - high_confidence_local_result
    - low_risk
    - routine_input
    - sufficient_wing_consensus
    - human_review_not_required
    - no_safety_concern
    - trace_complete
  requires_trace_record: true
  minimum_confidence: 0.9
  maximum_risk_level: low

carrier_activation_triggers:
  - trigger_id: low-confidence-trigger
    condition: low_confidence
    severity: medium
    activation_required: true
    human_review_required: false
    description: >
      Activate the carrier when wing confidence falls below the configured
      early-exit threshold.

  - trigger_id: conflicting-wing-reports-trigger
    condition: conflicting_wing_reports
    severity: high
    activation_required: true
    human_review_required: true
    description: >
      Activate the carrier and request human review when wing reports conflict
      in a way that affects the mission outcome.

  - trigger_id: safety-concern-trigger
    condition: safety_concern
    severity: critical
    activation_required: true
    human_review_required: true
    description: >
      Activate the carrier and require human review when a safety concern is
      detected by a safety guard wing.

thresholds:
  minimum_wing_confidence_for_early_exit: 0.9
  maximum_ambiguity_for_early_exit: 0.2
  minimum_consensus_ratio: 0.75
  risk_score_for_carrier_activation: 0.6
  risk_score_for_human_review: 0.8

escalation_decision:
  decision_required: true
  allowed_decisions:
    - early_exit
    - continue_with_wings
    - activate_carrier
    - request_human_review
    - halt_mission
  justification_required: true
  required_fields:
    - decision
    - reason
    - triggered_by
    - confidence
    - risk_level
    - human_review_status
    - trace_record_id

trace_requirements:
  log_activation_decision: true
  log_early_exit_decision: true
  log_trigger_conditions: true
  log_thresholds: true
  log_human_review_status: true

human_governance:
  human_review_available: true
  human_review_required_when:
    - high_risk
    - critical_risk
    - safety_concern
    - high_value_decision
    - conflicting_wing_reports
    - human_impacting_decision
    - attribution_or_reward_allocation
  note: >
    Carrier activation does not remove human governance. Human review remains
    required for safety-sensitive, high-impact, or attribution-related missions.
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
* why early exit was allowed
* whether human review occurred

### 7. Human Governance Remains Central

The carrier model is not the final authority in high-impact contexts.

Human review should remain available, especially when:

* decisions affect people
* outputs are uncertain
* safety risks exist
* attribution or reward allocation is involved

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
│   └── activation-policy.schema.json
├── examples/
│   ├── carrier-swarm-mission.example.yaml
│   ├── wing-role-registry.example.yaml
│   └── activation-policy.example.yaml
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

> How should inference be distributed, routed, escalated, role-assigned, policy-controlled, and recorded?

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

Potential fields include:

* wing contribution record
* carrier activation record
* early exit record
* filtered event record
* escalation explanation
* external trace receipt ID

### v0.5 — Compute and Royalty Integration

Add compute cost, optional energy cost, contribution weight, and reward allocation fields.

Potential integrations include:

* Compute Access Royalty OS
* Trace Receipt Protocol
* Origin Structure Market

## Conceptual Position

Carrier Swarm Inference Architecture does not reject large models.

It repositions them.

A large model should not be invoked as the default path for every input.
It should function as a carrier: a coordination, integration, memory, and final reasoning node.

Wing models perform the first movement.

The Activation Policy decides whether the mission can end early, continue with wings, activate the carrier, request human review, or halt.

The carrier integrates only when needed.

The Wing Role Registry ensures that the swarm does not become chaotic.
The Activation Policy ensures that the carrier does not become monolithic again.

This turns AI inference from a monolithic pipeline into a traceable, role-based, policy-controlled relay system.

In short:

> Monolith AGI is replaced by Carrier-Swarm AI.

## License

TBD.

