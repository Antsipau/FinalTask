from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import psycopg2
import pytest

chrome_options = Options()

chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")


def test_create_new_user():
    """Creating new user as admin staff"""
    new_user = "user_as_admin_staff"
    driver = webdriver.Chrome('/home/jrankel/resources/chromedriver', options=chrome_options)
    driver.get('http://localhost:8000/')
    driver.implicitly_wait(10)
    driver.find_element(By.CLASS_NAME, "btn-primary").click()
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("password")
    driver.find_element(By.CSS_SELECTOR, "#login-form > div.submit-row > input[type=submit]").submit()
    driver.find_element(By.CSS_SELECTOR, "#content-main > div.app-auth.module > table > tbody > "
                                         "tr.model-user > td:nth-child(2) > a").click()
    driver.find_element(By.CLASS_NAME, "vTextField").send_keys(new_user)
    driver.find_element(By.NAME, "password1").send_keys("Marneuscalgar40k")
    driver.find_element(By.NAME, "password2").send_keys("Marneuscalgar40k")
    driver.find_element(By.CLASS_NAME, "default").submit()
    driver.find_element(By.ID, "id_is_staff").click()
    driver.find_element(By.ID, "id_is_superuser").click()
    driver.find_element(By.CSS_SELECTOR, "#user_form > div > div > input.default").submit()

    driver.find_element(By.CSS_SELECTOR, "#user-tools > a:nth-child(4)").click()
    driver.find_element(By.CSS_SELECTOR, "#content > p:nth-child(3) > a").click()
    driver.find_element(By.NAME, "username").send_keys(new_user)
    driver.find_element(By.NAME, "password").send_keys("Marneuscalgar40k")
    driver.find_element(By.CSS_SELECTOR, "#login-form > div.submit-row > input[type=submit]").submit()

    text = driver.find_element(By.ID, "user-tools").text
    assert f'Welcome, {new_user}'.lower() in text.lower(), "Welcome message for registered user"


def test_exist_new_user_in_db():
    """Test user exists in database"""
    new_user = "user_as_admin_staff"
    connection = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost")
    mycursor = connection.cursor()
    mycursor.execute("SELECT username FROM auth_user WHERE username='user_as_admin_staff'")
    search_user = mycursor.fetchall()
    for user in search_user:
        return user
    assert new_user == search_user, "User with name user_as_admin_staff exists in database"


def test_delete_new_user():
    """Test user delete from database"""
    result = []
    new_user = "user_as_admin_staff"
    connection = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost")
    mycursor = connection.cursor()
    mycursor.execute("DELETE FROM auth_user WHERE username='user_as_admin_staff'")
    connection.commit()
    mycursor.execute("SELECT username FROM auth_user")
    all_users = mycursor.fetchall()
    for i in all_users:
        result.append(i)
    assert new_user not in result, "User with name user_as_admin_staff doesn't exist in database"


