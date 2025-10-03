from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.remote_transcription_configuration import RemoteTranscriptionConfiguration
from ...models.transcription_detailed import TranscriptionDetailed
from ...models.transcription_only_text import TranscriptionOnlyText
from ...types import Response


def _get_kwargs(
    *,
    body: RemoteTranscriptionConfiguration,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/transcribe-remote",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, Union["TranscriptionDetailed", "TranscriptionOnlyText"]]]:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Union["TranscriptionDetailed", "TranscriptionOnlyText"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_transcription_response_type_0 = TranscriptionDetailed.from_dict(data)

                return componentsschemas_transcription_response_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_transcription_response_type_1 = TranscriptionOnlyText.from_dict(data)

            return componentsschemas_transcription_response_type_1

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
) -> Response[Union[ErrorResponse, Union["TranscriptionDetailed", "TranscriptionOnlyText"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RemoteTranscriptionConfiguration,
) -> Response[Union[ErrorResponse, Union["TranscriptionDetailed", "TranscriptionOnlyText"]]]:
    """Transcribe an audio file located at a remote URL.

     This endpoint allows you to transcribe an audio file hosted at a publicly accessible URL.
    Provide the URL and transcription options within the JSON request body.
    Useful for transcribing files already stored online.

    Args:
        body (RemoteTranscriptionConfiguration): Configuration options for transcribing audio
            specified by a remote URL via the `/transcribe-remote` endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, Union['TranscriptionDetailed', 'TranscriptionOnlyText']]]
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
    body: RemoteTranscriptionConfiguration,
) -> Optional[Union[ErrorResponse, Union["TranscriptionDetailed", "TranscriptionOnlyText"]]]:
    """Transcribe an audio file located at a remote URL.

     This endpoint allows you to transcribe an audio file hosted at a publicly accessible URL.
    Provide the URL and transcription options within the JSON request body.
    Useful for transcribing files already stored online.

    Args:
        body (RemoteTranscriptionConfiguration): Configuration options for transcribing audio
            specified by a remote URL via the `/transcribe-remote` endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, Union['TranscriptionDetailed', 'TranscriptionOnlyText']]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RemoteTranscriptionConfiguration,
) -> Response[Union[ErrorResponse, Union["TranscriptionDetailed", "TranscriptionOnlyText"]]]:
    """Transcribe an audio file located at a remote URL.

     This endpoint allows you to transcribe an audio file hosted at a publicly accessible URL.
    Provide the URL and transcription options within the JSON request body.
    Useful for transcribing files already stored online.

    Args:
        body (RemoteTranscriptionConfiguration): Configuration options for transcribing audio
            specified by a remote URL via the `/transcribe-remote` endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, Union['TranscriptionDetailed', 'TranscriptionOnlyText']]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: RemoteTranscriptionConfiguration,
) -> Optional[Union[ErrorResponse, Union["TranscriptionDetailed", "TranscriptionOnlyText"]]]:
    """Transcribe an audio file located at a remote URL.

     This endpoint allows you to transcribe an audio file hosted at a publicly accessible URL.
    Provide the URL and transcription options within the JSON request body.
    Useful for transcribing files already stored online.

    Args:
        body (RemoteTranscriptionConfiguration): Configuration options for transcribing audio
            specified by a remote URL via the `/transcribe-remote` endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, Union['TranscriptionDetailed', 'TranscriptionOnlyText']]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
