"""Tests for recursive JSON search and its role-based access policy."""

import unittest

from recursive_json_search import json_search
from test_data import data


class json_search_test(unittest.TestCase):
    """Exercise the JSON search function and its access controls."""

    def test_search_found(self):
        """Find a permitted key nested within dictionaries and lists."""
        result = json_search("issueSummary", data, role="viewer")
        self.assertEqual(
            result,
            [("issueSummary", "Network Device 10.10.20.82 Is Unreachable From Controller")],
        )

    def test_search_not_found(self):
        """Return an empty list when the requested key is absent."""
        self.assertEqual(json_search("issueSummary", {"other": 1}, role="viewer"), [])

    def test_is_a_list(self):
        """Return matches as a list containing key/value pairs."""
        result = json_search("issueSummary", data, role="viewer")
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(match, tuple) and len(match) == 2 for match in result))

    def test_viewer_cannot_read_apikey(self):
        """Prevent viewers from reading API credentials."""
        self.assertEqual(json_search("apiKey", data, role="viewer"), [])

    def test_operator_cannot_read_apikey(self):
        """Prevent operators from reading API credentials."""
        self.assertEqual(json_search("apiKey", data, role="operator"), [])

    def test_viewer_cannot_read_management_ip(self):
        """Prevent viewers from reading management IP addresses."""
        self.assertEqual(json_search("managementIpAddress", data, role="viewer"), [])

    def test_no_role_cannot_read_protected(self):
        """Deny access to protected fields when no role is supplied."""
        self.assertEqual(json_search("apiKey", data), [])

    def test_unknown_role_denied(self):
        """Deny access to protected fields for roles absent from the policy."""
        self.assertEqual(json_search("apiKey", data, role="root"), [])
        self.assertEqual(json_search("issueSummary", data, role=""), [])

    def test_wrong_role_cannot_read_secret(self):
        """Apply authorization to secret matches nested four levels deep."""
        deeply_nested = {"a": [{"b": {"c": [{"apiKey": "deep-secret"}]}}]}
        self.assertEqual(json_search("apiKey", deeply_nested, role="operator"), [])

    def test_issue_summary_allowed_for_all_roles(self):
        """Allow each policy role to read the non-sensitive issue summary."""
        for role in ("admin", "operator", "viewer"):
            with self.subTest(role=role):
                self.assertEqual(
                    json_search("issueSummary", data, role=role),
                    [("issueSummary", "Network Device 10.10.20.82 Is Unreachable From Controller")],
                )


if __name__ == "__main__":
    unittest.main()
