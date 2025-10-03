from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_ai_transcription_segment import OpenAITranscriptionSegment
    from ..models.open_ai_transcription_word import OpenAITranscriptionWord


T = TypeVar("T", bound="OpenAICreateTranscriptionResponseVerboseJson")


@_attrs_define
class OpenAICreateTranscriptionResponseVerboseJson:
    """Represents a verbose json transcription response returned by model, based on the provided input."""

    language: str
    """ The language of the input audio. """
    duration: float
    """ The duration of the input audio. """
    text: str
    """ The transcribed text. """
    words: Union[Unset, list["OpenAITranscriptionWord"]] = UNSET
    """ Extracted words and their corresponding timestamps. """
    segments: Union[Unset, list["OpenAITranscriptionSegment"]] = UNSET
    """ Segments of the transcribed text and their corresponding details. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        language = self.language

        duration = self.duration

        text = self.text

        words: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.words, Unset):
            words = []
            for words_item_data in self.words:
                words_item = words_item_data.to_dict()
                words.append(words_item)

        segments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.segments, Unset):
            segments = []
            for segments_item_data in self.segments:
                segments_item = segments_item_data.to_dict()
                segments.append(segments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "language": language,
                "duration": duration,
                "text": text,
            }
        )
        if words is not UNSET:
            field_dict["words"] = words
        if segments is not UNSET:
            field_dict["segments"] = segments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_ai_transcription_segment import OpenAITranscriptionSegment
        from ..models.open_ai_transcription_word import OpenAITranscriptionWord

        d = dict(src_dict)
        language = d.pop("language")

        duration = d.pop("duration")

        text = d.pop("text")

        words = []
        _words = d.pop("words", UNSET)
        for words_item_data in _words or []:
            words_item = OpenAITranscriptionWord.from_dict(words_item_data)

            words.append(words_item)

        segments = []
        _segments = d.pop("segments", UNSET)
        for segments_item_data in _segments or []:
            segments_item = OpenAITranscriptionSegment.from_dict(segments_item_data)

            segments.append(segments_item)

        open_ai_create_transcription_response_verbose_json = cls(
            language=language,
            duration=duration,
            text=text,
            words=words,
            segments=segments,
        )

        open_ai_create_transcription_response_verbose_json.additional_properties = d
        return open_ai_create_transcription_response_verbose_json

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
