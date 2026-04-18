"""
Base Test Class and Utilities

This module provides the BaseClass that all test classes should inherit from.
It includes common utilities for element interaction, logging, and waiting.

Usage:
    from tests import BaseClass

    class TestMyFeature(BaseClass):
        def test_example(self):
            element = self.get_element(LOGIN_BUTTON)
            element.click()
"""

import inspect
import logging
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import config
import pytest
import time


@pytest.mark.usefixtures("setup")
class BaseClass:
    """
    Base class for all test classes.

    This class provides:
    - Automatic browser setup via the 'setup' fixture from conftest.py
    - Element finding with explicit waits
    - Logging capabilities
    - Dropdown selection utilities

    All test classes should inherit from BaseClass:
        class TestLogin(BaseClass):
            def test_login(self):
                ...
    """

    def log(self):
        """
        Get a configured logger instance for the calling test method.

        Each test method gets its own logger named after the method.
        Logs are written to the file specified in config.LOG_FOLDER.

        Returns:
            logging.Logger: Configured logger instance

        Usage:
            logger = self.log()
            logger.info("Starting login test")
            logger.error("Login failed")
        """
        # Get the name of the calling method (the test function)
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        # Create log folder if it doesn't exist
        os.makedirs(config.LOG_FOLDER, exist_ok=True)

        # Configure file handler for logging
        log_file_path = os.path.join(config.LOG_FOLDER, 'logfile.log')
        file_handler = logging.FileHandler(log_file_path)

        # Set log format: timestamp | log level | logger name | message
        formatter = logging.Formatter(
            "%(asctime)s :%(levelname)s : %(name)s :%(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Set minimum log level to DEBUG (captures all messages)
        logger.setLevel(logging.DEBUG)

        return logger

    def verify_link_presence(self, text):
        """
        Wait for a link with the given text to appear on the page.

        Args:
            text: The link text to wait for

        Raises:
            TimeoutException: If the link is not found within 10 seconds

        Usage:
            self.verify_link_presence("Click here")
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text))
        )
        return element

    def select_option_by_text(self, locator, text):
        """
        Select an option from a dropdown by its visible text.

        Args:
            locator: Tuple (By.STRATEGY, "value") identifying the dropdown
            text: The visible text of the option to select

        Usage:
            self.select_option_by_text(COUNTRY_DROPDOWN, "United States")
        """
        element = self.get_element(locator)
        select = Select(element)
        select.select_by_visible_text(text)

    def get_element(self, locator):
        """
        Find an element on the page using explicit wait.

        This method waits for the element to be present on the page
        before returning it. It also adds a configurable delay between
        actions to ensure page stability.

        Args:
            locator: Tuple in format (By.STRATEGY, "value")
                    Example: (By.NAME, "username")
                             (By.XPATH, "//button[@id='submit']")
                             (By.ID, "login-btn")

        Returns:
            WebElement: The located element ready for interaction

        Raises:
            TimeoutException: If element not found within WEB_DRIVER_WAIT seconds

        Usage:
            username_field = self.get_element((By.NAME, "username"))
            username_field.send_keys("john_doe")
        """
        # Add delay between actions for page stability
        time.sleep(config.ACTION_DELAY)

        # Wait for element to be present and return it
        element = WebDriverWait(self.driver, config.WEB_DRIVER_WAIT).until(
            EC.presence_of_element_located(locator)
        )
        return element
