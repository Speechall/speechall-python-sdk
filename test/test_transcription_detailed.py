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

from speechall.models.transcription_detailed import TranscriptionDetailed  # noqa: E501

class TestTranscriptionDetailed(unittest.TestCase):
    """TranscriptionDetailed unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TranscriptionDetailed:
        """Test TranscriptionDetailed
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TranscriptionDetailed`
        """
        model = TranscriptionDetailed()  # noqa: E501
        if include_optional:
            return TranscriptionDetailed(
                id = 'txn_123abc456def',
                text = 'Hello world. This is a test transcription with two speakers.',
                language = 'en',
                duration = 15.75,
                segments = [
                    speechall.models.transcription_segment.TranscriptionSegment(
                        start = 0.5, 
                        end = 4.25, 
                        text = 'Hello world.', 
                        speaker = 'Speaker 0', 
                        confidence = 0.95, )
                    ],
                words = [
                    speechall.models.transcription_word.TranscriptionWord(
                        start = 0.5, 
                        end = 4.25, 
                        word = 'Hello', 
                        speaker = 'Speaker 0', 
                        confidence = 0.95, )
                    ],
                provider_metadata = { }
            )
        else:
            return TranscriptionDetailed(
                id = 'txn_123abc456def',
                text = 'Hello world. This is a test transcription with two speakers.',
        )
        """

    def testTranscriptionDetailed(self):
        """Test TranscriptionDetailed"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
