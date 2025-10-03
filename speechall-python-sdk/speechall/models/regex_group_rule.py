from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.regex_group_rule_flags_item import RegexGroupRuleFlagsItem, check_regex_group_rule_flags_item
from ..models.regex_group_rule_kind import RegexGroupRuleKind, check_regex_group_rule_kind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.regex_group_rule_group_replacements import RegexGroupRuleGroupReplacements


T = TypeVar("T", bound="RegexGroupRule")


@_attrs_define
class RegexGroupRule:
    """Defines a replacement rule that uses regex capture groups to apply different replacements to different parts of the
    matched text.

    """

    kind: RegexGroupRuleKind
    """ Discriminator field identifying the rule type as 'regex_group'. """
    pattern: str
    """ The regular expression pattern containing capture groups `(...)`. The entire pattern must match for
    replacements to occur. """
    group_replacements: "RegexGroupRuleGroupReplacements"
    """ An object where keys are capture group numbers (as strings, e.g., "1", "2") and values are the respective
    replacement strings for those groups. Groups not listed are kept as matched. The entire match is reconstructed
    using these replacements. """
    flags: Union[Unset, list[RegexGroupRuleFlagsItem]] = UNSET
    """ An array of flags to modify the regex behavior. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        pattern = self.pattern

        group_replacements = self.group_replacements.to_dict()

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
                "groupReplacements": group_replacements,
            }
        )
        if flags is not UNSET:
            field_dict["flags"] = flags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.regex_group_rule_group_replacements import RegexGroupRuleGroupReplacements

        d = dict(src_dict)
        kind = check_regex_group_rule_kind(d.pop("kind"))

        pattern = d.pop("pattern")

        group_replacements = RegexGroupRuleGroupReplacements.from_dict(d.pop("groupReplacements"))

        flags = []
        _flags = d.pop("flags", UNSET)
        for flags_item_data in _flags or []:
            flags_item = check_regex_group_rule_flags_item(flags_item_data)

            flags.append(flags_item)

        regex_group_rule = cls(
            kind=kind,
            pattern=pattern,
            group_replacements=group_replacements,
            flags=flags,
        )

        regex_group_rule.additional_properties = d
        return regex_group_rule

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
