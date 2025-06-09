# OpenAICreateTranscriptionResponseJson

Represents a transcription response returned by model, based on the provided input.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The transcribed text. | 

## Example

```python
from openapi_client.models.open_ai_create_transcription_response_json import OpenAICreateTranscriptionResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of OpenAICreateTranscriptionResponseJson from a JSON string
open_ai_create_transcription_response_json_instance = OpenAICreateTranscriptionResponseJson.from_json(json)
# print the JSON string representation of the object
print OpenAICreateTranscriptionResponseJson.to_json()

# convert the object into a dict
open_ai_create_transcription_response_json_dict = open_ai_create_transcription_response_json_instance.to_dict()
# create an instance of OpenAICreateTranscriptionResponseJson from a dict
open_ai_create_transcription_response_json_from_dict = OpenAICreateTranscriptionResponseJson.from_dict(open_ai_create_transcription_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


