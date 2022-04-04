class TestData:
    CHROME_EXECUTABLE_PATH = "/home/jrankel/resources/chromedriver"
    FIREFOX_EXECUTABLE_PATH = "/home/jrankel/resources/geckodriver"

    BASE_URL = "http://localhost:8000/"
    # BASE_URL = "http://localhost:8000/admin/login/?next=/admin/"
    USER_NAME = "admin"
    PASSWORD = "password"

    LOGIN_PAGE_TITLE = "Log in | Django site admin"
    HOME_PAGE_TITLE = "Hello, world!"
    GO_TO_ADMIN_BUTTON_NAME = "Go to Admin"
