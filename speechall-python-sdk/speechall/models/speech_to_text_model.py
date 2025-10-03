import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.speech_to_text_model_accuracy_tier import (
    SpeechToTextModelAccuracyTier,
    check_speech_to_text_model_accuracy_tier,
)
from ..models.speech_to_text_model_model_type import SpeechToTextModelModelType, check_speech_to_text_model_model_type
from ..models.transcription_model_identifier import TranscriptionModelIdentifier, check_transcription_model_identifier
from ..models.transcription_provider import TranscriptionProvider, check_transcription_provider
from ..types import UNSET, Unset

T = TypeVar("T", bound="SpeechToTextModel")


@_attrs_define
class SpeechToTextModel:
    """Describes an available speech-to-text model, its provider, capabilities, and characteristics."""

    id: TranscriptionModelIdentifier
    """ Unique identifier for a specific Speech-to-Text model, composed as `provider.model_name`. Used to select the
    engine for transcription. """
    display_name: str
    """ A user-friendly name for the model. """
    provider: TranscriptionProvider
    """ The identifier for the underlying Speech-to-Text service provider (e.g., 'openai', 'deepgram'). """
    is_available: bool = True
    """ Indicates whether the model is currently available for use. """
    supports_srt: bool = False
    """ Indicates whether the model supports SRT subtitle format output. """
    supports_vtt: bool = False
    """ Indicates whether the model supports VTT subtitle format output. """
    description: Union[None, Unset, str] = UNSET
    """ A brief description of the model, its intended use case, or version notes. """
    cost_per_second_usd: Union[None, Unset, float] = UNSET
    """ The cost per second of audio processed in USD. """
    supported_languages: Union[None, Unset, list[str]] = UNSET
    """ A list of language codes (preferably BCP 47, e.g., "en-US", "en-GB", "es-ES") supported by this model. May
    include `auto` if automatic language detection is supported across multiple languages within a single audio
    file.
     """
    punctuation: Union[None, Unset, bool] = UNSET
    """ Indicates whether the model generally supports automatic punctuation insertion. """
    diarization: Union[None, Unset, bool] = UNSET
    """ Indicates whether the model generally supports speaker diarization (identifying different speakers). """
    streamable: Union[None, Unset, bool] = UNSET
    """ Indicates whether the model can be used for real-time streaming transcription via a WebSocket connection (if
    offered by Speechall). """
    real_time_factor: Union[None, Unset, float] = UNSET
    """ An approximate measure of processing speed for batch processing. Defined as (audio duration) / (processing
    time). A higher value means faster processing (e.g., RTF=2 means it processes 1 second of audio in 0.5 seconds).
    May not be available for all models or streaming scenarios.
     """
    max_duration_seconds: Union[None, Unset, float] = UNSET
    """ The maximum duration of a single audio file (in seconds) that the model can reliably process in one request.
    May vary by provider or plan. """
    max_file_size_bytes: Union[None, Unset, int] = UNSET
    """ The maximum size of a single audio file (in bytes) that can be uploaded for processing by this model. May
    vary by provider or plan. """
    version: Union[None, Unset, str] = UNSET
    """ The specific version identifier for the model. """
    release_date: Union[None, Unset, datetime.date] = UNSET
    """ The date when this specific version of the model was released or last updated. """
    model_type: Union[Unset, SpeechToTextModelModelType] = UNSET
    """ The primary type or training domain of the model. Helps identify suitability for different audio types. """
    accuracy_tier: Union[Unset, SpeechToTextModelAccuracyTier] = UNSET
    """ A general indication of the model's expected accuracy level relative to other models. Not a guaranteed
    metric. """
    supported_audio_encodings: Union[None, Unset, list[str]] = UNSET
    """ A list of audio encodings that this model supports or is optimized for (e.g., LINEAR16, FLAC, MP3, Opus).
    """
    supported_sample_rates: Union[None, Unset, list[int]] = UNSET
    """ A list of audio sample rates (in Hz) that this model supports or is optimized for. """
    speaker_labels: Union[None, Unset, bool] = UNSET
    """ Indicates whether the model can provide speaker labels for the transcription. """
    word_timestamps: Union[None, Unset, bool] = UNSET
    """ Indicates whether the model can provide timestamps for individual words. """
    confidence_scores: Union[None, Unset, bool] = UNSET
    """ Indicates whether the model provides confidence scores for the transcription or individual words. """
    language_detection: Union[None, Unset, bool] = UNSET
    """ Indicates whether the model supports automatic language detection for input audio. """
    custom_vocabulary_support: Union[None, Unset, bool] = UNSET
    """ Indicates if the model can leverage a custom vocabulary or language model adaptation. """
    profanity_filtering: Union[None, Unset, bool] = UNSET
    """ Indicates if the model supports filtering or masking of profanity. """
    noise_reduction: Union[None, Unset, bool] = UNSET
    """ Indicates if the model supports noise reduction. """
    voice_activity_detection: Union[None, Unset, bool] = UNSET
    """ Indicates whether the model supports voice activity detection (VAD) to identify speech segments. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str = self.id

        display_name = self.display_name

        provider: str = self.provider

        is_available = self.is_available

        supports_srt = self.supports_srt

        supports_vtt = self.supports_vtt

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        cost_per_second_usd: Union[None, Unset, float]
        if isinstance(self.cost_per_second_usd, Unset):
            cost_per_second_usd = UNSET
        else:
            cost_per_second_usd = self.cost_per_second_usd

        supported_languages: Union[None, Unset, list[str]]
        if isinstance(self.supported_languages, Unset):
            supported_languages = UNSET
        elif isinstance(self.supported_languages, list):
            supported_languages = self.supported_languages

        else:
            supported_languages = self.supported_languages

        punctuation: Union[None, Unset, bool]
        if isinstance(self.punctuation, Unset):
            punctuation = UNSET
        else:
            punctuation = self.punctuation

        diarization: Union[None, Unset, bool]
        if isinstance(self.diarization, Unset):
            diarization = UNSET
        else:
            diarization = self.diarization

        streamable: Union[None, Unset, bool]
        if isinstance(self.streamable, Unset):
            streamable = UNSET
        else:
            streamable = self.streamable

        real_time_factor: Union[None, Unset, float]
        if isinstance(self.real_time_factor, Unset):
            real_time_factor = UNSET
        else:
            real_time_factor = self.real_time_factor

        max_duration_seconds: Union[None, Unset, float]
        if isinstance(self.max_duration_seconds, Unset):
            max_duration_seconds = UNSET
        else:
            max_duration_seconds = self.max_duration_seconds

        max_file_size_bytes: Union[None, Unset, int]
        if isinstance(self.max_file_size_bytes, Unset):
            max_file_size_bytes = UNSET
        else:
            max_file_size_bytes = self.max_file_size_bytes

        version: Union[None, Unset, str]
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        release_date: Union[None, Unset, str]
        if isinstance(self.release_date, Unset):
            release_date = UNSET
        elif isinstance(self.release_date, datetime.date):
            release_date = self.release_date.isoformat()
        else:
            release_date = self.release_date

        model_type: Union[Unset, str] = UNSET
        if not isinstance(self.model_type, Unset):
            model_type = self.model_type

        accuracy_tier: Union[Unset, str] = UNSET
        if not isinstance(self.accuracy_tier, Unset):
            accuracy_tier = self.accuracy_tier

        supported_audio_encodings: Union[None, Unset, list[str]]
        if isinstance(self.supported_audio_encodings, Unset):
            supported_audio_encodings = UNSET
        elif isinstance(self.supported_audio_encodings, list):
            supported_audio_encodings = self.supported_audio_encodings

        else:
            supported_audio_encodings = self.supported_audio_encodings

        supported_sample_rates: Union[None, Unset, list[int]]
        if isinstance(self.supported_sample_rates, Unset):
            supported_sample_rates = UNSET
        elif isinstance(self.supported_sample_rates, list):
            supported_sample_rates = self.supported_sample_rates

        else:
            supported_sample_rates = self.supported_sample_rates

        speaker_labels: Union[None, Unset, bool]
        if isinstance(self.speaker_labels, Unset):
            speaker_labels = UNSET
        else:
            speaker_labels = self.speaker_labels

        word_timestamps: Union[None, Unset, bool]
        if isinstance(self.word_timestamps, Unset):
            word_timestamps = UNSET
        else:
            word_timestamps = self.word_timestamps

        confidence_scores: Union[None, Unset, bool]
        if isinstance(self.confidence_scores, Unset):
            confidence_scores = UNSET
        else:
            confidence_scores = self.confidence_scores

        language_detection: Union[None, Unset, bool]
        if isinstance(self.language_detection, Unset):
            language_detection = UNSET
        else:
            language_detection = self.language_detection

        custom_vocabulary_support: Union[None, Unset, bool]
        if isinstance(self.custom_vocabulary_support, Unset):
            custom_vocabulary_support = UNSET
        else:
            custom_vocabulary_support = self.custom_vocabulary_support

        profanity_filtering: Union[None, Unset, bool]
        if isinstance(self.profanity_filtering, Unset):
            profanity_filtering = UNSET
        else:
            profanity_filtering = self.profanity_filtering

        noise_reduction: Union[None, Unset, bool]
        if isinstance(self.noise_reduction, Unset):
            noise_reduction = UNSET
        else:
            noise_reduction = self.noise_reduction

        voice_activity_detection: Union[None, Unset, bool]
        if isinstance(self.voice_activity_detection, Unset):
            voice_activity_detection = UNSET
        else:
            voice_activity_detection = self.voice_activity_detection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "display_name": display_name,
                "provider": provider,
                "is_available": is_available,
                "supports_srt": supports_srt,
                "supports_vtt": supports_vtt,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if cost_per_second_usd is not UNSET:
            field_dict["cost_per_second_usd"] = cost_per_second_usd
        if supported_languages is not UNSET:
            field_dict["supported_languages"] = supported_languages
        if punctuation is not UNSET:
            field_dict["punctuation"] = punctuation
        if diarization is not UNSET:
            field_dict["diarization"] = diarization
        if streamable is not UNSET:
            field_dict["streamable"] = streamable
        if real_time_factor is not UNSET:
            field_dict["real_time_factor"] = real_time_factor
        if max_duration_seconds is not UNSET:
            field_dict["max_duration_seconds"] = max_duration_seconds
        if max_file_size_bytes is not UNSET:
            field_dict["max_file_size_bytes"] = max_file_size_bytes
        if version is not UNSET:
            field_dict["version"] = version
        if release_date is not UNSET:
            field_dict["release_date"] = release_date
        if model_type is not UNSET:
            field_dict["model_type"] = model_type
        if accuracy_tier is not UNSET:
            field_dict["accuracy_tier"] = accuracy_tier
        if supported_audio_encodings is not UNSET:
            field_dict["supported_audio_encodings"] = supported_audio_encodings
        if supported_sample_rates is not UNSET:
            field_dict["supported_sample_rates"] = supported_sample_rates
        if speaker_labels is not UNSET:
            field_dict["speaker_labels"] = speaker_labels
        if word_timestamps is not UNSET:
            field_dict["word_timestamps"] = word_timestamps
        if confidence_scores is not UNSET:
            field_dict["confidence_scores"] = confidence_scores
        if language_detection is not UNSET:
            field_dict["language_detection"] = language_detection
        if custom_vocabulary_support is not UNSET:
            field_dict["custom_vocabulary_support"] = custom_vocabulary_support
        if profanity_filtering is not UNSET:
            field_dict["profanity_filtering"] = profanity_filtering
        if noise_reduction is not UNSET:
            field_dict["noise_reduction"] = noise_reduction
        if voice_activity_detection is not UNSET:
            field_dict["voice_activity_detection"] = voice_activity_detection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = check_transcription_model_identifier(d.pop("id"))

        display_name = d.pop("display_name")

        provider = check_transcription_provider(d.pop("provider"))

        is_available = d.pop("is_available")

        supports_srt = d.pop("supports_srt")

        supports_vtt = d.pop("supports_vtt")

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_cost_per_second_usd(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        cost_per_second_usd = _parse_cost_per_second_usd(d.pop("cost_per_second_usd", UNSET))

        def _parse_supported_languages(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                supported_languages_type_0 = cast(list[str], data)

                return supported_languages_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        supported_languages = _parse_supported_languages(d.pop("supported_languages", UNSET))

        def _parse_punctuation(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        punctuation = _parse_punctuation(d.pop("punctuation", UNSET))

        def _parse_diarization(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        diarization = _parse_diarization(d.pop("diarization", UNSET))

        def _parse_streamable(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        streamable = _parse_streamable(d.pop("streamable", UNSET))

        def _parse_real_time_factor(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        real_time_factor = _parse_real_time_factor(d.pop("real_time_factor", UNSET))

        def _parse_max_duration_seconds(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        max_duration_seconds = _parse_max_duration_seconds(d.pop("max_duration_seconds", UNSET))

        def _parse_max_file_size_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_file_size_bytes = _parse_max_file_size_bytes(d.pop("max_file_size_bytes", UNSET))

        def _parse_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_release_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                release_date_type_0 = isoparse(data).date()

                return release_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        release_date = _parse_release_date(d.pop("release_date", UNSET))

        _model_type = d.pop("model_type", UNSET)
        model_type: Union[Unset, SpeechToTextModelModelType]
        if isinstance(_model_type, Unset):
            model_type = UNSET
        else:
            model_type = check_speech_to_text_model_model_type(_model_type)

        _accuracy_tier = d.pop("accuracy_tier", UNSET)
        accuracy_tier: Union[Unset, SpeechToTextModelAccuracyTier]
        if isinstance(_accuracy_tier, Unset):
            accuracy_tier = UNSET
        else:
            accuracy_tier = check_speech_to_text_model_accuracy_tier(_accuracy_tier)

        def _parse_supported_audio_encodings(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                supported_audio_encodings_type_0 = cast(list[str], data)

                return supported_audio_encodings_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        supported_audio_encodings = _parse_supported_audio_encodings(d.pop("supported_audio_encodings", UNSET))

        def _parse_supported_sample_rates(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                supported_sample_rates_type_0 = cast(list[int], data)

                return supported_sample_rates_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        supported_sample_rates = _parse_supported_sample_rates(d.pop("supported_sample_rates", UNSET))

        def _parse_speaker_labels(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        speaker_labels = _parse_speaker_labels(d.pop("speaker_labels", UNSET))

        def _parse_word_timestamps(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        word_timestamps = _parse_word_timestamps(d.pop("word_timestamps", UNSET))

        def _parse_confidence_scores(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        confidence_scores = _parse_confidence_scores(d.pop("confidence_scores", UNSET))

        def _parse_language_detection(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        language_detection = _parse_language_detection(d.pop("language_detection", UNSET))

        def _parse_custom_vocabulary_support(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        custom_vocabulary_support = _parse_custom_vocabulary_support(d.pop("custom_vocabulary_support", UNSET))

        def _parse_profanity_filtering(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        profanity_filtering = _parse_profanity_filtering(d.pop("profanity_filtering", UNSET))

        def _parse_noise_reduction(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        noise_reduction = _parse_noise_reduction(d.pop("noise_reduction", UNSET))

        def _parse_voice_activity_detection(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        voice_activity_detection = _parse_voice_activity_detection(d.pop("voice_activity_detection", UNSET))

        speech_to_text_model = cls(
            id=id,
            display_name=display_name,
            provider=provider,
            is_available=is_available,
            supports_srt=supports_srt,
            supports_vtt=supports_vtt,
            description=description,
            cost_per_second_usd=cost_per_second_usd,
            supported_languages=supported_languages,
            punctuation=punctuation,
            diarization=diarization,
            streamable=streamable,
            real_time_factor=real_time_factor,
            max_duration_seconds=max_duration_seconds,
            max_file_size_bytes=max_file_size_bytes,
            version=version,
            release_date=release_date,
            model_type=model_type,
            accuracy_tier=accuracy_tier,
            supported_audio_encodings=supported_audio_encodings,
            supported_sample_rates=supported_sample_rates,
            speaker_labels=speaker_labels,
            word_timestamps=word_timestamps,
            confidence_scores=confidence_scores,
            language_detection=language_detection,
            custom_vocabulary_support=custom_vocabulary_support,
            profanity_filtering=profanity_filtering,
            noise_reduction=noise_reduction,
            voice_activity_detection=voice_activity_detection,
        )

        speech_to_text_model.additional_properties = d
        return speech_to_text_model

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
