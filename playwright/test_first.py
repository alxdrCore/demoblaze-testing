from playwright.sync_api import sync_playwright

def test_open_demoblaze():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://demoblaze.com")
        
        print(page.title())
        assert "STORE" in page.title()
        
        browser.close