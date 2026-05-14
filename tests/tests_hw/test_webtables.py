from selenium.webdriver.support.select import Select

from pages.webtables import WebTables


def test_webtables_crud(browser):
    webtables = WebTables(browser)
    webtables.visit()

    first_name = 'Ivan'
    last_name = 'Petrov'
    email = 'ivan.petrov@test.com'
    age = '30'
    salary = '100000'
    department = 'QA'

    webtables.add_button().click()

    webtables.submit_button().click()
    assert 'was-validated' in webtables.registration_form().get_attribute('class')

    webtables.fill_form(first_name, last_name, email, age, salary, department)
    webtables.submit_button().click()

    assert webtables.table_contains_text(email)
    assert webtables.table_contains_text(first_name)

    browser.execute_script(
        "arguments[0].click();",
        webtables.edit_buttons()[-1]
    )

    assert webtables.first_name().get_attribute('value') == first_name
    assert webtables.last_name().get_attribute('value') == last_name
    assert webtables.user_email().get_attribute('value') == email

    updated_name = 'Petr'

    webtables.first_name().clear()
    webtables.first_name().send_keys(updated_name)

    webtables.submit_button().click()

    assert webtables.table_contains_text(updated_name)

    browser.execute_script(
        "arguments[0].click();",
        webtables.delete_buttons()[-1]
    )

    assert not webtables.table_contains_text(updated_name)


def test_webtables_pagination(browser):
    webtables = WebTables(browser)
    webtables.visit()

    assert webtables.current_page() == '1'
    assert webtables.total_pages() == '1'

    assert webtables.previous_button().get_attribute('disabled')
    assert webtables.next_button().get_attribute('disabled')

    users = []

    for i in range(8):
        users.append(
            (
                f'Ivan{i}',
                'Petrov',
                f'ivan{i}@test.com',
                '30',
                '100000',
                'QA'
            )
        )

    for user in users:
        webtables.add_button().click()
        webtables.fill_form(*user)
        webtables.submit_button().click()

    assert webtables.total_pages() == '2'
    assert not webtables.next_button().get_attribute('disabled')

    browser.execute_script("arguments[0].click();", webtables.next_button())
    assert webtables.current_page() == '2'

    browser.execute_script("arguments[0].click();", webtables.previous_button())
    assert webtables.current_page() == '1'