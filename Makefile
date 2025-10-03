.PHONY: generate install clean test help

help:
	@echo "Speechall Python SDK - Available Commands"
	@echo ""
	@echo "  make generate    - Generate SDK from OpenAPI spec"
	@echo "  make install     - Install SDK locally for development"
	@echo "  make clean       - Remove generated files and build artifacts"
	@echo "  make test        - Run tests (if available)"
	@echo "  make help        - Show this help message"

generate:
	@./scripts/generate.sh

install:
	@echo "📦 Installing Speechall Python SDK..."
	pip install -e .

clean:
	@echo "🧹 Cleaning build artifacts..."
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

test:
	@echo "🧪 Running tests..."
	pytest tests/ -v
