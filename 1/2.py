#coding:utf-8
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['deviceName'] = '69DDU16515003532'
desired_caps['appPackage'] = 'com.zhonglian.assetsvluation'
desired_caps['appActivity'] = '.view.activity.SplashActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
TouchAction(driver).tap(x=744, y=1666).perform()
sleep(5)
TouchAction(driver).tap(x=744, y=1682).perform()
sleep(5)
TouchAction(driver).tap(x=735, y=1674).perform()
sleep(5)
TouchAction(driver).tap(x=735, y=1674).perform()
sleep(5)
TouchAction(driver).tap(x=814, y=802).perform()
sleep(5)
TouchAction(driver).tap(x=220, y=652).perform()
sleep(5)
TouchAction(driver).tap(x=295, y=1724).perform()
sleep(5)
TouchAction(driver).tap(x=100, y=1732).perform()
sleep(5)
TouchAction(driver).tap(x=287, y=1225).perform()
sleep(5)

TouchAction(driver).tap(x=519, y=1574).perform()
sleep(5)
TouchAction(driver).tap(x=303, y=1217).perform()
sleep(5)
TouchAction(driver).tap(x=303, y=1217).perform()
sleep(5)
TouchAction(driver).tap(x=835, y=1171).perform()
sleep(5)
