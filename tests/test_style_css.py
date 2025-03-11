# tests/test_style_css.py

import pytest

# Assuming style.css should have some comments


def test_style_css_has_comments():
    with open("style.css", "r") as f:
        content = f.read()
        assert "/*" in content, "style.css should contain comments (/* */)"
