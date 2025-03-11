# tests/test_script.py

import pytest
from pathlib import Path


@pytest.fixture
def script_js_content():
    """Reads the content of script.js."""
    try:
        with open("script.js", "r") as f:
            return f.read()
    except FileNotFoundError:
        pytest.fail("script.js not found")


def test_script_js_exists():
    assert Path("script.js").exists()


# Add more tests for script.js functionality if applicable
