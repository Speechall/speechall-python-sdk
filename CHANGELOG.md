# Changelog

## [1.0.0] - 2026-10-04

### Added

- Smallest AI Pulse and Pulse Pro, Soniox STT Async v5, and Together AI Thinking Machines Inkling and Inkling Small transcription models.
- `smallestai` and `soniox` transcription providers.

### Removed

- Amazon Transcribe and Google Cloud Speech-to-Text models and providers. Applications using `amazon.transcribe`, `google.enhanced`, or `google.standard` must select a supported model before upgrading.

Gemini models remain supported. This major release reflects removal of supported model and provider identifiers.
