import time

import pytest

from config.config import TestData
from pages.login_page import LoginPage
from pages.home_page import HomePage
from tests.test_base import BaseTest


class TestLogin(BaseTest):

    def test_is_button_exists(self):
        """a test to make sure the "log in" button exists"""
        self.homePage = HomePage(self.driver)
        self.homePage.click_admin_button()
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_login_button_exists()
        assert flag

    def test_login_page_title(self):
        """a test to make sure the "login page" exists"""
        self.homePage = HomePage(self.driver)
        self.homePage.click_admin_button()
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        """a test to make sure that you can log in into admin page"""
        self.homePage = HomePage(self.driver)
        self.homePage.click_admin_button()
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        admin_page_title = self.loginPage.get_title(TestData.ADMIN_PAGE_TITLE)
        assert admin_page_title == TestData.ADMIN_PAGE_TITLE


