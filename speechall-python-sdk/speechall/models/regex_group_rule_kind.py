from typing import Literal, cast

RegexGroupRuleKind = Literal["regex_group"]

REGEX_GROUP_RULE_KIND_VALUES: set[RegexGroupRuleKind] = {
    "regex_group",
}


def check_regex_group_rule_kind(value: str) -> RegexGroupRuleKind:
    if value in REGEX_GROUP_RULE_KIND_VALUES:
        return cast(RegexGroupRuleKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGEX_GROUP_RULE_KIND_VALUES!r}")
