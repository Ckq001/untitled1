import unittest
from appium import webdriver
from time import sleep

class MyTestCase(unittest.TestCase):
    # 用于测试用例执行前初始化工作，如打开浏览器等，如不需要初始化，可以pass
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '127.0.0.1:21503'
        desired_caps['appPackage'] = 'com.ss.android.article.news'
        desired_caps['appActivity'] = '.activity.SplashBadgeActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

        print("____打开app_____")
        print("____执行用例_____")

        sleep(5)

        # pass

    # 用于测试用例执行后善后工作，如关闭浏览器等，如不需要，可以pass
    def tearDown(self):
        print("____执行完毕_____")

    #手机号登陆
    def testLoginMobile(self):
        """进入个人中心验证"""
        sleep(5)
        wode = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.TabHost/android.widget.RelativeLayout[2]/android.widget.TabWidget/android.widget.RelativeLayout[4]')
        wode.click()
        print("____进入个人中心_____")
        sleep(5)
        logintext = self.driver.find_element_by_id('com.ss.android.article.news:id/az3').text
        self.assertEqual(logintext,"登录推荐更精准")
    def testMultiply(self):
        """乘法验证"""
        self.testLoginMobile()
        print("____谁说的_____")
        self.assertEqual((2*10),20)


if __name__ == '__main__':
    unittest.main()