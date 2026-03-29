from pages.main_page import MainPage

def test_mainpage_load(driver, base_url):
    main_page = MainPage(driver)

    main_page.open_page(base_url)

    main_page.click_cart_page()
