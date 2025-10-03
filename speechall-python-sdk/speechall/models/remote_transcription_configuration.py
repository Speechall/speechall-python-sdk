from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transcript_language_code import TranscriptLanguageCode, check_transcript_language_code
from ..models.transcript_output_format import TranscriptOutputFormat, check_transcript_output_format
from ..models.transcription_model_identifier import TranscriptionModelIdentifier, check_transcription_model_identifier
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exact_rule import ExactRule
    from ..models.regex_group_rule import RegexGroupRule
    from ..models.regex_rule import RegexRule


T = TypeVar("T", bound="RemoteTranscriptionConfiguration")


@_attrs_define
class RemoteTranscriptionConfiguration:
    """Configuration options for transcribing audio specified by a remote URL via the `/transcribe-remote` endpoint."""

    model: TranscriptionModelIdentifier
    """ Unique identifier for a specific Speech-to-Text model, composed as `provider.model_name`. Used to select the
    engine for transcription. """
    file_url: str
    """ The publicly accessible URL of the audio file to transcribe. The API server must be able to fetch the audio
    from this URL. """
    language: Union[Unset, TranscriptLanguageCode] = UNSET
    """ The language code of the audio file, typically in ISO 639-1 format.
    Specifying the correct language improves transcription accuracy and speed.
    The special value `auto` can be used to request automatic language detection, if supported by the selected
    model.
    If omitted, the default language is English (`en`).
     """
    output_format: Union[Unset, TranscriptOutputFormat] = UNSET
    """ Specifies the desired format of the transcription output.
    - `text`: Plain text containing the full transcription.
    - `json_text`: A simple JSON object containing the transcription ID and the full text (`TranscriptionOnlyText`
    schema).
    - `json`: A detailed JSON object including segments, timestamps (based on `timestamp_granularity`), language,
    and potentially speaker labels and provider metadata (`TranscriptionDetailed` schema).
    - `srt`: SubRip subtitle format (returned as plain text).
    - `vtt`: WebVTT subtitle format (returned as plain text).
     """
    ruleset_id: Union[Unset, UUID] = UNSET
    """ The unique identifier (UUID) of a pre-defined replacement ruleset to apply to the final transcription text.
    """
    punctuation: Union[Unset, bool] = True
    """ Whether to add punctuation. Support varies by model (e.g., Deepgram, AssemblyAI). Defaults to `true`. """
    diarization: Union[Unset, bool] = False
    """ Enable speaker diarization. Defaults to `false`. """
    initial_prompt: Union[Unset, str] = UNSET
    """ Optional text prompt to guide the transcription model. Support varies (e.g., OpenAI). """
    temperature: Union[Unset, float] = UNSET
    """ Controls output randomness for supported models (e.g., OpenAI). Value between 0 and 1. """
    speakers_expected: Union[Unset, int] = UNSET
    """ Hint for the number of expected speakers for diarization (e.g., RevAI, Deepgram). """
    custom_vocabulary: Union[Unset, list[str]] = UNSET
    """ List of custom words/phrases to improve recognition (e.g., Deepgram, AssemblyAI). """
    replacement_ruleset: Union[Unset, list[Union["ExactRule", "RegexGroupRule", "RegexRule"]]] = UNSET
    """ An array of replacement rules to be applied directly to this transcription request, in order. This allows
    defining rules inline instead of (or in addition to) using a pre-saved `ruleset_id`. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.exact_rule import ExactRule
        from ..models.regex_rule import RegexRule

        model: str = self.model

        file_url = self.file_url

        language: Union[Unset, str] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language

        output_format: Union[Unset, str] = UNSET
        if not isinstance(self.output_format, Unset):
            output_format = self.output_format

        ruleset_id: Union[Unset, str] = UNSET
        if not isinstance(self.ruleset_id, Unset):
            ruleset_id = str(self.ruleset_id)

        punctuation = self.punctuation

        diarization = self.diarization

        initial_prompt = self.initial_prompt

        temperature = self.temperature

        speakers_expected = self.speakers_expected

        custom_vocabulary: Union[Unset, list[str]] = UNSET
        if not isinstance(self.custom_vocabulary, Unset):
            custom_vocabulary = self.custom_vocabulary

        replacement_ruleset: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.replacement_ruleset, Unset):
            replacement_ruleset = []
            for replacement_ruleset_item_data in self.replacement_ruleset:
                replacement_ruleset_item: dict[str, Any]
                if isinstance(replacement_ruleset_item_data, ExactRule):
                    replacement_ruleset_item = replacement_ruleset_item_data.to_dict()
                elif isinstance(replacement_ruleset_item_data, RegexRule):
                    replacement_ruleset_item = replacement_ruleset_item_data.to_dict()
                else:
                    replacement_ruleset_item = replacement_ruleset_item_data.to_dict()

                replacement_ruleset.append(replacement_ruleset_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "file_url": file_url,
            }
        )
        if language is not UNSET:
            field_dict["language"] = language
        if output_format is not UNSET:
            field_dict["output_format"] = output_format
        if ruleset_id is not UNSET:
            field_dict["ruleset_id"] = ruleset_id
        if punctuation is not UNSET:
            field_dict["punctuation"] = punctuation
        if diarization is not UNSET:
            field_dict["diarization"] = diarization
        if initial_prompt is not UNSET:
            field_dict["initial_prompt"] = initial_prompt
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if speakers_expected is not UNSET:
            field_dict["speakers_expected"] = speakers_expected
        if custom_vocabulary is not UNSET:
            field_dict["custom_vocabulary"] = custom_vocabulary
        if replacement_ruleset is not UNSET:
            field_dict["replacement_ruleset"] = replacement_ruleset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exact_rule import ExactRule
        from ..models.regex_group_rule import RegexGroupRule
        from ..models.regex_rule import RegexRule

        d = dict(src_dict)
        model = check_transcription_model_identifier(d.pop("model"))

        file_url = d.pop("file_url")

        _language = d.pop("language", UNSET)
        language: Union[Unset, TranscriptLanguageCode]
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = check_transcript_language_code(_language)

        _output_format = d.pop("output_format", UNSET)
        output_format: Union[Unset, TranscriptOutputFormat]
        if isinstance(_output_format, Unset):
            output_format = UNSET
        else:
            output_format = check_transcript_output_format(_output_format)

        _ruleset_id = d.pop("ruleset_id", UNSET)
        ruleset_id: Union[Unset, UUID]
        if isinstance(_ruleset_id, Unset):
            ruleset_id = UNSET
        else:
            ruleset_id = UUID(_ruleset_id)

        punctuation = d.pop("punctuation", UNSET)

        diarization = d.pop("diarization", UNSET)

        initial_prompt = d.pop("initial_prompt", UNSET)

        temperature = d.pop("temperature", UNSET)

        speakers_expected = d.pop("speakers_expected", UNSET)

        custom_vocabulary = cast(list[str], d.pop("custom_vocabulary", UNSET))

        replacement_ruleset = []
        _replacement_ruleset = d.pop("replacement_ruleset", UNSET)
        for replacement_ruleset_item_data in _replacement_ruleset or []:

            def _parse_replacement_ruleset_item(data: object) -> Union["ExactRule", "RegexGroupRule", "RegexRule"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_replacement_rule_type_0 = ExactRule.from_dict(data)

                    return componentsschemas_replacement_rule_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_replacement_rule_type_1 = RegexRule.from_dict(data)

                    return componentsschemas_replacement_rule_type_1
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_replacement_rule_type_2 = RegexGroupRule.from_dict(data)

                return componentsschemas_replacement_rule_type_2

            replacement_ruleset_item = _parse_replacement_ruleset_item(replacement_ruleset_item_data)

            replacement_ruleset.append(replacement_ruleset_item)

        remote_transcription_configuration = cls(
            model=model,
            file_url=file_url,
            language=language,
            output_format=output_format,
            ruleset_id=ruleset_id,
            punctuation=punctuation,
            diarization=diarization,
            initial_prompt=initial_prompt,
            temperature=temperature,
            speakers_expected=speakers_expected,
            custom_vocabulary=custom_vocabulary,
            replacement_ruleset=replacement_ruleset,
        )

        remote_transcription_configuration.additional_properties = d
        return remote_transcription_configuration

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
