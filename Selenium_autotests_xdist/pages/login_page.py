from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:

    LOGIN_USERNAME_FIELD = (By.ID, "loginusername")
    LOGIN_PASSWORD_FIELD = (By.ID, "loginpassword")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Log in']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
   
    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_USERNAME_FIELD))
        self.driver.find_element(*self.LOGIN_USERNAME_FIELD).send_keys(username)
        
    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_PASSWORD_FIELD))
        self.driver.find_element(*self.LOGIN_PASSWORD_FIELD).send_keys(password)
    
    def submit_login(self):
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_SUBMIT_BUTTON))
        self.driver.find_element(*self.LOGIN_SUBMIT_BUTTON).click()

    
    