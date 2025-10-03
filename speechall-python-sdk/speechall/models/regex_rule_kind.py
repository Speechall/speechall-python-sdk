from typing import Literal, cast

RegexRuleKind = Literal["regex"]

REGEX_RULE_KIND_VALUES: set[RegexRuleKind] = {
    "regex",
}


def check_regex_rule_kind(value: str) -> RegexRuleKind:
    if value in REGEX_RULE_KIND_VALUES:
        return cast(RegexRuleKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGEX_RULE_KIND_VALUES!r}")
