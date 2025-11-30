"""
Example: Transcribe a remote audio file using the Speechall API

This example demonstrates how to transcribe an audio file from a publicly
accessible URL using the Speechall Python SDK.

Requirements:
- Set SPEECHALL_API_TOKEN environment variable with your API token
- Have a publicly accessible audio file URL
"""

import os

from speechall import SpeechallApi, ReplacementRule, ExactRule
REMOTE_AUDIO_URL="https://storage.googleapis.com/kagglesdsdata/datasets/829978/1417968/harvard.wav?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20251127%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20251127T162539Z&X-Goog-Expires=345600&X-Goog-SignedHeaders=host&X-Goog-Signature=2413690e9eae7f5f19021283c74105971863b79f3147e1a2e268ba696d8ff93e227e9d30931b55a3f84564de6e0f8c870333b8e9021a7fa4689eb3dcb8b8fabe188f8cf57f56124809dd1a78190988800ee88135e06a879ca0a1afdb6e08000c2b0b4cb9f20fffe57e1820d5392f3613624a582124405101d89bb689ff714cebbdd6b6c4c671464d7422aa5c67059f64c2d7c556b4a5ac3a893d2f132e4e09d6d78bbb89815ef3c3acfa958eae709bc40d21b01960f057032de4e4a894353e26ec37788a2a7b71f6948c296dd0ad14dab84376ce92bc742e39a54a16f80c7f2fa3d45b91a4af201d07970b536bc19439fcc8f46f37d6dfa36eb28f7554c819c5"

def transcribe_remote_file():
    """Transcribe an audio file from a URL"""

    # Initialize the client with your API token
    api_token = os.getenv("SPEECHALL_API_TOKEN")
    if not api_token:
        raise ValueError(
            "SPEECHALL_API_TOKEN environment variable is required. "
            "Get your token from https://speechall.com"
        )

    client = SpeechallApi(token=api_token)

    # URL to your audio file
    # The file must be publicly accessible
    audio_url = REMOTE_AUDIO_URL

    print(f"Transcribing audio from URL: {audio_url}")
    print("This may take a moment...\n")

    # Transcribe the remote audio file
    response = client.speech_to_text.transcribe_remote(
        file_url=audio_url,
        model="openai.whisper-1",  # Model identifier
        language="en",  # Language code or "auto" for detection
        output_format="json",  # Options: "text", "json", "json_text", "srt", "vtt"
        punctuation=True,
        diarization=False,
    )

    # Display the transcription result
    print("=== Transcription Result ===")
    print(f"Text: {response.text}\n")

    # Access additional details if available
    if hasattr(response, 'language'):
        print(f"Language: {response.language}")

    if hasattr(response, 'duration'):
        print(f"Duration: {response.duration} seconds")

    if hasattr(response, 'segments') and response.segments:
        print(f"\nTotal segments: {len(response.segments)}")


def transcribe_remote_with_replacement_rules():
    """Example: Transcribe with inline replacement rules"""

    api_token = os.getenv("SPEECHALL_API_TOKEN")
    if not api_token:
        raise ValueError("SPEECHALL_API_TOKEN environment variable is required")

    client = SpeechallApi(token=api_token)

    audio_url = REMOTE_AUDIO_URL

    print("\n=== Transcription with Replacement Rules ===")
    print("Applying custom text replacements to the transcription...\n")

    # Define replacement rules to apply to the transcription
    # These rules will modify the final transcription text

    replacement_rules = [
        # Example: Replace "API" with "Application Programming Interface"
        ReplacementRule(
            rule=ExactRule(find="API", replace="Application Programming Interface")
        ),
    ]

    response = client.speech_to_text.transcribe_remote(
        file_url=audio_url,
        model="openai.whisper-1",
        language="en",
        output_format="json",
        replacement_ruleset=replacement_rules,  # Apply inline rules
    )

    print(f"Transcription with replacements: {response.text}")


def transcribe_with_multiple_options():
    """Example: Transcribe with various advanced options"""

    api_token = os.getenv("SPEECHALL_API_TOKEN")
    if not api_token:
        raise ValueError("SPEECHALL_API_TOKEN environment variable is required")

    client = SpeechallApi(token=api_token)

    audio_url = REMOTE_AUDIO_URL

    print("\n=== Advanced Transcription Options ===")

    response = client.speech_to_text.transcribe_remote(
        file_url=audio_url,
        model="openai.whisper-1",
        language="auto",  # Auto-detect language
        output_format="json",
        punctuation=True,
        diarization=True,  # Identify speakers
        speakers_expected=3,  # Hint: expecting 3 speakers
        initial_prompt="This is a technical discussion about cloud computing.",
        temperature=0.2,  # Lower temperature for more deterministic output
        custom_vocabulary=["AWS", "Azure", "Kubernetes", "DevOps"],
    )

    print("=== Detailed Transcription ===")
    print(f"Full text: {response.text[:200]}...")  # First 200 chars

    if hasattr(response, 'segments') and response.segments:
        print("\nShowing first 5 segments:")
        for i, segment in enumerate(response.segments[:5], 1):
            speaker = getattr(segment, 'speaker', 'Unknown')
            print(f"{i}. [Speaker {speaker}] [{segment.start:.2f}s] {segment.text}")


def list_available_models():
    """List all available speech-to-text models"""

    api_token = os.getenv("SPEECHALL_API_TOKEN")
    if not api_token:
        raise ValueError("SPEECHALL_API_TOKEN environment variable is required")

    client = SpeechallApi(token=api_token)

    print("\n=== Available Speech-to-Text Models ===\n")

    models = client.speech_to_text.list_speech_to_text_models()

    for model in models:
        print(f"Model: {model.id}")
        print(f"  Name: {model.display_name}")
        print(f"  Provider: {model.provider}")
        if hasattr(model, 'description') and model.description:
            print(f"  Description: {model.description}")
        if hasattr(model, 'supported_languages') and model.supported_languages:
            print(f"  Languages: {', '.join(model.supported_languages[:5])}...")
        print()


if __name__ == "__main__":
    try:
        # List available models first
        # list_available_models()

        # Basic remote transcription
        # Note: Update the audio_url in the function with a real URL
        # transcribe_remote_file()

        # Advanced examples (uncomment to try)
        transcribe_remote_with_replacement_rules()
        # transcribe_with_multiple_options()

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
