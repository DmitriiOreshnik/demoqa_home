from selenium.webdriver.common.by import By


class BaseComponent:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def get_text(self):
        return str(self.find_element().text)