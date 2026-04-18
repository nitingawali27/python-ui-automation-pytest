"""
Locator Package

This package contains locator definitions for all pages in the application.

Each module in this package defines the UI elements for a specific page using
Selenium's By strategy and selector tuples.

Available Locator Modules:
    - github_login_page_locator: Elements for GitHub login page
    - google_homepage_locator: Elements for Google homepage

Adding New Locators:
    1. Create a new file: <page_name>_locator.py
    2. Import By: from selenium.webdriver.common.by import By
    3. Define locators: ELEMENT_NAME = (By.STRATEGY, "selector")
    4. Import in tests: from locator.<page_name>_locator import ELEMENT_NAME
"""
