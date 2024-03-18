from selene import browser, be, have
import pytest


def test_search_res(browser_settings):
    browser.element('[name="q"]').clear()
    browser.element('[name="q"]').type('yashaka/selene').press_enter()
    browser.element('#search').should(
        have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_no_res(browser_settings):
    any_text = "gdsjfgjrwerwerewr"
    browser.element('[name="q"]').clear()
    browser.element('[name="q"]').type(any_text).press_enter()
    browser.element('#result-stats').should(have.text('About 0 results'))
