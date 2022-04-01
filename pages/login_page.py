from selenium.webdriver.common.by import By

from config.config import TestData
from pages.base_page import BasePage


class LoginPage(BasePage):

    """By locators - OR"""
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-form > div.submit-row > input[type=submit]")

    def __init__(self, driver):
        """constructor of the page class"""
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self, title):
        """to get title of the page"""
        return self.get_title(title)

    def is_username_field_enable(self):
        """to check that username field is enable"""
        return self.element_is_enabled(self.USERNAME_FIELD).is_enabled

    def is_password_field_enable(self):
        """to check that password field is enable"""
        return self.element_is_enabled(self.PASSWORD_FIELD).is_enabled

    def is_login_button_exists(self):
        """to check that button exists"""
        return self.element_is_visible(self.LOGIN_BUTTON)

    def do_login(self, username, password):
        """to  do action to log in"""
        self.do_send_key(self.USERNAME_FIELD, username)
        self.do_send_key(self.PASSWORD_FIELD, password)
        self.do_click(self.LOGIN_BUTTON)


