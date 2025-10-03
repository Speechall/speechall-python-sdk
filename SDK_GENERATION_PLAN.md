# Speechall Python SDK Generation Plan

## Overview

This document outlines the complete plan for generating a Python SDK from the Speechall OpenAPI specification using the `openapi-python-client` library. The goal is to minimize post-generation manual work so that whenever the OpenAPI spec changes, regeneration is as simple as running a single command.

## Prerequisites

- Python 3.8 or higher
- Access to the OpenAPI spec at `../speechall-openapi/openapi.yaml`
- Git for version control

## Implementation Steps

### 1. Install Required Tools

#### Option A: Using pipx (Recommended)
```bash
# Install pipx if not already installed
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Install openapi-python-client with dependencies
pipx install openapi-python-client --include-deps

# Install ruff for code formatting
pipx install ruff
```

#### Option B: Using pip
```bash
pip install openapi-python-client
pip install ruff
```

### 2. Create Configuration File

Create `config.yml` in the root directory:

```yaml
# Speechall Python SDK Configuration for openapi-python-client

# Project and package naming
project_name_override: "speechall-python-sdk"
package_name_override: "speechall"
package_version_override: "0.1.0"

# Code generation options
use_path_prefixes_for_title_model_names: false
literal_enums: true
docstrings_on_attributes: true

# Field naming
field_prefix: "field_"

# Post-generation hooks - automatically format and lint code
post_hooks:
  - "ruff check . --fix"
  - "ruff format ."

# Class overrides (add custom mappings as needed)
# Example:
# class_overrides:
#   OpenAI_CreateTranscriptionRequest:
#     class_name: CreateTranscriptionRequest
#     module_name: create_transcription_request
```

### 3. Create Generation Script

Create `scripts/generate.sh`:

```bash
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
```

Make it executable:
```bash
chmod +x scripts/generate.sh
```

### 4. Create Makefile

Create `Makefile` in the root directory:

```makefile
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
```

### 5. Create pyproject.toml

Create `pyproject.toml` for modern Python packaging:

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "speechall-python-sdk"
version = "0.1.0"
description = "Python SDK for the Speechall API - Speech-to-Text Service"
readme = "README.md"
requires-python = ">=3.8"
license = { text = "MIT" }
authors = [
    { name = "Speechall", email = "support@speechall.com" }
]
keywords = ["speechall", "speech-to-text", "transcription", "api", "sdk"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]

dependencies = [
    "httpx>=0.20.0",
    "attrs>=21.3.0",
    "python-dateutil>=2.8.2",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-asyncio>=0.18.0",
    "ruff>=0.1.0",
    "mypy>=1.0.0",
]

[project.urls]
Homepage = "https://speechall.com"
Documentation = "https://docs.speechall.com"
Repository = "https://github.com/speechall/speechall-python-sdk"
"Bug Tracker" = "https://github.com/speechall/speechall-python-sdk/issues"

[tool.ruff]
line-length = 120
target-version = "py38"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "W"]
ignore = []

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
python_functions = "test_*"
asyncio_mode = "auto"
```

### 6. Update .gitignore

Add generated SDK-specific entries to `.gitignore`:

```gitignore
# Add these lines to the existing .gitignore

# Generated SDK (we commit this)
# speechall-python-sdk/  # DO NOT ignore - we track the generated code

# Scripts directory should be tracked
# !scripts/
```

**Note**: The generated SDK code SHOULD be committed to version control for easy distribution and visibility of changes.

### 7. Create Initial README.md

Create `README.md`:

```markdown
# Speechall Python SDK

