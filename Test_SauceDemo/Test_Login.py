import pytest
from SauceDemoPages.LoginPage import LoginPage


# @pytest.mark.usefixtures("setup", "login")
class TestLogin():
    @pytest.mark.usefixtures("setup", "login")
    def test_001(self):
        print('success')

    @pytest.mark.usefixtures("setup")
    def test_002(self):
        x = LoginPage(self.driver)
        x.login_test()
