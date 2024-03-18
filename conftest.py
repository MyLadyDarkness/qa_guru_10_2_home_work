import pytest
from selene import browser, be, have


@pytest.fixture(scope="session")  # all tests will be run in one browser session
def browser_settings():
    browser.driver.set_window_size("800", "600")
    browser.open('https://www.google.com/')
    print("Browser fixture")
    yield  # go to body of test
    print("Close browser")
    browser.close()