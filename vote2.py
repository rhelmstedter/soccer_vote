import time
import pyautogui as pag
import webbrowser


def vote():
    WIDTH, HEIGHT = pag.size()
    pag.moveTo(WIDTH // 2, HEIGHT // 2)
    for _ in range(5):
        time.sleep(.5)
        pag.scroll(-10)

    player = pag.locateCenterOnScreen("./player.png")
    pag.moveTo(player)
    time.sleep(.6)
    pag.click()
    time.sleep(.6)
    pag.scroll(-10)
    vote = pag.locateCenterOnScreen("./vote.png")
    pag.moveTo(vote)
    pag.click()
    time.sleep(3)


while True:
    webbrowser.open("https://www.vcstar.com/story/sports/high-school/2026/02/03/vote-for-the-top-boys-soccer-player-in-the-area/88497911007/")
    try:
        vote()
    except pag.ImageNotFoundException:
        time.sleep(2)
    pag.keyDown("command")
    pag.press("w")
    pag.keyUp("command")
