from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from Utils.alerts_actions import AlertsActions

def test_add_to_cart(driver, product_name):
    main_page = MainPage(driver)

    main_page.open_page()
    main_page.click_on_product(product_name)

    product_page = ProductPage(driver)

    product_page.click_add_to_cart()

    alerts_system = AlertsActions(driver)
    
    alert_text = alerts_system.get_alert_text()
    assert "Product added" in alert_text
    alerts_system.accept_alert()

    main_page.click_cart_page()

    cart_page = CartPage(driver)

    cart_page.check_if_product_in_cart(product_name)
    
