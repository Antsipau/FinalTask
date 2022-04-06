class TestData:
    CHROME_EXECUTABLE_PATH = "/home/jrankel/resources/chromedriver"
    FIREFOX_EXECUTABLE_PATH = "/home/jrankel/resources/geckodriver"

    BASE_URL = "http://localhost:8000/"
    # BASE_URL = "http://localhost:8000/admin/login/?next=/admin/"
    USER_NAME = "admin"
    PASSWORD = "password"
    ACCOUNT_NAME = "ADMIN"

    HOME_PAGE_TITLE = "Hello, world!"
    HOME_PAGE_HEADER_NAME = "About"
    GO_TO_ADMIN_BUTTON_NAME = "Go to Admin"

    LOGIN_PAGE_TITLE = "Log in | Django site admin"

    ADMIN_PAGE_TITLE = "Site administration | Django site admin"
    ADMIN_PAGE_HEADER = "Django administration"

    TEST_DATABASE_NAME = "TestGroup"
