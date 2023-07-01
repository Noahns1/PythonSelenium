from behave import *
from selenium import webdriver

# python -m behave features\test_drive.feature

@given('launch chrome browser')
def launchBrowser(context):
    context.driver=webdriver.Chrome()


@when('open google')
def openGoogle(context):
    context.driver.get("https://www.google.com/")

@then('close browser')
def closeBrowser(context):
    context.driver.close()