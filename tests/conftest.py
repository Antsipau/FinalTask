from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import psycopg2
from psycopg2 import Error
import requests
import pytest
import time
from config.config import TestData

chrome_options = Options()

chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    yield
    web_driver.close()


# @pytest.fixture(autouse=True)
# def new_user():
#     """Create new user"""
#     response = requests.post('https://petstore.swagger.io/v2/user', json={"id": 22814228, "username": "ivan_antsipau",
#                                                                           "firstName": "ivan", "lastName": "antsipau",
#                                                                           "email": "test@test.com", "password": "123",
#                                                                           "phone": "+7495000000", "userStatus": 9090})
#     return response
#
#
# @pytest.fixture(autouse=True)
# def login_user():
#     """Login user"""
#     response = requests.get('https://petstore.swagger.io/v2/user/login?username=ivan_antsipau&password=123',
#                             json={"username": "ivan_antsipau", "password": "123"})
#     return response
#
#
# @pytest.fixture(autouse=True)
# def find_user():
#     """Find information about user"""
#     response = requests.get('https://petstore.swagger.io/v2/user/ivan_antsipau')
#     return response
#
#
# @pytest.fixture(autouse=True)
# def logout_user():
#     """Logout user"""
#     response = requests.get('https://petstore.swagger.io/v2/user/logout?username=ivan_antsipau&password=123')
#     return response
#
#
# @pytest.fixture(autouse=True)
# def delete_user():
#     """Delete user"""
#     response = requests.delete('https://petstore.swagger.io/v2/user/string')
#     return response
#
#
# @pytest.fixture(autouse=True)
# def add_pet():
#     """Add a pet"""
#     response = requests.post('https://petstore.swagger.io/v2/pet',
#                              json={"id": 222222, "category": {"id": 1, "name": "rufus"},
#                                    "name": "doggie", "photoUrls": ["some URL"],
#                                    "tags": [{"id": 1, "name": "rufus"}],
#                                    "status": "available"})
#     return response
#
#
# @pytest.fixture(autouse=True)
# def find_pet():
#     """Find a pet"""
#     response = requests.get('https://petstore.swagger.io/v2/pet/222222')
#     return response
#
#
# @pytest.fixture(autouse=True)
# def update_pet():
#     """Update a pet"""
#     response = requests.put('https://petstore.swagger.io/v2/pet', json={"id": 222222,
#                                                                         "category": {"id": 1, "name": "gizmo"},
#                                                                         "name": "doggie", "photoUrls": ["some URL"],
#                                                                         "tags": [{"id": 1, "name": "gizmo"}],
#                                                                         "status": "available"})
#     return response
#
#
# @pytest.fixture(autouse=True)
# def find_update_pet():
#     """Find updated pet"""
#     response = requests.get('https://petstore.swagger.io/v2/pet/222222')
#     return response
