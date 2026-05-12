from pages.modal_dialogs import ModalDialogs


def test_modal_elements(browser):
    modal_dialogs = ModalDialogs(browser)

    modal_dialogs.visit()

    assert len(modal_dialogs.submenu_buttons()) == 5


def test_navigation_modal(browser):
    modal_dialogs = ModalDialogs(browser)

    modal_dialogs.visit()

    browser.refresh()

    modal_dialogs.click_icon_home()

    browser.back()

    browser.set_window_size(900, 400)

    browser.forward()

    modal_dialogs.check_url()
    modal_dialogs.check_title()

    browser.set_window_size(1000, 1000)