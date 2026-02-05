from playwright.sync_api import sync_playwright, Playwright, TimeoutError
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    try:
        page.goto("https://www.vcstar.com/story/sports/high-school/2026/02/03/vote-for-the-top-boys-soccer-player-in-the-area/88497911007/",
                  timeout=3000)
    except TimeoutError:
        pass
    page.mouse.wheel(0, 1000)
    time.sleep(1)
    page.mouse.wheel(0, 1000)
    time.sleep(1)
    page.mouse.wheel(0, 1000)
    time.sleep(5)
    page.get_by_role("radio", name="PDI_answer16573377").check()
    page.locator("text=Vote").click()
    # browser.close()


with sync_playwright() as playwright:
    run(playwright)
