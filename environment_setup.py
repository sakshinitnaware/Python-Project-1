# Environment setup code for driver function

# Importing the pytest module and Selenium WebDriver 
import pytest
from selenium import webdriver

# Defining a fixture in pytest with function-level scope
@pytest.fixture(scope="function")
def setup():
    # Creating a new Chrome browser instance
    driver = webdriver.Chrome()
    # Maximizing the browser window for better visibility
    driver.maximize_window()
    # Navigating to the GUVI website
    driver.get("https://www.guvi.in")
    # Yielding the driver instance to the test for execution
    yield driver
    # Closing the browser after the test is complete
    driver.quit()