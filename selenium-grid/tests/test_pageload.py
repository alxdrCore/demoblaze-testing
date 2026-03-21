from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_mainpage_load(driver):
    driver.get("https://demoblaze.com")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[text()='About us']"))
    )

    aboutus_text = driver.find_element(By.XPATH, "//a[text()='About us']").text

    assert "About us" in aboutus_text 
