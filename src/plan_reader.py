# src/plan_reader.py

import re


def parse_plan(text):
    """Parses a plan text and extracts tasks.

    Args:
        text: The plan text.

    Returns:
        A list of task descriptions.
    """
    tasks = []
    for line in text.splitlines():
        if line.startswith("Task:"):
            tasks.append(line[5:].strip())
        elif line.startswith("Step:"):
            tasks.append(line[5:].strip())
        elif re.match(r"^\d+\.\s", line):
            match = re.match(r"^\d+\.\s(.*?)$", line)
            if match:
                tasks.append(match.group(1).strip())
    return tasks