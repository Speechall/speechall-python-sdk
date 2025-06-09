# OpenAICreateTranslationResponseJson

Standard JSON response for OpenAI-compatible translation requests when `response_format` is `json`. Contains the translated English text.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 

## Example

```python
from openapi_client.models.open_ai_create_translation_response_json import OpenAICreateTranslationResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of OpenAICreateTranslationResponseJson from a JSON string
open_ai_create_translation_response_json_instance = OpenAICreateTranslationResponseJson.from_json(json)
# print the JSON string representation of the object
print OpenAICreateTranslationResponseJson.to_json()

# convert the object into a dict
open_ai_create_translation_response_json_dict = open_ai_create_translation_response_json_instance.to_dict()
# create an instance of OpenAICreateTranslationResponseJson from a dict
open_ai_create_translation_response_json_from_dict = OpenAICreateTranslationResponseJson.from_dict(open_ai_create_translation_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


