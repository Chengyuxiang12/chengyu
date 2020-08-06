from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from xuesheng_web.page.base_page import BasePage


class Hdon(BasePage):
    def quit(self):
        self.find('xpath', '//*[@id="navbar"]/div/div[1]/p/a[2]').click()
        from xuesheng_web.page.main import Main
        return Main(self._driver)
    def add(self):
        self.find('id','txtName').send_keys("郊游")
        self.find('id','txtPlace').send_keys("萧山春")
        self.find('id','txtTime').send_keys("11/24/2016")
