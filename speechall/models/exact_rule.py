# coding: utf-8

"""
    Speechall API

    The Speechall REST API provides powerful and flexible speech-to-text capabilities. It allows you to transcribe audio files using various underlying STT providers and models, optionally apply custom text replacement rules, and access results in multiple formats. The API includes standard endpoints for transcription and endpoints compatible with the OpenAI API structure. 

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, validator

class ExactRule(BaseModel):
    """
    Defines a replacement rule based on finding an exact string match.  # noqa: E501
    """
    kind: StrictStr = Field(default=..., description="Discriminator field identifying the rule type as 'exact'.")
    search: StrictStr = Field(default=..., description="The exact text string to search for within the transcription.")
    replacement: StrictStr = Field(default=..., description="The text string to replace the found 'search' text with.")
    case_sensitive: Optional[StrictBool] = Field(default=False, alias="caseSensitive", description="If true, the search will match only if the case is identical. If false (default), the search ignores case.")
    __properties = ["kind", "search", "replacement", "caseSensitive"]

    @validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('exact',):
            raise ValueError("must be one of enum values ('exact')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ExactRule:
        """Create an instance of ExactRule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExactRule:
        """Create an instance of ExactRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExactRule.parse_obj(obj)

        _obj = ExactRule.parse_obj({
            "kind": obj.get("kind"),
            "search": obj.get("search"),
            "replacement": obj.get("replacement"),
            "case_sensitive": obj.get("caseSensitive") if obj.get("caseSensitive") is not None else False
        })
        return _obj


