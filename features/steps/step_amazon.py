from selenium.webdriver.support import expected_conditions as EC
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait


@given('User opens up Chrome')
def step_open_chrome(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

@then('User goes to Amazon')
def step_open_amazon(context):
    context.driver.get("https://www.amazon.com/")

# Below scripts are for scenario: Amazon - Find Selenium book and add to cart

@when('User clicks on search bar')
def step_search_bar(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').click()


@when('User searches for selenium book')
def step_impl(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('selenium book')
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then('Selects selenium book')
def step_impl(context):

    context.driver.implicitly_wait(10)
    context.driver.find_element(By.LINK_TEXT, 'Hands-On Selenium WebDriver with Java: '
                                              'A Deep Dive into the Development of '
                                              'End-to-End Tests').click()


@then('User is on the item page')
def step_impl(context):
    selenium_book = context.driver.find_element(By.ID, 'productTitle')
    actual_book_title = selenium_book.text
    expected_book_title = "Hands-On Selenium WebDriver with Java: " \
                          "A Deep Dive into the Development of End-to-End Tests"
    assert actual_book_title == expected_book_title, f'Actual = "{actual_book_title}",' \
                                                     f' Expected = "{expected_book_title}"'


@when('User clicks on Add to Cart')
def step_impl(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()


@when('User navigates to cart')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'Go to Cart').click()


@when('User Verifies selenium book is in cart')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'Hands-On Selenium WebDriver '
                                              'with Java: A Deep Dive into the '
                                              'Development of End-to-End Tests')

# Below scripts are for scenario: incorrectly attempt to create an account

@when('User clicks Account & Lists')
def step_impl(context):
    context.driver.find_element(By.ID, 'nav-link-accountList').click()


@then('User is on Sign in page')
def step_impl(context):
    signin = context.driver.find_element(By.XPATH, '//*[@id="authportal-main-section"]/div[2]/div[2]/div[1]/form/div/div/div/h1')
    actual_signin_title = signin.text
    expected_signin_title = "Sign in"
    assert actual_signin_title == expected_signin_title, f'Actual = "{actual_signin_title}",' \
                                                     f' Expected = "{expected_signin_title}"'


@when('User clicks Create your Amazon account')
def step_impl(context):
    context.driver.find_element(By.ID, 'createAccountSubmit').click()


@then('User is on Create account page')
def step_impl(context):
    create_account = context.driver.find_element(By.XPATH, '//*[@id="ap_register_form"]/div/div/h1')
    actual_create_account = create_account.text
    expected_create_account = "Create account"
    assert actual_create_account == expected_create_account, f'Actual = "{actual_create_account}",' \
                                                         f' Expected = "{expected_create_account}"'


@then('User clicks continue')
def step_impl(context):
    context.driver.find_element(By.ID, 'continue').click()


@then('Verifies error messages from incorrect entries')
def step_impl(context):
    for row in context.table:
        field_id = row['field']
        value = row['value']

        field_text = context.driver.find_element(By.ID, field_id)
        actual_field_text = field_text.text
        expected_field_text = value
        assert actual_field_text == expected_field_text


@when('User enters invalid email')
def step_impl(context):
    context.driver.find_element(By.ID, 'ap_email').send_keys('NotAnEmail')
    context.driver.find_element(By.ID, 'continue').click()



@then('Verifies error message for email')
def step_impl(context):
    #wait = WebDriverWait(context.driver, 100)
    email_error = context.driver.find_element(By.ID, 'auth-email-invalid-claim-alert')
    actual_email_error = email_error.text
    expected_email_error = 'Wrong or Invalid email address or mobile phone number. ' \
                           'Please correct and try again.'
    assert actual_email_error == expected_email_error, f'Actual = "{actual_email_error}",' \
                                                             f' Expected = "{expected_email_error}"'


@when('User enter mismatching passwords')
def step_impl(context):
    context.driver.find_element(By.ID, 'ap_password').send_keys('password1')
    context.driver.find_element(By.ID, 'ap_password_check').send_keys('password2')
    context.driver.find_element(By.ID, 'continue').click()



@then('Verifies error message for mismatching password')
def step_impl(context):
    password_error = context.driver.find_element(By.ID, 'auth-password-mismatch-alert')
    actual_password_error = password_error.text
    expected_password_error = 'Passwords must match'
    assert actual_password_error == expected_password_error, f'Actual = "{actual_password_error}",' \
                                                       f' Expected = "{expected_password_error}"'


@when('User enters an improper password')
def step_impl(context):
    context.driver.find_element(By.ID, 'ap_password').clear()
    context.driver.find_element(By.ID, 'ap_password').send_keys('badpw')
    context.driver.find_element(By.ID, 'continue').click()


@then('Verifies error message for improper password')
def step_impl(context):
    password_invalid = context.driver.find_element(By.ID, 'auth-password-invalid-password-alert')
    actual_password_invalid = password_invalid.text
    expected_password_invalid = 'Minimum 6 characters required'
    assert actual_password_invalid == expected_password_invalid, f'Actual = "{actual_password_invalid}",' \
                                                             f' Expected = "{expected_password_invalid}"'

# Below scripts are for scenario: Amazon - Validate text on item

@when('User searches for Python Selenium book')
def step_impl(context):
    context.driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Python Selenium Book")
    context.driver.find_element(By.ID, "nav-search-submit-button").click()


@when('User selects a Python Selenium book')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Test-Driven Development with Python: "
                                              "Obey the Testing Goat: "
                                              "Using Django, Selenium, and JavaScript").click()


@when('Clicks on Read more')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Read more").click()


@then('User validates Title and Author on item page')
def step_impl(context):
    for row in context.table:
        field_id = row['field']
        value = row['value']

        field_text = context.driver.find_element(By.ID, field_id)
        actual_field_text = field_text.text
        expected_field_text = value
        assert actual_field_text == expected_field_text, f'Actual = "{actual_field_text}",' \
                                                             f' Expected = "{expected_field_text}"'

@then('User validates book description')
def step_impl(context):
    for row in context.table:
        field_id = row['xpath']
        value = row['text']

        field_text = context.driver.find_element(By.XPATH, field_id)
        actual_field_text = field_text.text
        expected_field_text = value
        assert actual_field_text == expected_field_text, f'Actual = "{actual_field_text}",' \
                                                         f' Expected = "{expected_field_text}"'

@then('User validates preface')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[contains(text(), 'From the Preface')]")


