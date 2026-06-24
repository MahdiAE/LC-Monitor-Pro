import os
import sys
from playwright.sync_api import sync_playwright

def sanity_check():
    # Attempt to find the target HTML file
    current_dir = os.getcwd()
    target_files = [f for f in os.listdir(current_dir) if f.startswith("LC Monitor Pro v57") and f.endswith(".html")]

    if not target_files:
        print("No 'LC Monitor Pro v57' HTML file found in current directory.")
        return False

    # Use the most recent if multiple (sorted by name should work for the timestamped ones)
    file_name = sorted(target_files)[-1]
    file_path = f"file://{current_dir}/{file_name}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        errors = []
        page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda err: errors.append(err.message))

        print(f"Loading {file_name}...")
        try:
            page.goto(file_path, wait_until="networkidle")
            print("Page loaded successfully.")
        except Exception as e:
            print(f"Failed to load page: {e}")
            browser.close()
            return False

        if errors:
            print("Console errors detected:")
            for err in errors:
                print(f" - {err}")
        else:
            print("No console errors detected.")

        sidebar = page.query_selector(".sidebar")
        if sidebar:
            print("App UI (sidebar) detected.")
        else:
            print("App UI (sidebar) NOT detected.")

        browser.close()
        return True

if __name__ == "__main__":
    success = sanity_check()
    if not success:
        sys.exit(1)
