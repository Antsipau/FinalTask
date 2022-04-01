from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import pytest

chrome_options = Options()

chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")


def test_delete_image():
    """Delete first image from the main page"""
    driver = webdriver.Chrome('/home/jrankel/resources/chromedriver', options=chrome_options)
    driver.get("http://localhost:8000/")
    driver.implicitly_wait(10)

    last_image_src = driver.find_element(By.CSS_SELECTOR, ".col-md-4:last-child .card-img-top").get_attribute('src')

    driver.find_element(By.CLASS_NAME, "btn-primary").click()
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("password")
    driver.find_element(By.CSS_SELECTOR, "#login-form > div.submit-row > input[type=submit]").submit()
    driver.find_element(By.CSS_SELECTOR, "#content-main > div.app-app.module > table > tbody > tr > th > a").click()
    driver.find_element(By.CSS_SELECTOR, "tr:last-child>.action-checkbox").click()
    select = Select(driver.find_element(By.CSS_SELECTOR, 'select[name="action"]'))
    select.select_by_visible_text('Delete selected posts')
    driver.find_element(By.CSS_SELECTOR, "button.button").click()
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
    driver.get("http://localhost:8000/")

    updated_last_image_src = driver.find_element(By.CSS_SELECTOR, ".col-md-4:last-child .card-img-top").get_attribute('src')

    assert last_image_src != updated_last_image_src, "Last image before updating page not equal after updating"
