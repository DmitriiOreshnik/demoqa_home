from selenium.webdriver.common.by import By


def test_login_form_validate(browser):
    browser.get('https://demoqa.com/automation-practice-form')

    first_name = browser.find_element(By.CSS_SELECTOR, '#firstName')
    last_name = browser.find_element(By.CSS_SELECTOR, '#lastName')
    user_email = browser.find_element(By.CSS_SELECTOR, '#userEmail')
    form = browser.find_element(By.CSS_SELECTOR, '#userForm')
    submit = browser.find_element(By.CSS_SELECTOR, '#submit')

    assert first_name.get_attribute('placeholder') == 'First Name'
    assert last_name.get_attribute('placeholder') == 'Last Name'
    assert user_email.get_attribute('placeholder') == 'name@example.com'
    assert user_email.get_attribute('pattern') == '^([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+)\\.([a-zA-Z]{2,5})$'

    browser.execute_script("arguments[0].click();", submit)

    assert 'was-validated' in form.get_attribute('class')