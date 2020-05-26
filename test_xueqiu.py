import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.extensions.android.gsm import GsmCallActions


class Testxueqiu:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'MGFNW19821011492'
        desired_caps['browserName']='Browser'
        # desired_caps['appPackage'] = 'com.hpbr.bosszhipin'
        # desired_caps['appActivity'] = '.module.launcher.WelcomeActivity'
        
        desired_caps['noReset'] = 'True'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        pass

    # def test_xueqiu(self):
    #     self.driver.find_element(MobileBy.XPATH,
    #                              '//*[@resource-id="com.hpbr.bosszhipin:id/ly_menu"]//android.widget.RelativeLayout[2]').click()
    #     self.driver.find_element(MobileBy.ID, 'com.hpbr.bosszhipin:id/et_search').send_keys("腾讯")
    #     self.driver.find_element(MobileBy.XPATH,"//*[@text='腾讯实习生']").click()
    def test_lll(self):
        self.driver.get("http://m.baidu.com")
