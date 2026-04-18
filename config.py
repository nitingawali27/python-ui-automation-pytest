import os

# =============================================================================
# FRAMEWORK CONFIGURATION FILE
# =============================================================================
# This file contains all configurable settings for the test framework.
# Modify these values to customize test behavior without changing code.
# =============================================================================


# -----------------------------------------------------------------------------
# PATH CONFIGURATION
# -----------------------------------------------------------------------------
# Base directory of the project (where this config file is located)
BASE_DIRECTORY = os.getcwd()


# -----------------------------------------------------------------------------
# APPLICATION CONFIGURATION
# -----------------------------------------------------------------------------
# Starting URL that the browser will open when tests begin.
# Tests can navigate to other pages using self.driver.get(url) if needed.
BASE_URL = "https://www.google.com/"


# -----------------------------------------------------------------------------
# WEBDRIVER CONFIGURATION
# -----------------------------------------------------------------------------
# Directory containing browser driver executables (chromedriver.exe, geckodriver.exe)
# The framework expects drivers to be in: src/drivers/
DRIVER_PATH = os.path.join(BASE_DIRECTORY, 'src', 'drivers')

# Maximum time (in seconds) to wait for elements to appear on the page
# Increase this if tests fail due to slow page loading
WEB_DRIVER_WAIT = 60

# Run browser in headless mode (no visible window)
# Set to True for CI/CD pipelines or when you don't want the browser window visible
# Set to False to see the browser actions during test execution
HEADLESS = False

# Delay (in seconds) added between actions to allow page elements to stabilize
# Increase if tests are flaky due to fast interactions
ACTION_DELAY = 2


# -----------------------------------------------------------------------------
# DOWNLOAD CONFIGURATION
# -----------------------------------------------------------------------------
# Maximum time (in seconds) to wait for file downloads to complete
DOWNLOAD_WAIT_TIME = 60

# Folder where downloaded files will be saved
# The framework configures Chrome to automatically download to this location
DOWNLOAD_FOLDER = os.path.join(BASE_DIRECTORY, 'src', 'media', 'download')


# -----------------------------------------------------------------------------
# REPORTING CONFIGURATION
# -----------------------------------------------------------------------------
# Title displayed at the top of the HTML test report
REPORT_TITLE = "Orange HRM Testing"

# Folder where HTML test reports will be saved
REPORT_FOLDER = os.path.join(BASE_DIRECTORY, 'src', 'reports')

# Create a new report folder with timestamp for each test run
# Set to True: Each run creates a unique folder (e.g., reports/23-04-18-14-30-00/)
# Set to False: Overwrites the previous report in reports/report.html
INDIVIDUAL_REPORT = False

# Folder where execution logs will be saved
LOG_FOLDER = os.path.join(BASE_DIRECTORY, 'src', 'logs')
