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

from speechall.models.create_replacement_ruleset201_response import CreateReplacementRuleset201Response  # noqa: E501

class TestCreateReplacementRuleset201Response(unittest.TestCase):
    """CreateReplacementRuleset201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateReplacementRuleset201Response:
        """Test CreateReplacementRuleset201Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateReplacementRuleset201Response`
        """
        model = CreateReplacementRuleset201Response()  # noqa: E501
        if include_optional:
            return CreateReplacementRuleset201Response(
                id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
            )
        else:
            return CreateReplacementRuleset201Response(
                id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
        )
        """

    def testCreateReplacementRuleset201Response(self):
        """Test CreateReplacementRuleset201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
