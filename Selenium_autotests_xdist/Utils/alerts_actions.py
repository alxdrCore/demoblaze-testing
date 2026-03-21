from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class AlertsActions:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
   
    def get_alert_text(self):
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        return alert_text
    
    def accept_alert(self):
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
         
    
    