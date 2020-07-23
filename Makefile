.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

VENV_NAME?=${PWD}/venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
VENV_PYTHON=${VENV_NAME}/bin/python

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: venv ## check style with flake8
	${VENV_PYTHON} -m black algae tests
	${VENV_PYTHON} -m flake8 algae tests

test: venv  ## run tests quickly with virtualenv Python
	${VENV_PYTHON} -m pytest
	${VENV_PYTHON} -m coverage report -m

test-all: venv ## run tests on every Python version with tox
	${VENV_PYTHON} -m tox

venv: $(VENV_NAME)/bin/activate ## create and activate virtualenv

$(VENV_NAME)/bin/activate: setup.py requirements_dev.txt
	test -d $(VENV_NAME) || virtualenv -p `which python3.7` $(VENV_NAME)
	${VENV_PYTHON} -m pip install --upgrade pip
	${VENV_PYTHON} -m pip install --upgrade -r requirements_dev.txt
	${VENV_PYTHON} -m pip install -e .
	touch $(VENV_NAME)/bin/activate

coverage: ## check code coverage quickly with the default Python
	${VENV_PYTHON} -m coverage run --source algae -m pytest
	${VENV_PYTHON} -m coverage report -m
	${VENV_PYTHON} -m coverage html
	$(BROWSER) htmlcov/index.html

docs: venv ## generate Sphinx HTML documentation, including API docs
	rm -f docs/algae.rst
	rm -f docs/modules.rst
	$(VENV_ACTIVATE) && sphinx-apidoc -o docs/ algae
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: venv dist ## package and upload a release
	${VENV_PYTHON} -m twine upload dist/*

dist: clean ## builds source and wheel package
	${VENV_PYTHON} setup.py sdist
	${VENV_PYTHON} setup.py bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	${VENV_PYTHON} setup.py install
