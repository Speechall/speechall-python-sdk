# openapi_client.OpenAICompatibleSpeechToTextApi

All URIs are relative to *https://api.speechall.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**openai_compatible_create_transcription**](OpenAICompatibleSpeechToTextApi.md#openai_compatible_create_transcription) | **POST** /openai-compatible/audio/transcriptions | Transcribes audio into the input language, using OpenAI-compatible request format.
[**openai_compatible_create_translation**](OpenAICompatibleSpeechToTextApi.md#openai_compatible_create_translation) | **POST** /openai-compatible/audio/translations | Translates audio into English, using OpenAI-compatible request format.


# **openai_compatible_create_transcription**
> OpenaiCompatibleCreateTranscription200Response openai_compatible_create_transcription(file, model, language=language, prompt=prompt, response_format=response_format, temperature=temperature, timestamp_granularities=timestamp_granularities)

Transcribes audio into the input language, using OpenAI-compatible request format.

Mimics the OpenAI `/audio/transcriptions` endpoint. Accepts audio file uploads via `multipart/form-data`.
Allows specifying model, language, prompt, response format, temperature, and timestamp granularity similar to OpenAI.
Note: The `model` parameter should use Speechall's `provider.model` format.


### Example

* Bearer (API Key) Authentication (bearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.open_ai_audio_response_format import OpenAIAudioResponseFormat
from openapi_client.models.openai_compatible_create_transcription200_response import OpenaiCompatibleCreateTranscription200Response
from openapi_client.models.transcription_model_identifier import TranscriptionModelIdentifier
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.speechall.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.speechall.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OpenAICompatibleSpeechToTextApi(api_client)
    file = None # bytearray | The audio file object (not file name) to transcribe, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm. 
    model = openapi_client.TranscriptionModelIdentifier() # TranscriptionModelIdentifier | 
    language = 'language_example' # str | The language of the input audio. Supplying the input language in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) format will improve accuracy and latency.  (optional)
    prompt = 'prompt_example' # str | An optional text to guide the model's style or continue a previous audio segment. The [prompt](/docs/guides/speech-to-text/prompting) should match the audio language.  (optional)
    response_format = openapi_client.OpenAIAudioResponseFormat() # OpenAIAudioResponseFormat |  (optional)
    temperature = 0 # float | The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.  (optional) (default to 0)
    timestamp_granularities = ['timestamp_granularities_example'] # List[str] | The timestamp granularities to populate for this transcription. `response_format` must be set `verbose_json` to use timestamp granularities. Either or both of these options are supported: `word`, or `segment`. Note: There is no additional latency for segment timestamps, but generating word timestamps incurs additional latency.  (optional)

    try:
        # Transcribes audio into the input language, using OpenAI-compatible request format.
        api_response = api_instance.openai_compatible_create_transcription(file, model, language=language, prompt=prompt, response_format=response_format, temperature=temperature, timestamp_granularities=timestamp_granularities)
        print("The response of OpenAICompatibleSpeechToTextApi->openai_compatible_create_transcription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenAICompatibleSpeechToTextApi->openai_compatible_create_transcription: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| The audio file object (not file name) to transcribe, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.  | 
 **model** | [**TranscriptionModelIdentifier**](TranscriptionModelIdentifier.md)|  | 
 **language** | **str**| The language of the input audio. Supplying the input language in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) format will improve accuracy and latency.  | [optional] 
 **prompt** | **str**| An optional text to guide the model&#39;s style or continue a previous audio segment. The [prompt](/docs/guides/speech-to-text/prompting) should match the audio language.  | [optional] 
 **response_format** | [**OpenAIAudioResponseFormat**](OpenAIAudioResponseFormat.md)|  | [optional] 
 **temperature** | **float**| The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.  | [optional] [default to 0]
 **timestamp_granularities** | [**List[str]**](str.md)| The timestamp granularities to populate for this transcription. &#x60;response_format&#x60; must be set &#x60;verbose_json&#x60; to use timestamp granularities. Either or both of these options are supported: &#x60;word&#x60;, or &#x60;segment&#x60;. Note: There is no additional latency for segment timestamps, but generating word timestamps incurs additional latency.  | [optional] 

### Return type

[**OpenaiCompatibleCreateTranscription200Response**](OpenaiCompatibleCreateTranscription200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transcription successful. The response body format depends on the &#x60;response_format&#x60; parameter specified in the request: - &#x60;json&#x60;: Returns &#x60;OpenAI_CreateTranscriptionResponseJson&#x60;. - &#x60;verbose_json&#x60;: Returns &#x60;OpenAI_CreateTranscriptionResponseVerboseJson&#x60; with detailed segments and optional word timestamps. - &#x60;text&#x60;, &#x60;srt&#x60;, &#x60;vtt&#x60;: Returns the transcription as plain text in the specified format.  |  -  |
**400** | Bad Request - The request was malformed or contained invalid parameters (e.g., invalid language code, missing required field, unsupported option). The response body provides details. |  -  |
**401** | Unauthorized - Authentication failed. The API key is missing, invalid, or expired. |  -  |
**402** | Payment Required - There is no credit left on your account. |  -  |
**404** | Not Found - The requested resource could not be found. This could be an invalid API endpoint path, or a referenced resource ID (like &#x60;ruleset_id&#x60;) that doesn&#39;t exist. For &#x60;/transcribe-remote&#x60;, it could also mean the &#x60;file_url&#x60; was inaccessible. |  -  |
**429** | Too Many Requests - The client has exceeded the rate limit for API requests. Check the &#x60;Retry-After&#x60; header for guidance on when to retry. |  * Retry-After - The recommended number of seconds to wait before making another request. <br>  |
**500** | Internal Server Error - An unexpected error occurred on the server side while processing the request. Retrying the request later might succeed. If the problem persists, contact support. |  -  |
**503** | Service Unavailable - The server is temporarily unable to handle the request, possibly due to maintenance or overload. Try again later. |  -  |
**504** | Gateway Timeout - The server, while acting as a gateway or proxy, did not receive a timely response from an upstream server (e.g., the underlying STT provider). This might be a temporary issue with the provider. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openai_compatible_create_translation**
> OpenaiCompatibleCreateTranslation200Response openai_compatible_create_translation(file, model, prompt=prompt, response_format=response_format, temperature=temperature)

Translates audio into English, using OpenAI-compatible request format.

Mimics the OpenAI `/audio/translations` endpoint. Accepts audio file uploads via `multipart/form-data` and translates the speech into English text.
Allows specifying model, prompt, response format, and temperature similar to OpenAI.
Note: The `model` parameter should use Speechall's `provider.model` format (ensure the selected model supports translation).


### Example

* Bearer (API Key) Authentication (bearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.open_ai_audio_response_format import OpenAIAudioResponseFormat
from openapi_client.models.open_ai_create_translation_request_model import OpenAICreateTranslationRequestModel
from openapi_client.models.openai_compatible_create_translation200_response import OpenaiCompatibleCreateTranslation200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.speechall.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.speechall.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OpenAICompatibleSpeechToTextApi(api_client)
    file = None # bytearray | The audio file object (not file name) translate, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm. 
    model = openapi_client.OpenAICreateTranslationRequestModel() # OpenAICreateTranslationRequestModel | 
    prompt = 'prompt_example' # str | An optional text to guide the model's style or continue a previous audio segment. The [prompt](/docs/guides/speech-to-text/prompting) should be in English.  (optional)
    response_format = openapi_client.OpenAIAudioResponseFormat() # OpenAIAudioResponseFormat |  (optional)
    temperature = 0 # float | The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.  (optional) (default to 0)

    try:
        # Translates audio into English, using OpenAI-compatible request format.
        api_response = api_instance.openai_compatible_create_translation(file, model, prompt=prompt, response_format=response_format, temperature=temperature)
        print("The response of OpenAICompatibleSpeechToTextApi->openai_compatible_create_translation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenAICompatibleSpeechToTextApi->openai_compatible_create_translation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| The audio file object (not file name) translate, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.  | 
 **model** | [**OpenAICreateTranslationRequestModel**](OpenAICreateTranslationRequestModel.md)|  | 
 **prompt** | **str**| An optional text to guide the model&#39;s style or continue a previous audio segment. The [prompt](/docs/guides/speech-to-text/prompting) should be in English.  | [optional] 
 **response_format** | [**OpenAIAudioResponseFormat**](OpenAIAudioResponseFormat.md)|  | [optional] 
 **temperature** | **float**| The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.  | [optional] [default to 0]

### Return type

[**OpenaiCompatibleCreateTranslation200Response**](OpenaiCompatibleCreateTranslation200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Translation successful. The output is always English text. The response body format depends on the &#x60;response_format&#x60; parameter: - &#x60;json&#x60;: Returns &#x60;OpenAI_CreateTranslationResponseJson&#x60;. - &#x60;verbose_json&#x60;: Returns &#x60;OpenAI_CreateTranslationResponseVerboseJson&#x60; with detailed segments. - &#x60;text&#x60;, &#x60;srt&#x60;, &#x60;vtt&#x60;: Returns the translated English text as plain text in the specified format.  |  -  |
**400** | Bad Request - The request was malformed or contained invalid parameters (e.g., invalid language code, missing required field, unsupported option). The response body provides details. |  -  |
**401** | Unauthorized - Authentication failed. The API key is missing, invalid, or expired. |  -  |
**402** | Payment Required - There is no credit left on your account. |  -  |
**404** | Not Found - The requested resource could not be found. This could be an invalid API endpoint path, or a referenced resource ID (like &#x60;ruleset_id&#x60;) that doesn&#39;t exist. For &#x60;/transcribe-remote&#x60;, it could also mean the &#x60;file_url&#x60; was inaccessible. |  -  |
**429** | Too Many Requests - The client has exceeded the rate limit for API requests. Check the &#x60;Retry-After&#x60; header for guidance on when to retry. |  * Retry-After - The recommended number of seconds to wait before making another request. <br>  |
**500** | Internal Server Error - An unexpected error occurred on the server side while processing the request. Retrying the request later might succeed. If the problem persists, contact support. |  -  |
**503** | Service Unavailable - The server is temporarily unable to handle the request, possibly due to maintenance or overload. Try again later. |  -  |
**504** | Gateway Timeout - The server, while acting as a gateway or proxy, did not receive a timely response from an upstream server (e.g., the underlying STT provider). This might be a temporary issue with the provider. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

