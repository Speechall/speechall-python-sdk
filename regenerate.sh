#!/bin/bash

# OpenAPI Client Regeneration Script
# This script regenerates the OpenAPI client code while preserving custom files

set -e  # Exit on any error

# Configuration
OPENAPI_SPEC_PATH="../speechall-openapi/openapi.yaml"
GENERATOR="python-pydantic-v1"
OUTPUT_DIR="."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🔄 Speechall OpenAPI Client Regeneration${NC}"
echo "=============================================="

# Check if OpenAPI spec exists
if [ ! -f "$OPENAPI_SPEC_PATH" ]; then
    echo -e "${RED}❌ Error: OpenAPI spec not found at $OPENAPI_SPEC_PATH${NC}"
    echo "Please ensure the speechall-openapi repository is cloned at ../speechall-openapi/"
    exit 1
fi

# Check if openapi-generator is available
if ! command -v openapi-generator &> /dev/null; then
    echo -e "${RED}❌ Error: openapi-generator command not found${NC}"
    echo "Please install it with: npm install @openapitools/openapi-generator-cli -g"
    echo "Or use: brew install openapi-generator"
    exit 1
fi

# Show current status
echo -e "${YELLOW}📋 Current status:${NC}"
echo "  OpenAPI Spec: $OPENAPI_SPEC_PATH"
echo "  Generator: $GENERATOR"
echo "  Output Directory: $OUTPUT_DIR"
echo ""

# Backup custom files (just in case)
echo -e "${YELLOW}💾 Creating backup of custom files...${NC}"
BACKUP_DIR="backup_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

# Backup files if they exist
for file in example_transcribe.py simple_example.py EXAMPLE_README.md pyproject.toml; do
    if [ -f "$file" ]; then
        cp "$file" "$BACKUP_DIR/"
        echo "  ✅ Backed up $file"
    fi
done

# Regenerate the client
echo ""
echo -e "${BLUE}🔧 Regenerating OpenAPI client...${NC}"
openapi-generator generate \
    -i "$OPENAPI_SPEC_PATH" \
    -g "$GENERATOR" \
    -o "$OUTPUT_DIR" \
    --skip-validate-spec

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Client regeneration completed successfully!${NC}"
else
    echo -e "${RED}❌ Client regeneration failed!${NC}"
    exit 1
fi

# Restore custom pyproject.toml if backup exists
if [ -f "$BACKUP_DIR/pyproject.toml" ]; then
    echo -e "${YELLOW}🔧 Restoring custom pyproject.toml...${NC}"
    cp "$BACKUP_DIR/pyproject.toml" pyproject.toml
    echo "  ✅ Custom pyproject.toml restored"
fi

# Apply automatic fixes for known issues
echo ""
echo -e "${BLUE}🔧 Applying automatic fixes...${NC}"
if [ -f "fix_transcription_response.py" ]; then
    python3 fix_transcription_response.py
    if [ $? -eq 0 ]; then
        echo "  ✅ TranscriptionResponse oneOf fix applied"
    else
        echo -e "${YELLOW}  ⚠️  TranscriptionResponse fix failed - you may need to apply it manually${NC}"
    fi
else
    echo -e "${YELLOW}  ⚠️  fix_transcription_response.py not found - skipping automatic fix${NC}"
fi

# Reinstall dependencies
echo ""
echo -e "${BLUE}📦 Updating dependencies...${NC}"
if command -v uv &> /dev/null; then
    uv sync
    echo -e "${GREEN}✅ Dependencies updated with uv${NC}"
else
    pip install -r requirements.txt
    echo -e "${GREEN}✅ Dependencies updated with pip${NC}"
fi

# Clean up old backup if successful
echo ""
echo -e "${YELLOW}🧹 Cleaning up...${NC}"
if [ -d "$BACKUP_DIR" ]; then
    echo "Backup created at: $BACKUP_DIR"
    echo "You can safely delete it if everything looks good: rm -rf $BACKUP_DIR"
fi

echo ""
echo -e "${GREEN}🎉 Regeneration complete!${NC}"
echo ""
echo -e "${BLUE}📚 Next steps:${NC}"
echo "1. Test your examples: uv run python example_transcribe.py"
echo "2. Check for any new models or features in the updated client"
echo "3. Update your code if there are breaking changes"
echo "4. Delete the backup folder once you've verified everything works" 