# src/main.py
from plan_reader import parse_plan
from jira_issue_creator import create_jira_issue
import os

JIRA_PROJECT_KEY = "SP"

def main():
    # Read plan from file
    try:
        with open("plan.txt", "r") as f:
            plan_text = f.read()
    except FileNotFoundError:
        print("Error: plan.txt not found.")
        return

    # Parse plan
    tasks = parse_plan(plan_text)

    # Jira options (replace with your actual values or environment variables)
    jira_options = {
        'server': os.environ.get('JIRA_SERVER'),
        'basic_auth': (os.environ.get('JIRA_USER'), os.environ.get('JIRA_PASSWORD'))
    }

    # Create Jira issues for each task
    for task in tasks:
        if task:
            try:
                issue = create_jira_issue(JIRA_PROJECT_KEY, task, task, jira_options)
                if issue:
                    print(f"Created issue: {issue.key} - {task}")
                else:
                    print(f"Failed to create issue for task: {task}")
            except Exception as e:
                print(f"Error creating issue for task '{task}': {e}")

if __name__ == "__main__":
    main()
