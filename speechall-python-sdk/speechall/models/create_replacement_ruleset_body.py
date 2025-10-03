from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.exact_rule import ExactRule
    from ..models.regex_group_rule import RegexGroupRule
    from ..models.regex_rule import RegexRule


T = TypeVar("T", bound="CreateReplacementRulesetBody")


@_attrs_define
class CreateReplacementRulesetBody:
    name: str
    """ A user-defined name for this ruleset for easier identification. """
    rules: list[Union["ExactRule", "RegexGroupRule", "RegexRule"]]
    """ An ordered array of replacement rules. Rules are applied in the order they appear in this list. See the
    `ReplacementRule` schema for different rule types (exact, regex, regex_group). """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.exact_rule import ExactRule
        from ..models.regex_rule import RegexRule

        name = self.name

        rules = []
        for rules_item_data in self.rules:
            rules_item: dict[str, Any]
            if isinstance(rules_item_data, ExactRule):
                rules_item = rules_item_data.to_dict()
            elif isinstance(rules_item_data, RegexRule):
                rules_item = rules_item_data.to_dict()
            else:
                rules_item = rules_item_data.to_dict()

            rules.append(rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "rules": rules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exact_rule import ExactRule
        from ..models.regex_group_rule import RegexGroupRule
        from ..models.regex_rule import RegexRule

        d = dict(src_dict)
        name = d.pop("name")

        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:

            def _parse_rules_item(data: object) -> Union["ExactRule", "RegexGroupRule", "RegexRule"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_replacement_rule_type_0 = ExactRule.from_dict(data)

                    return componentsschemas_replacement_rule_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_replacement_rule_type_1 = RegexRule.from_dict(data)

                    return componentsschemas_replacement_rule_type_1
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_replacement_rule_type_2 = RegexGroupRule.from_dict(data)

                return componentsschemas_replacement_rule_type_2

            rules_item = _parse_rules_item(rules_item_data)

            rules.append(rules_item)

        create_replacement_ruleset_body = cls(
            name=name,
            rules=rules,
        )

        create_replacement_ruleset_body.additional_properties = d
        return create_replacement_ruleset_body

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
