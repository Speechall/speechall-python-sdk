from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transcription_segment import TranscriptionSegment
    from ..models.transcription_word import TranscriptionWord


T = TypeVar("T", bound="TranscriptionDetailed")


@_attrs_define
class TranscriptionDetailed:
    """A detailed JSON response format containing the full text, detected language, duration, individual timed segments,
    and potentially speaker labels and provider-specific metadata. Returned when `output_format` is `json`.

    """

    id: str
    """ A unique identifier for the transcription job/request. """
    text: str
    """ The full transcribed text as a single string. """
    language: Union[Unset, str] = UNSET
    """ The detected or specified language of the audio (ISO 639-1 code). """
    segments: Union[Unset, list["TranscriptionSegment"]] = UNSET
    """ An array of transcribed segments, providing time-coded chunks of the transcription. May include speaker
    labels if diarization was enabled. """
    words: Union[Unset, list["TranscriptionWord"]] = UNSET
    """ An array of transcribed words, providing time-coded chunks of the transcription. May include speaker labels
    if diarization was enabled. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        text = self.text

        language = self.language

        segments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.segments, Unset):
            segments = []
            for segments_item_data in self.segments:
                segments_item = segments_item_data.to_dict()
                segments.append(segments_item)

        words: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.words, Unset):
            words = []
            for words_item_data in self.words:
                words_item = words_item_data.to_dict()
                words.append(words_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "text": text,
            }
        )
        if language is not UNSET:
            field_dict["language"] = language
        if segments is not UNSET:
            field_dict["segments"] = segments
        if words is not UNSET:
            field_dict["words"] = words

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transcription_segment import TranscriptionSegment
        from ..models.transcription_word import TranscriptionWord

        d = dict(src_dict)
        id = d.pop("id")

        text = d.pop("text")

        language = d.pop("language", UNSET)

        segments = []
        _segments = d.pop("segments", UNSET)
        for segments_item_data in _segments or []:
            segments_item = TranscriptionSegment.from_dict(segments_item_data)

            segments.append(segments_item)

        words = []
        _words = d.pop("words", UNSET)
        for words_item_data in _words or []:
            words_item = TranscriptionWord.from_dict(words_item_data)

            words.append(words_item)

        transcription_detailed = cls(
            id=id,
            text=text,
            language=language,
            segments=segments,
            words=words,
        )

        transcription_detailed.additional_properties = d
        return transcription_detailed

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
