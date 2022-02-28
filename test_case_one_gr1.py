from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import psycopg2
from psycopg2 import Error
import pytest

chrome_options = Options()

chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")


def test_open_main_mage():
    """Test that shows us that we can open main page"""
    driver = webdriver.Chrome('/home/jrankel/Resources/chromedriver', options=chrome_options)
    driver.get('http://localhost:8000/')
    driver.implicitly_wait(10)
    title = driver.title
    assert title == "Hello, world!"


def test_enter_admin_page():
    """Test that shows us that we can open admin page"""
    driver = webdriver.Chrome('/home/jrankel/Resources/chromedriver', options=chrome_options)
    driver.get('http://localhost:8000/')
    driver.implicitly_wait(10)
    driver.find_element(By.CLASS_NAME, "btn-primary").click()
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("password")
    driver.find_element(By.CSS_SELECTOR, "#login-form > div.submit-row > input[type=submit]").submit()
    title = driver.title
    assert title == "Site administration | Django site admin"


def test_show_group():
    """Test that shows us that we can open admin page"""
    try:
        connection = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost")
        mycursor = connection.cursor()
        mycursor.execute("INSERT INTO auth_group(name) VALUES('TestGroup')")
        connection.commit()
        mycursor.close()
        connection.close()
    except Error as e:
        print(f"Connection error {e} occurred")


    driver = webdriver.Chrome('/home/jrankel/Resources/chromedriver', options=chrome_options)
    driver.get('http://localhost:8000/')
    driver.implicitly_wait(10)
    driver.find_element(By.CLASS_NAME, "btn-primary").click()
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("password")
    driver.find_element(By.CSS_SELECTOR, "#login-form > div.submit-row > input[type=submit]").submit()
    driver.find_element(By.CSS_SELECTOR, "#content-main > div.app-auth.module > table > "
                                         "tbody > tr.model-group > th > a").click()
    group_name = driver.find_element(By.CSS_SELECTOR, "#result_list > tbody > tr > th > a").text
    assert group_name == "TestGroup"