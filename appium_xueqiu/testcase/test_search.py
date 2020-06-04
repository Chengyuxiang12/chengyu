import pytest
import yaml

from appium_xueqiu.page.app import App


class TestSearch():
    def setup_class(self):
        self.search = App().start().main().goto_market().goto_search()

    def setup(self):
        pass

    @pytest.mark.parametrize(("a","b"), yaml.safe_load(open("./test_search.yaml", encoding="utf-8")))
    def test_search(self, a,b):
        self.search.search(a,b)
        if self.search.is_choose(a):
            self.search.reset(a)
        self.search.add(a)
        assert self.search.is_choose(a)
