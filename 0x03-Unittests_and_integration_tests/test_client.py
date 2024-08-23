#!/usr/bin/env python3
"""
Module to test the GithubOrgClient class
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """
    Test the GithubOrgClient class
    """
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value
        """
        test_payload = {"org_name": org_name}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        result = client.org
        
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        
        self.assertEqual(result, test_payload)
