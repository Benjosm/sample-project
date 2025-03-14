# src/config.py
import json

class JiraConfig:
    def __init__(self, config_file="config.json"):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        try:
            with open(self.config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def get_issue_type(self):
        return self.config.get('default_issue_type', 'Task')

def get_config():
    return JiraConfig()
