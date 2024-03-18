from selene import browser, be, have
from selenium import webdriver


def open_page():
    browser.open('https://www.google.com/')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    assert browser.element('[data-test-id="mainline"]') == 'Selene - User-oriented Web UI browser tests in Python'
    #browser.element('[data-test-id="mainline"]').should(
        #have.text('Selene - User-oriented Web UI browser tests in Python'))

    #assert ("123", 123)
