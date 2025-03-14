# test/test_jira_auth.py
import unittest
from unittest.mock import patch, mock_open, MagicMock
import os
from src.jira_auth import authenticate_jira


class TestJiraAuthentication(unittest.TestCase):
    @patch('src.jira_auth.JIRA')
    @patch.dict(os.environ, {"JIRA_URL": "http://example.com", "JIRA_USERNAME": "user", "JIRA_PASSWORD": "password"})
    def test_successful_authentication(self, mock_jira):
        # Mock the JIRA object to avoid actual authentication attempts
        mock_jira.return_value = MagicMock()
        try:
            jira = authenticate_jira()
            self.assertTrue(jira, "Authentication should be successful.")
        except Exception as e:
            self.fail(f"Authentication failed: {e}")