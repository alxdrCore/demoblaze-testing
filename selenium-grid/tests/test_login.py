from pages.login_page import LoginPage
from pages.main_page import MainPage
from Utils.alerts_actions import AlertsActions

def test_login_wrong_password(driver, user_data, base_url):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    alerts_actions = AlertsActions(driver)

    main_page.open_page(base_url)
    main_page.click_login_button()

    login_page.enter_username(user_data["username"])
    login_page.enter_password("WRONG-PASSWORD1!")
    login_page.submit_login()

    alert_text = alerts_actions.get_alert_text()
    alerts_actions.accept_alert()

    assert "Wrong password" in alert_text

def test_login_success(driver, user_data, base_url):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)

    main_page.open_page(base_url)
    main_page.click_login_button()
    
    login_page.enter_username(user_data["username"])
    login_page.enter_password(user_data["password"])
    login_page.submit_login()

    welcome = main_page.get_welcome_text()

    assert user_data["username"] in welcome, f"Неправильный юзер, оне не {user_data["username"]}! Получено : {welcome}"