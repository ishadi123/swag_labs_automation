from TestData.add_to_cart_test_data import AddToCartTestData
from pageObjects.AddToCartPage import AddToCartPage
from pageObjects.LoginPage import LoginPage
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities.test_utils import sleep, SHORT_WAIT, perform_check_out_assertion


class TestAddToCartPage:
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_username_standard()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_add_to_cart(self, setup):
        self.logger.info("")
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = LoginPage(self.driver)
        self.login_page.login_to_application(self.username, self.password)
        sleep(SHORT_WAIT)
        self.add_to_cart_page = AddToCartPage(self.driver)

        # Get initial cart count
        self.logger.info("Check cart count before and after add an item")
        initial_cart_count = self.add_to_cart_page.get_cart_count()
        self.logger.info(f"Initial cart count: {initial_cart_count}")

        self.add_to_cart_page.click_add_to_cart()

        # Get updated cart count
        updated_cart_count = self.add_to_cart_page.get_cart_count()
        self.logger.info(f"Updated cart count: {updated_cart_count}")

        # Verify cart count is incremented by 1
        assert updated_cart_count == initial_cart_count + 1, "Cart count did not update correctly after adding item"

        self.add_to_cart_page.click_cart()
        self.add_to_cart_page.click_checkout()
        self.add_to_cart_page.set_checkout(AddToCartTestData.first_name, AddToCartTestData.last_name,
                                           AddToCartTestData.zip_code)
        self.add_to_cart_page.click_continue()
        self.add_to_cart_page.click_finish()
        success_message = 'Thank you for your order!'
        sleep(SHORT_WAIT)
        perform_check_out_assertion(self.driver, self.add_to_cart_page, self.logger, success_message)
        sleep(SHORT_WAIT)
        self.add_to_cart_page.click_back_to_home()
        sleep(SHORT_WAIT)

        # Remove Item

        # Initial cart count before remove
        self.logger.info("Check cart count before and after remove an item")
        initial_cart_count = self.add_to_cart_page.get_cart_count()
        self.logger.info(f"Initial cart count : {initial_cart_count}")

        self.add_to_cart_page.click_add_to_cart()

        # Get updated cart count
        updated_cart_count = self.add_to_cart_page.get_cart_count()
        self.logger.info(f"Updated cart count after add item: {updated_cart_count}")

        # Verify cart count is incremented by 1
        assert updated_cart_count == initial_cart_count + 1

        self.add_to_cart_page.click_remove()

        # Get updated cart count
        updated_cart_count = self.add_to_cart_page.get_cart_count()
        self.logger.info(f"Updated cart count after remove: {updated_cart_count}")

        sleep(SHORT_WAIT)
        self.driver.close()
