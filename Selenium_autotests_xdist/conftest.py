import pytest
from selenium import webdriver

BASE_URL = "https://demoblaze.com"
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

@pytest.fixture(scope="session")
def user_data():
    return {
        "username": LOGIN_USERNAME,
        "password":LOGIN_PASSWORD
    }

@pytest.fixture(autouse=True)
def clear_cookies(driver):
    driver.delete_all_cookies()
    yield
    driver.delete_all_cookies()

@pytest.fixture(scope="session")
def product_name():
    return PRODUCT_NAME

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL