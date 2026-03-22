import pytest
from selenium import webdriver

PRODUCT_NAME = "Nokia lumia 1520"
LOGIN_USERNAME = "1"
LOGIN_PASSWORD = "1"

@pytest.fixture(params=["firefox", "chrome"])
def driver(request):
    options = None
    if request.param == "firefox":
        options = webdriver.FirefoxOptions()
    elif request.param == "chrome":
        options = webdriver.ChromeOptions()

    driver = webdriver.Remote(
        command_executor="http://localhost:4444",
        options=options
    )

    yield driver
    driver.delete_all_cookies()
    driver.quit()

@pytest.fixture(scope="function")
def user_data():
    return {
        "username" : LOGIN_USERNAME,
        "password" : LOGIN_PASSWORD
    }

@pytest.fixture()
def product_name():
    return PRODUCT_NAME

@pytest.fixture(autouse=True)
def clear_coockies(driver):
    driver.delete_all_cookies()
    yield
    driver.delete_all_cookies()