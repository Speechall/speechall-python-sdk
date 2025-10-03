from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from .. import types
from ..models.open_ai_audio_response_format import OpenAIAudioResponseFormat, check_open_ai_audio_response_format
from ..models.open_ai_create_translation_request_model_type_1 import (
    OpenAICreateTranslationRequestModelType1,
    check_open_ai_create_translation_request_model_type_1,
)
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="OpenAICreateTranslationRequest")


@_attrs_define
class OpenAICreateTranslationRequest:
    """Request schema for the OpenAI-compatible translation endpoint. Uses `multipart/form-data`. Translates audio into
    English.

    """

    file: File
    """ The audio file object (not file name) translate, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a,
    ogg, wav, or webm.
     """
    model: Union[OpenAICreateTranslationRequestModelType1, str]
    """ ID of the model to use. It follows the naming convention provider/model-name
     """
    prompt: Union[Unset, str] = UNSET
    """ An optional text to guide the model's style or continue a previous audio segment. The
    [prompt](/docs/guides/speech-to-text/prompting) should be in English.
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

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        model: str
        if isinstance(self.model, str):
            model = self.model
        else:
            model = self.model

        prompt = self.prompt

        response_format: Union[Unset, str] = UNSET
        if not isinstance(self.response_format, Unset):
            response_format = self.response_format

        temperature = self.temperature

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "file": file,
                "model": model,
            }
        )
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if response_format is not UNSET:
            field_dict["response_format"] = response_format
        if temperature is not UNSET:
            field_dict["temperature"] = temperature

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))

        if isinstance(self.model, str):
            files.append(("model", (None, str(self.model).encode(), "text/plain")))
        else:
            files.append(("model", (None, str(self.model).encode(), "text/plain")))

        if not isinstance(self.prompt, Unset):
            files.append(("prompt", (None, str(self.prompt).encode(), "text/plain")))

        if not isinstance(self.response_format, Unset):
            files.append(("response_format", (None, str(self.response_format).encode(), "text/plain")))

        if not isinstance(self.temperature, Unset):
            files.append(("temperature", (None, str(self.temperature).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        def _parse_model(data: object) -> Union[OpenAICreateTranslationRequestModelType1, str]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                model_type_1 = check_open_ai_create_translation_request_model_type_1(data)

                return model_type_1
            except:  # noqa: E722
                pass
            return cast(Union[OpenAICreateTranslationRequestModelType1, str], data)

        model = _parse_model(d.pop("model"))

        prompt = d.pop("prompt", UNSET)

        _response_format = d.pop("response_format", UNSET)
        response_format: Union[Unset, OpenAIAudioResponseFormat]
        if isinstance(_response_format, Unset):
            response_format = UNSET
        else:
            response_format = check_open_ai_audio_response_format(_response_format)

        temperature = d.pop("temperature", UNSET)

        open_ai_create_translation_request = cls(
            file=file,
            model=model,
            prompt=prompt,
            response_format=response_format,
            temperature=temperature,
        )

        return open_ai_create_translation_request
