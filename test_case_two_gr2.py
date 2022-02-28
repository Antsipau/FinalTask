# 1.Открыть приложение
# 2.Войти в админку
# 3. Удалить первое созданное изображение
# 4. Вернуться на главную страницу
# 5. Убедиться, что первое изображение не отображается на странице
import time

from selenium.common.exceptions import NoSuchElementException

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pytest

chrome_options = Options()

chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")

def test_delete_image():
    """Delete first image from the main page"""
    driver = webdriver.Chrome('/home/jrankel/Resources/chromedriver')
    driver.get('http://localhost:8000/')
    driver.implicitly_wait(10)
    last_image_src = driver.find_element(By.CSS_SELECTOR, ".col-md-4:last-child .card-img-top").get_attribute('src')


    driver.find_element(By.CLASS_NAME, "btn-primary").click()
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("password")
    driver.find_element(By.CSS_SELECTOR, "#login-form > div.submit-row > input[type=submit]").submit()
    driver.find_element(By.CSS_SELECTOR, "#content-main > div.app-app.module > table > tbody > tr > th > a").click()
    driver.find_element(By.CSS_SELECTOR, "tr:last-child>.action-checkbox").click()
    select = Select(driver.find_element(By.NAME, "action"))




    # driver.find_elements(By.XPATH, '//*[@id="result_list"]/tbody/tr')[-1].find_element(By.CSS_SELECTOR, "th > a").click()
    # image_uri = driver.find_element(By.CSS_SELECTOR, "#id_photo").text
    # driver.find_element(By.CSS_SELECTOR, "#post_form > div > div > p > a").click()
    # driver.find_element(By.CSS_SELECTOR, '#content > form > div > input[type=submit]:nth-child(2)').submit()
    # driver.find_element(By.CSS_SELECTOR, "#user-tools > a:nth-child(2)").click()
    # last_uri = driver.find_elements(By.XPATH, '/html/body/main/div/div/div/div')[-1].find_element(By.CSS_SELECTOR, "div > img").get_attribute('src')
    # assert image_uri not in last_uri
    #
    time.sleep(5)
