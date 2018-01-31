# coding='utf-8'
import time
from appium import webdriver

# Returns abs path relative to this file and not cwd
from appium.webdriver.common.touch_action import TouchAction

def screen_shot_name():
    return time.strftime('screen/%h%s.{}').format( 'png')

def save_screen_shot(driver):
    driver.get_screenshot_as_file(screen_shot_name())