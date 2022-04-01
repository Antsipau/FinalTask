import pytest

from config.config import TestData
from pages.login_page import LoginPage
from tests.test_base import BaseTest


class TestLogin(BaseTest):

    def test_is_button_exists(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_login_button_exists()
        assert flag

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)

