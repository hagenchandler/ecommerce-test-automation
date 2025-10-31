"""Playwright base page with common functionality."""
from playwright.sync_api import Page, expect
from utils.config import config

class BasePage:
    """Base class for all Playwright page objects."""
    
    def __init__(self, page: Page):
        self.page = page
        self.base_url = config.BASE_URL
        
    def navigate_to(self, path: str = ""):
        """Navigate to a specific path."""
        url = f"{self.base_url}{path}"
        self.page.goto(url)
        
    def get_title(self) -> str:
        """Get page title."""
        return self.page.title()
        
    def wait_for_url(self, url_pattern: str, timeout: int = config.PLAYWRIGHT_TIMEOUT):
        """Wait for URL to match pattern."""
        self.page.wait_for_url(url_pattern, timeout=timeout)
        
    def click(self, selector: str):
        """Click an element."""
        self.page.click(selector)
        
    def fill(self, selector: str, value: str):
        """Fill an input field."""
        self.page.fill(selector, value)
        
    def get_text(self, selector: str) -> str:
        """Get text content of an element."""
        return self.page.locator(selector).text_content()
        
    def is_visible(self, selector: str) -> bool:
        """Check if element is visible."""
        return self.page.locator(selector).is_visible()
        
    def wait_for_element(self, selector: str, timeout: int = config.PLAYWRIGHT_TIMEOUT):
        """Wait for element to be visible."""
        self.page.wait_for_selector(selector, timeout=timeout)
