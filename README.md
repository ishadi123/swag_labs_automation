Instructions to Run Automation Project

1. Set Up Your Environment
Install Python: Ensure Python is installed on the system. 

2. Install Necessary Packages:
Selenium: pip install selenium
WebDriver Manager: pip install webdriver-manager
PyTest (for running tests): pip install pytest

3. Running Tests from the Terminal
Open the Terminal
To run the tests, specifying the file path and the browser:

pytest path/to/test_file.py --browser chrome
Example - pytest tests/test_login.py --browser chrome
