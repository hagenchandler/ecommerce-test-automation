"""Configuration settings for test automation framework."""
import os
from typing import Dict

class Config:
    """Test configuration class."""
    
    BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    
    # Selenium configuration
    SELENIUM_BROWSER = os.getenv("SELENIUM_BROWSER", "firefox")  # Changed from "chrome"
    SELENIUM_IMPLICIT_WAIT = int(os.getenv("SELENIUM_IMPLICIT_WAIT", "10"))
    SELENIUM_PAGE_LOAD_TIMEOUT = int(os.getenv("SELENIUM_PAGE_LOAD_TIMEOUT", "30"))
    
    # Playwright configuration
    PLAYWRIGHT_BROWSER = os.getenv("PLAYWRIGHT_BROWSER", "chromium")  # chromium, firefox, webkit
    PLAYWRIGHT_TIMEOUT = int(os.getenv("PLAYWRIGHT_TIMEOUT", "30000"))
    
    VIEWPORT: Dict[str, int] = {
        "width": 1920,
        "height": 1080
    }
    
    # Test users from SauceDemo
    VALID_USER = "standard_user"
    LOCKED_USER = "locked_out_user"
    PROBLEM_USER = "problem_user"
    PASSWORD = "secret_sauce"
    
    # Paths
    SCREENSHOTS_DIR = "screenshots"
    REPORTS_DIR = "reports"

config = Config()
