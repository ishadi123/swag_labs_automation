import time
from utilities.helper import take_screenshot

SHORT_WAIT = 5
MEDIUM_WAIT = 7
LONG_WAIT = 10


def sleep(seconds):
    time.sleep(seconds)


def perform_login_invalid_credentials_assertion(driver, login_page, logger, success_message):
    if success_message in login_page.retrieve_error_message():
        assert True
        logger.info("********* Login with invalid username and valid password - Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "login_invalid_credentials_scr.png")
        logger.error("*********  Login with invalid username and valid password - Test Failed *********")
        assert False


def perform_locked_user_login_assertion(driver, login_page, logger, success_message):
    if success_message in login_page.retrieve_error_message_locked_user_login():
        assert True
        logger.info("********* Login locked user - Test Passed *********")
    else:
        take_screenshot(driver, ".\\Screenshots\\", "login_locked_user_scr.png")
        logger.error("*********  Login locked user - Test Failed *********")
        assert False
