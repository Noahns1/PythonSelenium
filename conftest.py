import pytest
from selenium import webdriver

@pytest.fixture
def browser(context):
    context.browser = webdriver.Firefox() # or webdriver.Chrome()
    yield context.browser
    context.browser.quit()