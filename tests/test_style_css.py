# tests/test_style_css.py
import pytest
from bs4 import BeautifulSoup

@pytest.fixture
def index_html_content():
    with open("index.html", "r") as f:
        return f.read()


@pytest.fixture
def soup(index_html_content):
    return BeautifulSoup(index_html_content, 'html.parser')


def test_worm_head_background_color(soup):
    head = soup.find(class_='worm-segment head')
    if head:
        style = head.get('style')
        assert "background-color: #347C17;" in style if style else False, "Worm head background color not set correctly"
    else:
        pytest.fail("Worm head element not found")
