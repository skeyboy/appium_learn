# coding=utf-8
import os
import utils
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
    # driver.implicitly_wait(time)
    print('depresed')


def onDuty(driver, tryCount=1):
    driver.wait_activity('com.alibaba.lightapp.runtime.activity.CommonWebViewActivity', 1)
    driver.implicitly_wait(5)
    try:
        driver.find_element_by_xpath('//android.view.View[@content-desc="上班打卡"]').click()
    except Exception as e:
        print(e)

        print('已经打过卡，无法再次打卡')
        if tryCount > 1:
            onDuty(driver, tryCount - 1)
        else:
            offDuty(driver, 3)


def offDuty(driver, tryCount=1):
    driver.wait_activity('com.alibaba.lightapp.runtime.activity.CommonWebViewActivity', 1)
    driver.implicitly_wait(5)

    try:
        driver.find_element_by_xpath('//android.view.View[@content-desc="下班打卡"]').click()
    except Exception as e:
        print(e)
        print('已经打过卡，无法再次打卡')
        if tryCount > 1:
            offDuty(driver, tryCount - 1)
        else:
            print('打卡结束')
            # driver.quit()


def login(driver, phone='13621019041', pwd='123456'):
    try:
        phone_input = driver.find_element_by_id('com.alibaba.android.rimet:id/et_phone_input')
        phone.send_keys(phone)
    except Exception as e:
        print(e)
    try:
        pwd_input = driver.find_elements_by_id('com.alibaba.android.rimet:id/et_pwd_login')
        pwd_input.send_keys(pwd)
    except Exception as e:
        print(e)

    try:
        login_btn = driver.find_element_by_id('com.alibaba.android.rimet:id/btn_next')
        login_btn.click()
    except Exception as e:
        print(e)


def check_new_info_alert(driver):
    try:
        alert_view = driver.find_element_by_id('com.alibaba.android.rimet:id/ll_start_chat')
        ok = alert_view.find_element_by_id('com.alibaba.android.rimet:id/btn_right_text')
        ok.click()
    except Exception as e:
        print(e)


# def chek_qingjia(driver):

def auto_login(driver,phone, pwd):
    driver.wait_activity('com.alibaba.android.user.login.SignUpWithPwdActivity',5)

    try:
        phone_input = driver.find_element_by_id('com.alibaba.android.rimet:id/et_phone_input')
        pwd_input = driver.find_element_by_id('com.alibaba.android.rimet:id/et_pwd_login')

        phone_input.clear()
        pwd_input.clear()

        phone_input.send_keys(phone)
        pwd_input.send_keys(pwd)
        driver.back()
        import time
        time.sleep(1)
        login_input = driver.find_element_by_id('com.alibaba.android.rimet:id/btn_next')
        login_input.click()
    except Exception as e:
        print("登录问题")
        print(e)



def unlock_screen(driver, *pwd_items):
    import time
    for pwd_item in  pwd_items:
        try:
            driver.find_element_by_id('com.alibaba.android.rimet:id/pwd_kb_{}'.format(pwd_item)).click()
        except Exception as e:
            print(e)
            print("密码点获取错误")
            utils.save_screen_shot(driver)
        time.sleep(0.5)
    time.sleep(0.5)

    try:
        driver.find_element_by_id('com.alibaba.android.rimet:id/pwd_error_tip')
        utils.save_screen_shot(driver)

        return False
    except Exception as  e :
        utils.save_screen_shot(driver)
        return True


def dingding(deviceName, platformVersion, platformName='Android', app="/Volumes/load/dingding.apk"):
    desired_caps = {}
    desired_caps['platformName'] = platformName
    desired_caps['platformVersion'] = platformVersion
    desired_caps['deviceName'] = deviceName
    desired_caps['app'] = app
    desired_caps['noReset'] = True
    desired_caps['fastReset'] = False
    desired_caps['appActivity'] = 'com.alibaba.android.rimet.biz.SplashActivity'
    desired_caps['appPackage'] = 'com.alibaba.android.rimet'


    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # driver.implicitly_wait(5)

    driver.wait_activity('com.alibaba.android.rimet.biz.SplashActivity',10)
    print(driver.current_activity)


    try:
        check_new_info_alert(driver)
        implicitly_wait(driver, 2)

        print(driver.current_activity)

        implicitly_wait(driver,5)

        try:
            auto_login(driver,'13621019041','123456')
        except Exception as  e:
            print(e)
            utils.save_screen_shot(driver)



        implicitly_wait(driver,3)
        print(driver.current_activity)

        driver.wait_activity('com.alibaba.android.user.pwd.activities.LockScreenPwdActivity',3)

        #错误密码尝试
        unlock_screen(driver,'1','2','3','5')
        import  time
        time.sleep(1)
        unlock_screen(driver, '1', '2', '3','4')

        # time.sleep(2)

        driver.wait_activity('.biz.home.activity.HomeActivity',3)
        print(utils.screen_shot_name())
        driver.save_screenshot(utils.screen_shot_name())

        compyTabItem = driver.find_element_by_xpath(
            '//android.widget.FrameLayout[@content-desc="工作"]/android.widget.RelativeLayout')
        compyTabItem.click()
        # driver.implicitly_wait(2)




        startBtn = driver.find_elements_by_id('com.alibaba.android.rimet:id/header_banner_item_title')[1]
        dingLogBtn = driver.find_elements_by_id('com.alibaba.android.rimet:id/oa_entry_icon')[5]

        TouchAction(driver).press(dingLogBtn).wait(500).move_to(startBtn).release().perform()


        try:
            dingding = driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.view.View/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[9]/android.widget.RelativeLayout/android.widget.ImageView')
            dingding.click()
        except  Exception as e:
            print(e)
            driver.quit()

        # implicitly_wait(driver, 3)
        driver.wait_activity('com.alibaba.lightapp.runtime.activity.CommonWebViewActivity', 5)

        print(driver.page_source)

        onDuty(driver, 1)
        print(driver.current_activity)

        time.sleep(60)

        # driver.quit()


    except Exception as e:
        print('element not found')
        print(e)

        driver.quit()


# dingding('emulator-5554', '5.1.1')
# dingding('M960BDQ9228C9', '7.0.0')
# dingding('9a6c2ad1', '7.0')
# dingding('71UBBLA223HG', '5.1')
# dingding('5PG0216413010987', '5.0.2')
