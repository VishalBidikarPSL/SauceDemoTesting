import pytest
from selenium import webdriver
from SauceDemoPages.LoginPage import LoginPage
import configparser

config = configparser.ConfigParser()
config.read(r'..\CommonBase\config.properties')


@pytest.fixture
def setup(request):
    request.cls.driver = webdriver.Chrome()
    request.cls.driver.maximize_window()
    request.cls.driver.implicitly_wait(5)
    request.cls.driver.get(config.get("Url", "base_url"))
    yield
    request.cls.driver.quit()


@pytest.fixture
def login(request):
    lg = LoginPage(request.cls.driver)
    lg.username_input(config.get("Credentials", "correct_username"))
    lg.password_input(config.get("Credentials", "correct_password"))
    lg.click_login()
