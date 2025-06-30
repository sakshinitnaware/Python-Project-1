# # Environment setup code for driver function

# Environment setup code for cross-browser driver function

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope="function")
def setup():
    driver = None

    try:
        # Try launching Chrome
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        print("Launched Chrome browser.")
    except Exception as e1:
        print("Chrome not available:", e1)
        try:
            # Try launching Firefox
            firefox_options = FirefoxOptions()
            firefox_options.add_argument("--start-maximized")
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
            print("Launched Firefox browser.")
        except Exception as e2:
            print("Firefox not available:", e2)
            try:
                # Try launching Edge
                edge_options = EdgeOptions()
                edge_options.add_argument("--start-maximized")
                driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)
                print("Launched Edge browser.")
            except Exception as e3:
                print("Edge not available:", e3)
                raise Exception("No supported browser is available on this system.")

    # Open target URL
    driver.get("https://www.guvi.in")
    yield driver
    driver.quit()




# # Importing the pytest module and Selenium WebDriver 
# import pytest
# from selenium import webdriver

# # Defining a fixture in pytest with function-level scope
# @pytest.fixture(scope="function")
# def setup():
#     # Creating a new Chrome browser instance
#     driver = webdriver.Chrome()
#     # Maximizing the browser window for better visibility
#     driver.maximize_window()
#     # Navigating to the GUVI website
#     driver.get("https://www.guvi.in")
#     # Yielding the driver instance to the test for execution
#     yield driver
#     # Closing the browser after the test is complete
#     driver.quit()

