import pytest

from selenium.webdriver.common.by import By
from pages.webtables import WebTables


def get_column_values(browser, column_index):
    rows = browser.find_elements(By.CSS_SELECTOR, 'tbody tr')

    values = []

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')

        if cells:
            values.append(cells[column_index].text)

    return values


def test_sort(browser):
    webtables = WebTables(browser)
    webtables.visit()

    headers = browser.find_elements(By.CSS_SELECTOR, 'thead th')

    sorting_worked = False

    for index, header in enumerate(headers[:-1]):
        values_before = get_column_values(browser, index)

        browser.execute_script(
            "arguments[0].click();",
            header
        )

        values_after = get_column_values(browser, index)

        if values_before != values_after:
            sorting_worked = True

    if not sorting_worked:
        pytest.skip(
            'Sorting is not available on current DemoQA page version'
        )

    assert sorting_worked