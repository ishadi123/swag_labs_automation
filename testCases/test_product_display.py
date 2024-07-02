from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.ProductDisplayPage import ProductDisplayPage
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT


class TestProductPage:
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_username_standard()
    password = ReadConfig.get_password()
    invalid_username = ReadConfig.get_invalid_username()
    locked_username = ReadConfig.get_username_locked_out_user()
    logger = LogGen.loggen()

    def test_sort_products(self, setup):
        self.logger.info("***** TC_PDP_001 - Started *****")
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = LoginPage(self.driver)
        self.login_page.login_to_application(self.username, self.password)
        sleep(SHORT_WAIT)
        self.product_page = ProductDisplayPage(self.driver)

        # Verify sorting A to Z
        self.product_page.select_a_to_z_option()
        sleep(SHORT_WAIT)
        product_names = [element.text for element in self.driver.find_elements(By.CLASS_NAME, 'inventory_item_name')]
        self.logger.info(f"Products sorted A to Z: {product_names}")
        assert product_names == sorted(product_names)

        # Verify sorting Z to A
        self.product_page.select_z_to_a_option()
        sleep(SHORT_WAIT)
        product_names = [element.text for element in self.driver.find_elements(By.CLASS_NAME, 'inventory_item_name')]
        self.logger.info(f"Products sorted Z to A: {product_names}")
        assert product_names == sorted(product_names, reverse=True)

        # Verify sorting Price Low to High
        self.product_page.select_low_to_high_option()
        sleep(SHORT_WAIT)
        product_prices = [float(element.text.replace('$', '')) for element in
                          self.driver.find_elements(By.CLASS_NAME, 'inventory_item_price')]
        self.logger.info(f"Products sorted Price Low to High: {product_prices}")
        assert product_prices == sorted(product_prices)

        # Verify sorting Price High to Low
        self.product_page.select_high_to_low_option()
        sleep(SHORT_WAIT)
        product_prices = [float(element.text.replace('$', '')) for element in
                          self.driver.find_elements(By.CLASS_NAME, 'inventory_item_price')]
        self.logger.info(f"Products sorted Price High to Low: {product_prices}")
        assert product_prices == sorted(product_prices, reverse=True)

        self.logger.info("***** TC_PDP_001 - Ended *****")
        self.driver.close()
