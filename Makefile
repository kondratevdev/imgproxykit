SHELL := /usr/bin/env bash
POETRY ?= poetry
SMOKE_EXTRAS ?=
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

.PHONY: type-check
type-check: ## Run mypy, Pyright, Pyrefly and ty, including public API type tests
	$(POETRY) run mypy .
	$(POETRY) run pyright
	$(POETRY) run pyrefly check --remove-unused-ignores
	$(POETRY) run ty check

.PHONY: unit
unit: ## Run unit tests with pytest
	$(POETRY) run pytest --ignore=tests/test_integration

.PHONY: smoke
smoke: ## Check package imports (SMOKE_EXTRAS='django fastapi' for integrations)
	$(POETRY) run python -c 'from imgproxykit import Client, Transform'
	$(POETRY) run python -c 'from imgproxykit.options import *'
	$(POETRY) run python -c 'from imgproxykit.serialization import *'
	$(POETRY) run python -c 'from imgproxykit.signing import *'
	$(POETRY) run python -c 'from imgproxykit.integrations import *'
	for extra in $(SMOKE_EXTRAS); do \
	  case "$$extra" in \
	    django) $(POETRY) run python -c 'import imgproxykit.integrations.django' ;; \
	    fastapi) $(POETRY) run python -c 'from imgproxykit.integrations.fastapi import *' ;; \
	  esac; \
	done

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
check: lint type-check package smoke test ## Run all checks and tests
