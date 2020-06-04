from xuesheng_web.page.base_page import BasePage


class Hdon(BasePage):
    def quit(self):
        self.find('xpath', '//*[@id="navbar"]/div/div[1]/p/a[2]').click()
        from xuesheng_web.page.main import Main
        return Main(self._driver)