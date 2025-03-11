# tests/test_style_css.py
import pytest


# Assuming style.css exists and is linked in index.html


def test_body_background_color():
    with open("style.css", "r") as f:
        css_content = f.read()
    assert "background-color: #f0f0f0;" in css_content, "Background color should be #f0f0f0"


def test_worm_color():
    with open("style.css", "r") as f:
        css_content = f.read()
    assert "color: green;" in css_content, "Worm color should be green"


