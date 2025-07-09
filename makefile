.PHONY: help install test lint format check clean

help:
	@echo "Available commands:"
	@echo "  make install   - Create venv and install dependencies"
	@echo "  make test      - Run pytest"
	@echo "  make lint      - Run flake8"
	@echo "  make format    - Auto-format code with black"
	@echo "  make check     - Run lint, format check, and tests"
	@echo "  make clean     - Remove .pyc files and __pycache__ folders"

install:
	python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

test:
	pytest

lint:
	flake8 .

format:
	black .

check: lint
	black --check .
	pytest

clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -r {} +
