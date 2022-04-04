from selenium.webdriver.common.by import By

from config.config import TestData
from pages.base_page import BasePage


class HomePage(BasePage):

    GO_TO_ADMIN_BUTTON = (By.CLASS_NAME, "btn-primary")
    NAVIGATION_BAR = (By.CLASS_NAME, "navbar-toggler")

    def __init__(self, driver):
        """constructor of the page class"""
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_home_page_title(self, title):
        """to get title of the page"""
        return self.get_title(title)

    def is_go_to_admin_button_exists(self):
        """to check that button exists"""
        return self.element_is_visible(self.GO_TO_ADMIN_BUTTON)

    def click_admin_button(self):
        """to check admin button is clickable"""
        self.do_click(self.GO_TO_ADMIN_BUTTON)

    def click_navbar(self):
        """"to check navbar is clickable"""
        self.do_click(self.NAVIGATION_BAR)

    def get_text_from_go_to_admin_button(self):
        """to check name of the "go to admin" button"""
        return self.get_element_text(self.GO_TO_ADMIN_BUTTON)



