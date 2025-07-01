# Test Script code to Automate the test cases 

# Importing important Pytest library and files   
import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment_setup import setup
from Pages.login_page import LoginPage
from Pages.sign_in_page import SignUpPage
from Pages.dashboard_page import DashboardPage
from TestData import data

# Test Case 1: Check if the URL is correct after launching the site
def test_tc_1_url_validity(setup):
    # Assert that the current URL contains "guvi.in"
    assert "guvi.in" in setup.current_url, "URL is not valid"
    print("PASS : URL TEST")


# Test Case 2: Check if the title of the homepage is correct
def test_tc_2_title_check(setup):
    # Expected title of the GUVI homepage
    expected_title = "GUVI | Learn to code in your native language"
    # Assert that the actual title matches the expected title
    assert setup.title == expected_title, f"Expected title '{expected_title}', got '{setup.title}'"
    print("PASS : TITLE TEST")


# Test Case 3: Verify login button is Visible, clickable and navigates correctly
def test_tc_3_login_button_clickable(setup):
    # Create instance of LoginPage using setup (WebDriver)
    login = LoginPage(setup)
    # Click the login button
    #assert login.login_button_visible(), "Login button did not navigate to login page"
    # Assert that after clicking, URL contains 'login'
    login.click_login_button()
    assert "sign-in" in setup.current_url.lower(), "Login button did not navigate to login page"
    print("PASS : LOGIN BUTTON VISIBLE AND CLICKABLE")


# # Test Case 4: Verify the Sign-Up button is Visible, clickable and functional
def test_tc_4_signup_button_clickable(setup):
    # Create instance of SignUpPage
    signup = SignUpPage(setup)
    # Click the Sign-Up button
    signup.click_sign_up_button()
    # Assert the URL changed to include 'sign-in'
    assert "register" in setup.current_url.lower(), "Sign-Up button did not navigate correctly"
    print("PASS : SIGN-IN BUTTON VISIBLE AND CLICKABLE")

# Test Case 5: Verify clicking the Sign-Up button redirects to correct URL
def test_tc_5_signup_redirect(setup):
    # Create instance of SignUpPage
    signup = SignUpPage(setup)
    # Click the Sign-Up button
    signup.click_sign_up_button()
    # Assert the redirected URL is exactly as expected
    assert setup.current_url == "https://www.guvi.in/register/", "Sign-Up did not redirect to sign-in page"
    print("PASS : SIGN-IN BUTTON REDIDETED TO SIGN-IN PAGE")

# Test Case 6: Test login with valid credentials
def test_tc_6_valid_login(setup):
    # Create instance of LoginPage
    login = LoginPage(setup)
    # Click login button to open login form
    login.click_login_button()
    # Enter a valid email
    login.enter_email(data.VALID_EMAIL)
    # Enter a valid password
    login.enter_password(data.VALID_PASSWORD)
    # Assert that user is redirected to dashboard or profile page
    assert login.submit_login(), "Login failed with valid credentials"
    print("PASS : VALID LOGIN")
    
# Test Case 7: Test login with invalid credentials
def test_tc_7_invalid_login(setup):
    # Create instance of LoginPage
    login = LoginPage(setup)
    # Click login button to open login form
    login.click_login_button()
    # Enter invalid email
    login.enter_email(data.INVALID_EMAIL)
    # Enter invalid password
    login.enter_password(data.INVALID_PASSWORD)
    # Submit login form
    login.submit_login()
    # Assert that login fails and error message or page is shown
    assert "Invalid" in setup.page_source or "error" in setup.page_source or "login" in setup.current_url.lower(), "Login succeeded with invalid credentials"
    print("PASS : INVALID LOGIN")

# Test Case 8: Verify that all top navigation menu items are visible
def test_tc_8_top_menu_items(setup):
    # Create instance of loginPage
    login = LoginPage(setup)
    login.click_login_button()
    # Enter a valid email
    login.enter_email(data.VALID_EMAIL)
    # Enter a valid password
    login.enter_password(data.VALID_PASSWORD)
    # Submit login form
    login.submit_login()
    # Create instance of DashboardPage after login
    print("DashBoard instance")
    dashboard = DashboardPage(setup)
    # Assert that all expected top menu items are visible
    assert dashboard.top_menu_bar(), "Top menu items are missing or not visible"
    print("PASS : ALL THE TABS ON MENU ARE VISIBLE")

# Test Case 9: Verify that the Dobby chatbot is visible on the homepage
def test_tc_9_dobby_visible(setup):
    # Create instance of loginPage
    login = LoginPage(setup)
    login.click_login_button()
    # Enter a valid email
    login.enter_email(data.VALID_EMAIL)
    # Enter a valid password
    login.enter_password(data.VALID_PASSWORD)
    # Submit login form
    login.submit_login()
    # Create instance of DashboardPage after login
    dashboard = DashboardPage(setup)
    # Assert that the Dobby Assistant is visible
    assert dashboard.is_dobby_visible(), "Dobby Guvi Assistant not visible on homepage"
    print("PASS : DOBBY IS VISIBLE")

# Test Case 10: Test logout functionality after a successful login
def test_tc_10_logout_functionality(setup):
    # Create instance of LoginPage
    login = LoginPage(setup)
    # Click login button to open form
    login.click_login_button()
    # Enter valid email
    login.enter_email(data.VALID_EMAIL)
    # Enter valid password
    login.enter_password(data.VALID_PASSWORD)
    # Submit login form
    login.submit_login()
    # Create instance of DashboardPage after login
    dashboard = DashboardPage(setup)
    # Perform logout
    dashboard.logout()
    # Assert that user is redirected to login or homepage
    assert "login" in setup.current_url.lower() or "guvi.in" in setup.current_url, "Logout failed"
    print("PASS : LOGOUT WEBPAGE")
