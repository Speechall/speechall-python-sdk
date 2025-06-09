# OpenAICreateTranscriptionResponseVerboseJson

Represents a verbose json transcription response returned by model, based on the provided input.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | The language of the input audio. | 
**duration** | **float** | The duration of the input audio. | 
**text** | **str** | The transcribed text. | 
**words** | [**List[OpenAITranscriptionWord]**](OpenAITranscriptionWord.md) | Extracted words and their corresponding timestamps. | [optional] 
**segments** | [**List[OpenAITranscriptionSegment]**](OpenAITranscriptionSegment.md) | Segments of the transcribed text and their corresponding details. | [optional] 

## Example

```python
from openapi_client.models.open_ai_create_transcription_response_verbose_json import OpenAICreateTranscriptionResponseVerboseJson

# TODO update the JSON string below
json = "{}"
# create an instance of OpenAICreateTranscriptionResponseVerboseJson from a JSON string
open_ai_create_transcription_response_verbose_json_instance = OpenAICreateTranscriptionResponseVerboseJson.from_json(json)
# print the JSON string representation of the object
print OpenAICreateTranscriptionResponseVerboseJson.to_json()

# convert the object into a dict
open_ai_create_transcription_response_verbose_json_dict = open_ai_create_transcription_response_verbose_json_instance.to_dict()
# create an instance of OpenAICreateTranscriptionResponseVerboseJson from a dict
open_ai_create_transcription_response_verbose_json_from_dict = OpenAICreateTranscriptionResponseVerboseJson.from_dict(open_ai_create_transcription_response_verbose_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


