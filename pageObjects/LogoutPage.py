from locators.common_locators import CommonLocators
from pageObjects.BasePage import BasePage
from locators.login_locators import LoginPageLocators
from utilities.test_utils import sleep, SHORT_WAIT


class LogoutPage(BasePage):
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

    def click_logout(self):
        self.click_element("button_menu_xpath", self.locator.button_menu_xpath)
        sleep(SHORT_WAIT)
        self.click_element("hyperlink_logout_xpath", self.locator.hyperlink_logout_xpath)



