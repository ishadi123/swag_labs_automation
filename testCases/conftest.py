from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-notifications")
    if browser == "chrome":
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
    elif browser == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
