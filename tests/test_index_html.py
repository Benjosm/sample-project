# tests/test_index_html.py
import pytest


def test_worm_segments_exist():
    with open("index.html", "r") as f:
        html_content = f.read()

    assert '<div class="worm-segment head">' in html_content
    assert '<div class="worm-segment body">' in html_content
    assert '<div class="worm-segment tail">' in html_content
    assert html_content.count('<div class="worm-segment body">') == 6
