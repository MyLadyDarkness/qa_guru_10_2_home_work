import pytest


@pytest.fixture(scope="session")  # all tests will be run in one browser session
def browser1():
    print("Browser fixture")
    yield  # go to body of test
    print("Close browser")