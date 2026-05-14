from selenium.webdriver.common.by import By


class WebTables:

    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://demoqa.com/webtables'

    def visit(self):
        self.driver.get(self.url)

    def find_element(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def find_elements(self, locator):
        return self.driver.find_elements(By.CSS_SELECTOR, locator)

    def add_button(self):
        return self.find_element('#addNewRecordButton')

    def submit_button(self):
        return self.find_element('#submit')

    def registration_form(self):
        return self.find_element('#userForm')

    def first_name(self):
        return self.find_element('#firstName')

    def last_name(self):
        return self.find_element('#lastName')

    def user_email(self):
        return self.find_element('#userEmail')

    def age(self):
        return self.find_element('#age')

    def salary(self):
        return self.find_element('#salary')

    def department(self):
        return self.find_element('#department')

    def fill_form(self, first_name, last_name, email, age, salary, department):
        self.first_name().clear()
        self.first_name().send_keys(first_name)

        self.last_name().clear()
        self.last_name().send_keys(last_name)

        self.user_email().clear()
        self.user_email().send_keys(email)

        self.age().clear()
        self.age().send_keys(age)

        self.salary().clear()
        self.salary().send_keys(salary)

        self.department().clear()
        self.department().send_keys(department)

    def table_text(self):
        return self.driver.find_element(By.TAG_NAME, 'body').text

    def edit_buttons(self):
        return self.find_elements('span[title="Edit"]')

    def delete_buttons(self):
        return self.find_elements('span[title="Delete"]')

    def rows_dropdown(self):
        return self.find_element('select')

    def next_button(self):
        return self.driver.find_element(By.XPATH, '//button[text()="Next"]')

    def previous_button(self):
        return self.driver.find_element(By.XPATH, '//button[text()="Previous"]')

    def current_page(self):
        text = self.table_text()

        if 'Page 2 of' in text:
            return '2'

        return '1'

    def total_pages(self):
        text = self.table_text()

        if 'Page 1 of 2' in text or 'Page 2 of 2' in text:
            return '2'

        return '1'

    def table_contains_text(self, text):
        return text in self.table_text()