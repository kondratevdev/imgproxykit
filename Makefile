SHELL := /usr/bin/env bash
POETRY ?= poetry
.DEFAULT_GOAL := help

.PHONY: help
help: ## Show the help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: lint
lint: ## Run linting checks (ruff, flake8, slotscheck, import-linter)
	$(POETRY) run ruff check --exit-non-zero-on-fix
	$(POETRY) run ruff format --check --diff
	$(POETRY) run flake8 .
	$(POETRY) run slotscheck -v -m imgproxykit
	$(POETRY) run lint-imports

# TODO: Add accepted and rejected public API typing examples for mypy and
# Pyright: credentials, exclusive URL arguments, formats, and option types.
.PHONY: type-check
type-check: ## Run mypy, Pyright, Pyrefly and ty, including public API type tests
	$(POETRY) run mypy .
	$(POETRY) run pyright
	$(POETRY) run pyrefly check --remove-unused-ignores
	$(POETRY) run ty check

.PHONY: unit
unit: ## Run unit tests with pytest
	$(POETRY) run pytest --ignore=tests/test_integration

.PHONY: integration
integration: ## Run integration tests (requires Docker)
	$(POETRY) run pytest tests/test_integration --cov-fail-under=0

.PHONY: package
package: ## Check package dependencies with pip
	$(POETRY) check --lock
	$(POETRY) run pip check

.PHONY: docs
docs: ## Build HTML documentation (install dependencies with poetry install --with docs)
	$(POETRY) run sphinx-build -W -b html docs docs/_build/html

.PHONY: test
test: ## Run all tests including integration tests (requires Docker)
	$(POETRY) run pytest

.PHONY: check
check: lint type-check package test ## Run all checks and tests
