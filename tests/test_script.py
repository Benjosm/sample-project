# tests/test_script.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def browser():
    service = Service(executable_path="/usr/bin/chromedriver")  # Assuming chromedriver is installed
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def test_script_functionality(browser):
    browser.get("file:///usr/src/sample-project/index.html")  # Assumes index.html exists in the root
    # Add some assertions to test your javascript function here. 
    # For example, if your script changes the text of an element with id="myElement":
    # browser.execute_script("myFunction();")  # Assuming myFunction() exists in script.js
    # element = browser.find_element(By.ID, "myElement")
    # assert element.text == "Expected Text", "Script did not modify element as expected"
    
    #This is a failing test to start
    assert 1 == 2, "This test should fail as a starting point."