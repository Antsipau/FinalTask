from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This class is the parent of all pages. It contains all the generic methods and utilities for all the pages"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self, title):
        """to get the title of the page"""
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def get_element_text(self, by_locator):
        """to get name of element"""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def element_is_visible(self, by_locator):
        """to know that element is visible"""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def element_is_enabled(self, by_locator):
        """to know that element is enabled"""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def do_click(self, by_locator):
        """to do click on element"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_key(self, by_locator, text):
        """to send some key into field"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)






