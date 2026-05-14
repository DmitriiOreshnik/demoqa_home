from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_alert(browser):
    browser.get('https://demoqa.com/alerts')

    timer_alert_button = browser.find_element(By.CSS_SELECTOR, '#timerAlertButton')

    assert timer_alert_button.is_displayed()

    timer_alert_button.click()

    WebDriverWait(browser, 10).until(EC.alert_is_present())

    alert = browser.switch_to.alert

    assert alert.text == 'This alert appeared after 5 seconds'

    alert.accept()