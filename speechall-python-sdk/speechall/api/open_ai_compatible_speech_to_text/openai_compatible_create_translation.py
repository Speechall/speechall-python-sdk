from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.open_ai_create_translation_request import OpenAICreateTranslationRequest
from ...models.open_ai_create_translation_response_json import OpenAICreateTranslationResponseJson
from ...models.open_ai_create_translation_response_verbose_json import OpenAICreateTranslationResponseVerboseJson
from ...types import Response


def _get_kwargs(
    *,
    body: OpenAICreateTranslationRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/openai-compatible/audio/translations",
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[ErrorResponse, Union["OpenAICreateTranslationResponseJson", "OpenAICreateTranslationResponseVerboseJson"]]
]:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> Union["OpenAICreateTranslationResponseJson", "OpenAICreateTranslationResponseVerboseJson"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = OpenAICreateTranslationResponseVerboseJson.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = OpenAICreateTranslationResponseJson.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ErrorResponse.from_dict(response.json())

        return response_402

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503

    if response.status_code == 504:
        response_504 = ErrorResponse.from_dict(response.json())

        return response_504

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[ErrorResponse, Union["OpenAICreateTranslationResponseJson", "OpenAICreateTranslationResponseVerboseJson"]]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: OpenAICreateTranslationRequest,
) -> Response[
    Union[ErrorResponse, Union["OpenAICreateTranslationResponseJson", "OpenAICreateTranslationResponseVerboseJson"]]
]:
    """Translates audio into English, using OpenAI-compatible request format.

     Mimics the OpenAI `/audio/translations` endpoint. Accepts audio file uploads via `multipart/form-
    data` and translates the speech into English text.
    Allows specifying model, prompt, response format, and temperature similar to OpenAI.
    Note: The `model` parameter should use Speechall's `provider.model` format (ensure the selected
    model supports translation).

    Args:
        body (OpenAICreateTranslationRequest): Request schema for the OpenAI-compatible
            translation endpoint. Uses `multipart/form-data`. Translates audio into English.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, Union['OpenAICreateTranslationResponseJson', 'OpenAICreateTranslationResponseVerboseJson']]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: OpenAICreateTranslationRequest,
) -> Optional[
    Union[ErrorResponse, Union["OpenAICreateTranslationResponseJson", "OpenAICreateTranslationResponseVerboseJson"]]
]:
    """Translates audio into English, using OpenAI-compatible request format.

     Mimics the OpenAI `/audio/translations` endpoint. Accepts audio file uploads via `multipart/form-
    data` and translates the speech into English text.
    Allows specifying model, prompt, response format, and temperature similar to OpenAI.
    Note: The `model` parameter should use Speechall's `provider.model` format (ensure the selected
    model supports translation).

    Args:
        body (OpenAICreateTranslationRequest): Request schema for the OpenAI-compatible
            translation endpoint. Uses `multipart/form-data`. Translates audio into English.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, Union['OpenAICreateTranslationResponseJson', 'OpenAICreateTranslationResponseVerboseJson']]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: OpenAICreateTranslationRequest,
) -> Response[
    Union[ErrorResponse, Union["OpenAICreateTranslationResponseJson", "OpenAICreateTranslationResponseVerboseJson"]]
]:
    """Translates audio into English, using OpenAI-compatible request format.

     Mimics the OpenAI `/audio/translations` endpoint. Accepts audio file uploads via `multipart/form-
    data` and translates the speech into English text.
    Allows specifying model, prompt, response format, and temperature similar to OpenAI.
    Note: The `model` parameter should use Speechall's `provider.model` format (ensure the selected
    model supports translation).

    Args:
        body (OpenAICreateTranslationRequest): Request schema for the OpenAI-compatible
            translation endpoint. Uses `multipart/form-data`. Translates audio into English.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, Union['OpenAICreateTranslationResponseJson', 'OpenAICreateTranslationResponseVerboseJson']]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: OpenAICreateTranslationRequest,
) -> Optional[
    Union[ErrorResponse, Union["OpenAICreateTranslationResponseJson", "OpenAICreateTranslationResponseVerboseJson"]]
]:
    """Translates audio into English, using OpenAI-compatible request format.

     Mimics the OpenAI `/audio/translations` endpoint. Accepts audio file uploads via `multipart/form-
    data` and translates the speech into English text.
    Allows specifying model, prompt, response format, and temperature similar to OpenAI.
    Note: The `model` parameter should use Speechall's `provider.model` format (ensure the selected
    model supports translation).

    Args:
        body (OpenAICreateTranslationRequest): Request schema for the OpenAI-compatible
            translation endpoint. Uses `multipart/form-data`. Translates audio into English.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, Union['OpenAICreateTranslationResponseJson', 'OpenAICreateTranslationResponseVerboseJson']]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
