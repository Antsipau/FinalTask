from selenium.webdriver.common.by import By

from config.config import TestData
from pages.base_page import BasePage


class AdminPage(BasePage):

    ACCOUNT_NAME = (By.CSS_SELECTOR, "#user-tools > strong")
    VIEW_SITE_LINK = (By.CSS_SELECTOR, "#user-tools > a:nth-child(2)")
    CHANGE_PASSWORD_LINK = (By.CSS_SELECTOR, "#user-tools > a:nth-child(3)")
    LOG_OUT_LINK = (By.CSS_SELECTOR, "#user-tools > a:nth-child(4)")
    POSTS_LINK = (By.CSS_SELECTOR, "#content-main > div.app-app.module > table > tbody > tr > th > a")
    GROUPS_BUTTON = (By.CSS_SELECTOR, "#content-main > div.app-auth.module > table > tbody > tr.model-group > th > a")
    USERS_LINK = (By.CSS_SELECTOR, "#content-main > div.app-auth.module > table > tbody > tr.model-user > th > a")

    def __init__(self, driver):
        super().__init__(driver)

    def get_admin_page_title(self, title):
        return self.get_title(title)

    def click_on_view_site_link(self):
        self.do_click(self.VIEW_SITE_LINK)

    def click_on_posts_button(self):
        self.do_click()

    def get_account_name(self):
        if self.element_is_visible(self.ACCOUNT_NAME):
            return self.get_element_text(self.ACCOUNT_NAME)



