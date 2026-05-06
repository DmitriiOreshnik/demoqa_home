from pages.swag_labs import SwagLabs


def test_check_icon(driver):
    swag_labs = SwagLabs(driver)
    swag_labs.visit()
    assert swag_labs.exist_icon()


def test_check_username(driver):
    swag_labs = SwagLabs(driver)
    swag_labs.visit()
    assert swag_labs.find_element(locator='input#user-name')


def test_check_password(driver):
    swag_labs = SwagLabs(driver)
    swag_labs.visit()
    assert swag_labs.find_element(locator='input#password')