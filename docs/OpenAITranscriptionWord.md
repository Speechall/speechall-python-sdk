# OpenAITranscriptionWord

Represents a single word identified during transcription, including its start and end times. Included in `verbose_json` response when `word` granularity is requested.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**word** | **str** | The text content of the word. | 
**start** | **float** | Start time of the word in seconds. | 
**end** | **float** | End time of the word in seconds. | 

## Example

```python
from openapi_client.models.open_ai_transcription_word import OpenAITranscriptionWord

# TODO update the JSON string below
json = "{}"
# create an instance of OpenAITranscriptionWord from a JSON string
open_ai_transcription_word_instance = OpenAITranscriptionWord.from_json(json)
# print the JSON string representation of the object
print OpenAITranscriptionWord.to_json()

# convert the object into a dict
open_ai_transcription_word_dict = open_ai_transcription_word_instance.to_dict()
# create an instance of OpenAITranscriptionWord from a dict
open_ai_transcription_word_from_dict = OpenAITranscriptionWord.from_dict(open_ai_transcription_word_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


