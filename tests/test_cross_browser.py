# tests/test_cross_browser.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(params=["chrome", "firefox", "edge"], scope="function")
def browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {request.param}")
    
    driver.implicitly_wait(10) # seconds
    yield driver
    driver.quit()


def test_page_title(browser):
    browser.get("file:///usr/src/sample-project/index.html")  # Assuming index.html is in the root
    assert "Worm Game" in browser.title


def test_worm_container_exists(browser):
    browser.get("file:///usr/src/sample-project/index.html")
    worm_container = browser.find_element(By.ID, "worm-container")
    assert worm_container is not None


def test_worm_container_style(browser):
    browser.get("file:///usr/src/sample-project/index.html")
    worm_container = browser.find_element(By.ID, "worm-container")
    # Example: Check if the container has a specific background color (adjust as needed)
    assert "rgb(0, 128, 0)" in worm_container.value_of_css_property("background-color") # Green
