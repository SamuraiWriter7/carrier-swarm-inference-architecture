# Changelog

All notable changes to this project will be documented in this file.

This repository follows a lightweight candidate-based release process during early specification development.

## [Unreleased]

### Planned

* Add Compute and Royalty Integration.
* Define compute cost records.
* Define optional energy cost records.
* Define reward allocation readiness.
* Define royalty allocation hooks.
* Explore integration with Compute Access Royalty OS, Trace Receipt Protocol, and Origin Structure Market.

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

### Trace Receipt Integration Fields

The v0.4 schema defines:

* integration identifier
* version
* mission reference
* trace receipts
* contribution records
* carrier activation record
* early exit records
* filtered event records
* audit boundary

### Validation

* Confirmed that `carrier-swarm-mission.example.yaml` validates successfully against `carrier-swarm-mission.schema.json`.
* Confirmed that `wing-role-registry.example.yaml` validates successfully against `wing-role-registry.schema.json`.
* Confirmed that `activation-policy.example.yaml` validates successfully against `activation-policy.schema.json`.
* Confirmed that `trace-receipt-integration.example.yaml` validates successfully against `trace-receipt-integration.schema.json`.
* Confirmed that GitHub Actions validation workflow passes.

### Conceptual Position

`v0.4.0-candidate` establishes the trace and audit layer of Carrier Swarm Inference Architecture.

In v0.1, the repository defined how a mission is recorded.

In v0.2, the repository defined what each wing model is allowed and expected to do.

In v0.3, the repository defined when the carrier model should wake up.

In v0.4, the repository defines how the mission proves what happened.

This prevents carrier-swarm inference from becoming an opaque multi-agent process.

The system should be able to answer:

* who participated;
* what each wing did;
* what was filtered;
* why early exit was rejected or accepted;
* why the carrier was activated;
* whether human review was required;
* whether the record is ready for future royalty or compute allocation integration.

The core principle remains:

> Do not invoke the largest model by default.
> Let smaller models scout, filter, compress, verify, route, and record first.

### Repository Status

`v0.4.0-candidate` represents the fourth functional validation point of the repository.

The repository now includes:

* mission schema
* mission example
* wing role registry schema
* wing role registry example
* activation policy schema
* activation policy example
* trace receipt integration schema
* trace receipt integration example
* validation script
* GitHub Actions workflow
* validated v0.1, v0.2, v0.3, and v0.4 examples

## [v0.3.0-candidate] - 2026-06-24

### Added

* Added `schemas/activation-policy.schema.json`.
* Added `examples/activation-policy.example.yaml`.
* Updated `scripts/validate_examples.py` to validate:

  * `Carrier Swarm Mission`
  * `Wing Role Registry`
  * `Activation Policy`
* Updated `README.md` to reflect v0.3 status, scope, examples, validation output, repository structure, roadmap, and conceptual position.
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

### Activation Policy Fields

The v0.3 schema defines:

* policy identifier
* version
* default carrier activation mode
* early exit rules
* carrier activation triggers
* optional numeric thresholds
* escalation decision records
* trace requirements
* human governance boundaries

### Validation

* Confirmed that `carrier-swarm-mission.example.yaml` validates successfully against `carrier-swarm-mission.schema.json`.
* Confirmed that `wing-role-registry.example.yaml` validates successfully against `wing-role-registry.schema.json`.
* Confirmed that `activation-policy.example.yaml` validates successfully against `activation-policy.schema.json`.
* Confirmed that GitHub Actions validation workflow passes.

### Conceptual Position

`v0.3.0-candidate` establishes the energy-aware decision layer of Carrier Swarm Inference Architecture.

In v0.1, the repository defined how a mission is recorded.

In v0.2, the repository defined what each wing model is allowed and expected to do.

In v0.3, the repository defines when the carrier model should wake up.

This prevents the carrier from becoming an always-on monolithic system again.

The core principle remains:

> Do not invoke the largest model by default.
> Let smaller models scout, filter, compress, verify, route, and record first.

### Repository Status

`v0.3.0-candidate` represents the third functional validation point of the repository.

The repository now includes:

* mission schema
* mission example
* wing role registry schema
* wing role registry example
* activation policy schema
* activation policy example
* validation script
* GitHub Actions workflow
* validated v0.1, v0.2, and v0.3 examples

## [v0.2.0-candidate] - 2026-06-24

### Added

* Added `schemas/wing-role-registry.schema.json`.
* Added `examples/wing-role-registry.example.yaml`.
* Updated `scripts/validate_examples.py` to validate both:

  * `Carrier Swarm Mission`
  * `Wing Role Registry`
* Updated `README.md` to reflect v0.2 status, scope, examples, validation output, repository structure, and roadmap.
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

`v0.2.0-candidate` turns the carrier-swarm model from a general inference relay concept into a role-based architecture.

In v0.1, the repository defined how a mission is recorded.

In v0.2, the repository defines what each wing model is allowed and expected to do.

This prevents the swarm from becoming a vague collection of helper agents.
Each wing now has a defined role, activation condition, permission boundary, and trace obligation.

The core principle remains:

> Do not invoke the largest model by default.
> Let smaller models scout, filter, compress, verify, route, and record first.

### Repository Status

`v0.2.0-candidate` represents the second functional validation point of the repository.

The repository now includes:

* mission schema
* mission example
* wing role registry schema
* wing role registry example
* validation script
* GitHub Actions workflow
* validated v0.1 and v0.2 examples

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

This candidate release established the first minimal specification for replacing always-on monolithic AI inference with a carrier-swarm relay structure.

The core principle is:

> Do not invoke the largest model by default.
> Let smaller models scout, filter, compress, and route first.

In this model:

* the carrier is not a monolithic god model;
* wing models are not reduced copies of the carrier;
* inference is routed, filtered, escalated, and recorded;
* human review remains part of the governance boundary.

### Repository Status

`v0.1.0-candidate` represents the first functional validation point of the repository.

The initial carrier-swarm mission schema, example, validation script, and GitHub Actions workflow are now in place.
