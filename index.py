# coding=utf-8
import os
import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
from appium.webdriver.common.touch_action import TouchAction

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def implicitly_wait(driver, time):
    driver.implicitly_wait(time)





desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'emulator-5554'

desired_caps['platformVersion'] = '7.0.0'
desired_caps['deviceName'] = 'M960BDQ9228C9'

desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = '9a6c2ad1'

# desired_caps['platformVersion'] = '5.0.2'
# desired_caps['deviceName'] = '5PG0216413010987'
# desired_caps['noReset'] = True

desired_caps['app'] = "/Volumes/load/kk.apk"
desired_caps['app'] = "/Volumes/load/dingding.apk"
desired_caps['noReset'] = True

# desired_caps['app'] ="/Users/le/Desktop/pgyer.apk"
# desired_caps['appPackage'] = 'com.pgyer'
# desired_caps['appActivity'] = '.ContactManager'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

try:
    compyTabItem = driver.find_element_by_xpath(
        '//android.widget.FrameLayout[@content-desc="工作"]/android.widget.RelativeLayout')
    compyTabItem.click()
    driver.implicitly_wait(2)
    TouchAction(driver).press(x=692, y=1500).move_to(x=25, y=-604).release().perform()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[9]/android.widget.RelativeLayout/android.widget.ImageView') \
        .click()
    implicitly_wait(driver, 3)


    try:
        driver.wait_activity('com.alibaba.lightapp.runtime.activity.CommonWebViewActivity', 5)

        try:
            driver.find_element_by_xpath('//android.view.View[@content-desc="上班打卡"]').click()
        except:
            print('已经打过卡，无法再次打卡')

        try:
            driver.find_element_by_xpath('//android.view.View[@content-desc="下班打卡"]').click()
        except:
            print('已经打过卡，无法再次打卡')


    except:
        print("打卡异常")

except:
    print('element not found')

