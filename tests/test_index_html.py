# tests/test_index_html.py

import pytest

from pathlib import Path

@pytest.fixture
def index_html_content():
    """Reads the content of index.html."""
    try:
        with open("index.html", "r") as f:
            return f.read()
    except FileNotFoundError:
        pytest.fail("index.html not found")


def test_index_html_exists():
    assert Path("index.html").exists()


def test_index_html_contains_title(index_html_content):
    assert "<title>" in index_html_content

