# coding=utf-8

from appium import webdriver

caps = {}
caps["app"] = "/Volumes/load/12306.apk"
caps["noReset"] = True
caps["platformName"] = "Android"
caps["deviceName"] = "5PG0216413010987"
caps["platformVersion"] = "5.0.2"


def add_persons(driver):
    driver.find_element_by_xpath(
        '//android.webkit.WebView[@content-desc="添加乘客"]/android.widget.ListView[1]/android.view.View/android.widget.CheckBox').click()
    driver.find_element_by_xpath(
        '//android.webkit.WebView[@content-desc="添加乘客"]/android.widget.ListView[3]/android.view.View[5]/android.widget.CheckBox').click()

    driver.find_element_by_xpath('//android.widget.TextView[@content-desc="完成"]').click()

    # 提交订单
    driver.find_element_by_xpath(
        '//android.webkit.WebView[@content-desc="确认订单"]/android.widget.ListView[2]/android.view.View[2]').click()
    # driver.find_element_by_xpath('//android.view.View[@content-desc="提交订单"]').click()


def buy_train_no(driver, trainNo='Z202'):
    driver.find_element_by_id('//android.view.View[@content-desc="' + trainNo + '"]').click()
    try:
        sure = driver.find_element_by_id('com.MobileTicket.common:id/sure')
        sure.click()
        print("无票")
    except:
        print("有票，继续")
        print(driver.current_activity)
        add_persons(driver)



driver = webdriver.Remote("http://localhost:4722/wd/hub", caps)

driver.wait_activity('com.alipay.mobile.quinox.LauncherActivity', 5)

driver.implicitly_wait(4)

driver.wait_activity('.ui.activity.MainActivity', 2)


def try_again(driver, t=1):
    try:
        try_btn = driver.find_element_by_xpath('//android.view.View[@content-desc="点击重试"]')
        try_btn.click()
        print(driver.current_activity)
        driver.implicitly_wait(3)
        driver.wait_activity('com.alipay.mobile.nebulacore.ui.H5Activity', 2)
        if t >1:

            try_again(driver, t-1)
    except:
        print("正常载入……")
        driver.wait_activity('com.alipay.mobile.nebulacore.ui.H5Activity', 2)
        try:
            print(driver.current_activity)
            buy_train_no(driver, 'Z202')
            # buy_train_no(driver, 'Z162')

        except:
            print('查找异常')


# 普通列车
try:
    train_kind = driver.find_element_by_id('com.MobileTicket.launcher:id/ticket_home_seat_type_ztk')
    train_kind.click()
except:
    print(driver.current_activity)

try:
    search_btn = driver.find_element_by_id('com.MobileTicket.launcher:id/ticket_home_btn_search')
    search_btn.click()
except:
    print(driver.current_activity)

driver.wait_activity('com.alipay.mobile.nebulacore.ui.H5Activity', 2)
try_again(driver, 3)
