# tests/test_cross_browser.py
import pytest
from selenium import webdriver
from selenium.webdriver.safari.options import Options

# Define a fixture to set up a Safari driver
@pytest.fixture(scope="session")
def safari_driver():
    options = Options()
    # options.add_argument("--headless")  # Safari doesn't support headless mode directly
    driver = webdriver.Safari(options=options)
    yield driver
    driver.quit()

# Define a test function
def test_cross_browser_compatibility(safari_driver):
    # Replace with the URL of your application
    safari_driver.get("file:///usr/src/sample-project/index.html")

    # Example: Check if a specific element is present
    try:
        element = safari_driver.find_element("id", "myElement")  # Assuming an element with id 'myElement' exists in index.html. This will cause the test to fail if not.
        assert element.is_displayed()
        print("Safari test passed")
    except:
        pytest.fail("Safari test failed")