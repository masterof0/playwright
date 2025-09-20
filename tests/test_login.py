import os
import pytest
from playwright.sync_api import Playwright, Browser, expect, sync_playwright

baseUrl = os.getenv("BASE_URL")


@pytest.mark.login
@pytest.mark.order(1)
def test_login(playwright: Playwright) -> None:
    playwright.selectors.set_test_id_attribute("data-cy")
    browser = playwright.chromium.launch(
        headless=False, args=["--ignore-certificate-errors"], slow_mo=1000
    )
    context = browser.new_context()
    page = context.new_page()
    # page.goto("http://localhost:8080/")
    if baseUrl:
        page.goto(baseUrl)
    else:
        pytest.exit("BASE_URL is not defined")
    expect(page.get_by_role("button", name="Local Dev Log in")).to_be_visible()
    page.get_by_test_id("logIn").click()
    expect(page.get_by_text("Choose a Role")).to_be_visible()
    page.get_by_role("dialog").get_by_test_id("confirmRole").click()
    # page.wait_for_timeout(5000)

    context.storage_state(path="tests/.auth/state.json")

    # ---------------------
    browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
