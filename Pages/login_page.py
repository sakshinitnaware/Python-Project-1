# Loging page code to automate the funtions of login with visibility and clickability of login button, loging with valid and invalid credentials. 

# Importing important Selenium library for wait, Expected conditions, Exceptions

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from time import sleep
from Locators.locator import locator


# Define a class to model actions on the Login Page
class LoginPage: 
    # Constructor to initialize the WebDriver and WebDriverWait
    def __init__(self, driver):
        # Assign the WebDriver instance
        self.driver = driver  
        # Create an explicit wait of 10 seconds
        self.wait = WebDriverWait(self.driver, 30)  # Create an explicit wait of 10 seconds

    def login_button_visible(self):
        try:
            # Wait until the login button is visible, then click it
            log_in_btn = self.wait.until(EC.visibility_of_element_located((By.XPATH, locator.LOGIN_BUTTON)))
            print("Login button clicked")
            sleep(5)
            return log_in_btn.is_displayed()
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException) as e:
            # Handle exceptions if element is not found, times out, or cannot be interacted with
            print("ERROR: Login button :", e)

    # Method to click the login button on the homepage
    def click_login_button(self):
        try:
            # Wait until the login button is clickable, then click it
            log_in_btn = self.wait.until(EC.visibility_of_element_located((By.XPATH, locator.LOGIN_BUTTON)))
            if log_in_btn.is_displayed() :
                self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.LOGIN_BUTTON))).click()
                print("Login button clicked")
                sleep(5)
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException) as e:
            # Handle exceptions if element is not found, times out, or cannot be interacted with
            print("ERROR: Login button :", e)

    # Method to enter the email into the email field
    def enter_email(self, email):
        try:
            # Wait until the email field is present in the DOM, then send keys
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator.EMAIL_FIELD))).send_keys(email)
            print("Entered email")
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException) as e:
            # Handle exceptions related to locating or interacting with the email field
            print("ERROR: Email field :", e)

    # Method to enter the password into the password field
    def enter_password(self, password):
        try:
            # Wait until the password field is present in the DOM, then send keys
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator.PASSWORD_FIELD))).send_keys(password)
            print("Entered password")
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException) as e:
            # Handle exceptions related to locating or interacting with the password field
            print("ERROR: Password field :", e)

    # Method to click the login/submit button to perform login
    def submit_login(self):
        try:
            # Wait until the submit button is clickable, then click to attempt login
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.LOGIN_SUBMIT))).click()
            print("Login submitted")
            sleep(10)
            pop_up = self.wait.until(EC.presence_of_element_located((By.XPATH, locator.LATER_BUTTON)))
            if pop_up.is_displayed() :
                pop_up.click()
                print("pop up dismissed")
            return self.wait.until(EC.presence_of_element_located((By.XPATH, locator.DROP_BOX)))
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException, Exception) as e:
            # Handle exceptions if the submit button is not available or not interactable
            print("ERROR: Submit login :", e)
            return False
