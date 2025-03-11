# tests/test_script.py
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("file:///usr/src/sample-project/index.html")
        yield page
        browser.close()


def test_worm_initial_position_random(page):
    # Get the initial position of the worm
    worm_x = page.evaluate("() => window.wormX")
    worm_y = page.evaluate("() => window.wormY")

    # Check if the worm's initial position is within the viewport
    viewport_width = page.viewport_size['width']
    viewport_height = page.viewport_size['height']

    assert 0 <= worm_x <= viewport_width, f"Worm X position {worm_x} is not within viewport width (0-{viewport_width})"
    assert 0 <= worm_y <= viewport_height, f"Worm Y position {worm_y} is not within viewport height (0-{viewport_height})"
