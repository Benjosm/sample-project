# src/cli.py
import argparse

def main():
    parser = argparse.ArgumentParser(description='Process plan files and interact with Jira.')
    parser.add_argument('plan_file', help='Path to the plan file')
    parser.add_argument('--jira_url', help='Jira instance URL')
    parser.add_argument('--jira_username', help='Jira username')
    parser.add_argument('--jira_password', help='Jira password or API token')

    args = parser.parse_args()

    print(f'Processing plan file: {args.plan_file}')
    if args.jira_url:
        print(f'Connecting to Jira at: {args.jira_url}')

if __name__ == '__main__':
    main()
