# GUVI Web Application - Automation Testing Framework

**This project is an automation testing framework built to validate key functionalities of the GUVI Web Application. Using Selenium, Pytest, and 
the Page Object Model (POM) design pattern, the framework ensures modularity, readability, and ease of maintenance.
The primary focus is on automating and verifying core workflows like login, signup, dashboard UI elements, and logout. 
POM is used to separate test logic from page interactions, making the codebase scalable and easy to update when UI changes occur. 
Locators and test data are maintained centrally to enhance control and reduce redundancy.The framework supports cross-browser testing 
and headless execution, making it suitable for both local runs and CI/CD pipelines. It generates structured JSON reports on every run 
and includes logic to re-run failed tests to capture flaky behavior. A merged HTML report compiles the results from multiple retries, 
showing each test case’s outcomes across trials and summarizing their final status.This project serves as a robust foundation for web 
automation, with flexible architecture and clear reporting. It's ideal for quality 
assurance teams aiming to automate UI testing for web apps in an efficient and organized manner.**

## 🔧 Tech Stack
- Selenium
- Pytest
- Page Object Model (POM)
- Python

## 📁 Folder Structure
```
Project-1/
│
├── pages/
│ ├── login_page.py
│ ├── sign_up_page.py
│ └── dashboard_page.py
│
├── Reports/
│ ├── assets/
│ ├── firsttest_report.json
│ ├── merge_report_script.py
│ ├── merged_final_report.html
│ ├── merged_report.json
│ ├── retest_report1.json
│ ├── retest_report2.json
│ ├── retest_report3.json
│ └── retest_report4.json
│
├── locators/
│ └── locators.py
│
├── data/
│ └── test_data.py
│
├── tests/
│ └── test_guvi.py
│
├── environment_setup.py
```

- pages/: Page classes for modular automation
- locators/: Centralized locator storage
- reports/: Storing the results
- data/: Test data
- tests/: Test cases
- environment_setupt.py: Fixtures and setup


## 🔩 Features
- Cross-browser compatible (with browser driver setup)
- Positive and negative login and sign-up test cases
- UI element verification for dashboaard and AI bot
- Page redirection and logout testing

## Test Case Discription

| Test Case Name                      | Description                                            |
| ----------------------------------- | ------------------------------------------------------ |
| test_tc_1_url_validity            | Verifies if the GUVI website loads with a valid URL.   |
| test_tc_2_title_check             | Validates that the webpage title is correct.           |
| test_tc_3_login_button_clickable  | Checks if the login button is visible and clickable.   |
| test_tc_4_signup_button_clickable | Checks if the signup button is visible and clickable.  |
| test_tc_5_signup_redirect         | Ensures clicking signup redirects to the signup page.  |
| test_tc_6_valid_login             | Verifies login functionality with valid credentials.   |
| test_tc_7_invalid_login           | Ensures error handling for incorrect login details.    |
| test_tc_8_top_menu_items          | Validates that all top menu items are present.         |
| test_tc_9_dobby_visible           | Checks if the “Dobby” element is displayed post-login. |
| test_tc_10_logout_functionality   | Confirms that logout functionality works as expected.  |


## How to run 
To execute the automated test suite and generate reports, follow the steps below:

1. **Install dependencies** (if not already installed):
2. **Run all test cases and generate a full HTML report** : pytest TestScript/testscript.py -d -s --html=Reports/report.html
   If the test cases have inconsistent fails and errors you can try with the below steps to avoid hassel but the
   below cmd will generate .json report and then we need to converte to html by exucuting scrip.
          **Run all test cases and generate a full report**: pytest TestScript/testscript.py -s --json-report --json-report-file=Reports/firsttest_report.json
          **(Optional) Re-run only failed test cases (for retries):** pytest TestScript/testscript.py -s --lf --json-report --json-report-file=Reports/retest_reportX.json
         
## How to generate the final html reports by merging all the .json results 
  execute the below command and the final merged report will be generated.
  python merge_report_script.py


## Test Results 
![Test Screenshot](Reports/TestScreenshot.png)
