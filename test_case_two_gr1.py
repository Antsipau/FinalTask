# TC_2:
#     1. Открыть приложение
#     2. Войти в админку
#     3. Создать пользователя
#     4. Добавить созданного пользователя в группу
#     5. Проверить, что в базе данных пользователь добавлен в группу
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import psycopg2
import pytest

chrome_options = Options()

chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")


def test_create_user():
    """Create and add user to the group"""
    driver = webdriver.Chrome('/home/jrankel/Resources/chromedriver', options=chrome_options)
    driver.get('http://localhost:8000/')
    driver.implicitly_wait(10)
    driver.find_element(By.CLASS_NAME, "btn-primary").click()
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("password")
    driver.find_element(By.CSS_SELECTOR, "#login-form > div.submit-row > input[type=submit]").submit()
    driver.find_element(By.CSS_SELECTOR, "#content-main > div.app-auth.module > table > tbody > "
                                         "tr.model-user > td:nth-child(2) > a").click()
    driver.find_element(By.CLASS_NAME, "vTextField").send_keys("user_one")
    driver.find_element(By.NAME, "password1").send_keys("Marneuscalgar40k")
    driver.find_element(By.NAME, "password2").send_keys("Marneuscalgar40k")
    driver.find_element(By.CLASS_NAME, "default").submit()
    driver.find_element(By.CSS_SELECTOR, "#id_groups_add_all_link").click()
    driver.find_element(By.CSS_SELECTOR, "#user_form > div > div > input.default").submit()

    connection = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost")
    mycursor = connection.cursor()
    mycursor.execute("SELECT id FROM auth_user WHERE username='user_one'")
    search_user_id_in_auth_user = mycursor.fetchall()

    mycursor.execute("SELECT user_id FROM auth_user_groups")
    search_user_id_in_auth_user_groups = mycursor.fetchall()

    result = []
    for i in search_user_id_in_auth_user:
        for j in search_user_id_in_auth_user_groups:
            if i == j:
                result.append(i)
    assert search_user_id_in_auth_user == result


def test_delete_info():
    connection = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost")
    mycursor = connection.cursor()
    mycursor.execute("DELETE FROM auth_user_groups")
    connection.commit()
    mycursor.execute("DELETE FROM auth_user WHERE username='user_one'")
    connection.commit()





