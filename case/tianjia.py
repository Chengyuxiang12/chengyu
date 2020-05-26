from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Tianjia(BasePage):
    def sub(self):
        self.find(By.XPATH, '//*[@id="member_list"]/tr[1]/td[1]/input')
        self.find(By.XPATH, '//*[@id="js_contacts67"]/div/div[2]/div/div[2]/div[3]/div[1]/a[3]')
