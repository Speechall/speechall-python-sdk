# OpenAITranscriptionSegment

Represents a segment of transcribed or translated text, based on OpenAI's verbose JSON structure.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the segment. | 
**seek** | **int** | Seek offset of the segment. | 
**start** | **float** | Start time of the segment in seconds. | 
**end** | **float** | End time of the segment in seconds. | 
**text** | **str** | Text content of the segment. | 
**tokens** | **List[int]** | Array of token IDs for the text content. | 
**temperature** | **float** | Temperature parameter used for generating the segment. | 
**avg_logprob** | **float** | Average logprob of the segment. If the value is lower than -1, consider the logprobs failed. | 
**compression_ratio** | **float** | Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed. | 
**no_speech_prob** | **float** | Probability of no speech in the segment. If the value is higher than 1.0 and the &#x60;avg_logprob&#x60; is below -1, consider this segment silent. | 

## Example

```python
from openapi_client.models.open_ai_transcription_segment import OpenAITranscriptionSegment

# TODO update the JSON string below
json = "{}"
# create an instance of OpenAITranscriptionSegment from a JSON string
open_ai_transcription_segment_instance = OpenAITranscriptionSegment.from_json(json)
# print the JSON string representation of the object
print OpenAITranscriptionSegment.to_json()

# convert the object into a dict
open_ai_transcription_segment_dict = open_ai_transcription_segment_instance.to_dict()
# create an instance of OpenAITranscriptionSegment from a dict
open_ai_transcription_segment_from_dict = OpenAITranscriptionSegment.from_dict(open_ai_transcription_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


