# coding: utf-8

"""
    Speechall API

    The Speechall REST API provides powerful and flexible speech-to-text capabilities. It allows you to transcribe audio files using various underlying STT providers and models, optionally apply custom text replacement rules, and access results in multiple formats. The API includes standard endpoints for transcription and endpoints compatible with the OpenAI API structure. 

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field

from speechall.models.create_replacement_ruleset201_response import CreateReplacementRuleset201Response
from speechall.models.create_replacement_ruleset_request import CreateReplacementRulesetRequest

from speechall.api_client import ApiClient
from speechall.api_response import ApiResponse
from speechall.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ReplacementRulesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_replacement_ruleset(self, create_replacement_ruleset_request : Annotated[CreateReplacementRulesetRequest, Field(..., description="JSON object containing the name for the ruleset and an array of replacement rule objects.")], **kwargs) -> CreateReplacementRuleset201Response:  # noqa: E501
        """Create a reusable set of text replacement rules.  # noqa: E501

        Defines a named set of replacement rules (exact match, regex) that can be applied during transcription requests using its `ruleset_id`. Rules within a set are applied sequentially to the transcription text.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_replacement_ruleset(create_replacement_ruleset_request, async_req=True)
        >>> result = thread.get()

        :param create_replacement_ruleset_request: JSON object containing the name for the ruleset and an array of replacement rule objects. (required)
        :type create_replacement_ruleset_request: CreateReplacementRulesetRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateReplacementRuleset201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the create_replacement_ruleset_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.create_replacement_ruleset_with_http_info(create_replacement_ruleset_request, **kwargs)  # noqa: E501

    @validate_arguments
    def create_replacement_ruleset_with_http_info(self, create_replacement_ruleset_request : Annotated[CreateReplacementRulesetRequest, Field(..., description="JSON object containing the name for the ruleset and an array of replacement rule objects.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Create a reusable set of text replacement rules.  # noqa: E501

        Defines a named set of replacement rules (exact match, regex) that can be applied during transcription requests using its `ruleset_id`. Rules within a set are applied sequentially to the transcription text.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_replacement_ruleset_with_http_info(create_replacement_ruleset_request, async_req=True)
        >>> result = thread.get()

        :param create_replacement_ruleset_request: JSON object containing the name for the ruleset and an array of replacement rule objects. (required)
        :type create_replacement_ruleset_request: CreateReplacementRulesetRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CreateReplacementRuleset201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'create_replacement_ruleset_request'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_replacement_ruleset" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['create_replacement_ruleset_request'] is not None:
            _body_params = _params['create_replacement_ruleset_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['bearerAuth']  # noqa: E501

        _response_types_map = {
            '201': "CreateReplacementRuleset201Response",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '402': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
            '504': "ErrorResponse",
        }

        return self.api_client.call_api(
            '/replacement-rulesets', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
