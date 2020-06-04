from time import sleep

import pytest
import yaml

from xuesheng_web.page.main import Main
from selenium import webdriver


class TestLogin():
    def setup_class(self):
        self.main = Main()


    @pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("./zhanghao.yaml", encoding="utf-8")))
    def testlogin(self, a, b):
        dl=self.main.login(a, b)
        sleep(5)

        dl.add_hdong().quit()
