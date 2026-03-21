from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

class MainPage:

    BUTTON_LOGIN = (By.ID, "login2")
    WELCOME_TEXT = (By.ID, "nameofuser")
    BUTTON_CART = (By.ID, "cartur")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_page(self):
        self.driver.get("https://demoblaze.com")

    def click_login_button(self):
        self.wait.until(EC.visibility_of_element_located(self.BUTTON_LOGIN))
        self.driver.find_element(*self.BUTTON_LOGIN).click()
    
    def get_welcome_text(self):
        self.wait.until(EC.visibility_of_element_located(self.WELCOME_TEXT))
        return self.driver.find_element(*self.WELCOME_TEXT).text
    
    def click_on_product(self, productName):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[text()='{productName}']")))
        self.driver.find_element(By.XPATH, f"//a[text()='{productName}']").click()

    def click_cart_page(self):
        self.wait.until(EC.visibility_of_element_located(self.BUTTON_CART))
        self.driver.find_element(*self.BUTTON_CART).click()
        
    
    
    