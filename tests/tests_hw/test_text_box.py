from selenium.webdriver.common.by import By


def test_text_box(browser):
    browser.get('https://demoqa.com/text-box')

    full_name = 'Ivan Ivanov'
    current_address = 'Moscow, Test street, 10'

    browser.find_element(By.CSS_SELECTOR, '#userName').send_keys(full_name)
    browser.find_element(By.CSS_SELECTOR, '#currentAddress').send_keys(current_address)

    browser.execute_script("arguments[0].click();", browser.find_element(By.CSS_SELECTOR, '#submit'))

    output_name = browser.find_element(By.CSS_SELECTOR, '#output #name')
    output_address = browser.find_element(By.CSS_SELECTOR, '#output #currentAddress')

    assert full_name in output_name.text
    assert current_address in output_address.text