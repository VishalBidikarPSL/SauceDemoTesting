import pytest
from SauceDemoPages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup")
class TestLogin():

    # def test_001(self):
    #     lg = LoginPage(self.driver)
    #     print('success')

    def test_002(self):
        x = LoginPage(self.driver)
        x.login_test()




