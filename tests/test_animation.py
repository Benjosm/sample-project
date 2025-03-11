# tests/test_animation.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_animation_exists(driver):
    driver.get("file:///usr/src/sample-project/index.html")
    try:
        # Assuming there is an element with class 'animated-element' that has animation
        element = driver.find_element(By.CLASS_NAME, "animated-element")
        assert element is not None
    except:
        pytest.fail("Animation element not found")


def test_animation_plays(driver):
    driver.get("file:///usr/src/sample-project/index.html")
    try:
        element = driver.find_element(By.CLASS_NAME, "animated-element")
        initial_position = element.location
        # Wait for animation to potentially change the element's position
        import time
        time.sleep(2)
        final_position = element.location
        # Check if the position has changed (a basic way to check for animation)
        assert initial_position != final_position
    except:
        pytest.fail("Animation did not play or element not found")
