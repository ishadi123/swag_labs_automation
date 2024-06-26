from locators.common_locators import CommonLocators
from locators.login_locators import LoginPageLocators
from locators.product_display_locators import ProductDisplayPageLocators
from pageObjects.BasePage import BasePage
from utilities.test_utils import sleep, SHORT_WAIT


class ProductDisplayPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_locator = LoginPageLocators()
        self.locator = ProductDisplayPageLocators()
        self.locators = CommonLocators()

    def click_product_sort_container(self):
        self.click_element("select_product_sort_container_xpath", self.locator.select_product_sort_container_xpath)

    def select_a_to_z_option(self):
        self.click_product_sort_container()
        sleep(SHORT_WAIT)
        self.click_element("option_a_to_z_xpath", self.locator.option_a_to_z_xpath)

    def select_z_to_a_option(self):
        self.click_product_sort_container()
        sleep(SHORT_WAIT)
        self.click_element("option_z_to_a_xpath", self.locator.option_z_to_a_xpath)

    def select_low_to_high_option(self):
        self.click_product_sort_container()
        sleep(SHORT_WAIT)
        self.click_element("option_low_to_high_xpath", self.locator.option_low_to_high_xpath)

    def select_high_to_low_option(self):
        self.click_product_sort_container()
        sleep(SHORT_WAIT)
        self.click_element("option_high_to_low_xpath", self.locator.option_high_to_low_xpath)
