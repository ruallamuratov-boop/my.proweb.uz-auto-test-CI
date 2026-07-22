from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib3.util import wait

class VideoPage:
    def __init__(self, driver):
        self.driver = driver
        self.later = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-actions > div > button:nth-child(1)")
        self.play_vid = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(2) > div.hidden > div > div.video-player-proweb__wrapper > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-left > button")
        self.full_scr = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(2) > div.hidden > div > div.video-player-proweb__wrapper > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button:nth-child(3) > span")
        self.scr_tap = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(2) > div.hidden > div > div.video-player-proweb__wrapper > div.video-player-proweb__actinview")
        self.full_scr_ext = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(2) > div.hidden > div > div.video-player-proweb__wrapper > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button:nth-child(3) > span")
        self.vote = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div.videolesson__general-footer-rating.mt10 > div > div > div > div > span:nth-child(5)")
        self.vote_send = (By.CSS_SELECTOR, "#dialog > div > div > div > div > div > button")

    def click_later(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.element_to_be_clickable(self.later)).click()

    def click_play_vid(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.play_vid)).click()

    def click_full_scr(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.full_scr)).click()

    def click_scr_tap(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.scr_tap)).click()

    def click_full_scr_ext(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.full_scr_ext)).click()

    def click_vote(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.vote)).click()

    def click_vote_send(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.vote_send)).click()