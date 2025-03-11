# tests/test_readme.py

import pytest
import os

# Assuming README.md is in the project root
README_PATH = "README.md"

@pytest.fixture
def readme_content():
    with open(README_PATH, "r") as f:
        return f.read()


def test_readme_exists():
    assert os.path.exists(README_PATH), f"{README_PATH} does not exist"


def test_readme_project_description(readme_content):
    assert "Worm Website" in readme_content, "README.md missing project description."


def test_readme_usage_instructions(readme_content):
    assert "index.html" in readme_content and "run" in readme_content, "README.md missing usage instructions."


def test_readme_technology_stack(readme_content):
    assert "HTML" in readme_content and "CSS" in readme_content and "JavaScript" in readme_content, "README.md missing technology stack details."
