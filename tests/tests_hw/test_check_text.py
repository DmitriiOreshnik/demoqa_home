from pages.base_page import BasePage
from components.base_component import BaseComponent
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_footer_text(driver):
    page = BasePage(driver)

    page.base_url = 'https://demoqa.com/'
    page.visit()

    footer = BaseComponent(driver, 'footer span')

    assert footer.get_text() == '© 2013-2026 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_check_center_text(driver):
    page = BasePage(driver)

    page.base_url = 'https://demoqa.com/'
    page.visit()

    elements = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.card.mt-4.top-card'))
    )

    driver.execute_script("arguments[0].scrollIntoView();", elements)
    driver.execute_script("arguments[0].click();", elements)

    center_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[text()='Please select an item from left to start practice.']")
        )
    )

    assert center_text.text == 'Please select an item from left to start practice.'