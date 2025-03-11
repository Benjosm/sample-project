# tests/test_cross_browser.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# Fixture to set up a Chrome browser instance
@pytest.fixture(scope="module")
def chrome_browser():
    options = Options()
    # Add any browser-specific options here, such as headless mode or specific window size
    # options.add_argument("--headless")
    service = webdriver.chrome.service.Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options, service=service)
    yield driver
    driver.quit()


# Fixture to set up a Firefox browser instance
@pytest.fixture(scope="module")
def firefox_browser():
    options = FirefoxOptions()
    # options.headless = True
    service = webdriver.firefox.service.Service(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(options=options, service=service)
    yield driver
    driver.quit()


# Test to verify that the page title is correct in Chrome
def test_page_title_chrome(chrome_browser):
    chrome_browser.get("file:///usr/src/sample-project/index.html")  # Assuming index.html is in the same directory
    assert "Sample Project" in chrome_browser.title


# Test to verify that a specific element exists in Chrome
def test_element_exists_chrome(chrome_browser):
    chrome_browser.get("file:///usr/src/sample-project/index.html")
    element = chrome_browser.find_element(By.TAG_NAME, "h1")
    assert element.text == "Hello, World!"


# Test to verify that the page title is correct in Firefox
def test_page_title_firefox(firefox_browser):
    firefox_browser.get("file:///usr/src/sample-project/index.html")
    assert "Sample Project" in firefox_browser.title


# Test to verify that a specific element exists in Firefox
def test_element_exists_firefox(firefox_browser):
    firefox_browser.get("file:///usr/src/sample-project/index.html")
    element = firefox_browser.find_element(By.TAG_NAME, "h1")
    assert element.text == "Hello, World!"
