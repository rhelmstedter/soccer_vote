from playwright.sync_api import sync_playwright, Playwright, TimeoutError
import time

GIRLS_URL = "https://www.vcstar.com/story/sports/high-school/2026/03/11/vote-for-the-top-high-school-girls-soccer-player-in-the-area/89103016007/"
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    try:
        page.goto(GIRLS_URL, timeout=2000)
    except TimeoutError:
        pass
    page.mouse.wheel(0, 1000)
    time.sleep(.5)
    page.mouse.wheel(0, 1000)
    iframe_locator = page.frame_locator(r'iframe[title="Embedded reader poll - Fans Choice: Who is Ventura County\'s No. 1 girls soccer player?"]')
    iframe_locator.get_by_label('Carmen Sanchez, Del Sol').click()
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
