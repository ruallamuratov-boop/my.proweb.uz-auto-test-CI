from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
from urllib3.util import wait

class CoworkingPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkbox_selector = (By.CSS_SELECTOR,".coworking__page-dialog-rules-check label button")
        self.btn_next = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-actions > button:nth-child(2)")
        self.aybek2 = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div.stepper-body > div > div > div > div.coworking__page-dialog-follow-branch > div:nth-child(2) > div.list-tile.coworking__page-dialog-follow-branch-item-list")
        self.btn_select1 = (By.CSS_SELECTOR, "#dialog > div.material-dialog.coworking__branch-dialog > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div > div:nth-child(1) > div.list-tile__trailing")
        self.btn_confirm_select1 = (By.CSS_SELECTOR, "#dialog > div.material-dialog.coworking__branch-dialog > div > div.material-dialog__window-actions > button:nth-child(2)")
        self.date2 = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div.stepper-body > div > div > div > div.coworking__page-dialog-follow-date > div > div:nth-child(4)")
        self.group_select = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div.stepper-body > div > div > div > div.list-tile.coworking__page-dialog-follow-list > div")
        self.group_select2 = (By.CSS_SELECTOR, "#dialog > div:nth-child(2) > div > div.material-dialog__window-container > div.material-dialog__window-body > div > div > div > div.list-tile__trailing > button")
        self.group_select3 = (By.CSS_SELECTOR, "#dialog > div:nth-child(2) > div > div.material-dialog__window-actions > button:nth-child(2)")
        self.time = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div.stepper-body > div > div > div > div.coworking__page-dialog-follow-timeseat > div:nth-child(1) > label")
        self.input_h = (By.CSS_SELECTOR, "#dialog > div.material-dialog.timepicker > div > div.material-dialog__window-container > div.material-dialog__window-body > div > label:nth-child(1)")
        self.input_m = (By.CSS_SELECTOR, "#dialog > div.material-dialog.timepicker > div > div.material-dialog__window-container > div.material-dialog__window-body > div > label:nth-child(2)")
        self.btn_select4 = (By.CSS_SELECTOR, "#dialog > div.material-dialog.timepicker > div > div.material-dialog__window-actions > button:nth-child(2)")
        self.place = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-container > div.material-dialog__window-body > div.stepper-body > div > div > div > div.coworking__page-dialog-follow-timeseat > div:nth-child(2) > div")
        self.place11 = (By.CSS_SELECTOR, "#dialog > div:nth-child(2) > div > div.material-dialog__window-container > div.material-dialog__window-body > div.md3-list > div:nth-child(10) > div.list-tile__trailing")
        self.select5 = (By.CSS_SELECTOR, "#dialog > div:nth-child(2) > div > div.material-dialog__window-actions > button:nth-child(2)")
        self.btn_book = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-actions > button:nth-child(2)")
        self.btn_cancel = (By.CSS_SELECTOR, "#app div.coworking button.baseavatar_close")
        self.yes_confirm = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-actions > button:nth-child(2)")


    def click_checkbox_selector(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.checkbox_selector)).click()

    def click_btn_next(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_book)).click()

    def click_aybek2(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.aybek2)).click()

    def click_btn_select1(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_select1)).click()

    def click_btn_confirm_select1(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_confirm_select1)).click()

    def click_date2(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.date2)).click()

    def click_group_select(self):
        self.scroll_to_element(self.group_select)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.group_select)).click()

    def click_group_select2(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.group_select2)).click()

    def click_group_select3(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.group_select3)).click()

    def click_time(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.time)).click()

    def enter_hours(self, hours_text):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(self.input_h))
        element.send_keys(Keys.BACK_SPACE)
        element.send_keys(Keys.BACK_SPACE)
        element.send_keys(hours_text)

    def enter_minutes(self, minutes_text):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(self.input_m))
        element.send_keys(Keys.BACK_SPACE)
        element.send_keys(Keys.BACK_SPACE)
        element.send_keys(minutes_text)

    def click_btn_select4(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_select4)).click()

    def click_place(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.place)).click()

    def click_place11(self):
        self.scroll_to_element(self.place11)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.place11)).click()

    def click_select5(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.select5)).click()

    def click_btn_book(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_book)).click()

    def click_btn_cancel(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_cancel)).click()

    def click_yes_confirm(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.yes_confirm)).click()

    def scroll_to_element(self, locator, timeout=10, pause=1):
        """Плавно скроллит к элементу по локатору (учитывает вложенные
        скролл-контейнеры, например внутри модальных диалогов)."""
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            element
        )
        time.sleep(pause)  # даём анимации скролла завершиться
        return element
