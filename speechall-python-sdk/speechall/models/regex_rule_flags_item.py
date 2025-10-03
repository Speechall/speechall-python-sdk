from typing import Literal, cast

RegexRuleFlagsItem = Literal["i", "m", "s", "u", "x"]

REGEX_RULE_FLAGS_ITEM_VALUES: set[RegexRuleFlagsItem] = {
    "i",
    "m",
    "s",
    "u",
    "x",
}


def check_regex_rule_flags_item(value: str) -> RegexRuleFlagsItem:
    if value in REGEX_RULE_FLAGS_ITEM_VALUES:
        return cast(RegexRuleFlagsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGEX_RULE_FLAGS_ITEM_VALUES!r}")
