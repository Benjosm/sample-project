# test/test_jira_issue_creator.py
import unittest
from unittest.mock import patch

# Assuming the function is in src/jira_issue_creator.py
from src.jira_issue_creator import create_jira_issue


class TestIssueCreation(unittest.TestCase):
    @patch('src.jira_issue_creator.create_jira_issue')
    def test_create_issue_with_hardcoded_data(self, mock_create_jira_issue):
        # Sample data for the issue
        issue_data = {
            'project': {'key': 'SP'},
            'issuetype': {'name': 'Task'},
            'summary': 'Test issue from automated test',
            'description': 'This is a test issue created by an automated test.'
        }
        
        # Call the function to create the issue
        try:
          create_jira_issue(issue_data)
        except Exception as e:
          # Assert that the function raises an exception
          self.fail(f"create_jira_issue raised an exception: {e}")
        
        # Assert that the function was called with the correct arguments. The mock will throw an exception if it wasn't
        mock_create_jira_issue.assert_called_once()


if __name__ == '__main__':
    unittest.main()
