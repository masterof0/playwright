import os
import pytest
from playwright.sync_api import Playwright, Browser, expect, sync_playwright

baseUrl = os.getenv("BASE_URL")


def test_context(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(
        headless=False, args=["--ignore-certificate-errors"], slow_mo=1000
    )
    context = browser.new_context(storage_state="tests/.auth/state.json")
    page = context.new_page()
    page.goto(f"{baseUrl}/settings")
    expect(page.get_by_role("tab", name="Vectra MDR News")).to_be_visible()
    # page.wait_for_timeout(5000)
    # browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
