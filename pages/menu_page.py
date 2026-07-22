from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib3.util import wait


class MenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.coworking_booking = (By.CSS_SELECTOR, "#app > div > div.home-content > div > div > div.container.container_mobile > div > div.home-eduV2__reminders > div.home-eduV2__reminders-block > div:nth-child(1) > div.home-eduV2__reminders-coworking > div.flex.column.gap10.jcsb > div.home-eduV2__reminders-action.flex.column > div > div.list-tile__trailing")
        self.group = (By.CSS_SELECTOR, "#app > div > div.home-content > div > div > div.container.container_mobile > div > div.home-eduV2__groups > div.home-eduV2__groups-cards > div > div.home-eduV2__groups-cards-card-bot > div.flex.jcsb.aic.gap15 > div.go-btn")
        self.videos = (By.CSS_SELECTOR, "#tabbar > div > div.tab-header > div.tab-header__wrapper > div:nth-child(2)")
        self.lesson28 = (By.CSS_SELECTOR, "#app > div > div.container.container_mobile > div > div > div.new-lessons_content > div > div:nth-child(5) > div.flex.gap20 > div:nth-child(4) > div.lesson-card > div > div.lesson-card-left > div.lesson-card-left_actions > button")
        self.btn_profile = (By.CSS_SELECTOR, "#app > div > div.header > div > div.header__avatar.pointer.flex.gap5")
        self.btn_exit = (By.CSS_SELECTOR, "#app > div > div.user-container > div > div > div.relative.w100p > div.flex.column.gap15.w100p.relative > div:nth-child(6) > div > div")
        self.btn_exit_y = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-actions > button:nth-child(2) > span")
        self.go_coworking = (By.CSS_SELECTOR, "#app > div > div.home-content > div > div > div.container.container_mobile > div > div.home-eduV2__reminders > div.home-eduV2__reminders-block > div:nth-child(1) > div.flex.aic.jcsb.mb10 > div")
        self.go_home = (By.CSS_SELECTOR, "#app > div > div.layout > div > div > div.desktop-navigation__icons > ul > li:nth-child(1)")

    def click_coworking_booking(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.coworking_booking)).click()

    def click_group(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.group)).click()

    def click_videos(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.videos)).click()

    def click_lesson28(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.lesson28)).click()

    def click_btn_profile(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_profile)).click()

    def click_btn_exit(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_exit)).click()

    def click_btn_y(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_exit_y)).click()

    def click_go_coworking(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.go_coworking)).click()

    def click_go_home(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.go_home)).click()