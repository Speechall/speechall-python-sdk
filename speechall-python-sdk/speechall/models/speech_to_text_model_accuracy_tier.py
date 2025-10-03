from typing import Literal, cast

SpeechToTextModelAccuracyTier = Literal["basic", "enhanced", "premium", "standard"]

SPEECH_TO_TEXT_MODEL_ACCURACY_TIER_VALUES: set[SpeechToTextModelAccuracyTier] = {
    "basic",
    "enhanced",
    "premium",
    "standard",
}


def check_speech_to_text_model_accuracy_tier(value: str) -> SpeechToTextModelAccuracyTier:
    if value in SPEECH_TO_TEXT_MODEL_ACCURACY_TIER_VALUES:
        return cast(SpeechToTextModelAccuracyTier, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SPEECH_TO_TEXT_MODEL_ACCURACY_TIER_VALUES!r}")
