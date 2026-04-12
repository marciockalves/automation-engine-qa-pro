from playwright.sync_api import sync_playwright

def test_google_opening():
    with sync_playwright() as p:
        # Usamos o chromium nativo do container
        browser = p.chromium.launch(headless=False) 
        page = browser.new_page()
        page.goto("https://www.google.com")
        print(f"Título da página: {page.title()}")
        page.screenshot(path="debug_docker.png")
        browser.close()

if __name__ == "__main__":
    test_google_opening()