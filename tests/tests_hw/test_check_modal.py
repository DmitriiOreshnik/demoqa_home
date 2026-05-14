import urllib.request

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = 'https://demoqa.com/modal-dialogs'


def is_page_available(url):
    try:
        response = urllib.request.urlopen(url, timeout=5)
        return response.status == 200
    except Exception:
        return False


@pytest.mark.skipif(not is_page_available(URL), reason='Page is not available')
def test_check_modal(browser):
    browser.get(URL)

    small_modal_button = browser.find_element(By.CSS_SELECTOR, '#showSmallModal')
    large_modal_button = browser.find_element(By.CSS_SELECTOR, '#showLargeModal')

    assert small_modal_button.text == 'Small modal'
    assert large_modal_button.text == 'Large modal'

    small_modal_button.click()

    small_modal = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.modal-content'))
    )

    assert small_modal.is_displayed()

    browser.find_element(By.CSS_SELECTOR, '#closeSmallModal').click()

    WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, '.modal-content'))
    )

    large_modal_button = browser.find_element(By.CSS_SELECTOR, '#showLargeModal')
    large_modal_button.click()

    large_modal = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.modal-content'))
    )

    assert large_modal.is_displayed()

    browser.find_element(By.CSS_SELECTOR, '#closeLargeModal').click()

    WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, '.modal-content'))
    )