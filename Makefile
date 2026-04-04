.DEFAULT_GOAL := help

.PHONY: help install run test lint

help:
	@echo "B3 SOC Brain – available targets:"
	@echo "  install  Install Python dependencies"
	@echo "  run      Start the API server (default: localhost:8000)"
	@echo "  test     Run the test suite"
	@echo "  lint     Run code style checks"

install:
	pip install -r requirements.txt

run:
	bash scripts/run.sh

test:
	python -m pytest tests/ -v

lint:
	python -m py_compile src/api/main.py && echo "Lint OK"
