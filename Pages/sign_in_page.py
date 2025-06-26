# Sign in page code to automate the funtions of Sign-in  with visibility and clickability of sign-in button,  

# Importing important Selenium library for wait, Expected conditions, Exceptions
import os
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from time import sleep
from Locators.locator import locator


class SignUpPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def click_sign_up_button(self):
        try:
            sign_in_btn_visible = self.wait.until(EC.visibility_of_element_located((By.XPATH, locator.SIGNUP_BUTTON)))
            if sign_in_btn_visible.is_displayed() :
                self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.SIGNUP_BUTTON))).click()
                print("Sign-Up button clicked")
                sleep(10)
            else :
                print("couldnt find sign in button",Exception)
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException) as e:
            print("ERROR: Sign-Up button :", e)
