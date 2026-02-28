import json
from typing import Any, Dict, Tuple


def load_json(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: str, obj: Dict[str, Any]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, sort_keys=True)
        f.write("\n")


def deep_equal(a: Dict[str, Any], b: Dict[str, Any]) -> Tuple[bool, str]:
    """
    Strict compare + helpful message for CI logs.
    """
    if a == b:
        return True, "match"
    return False, "golden mismatch: output differs from baseline"
