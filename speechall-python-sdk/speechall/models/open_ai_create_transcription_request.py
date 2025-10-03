from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from .. import types
from ..models.open_ai_audio_response_format import OpenAIAudioResponseFormat, check_open_ai_audio_response_format
from ..models.open_ai_create_transcription_request_timestamp_granularities_item import (
    OpenAICreateTranscriptionRequestTimestampGranularitiesItem,
    check_open_ai_create_transcription_request_timestamp_granularities_item,
)
from ..models.transcription_model_identifier import TranscriptionModelIdentifier, check_transcription_model_identifier
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="OpenAICreateTranscriptionRequest")


@_attrs_define
class OpenAICreateTranscriptionRequest:
    """Request schema for the OpenAI-compatible transcription endpoint. Uses `multipart/form-data`."""

    file: File
    """ The audio file object (not file name) to transcribe, in one of these formats: flac, mp3, mp4, mpeg, mpga,
    m4a, ogg, wav, or webm.
     """
    model: TranscriptionModelIdentifier
    """ Unique identifier for a specific Speech-to-Text model, composed as `provider.model_name`. Used to select the
    engine for transcription. """
    language: Union[Unset, str] = UNSET
    """ The language of the input audio. Supplying the input language in
    [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) format will improve accuracy and latency.
     """
    prompt: Union[Unset, str] = UNSET
    """ An optional text to guide the model's style or continue a previous audio segment. The
    [prompt](/docs/guides/speech-to-text/prompting) should match the audio language.
     """
    response_format: Union[Unset, OpenAIAudioResponseFormat] = UNSET
    """ The format of the output, in one of these options: `json`, `text`, `srt`, `verbose_json`, or `vtt`.
     """
    temperature: Union[Unset, float] = 0.0
    """ The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while
    lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log
    probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until
    certain thresholds are hit.
     """
    timestamp_granularities: Union[Unset, list[OpenAICreateTranscriptionRequestTimestampGranularitiesItem]] = UNSET
    """ The timestamp granularities to populate for this transcription. `response_format` must be set `verbose_json`
    to use timestamp granularities. Either or both of these options are supported: `word`, or `segment`. Note: There
    is no additional latency for segment timestamps, but generating word timestamps incurs additional latency.
     """

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        model: str = self.model

        language = self.language

        prompt = self.prompt

        response_format: Union[Unset, str] = UNSET
        if not isinstance(self.response_format, Unset):
            response_format = self.response_format

        temperature = self.temperature

        timestamp_granularities: Union[Unset, list[str]] = UNSET
        if not isinstance(self.timestamp_granularities, Unset):
            timestamp_granularities = []
            for timestamp_granularities_item_data in self.timestamp_granularities:
                timestamp_granularities_item: str = timestamp_granularities_item_data
                timestamp_granularities.append(timestamp_granularities_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "file": file,
                "model": model,
            }
        )
        if language is not UNSET:
            field_dict["language"] = language
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if response_format is not UNSET:
            field_dict["response_format"] = response_format
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if timestamp_granularities is not UNSET:
            field_dict["timestamp_granularities[]"] = timestamp_granularities

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))

        files.append(("model", (None, str(self.model).encode(), "text/plain")))

        if not isinstance(self.language, Unset):
            files.append(("language", (None, str(self.language).encode(), "text/plain")))

        if not isinstance(self.prompt, Unset):
            files.append(("prompt", (None, str(self.prompt).encode(), "text/plain")))

        if not isinstance(self.response_format, Unset):
            files.append(("response_format", (None, str(self.response_format).encode(), "text/plain")))

        if not isinstance(self.temperature, Unset):
            files.append(("temperature", (None, str(self.temperature).encode(), "text/plain")))

        if not isinstance(self.timestamp_granularities, Unset):
            for timestamp_granularities_item_element in self.timestamp_granularities:
                files.append(
                    (
                        "timestamp_granularities[]",
                        (None, str(timestamp_granularities_item_element).encode(), "text/plain"),
                    )
                )

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        model = check_transcription_model_identifier(d.pop("model"))

        language = d.pop("language", UNSET)

        prompt = d.pop("prompt", UNSET)

        _response_format = d.pop("response_format", UNSET)
        response_format: Union[Unset, OpenAIAudioResponseFormat]
        if isinstance(_response_format, Unset):
            response_format = UNSET
        else:
            response_format = check_open_ai_audio_response_format(_response_format)

        temperature = d.pop("temperature", UNSET)

        timestamp_granularities = []
        _timestamp_granularities = d.pop("timestamp_granularities[]", UNSET)
        for timestamp_granularities_item_data in _timestamp_granularities or []:
            timestamp_granularities_item = check_open_ai_create_transcription_request_timestamp_granularities_item(
                timestamp_granularities_item_data
            )

            timestamp_granularities.append(timestamp_granularities_item)

        open_ai_create_transcription_request = cls(
            file=file,
            model=model,
            language=language,
            prompt=prompt,
            response_format=response_format,
            temperature=temperature,
            timestamp_granularities=timestamp_granularities,
        )

        return open_ai_create_transcription_request
