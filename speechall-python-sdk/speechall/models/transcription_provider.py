from typing import Literal, cast

TranscriptionProvider = Literal[
    "amazon",
    "assemblyai",
    "azure",
    "cloudflare",
    "deepgram",
    "elevenlabs",
    "falai",
    "fireworksai",
    "gemini",
    "gladia",
    "google",
    "groq",
    "ibm",
    "mistral",
    "openai",
    "revai",
    "speechmatics",
]

TRANSCRIPTION_PROVIDER_VALUES: set[TranscriptionProvider] = {
    "amazon",
    "assemblyai",
    "azure",
    "cloudflare",
    "deepgram",
    "elevenlabs",
    "falai",
    "fireworksai",
    "gemini",
    "gladia",
    "google",
    "groq",
    "ibm",
    "mistral",
    "openai",
    "revai",
    "speechmatics",
}


def check_transcription_provider(value: str) -> TranscriptionProvider:
    if value in TRANSCRIPTION_PROVIDER_VALUES:
        return cast(TranscriptionProvider, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRANSCRIPTION_PROVIDER_VALUES!r}")
