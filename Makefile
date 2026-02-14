PYTHON = python3
MAIN = main.py
VENV = .venv
PIP = $(VENV)/bin/pip
PY = $(VENV)/bin/python

install:
	$(PYTHON) -m venv $(VENV)
	. $(VENV)/bin/activate && pip install --upgrade pip
	@if [ -f requirements.txt ]; then \
		. $(VENV)/bin/activate && pip install -r requirements.txt; \
	fi
	. $(VENV)/bin/activate && pip install flake8 mypy

run:
	$(PY) $(MAIN)

debug:
	$(PY) -m pdb $(MAIN)

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".venv" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

lint:
	$(PY) -m flake8 .
	$(PY) -m mypy . \
		--warn-return-any \
		--warn-unused-ignores \
		--ignore-missing-imports \
		--disallow-untyped-defs \
		--check-untyped-defs

lint-strict:
	$(PY) -m flake8 .
	$(PY) -m mypy . --strict


.PHONY: install run debug clean lint lint-strict
