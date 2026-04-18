"""
Google Homepage Locators

This module defines all UI elements (locators) for the Google homepage.
Each locator is a tuple containing the Selenium By strategy and the selector value.

Usage:
    from locator.google_homepage_locator import SEARCH_BAR
    search_bar = self.get_element(SEARCH_BAR)
    search_bar.send_keys("search query")

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
"""

from selenium.webdriver.common.by import By


# -----------------------------------------------------------------------------
# SEARCH ELEMENTS
# -----------------------------------------------------------------------------

# Main search input field on the Google homepage
# Located by the 'name' attribute with value "q"
SEARCH_BAR = (By.NAME, "q")
