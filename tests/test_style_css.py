# tests/test_style_css.py
import pytest


def test_style_css_exists():
    try:
        with open("style.css", "r") as f:
            pass
    except FileNotFoundError:
        pytest.fail("style.css does not exist")


def test_style_css_has_some_content():
    with open("style.css", "r") as f:
        content = f.read()
    assert len(content) > 0, "style.css is empty"
