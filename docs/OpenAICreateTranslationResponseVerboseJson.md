# OpenAICreateTranslationResponseVerboseJson


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | The language of the output translation (always &#x60;english&#x60;). | 
**duration** | **str** | The duration of the input audio. | 
**text** | **str** | The translated text. | 
**segments** | [**List[OpenAITranscriptionSegment]**](OpenAITranscriptionSegment.md) | Segments of the translated text and their corresponding details. | [optional] 

## Example

```python
from openapi_client.models.open_ai_create_translation_response_verbose_json import OpenAICreateTranslationResponseVerboseJson

# TODO update the JSON string below
json = "{}"
# create an instance of OpenAICreateTranslationResponseVerboseJson from a JSON string
open_ai_create_translation_response_verbose_json_instance = OpenAICreateTranslationResponseVerboseJson.from_json(json)
# print the JSON string representation of the object
print OpenAICreateTranslationResponseVerboseJson.to_json()

# convert the object into a dict
open_ai_create_translation_response_verbose_json_dict = open_ai_create_translation_response_verbose_json_instance.to_dict()
# create an instance of OpenAICreateTranslationResponseVerboseJson from a dict
open_ai_create_translation_response_verbose_json_from_dict = OpenAICreateTranslationResponseVerboseJson.from_dict(open_ai_create_translation_response_verbose_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


