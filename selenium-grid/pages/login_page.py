from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:

    LOGIN_BUTTON = (By.ID, "login2")
    LOGIN_USERNAME_FIELD = (By.ID, "loginusername")
    LOGIN_PASSWORD_FIELD = (By.ID, "loginpassword")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Log in']")
    WELCOME_TEXT = (By.ID, "nameofuser")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open(self):
        self.driver.get("https://demoblaze.com")
    
    def click_login_button(self, username):
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_BUTTON))
        self.driver.find_element(*self.LOGIN_BUTTON).click()
    
    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_USERNAME_FIELD))
        self.driver.find_element(*self.LOGIN_USERNAME_FIELD).send_keys(username)
        
    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_PASSWORD_FIELD))
        self.driver.find_element(*self.LOGIN_USERNAME_FIELD).send_keys(password)
    
    def submit_login(self):
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_SUBMIT_BUTTON))
        self.driver.find_element(*self.LOGIN_SUBMIT_BUTTON).click()

    def get_welcome_text(self):
        self.wait.until(EC.visibility_of_element_located(self.WELCOME_TEXT))
        return self.driver.find_element(*self.WELCOME_TEXT).text
    
    def get_alert_text(self):
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        return alert_text
    
    def accept_alert(self):
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
         
    
    