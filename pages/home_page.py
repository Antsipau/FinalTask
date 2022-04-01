from selenium.webdriver.common.by import By

from config.config import TestData
from pages.base_page import BasePage


class HomePage(BasePage):

    """By locators - OR"""
    GO_TO_ADMIN_BUTTON = (By.CLASS_NAME, "btn-primary")

    def __init__(self, driver):
        """constructor of the page class"""
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def click_admin_button(self):
        self.do_click(self.GO_TO_ADMIN_BUTTON)
