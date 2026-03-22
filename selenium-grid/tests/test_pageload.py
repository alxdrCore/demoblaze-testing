from pages.main_page import MainPage

def test_mainpage_load(driver):
    main_page = MainPage(driver)

    main_page.open_page()

    main_page.click_cart_page()
