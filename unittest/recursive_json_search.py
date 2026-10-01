"""Recursive, role-aware search for values in JSON-like objects."""

from policy import POLICY


def json_search(key, input_object, role=None):
    """Return all accessible ``(key, value)`` matches in nested JSON data."""
    # Unknown and missing roles have no permissions (deny by default).
    if role not in {"admin", "operator", "viewer"}:
        return []

    allowed_roles = POLICY.get(key, ())
    if role not in allowed_roles:
        return []

    matches = []

    def visit(value):
        if isinstance(value, dict):
            for child_key, child_value in value.items():
                if child_key == key:
                    matches.append((child_key, child_value))
                visit(child_value)
        elif isinstance(value, list):
            for item in value:
                visit(item)

    visit(input_object)
    return matches
