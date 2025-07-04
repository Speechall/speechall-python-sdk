# coding: utf-8

"""
    Speechall API

    The Speechall REST API provides powerful and flexible speech-to-text capabilities. It allows you to transcribe audio files using various underlying STT providers and models, optionally apply custom text replacement rules, and access results in multiple formats. The API includes standard endpoints for transcription and endpoints compatible with the OpenAI API structure. 

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from speechall.models.error_response import ErrorResponse  # noqa: E501

class TestErrorResponse(unittest.TestCase):
    """ErrorResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ErrorResponse:
        """Test ErrorResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ErrorResponse`
        """
        model = ErrorResponse()  # noqa: E501
        if include_optional:
            return ErrorResponse(
                message = ''
            )
        else:
            return ErrorResponse(
                message = '',
        )
        """

    def testErrorResponse(self):
        """Test ErrorResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
