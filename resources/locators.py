from selenium.webdriver.common.by import By


class WebAppLocators:

    GO_TO_ADMIN_BTN = (By.LINK_TEXT, 'Go to Admin')

    USERNAME_FIELD = (By.CSS_SELECTOR, "input[type='text']")

    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[type="password"]')

    LOGIN_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')

    LIST_OF_GROUPS = (By.LINK_TEXT, 'Groups')


class TestCase1Locators:

    EXPECTED_TEST_GROUP = (By.LINK_TEXT, "TestGroup")

    ADD_USER_BUTTON = (By.CSS_SELECTOR, ".model-user>td>.addlink")

    ADD_USER_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="username"]')

    ADD_USER_PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[name="password1"]')

    ADD_USER_PASSWORD_CONFIRMATION_FIELD = (By.CSS_SELECTOR, 'input[name="password2"]')

    SAVE_NEW_USER_BUTTON = (By.CSS_SELECTOR, '.default')

    SUCCESS_MESSAGE_LOCATOR = (By.CSS_SELECTOR, 'li.success>a')

    USERS_BUTTON = (By.CSS_SELECTOR, '.model-user>[scope="row"]>a')

    TEST_USER_ELEMENT = (By.LINK_TEXT, 'TestName')

    TEST_GROUP_IN_SELECT_GROUP = (By.CSS_SELECTOR, '[title="TestGroup"]')

    FORWARD_ARROW = (By.CSS_SELECTOR, "#id_groups_add_link")

    TEST_GROUP_IN_USER_PAGE_ELEMENT = (By.LINK_TEXT, 'TestName')


class TestGroup2Locators:

    THE_VERY_LAST_IMAGE = (By.CSS_SELECTOR, '.col-md-4:last-child .card-img-top')

    POSTS_BUTTON = (By.LINK_TEXT, 'Posts')

    THE_VERY_LAST_POST_CHECKBOX = (By.CSS_SELECTOR, 'tr:last-child>.action-checkbox')

    SELECT_POST_TO_CHANGE_ELEMENT = (By.CSS_SELECTOR, 'select[name="action"]')

    GO_BUTTON = (By.CSS_SELECTOR, "button.button")

    YES_IM_SURE_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')

    ADD_USER_BUTTON = (By.CSS_SELECTOR, ".model-user>td>.addlink")

    ADD_USER_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="username"]')

    ADD_USER_PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[name="password1"]')

    ADD_USER_PASSWORD_CONFIRMATION_FIELD = (By.CSS_SELECTOR, 'input[name="password2"]')

    LOG_OUT_BTN = (By.CSS_SELECTOR, "#user-tools>a:nth-child(4)")

    ADD_STAFF_STATUS_BTN = (By.ID, 'id_is_staff')

    GREETINGS_MESSAGE_FIELD = (By.CSS_SELECTOR, '#user-tools')
