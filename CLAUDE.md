# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python-based UI automation testing framework using **Pytest** and **Selenium WebDriver**. It follows a modular design pattern with page locators, base classes, and test classes.

## Common Commands

### Run Tests
```bash
# Run all tests (default: Chrome browser)
pytest

# Run with specific browser
pytest --browser_name firefox
pytest --browser_name chrome

# Run in headless mode (no browser window visible)
pytest --headless

# Combine options: Firefox in headless mode
pytest --browser_name firefox --headless

# Run a single test file
pytest tests/test_google_search_page.py

# Run a specific test class
pytest tests/test_github_login.py::TestGithubPage

# Run a specific test method
pytest tests/test_github_login.py::TestGithubPage::test_1_login_wrong_username_wrong_password

# Run with verbose output
pytest -v
```

### Virtual Environment (Windows)
```bash
python -m venv ENVIRONMENT_NAME
ENVIRONMENT_NAME\scripts\activate
pip install -r requirements.txt
```

## Architecture

### Test Structure Pattern
Tests follow a layered architecture:

1. **Locator Layer** (`locator/`): Defines page elements using Selenium's `By` strategy
   - Example: `SEARCH_BAR = (By.NAME, "q")`

2. **Base Class** (`tests/__init__.py`): `BaseClass` provides common utilities
   - `get_element(locator)`: Returns element with explicit wait
   - `log()`: Returns configured logger instance
   - `verifyLinkPresence(text)`: Wait for link text presence
   - `selectOptionByText(locator, text)`: Select dropdown option

3. **Test Layer** (`tests/`): Test classes inherit from `BaseClass`
   - Use `@pytest.mark.usefixtures("setup")` decorator
   - Access driver via `self.driver`
   - Test methods must start with `test_`

### Configuration System
- **`config.py`**: Central configuration file
  - `BASE_URL`: Starting URL for tests
  - `DRIVER_PATH`: Location of WebDriver executables
  - `WEB_DRIVER_WAIT`: Global wait timeout (60s default)
  - `HEADLESS`: Run browser in headless mode
  - `ACTION_DELAY`: Delay between actions (2s default)
  - `REPORT_FOLDER` / `LOG_FOLDER`: Output directories

### Fixture Setup (`conftest.py`)
- **`setup` fixture (class scope)**: Initializes browser driver
  - Supports Chrome, Firefox, IE via `--browser_name` option
  - Chrome configured with download preferences
  - Driver available as `request.cls.driver`
  - Automatically closes after test class

### Reporting & Logging
- HTML reports generated automatically via `pytest-html` plugin
- Screenshots captured on test failure and embedded in reports
- Individual reports can be enabled via `config.INDIVIDUAL_REPORT = True`
- Logs written to `src/logs/logfile.log`

## File Organization

```
locator/               # Page element locators (By.XPATH, By.ID, etc.)
  ├── github_login_page_locator.py
  └── google_homepage_locator.py

tests/                 # Test classes (inherit from BaseClass)
  ├── __init__.py      # BaseClass with utilities
  ├── test_github_login.py
  └── test_google_search_page.py

src/
  ├── drivers/         # WebDriver executables (chromedriver.exe, geckodriver.exe)
  ├── logs/            # Execution logs
  ├── reports/         # HTML test reports
  └── media/download/  # Download directory

config.py              # Framework configuration
conftest.py            # Pytest fixtures and hooks
pytest.ini             # Pytest settings
```

## Writing New Tests

1. **Create locators** in `locator/<page_name>_locator.py`:
```python
from selenium.webdriver.common.by import By
ELEMENT_NAME = (By.XPATH, "//button[@id='submit']")
```

2. **Create test class** in `tests/test_<feature>.py`:
```python
from tests import BaseClass
from locator.<page_name>_locator import *

class TestFeatureName(BaseClass):
    def test_1_scenario(self):
        self.log().info("Test started")
        self.get_element(ELEMENT_NAME).click()
        assert True
```

## Important Notes

- **Driver Management**: Selenium 4+ automatically downloads and manages ChromeDriver/GeckoDriver. Manual setup in `src/drivers/` is optional.
- **BASE_URL** in `config.py` is the initial URL; tests can navigate elsewhere via `self.driver.get(url)`
- **Test order**: Methods execute alphabetically; use `test_1_`, `test_2_` prefixes to control order
- **Headless mode**: Use `--headless` flag or set `HEADLESS = True` in `config.py`. Command-line flag takes precedence.
- **Screenshots on failure**: Automatically captured and embedded in HTML reports
