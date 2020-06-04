from selenium.webdriver.common.by import By

from xuesheng_web.page.base_page import BasePage


class Main(BasePage):
    _base_url = 'http://localhost:8090/'

    def login(self, a, b):
        self._params["a"] = a
        self._params["b"] = b
        self.steps("../page/login.yaml")
        from xuesheng_web.page.index import Index
        return Index(self._driver)
