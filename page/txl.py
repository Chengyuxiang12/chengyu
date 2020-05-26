from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from case.tianjia import Tianjia
from page.base_page import BasePage


class AddressBook(BasePage):

    def add_menber(self):
        self.find(By.ID, 'username').send_keys('abcdefffff')
        self.find(By.ID, 'memberAdd_acctid').send_keys('abcdefffff')
        self.find(By.ID, 'memberAdd_phone').send_keys('11111111111')
        self.find(By.CSS_SELECTOR, '//*[@id="js_contacts77"]/div/div[2]/div/div[4]/div/form/div[1]/a[1]').click()
        zhuce = len(self.find(By.CSS_SELECTOR, '.member_edit_item_Account>div:nth-child(2) .ww_inputWithTips_tips').text)
        if zhuce > 0:
            self.find(By.CSS_SELECTOR, '.js_btn_cancel').click()
            self.find(By.CSS_SELECTOR, '.ww_dialog_foot>a:nth-child(2)').click()

            return Tianjia(self._driver)
        else:
            print("xxxx")
