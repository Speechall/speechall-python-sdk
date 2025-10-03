from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OpenAITranscriptionSegment")


@_attrs_define
class OpenAITranscriptionSegment:
    """Represents a segment of transcribed or translated text, based on OpenAI's verbose JSON structure."""

    id: int
    """ Unique identifier of the segment. """
    seek: int
    """ Seek offset of the segment. """
    start: float
    """ Start time of the segment in seconds. """
    end: float
    """ End time of the segment in seconds. """
    text: str
    """ Text content of the segment. """
    tokens: list[int]
    """ Array of token IDs for the text content. """
    temperature: float
    """ Temperature parameter used for generating the segment. """
    avg_logprob: float
    """ Average logprob of the segment. If the value is lower than -1, consider the logprobs failed. """
    compression_ratio: float
    """ Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed. """
    no_speech_prob: float
    """ Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1,
    consider this segment silent. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        seek = self.seek

        start = self.start

        end = self.end

        text = self.text

        tokens = self.tokens

        temperature = self.temperature

        avg_logprob = self.avg_logprob

        compression_ratio = self.compression_ratio

        no_speech_prob = self.no_speech_prob

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "seek": seek,
                "start": start,
                "end": end,
                "text": text,
                "tokens": tokens,
                "temperature": temperature,
                "avg_logprob": avg_logprob,
                "compression_ratio": compression_ratio,
                "no_speech_prob": no_speech_prob,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        seek = d.pop("seek")

        start = d.pop("start")

        end = d.pop("end")

        text = d.pop("text")

        tokens = cast(list[int], d.pop("tokens"))

        temperature = d.pop("temperature")

        avg_logprob = d.pop("avg_logprob")

        compression_ratio = d.pop("compression_ratio")

        no_speech_prob = d.pop("no_speech_prob")

        open_ai_transcription_segment = cls(
            id=id,
            seek=seek,
            start=start,
            end=end,
            text=text,
            tokens=tokens,
            temperature=temperature,
            avg_logprob=avg_logprob,
            compression_ratio=compression_ratio,
            no_speech_prob=no_speech_prob,
        )

        open_ai_transcription_segment.additional_properties = d
        return open_ai_transcription_segment

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
