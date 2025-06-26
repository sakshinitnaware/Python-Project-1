# Define a class to store element locators used for automation
class locator:
    # LOGIN XPATH Locator
    LOGIN_BUTTON = "//*[@id='login-btn']"
    # SIGNUP XPATH Locator
    SIGNUP_BUTTON = "//a[text()='Sign up']"
    # EMAIL FIELD XPATH Locator
    EMAIL_FIELD = "//input[@id='email']"
    # PASSWORD FIELD XPATH Locator
    PASSWORD_FIELD = "//input[@id='password']"
    # LOGIN SUBMIT BUTTON XPATH Locator
    LOGIN_SUBMIT = "//*[@id='login-btn']"
    # LATER BUTTON XPATH Locator to dismiss the pop-up
    LATER_BUTTON = "//button[text()='Later' and contains(@class, 'border-primary')]"
    GUVI_LOGO = "//a[img[contains(@class, 'guvi_logo')]]"
    
    # Post-login to logout there is Dropdown and then Logout XPATH Locator
    DROP_BOX = "//*[@id='dropdown_contents']"
    PROFILE = "//img[@alt='Profile' and contains(@src, 'guvi-profile-images')]"
    LOGOUT_BUTTON = "//*[@id='dropdown_contents']//*[contains(text(), 'Sign Out')]"

    # Top Menu Navigation XPATH Locator
    COURSE_MENU = "//a[@href='/courses/' and contains(text(), 'Courses')]"
    LIVE_CLASSES_MENU = "//*[@id='liveclasseslink']"
    PRACTICE_MENU = "//*[@id='practiceslink']"
    RESOURCES_MENU = "//*[@id='resourceslink']"
    PRODUCTS_MENU = "//*[@id='solutionslink']"

    # Chatbot XPATH Locator
    DOBBY_ASSISTANT = "//*[@id='chateleon-container-gif-0']"
