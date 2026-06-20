#!/bin/bash
set -e

echo "🔍 Validating OpenAPI spec..."
# Check if OpenAPI file exists
if [ ! -f "../../Speechall-Repositories/speechall-openapi/openapi.yaml" ]; then
    echo "❌ Error: OpenAPI spec not found at ../../Speechall-Repositories/speechall-openapi/openapi.yaml"
    exit 1
fi

echo "✅ OpenAPI spec found"

echo "🚀 Generating Python SDK with Fern..."
fern generate --local --force

echo "✅ SDK generation complete!"

# Optional: Run tests if they exist
if [ -f "pytest.ini" ] || [ -d "tests" ]; then
    echo "🧪 Running tests..."
    if command -v pytest &> /dev/null; then
        pytest
    else
        echo "⚠️  pytest not installed, skipping tests"
    fi
fi

echo "✨ Regeneration complete!"
