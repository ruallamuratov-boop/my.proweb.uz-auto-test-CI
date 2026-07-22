import time
from time import sleep
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import allure

from pages import video_page
from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from pages.video_page import VideoPage
from pages.coworking_page import CoworkingPage


def test_proweb_chrome(driver_chrome):
    driver_chrome.get("https://my.proweb.uz")
    login_page = LoginPage(driver_chrome)
    time.sleep(5)
    login_page.click_btn_lang()
    time.sleep(3)
    login_page.enter_login("998771140140")
    time.sleep(3)
    login_page.click_btn_enter1()
    time.sleep(3)
    login_page.enter_password("FernandoAlonso14")
    time.sleep(3)
    login_page.click_btn_enter2()
    time.sleep(3)
    try:
        login_page.click_session1()
        time.sleep(3)
        login_page.click_session_end()
        time.sleep(3)
    except NoSuchElementException:
        pass
    menu_page = MenuPage(driver_chrome)
    menu_page.click_coworking_booking()
    time.sleep(3)
    coworking_page = CoworkingPage(driver_chrome)

    coworking_page.click_checkbox_selector()
    time.sleep(3)
    coworking_page.click_btn_next()
    time.sleep(3)

    coworking_page.click_aybek2()
    time.sleep(3)
    coworking_page.click_btn_select1()
    time.sleep(3)
    coworking_page.click_btn_confirm_select1()
    time.sleep(3)

    coworking_page.click_date2()
    time.sleep(3)
    coworking_page.click_group_select()
    time.sleep(3)
    coworking_page.click_group_select2()
    time.sleep(3)
    coworking_page.click_group_select3()
    time.sleep(3)

    coworking_page.click_time()
    time.sleep(3)
    coworking_page.enter_hours("20")
    coworking_page.enter_minutes("00")
    time.sleep(3)
    coworking_page.click_btn_select4()
    time.sleep(3)

    coworking_page.click_place()
    time.sleep(3)
    coworking_page.click_place11()
    time.sleep(3)
    coworking_page.click_select5()
    time.sleep(3)

    coworking_page.click_btn_book()
    time.sleep(3)

    menu_page.click_go_coworking()
    time.sleep(3)
    coworking_page.click_btn_cancel()
    time.sleep(3)
    coworking_page.click_yes_confirm()
    time.sleep(3)
    menu_page.click_go_home()
    time.sleep(3)

    menu_page.click_group()
    time.sleep(3)
    menu_page.click_videos()
    time.sleep(3)
    menu_page.click_lesson28()
    time.sleep(3)
    video_page = VideoPage(driver_chrome)
    try:
        video_page.click_later()
        time.sleep(3)
    except (TimeoutException, NoSuchElementException):
        pass
    video_page.click_play_vid()
    time.sleep(2)
    video_page.click_full_scr()
    time.sleep(2)
    video_page.click_scr_tap()
    time.sleep(80)
    video_page.click_full_scr_ext()
    time.sleep(2)
    try:
        video_page.click_vote()
        time.sleep(3)
        video_page.click_vote_send()
        time.sleep(3)
    except (TimeoutException, NoSuchElementException):
        pass
    menu_page.click_btn_profile()
    time.sleep(3)
    menu_page.click_btn_exit()
    time.sleep(3)
    menu_page.click_btn_y()
    time.sleep(3)











