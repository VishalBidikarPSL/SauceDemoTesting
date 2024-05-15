import pytest
from SauceDemoPages.LoginPage import LoginPage
from SauceDemoPages.CartPage import CartPage
import allure


@allure.severity(allure.severity_level.NORMAL)
class Test_Cart:
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures("setup", "login")
    def test_001(self):
        x = CartPage(self.driver)
        x.adding_items()
        x.cart_click()
        x.test_header_text()
        x.verify_cart()
        x.remove()
        x.verify_cart()
        x.continue_shopping()
        x.cart_click()
        x.checkout_click()
        x.assert_checkout()
        x.cancel_click()
        x.checkout_click()
        x.checkout_form("Shane", "Furtado", 403601)
        x.continue_click()
        x.finish_click()
        x.finish_check()
        x.back_click()

        y= LoginPage(self.driver)
        y.Logout()
