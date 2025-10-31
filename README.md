# E-Commerce Test Automation Framework

A comprehensive test automation framework demonstrating UI testing capabilities with both Selenium WebDriver and Playwright, featuring 28 automated test cases with 100% pass rate.

## Project Overview

This framework automates end-to-end testing for [SauceDemo](https://www.saucedemo.com/), a demo e-commerce application, showcasing professional QA automation practices including:

- **Dual Framework Support**: Both Selenium WebDriver and Playwright implementations
- **Page Object Model**: Maintainable and scalable test architecture
- **28 Automated Tests**: Login, shopping cart, checkout, and validation scenarios
- **Performance Comparison**: Benchmarking between Selenium and Playwright
- **CI/CD Ready**: GitHub Actions configuration for automated testing
- **Comprehensive Reporting**: HTML reports with screenshots on failure

## Tech Stack

| Category | Technologies |
|----------|-------------|
| **Language** | Python 3.9+ |
| **Test Frameworks** | Selenium WebDriver 4.15, Playwright 1.40 |
| **Test Runner** | Pytest 7.4 |
| **Browsers** | Firefox (Selenium), Chromium (Playwright) |
| **Reporting** | pytest-html, Screenshots on Failure |
| **CI/CD** | GitHub Actions |
| **Design Pattern** | Page Object Model (POM) |

## Prerequisites

- Python 3.9 or higher
- Firefox browser (for Selenium tests)
- Git

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/hagenchandler/ecommerce-test-automation.git
cd ecommerce-test-automation
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Install Python packages
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

### 4. Run Tests

```bash
# Run all tests (28 tests - Selenium + Playwright + Comparison)
pytest --selenium-browser firefox --html=reports/report.html --self-contained-html -v

# View the HTML report
firefox reports/report.html  # On Linux
open reports/report.html     # On macOS
start reports/report.html    # On Windows
```

## Project Structure

```
ecommerce-test-automation/
├── .github/
│   └── workflows/
│       └── test.yml              # CI/CD pipeline configuration
├── pages/
│   ├── selenium/                 # Selenium page objects
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── products_page.py
│   │   └── cart_page.py
│   └── playwright/               # Playwright page objects
│       ├── base_page.py
│       ├── login_page.py
│       ├── products_page.py
│       └── cart_page.py
├── tests/
│   ├── ui_selenium/              # Selenium test suites
│   │   ├── test_login.py         # Login functionality tests
│   │   ├── test_products.py      # Product page tests
│   │   └── test_checkout.py      # Checkout flow tests
│   ├── ui_playwright/            # Playwright test suites
│   │   ├── test_login.py
│   │   ├── test_products.py
│   │   └── test_checkout.py
│   ├── comparison/               # Performance comparison tests
│   │   └── test_performance_comparison.py
│   └── conftest.py               # Pytest fixtures and configuration
├── utils/
│   ├── config.py                 # Test configuration
│   ├── helpers.py                # Utility functions
│   └── driver_factory.py         # Selenium WebDriver factory
├── reports/                       # Generated test reports
├── screenshots/                  # Failure screenshots
├── requirements.txt              # Python dependencies
├── pytest.ini                    # Pytest configuration
└── README.md
```

## Test Coverage

### Functional Test Cases (24 tests)

#### Login Tests (8 tests)
- Successful login with valid credentials
- Login failure with invalid username
- Login failure with invalid password
- Login failure with empty credentials
- Locked out user validation

#### Product Tests (8 tests)
- Product catalog display validation
- Add single item to cart
- Add multiple items to cart
- Remove items from cart
- Product sorting functionality

#### Checkout Tests (8 tests)
- Cart page displays added items
- Remove items from cart page
- Continue shopping functionality
- Checkout flow validation

### Performance Comparison Tests (4 tests)
- Login time comparison (Selenium vs Playwright)
- Cart operations performance benchmarking
- Results: Playwright executes ~60% faster than Selenium

## 🎮 Running Tests

### Run All Tests
```bash
# All 28 tests with HTML report
pytest --selenium-browser firefox --html=reports/report.html --self-contained-html -v
```

### Run Specific Test Suites
```bash
# Only Selenium tests (12 tests)
pytest -m selenium --selenium-browser firefox -v

# Only Playwright tests (12 tests)
pytest -m playwright -v

# Only smoke tests (critical path tests)
pytest -m smoke --selenium-browser firefox -v

# Performance comparison tests
pytest -m comparison --selenium-browser firefox -v -s
```

### Run with Parallel Execution
```bash
# Run tests across 4 workers (faster execution)
pytest -n 4 --selenium-browser firefox -v
```

### Run Specific Test Files
```bash
# Run login tests only
pytest tests/ui_selenium/test_login.py --selenium-browser firefox -v

# Run Playwright checkout tests
pytest tests/ui_playwright/test_checkout.py -v
```

### Cross-Browser Testing (Selenium)
```bash
# Firefox (default)
pytest -m selenium --selenium-browser firefox -v

# Chrome (requires Chrome installed)
pytest -m selenium --selenium-browser chrome -v

# Edge (requires Edge installed)
pytest -m selenium --selenium-browser edge -v
```

## Test Reports

After running tests, view the generated HTML report:

```bash
# The report is generated at:
reports/report.html

# Open it in your browser:
firefox reports/report.html  # Linux
open reports/report.html     # macOS
start reports/report.html    # Windows
```

The report includes:
- Test execution summary
- Pass/Fail status for each test
- Execution time for each test
- Screenshots for failed tests
- Test environment details

## Design Patterns & Best Practices

### Page Object Model (POM)
All page interactions are encapsulated in page classes, making tests maintainable and reusable:

```python
# Example: Selenium Login Page
class LoginPage(BasePage):
    def login(self, username, password):
        self.send_keys(By.ID, "user-name", username)
        self.send_keys(By.ID, "password", password)
        self.click(By.ID, "login-button")
```

### Pytest Fixtures
Centralized setup and teardown for test execution:

```python
@pytest.fixture
def selenium_driver(request):
    """Create Selenium WebDriver instance."""
    browser = request.config.getoption("--selenium-browser")
    driver = DriverFactory.get_driver(browser=browser)
    yield driver
    driver.quit()
```

### Automatic Screenshots on Failure
Failed tests automatically capture screenshots for debugging:

```python
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    if report.failed:
        take_screenshot(driver, item.name)
```

## Configuration

Test configuration is centralized in `utils/config.py`:

```python
# Browser settings
SELENIUM_BROWSER = "firefox"  # chrome, firefox, edge
PLAYWRIGHT_BROWSER = "chromium"  # chromium, firefox, webkit

# Test settings
HEADLESS = True  # Run browsers in headless mode
TIMEOUT = 30000  # Page load timeout (ms)
IMPLICIT_WAIT = 10  # Implicit wait (seconds)
```

## CI/CD Integration

This project includes a complete GitHub Actions workflow (`.github/workflows/test.yml`) that:

1. Runs on every push and pull request
2. Tests across Python 3.9, 3.10, and 3.11
3. Executes both Selenium and Playwright tests
4. Tests across multiple browsers
5. Generates and uploads test reports as artifacts
6. Runs daily smoke tests automatically

## Performance Benchmarks

Based on performance comparison tests:

| Operation | Selenium (Firefox) | Playwright (Chromium) | Improvement |
|-----------|-------------------|----------------------|-------------|
| Login Flow | ~2.0s | ~1.1s | **45% faster** |
| Cart Operations | ~2.5s | ~0.5s | **80% faster** |

**Key Findings:**
- Playwright demonstrates significantly faster execution times
- Playwright's auto-wait mechanism reduces test flakiness
- Both frameworks provide reliable cross-browser testing

## Troubleshooting

### WebDriver Issues (Selenium)
```bash
# Clear WebDriver cache
rm -rf ~/.wdm

# Reinstall webdriver-manager
pip install --upgrade webdriver-manager
```

### Playwright Installation Issues
```bash
# Reinstall Playwright browsers
playwright install --force

# Install system dependencies (Linux)
playwright install-deps
```

### Python Cache Issues
```bash
# Clear Python cache files
find . -type d -name __pycache__ -exec rm -rf {} +
find . -name "*.pyc" -delete
rm -rf .pytest_cache
```

### Tests Not Found
Make sure you're running pytest from the project root directory where `pytest.ini` is located

## Test Data

This framework uses [SauceDemo](https://www.saucedemo.com/), a demo e-commerce site specifically designed for test automation practice.

**Test Users:**
- Standard User: `standard_user` / `secret_sauce`
- Locked Out User: `locked_out_user` / `secret_sauce`
- Problem User: `problem_user` / `secret_sauce`

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Chandler Hagen**

- Email: chandlerjhagen@gmail.com
- LinkedIn: [linkedin.com/in/chandler-hagen](https://www.linkedin.com/in/chandler-hagen)
- Portfolio: [chandlerhagen.com](https://chandlerhagen.com/)
- GitHub: [@hagenchandler](https://github.com/hagenchandler)

##  Acknowledgments

- [Sauce Labs](https://www.saucedemo.com/) for providing the demo application
- [Selenium](https://www.selenium.dev/) and [Playwright](https://playwright.dev/) communities
- [Pytest](https://pytest.org/) framework maintainers

---
 
## Additional Resources

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Playwright Documentation](https://playwright.dev/python/docs/intro)
- [Pytest Documentation](https://docs.pytest.org/)
- [Page Object Model Pattern](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
