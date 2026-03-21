import pytest
from selenium import webdriver

PRODUCT_NAME = "Nokia lumia 1520"
LOGIN_USERNAME = "1"
LOGIN_PASSWORD = "1"

@pytest.fixture(params=["firefox", "chrome"], scope="function")
def driver(request):
    if request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "chrome":
        driver = webdriver.Chrome()
    yield driver
    driver.delete_all_cookies()
    driver.quit()

@pytest.fixture(scope="function")
def user_data():
    return {
        "username": LOGIN_USERNAME,
        "password":LOGIN_PASSWORD
    }

@pytest.fixture(autouse=True)
def clear_coockies(driver):
    driver.delete_all_cookies()
    yield
    driver.delete_all_cookies()

@pytest.fixture(scope="function")
def product_name():
    return PRODUCT_NAME