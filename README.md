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
