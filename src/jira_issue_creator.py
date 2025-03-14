# src/jira_issue_creator.py
from jira import JIRA


def create_jira_issue(project_key, summary, description, jira_options):
    """Creates a Jira issue.

    Args:
        project_key (str): The key of the Jira project.
        summary (str): The summary of the issue.
        description (str): The description of the issue.
        jira_options (dict): Jira connection options.

    Returns:
        jira.Issue: The created Jira issue, or None if an error occurred.
    """
    try:
        jira = JIRA(**jira_options)
        issue = jira.create_issue(
            project=project_key,
            summary=summary,
            description=description,
            issuetype={'name': 'Task'}
        )
        return issue
    except Exception as e:
        print(f"Error creating Jira issue: {e}")
        return None
