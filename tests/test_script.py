# tests/test_script.py

import pytest
import os

# Assuming script.js exists and is not empty

def test_script_js_exists():
    """Test that script.js file exists."""
    assert os.path.exists("script.js"), "script.js does not exist"


def test_script_js_is_not_empty():
    """Test that script.js is not empty"""
    with open("script.js", "r") as f:
        content = f.read()
        assert len(content) > 0, "script.js is empty"
