from typing import Literal, cast

OpenAIAudioResponseFormat = Literal["json", "srt", "text", "verbose_json", "vtt"]

OPEN_AI_AUDIO_RESPONSE_FORMAT_VALUES: set[OpenAIAudioResponseFormat] = {
    "json",
    "srt",
    "text",
    "verbose_json",
    "vtt",
}


def check_open_ai_audio_response_format(value: str) -> OpenAIAudioResponseFormat:
    if value in OPEN_AI_AUDIO_RESPONSE_FORMAT_VALUES:
        return cast(OpenAIAudioResponseFormat, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OPEN_AI_AUDIO_RESPONSE_FORMAT_VALUES!r}")
