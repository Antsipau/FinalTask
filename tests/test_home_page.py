import pytest
import time

from config.config import TestData
from pages.home_page import HomePage
from tests.test_base import BaseTest


class TestHomePage(BaseTest):

    def test_get_home_page_title(self):
        """a test to make sure the "home page" exists"""
        self.homePage = HomePage(self.driver)
        home_page_title = self.homePage.get_title(TestData.HOME_PAGE_TITLE)
        assert home_page_title == TestData.HOME_PAGE_TITLE

    def test_go_to_admin_button_exists(self):
        """a test to make sure the "go to admin" button exists"""
        self.homePage = HomePage(self.driver)
        flag = self.homePage.is_go_to_admin_button_exists()
        assert flag

    def test_get_text_go_to_admin_button(self):
        """a test to make sure the "go to admin" button is correct button"""
        self.homePage = HomePage(self.driver)
        button_name = self.homePage.get_text_from_go_to_admin_button()
        assert button_name == TestData.GO_TO_ADMIN_BUTTON_NAME

    def test_admin_button_clickable(self):
        """a test to make sure the "go to admin" button is clickable"""
        self.homePage = HomePage(self.driver)
        self.homePage.click_admin_button()
        login_page_title = self.homePage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert login_page_title == TestData.LOGIN_PAGE_TITLE

    def test_navbar_clickable(self):
        """a test to make sure the "navigation bar" is clickable"""
        self.homePage = HomePage(self.driver)
        self.homePage.click_navbar()
        header_name = self.homePage.get_home_page_header_name()
        assert header_name == TestData.HOME_PAGE_HEADER_NAME
