import os
from playwright.sync_api import sync_playwright

def capture_redesigns():
    # Use relative path for screenshots
    screenshot_dir = os.path.join(os.getcwd(), "redesign_screenshots")
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        current_dir = os.getcwd()
        file_path = f"file://{current_dir}/redesign_suggestions.html"
        page.goto(file_path)

        proposals = [
            "dash-1", "dash-2", "dash-3", "dash-4", "dash-5",
            "site-1", "site-2", "site-3", "site-4", "site-5"
        ]

        for pid in proposals:
            element = page.query_selector(f"#{pid}")
            if element:
                element.screenshot(path=os.path.join(screenshot_dir, f"{pid}.png"))
                print(f"Captured {pid}.png")
            else:
                print(f"Failed to find {pid}")

        page.screenshot(path=os.path.join(screenshot_dir, "full_overview.png"), full_page=True)
        print("Captured full_overview.png")

        browser.close()

if __name__ == "__main__":
    capture_redesigns()
