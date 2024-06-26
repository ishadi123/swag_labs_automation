from selenium.common import NoSuchElementException
from self import self
from pageObjects.LoginPage import LoginPage
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, perform_login_invalid_credentials_assertion, \
    perform_locked_user_login_assertion


class TestLogin:
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_username_standard()
    password = ReadConfig.get_password()
    invalid_username = ReadConfig.get_invalid_username()
    locked_username = ReadConfig.get_username_locked_out_user()
    logger = LogGen.loggen()

    def test_valid_login(self, setup):
        self.logger.info("***** TC_LF_001 - Started *****")
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = LoginPage(self.driver)
        self.login_page.login_to_application(self.username, self.password)
        sleep(SHORT_WAIT)

        try:
            title_element = self.login_page.find_element("title_xpath", "//span[@class='title']")
            assert title_element.is_displayed(), "Login failed or Products page not loaded"
            self.logger.info("Login successful, Products page loaded.")
        except NoSuchElementException as e:
            self.logger.error(f"Error: {e}")
            assert False, "Products page not loaded after login"

        self.driver.close()
        sleep(SHORT_WAIT)
        self.logger.info("***** TC_LF_001 - Ended *****")

    def test_invalid_login(self, setup):
        self.logger.info("***** TC_LF_002 - Started *****")
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = LoginPage(self.driver)
        try:
            self.login_page.login_with_invalid_username_and_valid_password(self.locked_username, self.password)
            success_message = 'Username and password do not match any user in this service'
            sleep(SHORT_WAIT)
            perform_login_invalid_credentials_assertion(self.driver, self.login_page, self.logger, success_message)

        except Exception as e:
            raise e
        self.logger.info("***** TC_LF_002 - Ended *****")
        self.driver.close()

    def test_locked_user_login(self, setup):
        self.logger.info("***** TC_LF_003 - Started *****")
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = LoginPage(self.driver)
        try:
            self.login_page.login_to_application(self.locked_username, self.password)
            success_message = 'Sorry, this user has been locked out.'
            sleep(SHORT_WAIT)
            perform_locked_user_login_assertion(self.driver, self.login_page, self.logger, success_message)

        except Exception as e:
            raise e
        self.logger.info("***** TC_LF_002 - Ended *****")
        self.driver.close()
