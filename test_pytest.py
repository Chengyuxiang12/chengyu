import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestDemo():
    def setup(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        # self.driver.quit()
        pass

    def test_demo(self):
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        db = shelve.open("cookies")
        # db['cookie'] = self.driver.get_cookies()
        cookies = db['cookie']
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element_by_id('menu_contacts').click()

        sleep(6)
        db.close()
