# tests/test_style.py
import pytest

# Assuming style.css and index.html are the relevant files


def test_stylesheet_exists():
    with open("style.css", "r") as f:
        assert f.read() is not None


def test_responsive_design():
    # This is a placeholder.  Needs a more robust test
    # This is a test to make sure the index.html contains viewport meta tag.
    with open("index.html", "r") as f:
        content = f.read()
        assert '<meta name="viewport"' in content


