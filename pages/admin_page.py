from selenium.webdriver.common.by import By

from config.config import TestData
from pages.base_page import BasePage


class AdminPage(BasePage):
    HEADER = (By.CSS_SELECTOR, "#site-name > a")
    USER_ACCOUNT_NAME = (By.CSS_SELECTOR, "#user-tools > strong")
    VIEW_SITE_LINK = (By.CSS_SELECTOR, "#user-tools > a:nth-child(2)")
    CHANGE_PASSWORD_LINK = (By.CSS_SELECTOR, "#user-tools > a:nth-child(3)")
    LOG_OUT_LINK = (By.CSS_SELECTOR, "#user-tools > a:nth-child(4)")
    POSTS_LINK = (By.CSS_SELECTOR, "#content-main > div.app-app.module > table > tbody > tr > th > a")
    GROUPS_BUTTON = (By.CSS_SELECTOR, "#content-main > div.app-auth.module > table > tbody > tr.model-group > th > a")
    USERS_LINK = (By.CSS_SELECTOR, "#content-main > div.app-auth.module > table > tbody > tr.model-user > th > a")

    def __init__(self, driver):
        super().__init__(driver)

    def get_admin_page_title(self, title):
        """to get title of the page"""
        return self.get_title(title)

    def get_admin_page_header(self):
        """to get header name"""
        if self.element_is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)

    def click_on_view_site_link(self):
        """to click on "view site" link"""
        self.do_click(self.VIEW_SITE_LINK)

    def click_on_posts_link(self):
        """to click on "posts" link """
        self.do_click(self.POSTS_LINK)

    def get_account_name(self):
        """to get an account name"""
        if self.element_is_visible(self.USER_ACCOUNT_NAME):
            return self.get_element_text(self.USER_ACCOUNT_NAME)
