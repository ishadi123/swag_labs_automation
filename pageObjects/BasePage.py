from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator_name, locator_value):
        # element = self.get_element(locator_name, locator_value)
        # element.click()
        try:
            element = self.get_element(locator_name, locator_value)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, locator_value)))
            element.click()
        except Exception as e:
            print(f"Error clicking element {locator_name}: {e}")

    def send_keys_to_element(self, text, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.send_keys(text)

    def find_element(self, locator_name, locator_value):
        return self.get_element(locator_name, locator_value)

    def retrieve_element_text(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.text

    def get_element(self, locator_name, locator_value):
        element = None
        if locator_name.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_name.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_name.endswith("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_name.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_name.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_name.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element

    def quit(self):
        self.driver.quit()
