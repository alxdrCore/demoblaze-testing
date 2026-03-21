from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_cart(driver):
    driver.get("https://demoblaze.com")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[text()='Monitors']"))
    )

    driver.find_element(By.XPATH, "//a[text()='Monitors']").click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[text()='Apple monitor 24']"))
    )

    driver.find_element(By.XPATH, "//a[text()='Apple monitor 24']").click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[text()='Add to cart']"))
    )

    driver.find_element(By.XPATH, "//a[text()='Add to cart']").click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    driver.find_element(By.ID, "cartur").click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//td[text()='Apple monitor 24']"))
    )

    monitor = driver.find_element(By.XPATH, "//td[text()='Apple monitor 24']").text

    print("Тест успешно пройден")
