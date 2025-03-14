# src/jira_auth.py
import os
from jira import JIRA


def authenticate_jira():
    """Authenticates with the Jira API using environment variables for credentials."""
    jira_url = os.environ.get('JIRA_URL')
    jira_username = os.environ.get('JIRA_USERNAME')
    jira_password = os.environ.get('JIRA_PASSWORD')

    if not all([jira_url, jira_username, jira_password]):
        raise ValueError("Missing Jira credentials. Please set JIRA_URL, JIRA_USERNAME, and JIRA_PASSWORD environment variables.")

    try:
        # Basic authentication
        auth_options = {
            'server': jira_url,
            'basic_auth': (jira_username, jira_password)
        }
        jira = JIRA(**auth_options)
        # Test authentication by retrieving the current user's details
        jira.current_user()
        return jira
    except Exception as e:
        print(f"Authentication failed: {e}")
        raise
