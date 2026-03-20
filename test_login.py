from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_wrong_password(driver, user_data):
    driver.get("https://demoblaze.com")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "login2"))
    )
    driver.find_element(By.ID, "login2").click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "loginusername"))
    )

    driver.find_element(By.ID, "loginusername").send_keys(user_data["username"])
    driver.find_element(By.ID, "loginpassword").send_keys("!!!!!!!!!!!!")
    driver.find_element(By.XPATH, "//button[text()='Log in']").click()

    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    alert.accept()

    assert "Wrong password" in alert_text

def test_login_success(driver, user_data):
    driver.get("https://demoblaze.com")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "login2"))
    )

    driver.find_element(By.ID, "login2").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "loginusername"))
    )

    driver.find_element(By.ID, "loginusername").send_keys(user_data["username"])
    driver.find_element(By.ID, "loginpassword").send_keys(user_data["password"])
    driver.find_element(By.XPATH, "//button[text()='Log in']").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "nameofuser"))
    )

    welcome = driver.find_element(By.ID, "nameofuser").text

    assert "1" in welcome, f"Неправильный юзер, оне не '1'! Получено : {welcome}"
    print(welcome)