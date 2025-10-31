"""Selenium login page object."""
from selenium.webdriver.common.by import By
from pages.selenium.base_page import BasePage

class LoginPage(BasePage):
    """Login page interactions using Selenium."""
    
    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    def navigate(self):
        """Navigate to login page."""
        self.navigate_to("/")
        
    def login(self, username: str, password: str):
        """Perform login action."""
        self.send_keys(*self.USERNAME_INPUT, username)
        self.send_keys(*self.PASSWORD_INPUT, password)
        self.click(*self.LOGIN_BUTTON)
        
    def get_error_message(self) -> str:
        """Get error message text."""
        return self.get_text(*self.ERROR_MESSAGE)
        
    def is_error_displayed(self) -> bool:
        """Check if error message is displayed."""
        return self.is_visible(*self.ERROR_MESSAGE)
