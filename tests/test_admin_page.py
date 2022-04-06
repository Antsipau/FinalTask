import time

import pytest

from config.config import TestData
from pages.admin_page import AdminPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from tests.test_base import BaseTest


class TestAdmin(BaseTest):
    def test_view_site_link_clickable(self):
        """a test to make sure that you can return to the home page using "view site" link"""
        self.homePage = HomePage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.homePage.click_admin_button()
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.adminPage = AdminPage(self.driver)
        self.adminPage.click_on_view_site_link()
        home_page_title = self.adminPage.get_title(TestData.HOME_PAGE_TITLE)
        assert home_page_title == TestData.HOME_PAGE_TITLE
