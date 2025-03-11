# tests/test_style_css.py
import pytest

# Assuming style.css is in the same directory as index.html
STYLESHEET_PATH = 'style.css'

@pytest.fixture
def stylesheet_content():
    with open(STYLESHEET_PATH, 'r') as f:
        return f.read()


def test_body_background_color(stylesheet_content):
    assert 'background-color: #f0f0f0' in stylesheet_content or 'background-color: #f8f8f8' in stylesheet_content, \
           f"Expected body background-color to be #f0f0f0 or #f8f8f8, but found neither in {STYLESHEET_PATH}"


def test_body_font_family(stylesheet_content):
    assert 'font-family: sans-serif' in stylesheet_content, \
           f"Expected body font-family to be sans-serif, but not found in {STYLESHEET_PATH}"
