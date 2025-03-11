# tests/test_cross_browser.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action='store', default='chrome', help='browser to use: chrome,firefox, safari'
    )

@pytest.fixture(scope='session')
def driver(request):
    browser = request.config.getoption('browser')
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'safari':
        driver = webdriver.Safari()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.implicitly_wait(10)  # seconds
    yield driver
    driver.quit()


@pytest.mark.parametrize("browser", ["chrome", "firefox", "safari"])
def test_page_title(driver, browser):
    driver.get("file:///usr/src/sample-project/index.html")
    expected_title = "Sample Project"
    assert expected_title in driver.title

@pytest.mark.parametrize("browser", ["chrome", "firefox", "safari"])
def test_css_styles(driver, browser):
    driver.get("file:///usr/src/sample-project/index.html")
    element = driver.find_element("css selector", "h1")
    assert element.value_of_css_property("color") == "rgba(0, 0, 0, 1)" # Assuming black text as default
