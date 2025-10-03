"""
Example: Transcribe a local audio file using the Speechall API

This example demonstrates how to transcribe a local audio file using the
Speechall Python SDK. It shows various options including language detection,
output formats, and optional features like diarization and punctuation.

Requirements:
- Set SPEECHALL_API_TOKEN environment variable with your API token
- Have an audio file to transcribe (e.g., audio.mp3, audio.wav)
"""

import os
from pathlib import Path

from speechall import Speechall


def transcribe_local_file():
    """Transcribe a local audio file"""
    
    # Initialize the client with your API token
    # You can get your token from https://speechall.com
    api_token = os.getenv("SPEECHALL_API_TOKEN")
    if not api_token:
        raise ValueError(
            "SPEECHALL_API_TOKEN environment variable is required. "
            "Get your token from https://speechall.com"
        )
    
    client = Speechall(token=api_token)
    
    # Path to your audio file
    audio_file_path = "audio.mp3"  # Replace with your audio file path
    
    if not Path(audio_file_path).exists():
        print(f"Error: Audio file not found at {audio_file_path}")
        print("Please update the audio_file_path variable with the path to your audio file.")
        return
    
    # Read the audio file
    with open(audio_file_path, "rb") as audio_file:
        audio_data = audio_file.read()
    
    print(f"Transcribing {audio_file_path}...")
    print("This may take a moment depending on the audio length...\n")
    
    # Transcribe the audio file
    # Using OpenAI's Whisper model as an example
    response = client.speech_to_text.transcribe(
        model="openai.whisper-1",  # Model identifier in format "provider.model"
        request=audio_data,
        language="en",  # Language code (ISO 639-1) or "auto" for detection
        output_format="json",  # Options: "text", "json", "json_text", "srt", "vtt"
        punctuation=True,  # Enable automatic punctuation
        diarization=False,  # Enable speaker diarization (identifies different speakers)
    )
    
    # Display the transcription result
    print("=== Transcription Result ===")
    print(f"Text: {response.text}\n")
    
    # If using JSON format, you can access detailed information
    if hasattr(response, 'language'):
        print(f"Detected Language: {response.language}")
    
    if hasattr(response, 'duration'):
        print(f"Duration: {response.duration} seconds")
    
    if hasattr(response, 'segments') and response.segments:
        print(f"\n=== Segments ({len(response.segments)} total) ===")
        for i, segment in enumerate(response.segments[:3], 1):  # Show first 3 segments
            print(f"{i}. [{segment.start:.2f}s - {segment.end:.2f}s] {segment.text}")
        if len(response.segments) > 3:
            print(f"... and {len(response.segments) - 3} more segments")


def transcribe_with_diarization():
    """Example: Transcribe with speaker diarization enabled"""
    
    api_token = os.getenv("SPEECHALL_API_TOKEN")
    if not api_token:
        raise ValueError("SPEECHALL_API_TOKEN environment variable is required")
    
    client = Speechall(token=api_token)
    
    audio_file_path = "conversation.mp3"  # Audio with multiple speakers
    
    if not Path(audio_file_path).exists():
        print(f"Skipping diarization example - audio file not found: {audio_file_path}")
        return
    
    with open(audio_file_path, "rb") as audio_file:
        audio_data = audio_file.read()
    
    print("\n=== Transcription with Speaker Diarization ===")
    print("Identifying different speakers in the audio...\n")
    
    response = client.speech_to_text.transcribe(
        model="openai.whisper-1",
        request=audio_data,
        language="en",
        output_format="json",
        diarization=True,  # Enable speaker identification
        speakers_expected=2,  # Optional: hint about number of speakers
    )
    
    print("=== Transcription with Speakers ===")
    if hasattr(response, 'segments') and response.segments:
        for segment in response.segments:
            speaker = getattr(segment, 'speaker', 'Unknown')
            print(f"[Speaker {speaker}] {segment.text}")


def transcribe_with_custom_vocabulary():
    """Example: Transcribe with custom vocabulary for better accuracy"""
    
    api_token = os.getenv("SPEECHALL_API_TOKEN")
    if not api_token:
        raise ValueError("SPEECHALL_API_TOKEN environment variable is required")
    
    client = Speechall(token=api_token)
    
    audio_file_path = "technical_talk.mp3"
    
    if not Path(audio_file_path).exists():
        print(f"Skipping custom vocabulary example - audio file not found: {audio_file_path}")
        return
    
    with open(audio_file_path, "rb") as audio_file:
        audio_data = audio_file.read()
    
    print("\n=== Transcription with Custom Vocabulary ===")
    
    # Add specific words/phrases to improve recognition
    # Useful for proper nouns, technical jargon, etc.
    response = client.speech_to_text.transcribe(
        model="openai.whisper-1",
        request=audio_data,
        language="en",
        output_format="json",
        custom_vocabulary=["Kubernetes", "API", "Docker", "microservices"],
    )
    
    print(f"Result: {response.text}")


if __name__ == "__main__":
    try:
        # Basic transcription example
        transcribe_local_file()
        
        # Additional examples (uncomment to try)
        # transcribe_with_diarization()
        # transcribe_with_custom_vocabulary()
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
