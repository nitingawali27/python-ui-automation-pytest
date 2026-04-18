"""
GitHub Login Page Locators

This module defines all UI elements (locators) for the GitHub login page.
Each locator is a tuple containing the Selenium By strategy and the selector value.

Usage:
    from locator.github_login_page_locator import USERNAME_INPUT, PASSWORD_INPUT
    element = self.get_element(USERNAME_INPUT)

Note:
    Locators are defined as tuples in the format:
    (By.STRATEGY, "selector_value")

    Available strategies:
    - By.ID: Find by element ID
    - By.NAME: Find by element name attribute
    - By.XPATH: Find by XPath expression
    - By.CSS_SELECTOR: Find by CSS selector
    - By.CLASS_NAME: Find by CSS class
    - By.TAG_NAME: Find by HTML tag
    - By.LINK_TEXT: Find by exact link text
    - By.PARTIAL_LINK_TEXT: Find by partial link text
"""

from selenium.webdriver.common.by import By


# -----------------------------------------------------------------------------
# LOGIN FORM ELEMENTS
# -----------------------------------------------------------------------------

# Username/email input field on the login form
USERNAME_INPUT = (By.NAME, "login")

# Password input field on the login form
PASSWORD_INPUT = (By.NAME, "password")

# Sign-in button to submit the login form
SIGNIN_BUTTON = (By.NAME, "commit")


# -----------------------------------------------------------------------------
# POST-LOGIN ELEMENTS (for verification)
# -----------------------------------------------------------------------------

# Example: Profile button that appears after successful login
# Note: This XPath is a placeholder and should be updated based on actual GitHub UI
PROFILE_BUTTON = (By.XPATH, "//div[text()='Incorrect username ']")
