from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


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

@when(u'User clicks Account & Lists')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User clicks Account & Lists')


@then(u'User is on Sign in page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User is on Sign in page')


@when(u'User clicks Create your Amazon account')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User clicks Create your Amazon account')


@then(u'User is on Create account page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User is on Create account page')


@then(u'User clicks continue')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User clicks continue')


@then(u'Verifies error messages from incorrect entries')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Verifies error messages from incorrect entries')


@when(u'User enters invalid email')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enters invalid email')


@then(u'Verifies error message for email')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Verifies error message for email')


@when(u'User enter mismatching passwords')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enter mismatching passwords')


@then(u'Verifies error message for mismatching password')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Verifies error message for mismatching password')


@when(u'User enters an improper password')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enters an improper password')


@then(u'Verifies error message for improper password')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Verifies error message for improper password')