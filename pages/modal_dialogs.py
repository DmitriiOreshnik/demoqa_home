from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ModalDialogs(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = 'https://demoqa.com/modal-dialogs'

    def submenu_buttons(self):
        buttons = self.driver.find_elements(By.CSS_SELECTOR, 'div.element-list li')
        return [button for button in buttons if button.is_displayed()]

    def icon_home(self):
        return self.find_element(locator='header a')

    def click_icon_home(self):
        self.driver.execute_script("arguments[0].click();", self.icon_home())

    def check_url(self):
        assert self.driver.current_url == 'https://demoqa.com/'

    def check_title(self):
        assert self.driver.title == 'demosite'