from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.Username_Text_Field_Name = "user-name"
        self.Password_Text_Field_Name = "password"
        self.Login_Button = "login-button"

    def username_input(self, username):
        self.driver.find_element(By.ID, self.Username_Text_Field_Name).send_keys(username)

    def password_input(self, password):
        self.driver.find_element(By.ID, self.Password_Text_Field_Name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.Login_Button).click()
