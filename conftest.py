import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()


@pytest.fixture
def browser():
    browser = webdriver.Chrome()

    yield browser

    browser.quit()