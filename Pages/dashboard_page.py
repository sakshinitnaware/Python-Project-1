# Dashboard page code to automate the funtions of validating the Menu bar tabs and Ai chat bot 

# Importing important Selenium library for wait, Expected conditions, Exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from time import sleep
from Locators.locator import locator


# Define a class to handle interactions on the Dashboard page
class DashboardPage: 
    # Constructor to initialize WebDriver and WebDriverWait
    def __init__(self, driver):
        self.driver = driver  # Store the WebDriver instance
        self.wait = WebDriverWait(self.driver, 30)  # Set up an explicit wait of 10 seconds

    # Method to verify visibility of top navigation menu items
    def top_menu_bar(self):
        try:
            print("starting the menu bar test case")
            # If current URL is not homepage, click on GUVI logo to go to homepage
            sleep(10)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.LATER_BUTTON))).click()
            print("Current URL:", self.driver.current_url)
            if "courses" in self.driver.current_url or "dashboard" in self.driver.current_url:
                print("Redirecting to homepage")
                # clickon the GUVI Logo to redirect to guvi.in
                redirecting_guvi = self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.GUVI_LOGO)))
                redirecting_guvi.click()
                # Wain until the webpage loads completely
                self.wait.until(EC.url_contains("guvi.in"))
                sleep(50)
            print("Checking the top menu items")
            # Check visibility of all required menu items
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator.COURSE_MENU)))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator.LIVE_CLASSES_MENU)))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator.PRACTICE_MENU)))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator.RESOURCES_MENU)))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator.PRODUCTS_MENU)))
            print("All top menu items are visible")
            # Return True if all elements are visible
            return True 
        except (NoSuchElementException, TimeoutException) as e:
            # Handle missing or delayed elements
            print("ERROR: Menu items :", e)
            # Return False if any item is not found
            return False  

    # Method to verify if the Dobby Assistant chatbot is visible
    def is_dobby_visible(self):
        try:
            # Redirecting to Guvi.in 
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.GUVI_LOGO))).click()
            print("rediredted to Guvi.in")
            sleep(15)
            # Wait until the Dobby chatbot is visible on the page
            print("landed on guvi")
            ai_bot = self.wait.until(EC.visibility_of_element_located((By.XPATH, locator.DOBBY_ASSISTANT)))
             # Log success
            print("Dobby is visible") 
            # Return True if element is displayed
            return ai_bot.is_displayed()  
        # Handle error if Dobby is not visible or fails to load
        except (NoSuchElementException, TimeoutException) as e:
            print("ERROR: Dobby Assistant :", e)
            # Return False if not found or not visible
            return False  

    # Method to perform logout from the dashboard
    def logout(self):
        try:
            # Redirecting to Guvi.in 
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.GUVI_LOGO))).click()
            # Wait and click on the dropdown to show logout option
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.DROP_BOX))).click()
            # Wait and click on the "Sign Out" or logout button
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.LOGOUT_BUTTON))).click()
            # Log success
            print("Logged out successfully")  
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException) as e:
            # Handle error if logout flow fails
            print("ERROR: Logout process :", e)
