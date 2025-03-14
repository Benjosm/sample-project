# test/test_config.py
import unittest
from unittest.mock import patch
import json

from src.config import JiraConfig

class TestConfig(unittest.TestCase):

    def test_default_issue_type(self):
        config = JiraConfig(config_file="config.json")
        self.assertEqual(config.get_issue_type(), 'Task')

    def test_issue_type_override(self):
        # Create a temporary config file with an issue type override
        with open("config.json", "w") as f:
            json.dump({"default_issue_type": "Bug"}, f)

        config = JiraConfig(config_file="config.json")
        self.assertEqual(config.get_issue_type(), 'Bug')

if __name__ == '__main__':
    unittest.main()
