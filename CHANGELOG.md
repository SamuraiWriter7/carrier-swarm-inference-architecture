# Changelog

All notable changes to this project will be documented in this file.

This repository follows a lightweight candidate-based release process during early specification development.

## [Unreleased]

### Planned

* Refine compute and royalty allocation semantics.
* Add stronger cross-schema references.
* Add optional examples for early-exit missions.
* Add optional examples for carrier-not-activated missions.
* Explore integration with Compute Access Royalty OS, Trace Receipt Protocol, AI Search Trace Receipt Standard, and Origin Structure Market.
* Consider whether v0.6 should continue in this repository or begin a second-stage repository.

## [v0.5.0-candidate] - 2026-06-24

### Added

* Added `schemas/compute-royalty-integration.schema.json`.
* Added `examples/compute-royalty-integration.example.yaml`.
* Updated `scripts/validate_examples.py` to validate:

  * `Carrier Swarm Mission`
  * `Wing Role Registry`
  * `Activation Policy`
  * `Trace Receipt Integration`
  * `Compute and Royalty Integration`
* Updated `README.md` to reflect v0.5 status, scope, validation output, repository structure, roadmap, and conceptual position.
* Confirmed GitHub Actions validation passes with v0.5 files.

### Defined

* Introduced `Compute and Royalty Integration` as the compute, cost, contribution, and reward-allocation layer for carrier-swarm inference systems.
* Defined how carrier-swarm missions can connect to compute usage records.
* Defined optional energy cost records.
* Defined optional monetary cost estimates.
* Defined contribution allocation records.
* Defined reward eligibility.
* Defined royalty hooks.
* Defined compute access hooks.
* Defined origin attribution hooks.
* Defined audit export hooks.
* Defined allocation boundaries.

### Compute and Royalty Integration Fields

The v0.5 schema defines:

* integration identifier
* version
* mission reference
* trace reference
* compute records
* contribution allocation
* royalty hooks
* allocation boundary

### Initial Compute Records

The v0.5 example includes compute records for:

* Scout Wing
* Router Wing
* Compression Wing
* Carrier Node
* Human Operator

Each compute record may include:

* node identifier
* node type
* role
* compute unit
* compute cost
* optional energy cost in millijoules
* optional monetary cost estimate
* cost recording status
* cost estimation method

### Initial Allocation Records

The v0.5 example includes contribution allocation records for:

* scouting
* routing
* compression
* carrier integration
* human review

Each allocation record may include:

* participant identifier
* participant type
* role
* contribution weight
* reward eligibility
* allocation note

### Initial Royalty Hooks

The v0.5 example includes hooks for:

* royalty allocation
* origin attribution
* audit export

Target protocols include:

* Compute Access Royalty OS
* Origin Structure Market
* Trace Receipt Protocol

### Validation

* Confirmed that `carrier-swarm-mission.example.yaml` validates successfully against `carrier-swarm-mission.schema.json`.
* Confirmed that `wing-role-registry.example.yaml` validates successfully against `wing-role-registry.schema.json`.
* Confirmed that `activation-policy.example.yaml` validates successfully against `activation-policy.schema.json`.
* Confirmed that `trace-receipt-integration.example.yaml` validates successfully against `trace-receipt-integration.schema.json`.
* Confirmed that `compute-royalty-integration.example.yaml` validates successfully against `compute-royalty-integration.schema.json`.
* Confirmed that GitHub Actions validation workflow passes.

### Conceptual Position

`v0.5.0-candidate` establishes the compute and royalty integration layer of Carrier Swarm Inference Architecture.

In v0.1, the repository defined how a mission is recorded.

In v0.2, the repository defined what each wing model is allowed and expected to do.

In v0.3, the repository defined when the carrier model should wake up.

In v0.4, the repository defined how the mission proves what happened.

In v0.5, the repository defines how compute usage, optional energy cost, contribution weight, and reward allocation readiness can be connected.

This turns carrier-swarm inference into a compute-aware, trace-aware, contribution-aware, and royalty-ready relay system.

The core principle remains:

> Do not invoke the largest model by default.
> Let smaller models scout, filter, compress, verify, route, record, and account first.

### Repository Status

`v0.5.0-candidate` represents the fifth functional validation point of the repository.

The repository now includes:

* mission schema
* mission example
* wing role registry schema
* wing role registry example
* activation policy schema
* activation policy example
* trace receipt integration schema
* trace receipt integration example
* compute and royalty integration schema
* compute and royalty integration example
* validation script
* GitHub Actions workflow
* validated v0.1, v0.2, v0.3, v0.4, and v0.5 examples

### First Arc Summary

The first arc now defines a complete carrier-swarm inference lifecycle:

1. Record the mission.
2. Define the wings.
3. Decide when the carrier wakes up.
4. Prove what happened.
5. Connect compute, contribution, and reward allocation.

## [v0.4.0-candidate] - 2026-06-24

### Added

* Added `schemas/trace-receipt-integration.schema.json`.
* Added `examples/trace-receipt-integration.example.yaml`.
* Updated `scripts/validate_examples.py` to validate:

  * `Carrier Swarm Mission`
  * `Wing Role Registry`
  * `Activation Policy`
  * `Trace Receipt Integration`
* Updated `README.md` to reflect v0.4 status, scope, validation output, repository structure, roadmap, and conceptual position.
* Confirmed GitHub Actions validation passes with v0.4 files.

### Defined

