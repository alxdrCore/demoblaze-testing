import pytest
from selenium import webdriver

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

@pytest.fixture()
def user_data():
    return {
        "username":"1",
        "password":"1"
    }

@pytest.fixture(autouse=True)
def clear_coockies(driver):
    driver.delete_all_cookies()
    yield
    driver.delete_all_cookies()