import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.delete_all_cookies()
    driver.quit()

@pytest.fixture(scope="session")
def user_data():
    return {
        "username":"1",
        "password":"1"
    }