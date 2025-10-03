#!/bin/bash

# Speechall Python SDK Generation Script
# This script generates the Python SDK from the OpenAPI specification

set -e  # Exit on error

echo "🚀 Generating Speechall Python SDK..."

# Path to OpenAPI spec
OPENAPI_PATH="../speechall-openapi/openapi.yaml"

# Check if OpenAPI file exists
if [ ! -f "$OPENAPI_PATH" ]; then
    echo "❌ Error: OpenAPI spec not found at $OPENAPI_PATH"
    exit 1
fi

# Generate the client
openapi-python-client generate \
    --path "$OPENAPI_PATH" \
    --config config.yml \
    --overwrite

echo "✅ SDK generation complete!"
echo ""
echo "Next steps:"
echo "  1. Review the generated code in the speechall/ directory"
echo "  2. Run tests if available"
echo "  3. Install locally: pip install -e ."
