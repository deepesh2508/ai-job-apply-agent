from playwright.sync_api import sync_playwright
from form_filler import handle_steps
from config import AUTO_SUBMIT

def run():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]
        page = context.pages[0]

        print("Connected to browser")

        handle_steps(page)

        # Submit
        if AUTO_SUBMIT:
            page.click("button:has-text('Submit application')")
            print("Application submitted ✅")
        else:
            input("Review karo, Enter dabao submit ke liye...")
            page.click("button:has-text('Submit application')")

run()