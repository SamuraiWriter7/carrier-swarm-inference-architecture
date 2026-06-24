# Changelog

All notable changes to this project will be documented in this file.

This repository follows a lightweight candidate-based release process during early specification development.

## [Unreleased]

### Planned

* Define standard wing model roles in a Wing Role Registry.
* Add activation thresholds for carrier model escalation.
* Add trace receipt integration fields.
* Add compute cost and optional energy cost logging.
* Explore integration with Compute Access Royalty OS and Trace Receipt protocols.

## [v0.1.0-candidate] - 2026-06-24

### Added

* Initial repository structure for Carrier Swarm Inference Architecture.
* Added `README.md` describing the carrier-swarm inference relay model.
* Added `schemas/carrier-swarm-mission.schema.json`.
* Added `examples/carrier-swarm-mission.example.yaml`.
* Added `scripts/validate_examples.py` for validating YAML examples against JSON Schema.
* Added GitHub Actions workflow for automated validation.
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

This candidate release establishes the first minimal specification for replacing always-on monolithic AI inference with a carrier-swarm relay structure.

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
