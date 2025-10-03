from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TranscriptionWord")


@_attrs_define
class TranscriptionWord:
    """Represents a word in the transcription, providing time-coded chunks of the transcription."""

    start: float
    """ The start time of the word in seconds from the beginning of the audio. """
    end: float
    """ The end time of the word in seconds from the beginning of the audio. """
    word: str
    """ The transcribed word. """
    speaker: Union[Unset, str] = UNSET
    """ An identifier for the speaker of this word, present if diarization was enabled and successful. """
    confidence: Union[Unset, float] = UNSET
    """ The model's confidence score for the transcription of this word, typically between 0 and 1 (if provided by
    the model). """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start = self.start

        end = self.end

        word = self.word

        speaker = self.speaker

        confidence = self.confidence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start": start,
                "end": end,
                "word": word,
            }
        )
        if speaker is not UNSET:
            field_dict["speaker"] = speaker
        if confidence is not UNSET:
            field_dict["confidence"] = confidence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start = d.pop("start")

        end = d.pop("end")

        word = d.pop("word")

        speaker = d.pop("speaker", UNSET)

        confidence = d.pop("confidence", UNSET)

        transcription_word = cls(
            start=start,
            end=end,
            word=word,
            speaker=speaker,
            confidence=confidence,
        )

        transcription_word.additional_properties = d
        return transcription_word

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
