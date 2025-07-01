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
        # Try launching Chrome in headless mode
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        print("Launched Chrome in headless mode.")
    except Exception as e1:
        print("Chrome not available:", e1)
        try:
            # Try launching Firefox in headless mode
            firefox_options = FirefoxOptions()
            firefox_options.add_argument("--headless")
            firefox_options.add_argument("--no-sandbox")
            firefox_options.add_argument("--disable-dev-shm-usage")
            firefox_options.add_argument("--window-size=1920,1080")
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
            print("Launched Firefox in headless mode.")
        except Exception as e2:
            print("Firefox not available:", e2)
            try:
                # Try launching Edge in headless mode
                edge_options = EdgeOptions()
                edge_options.add_argument("--headless=new")
                edge_options.add_argument("--no-sandbox")
                edge_options.add_argument("--disable-dev-shm-usage")
                edge_options.add_argument("--window-size=1920,1080")
                driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)
                print("Launched Edge in headless mode.")
            except Exception as e3:
                print("Edge not available:", e3)
                raise Exception("No supported browser is available in headless mode on this system.")

    # Load target website
    driver.get("https://www.guvi.in")
    yield driver
    driver.quit()
