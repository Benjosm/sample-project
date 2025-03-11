# tests/test_style.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_worm_tail_background_color(driver):
    driver.get("file:///usr/src/sample-project/index.html")
    tail_segment = driver.find_element("css selector", ".worm-segment.tail")
    background_color = tail_segment.value_of_css_property("background-color")
    assert background_color == "rgba(50, 205, 50, 1)"  # Medium Green
