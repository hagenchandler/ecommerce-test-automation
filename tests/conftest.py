"""Pytest fixtures and configuration for both Selenium and Playwright."""
import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page
from utils.config import config
from utils.helpers import take_screenshot
from utils.driver_factory import DriverFactory

# Selenium imports
from pages.selenium.login_page import LoginPage as SeleniumLoginPage
from pages.selenium.products_page import ProductsPage as SeleniumProductsPage
from pages.selenium.cart_page import CartPage as SeleniumCartPage

# Playwright imports
from pages.playwright.login_page import LoginPage as PlaywrightLoginPage
from pages.playwright.products_page import ProductsPage as PlaywrightProductsPage
from pages.playwright.cart_page import CartPage as PlaywrightCartPage

# ========== SELENIUM FIXTURES ==========

@pytest.fixture(scope="function")
def selenium_driver(request):
    """Create Selenium WebDriver instance for each test."""
    # Get browser from command line option, default to config value
    browser = request.config.getoption("--selenium-browser", default=None)
    if browser is None:
        browser = config.SELENIUM_BROWSER  # This should be "firefox"
    
    driver = DriverFactory.get_driver(browser=browser)
    yield driver
    driver.quit()

@pytest.fixture
def selenium_login_page(selenium_driver):
    """Create Selenium LoginPage instance."""
    return SeleniumLoginPage(selenium_driver)

@pytest.fixture
def selenium_products_page(selenium_driver):
    """Create Selenium ProductsPage instance."""
    return SeleniumProductsPage(selenium_driver)

@pytest.fixture
def selenium_cart_page(selenium_driver):
    """Create Selenium CartPage instance."""
    return SeleniumCartPage(selenium_driver)

@pytest.fixture
def selenium_authenticated(selenium_driver):
    """Provide an authenticated Selenium session."""
    login_page = SeleniumLoginPage(selenium_driver)
    login_page.navigate()
    login_page.login(config.VALID_USER, config.PASSWORD)
    return selenium_driver

# ========== PLAYWRIGHT FIXTURES ==========

@pytest.fixture(scope="session")
def playwright_browser():
    """Create Playwright browser instance for test session."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=config.HEADLESS)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def playwright_context(playwright_browser: Browser):
    """Create new Playwright browser context for each test."""
    context = playwright_browser.new_context(
        viewport=config.VIEWPORT,
        record_video_dir="videos/" if not config.HEADLESS else None
    )
    yield context
    context.close()

@pytest.fixture(scope="function")
def playwright_page(playwright_context: BrowserContext):
    """Create new Playwright page for each test."""
    page = playwright_context.new_page()
    yield page
    page.close()

@pytest.fixture
def playwright_login_page(playwright_page: Page):
    """Create Playwright LoginPage instance."""
    return PlaywrightLoginPage(playwright_page)

@pytest.fixture
def playwright_products_page(playwright_page: Page):
    """Create Playwright ProductsPage instance."""
    return PlaywrightProductsPage(playwright_page)

@pytest.fixture
def playwright_cart_page(playwright_page: Page):
    """Create Playwright CartPage instance."""
    return PlaywrightCartPage(playwright_page)

@pytest.fixture
def playwright_authenticated(playwright_page: Page):
    """Provide an authenticated Playwright session."""
    login_page = PlaywrightLoginPage(playwright_page)
    login_page.navigate()
    login_page.login(config.VALID_USER, config.PASSWORD)
    return playwright_page

# ========== SCREENSHOT ON FAILURE ==========

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Take screenshot on test failure."""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        # Check if test uses Selenium
        if "selenium_driver" in item.funcargs:
            driver = item.funcargs["selenium_driver"]
            take_screenshot(driver, item.name, "selenium")
        
        # Check if test uses Playwright
        if "playwright_page" in item.funcargs:
            page = item.funcargs["playwright_page"]
            take_screenshot(page, item.name, "playwright")

# ========== COMMAND LINE OPTIONS ==========

def pytest_addoption(parser):
    """Add custom command line options."""
    parser.addoption(
        "--selenium-browser",
        action="store",
        default="chrome",
        help="Browser to use for Selenium tests: chrome, firefox, edge"
    )
