# tests/test_index_html.py
import pytest

# Assuming index.html has a title


def test_index_html_has_title():
    with open("index.html", "r") as f:
        content = f.read()
    assert "<title>" in content, "index.html does not contain a title tag"
