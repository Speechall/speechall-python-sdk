from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.exact_rule_kind import ExactRuleKind, check_exact_rule_kind
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExactRule")


@_attrs_define
class ExactRule:
    """Defines a replacement rule based on finding an exact string match."""

    kind: ExactRuleKind
    """ Discriminator field identifying the rule type as 'exact'. """
    search: str
    """ The exact text string to search for within the transcription. """
    replacement: str
    """ The text string to replace the found 'search' text with. """
    case_sensitive: Union[Unset, bool] = False
    """ If true, the search will match only if the case is identical. If false (default), the search ignores case.
    """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        search = self.search

        replacement = self.replacement

        case_sensitive = self.case_sensitive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "search": search,
                "replacement": replacement,
            }
        )
        if case_sensitive is not UNSET:
            field_dict["caseSensitive"] = case_sensitive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = check_exact_rule_kind(d.pop("kind"))

        search = d.pop("search")

        replacement = d.pop("replacement")

        case_sensitive = d.pop("caseSensitive", UNSET)

        exact_rule = cls(
            kind=kind,
            search=search,
            replacement=replacement,
            case_sensitive=case_sensitive,
        )

        exact_rule.additional_properties = d
        return exact_rule

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
