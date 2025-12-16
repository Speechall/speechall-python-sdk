## Code Generation

This SDK is auto-generated using **Fern** from an OpenAPI specification.

### Key Files
- **OpenAPI Spec**: `../speechall-openapi/openapi.yaml` (external repo)
- **Generator Config**: `fern/generators.yml` (Fern Python SDK v4.30.3)
- **Protected Files**: `.fernignore` (files NOT overwritten during generation)
- **Regeneration Script**: `regenerate.sh`

### What Gets Generated
- **All files in `src/`** (55 Python files)
  - API clients (`client.py`, `raw_client.py`)
  - Data types (`types/`)
  - Error classes (`errors/`)
  - Core utilities (`core/`)

### What's Protected (in .fernignore)
- All markdown files (`*.md`)
- Examples (`examples/`)
- Configuration (`pyproject.toml`, `.gitignore`)
- IDE settings (`.vscode/`, `.idea/`, `.claude/`)

### Regenerating Code
```bash
./regenerate.sh
```

This runs `fern generate --local --force` and optionally runs tests.

### Filtering Endpoints from Generation
Some endpoints are excluded from SDK generation using **`x-fern-ignore: true`** in the OpenAPI spec:
- `/openai-compatible/audio/transcriptions`
- `/openai-compatible/audio/translations`

These endpoints remain in the API spec for documentation but don't generate SDK code. To exclude an endpoint, add to its definition:
```yaml
x-internal: true      # Marks as internal (optional)
x-fern-ignore: true   # Excludes from SDK generation
```

### Important Rules
- ❌ **NEVER manually edit files in `src/`** - they will be overwritten
- ✅ API changes must be made in the OpenAPI specification
- ✅ To exclude endpoints from generation, use `x-fern-ignore: true` in the OpenAPI spec
- ✅ After updating the OpenAPI spec, run `./regenerate.sh`
- ✅ Manual code changes only in protected files (examples, docs, config)


@AGENTS.md
