from time import sleep

from selenium.webdriver.common.by import By

from xuesheng_web.page.base_page import BasePage


# from xuesheng_web.page.main import Main
from xuesheng_web.page.hdou import Hdon


class Index(BasePage):


    def add_hdong(self):
        self.find('css selector', ".navbar-right>li:nth-child(2)").click()
        return Hdon(self._driver)
