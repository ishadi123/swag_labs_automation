from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.common_locators import CommonLocators
from pageObjects.BasePage import BasePage
from locators.login_locators import LoginPageLocators
# from locators.common_locators import CommonLocators
from utilities.test_utils import sleep, SHORT_WAIT


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = LoginPageLocators()
        self.locators = CommonLocators()

    def set_username(self, username):
        self.send_keys_to_element(username, "textbox_username_xpath", self.locator.textbox_username_xpath)

    def set_password(self, password):
        self.send_keys_to_element(password, "textbox_password_xpath", self.locator.textbox_password_xpath)

    def set_invalid_username(self, username):
        self.send_keys_to_element(username, "textbox_username_xpath", self.locator.textbox_username_xpath)

    def set_invalid_password(self, password):
        self.send_keys_to_element(password, "textbox_password_xpath", self.locator.textbox_password_xpath)

    def click_login(self):
        self.click_element("button_login_xpath", self.locator.button_login_xpath)

    def login_to_application(self, email_address_text, password_text):
        self.set_username(email_address_text)
        self.set_password(password_text)
        sleep(SHORT_WAIT)
        return self.click_login()

    def login_with_invalid_username_and_valid_password(self, email_address_text, password_text):
        self.set_invalid_username(email_address_text)
        self.set_password(password_text)
        return self.click_login()

    def click_logout(self):
        self.click_element("hyperlink_logout_xpath", self.locator.hyperlink_logout_xpath)

    def retrieve_error_message(self):
        return self.retrieve_element_text("error_message_xpath", self.locators.error_message_xpath)

    def retrieve_error_message_locked_user_login(self):
        return self.retrieve_element_text("error_message_locked_user_xpath",
                                          self.locators.error_message_locked_user_xpath)

