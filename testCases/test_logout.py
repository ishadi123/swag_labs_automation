from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from self import self

from pageObjects.LoginPage import LoginPage
from pageObjects.LogoutPage import LogoutPage
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT


class TestLogout:
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_username_standard()
    password = ReadConfig.get_password()
    username_visual_user = ReadConfig.get_username_visual_user()
    username_error_user = ReadConfig.get_username_error_user()
    logger = LogGen.loggen()

    def test_logout(self, setup):
        self.logger.info("***** TC_LG_001 - Started *****")
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = LoginPage(self.driver)
        self.login_page.login_to_application(self.username, self.password)
        sleep(SHORT_WAIT)
        self.logout_page = LogoutPage(self.driver)
        self.logout_page.click_logout()
        self.logger.info("Logged out successfully.")
        sleep(SHORT_WAIT)
        WebDriverWait(self.driver, SHORT_WAIT).until(EC.url_contains("https://www.saucedemo.com/"))
        assert "https://www.saucedemo.com/" in self.driver.current_url
        self.logger.info("Redirected to Login page after logout.")
        self.driver.close()
        sleep(SHORT_WAIT)
        self.logger.info("***** TC_LG_001 - Ended *****")

    def test_logout_with_different_users(self, setup):
        self.logger.info("***** TC_LG_002 - Started *****")
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = LoginPage(self.driver)
        # Login as an error user
        self.login_page.login_to_application(self.username_error_user, self.password)
        sleep(SHORT_WAIT)
        self.logout_page = LogoutPage(self.driver)
        self.logout_page.click_logout()
        self.logger.info("Logged out successfully.")
        WebDriverWait(self.driver, SHORT_WAIT).until(EC.url_contains("https://www.saucedemo.com/"))
        assert "https://www.saucedemo.com/" in self.driver.current_url
        self.logger.info("Redirected to Login page after logout.")
        sleep(SHORT_WAIT)
        # Login as a visual_user
        self.login_page.login_to_application(self.username_visual_user, self.password)
        self.logout_page = LogoutPage(self.driver)
        self.logout_page.click_logout()
        self.logger.info("Logged out successfully.")
        sleep(SHORT_WAIT)
        WebDriverWait(self.driver, SHORT_WAIT).until(EC.url_contains("https://www.saucedemo.com/"))
        assert "https://www.saucedemo.com/" in self.driver.current_url
        self.logger.info("Redirected to Login page after logout.")
        self.driver.close()
        sleep(SHORT_WAIT)
        self.logger.info("***** TC_LG_002 - Ended *****")

    def test_logout_and_browsing_back(self, setup):
        self.logger.info("***** TC_LG_003 - Started *****")
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = LoginPage(self.driver)
        self.login_page.login_to_application(self.username, self.password)
        sleep(SHORT_WAIT)
        self.logout_page = LogoutPage(self.driver)
        self.logout_page.click_logout()
        self.logger.info("Logged out successfully.")
        WebDriverWait(self.driver, SHORT_WAIT).until(EC.url_contains("https://www.saucedemo.com/"))
        assert "https://www.saucedemo.com/" in self.driver.current_url
        self.logger.info("Redirected to Login page after logout.")
        sleep(SHORT_WAIT)
        self.driver.back()
        assert "inventory.html" not in self.driver.current_url
        self.logger.info("User cannot access Products page after logout.")
        sleep(SHORT_WAIT)
        self.driver.close()
        sleep(SHORT_WAIT)
        self.logger.info("***** TC_LG_003 - Ended *****")
