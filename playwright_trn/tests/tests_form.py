from playwright.sync_api import sync_playwright

def test_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the local web application
        page.goto('http://127.0.0.1:5000')

        # Check if the content contains 'Hello, Docker!'
        assert "Hello, Docker!" in page.content()

        browser.close()

if __name__ == "__main__":
    test_homepage()