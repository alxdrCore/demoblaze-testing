from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


class ProductPage:

    BUTTON_ADD_TO_CART = (By.XPATH, "//a[text()='Add to cart']")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_add_to_cart(self):
        self.wait.until(EC.visibility_of_element_located(self.BUTTON_ADD_TO_CART))
        self.driver.find_element(*self.BUTTON_ADD_TO_CART).click()
