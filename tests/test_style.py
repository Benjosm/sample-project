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


def test_h1_color():
    # This test checks if the h1 tag has the correct color from style.css
    with open("index.html", "r") as html_file, open("style.css", "r") as css_file:
        html_content = html_file.read()
        css_content = css_file.read()

        # Assuming style.css contains something like: h1 { color: blue; }
        if "h1 { color: blue; }" in css_content:
            assert "<h1" in html_content  # Make sure h1 tag exists
        else:
            pytest.fail("CSS rule 'h1 { color: blue; }' not found in style.css")
