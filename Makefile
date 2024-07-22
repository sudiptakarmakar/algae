.PHONY: clean clean-test clean-pyc clean-build

PYTHON             ?= python3.12
VENV               := venv

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/ false/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

.PHONY: env
env: setup.cfg setup.py requirements.txt
	test -d $(VENV) || $(PYTHON) -m venv $(VENV)

lint: venv ## check style with flake8
	$(VENV)/bin/$(PYTHON) -m black --line-length=88 src/algae tests
	$(VENV)/bin/$(PYTHON) -m flake8 src/algae tests

.PHONY: install
install: clean env
	$(VENV)/bin/$(PYTHON) -m pip install .

.PHONY: test
test: install
	$(VENV)/bin/$(PYTHON) -m pip install pytest pytest-custom_exit_code
	$(VENV)/bin/$(PYTHON) -m pytest --suppress-no-test-exit-code -vvv tests

.PHONY: coverage
coverage: install
	$(VENV)/bin/$(PYTHON) -m pip install pytest pytest-custom_exit_code coverage pytest-cov
	$(VENV)/bin/$(PYTHON) -m coverage run --source src/algae -m pytest --suppress-no-test-exit-code -vvv tests
	$(VENV)/bin/$(PYTHON) -m coverage report -m
