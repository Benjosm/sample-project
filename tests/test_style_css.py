# tests/test_style_css.py

import pytest
import os

# Assuming style.css exists and is not empty

def test_style_css_exists():
    """Test that style.css file exists."""
    assert os.path.exists("style.css"), "style.css does not exist"


def test_style_css_is_not_empty():
    """Test that style.css is not empty"""
    with open("style.css", "r") as f:
        content = f.read()
        assert len(content) > 0, "style.css is empty"
