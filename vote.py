from playwright.sync_api import sync_playwright, Playwright, TimeoutError
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    try:
        page.goto("https://www.vcstar.com/story/sports/high-school/2026/02/03/vote-for-the-top-boys-soccer-player-in-the-area/88497911007/",
                  timeout=2000)
    except TimeoutError:
        pass
    page.mouse.wheel(0, 1000)
    time.sleep(.5)
    page.mouse.wheel(0, 1000)
    iframe_locator = page.frame_locator(r'iframe[title="Embedded reader poll - Fans Choice: Who is Ventura County\'s No. 1 boys soccer player?"]')
    iframe_locator.get_by_label('Cesar Fonseca, Del Sol').click()
    iframe_locator.get_by_role("button").click()
    time.sleep(1)
    browser.close()


count = 0
while True:
    for _ in range(10):
        with sync_playwright() as playwright:
            run(playwright)
        count += 1
        print(f"Votes: {count}", end="\r")
    time.sleep(300)
