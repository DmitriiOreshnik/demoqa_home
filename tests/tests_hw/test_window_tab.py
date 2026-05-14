from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_window_tab(browser):
    browser.get('https://demoqa.com/links')

    home_link = browser.find_element(By.CSS_SELECTOR, '#simpleLink')

    assert home_link.text == 'Home'
    assert home_link.get_attribute('href') == 'https://demoqa.com/'

    old_tabs = browser.window_handles

    home_link.click()

    WebDriverWait(browser, 10).until(
        lambda driver: len(driver.window_handles) > len(old_tabs)
    )

    new_tabs = browser.window_handles

    assert len(new_tabs) == len(old_tabs) + 1