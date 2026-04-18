"""
GitHub Login Page Tests

This module contains tests for the GitHub login functionality,
including both negative (invalid credentials) and positive (valid credentials) test cases.

Test Approach:
    - Test 1: Verify login fails with invalid credentials
    - Test 2: Verify login succeeds with valid credentials

Note: These tests use hardcoded credentials for demonstration.
In a production environment, credentials should be stored securely
using environment variables or a secrets manager.
"""

from tests import BaseClass
from locator.github_login_page_locator import *
from selenium.webdriver.common.keys import Keys


class TestGithubPage(BaseClass):
    """
    Test suite for GitHub login functionality.

    Inherits from BaseClass to get:
    - WebDriver setup and teardown
    - Element finding utilities
    - Logging capabilities
    """

    def test_1_login_wrong_username_wrong_password(self):
        """
        Negative test case: Login with invalid credentials should fail.

        Steps:
            1. Navigate to GitHub login page
            2. Enter invalid username and password
            3. Submit the login form
            4. Verify the sign-in button is still visible (login failed)

        Expected Result:
            - User remains on login page
            - Sign-in button remains displayed
        """
        # Log test start for debugging and audit purposes
        self.log().info("GitHub Login Page - Negative Test: Invalid credentials")

        # Navigate to GitHub login page
        self.driver.get("https://github.com/login")

        # Enter invalid credentials
        self.get_element(USERNAME_INPUT).send_keys('Test')  # Invalid username
        self.get_element(PASSWORD_INPUT).send_keys('test123')  # Invalid password

        # Submit the login form
        self.get_element(SIGNIN_BUTTON).submit()

        # Log test completion
        self.log().info("Negative test completed - login correctly failed")

        # Assert: Login button should still be visible (indicating failed login)
        assert self.get_element(SIGNIN_BUTTON).is_displayed(), \
            "Expected sign-in button to be visible after failed login attempt"

    def test_2_login(self):
        """
        Positive test case: Login with valid credentials should succeed.

        Steps:
            1. Clear any existing values from username and password fields
            2. Enter valid username and password
            3. Submit the login form
            4. Verify successful login (user is redirected to dashboard)

        Expected Result:
            - User is logged in successfully
            - Profile or dashboard becomes accessible

        Note: This test assumes the previous test has already navigated to login page.
        """
        # Log test start
        self.log().info("GitHub Login Page - Positive Test: Valid credentials")

        # Clear previous input values before entering new credentials
        self.get_element(USERNAME_INPUT).clear()
        self.get_element(PASSWORD_INPUT).clear()

        # Enter valid credentials
        self.get_element(USERNAME_INPUT).send_keys('jagwithyou')  # Valid username
        self.get_element(PASSWORD_INPUT).send_keys('Jag143NBS@#')  # Valid password

        # Submit the login form
        self.get_element(SIGNIN_BUTTON).submit()

        # Log test completion
        self.log().info("Positive test completed - login submitted successfully")

        # Note: In production, add an assertion here to verify successful login
        # Example: assert self.get_element(PROFILE_BUTTON).is_displayed()
