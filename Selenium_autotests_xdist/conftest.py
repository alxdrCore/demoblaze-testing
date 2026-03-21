import pytest
from selenium import webdriver

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
        "username":"1",
        "password":"1"
    }

@pytest.fixture(autouse=True)
def clear_coockies(driver):
    driver.delete_all_cookies()
    yield
    driver.delete_all_cookies()
