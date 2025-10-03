# Speechall Python SDK Examples

This directory contains example scripts demonstrating how to use the Speechall Python SDK to transcribe audio files.

## Prerequisites

1. **Get a Speechall API Token**
   - Sign up at [https://speechall.com](https://speechall.com)
   - Generate an API token from your dashboard

2. **Set up your environment**
   - Install `uv` (recommended) or use `pip`
   - Set your API token as an environment variable

## Installation

### Using uv (Recommended)

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create a virtual environment and install the SDK in editable mode
cd examples
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install the SDK from the repo root so imports like `from speechall import Speechall` work
uv pip install -e ..
```

### Using pip

```bash
# Create a virtual environment
cd examples
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install the SDK in editable mode from the repo root
pip install -e ..
```

**Note:** These examples import the installed `speechall` package. Install the SDK in editable mode so your local changes are picked up:
- Using uv: `uv pip install -e ..`
- Using pip: `pip install -e ..`

## Setting Your API Token

Set your Speechall API token as an environment variable:

```bash
# Linux/macOS
export SPEECHALL_API_TOKEN="your-api-token-here"

# Windows (Command Prompt)
set SPEECHALL_API_TOKEN=your-api-token-here

# Windows (PowerShell)
$env:SPEECHALL_API_TOKEN="your-api-token-here"
```

Alternatively, create a `.env` file in the examples directory:

```bash
SPEECHALL_API_TOKEN=your-api-token-here
```

## Available Examples

### 1. Transcribe Local File (`transcribe_local_file.py`)

Demonstrates how to transcribe audio files from your local file system.

**Features shown:**
- Basic transcription
- Language detection
- Output format options (text, JSON, SRT, VTT)
- Speaker diarization (identifying different speakers)
- Custom vocabulary for improved accuracy

**Usage:**

```bash
# Make sure you have an audio file (e.g., audio.mp3)
# Update the audio_file_path variable in the script

python transcribe_local_file.py
```

**Example code:**

```python
from speechall import Speechall

client = Speechall(token="your-token")

with open("audio.mp3", "rb") as f:
    response = client.speech_to_text.transcribe(
        model="openai.whisper-1",
        request=f.read(),
        language="en",
        output_format="json",
    )

print(response.text)
```

### 2. Transcribe Remote File (`transcribe_remote_file.py`)

Shows how to transcribe audio files from publicly accessible URLs.

**Features shown:**
- Transcribing from URL
- Inline replacement rules
- Advanced options (temperature, prompts, etc.)
- Listing available models

**Usage:**

```bash
# The script will list available models
python transcribe_remote_file.py

# Uncomment the example functions to transcribe from URLs
```

**Example code:**

```python
from speechall import Speechall

client = Speechall(token="your-token")

response = client.speech_to_text.transcribe_remote(
    file_url="https://example.com/audio.mp3",
    model="openai.whisper-1",
    language="en",
    output_format="json",
)

print(response.text)
```

## Supported Audio Formats

The Speechall API supports common audio formats including:
- MP3
- WAV
- M4A
- FLAC
- OGG
- WEBM

## Available Models

To see all available speech-to-text models:

```python
from speechall import Speechall

client = Speechall(token="your-token")
models = client.speech_to_text.list_speech_to_text_models()

for model in models:
    print(f"{model.model_identifier}: {model.display_name}")
```

Common models include:
- `openai.whisper-1` - OpenAI's Whisper model
- And many others from various providers

## Output Formats

The API supports several output formats:

- **`text`** - Plain text transcription
- **`json`** - Detailed JSON with segments, timestamps, and metadata
- **`json_text`** - JSON with simplified text output
- **`srt`** - SubRip subtitle format
- **`vtt`** - WebVTT subtitle format

## Advanced Features

### Speaker Diarization

Identify different speakers in your audio:

```python
response = client.speech_to_text.transcribe(
    model="openai.whisper-1",
    request=audio_data,
    diarization=True,
    speakers_expected=2,  # Optional hint
)

for segment in response.segments:
    print(f"Speaker {segment.speaker}: {segment.text}")
```

### Custom Vocabulary

Improve accuracy for specific words or phrases:

```python
response = client.speech_to_text.transcribe(
    model="openai.whisper-1",
    request=audio_data,
    custom_vocabulary=["Kubernetes", "API", "Docker"],
)
```

### Language Detection

Let the model auto-detect the language:

```python
response = client.speech_to_text.transcribe(
    model="openai.whisper-1",
    request=audio_data,
    language="auto",  # Auto-detect
)

print(f"Detected language: {response.language}")
```

## Error Handling

Always wrap API calls in try-except blocks:

```python
from speechall import Speechall
from speechall.errors import (
    UnauthorizedError,
    PaymentRequiredError,
    TooManyRequestsError,
)

try:
    response = client.speech_to_text.transcribe(...)
except UnauthorizedError:
    print("Invalid API token")
except PaymentRequiredError:
    print("Insufficient credits")
except TooManyRequestsError:
    print("Rate limit exceeded")
except Exception as e:
    print(f"Error: {e}")
```

## Troubleshooting

**Issue: `SPEECHALL_API_TOKEN environment variable is required`**
- Make sure you've set the environment variable correctly
- Check that you're running the script in the same terminal session where you set the variable
- Try printing the variable: `echo $SPEECHALL_API_TOKEN` (Linux/macOS) or `echo %SPEECHALL_API_TOKEN%` (Windows)

**Issue: `Audio file not found`**
- Verify the file path is correct
- Use absolute paths if relative paths aren't working
- Make sure the file exists: `ls audio.mp3` or `dir audio.mp3`

**Issue: Import errors**
- Make sure you're in the virtual environment: `source .venv/bin/activate`
- Reinstall the package: `uv pip install -e ..` or `pip install -e ..`
- Check that you're running from the examples directory

**Issue: API errors (401, 402, 429, etc.)**
- **401 Unauthorized**: Check your API token is valid
- **402 Payment Required**: Add credits to your account
- **429 Too Many Requests**: You've hit the rate limit, wait a moment
- **500 Internal Server Error**: Contact Speechall support

## Additional Resources

- [Speechall Documentation](https://docs.speechall.com)
- [API Reference](https://docs.speechall.com/api-reference)
- [Speechall Dashboard](https://speechall.com/dashboard)

## Contributing

Found an issue or want to add more examples? Feel free to open an issue or submit a pull request!

## License

These examples are provided under the same license as the Speechall Python SDK.
