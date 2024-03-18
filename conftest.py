import pytest
from selene import browser


@pytest.fixture(scope="function")
def browser_settings():
    browser.config.base_url = 'https://google.com'
    browser.config.window_height = 800
    browser.config.window_width = 600
    yield
    browser.quit()
