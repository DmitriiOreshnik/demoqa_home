import time

from pages.accordion import Accordion


def test_visible_accordion(browser):
    accordion = Accordion(browser)

    accordion.visit()

    assert accordion.section1_content().is_displayed()

    accordion.section1_heading().click()

    time.sleep(2)

    assert not accordion.section1_content().is_displayed()


def test_visible_accordion_default(browser):
    accordion = Accordion(browser)

    accordion.visit()

    assert not accordion.section2_content_first().is_displayed()
    assert not accordion.section2_content_second().is_displayed()
    assert not accordion.section3_content().is_displayed()