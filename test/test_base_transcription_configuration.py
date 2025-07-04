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

from speechall.models.base_transcription_configuration import BaseTranscriptionConfiguration  # noqa: E501

class TestBaseTranscriptionConfiguration(unittest.TestCase):
    """BaseTranscriptionConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BaseTranscriptionConfiguration:
        """Test BaseTranscriptionConfiguration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BaseTranscriptionConfiguration`
        """
        model = BaseTranscriptionConfiguration()  # noqa: E501
        if include_optional:
            return BaseTranscriptionConfiguration(
                model = 'openai.whisper-1',
                language = 'en',
                output_format = 'text',
                ruleset_id = '',
                punctuation = True,
                timestamp_granularity = 'segment',
                diarization = True,
                initial_prompt = '',
                temperature = 0,
                smart_format = True,
                speakers_expected = 1,
                custom_vocabulary = ["Speechall","Actondon","HIPAA"]
            )
        else:
            return BaseTranscriptionConfiguration(
                model = 'openai.whisper-1',
        )
        """

    def testBaseTranscriptionConfiguration(self):
        """Test BaseTranscriptionConfiguration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
