# coding=utf-8

from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction

{
    "app": "/Volumes/load/weixin.apk",
    "noReset": True,
    "platformName": "Android",
    "deviceName": "5PG0216413010987",
    "platformVersion": "5.0.2",
    "appActivity": ".ui.LauncherUI",
    "fastReset": False,
    "appPackage": "com.tencent.mm",
    "automationName": "appium",
    "androidProcess": "com.tencent.mm:appbrand1"
}
caps = {}
caps["app"] = "/Volumes/load/weixin.apk"
caps["noReset"] = True
caps["platformName"] = "Android"
caps["deviceName"] = "5PG0216413010987"
caps["platformVersion"] = "5.0.2"

# caps["deviceName"] = "M960BDQ9228C9"
# caps["platformVersion"] = "7.0.0"
caps["appActivity"] = ".ui.LauncherUI"
caps["fastReset"] = False
caps["appPackage"] = "com.tencent.mm"
caps["automationName"] = "appium"
caps["androidProcess"] = "com.tencent.mm:appbrand1"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(5)


def auto_save_hongbao(driver):
    print(driver.current_activity)
    try:
        kai = driver.find_element_by_id('com.tencent.mm:id/c2i')
        print(driver.page_source)
        kai.click()
        driver.wait_activity('.plugin.luckymoney.ui.LuckyMoneyDetailUI', 0.5)
        driver.back()

    except:
        print('没有发现未领取的红包')
        driver.back()



def auto_find_hongbao(driver):
    print(driver.current_activity)
    hongbaos = driver.find_elements_by_id('com.tencent.mm:id/ada')
    if len(hongbaos) == 0:
        driver.back()
    index = 0
    for hongbao in hongbaos:
        hongbao.click()
        # driver.wait_activity('.plugin.luckymoney.ui.LuckyMoneyReceiveUI', 0.5)
        auto_save_hongbao(driver)
        if index ==  len(hongbaos)-1:
            driver.back()

        index = index +1


def auto_loop(driver):
    chats = driver.find_elements_by_id('com.tencent.mm:id/apr')
    for chat in chats:
        try:
            hongdian = chat.find_element_by_id('com.tencent.mm:id/iu')
            if hongdian:
                print('有消息')
                chat.click()
                driver.wait_activity('.ui.LauncherUI', 1)
                auto_find_hongbao(driver)
        except Exception as e:
            print('没有小红点')
            print(e)


while True:
    auto_loop(driver)
    time.sleep(0.5)

# driver.quit()
