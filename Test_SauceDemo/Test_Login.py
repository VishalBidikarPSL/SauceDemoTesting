import pytest
from SauceDemoPages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup", "login")
class TestLogin():

    def test_001(self):
        lg = LoginPage(self.driver)
        print('success')





