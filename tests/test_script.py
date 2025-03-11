# tests/test_script.py
import pytest


def test_script_exists():
    try:
        with open("script.js", "r") as f:
            pass
    except FileNotFoundError:
        pytest.fail("script.js does not exist")


def test_script_has_some_content():
    with open("script.js", "r") as f:
        content = f.read()
    assert len(content) > 0, "script.js is empty"
