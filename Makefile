#!/usr/bin/env make

.PHONY: dep
dep:
	pip install poetry
	poetry install

.PHONY: test
test: lint format-check unit

.PHONY: unit
unit:
	poetry run py.test -vv

.PHONY: integration
integration:
	poetry run molecule test

.PHONY: cov
cov:
	poetry run py.test --cov apps --cov molecule_k3d --cov-report term-missing --showlocals

.PHONY: lint
lint:
	poetry run flake8

.PHONY: format
format:
	poetry run black .
	poetry run isort .

.PHONY: format-check
format-check:
	poetry run black --diff --check .
	poetry run isort --check-only --diff .

.PHONY: build-dist
build-dist:
	poetry build

.PHONY: dist-publish
dist-publish:
	poetry publish --build \
		-u $(PYPI_USERNAME) \
		-p $(PYPI_PASSWORD)
