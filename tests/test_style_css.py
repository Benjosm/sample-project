# tests/test_style_css.py
import pytest

# Assuming style.css exists and is linked in index.html

def test_css_exists():
    with open("style.css", "r") as f:
        assert f.read() is not None


def test_css_for_responsiveness():
    # This is a placeholder.  You'll need to inspect the CSS content.
    # For example, check for media queries.
    try:
      with open("style.css", "r") as f:
        css_content = f.read()
      assert "@media" in css_content
    except FileNotFoundError:
      pytest.fail("style.css not found")

