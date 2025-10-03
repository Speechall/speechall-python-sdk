from typing import Literal, cast

TranscriptOutputFormat = Literal["json", "json_text", "srt", "text", "vtt"]

TRANSCRIPT_OUTPUT_FORMAT_VALUES: set[TranscriptOutputFormat] = {
    "json",
    "json_text",
    "srt",
    "text",
    "vtt",
}


def check_transcript_output_format(value: str) -> TranscriptOutputFormat:
    if value in TRANSCRIPT_OUTPUT_FORMAT_VALUES:
        return cast(TranscriptOutputFormat, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRANSCRIPT_OUTPUT_FORMAT_VALUES!r}")