* Introduced `Trace Receipt Integration` as the trace and audit layer for carrier-swarm inference systems.
* Defined how a carrier-swarm mission can link to trace receipts.
* Defined contribution records for wing, carrier, trace, and human participants.
* Defined carrier activation records.
* Defined early exit records.
* Defined filtered event records.
* Defined audit boundaries.
* Defined future readiness for royalty or compute allocation integration.

### Validation

* Confirmed that `carrier-swarm-mission.example.yaml` validates successfully against `carrier-swarm-mission.schema.json`.
* Confirmed that `wing-role-registry.example.yaml` validates successfully against `wing-role-registry.schema.json`.
* Confirmed that `activation-policy.example.yaml` validates successfully against `activation-policy.schema.json`.
* Confirmed that `trace-receipt-integration.example.yaml` validates successfully against `trace-receipt-integration.schema.json`.
* Confirmed that GitHub Actions validation workflow passes.

### Conceptual Position

`v0.4.0-candidate` established the trace and audit layer of Carrier Swarm Inference Architecture.

It defines how the mission proves what happened.

## [v0.3.0-candidate] - 2026-06-24

### Added

* Added `schemas/activation-policy.schema.json`.
* Added `examples/activation-policy.example.yaml`.
* Updated `scripts/validate_examples.py` to validate:

  * `Carrier Swarm Mission`
  * `Wing Role Registry`
  * `Activation Policy`
* Updated `README.md` to reflect v0.3 status, scope, validation output, repository structure, roadmap, and conceptual position.
* Confirmed GitHub Actions validation passes with v0.3 files.

### Defined

* Introduced the `Activation Policy` as the decision layer for carrier-swarm inference systems.
* Defined when the carrier model should be activated.
* Defined when early exit is allowed.
* Defined when wing models may continue without carrier activation.
* Defined when human review is required.
* Defined when a mission may be halted.
* Defined initial escalation decision outcomes:

  * early exit
  * continue with wings
  * activate carrier
  * request human review
  * halt mission

### Validation

* Confirmed that `carrier-swarm-mission.example.yaml` validates successfully against `carrier-swarm-mission.schema.json`.
* Confirmed that `wing-role-registry.example.yaml` validates successfully against `wing-role-registry.schema.json`.
* Confirmed that `activation-policy.example.yaml` validates successfully against `activation-policy.schema.json`.
* Confirmed that GitHub Actions validation workflow passes.

### Conceptual Position

`v0.3.0-candidate` established the energy-aware decision layer of Carrier Swarm Inference Architecture.

It defines when the carrier model should wake up.

## [v0.2.0-candidate] - 2026-06-24

### Added

* Added `schemas/wing-role-registry.schema.json`.
* Added `examples/wing-role-registry.example.yaml`.
* Updated `scripts/validate_examples.py` to validate both:

  * `Carrier Swarm Mission`
  * `Wing Role Registry`
* Updated `README.md` to reflect v0.2 status, scope, validation output, repository structure, and roadmap.
* Confirmed GitHub Actions validation passes with v0.2 files.

### Defined

* Introduced the `Wing Role Registry` as the standard role definition layer for carrier-swarm inference systems.
* Defined wing roles as lightweight specialized inference units with explicit:

  * responsibility
  * activation mode
  * escalation permission
  * activation conditions
  * trace requirements
  * human governance notes
* Defined initial wing roles:

  * Scout Wing
  * Router Wing
  * Compression Wing
  * Verification Wing
  * Safety Guard Wing
  * Memory Wing
  * Trace Wing

### Validation

* Confirmed that `carrier-swarm-mission.example.yaml` validates successfully against `carrier-swarm-mission.schema.json`.
* Confirmed that `wing-role-registry.example.yaml` validates successfully against `wing-role-registry.schema.json`.
* Confirmed that GitHub Actions validation workflow passes.

### Conceptual Position

`v0.2.0-candidate` turned the carrier-swarm model from a general inference relay concept into a role-based architecture.

It defines what each wing model is allowed and expected to do.

## [v0.1.0-candidate] - 2026-06-24

### Added

* Initial repository structure for Carrier Swarm Inference Architecture.
* Added `README.md` describing the carrier-swarm inference relay model.
* Added `schemas/carrier-swarm-mission.schema.json`.
* Added `examples/carrier-swarm-mission.example.yaml`.
* Added `scripts/validate_examples.py` for validating YAML examples against JSON Schema.
* Added GitHub Actions workflow for automated validation.
* Added `CHANGELOG.md`.
* Established the initial `Carrier Swarm Mission` record format.

### Defined

* Carrier model as an on-demand coordination, integration, memory, and final reasoning node.
* Wing models as lightweight specialized inference units.
* Minimal relay cycle:

  * dispatch
  * local inference
  * event filtering
  * return report
  * carrier integration
  * human review
  * trace record
* Initial activation policy fields:

  * central activation mode
  * early exit flag
  * escalation conditions
  * confidence threshold
  * risk threshold
* Initial trace fields:

  * receipt requirement
  * contribution logging
  * optional energy logging
  * human review requirement
  * external trace record identifier

### Validation

* Confirmed that `carrier-swarm-mission.example.yaml` validates successfully against `carrier-swarm-mission.schema.json`.
* Confirmed that GitHub Actions validation workflow passes.

### Conceptual Position

`v0.1.0-candidate` established the first minimal specification for replacing always-on monolithic AI inference with a carrier-swarm relay structure.

It defines how a carrier-swarm mission is recorded.
