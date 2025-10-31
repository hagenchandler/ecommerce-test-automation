"""Playwright login page object."""
from pages.playwright.base_page import BasePage

class LoginPage(BasePage):
    """Login page interactions using Playwright."""
    
    # Locators
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"
    
    def navigate(self):
        """Navigate to login page."""
        self.navigate_to("/")
        
    def login(self, username: str, password: str):
        """Perform login action."""
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        
    def get_error_message(self) -> str:
        """Get error message text."""
        return self.get_text(self.ERROR_MESSAGE)
        
    def is_error_displayed(self) -> bool:
        """Check if error message is displayed."""
        return self.is_visible(self.ERROR_MESSAGE)
