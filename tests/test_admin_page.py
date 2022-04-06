import time

import pytest

from config.config import TestData
from pages.admin_page import AdminPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from tests.test_base import BaseTest


class TestAdmin(BaseTest):

    def test_get_admin_page_title(self):
        """a test to make sure the "admin page" exists"""
        self.homePage = HomePage(self.driver)
        self.homePage.click_admin_button()
        self.loginPage = LoginPage(self.driver)
        adminPage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        title = adminPage.get_admin_page_title(TestData.ADMIN_PAGE_TITLE)
        assert title == TestData.ADMIN_PAGE_TITLE

    def test_view_site_link_clickable(self):
        """a test to make sure that you can return to the home page using "view site" link"""
        self.homePage = HomePage(self.driver)
        self.homePage.click_admin_button()
        self.loginPage = LoginPage(self.driver)
        adminPage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        adminPage.click_on_view_site_link()
        home_page_title = self.homePage.get_title(TestData.HOME_PAGE_TITLE)
        assert home_page_title == TestData.HOME_PAGE_TITLE
