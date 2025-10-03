from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.regex_rule_flags_item import RegexRuleFlagsItem, check_regex_rule_flags_item
from ..models.regex_rule_kind import RegexRuleKind, check_regex_rule_kind
from ..types import UNSET, Unset

T = TypeVar("T", bound="RegexRule")


@_attrs_define
class RegexRule:
    """Defines a replacement rule based on matching a regular expression pattern."""

    kind: RegexRuleKind
    """ Discriminator field identifying the rule type as 'regex'. """
    pattern: str
    r""" The regular expression pattern to search for. Uses standard regex syntax (implementation specific, often
    PCRE-like). Remember to escape special characters if needed (e.g., `\\.` for a literal dot). """
    replacement: str
    """ The replacement text. Can include backreferences to capture groups from the pattern, like `$1`, `$2`, etc. A
    literal `$` should be escaped (e.g., `$$`). """
    flags: Union[Unset, list[RegexRuleFlagsItem]] = UNSET
    """ An array of flags to modify the regex behavior (e.g., 'i' for case-insensitivity). """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        pattern = self.pattern

        replacement = self.replacement

        flags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.flags, Unset):
            flags = []
            for flags_item_data in self.flags:
                flags_item: str = flags_item_data
                flags.append(flags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "pattern": pattern,
                "replacement": replacement,
            }
        )
        if flags is not UNSET:
            field_dict["flags"] = flags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = check_regex_rule_kind(d.pop("kind"))

        pattern = d.pop("pattern")

        replacement = d.pop("replacement")

        flags = []
        _flags = d.pop("flags", UNSET)
        for flags_item_data in _flags or []:
            flags_item = check_regex_rule_flags_item(flags_item_data)

            flags.append(flags_item)

        regex_rule = cls(
            kind=kind,
            pattern=pattern,
            replacement=replacement,
            flags=flags,
        )

        regex_rule.additional_properties = d
        return regex_rule

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
