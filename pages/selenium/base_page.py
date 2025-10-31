"""Selenium base page with common functionality."""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.config import config

class BasePage:
    """Base class for all Selenium page objects."""
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = config.BASE_URL
        self.wait = WebDriverWait(driver, 10)
        
    def navigate_to(self, path: str = ""):
        """Navigate to a specific path."""
        url = f"{self.base_url}{path}"
        self.driver.get(url)
        
    def get_title(self) -> str:
        """Get page title."""
        return self.driver.title
        
    def wait_for_url_contains(self, url_fragment: str, timeout: int = 10):
        """Wait for URL to contain specific text."""
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url_fragment)
        )
        
    def click(self, by: By, locator: str):
        """Click an element."""
        element = self.wait.until(EC.element_to_be_clickable((by, locator)))
        element.click()
        
    def send_keys(self, by: By, locator: str, text: str):
        """Send keys to an input field."""
        element = self.wait.until(EC.visibility_of_element_located((by, locator)))
        element.clear()
        element.send_keys(text)
        
    def get_text(self, by: By, locator: str) -> str:
        """Get text content of an element."""
        element = self.wait.until(EC.visibility_of_element_located((by, locator)))
        return element.text
        
    def is_visible(self, by: By, locator: str, timeout: int = 5) -> bool:
        """Check if element is visible."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, locator))
            )
            return True
        except:
            return False
            
    def wait_for_element(self, by: By, locator: str, timeout: int = 10):
        """Wait for element to be visible."""
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, locator))
        )
        
    def find_element(self, by: By, locator: str):
        """Find and return an element."""
        return self.driver.find_element(by, locator)
        
    def find_elements(self, by: By, locator: str):
        """Find and return multiple elements."""
        return self.driver.find_elements(by, locator)
