from typing import Literal, cast

RegexGroupRuleFlagsItem = Literal["i", "m", "s", "u", "x"]

REGEX_GROUP_RULE_FLAGS_ITEM_VALUES: set[RegexGroupRuleFlagsItem] = {
    "i",
    "m",
    "s",
    "u",
    "x",
}


def check_regex_group_rule_flags_item(value: str) -> RegexGroupRuleFlagsItem:
    if value in REGEX_GROUP_RULE_FLAGS_ITEM_VALUES:
        return cast(RegexGroupRuleFlagsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGEX_GROUP_RULE_FLAGS_ITEM_VALUES!r}")
