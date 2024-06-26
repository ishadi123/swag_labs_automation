import os


def take_screenshot(driver, folder, filename):
    screenshot_path = os.path.join(folder, filename)
    driver.save_screenshot(screenshot_path)
    return screenshot_path
