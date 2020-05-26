from page.main import Main


class TestAdd:
    def setup(self):
        self.main=Main()

    def test_addmember(self):
        add_menber = self.main.goto_add_menber()
        add_menber.add_menber()
