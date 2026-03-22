from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def check_if_product_in_cart(self, productName):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//td[text()='{productName}']")))
        self.driver.find_element(By.XPATH, f"//td[text()='{productName}']")


    
    