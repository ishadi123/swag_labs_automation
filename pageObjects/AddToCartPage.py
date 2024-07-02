from locators.add_to_cart_locators import AddToCartPageLocators
from locators.login_locators import LoginPageLocators
from pageObjects.BasePage import BasePage
from utilities.test_utils import sleep, SHORT_WAIT


class AddToCartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.login_locators = LoginPageLocators()
        self.add_to_cart_locators = AddToCartPageLocators()

    def click_add_to_cart(self):
        self.click_element("button_add_to_cart_xpath", self.add_to_cart_locators.button_add_to_cart_xpath)
        sleep(SHORT_WAIT)

    def click_cart(self):
        self.click_element("hyperlink_cart_xpath", self.add_to_cart_locators.hyperlink_cart_xpath)
        sleep(SHORT_WAIT)

    def click_checkout(self):
        self.click_element("button_checkout_xpath", self.add_to_cart_locators.button_checkout_xpath)
        sleep(SHORT_WAIT)

    def set_firstname(self, first_name):
        self.send_keys_to_element(first_name, "input_first_name_xpath", self.add_to_cart_locators.
                                  input_first_name_xpath)
        sleep(SHORT_WAIT)

    def set_lastname(self, last_name):
        self.send_keys_to_element(last_name, "input_last_name_xpath", self.add_to_cart_locators.
                                  input_last_name_xpath)
        sleep(SHORT_WAIT)

    def set_zipcode(self, zip_code):
        self.send_keys_to_element(zip_code, "input_zip_code_xpath", self.add_to_cart_locators.
                                  input_zip_code_xpath)
        sleep(SHORT_WAIT)

    def set_checkout(self, first_name, last_name, zip_code):
        self.set_firstname(first_name)
        sleep(SHORT_WAIT)
        self.set_lastname(last_name)
        sleep(SHORT_WAIT)
        self.set_zipcode(zip_code)
        sleep(SHORT_WAIT)

    def click_continue(self):
        self.click_element("button_continue_xpath", self.add_to_cart_locators.button_continue_xpath)
        sleep(SHORT_WAIT)

    def click_finish(self):
        self.click_element("button_finish_xpath", self.add_to_cart_locators.button_finish_xpath)

    def retrieve_message_successfully_check_out(self):
        return self.retrieve_element_text("heading_thank_you_xpath",
                                          self.add_to_cart_locators.heading_thank_you_xpath)

    def click_back_to_home(self):
        self.click_element("button_back_to_home_xpath", self.add_to_cart_locators.button_back_to_home_xpath)

    def click_remove(self):
        self.click_element("button_remove_item_xpath", self.add_to_cart_locators.button_remove_item_xpath)

    def get_cart_count(self):
        try:
            cart_count_element = self.find_element("span_cart_count_xpath",
                                                   self.add_to_cart_locators.span_cart_count_xpath)
            return int(cart_count_element.text)
        except:
            return 0
