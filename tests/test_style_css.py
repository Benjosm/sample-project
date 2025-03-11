# tests/test_style_css.py

import pytest
from pathlib import Path


@pytest.fixture
def style_css_content():
    """Reads the content of style.css."""
    try:
        with open("style.css", "r") as f:
            return f.read()
    except FileNotFoundError:
        pytest.fail("style.css not found")


def test_style_css_exists():
    assert Path("style.css").exists()


# Add more tests for style.css functionality if applicable
