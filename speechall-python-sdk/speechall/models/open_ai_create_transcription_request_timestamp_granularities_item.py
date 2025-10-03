from typing import Literal, cast

OpenAICreateTranscriptionRequestTimestampGranularitiesItem = Literal["segment", "word"]

OPEN_AI_CREATE_TRANSCRIPTION_REQUEST_TIMESTAMP_GRANULARITIES_ITEM_VALUES: set[
    OpenAICreateTranscriptionRequestTimestampGranularitiesItem
] = {
    "segment",
    "word",
}


def check_open_ai_create_transcription_request_timestamp_granularities_item(
    value: str,
) -> OpenAICreateTranscriptionRequestTimestampGranularitiesItem:
    if value in OPEN_AI_CREATE_TRANSCRIPTION_REQUEST_TIMESTAMP_GRANULARITIES_ITEM_VALUES:
        return cast(OpenAICreateTranscriptionRequestTimestampGranularitiesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {OPEN_AI_CREATE_TRANSCRIPTION_REQUEST_TIMESTAMP_GRANULARITIES_ITEM_VALUES!r}"
    )
