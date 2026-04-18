"""
Pytest Configuration and Fixtures

This file contains pytest hooks, fixtures, and configuration.
It automatically sets up the browser before tests and generates HTML reports.

Key Features:
- Browser initialization fixture (Chrome, Firefox, IE support)
- Automatic screenshot capture on test failure
- HTML report generation with custom formatting
- Command-line option for browser selection
"""

import pytest
from selenium import webdriver
import time
import config
from datetime import datetime
from pathlib import Path
import os

# Import for HTML report customization (must be imported before use)
try:
    from py.xml import html
except ImportError:
    html = None

# Global variable to hold the WebDriver instance across functions
driver = None


def pytest_addoption(parser):
    """
    Add a custom command-line option for selecting the browser.

    Usage:
        pytest --browser_name chrome      # Run tests in Chrome (default)
        pytest --browser_name firefox     # Run tests in Firefox
    """
    parser.addoption(
        "--browser_name", action="store", default="chrome",
        help="Browser to run tests in: chrome, firefox, or IE"
    )


@pytest.fixture(scope="class")
def setup(request):
    """
    Fixture to set up and tear down the browser for each test class.

    This fixture:
    1. Reads the browser_name from command-line options
    2. Initializes the appropriate WebDriver
    3. Opens the BASE_URL
    4. Maximizes the browser window
    5. Provides the driver to test classes via request.cls.driver
    6. Closes the browser after all tests in the class complete

    The fixture has 'class' scope, meaning it runs once before all tests
    in a class and tears down after all tests complete.

    Usage:
        @pytest.mark.usefixtures("setup")
        class TestMyFeature(BaseClass):
            def test_example(self):
                self.driver.find_element(...)  # Access driver via self.driver
    """
    global driver

    # Get the browser name from command-line argument (default: chrome)
    browser_name = request.config.getoption("browser_name")

    # Initialize the appropriate WebDriver based on browser choice
    if browser_name == "chrome":
        # Configure Chrome options for downloads and headless mode
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": config.DOWNLOAD_FOLDER,
            "download.prompt_for_download": False,  # Don't ask for download location
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })

        # Add headless mode if configured
        if config.HEADLESS:
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')

        # Start Chrome - Selenium 4+ automatically manages ChromeDriver
        print("==================== Launching Chrome Browser")
        driver = webdriver.Chrome(options=chrome_options)

    elif browser_name == "firefox":
        # Start Firefox - Selenium 4+ automatically manages geckodriver
        print("==================== Launching Firefox Browser")
        driver = webdriver.Firefox()

    elif browser_name == "IE":
        print("IE driver support is available but requires additional configuration")
        raise NotImplementedError("IE browser support not yet implemented")

    else:
        raise ValueError(f"Unsupported browser: {browser_name}. Use 'chrome' or 'firefox'")

    # Open the starting URL and maximize the window
    driver.get(config.BASE_URL)
    driver.maximize_window()

    # Make the driver available to test classes
    request.cls.driver = driver

    # Yield control to the tests
    yield

    # Cleanup: Close the browser after all tests in the class complete
    driver.close()


# Global variable to track the report directory
reports_dir = None


def create_report_folder():
    """
    Create the report folder for HTML test reports.

    If INDIVIDUAL_REPORT is True, creates a timestamped folder.
    If INDIVIDUAL_REPORT is False, uses the single reports folder.
    """
    global reports_dir

    if config.INDIVIDUAL_REPORT:
        # Create a unique folder with timestamp for this test run
        reports_dir = Path(config.REPORT_FOLDER, datetime.now().strftime('%y-%m-%d-%H-%M-%S'))
        reports_dir.mkdir(parents=True, exist_ok=True)
    else:
        # Use a single report folder, create if it doesn't exist
        reports_dir = Path(config.REPORT_FOLDER)
        if not os.path.exists(reports_dir):
            reports_dir.mkdir(parents=True, exist_ok=False)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """
    Pytest hook to configure report generation.

    This runs before test collection and sets up the HTML report path.
    """
    # Create the report directory
    create_report_folder()

    # Set the HTML report file path
    report = reports_dir / "report.html"

    # Configure pytest-html plugin options
    config.option.htmlpath = report
    config.option.self_contained_html = True  # Embed all resources in single file


def pytest_html_results_table_header(cells):
    """
    Customize the HTML report table header.

    Adds 'Description' and 'Time' columns to the report.
    """
    if html:
        cells.insert(2, html.th('Description'))
        cells.insert(3, html.th('Time', class_='sortable time', col='time'))
        cells.pop()


def pytest_html_results_table_row(report, cells):
    """
    Customize the HTML report table rows.

    Populates the 'Description' and 'Time' columns with data.
    """
    if html:
        cells.insert(2, html.td(getattr(report, 'description', 'No description')))
        cells.insert(3, html.td(datetime.utcnow(), class_='col-time'))
        cells.pop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Pytest hook to capture screenshots on test failure.

    When a test fails or errors, this hook:
    1. Captures a screenshot of the browser
    2. Saves it to the reports folder
    3. Embeds the screenshot in the HTML report
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()

    # Extract the test method's docstring for the description column
    report.description = str(item.function.__doc__ or "No description provided")

    extra = getattr(report, 'extra', [])

    # Capture screenshot if the test failed or had an error
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')

        if (report.skipped and xfail) or (report.failed and not xfail):
            # Generate filename from test node ID
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)

            if file_name:
                # Embed screenshot in HTML report
                html_content = (
                    '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '
                    'onclick="window.open(this.src)" align="right"/></div>' % file_name
                )
                extra.append(pytest_html.extras.html(html_content))

        report.extra = extra


def _capture_screenshot(name):
    """
    Capture a screenshot and save it to the reports directory.

    Args:
        name: Filename for the screenshot
    """
    global reports_dir

    # Create a 'tests' subdirectory for screenshots
    reports_dir = str(Path(reports_dir))
    tests_dir = os.path.join(reports_dir, 'tests')
    if not os.path.exists(tests_dir):
        os.makedirs(tests_dir)

    # Save the screenshot
    try:
        full_path = os.path.join(reports_dir, name)
        driver.get_screenshot_as_file(full_path)
    except Exception as e:
        print(f"Failed to capture screenshot: {e}")


def pytest_html_report_title(report):
    """
    Set the title of the HTML report.
    """
    report.title = config.REPORT_TITLE
