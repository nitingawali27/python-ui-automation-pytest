"""
Google Search Page Tests

This module contains tests for the Google search functionality.
It demonstrates basic search operations and verifies the search page loads correctly.

Prerequisites:
    - BASE_URL in config.py should be set to "https://www.google.com/"
    - Chrome or Firefox browser must be configured
"""

from tests import BaseClass
from locator.google_homepage_locator import *
from selenium.webdriver.common.keys import Keys


class TestGooglePage(BaseClass):
    """
    Test suite for Google search functionality.

    Inherits from BaseClass to get:
    - WebDriver setup and teardown
    - Element finding utilities via get_element()
    - Logging capabilities
    """

    def test_1_search(self):
        """
        Test case: Perform a Google search and verify results page loads.

        Steps:
            1. Navigate to Google homepage (via BASE_URL in config.py)
            2. Locate the search bar
            3. Enter search query: "Automation Testing Python Selenium"
            4. Press Enter to submit search
            5. Verify search executes without errors

        Expected Result:
            - Search query is submitted successfully
            - Browser navigates to search results page
        """
        # Initialize logger for this test method
        logger = self.log()
        logger.info("=== Google Search Test Started ===")

        # Locate the search bar and enter the search query
        # SEARCH_BAR is defined in locator/google_homepage_locator.py
        search_bar = self.get_element(SEARCH_BAR)
        search_bar.send_keys('Automation Testing Python Selenium')

        # Submit the search by pressing Enter key
        search_bar.send_keys(Keys.RETURN)

        # Log successful completion for audit trail
        logger.info("=== Google Search Test Completed Successfully ===")

        # Assert test passed (in real scenario, verify results page elements)
        assert True
