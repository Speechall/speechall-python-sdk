from typing import Literal, cast

OpenAICreateTranslationRequestModelType1 = Literal["deepgram.whisper-large", "openai.whisper-1"]

OPEN_AI_CREATE_TRANSLATION_REQUEST_MODEL_TYPE_1_VALUES: set[OpenAICreateTranslationRequestModelType1] = {
    "deepgram.whisper-large",
    "openai.whisper-1",
}


def check_open_ai_create_translation_request_model_type_1(value: str) -> OpenAICreateTranslationRequestModelType1:
    if value in OPEN_AI_CREATE_TRANSLATION_REQUEST_MODEL_TYPE_1_VALUES:
        return cast(OpenAICreateTranslationRequestModelType1, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {OPEN_AI_CREATE_TRANSLATION_REQUEST_MODEL_TYPE_1_VALUES!r}"
    )
