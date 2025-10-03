"""
Example: Transcribe a remote audio file using the Speechall API

This example demonstrates how to transcribe an audio file from a publicly
accessible URL using the Speechall Python SDK.

Requirements:
- Set SPEECHALL_API_TOKEN environment variable with your API token
- Have a publicly accessible audio file URL
"""

import os

from speechall import Speechall, ReplacementRule, ExactRule


def transcribe_remote_file():
    """Transcribe an audio file from a URL"""
    
    # Initialize the client with your API token
    api_token = os.getenv("SPEECHALL_API_TOKEN")
    if not api_token:
        raise ValueError(
            "SPEECHALL_API_TOKEN environment variable is required. "
            "Get your token from https://speechall.com"
        )
    
    client = Speechall(token=api_token)
    
    # URL to your audio file
    # The file must be publicly accessible
    audio_url = "https://example.com/path/to/audio.mp3"
    
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
    
    client = Speechall(token=api_token)
    
    audio_url = "https://example.com/audio.mp3"
    
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
    
    client = Speechall(token=api_token)
    
    audio_url = "https://example.com/meeting.mp3"
    
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
        print(f"\nShowing first 5 segments:")
        for i, segment in enumerate(response.segments[:5], 1):
            speaker = getattr(segment, 'speaker', 'Unknown')
            print(f"{i}. [Speaker {speaker}] [{segment.start:.2f}s] {segment.text}")


def list_available_models():
    """List all available speech-to-text models"""
    
    api_token = os.getenv("SPEECHALL_API_TOKEN")
    if not api_token:
        raise ValueError("SPEECHALL_API_TOKEN environment variable is required")
    
    client = Speechall(token=api_token)
    
    print("\n=== Available Speech-to-Text Models ===\n")
    
    models = client.speech_to_text.list_speech_to_text_models()
    
    for model in models:
        print(f"Model: {model.model_identifier}")
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
        list_available_models()
        
        # Basic remote transcription
        # Note: Update the audio_url in the function with a real URL
        # transcribe_remote_file()
        
        # Advanced examples (uncomment to try)
        # transcribe_remote_with_replacement_rules()
        # transcribe_with_multiple_options()
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
