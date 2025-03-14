# test/test_jira_issue_creator.py
import unittest
from unittest.mock import patch
from src.jira_issue_creator import create_jira_issue


class TestIssueCreation(unittest.TestCase):
    @patch('src.jira_issue_creator.JIRA')
    def test_create_issue_with_hardcoded_data(self, mock_jira):
        issue_data = {
            'project': {'key': 'SP'},
            'issuetype': {'name': 'Task'},
            'summary': 'Test Issue',
            'description': 'This is a test issue',
            'customfield_10000': 'some value' # Example custom field
        }
        # Mock the JIRA object and the create_issue method to avoid actual issue creation
        mock_jira_instance = mock_jira.return_value
        mock_jira_instance.create_issue.return_value = True # Simulate successful issue creation
        try:
            create_jira_issue(issue_data['summary'], issue_data['description'], {'server': 'dummy','basic_auth': ('user', 'pass')}, issue_data)
            # If create_jira_issue doesn't raise an exception, the test passes
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"create_jira_issue raised an exception: {e}")
