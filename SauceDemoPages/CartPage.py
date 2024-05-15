from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.Cart_Btn = "shopping_cart_link"
        self.Add_Cart1 = "add-to-cart-sauce-labs-backpack"
        self.Add_Cart2 = "add-to-cart-sauce-labs-bike-light"
        self.Add_Cart3 = "add-to-cart-sauce-labs-bolt-t-shirt"
        self.Add_Cart4 = "add-to-cart-sauce-labs-fleece-jacket"
        self.Add_Cart5 = "add-to-cart-sauce-labs-onesie"
        self.Add_Cart6 = "add-to-cart-test.allthethings()-t-shirt-(red)"

        self.Cart_itemsNo = "//*[@id='shopping_cart_container']/a/span"

        self.remove_item1 = "//*[@id='remove-sauce-labs-backpack']"
        self.remove_item2 = "//*[@id='remove-sauce-labs-bike-light']"
        self.remove_item3 = "//*[@id='remove-sauce-labs-bolt-t-shirt']"

        self.continue_btn = "continue-shopping"
        self.checkout_btn = "checkout"
        self.cancel1 = "//*[@id='cancel']"
        self.continue_btn2 = "continue"

        self.form_fname="first-name"
        self.form_lname = "last-name"
        self.form_post = "postal-code"

        self.finish1= "finish"
        self.back="back-to-products"

    def cart_click(self):
        self.driver.find_element(By.CLASS_NAME, self.Cart_Btn).click()

    def adding_items(self):
        for i in range(1, 7):
            cart_id = f"Add_Cart{i}"
            add_cart_element = getattr(self, cart_id)
            self.driver.find_element(By.ID, add_cart_element).click()

    def test_header_text(self):
        header_element = self.driver.find_element(By.CLASS_NAME, "app_logo")
        expected_header_text = "Swag Labs"
        actual_header_text = header_element.text
        assert actual_header_text == expected_header_text, "Header text does not match"

    def verify_cart(self):
        # Find all cart items
        cart_items = self.driver.find_elements(By.CLASS_NAME, "cart_item_label")
        cart_items_count = len(cart_items)

        # Find the displayed cart count logo
        cart_items_count_logo_element = self.driver.find_element(By.XPATH, self.Cart_itemsNo)
        cart_items_count_logo = int(cart_items_count_logo_element.text)

        assert cart_items_count == cart_items_count_logo, "Count does not match"

    def remove(self):
        for i in range(1, 3):
            cart_id = f"remove_item{i}"
            remove = getattr(self, cart_id)
            self.driver.find_element(By.XPATH, remove).click()

    def continue_shopping(self):
        self.driver.find_element(By.ID, self.continue_btn).click()

    def checkout_click(self):
        self.driver.find_element(By.ID, self.checkout_btn).click()

    def assert_checkout(self):
        header_element = self.driver.find_element(By.CLASS_NAME, "title")
        expected_text = "Checkout: Your Information"
        actual_text = header_element.text
        assert actual_text == expected_text, "Not Checkout Page"

    def cancel_click(self):
        self.driver.find_element(By.XPATH, self.cancel1).click()

    def continue_click(self):
        self.driver.find_element(By.ID, self.continue_btn2).click()

    def finish_click(self):
        self.driver.find_element(By.ID, self.finish1).click()

    def checkout_form(self,first_name,last_name,postal):
        self.driver.find_element(By.ID, self.form_fname).send_keys(first_name)
        self.driver.find_element(By.ID, self.form_lname).send_keys(last_name)
        self.driver.find_element(By.ID, self.form_post).send_keys(postal)

    def finish_check(self):
        header_element = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/span")
        expected_text = "Checkout: Complete!"
        actual_text = header_element.text
        assert actual_text == expected_text, "Not Checkout Page"

    def back_click(self):
        self.driver.find_element(By.ID, self.back).click()
