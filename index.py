# coding=utf-8
import os
from appium import webdriver

# Returns abs path relative to this file and not cwd
from appium.webdriver.common.touch_action import TouchAction

# os.system('./appium.sh')
# import time
# time.sleep(1)

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def implicitly_wait(driver, time):
    driver.implicitly_wait(time)


def onDuty(driver):
    try:
        # 等待打卡页面完成
        driver.wait_activity('com.alibaba.lightapp.runtime.activity.CommonWebViewActivity', 5)

        try:
            driver.find_element_by_xpath('//android.view.View[@content-desc="上班打卡"]').click()
        except:
            print('已经打过卡，无法再次打卡')
    except:
        print("打卡异常")
        # driver.quit()


def offDuty(driver):
    try:
        driver.wait_activity('com.alibaba.lightapp.runtime.activity.CommonWebViewActivity', 5)
        driver.find_element_by_xpath('//android.view.View[@content-desc="下班打卡"]').click()
    except:
        print('已经打过卡，无法再次打卡')

    noOffDuty = driver.find_element_by_xpath('//android.widget.Button[@content-desc="不打卡"]')
    noOffDuty.click()


def dingding(deviceName, platformVersion, platformName='Android', app="/Volumes/load/dingding.apk"):

    desired_caps = {}
    desired_caps['platformName'] = platformName
    desired_caps['platformVersion'] = platformVersion
    desired_caps['deviceName'] = deviceName
    desired_caps['app'] = app
    desired_caps['noReset'] = True

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

        onDuty(driver)

        offDuty(driver)

    except:
        print('element not found')
        driver.quit()


# dingding('emulator-5554', '5.1.1')
dingding('M960BDQ9228C9', '7.0.0')
# dingding('7.0', '9a6c2ad1')
