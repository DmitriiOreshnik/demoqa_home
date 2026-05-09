from pages.base_page import BasePage


class Accordion(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = 'https://demoqa.com/accordian'

    def section1_content(self):
        return self.find_element(
            locator='div.accordion-item:first-child div.accordion-body p'
        )

    def section1_heading(self):
        return self.find_element(
            locator='div.accordion-item:first-child .accordion-header'
        )

    def section2_content_first(self):
        return self.find_element(
            locator='div.accordion-item:nth-child(2) p:nth-child(1)'
        )

    def section2_content_second(self):
        return self.find_element(
            locator='div.accordion-item:nth-child(2) p:nth-child(2)'
        )

    def section3_content(self):
        return self.find_element(
            locator='div.accordion-item:nth-child(3) p'
        )