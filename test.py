from selenium import webdriver


class Test():
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://localhost:8090/')
    def test1(self):
        self.driver.find_element('xpath',"/html/body/div[2]/div[2]/form/div[1]/a").click()