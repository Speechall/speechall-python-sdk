from typing import Literal, cast

ExactRuleKind = Literal["exact"]

EXACT_RULE_KIND_VALUES: set[ExactRuleKind] = {
    "exact",
}


def check_exact_rule_kind(value: str) -> ExactRuleKind:
    if value in EXACT_RULE_KIND_VALUES:
        return cast(ExactRuleKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EXACT_RULE_KIND_VALUES!r}")
