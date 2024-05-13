from selenium.webdriver.common.by import By

from CommonBase import Commonbase


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.Username_Text_Field_Name = "user-name"
        self.Password_Text_Field_Name = "password"
        self.Login_Button = "login-button"
        self.Burger_Menu="react-burger-menu-btn"
        self.Logout_Button="logout_sidebar_link"
    def username_input(self, username):
        self.driver.find_element(By.ID, self.Username_Text_Field_Name).send_keys(username)

    def password_input(self, password):
        self.driver.find_element(By.ID, self.Password_Text_Field_Name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.Login_Button).click()

    def Logout(self):
        Burger_Menu = self.driver.find_element(By.ID, self.Burger_Menu)
        Logout_Button = self.driver.find_element(By.ID, self.Logout_Button)

        Burger_Menu.click()
        Logout_Button.click()
    def login_test(self):
        y = Commonbase.Commonbase()
        data = y.read_excel()
        rows = data[data['index'].notna()].index.tolist()

        for index in rows:
            user_name = self.driver.find_element(By.ID, self.Username_Text_Field_Name)
            password = self.driver.find_element(By.ID, self.Password_Text_Field_Name)
            login_btn = self.driver.find_element(By.ID, self.Login_Button)


            u_value = data.iloc[index, 1]
            user_name.clear()
            user_name.send_keys(u_value)
            p_value = data.iloc[index, 2]
            password.clear()
            password.send_keys(p_value)

            try:

                login_btn.click()
                self.Logout()



            except:
                print('password doesnt work')
