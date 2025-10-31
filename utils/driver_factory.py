"""Selenium WebDriver factory for browser initialization."""
from selenium import webdriver
from utils.config import config

class DriverFactory:
    """Factory class for creating WebDriver instances."""
    
    @staticmethod
    def get_driver(browser: str = None, headless: bool = None):
        """Create and return a WebDriver instance.
        
        Args:
            browser: Browser name (chrome, firefox, edge)
            headless: Run in headless mode
            
        Returns:
            WebDriver instance
        """
        browser = browser or config.SELENIUM_BROWSER
        headless = headless if headless is not None else config.HEADLESS
        
        if browser.lower() == "chrome":
            return DriverFactory._get_chrome_driver(headless)
        elif browser.lower() == "firefox":
            return DriverFactory._get_firefox_driver(headless)
        elif browser.lower() == "edge":
            return DriverFactory._get_edge_driver(headless)
        else:
            raise ValueError(f"Unsupported browser: {browser}")
    
    @staticmethod
    def _get_chrome_driver(headless: bool):
        """Create Chrome WebDriver."""
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument(f"--window-size={config.VIEWPORT['width']},{config.VIEWPORT['height']}")
        
        # Selenium 4.6+ has built-in driver management
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(config.SELENIUM_IMPLICIT_WAIT)
        driver.set_page_load_timeout(config.SELENIUM_PAGE_LOAD_TIMEOUT)
        return driver
    
    @staticmethod
    def _get_firefox_driver(headless: bool):
        """Create Firefox WebDriver."""
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument(f"--width={config.VIEWPORT['width']}")
        options.add_argument(f"--height={config.VIEWPORT['height']}")
        
        # Selenium 4.6+ has built-in driver management
        driver = webdriver.Firefox(options=options)
        driver.implicitly_wait(config.SELENIUM_IMPLICIT_WAIT)
        driver.set_page_load_timeout(config.SELENIUM_PAGE_LOAD_TIMEOUT)
        return driver
    
    @staticmethod
    def _get_edge_driver(headless: bool):
        """Create Edge WebDriver."""
        options = webdriver.EdgeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f"--window-size={config.VIEWPORT['width']},{config.VIEWPORT['height']}")
        
        # Selenium 4.6+ has built-in driver management
        driver = webdriver.Edge(options=options)
        driver.implicitly_wait(config.SELENIUM_IMPLICIT_WAIT)
        driver.set_page_load_timeout(config.SELENIUM_PAGE_LOAD_TIMEOUT)
        return driver
