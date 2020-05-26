from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage
from page.txl import AddressBook


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def goto_add_menber(self):
        self.find(By.ID, 'menu_contacts').click()
        locator = (By.CSS_SELECTOR, '.js_add_member:nth-child(2)')
        self.wait_for(locator)
        self.find(By.LINK_TEXT, '添加成员').click()
        return AddressBook(self._driver)
