#!/usr/bin/env python3
"""
Validate Carrier Swarm Inference Architecture examples.

This script validates YAML example files against their corresponding
JSON Schema definitions.

Usage:
    python scripts/validate_examples.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

ROOT_DIR = Path(__file__).resolve().parents[1]

VALIDATION_TARGETS = [
    {
        "name": "Carrier Swarm Mission",
        "schema": ROOT_DIR / "schemas" / "carrier-swarm-mission.schema.json",
        "example": ROOT_DIR / "examples" / "carrier-swarm-mission.example.yaml",
    },
    {
        "name": "Wing Role Registry",
        "schema": ROOT_DIR / "schemas" / "wing-role-registry.schema.json",
        "example": ROOT_DIR / "examples" / "wing-role-registry.example.yaml",
    },
]


def load_json(path: Path) -> dict[str, Any]:
    """Load a JSON file."""
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_yaml(path: Path) -> Any:
    """Load a YAML file."""
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def validate_target(name: str, schema_path: Path, example_path: Path) -> bool:
    """Validate one YAML example against one JSON Schema."""
    print(f"[validate] {name}")
    print(f"  schema : {schema_path.relative_to(ROOT_DIR)}")
    print(f"  example: {example_path.relative_to(ROOT_DIR)}")

    if not schema_path.exists():
        print(f"[error] Schema file not found: {schema_path}")
        return False

    if not example_path.exists():
        print(f"[error] Example file not found: {example_path}")
        return False

    try:
        schema = load_json(schema_path)
        example = load_yaml(example_path)
    except Exception as error:
        print(f"[error] Failed to load files: {error}")
        return False

    try:
        Draft202012Validator.check_schema(schema)
    except Exception as error:
        print(f"[error] Invalid JSON Schema: {error}")
        return False

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(example), key=lambda error: list(error.path))

    if errors:
        print(f"[error] {name} validation failed")
        for error in errors:
            path = ".".join(str(part) for part in error.path)
            location = path if path else "<root>"
            print(f"  - path: {location}")
            print(f"    message: {error.message}")
        return False

    print(f"[ok] {example_path.name} is valid")
    return True


def main() -> int:
    """Run all validation targets."""
    all_valid = True

    for target in VALIDATION_TARGETS:
        is_valid = validate_target(
            name=target["name"],
            schema_path=target["schema"],
            example_path=target["example"],
        )
        all_valid = all_valid and is_valid

    if not all_valid:
        return 1

    print("[ok] all examples are valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())

