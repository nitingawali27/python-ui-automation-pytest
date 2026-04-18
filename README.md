# Automation Testing with Python

A beginner-friendly Python automation testing framework using **Pytest** and **Selenium WebDriver**. This framework makes it easy to write and maintain UI tests for web applications with automatic driver management, HTML reports, and comprehensive logging.

## Features

- **Modular Design**: Separate locators, tests, and utilities for maintainability
- **Cross-Browser Support**: Run tests on Chrome, Firefox, or IE
- **Automatic Driver Management**: Selenium 4+ automatically downloads compatible drivers
- **HTML Reports**: Automatic test reports with screenshots on failure
- **Logging**: Detailed execution logs with timestamps
- **Easy Configuration**: Centralized settings in `config.py`

---

## Prerequisites

Before you begin, ensure you have:

- **Python 3.7+** installed ([Download Python](https://www.python.org/downloads/))
- **Chrome** or **Firefox** browser installed
- **Git** for cloning the repository
- Basic knowledge of Python

---

## Quick Start Guide

### Step 1: Clone the Repository

```bash
git clone https://github.com/jagwithyou/automation-testing-python-selenium.git
cd automation-testing-python-selenium
```

### Step 2: Set Up Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\scripts\activate

# Activate virtual environment (Mac/Linux)
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install pytest selenium pytest-html
```

This installs:
- `pytest` - Testing framework
- `selenium` - WebDriver for browser automation (4.x with automatic driver management)
- `pytest-html` - HTML report generation

### Step 4: Run Tests

```bash
# Run all tests (default browser: Chrome)
pytest

# Run with Firefox
pytest --browser_name firefox

# Run in headless mode (no browser window visible)
pytest --headless

# Combine options: Firefox in headless mode
pytest --browser_name firefox --headless

# Run specific test file
pytest tests/test_google_search_page.py

# Run with verbose output
pytest -v
```

### Step 5: View Results

- **HTML Report**: Open `src/reports/report.html` in your browser
- **Logs**: Check `src/logs/logfile.log`
- **Screenshots**: Available in `src/reports/tests/` (captured on test failure)

---

## Project Structure

```
automation-testing-python-selenium/
│
├── config.py                    # Framework configuration
├── conftest.py                  # Pytest fixtures and hooks
├── pytest.ini                   # Pytest settings
├── requirements.txt             # Python dependencies (see note below)
├── CLAUDE.md                    # Guide for Claude Code AI assistant
│
├── locator/                     # Page element locators
│   ├── __init__.py
│   ├── github_login_page_locator.py
│   └── google_homepage_locator.py
│
├── src/                         # Framework resources
│   ├── drivers/                 # WebDriver executables (optional, auto-managed)
│   ├── logs/                    # Execution logs
│   ├── media/download/          # Downloaded files
│   └── reports/                 # Test reports
│
└── tests/                       # Test cases
    ├── __init__.py              # BaseClass with utilities
    ├── test_github_login.py
    └── test_google_search_page.py
```

**Note on `requirements.txt`**: The original requirements.txt contains pinned versions that may be incompatible with newer Python versions. Use `pip install pytest selenium pytest-html` instead for the latest compatible versions.

---

## How to Write a New Test

Follow these steps to add a new test to the framework:

### Step 1: Create Locators (if testing a new page)

Create a new file in `locator/` (e.g., `locator/my_page_locator.py`):

```python
from selenium.webdriver.common.by import By

# Define elements on the page
USERNAME_FIELD = (By.NAME, "username")
PASSWORD_FIELD = (By.ID, "password")
LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
```

### Step 2: Create Test File

Create a new file in `tests/` (e.g., `tests/test_my_feature.py`):

```python
from tests import BaseClass
from locator.my_page_locator import *

class TestMyFeature(BaseClass):
    """Test suite for my feature."""

    def test_1_login_success(self):
        """Test that user can log in with valid credentials."""
        # Log test start
        self.log().info("Starting login test")

        # Navigate to the page (if not using BASE_URL)
        self.driver.get("https://example.com/login")

        # Enter username
        self.get_element(USERNAME_FIELD).send_keys("my_username")

        # Enter password
        self.get_element(PASSWORD_FIELD).send_keys("my_password")

        # Click login button
        self.get_element(LOGIN_BUTTON).click()

        # Assert expected result
        assert "dashboard" in self.driver.current_url

        self.log().info("Login test passed")
```

### Step 3: Run Your Test

```bash
# Run your specific test file
pytest tests/test_my_feature.py -v
```

---

## Configuration Guide

Edit `config.py` to customize framework behavior:

| Setting | Description | Default |
|---------|-------------|---------|
| `BASE_URL` | Starting URL for tests | `"https://www.google.com/"` |
| `WEB_DRIVER_WAIT` | Maximum wait time for elements (seconds) | `60` |
| `HEADLESS` | Run browser without visible window | `False` |
| `ACTION_DELAY` | Delay between actions (seconds) | `2` |
| `INDIVIDUAL_REPORT` | Create timestamped report folders | `False` |
| `REPORT_TITLE` | Title in HTML report | `"Orange HRM Testing"` |

---

## Common Tasks

### Run a Single Test
```bash
pytest tests/test_github_login.py::TestGithubPage::test_1_login_wrong_username_wrong_password -v
```

### Run Tests in Headless Mode

**Option 1: Command-line flag (Recommended)**
```bash
pytest --headless
```

**Option 2: Configuration file**
1. Edit `config.py`
2. Set `HEADLESS = True`
3. Run `pytest`

**Note**: The command-line flag `--headless` takes precedence over the config file setting.

### Debug a Failing Test
1. Check the HTML report: `src/reports/report.html`
2. View the screenshot in `src/reports/tests/`
3. Read the log file: `src/logs/logfile.log`

### Change the Starting URL
Edit `config.py` and modify `BASE_URL`:
```python
BASE_URL = "https://your-website.com/"
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `SessionNotCreatedException` | Selenium 4+ automatically manages drivers. If issues persist, update selenium: `pip install -U selenium` |
| Tests fail with "element not found" | Increase `WEB_DRIVER_WAIT` in `config.py` |
| Tests are flaky | Increase `ACTION_DELAY` in `config.py` |
| Reports not generating | Check that `src/reports/` folder exists and is writable |
| `FileNotFoundError` for logs folder | The framework auto-creates the logs folder. If issue persists, create manually: `mkdir src/logs` |

---

## Contributing

We welcome contributions! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please give this repository a star if you find it helpful!

---

## License

This project is open source. Feel free to use, modify, and distribute.

---

## Support

If you encounter issues:
1. Check the [Troubleshooting](#troubleshooting) section
2. Review the logs in `src/logs/logfile.log`
3. Create an issue in the GitHub repository

Happy Testing!