Python SDK for the [Speechall API](https://speechall.com) - A powerful speech-to-text service supporting multiple providers and models.

## Installation

```bash
pip install speechall-python-sdk
```

Or install from source:

```bash
git clone https://github.com/speechall/speechall-python-sdk.git
cd speechall-python-sdk
pip install -e .
```

## Quick Start

```python
from speechall import Client

# Initialize the client with your API key
client = Client(base_url="https://api.speechall.com/v1", token="your-api-key")

# Transcribe an audio file
with open("audio.mp3", "rb") as audio_file:
    response = client.transcribe(
        model="openai.whisper-1",
        language="en",
        output_format="json",
        file=audio_file
    )

print(response.text)
```

## Features

- 🎯 Support for multiple STT providers (OpenAI, Deepgram, AssemblyAI, and more)
- 🌍 Multi-language transcription
- 🎭 Speaker diarization
- 📝 Multiple output formats (text, JSON, SRT, VTT)
- 🔄 Custom replacement rules
- ⚡ Async/await support
- 🔐 Bearer token authentication

## API Documentation

For detailed API documentation, visit [https://docs.speechall.com](https://docs.speechall.com)

## Available Models

Get a list of all available models:

```python
models = client.list_speech_to_text_models()
for model in models:
    print(f"{model.id}: {model.display_name}")
```

## Advanced Usage

### Transcribe from URL

```python
response = client.transcribe_remote(
    file_url="https://example.com/audio.mp3",
    model="deepgram.nova-2",
    language="en",
    output_format="json",
    diarization=True
)
```

### OpenAI-Compatible Endpoints

```python
# Use OpenAI-compatible transcription endpoint
response = client.openai_compatible_create_transcription(
    file=audio_file,
    model="openai.whisper-1",
    response_format="verbose_json",
    temperature=0.0
)
```

## Development

### Regenerating the SDK

When the OpenAPI specification is updated, regenerate the SDK:

```bash
make generate
```

Or run the script directly:

```bash
./scripts/generate.sh
```

### Running Tests

```bash
make test
```

### Installing for Development

```bash
make install
```

## License

MIT License - see [LICENSE](LICENSE) file for details

## Support

- 📧 Email: support@speechall.com
- 🌐 Website: https://speechall.com
- 📚 Documentation: https://docs.speechall.com
```

### 8. Create scripts Directory

```bash
mkdir -p scripts
```

### 9. Initial Generation

Run the generation for the first time:

```bash
./scripts/generate.sh
```

This will create:
- `speechall-python-sdk/` directory with the generated client
- All models, API methods, and type definitions
- Properly formatted code (via post-hooks)

### 10. Add Custom Extensions (Optional)

If you need custom functionality that won't be overwritten:

Create `custom/` directory outside the generated code:

```bash
mkdir -p custom
touch custom/__init__.py
```

Example `custom/helpers.py`:

```python
"""
Custom helper functions for Speechall SDK.
These are not generated and won't be overwritten.
"""

from speechall import Client

def create_authenticated_client(api_key: str) -> Client:
    """Helper to create a properly authenticated client."""
    return Client(
        base_url="https://api.speechall.com/v1",
        token=api_key
    )

def transcribe_file_simple(
    client: Client,
    file_path: str,
    model: str = "openai.whisper-1",
    language: str = "en"
) -> str:
    """Simple helper to transcribe a file and return text."""
    with open(file_path, "rb") as f:
        response = client.transcribe(
            model=model,
            language=language,
            output_format="text",
            file=f
        )
    return response
```

## Workflow for Updates

### When OpenAPI Spec Changes:

1. Update the OpenAPI spec in `../speechall-openapi/openapi.yaml`
2. Run regeneration:
   ```bash
   make generate
   ```
3. Review the git diff to see what changed
4. Run tests if available
5. Commit the changes
6. Bump version in `config.yml` and `pyproject.toml` if needed
7. Publish to PyPI

### Publishing to PyPI:

```bash
# Build the package
python -m build

# Upload to PyPI
python -m twine upload dist/*
```

## Configuration Customization

### config.yml Options

You can customize the generation by modifying `config.yml`:

- **`class_overrides`**: Rename specific generated classes
- **`literal_enums`**: Use Literal instead of Enum classes
- **`use_path_prefixes_for_title_model_names`**: Control model naming
- **`post_hooks`**: Add additional post-generation commands
- **`docstrings_on_attributes`**: Place docs on attributes vs class
- **`field_prefix`**: Prefix for invalid Python identifiers

Example class override:

```yaml
class_overrides:
  OpenAI_CreateTranscriptionRequest:
    class_name: OpenAITranscriptionRequest
    module_name: openai_transcription_request
```

## Troubleshooting

### Generation fails with "invalid OpenAPI spec"
- Validate the OpenAPI spec: `openapi-spec-validator ../speechall-openapi/openapi.yaml`
- Check for unsupported features

### Import errors after generation
- Make sure to install the package: `pip install -e .`
- Check dependencies in `pyproject.toml`

### Ruff formatting fails
- Install ruff: `pip install ruff`
- Or comment out post_hooks in `config.yml`

## Benefits of This Approach

✅ **Zero Manual Work**: Run one command to regenerate
✅ **Automatic Formatting**: Post-hooks handle code style
✅ **Type Safety**: Full type hints generated
✅ **Version Control**: Track changes to generated code
✅ **Easy Updates**: OpenAPI changes → regenerate → done
✅ **Customizable**: config.yml for full control
✅ **Modern Python**: Uses latest best practices
✅ **Well Documented**: Auto-generated from OpenAPI descriptions

## Next Steps

1. ✅ Set up the project structure (this plan)
2. 🔄 Run initial generation
3. 📝 Customize config.yml as needed
4. 🧪 Add tests for critical functionality
5. 📚 Enhance README with more examples
6. 🚀 Publish to PyPI
7. 🔁 Iterate: Update OpenAPI → Regenerate → Publish

## Support & Contributing

For issues, questions, or contributions, please visit the repository or contact support@speechall.com.
