from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class Testapp():
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.kuaishou.nebula"
        caps["appActivity"] = "com.yxcorp.gifshow.HomeActivity"
        caps['noReset'] = "true"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_broxser(self):
        action = TouchAction(self.driver)
        while True:
            action.press(x=573, y=1580).wait(200).move_to(x=573, y=1108).release().perform()
            sleep(15)
