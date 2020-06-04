import yaml
from selenium.webdriver.common.by import By

from appium_xueqiu.page.base_page import BasePage


class Search(BasePage):
    def search(self, a,b):
        # self._params["name"]=name
        self._params["a"] = a
        self._params["b"] = b
        self.steps("../page/search.yaml")

    def add(self,a):
        self._params["a"] = a

        self.steps("../page/search.yaml")

    def is_choose(self, a):
        self._params["a"] = a
        return self.steps("../page/search.yaml")

    def reset(self, a):
        self._params["a"] = a
        return self.steps("../page/search.yaml")
