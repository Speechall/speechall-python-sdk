from typing import Literal, cast

SpeechToTextModelModelType = Literal[
    "command_and_search", "general", "legal", "medical", "meeting", "phone_call", "video", "voicemail"
]

SPEECH_TO_TEXT_MODEL_MODEL_TYPE_VALUES: set[SpeechToTextModelModelType] = {
    "command_and_search",
    "general",
    "legal",
    "medical",
    "meeting",
    "phone_call",
    "video",
    "voicemail",
}


def check_speech_to_text_model_model_type(value: str) -> SpeechToTextModelModelType:
    if value in SPEECH_TO_TEXT_MODEL_MODEL_TYPE_VALUES:
        return cast(SpeechToTextModelModelType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SPEECH_TO_TEXT_MODEL_MODEL_TYPE_VALUES!r}")
